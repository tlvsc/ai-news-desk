"""Deterministic synthetic pool for the dry end-to-end test: ~330 items over the 55 registered sources, with
same-event duplicates across sources, a few out-of-window items, fun items and obvious 'critical' items.
Content is nonsense on purpose (house rule 6: never invent real news); it only exercises the code paths.

    python tests/make_fixture.py [--edition 2026-09-27] [--out tests/fixtures/pool_320.jsonl]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import random
import zlib
import sys
import zoneinfo
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import load_json, SOURCES_PATH  # noqa: E402

ACTORS = {"POL": ["the European Commission", "the White House", "Britain's AI Safety Institute", "India's IT ministry", "the Pentagon"],
          "MKT": ["chipmaker Nervo", "cloud company Skyvault", "startup Quillbot Labs", "Orbital Semiconductor", "investment firm Pelican Capital"],
          "SEC": ["security firm Redshield", "researchers at Tallgrass University", "the cyber agency CERT-Nord", "Bluefin Bank", "vendor Lockstep"],
          "ENE": ["utility Northgrid", "data centre builder Kilnworks", "Solaris Power", "the grid operator Meshline", "Cobalt Energy"],
          "ROB": ["robot maker Ferrous Dynamics", "warehouse firm Cartwell", "drone company Skyhook", "Kestrel Robotics", "farm robot startup Sprout"],
          "MOD": ["model lab Halcyon", "the open source group Lattice", "assistant maker Pendant", "Vertex Labs", "toolmaker Quarry"],
          "RES": ["scientists at Meridian Institute", "a team at Coastal University", "the Alder Lab", "researchers at Pinegrove", "the Brightwater Observatory"],
          "LAW": ["a federal court in Ohio", "the Dutch data authority", "authors' group Inkwell", "the competition regulator", "a Tokyo district court"],
          "HEA": ["hospital group Larkspur Health", "the drug agency", "clinic chain Wellmark", "biotech Cellara", "a Boston hospital"],
          "SOC": ["the teachers' union Chalkline", "the city of Bremen", "newspaper The Daily Tide", "a Kenyan school network", "the film guild"],
          "FUN": ["a hobbyist in Leeds", "a cat named Turbo", "a village bakery", "a retired accountant", "a chess club in Lima"]}
DEEDS = {"POL": ["published new rules for AI in elections", "delayed the AI act deadline by six months", "signed an AI safety pact with twelve countries", "ordered agencies to list every AI system they use"],
         "MKT": ["raised three hundred million dollars at a four billion valuation", "reported quarterly AI revenue of two billion dollars", "bought a rival for one point two billion", "cut prices of its AI chips by thirty percent"],
         "SEC": ["found a flaw that lets chatbots leak customer records", "warned that AI written phishing rose eighty percent", "patched an agent that could be hijacked through a web form", "traced a data theft to a poisoned model file"],
         "ENE": ["switched on a two gigawatt data centre campus", "said AI demand will double power use by twenty thirty", "paused a data centre over water limits", "signed a deal for one gigawatt of solar for AI servers"],
         "ROB": ["showed a robot that folds laundry from one demonstration", "put two hundred humanoid robots to work in a car plant", "flew a drone that lands on a moving truck", "sold its first robot that picks strawberries at night"],
         "MOD": ["released a model that runs on a phone and beats last year's best", "opened its agent tool to every developer for free", "added a voice mode that speaks forty languages", "launched a coding assistant that fixes its own bugs"],
         "RES": ["used AI to predict a protein shape in one minute", "trained a model that spots earthquakes ten seconds earlier", "found AI can read ancient scrolls without unrolling them", "showed a model that solves olympiad geometry"],
         "LAW": ["ruled that AI output cannot be copyrighted", "fined a chatbot maker four million euros over data use", "sued a model lab over training on books", "ordered an AI company to delete a voice clone"],
         "HEA": ["approved an AI tool that reads chest scans", "found AI cut missed cancers by twenty percent in a trial", "started using AI to write discharge notes", "paused an AI triage tool after errors"],
         "SOC": ["banned AI homework helpers in exams", "gave every pupil an AI tutor", "found half of students use AI weekly", "warned that AI fake videos spread before a vote"],
         "FUN": ["taught an AI to bark at the mail carrier", "won a bake-off with an AI written recipe", "used a chatbot to name every pigeon in the square", "beat a robot at table tennis after nine tries"]}
CRITICAL = [("MOD", "model lab Halcyon", "released a frontier model that plans a week of work on its own, in a change that affects every office"),
            ("POL", "the White House", "signed an executive order that requires licences for every large AI model"),
            ("SEC", "the cyber agency CERT-Nord", "said an AI worm infected banks in nine countries overnight")]


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--edition", default="2026-09-27")
    p.add_argument("--out", default=str(Path(__file__).parent / "fixtures" / "pool_320.jsonl"))
    p.add_argument("--major", default=str(Path(__file__).parent / "fixtures" / "major_news_list.json"))
    a = p.parse_args()
    rnd = random.Random(20260927)
    edition = dt.date.fromisoformat(a.edition)
    tz = zoneinfo.ZoneInfo("Asia/Jerusalem")
    end = dt.datetime(edition.year, edition.month, edition.day, 9, 0, tzinfo=tz)
    sources = load_json(SOURCES_PATH)["sources"] if isinstance(load_json(SOURCES_PATH), dict) else load_json(SOURCES_PATH)
    rows, events, n = [], [], 0
    by_cat: dict[str, list] = {}
    for s in sources:
        by_cat.setdefault(s.get("category", "MOD"), []).append(s)
    # critical events, each reported by three sources in the category and one elsewhere
    for k, (cat, actor, deed) in enumerate(CRITICAL):
        title = f"{actor[0].upper() + actor[1:]} {deed}"
        events.append({"cat": cat, "title": title, "actor": actor, "deed": deed, "n_sources": 4, "crit": True})
    for cat, srcs in by_cat.items():
        for i in range(9):
            actor = rnd.choice(ACTORS.get(cat, ACTORS["MOD"]))
            deed = rnd.choice(DEEDS.get(cat, DEEDS["MOD"]))
            detail = rnd.choice(["in Berlin", "for hospitals", "after a two year test", "with a rival", "in a court filing", "at its annual event",
                                 "for farmers", "across Asia", "with government money", "despite protests", "for the first time", "in a leaked memo"])
            title = f"{actor[0].upper() + actor[1:]} {deed} {detail} ({cat.lower()} {i})"
            events.append({"cat": cat, "title": title, "actor": actor, "deed": deed, "n_sources": 1 + (1 if i % 3 == 0 else 0) + (1 if i % 5 == 0 else 0), "crit": False})
    for e in events:
        pool = by_cat.get(e["cat"], sources)
        picked = rnd.sample(pool, min(e["n_sources"], len(pool)))
        if e["n_sources"] > len(pool):
            picked += rnd.sample(sources, e["n_sources"] - len(pool))
        for j, src in enumerate(picked):
            n += 1
            hours = rnd.uniform(0.5, 23.5)
            pub = end - dt.timedelta(hours=hours)
            variant = e["title"] if j == 0 else e["title"].replace(" (", ", sources say (") if j == 1 else e["title"].replace(e["actor"][0].upper() + e["actor"][1:], e["actor"][0].upper() + e["actor"][1:] + " has", 1)
            text = (f"{variant}. The announcement came on {pub.strftime('%d %B')} and named {e['actor']} as the actor. "
                    f"Officials said the number involved was {rnd.choice(['two hundred', 'fifty', 'one thousand', 'twelve'])} and that more details follow next week. "
                    f"Critics questioned the timing.")
            rows.append({"source_id": src["id"], "title": variant, "link": f"https://{src['url'].split('/')[2]}/story/{n}-{zlib.crc32(e['title'].encode()) % 100000}",
                         "published": pub.isoformat(), "summary": text[:200], "text": text, "fun": e["cat"] == "FUN"})
    # filler: unique minor items so every source has items and the pool passes 300
    while len(rows) < 330:
        src = rnd.choice(sources)
        cat = src.get("category", "MOD")
        n += 1
        actor = rnd.choice(ACTORS.get(cat, ACTORS["MOD"]))
        deed = rnd.choice(DEEDS.get(cat, DEEDS["MOD"]))
        pub = end - dt.timedelta(hours=rnd.uniform(0.5, 23.5))
        title = f"{actor[0].upper() + actor[1:]} {deed} in a smaller update {n}"
        text = f"{title}. A short note published on {pub.strftime('%d %B')} with a figure of {rnd.randint(2, 90)} percent. It is a minor item."
        rows.append({"source_id": src["id"], "title": title, "link": f"https://{src['url'].split('/')[2]}/note/{n}", "published": pub.isoformat(),
                     "summary": text[:160], "text": text, "fun": cat == "FUN"})
    # out-of-window items
    for i in range(12):
        src = rnd.choice(sources)
        n += 1
        pub = end - dt.timedelta(days=rnd.randint(2, 9))
        rows.append({"source_id": src["id"], "title": f"Old item {n} about AI from last week", "link": f"https://{src['url'].split('/')[2]}/old/{n}",
                     "published": pub.isoformat(), "summary": "old", "text": "Old item, outside the window.", "fun": False})
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    major = [{"title": e["title"], "url": "", "date": edition.isoformat()} for e in events[:3]] + [{"title": events[10]["title"], "url": "", "date": edition.isoformat()}]
    Path(a.major).write_text(json.dumps(major, indent=1), encoding="utf-8")
    print(f"wrote {len(rows)} rows to {out} ({len(events)} events, {sum(1 for r in rows if r['title'].startswith('Old'))} out of window); major list {len(major)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
