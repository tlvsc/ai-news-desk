"""Deterministic stand-ins for every LLM prompt, so the pipeline can be tested end to end with zero tokens.

The output shapes here ARE the contract each stage expects from the real model. Keep them in step with
llm/prompts/*.md. Content is obviously synthetic (marked DRY) and must never reach a real edition.
"""
from __future__ import annotations

import hashlib
import re

CATS = ["Politics and government of AI", "Market, industry and finance", "Security and cyber",
        "Energy and infrastructure", "Robotics", "Models and tools", "Research and science", "Ethics and law",
        "Health", "Society and education", "Fun and humour"]
KEYS = ["POL", "MKT", "SEC", "ENE", "ROB", "MOD", "RES", "LAW", "HEA", "SOC", "FUN"]


def _h(s: str, mod: int) -> int:
    return int(hashlib.md5(s.encode("utf-8")).hexdigest(), 16) % mod


def _sentences(text: str, n: int) -> str:
    parts = [p.strip() for p in re.split(r"(?<=[.!?])\s+", (text or "").strip()) if p.strip()]
    return " ".join(parts[:n]) if parts else "DRY summary."


def answer(prompt_name: str, payload):
    fn = globals().get("p_" + prompt_name)
    if fn is None:
        raise ValueError(f"no dry answer for prompt {prompt_name}")
    return fn(payload)


def p_digest(payload):
    out = []
    for it in payload["items"]:
        text = it.get("text") or it.get("title", "")
        cat = it.get("category_hint") or KEYS[_h(it["id"], len(KEYS))]
        out.append({"id": it["id"], "headline": it.get("title", "")[:140],
                    "summary": _sentences(text, 2)[:400], "key_facts": [_sentences(text, 1)[:160], "DRY fact"],
                    "entities": [w for w in re.findall(r"\b[A-Z][a-zA-Z]{3,}\b", it.get("title", ""))][:4],
                    "event_date": it.get("published", "")[:10], "ai_relevant": True, "fun": cat == "FUN",
                    "category_guess": cat})
    return {"digests": out}


def p_dedupe_pairs(payload):
    def caps(t):
        return set(re.findall(r"\b[A-Z][a-zA-Z]{2,}\b", t or ""))
    return {"pairs": [{"a": p["a"], "b": p["b"],
                       "same_event": p.get("similarity", 0) >= 0.5 and bool(caps(p.get("a_headline", "")) & caps(p.get("b_headline", ""))),
                       "reason": "DRY: similarity plus a shared name"} for p in payload["pairs"]]}


def p_classify(payload):
    out = []
    for ev in payload["events"]:
        key = ev.get("category_guess") or KEYS[_h(ev["id"], len(KEYS))]
        h = _h(ev["id"] + "s", 24)
        score = 10 if h == 0 else 9 if h < 4 else 8 if h < 8 else 7 if h < 14 else 6 if h < 19 else 5  # 10 is rare, as in life
        if ev.get("fun"):
            key, score = "FUN", min(score, 7)
        out.append({"id": ev["id"], "category": key, "subcategory": "DRY topic", "importance": score,
                    "label": "CRITICAL" if score >= 10 else "HIGH" if score >= 8 else "MEDIUM" if score >= 6 else "WATCHLIST",
                    "verification": "REPORTED", "why_it_matters": "DRY reason it matters.",
                    "big_name": _h(ev["id"] + "b", 5) == 0})
    return {"classified": out}


def p_report_story(payload):
    return {"stories": [{"id": ev["id"], "headline": ev["headline"], "importance_reason": "DRY reason and affected parties.",
                         "summary": _sentences(ev.get("summary", ""), 2) or "DRY summary."} for ev in payload["events"]]}


def p_analysis(payload):
    return {"analysis_markdown": "## Forward-looking analysis\n\nDRY analysis placeholder: assumptions, probabilities and "
                                 "scenarios would appear here, derived only from the listed items.\n"}


def p_bulletin_copy(payload):
    return {"items": [{"id": it["id"], "headline": it["headline"].rstrip(".") + ".",
                       "body": "DRY sentence one about what happened. DRY sentence two about why it matters."}
                      for it in payload["items"]]}


def p_meaning_check(payload):
    return {"results": [{"id": it["id"], "result": "PASS", "missing": [], "unsupported": [], "note": "DRY"}
                        for it in payload["items"]]}


def p_bigger_picture(payload):
    return {"head": "DRY: the bigger picture headline.", "card_body": "DRY card body sentence one. DRY sentence two.",
            "items": ["DRY item one (report items 1, 2)", "DRY item two (report items 3)"],
            "spoken": "And for the bigger picture, DRY spoken analysis line that runs roughly forty eight syllables in total for the reel.",
            "full_markdown": "# The Bigger Picture — Daily AI Analysis\n\nDRY analysis body.\n", "report_refs": [1, 2, 3]}


def p_cards_copy(payload):
    out = []
    for it in payload["items"]:
        out.append({"id": it["id"], "head": it["headline"].rstrip(".") + ".",
                    "body": "DRY sentence one says what happened. DRY sentence two says why it matters.",
                    "cat": f"{it.get('category_name', 'Models and tools')} / DRY", "src": (it.get("source") or "SOURCE").upper(),
                    "pill": it.get("verification", "REPORTED")})
    teaser = [{"id": t["id"], "head": t["headline"].rstrip(".") + ".", "cat": t.get("category_name", "")} for t in payload.get("teaser", [])]
    return {"cards": out, "teaser": teaser}


def p_headlines_copy(payload):
    out = []
    for it in payload["items"]:
        intro = {"story": "In the news.", "fun": "And a lighter story.", "teaser": "Also in the full report:",
                 "bigger_picture": "And for the bigger picture:"}.get(it["kind"], "")
        head = it.get("headline") or " and ".join(t["headline"].rstrip(".") for t in it.get("teaser_items", [])[:2]) or "DRY item"
        base = f"{intro} {head.rstrip('.')}. DRY second clause of the spoken line."
        if it.get("fix"):
            base = f"{intro} {head.rstrip('.')[:60]}. DRY rewrite to fit the box."
        if it["kind"] == "bigger_picture":
            base = f"{intro} DRY spoken analysis, money keeps flowing while power delays and debt test the build-out, and the question of who is responsible grows."
        out.append({"id": it["id"], "script": base, "symbol": "a simple glowing icon, simple text-free symbol"})
    return {"items": out}


def p_editorial_qa(payload):
    return {"status": "APPROVED", "checks": [{"name": "facts", "result": "PASS", "note": "DRY"}], "corrections": []}
