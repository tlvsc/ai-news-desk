"""s03_dedupe: cluster pool records into events and give EVERY record a disposition. Code first, model only for
ambiguous pairs (cheap, batched). Nothing disappears silently (18 Sep gate C).

Input:  work/digests.jsonl, history/events_history.jsonl (previous editions)
Output: work/events.jsonl (one per retained event), work/pool_dispositions.jsonl (every raw record)
Dispositions: RETAINED EVENT ID | DUPLICATE OF | PREVIOUSLY COVERED | OUT OF WINDOW | UNVERIFIED | LOW MATERIALITY |
              HELD FOR REVIEW | NOT AI-RELEVANT
"""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import jaccard, log, read_jsonl, stage_main, tokens, write_jsonl  # noqa: E402
from lib.llm_client import LLMClient, batched  # noqa: E402

SAME = 0.55      # at or above: same event, no model needed
MAYBE = 0.30     # between MAYBE and SAME: ask the cheap model
HISTORY = 0.50   # match against previous editions


class UnionFind:
    def __init__(self, ids):
        self.p = {i: i for i in ids}

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[max(ra, rb)] = min(ra, rb)


def run(ctx, extra_args=None) -> int:
    recs = read_jsonl(ctx.work / "digests.jsonl")
    if not recs:
        log.error("no digests.jsonl; run s02 first")
        return 1
    active = [r for r in recs if r.get("disposition") == "PENDING"]
    sig = {r["id"]: tokens((r.get("headline") or r["title"]) + " " + (r.get("summary") or "")) for r in active}
    uf = UnionFind([r["id"] for r in active])
    by_url = {}
    maybe = []
    for r in active:
        by_url.setdefault(r["url_norm"], []).append(r["id"])
    for ids in by_url.values():
        for other in ids[1:]:
            uf.union(ids[0], other)
    ents = {r["id"]: {e.lower() for e in (r.get("entities") or []) if e} for r in active}
    for i, a in enumerate(active):
        for b in active[i + 1:]:
            s = jaccard(sig[a["id"]], sig[b["id"]])
            if s < MAYBE:
                continue
            # two different actors doing the same kind of deed read alike: auto-merge only when an entity is shared;
            # a pair with known, disjoint entities is a different event and never reaches the model (token rule).
            ea, eb = ents[a["id"]], ents[b["id"]]
            shared_actor = not ea or not eb or bool(ea & eb)
            if s >= SAME and shared_actor:
                uf.union(a["id"], b["id"])
            elif shared_actor or s >= SAME:
                maybe.append((a, b, round(s, 2)))
    # ambiguous pairs: cheap model, only when a pair is not already in one cluster
    llm = LLMClient(ctx)
    pairs = sorted((x for x in maybe if uf.find(x[0]["id"]) != uf.find(x[1]["id"])), key=lambda x: -x[2])
    cap = int(ctx.config["llm"].get("max_dedupe_pairs", 240))
    undecided = len(pairs) - cap if len(pairs) > cap else 0
    pairs = pairs[:cap]  # the least similar leftovers stay separate events, recorded below
    size = ctx.config["llm"]["batch_sizes"].get("dedupe_pairs", 60)
    decided = 0
    for batch in batched(pairs, size):
        payload = {"pairs": [{"a": a["id"], "b": b["id"], "similarity": s,
                              "a_headline": a.get("headline") or a["title"], "a_summary": a.get("summary", ""),
                              "b_headline": b.get("headline") or b["title"], "b_summary": b.get("summary", "")}
                             for a, b, s in batch]}
        reply = llm.call("cheap", "dedupe_pairs", payload, stage="s03_dedupe")
        for res in reply.get("pairs", []):
            if res.get("same_event"):
                uf.union(res["a"], res["b"])
                decided += 1
    # clusters -> events
    clusters: dict[str, list[dict]] = {}
    for r in active:
        clusters.setdefault(uf.find(r["id"]), []).append(r)
    history = load_history(ctx)
    hist_sig = [(h, tokens(h.get("headline", "") + " " + h.get("summary", ""))) for h in history]
    events, dispositions = [], {}
    n = 0
    for root, members in clusters.items():
        members.sort(key=lambda m: (m.get("published") or "9999", m["id"]))
        primary = members[0]
        n += 1
        eid = f"EVT-{ctx.edition.strftime('%Y%m%d')}-{n:04d}"
        facts, seen = [], set()
        for m in members:
            for f in m.get("key_facts", []):
                if f and f.lower() not in seen:
                    seen.add(f.lower())
                    facts.append(f)
        merged = tokens((primary.get("headline") or primary["title"]) + " " + (primary.get("summary") or ""))
        prior = max(((jaccard(merged, hs), h) for h, hs in hist_sig), key=lambda x: x[0], default=(0, None))
        ev = {"id": eid, "headline": primary.get("headline") or primary["title"], "summary": primary.get("summary", ""),
              "key_facts": facts[:6], "entities": primary.get("entities", []), "published": primary.get("published"),
              "event_date": primary.get("event_date"), "primary_source": primary["source_name"], "primary_url": primary["url"],
              "sources": sorted({m["source_name"] for m in members}), "member_ids": [m["id"] for m in members],
              "urls": [m["url"] for m in members], "category_guess": primary.get("category_guess"),
              "fun": any(m.get("fun") for m in members), "window_check": primary["window_check"],
              "prior_match": {"score": round(prior[0], 2), "edition": prior[1].get("edition"), "headline": prior[1].get("headline")}
              if prior[1] and prior[0] >= HISTORY else None}
        if ev["prior_match"]:
            ev["disposition"] = "PREVIOUSLY COVERED"
        elif primary["window_check"] == "UNVERIFIED DATE":
            ev["disposition"] = "UNVERIFIED"
        else:
            ev["disposition"] = "RETAINED EVENT ID"
        events.append(ev)
        for i, m in enumerate(members):
            dispositions[m["id"]] = ev["disposition"] if i == 0 else f"DUPLICATE OF {eid}"
            if i == 0:
                dispositions[m["id"]] = f"{ev['disposition']} {eid}" if ev["disposition"] == "RETAINED EVENT ID" else ev["disposition"]
    rows = []
    for r in recs:
        d = dispositions.get(r["id"], r.get("disposition", "HELD FOR REVIEW"))
        rows.append({"id": r["id"], "title": r["title"], "source": r["source_name"], "url": r["url"],
                     "published": r.get("published"), "window_check": r["window_check"], "disposition": d})
    write_jsonl(ctx.work / "events.jsonl", events)
    write_jsonl(ctx.work / "pool_dispositions.jsonl", rows)
    retained = sum(1 for e in events if e["disposition"] == "RETAINED EVENT ID")
    ctx.report_append("s03 dedupe", f"{len(active)} pending records -> {len(events)} events ({retained} retained, "
                                    f"{sum(1 for e in events if e['disposition']=='PREVIOUSLY COVERED')} previously covered, "
                                    f"{sum(1 for e in events if e['disposition']=='UNVERIFIED')} unverified date). "
                                    f"{len(pairs)} ambiguous pairs sent to the cheap model in {-(-len(pairs) // max(1, size))} calls, {decided} merged; "
                                    f"{undecided} less similar pairs kept separate without a call (cap {cap}).")
    ctx.set_stage("s03_dedupe", "done", events=len(events), retained=retained, llm_pairs=len(pairs), undecided_pairs=undecided)
    return 0


def load_history(ctx) -> list[dict]:
    path = ctx.history / "events_history.jsonl"
    days = ctx.config["gates"].get("dedupe_history_days", 30)
    cutoff = (ctx.edition - dt.timedelta(days=days)).isoformat()
    return [h for h in read_jsonl(path) if h.get("edition", "") >= cutoff and h.get("edition") != ctx.edition.isoformat()]


if __name__ == "__main__":
    stage_main(run, __doc__)
