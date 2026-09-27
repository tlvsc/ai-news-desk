"""LLM access for the V1 workflow: Claude Code in headless print mode on Rafael's subscription.

Design (26 Sep 2026 handoff, Model Setup Comparison 25 Sep):
  * Every call is ONE batch over compact records. Raw article text is read once, in s02, and never again.
  * Three tiers: cheap (digest, classify, duplicate pairs), mid (writing copy), strong (analysis, final QA).
  * Every call is logged with tokens and cost to work/llm_log.jsonl so the daily budget is measured, not guessed.
  * Modes: live = run `claude -p`; dry = deterministic placeholders so the whole pipeline can be exercised without
    tokens; manual = write the request to work/llm_requests/ and stop, for a Claude Code session to answer
    with a subagent and drop the reply in work/llm_replies/.
The model receives only the prompt file plus the JSON payload. It gets no tools and one turn.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import time
from pathlib import Path

from .common import PKG_ROOT, log

PROMPTS_DIR = PKG_ROOT / "llm" / "prompts"
SYSTEM_PROMPT = ("You are a precise newsroom assistant for AI News Desk. You receive one instruction file and one JSON "
                 "payload. Follow the instruction file exactly. Reply with JSON only: no prose, no markdown fences, "
                 "no explanations. Never invent a link, date, number, quote or fact that is not in the payload.")


class LLMError(RuntimeError):
    pass


class LLMClient:
    def __init__(self, ctx, mode: str | None = None):
        self.ctx = ctx
        self.cfg = ctx.config.get("llm", {})
        self.mode = mode or ctx.llm_mode or "live"
        self.log_path = ctx.work / "llm_log.jsonl"
        self.req_dir = ctx.work / "llm_requests"
        self.rep_dir = ctx.work / "llm_replies"

    # ------------------------------------------------------------------ public
    def call(self, tier: str, prompt_name: str, payload, *, stage: str, expect: str = "object"):
        """Return parsed JSON (object or list). Raises LLMError after retries."""
        prompt_text = (PROMPTS_DIR / f"{prompt_name}.md").read_text(encoding="utf-8")
        body = prompt_text.rstrip() + "\n\nPAYLOAD (JSON):\n" + json.dumps(payload, ensure_ascii=False)
        key = hashlib.sha256(body.encode("utf-8")).hexdigest()[:16]
        cached = self._cached(key)
        if cached is not None:
            log.info("llm %s/%s: cached reply %s", stage, prompt_name, key)
            return cached
        if self.mode == "dry":
            from . import llm_dry
            reply = llm_dry.answer(prompt_name, payload)
            self._log(stage, prompt_name, tier, "dry", key, {}, 0.0)
            return reply
        if self.mode == "manual":
            self.req_dir.mkdir(parents=True, exist_ok=True)
            req = self.req_dir / f"{stage}_{prompt_name}_{key}.md"
            req.write_text(SYSTEM_PROMPT + "\n\n" + body, encoding="utf-8")
            reply_path = self.rep_dir / f"{stage}_{prompt_name}_{key}.json"
            if reply_path.exists():
                return self._parse(reply_path.read_text(encoding="utf-8"), expect)
            raise LLMError(f"MANUAL MODE: answer the request in {req} with a {tier} subagent and save the JSON reply "
                           f"to {reply_path}, then re-run the stage.")
        return self._live(tier, prompt_name, body, key, stage, expect)

    # ------------------------------------------------------------------ live
    def _live(self, tier, prompt_name, body, key, stage, expect):
        model = self.cfg.get("models", {}).get(tier, tier)
        effort = self.cfg.get("effort", {}).get(tier)
        exe = shutil.which(self.cfg.get("cli", "claude")) or shutil.which("claude.cmd") or self.cfg.get("cli", "claude")
        cmd = [exe, "-p", "--bare", "--model", model, "--output-format", "json", "--max-turns", "1",
               "--system-prompt", SYSTEM_PROMPT, "--disallowedTools", "*"]
        if effort:
            cmd += ["--effort", effort]
        attempts = 1 + int(self.cfg.get("max_retries", 1))
        last_err = None
        for attempt in range(1, attempts + 1):
            t0 = time.time()
            try:
                proc = subprocess.run(cmd, input=body, text=True, capture_output=True,
                                      timeout=int(self.cfg.get("timeout_seconds", 600)), encoding="utf-8")
            except (subprocess.TimeoutExpired, FileNotFoundError) as exc:
                last_err = f"{type(exc).__name__}: {exc}"
                log.warning("llm %s attempt %d failed: %s", prompt_name, attempt, last_err)
                continue
            if proc.returncode != 0:
                last_err = f"exit {proc.returncode}: {proc.stderr[-800:]}"
                log.warning("llm %s attempt %d failed: %s", prompt_name, attempt, last_err)
                continue
            try:
                envelope = json.loads(proc.stdout)
            except json.JSONDecodeError:
                envelope = {"result": proc.stdout}
            usage = envelope.get("usage", {})
            cost = float(envelope.get("total_cost_usd", 0.0) or 0.0)
            text = envelope.get("result", "") if isinstance(envelope, dict) else str(envelope)
            self._log(stage, prompt_name, tier, model, key, usage, cost, seconds=round(time.time() - t0, 1))
            try:
                parsed = self._parse(text, expect)
            except LLMError as exc:
                last_err = str(exc)
                log.warning("llm %s attempt %d: bad JSON (%s)", prompt_name, attempt, last_err[:200])
                body = body + "\n\nYour previous reply was not valid JSON. Reply with the JSON only."
                continue
            self._store(key, parsed)
            return parsed
        raise LLMError(f"{stage}/{prompt_name}: no valid reply after {attempts} attempts: {last_err}")

    # ------------------------------------------------------------------ helpers
    @staticmethod
    def _parse(text: str, expect: str):
        t = text.strip()
        t = re.sub(r"^```(?:json)?\s*|\s*```$", "", t, flags=re.S)
        start = t.find("[") if expect == "list" else t.find("{")
        end = t.rfind("]") if expect == "list" else t.rfind("}")
        if start < 0 or end < 0:
            raise LLMError("no JSON found in reply")
        try:
            return json.loads(t[start:end + 1])
        except json.JSONDecodeError as exc:
            raise LLMError(f"invalid JSON: {exc}") from exc

    def _cache_path(self, key: str) -> Path:
        return self.ctx.work / "llm_cache" / f"{key}.json"

    def _cached(self, key: str):
        p = self._cache_path(key)
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8"))
        return None

    def _store(self, key: str, parsed) -> None:
        p = self._cache_path(key)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(parsed, ensure_ascii=False), encoding="utf-8")

    def _log(self, stage, prompt_name, tier, model, key, usage, cost, seconds=0.0):
        row = {"at": time.strftime("%Y-%m-%dT%H:%M:%S"), "stage": stage, "prompt": prompt_name, "tier": tier,
               "model": model, "key": key, "seconds": seconds, "cost_usd": cost,
               "input_tokens": usage.get("input_tokens"), "output_tokens": usage.get("output_tokens"),
               "cache_read": usage.get("cache_read_input_tokens"), "cache_create": usage.get("cache_creation_input_tokens")}
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        with self.log_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(row) + "\n")

    def summary(self) -> dict:
        rows = []
        if self.log_path.exists():
            rows = [json.loads(l) for l in self.log_path.read_text(encoding="utf-8").splitlines() if l.strip()]
        out = {"calls": len(rows), "cost_usd": round(sum(r.get("cost_usd") or 0 for r in rows), 4),
               "input_tokens": sum(r.get("input_tokens") or 0 for r in rows),
               "output_tokens": sum(r.get("output_tokens") or 0 for r in rows),
               "cache_read": sum(r.get("cache_read") or 0 for r in rows), "by_model": {}}
        for r in rows:
            m = out["by_model"].setdefault(r.get("model"), {"calls": 0, "cost_usd": 0.0})
            m["calls"] += 1
            m["cost_usd"] = round(m["cost_usd"] + (r.get("cost_usd") or 0), 4)
        return out


def batched(items: list, size: int):
    for i in range(0, len(items), max(1, size)):
        yield items[i:i + size]
