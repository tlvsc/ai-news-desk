"""Unit tests, standard library only:  python -m unittest tests.test_units -v"""
from __future__ import annotations

import datetime as dt
import json
import sys
import tempfile
import unittest
from pathlib import Path

PKG = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PKG))
from lib import syllables  # noqa: E402
from lib.common import RunContext, jaccard, load_json, norm_url, reporting_window, short_date, title_date, tokens  # noqa: E402
from stages import s05_gates, s09_cards_select, s13_headlines_fill, s16_stitch  # noqa: E402


def ctx_in(tmp: Path, **over) -> RunContext:
    cfg = load_json(PKG / "config" / "v1_config.json")
    cfg["local_root"] = str(tmp / "runs")
    cfg["history_root"] = str(tmp / "history")
    cfg.update(over)
    c = RunContext(dt.date(2026, 9, 27), cfg, llm_mode="dry")
    c.ensure_dirs()
    return c


class Syllables(unittest.TestCase):
    def test_formula(self):
        self.assertEqual(syllables.box_seconds(35), 7.95)
        self.assertEqual(syllables.box_seconds(37), 8.41)

    def test_known_lines(self):
        # Headlines_25-9-26_selection.md, counted by Rafael's script with its word list
        known = [("China's Xi told Trump the two countries should be partners, not rivals, and must keep AI under human control. He offered no specific rules.", 35),
                 ("Anthropic signed a nearly twelve billion dollar deal to rent computing power from cloud company Akamai, whose shares jumped about twenty percent.", 37),
                 ("Researchers showed that poisoned entries in a web form could hijack Salesforce's AI agents and steal customer data. Salesforce fixed the flaws.", 35),
                 ("Oracle may delay payments on its New Mexico AI data center, as the gas pipeline to power it slipped to twenty twenty-seven.", 36),
                 ("Waymo says its driverless cars, after two hundred seventy million miles, had eighty-two percent fewer injury crashes than humans.", 35)]
        for line, n in known:
            self.assertEqual(syllables.count(line), n, line)

    def test_audit_matches_count(self):
        line = "Anthropic signed a nearly twelve billion dollar deal with cloud company Akamai."
        self.assertEqual(sum(s for _, s in syllables.audit(line)), syllables.count(line))


class Dates(unittest.TestCase):
    def test_names(self):
        self.assertEqual(short_date(dt.date(2026, 9, 26)), "26-9-26")
        self.assertEqual(title_date(dt.date(2026, 9, 11)), "FRI 11 SEP 2026")

    def test_window(self):
        a, b = reporting_window(dt.date(2026, 9, 27), "Asia/Jerusalem", 9)
        self.assertEqual((b - a).total_seconds(), 86400)
        self.assertEqual(b.hour, 9)


class Text(unittest.TestCase):
    def test_norm_url(self):
        self.assertEqual(norm_url("https://www.Example.com/a/b/?utm_source=x&id=3#frag"), "https://example.com/a/b?id=3")

    def test_jaccard(self):
        self.assertGreaterEqual(jaccard(tokens("Halcyon releases frontier model"), tokens("Halcyon has released a frontier model")), 0.5)


class Gates(unittest.TestCase):
    def test_pool_gate_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            ctx = ctx_in(Path(d))
            (ctx.work / "raw_pool.jsonl").write_text("".join(json.dumps({"id": f"R{i}", "window_check": "IN WINDOW"}) + "\n" for i in range(120)), encoding="utf-8")
            (ctx.work / "events.jsonl").write_text(json.dumps({"id": "E1", "disposition": "RETAINED EVENT ID", "headline": "x", "summary": ""}) + "\n", encoding="utf-8")
            cp, _ = s05_gates.compute(ctx, {})
            self.assertEqual(cp["stages"]["pool_gate_min_300"], "FAIL")
            self.assertEqual(cp["stages"]["source_fetch_gate"], "FAIL")
            self.assertEqual(cp["major_news_miss_gate"], "NOT RUN")
            self.assertEqual(s05_gates.run(ctx, []), 2)
            self.assertEqual(s05_gates.run(ctx, ["--override", "pool_gate_min_300=test", "--override", "source_fetch_gate=test", "--override", "major_news_miss_gate=test"]), 0)


def items(n=60):
    cats = ["POL", "MKT", "SEC", "ENE", "ROB", "MOD", "RES", "LAW", "HEA", "SOC", "FUN"]
    names = {"POL": "Politics and government of AI", "MKT": "Market, industry and finance", "SEC": "Security and cyber", "ENE": "Energy and infrastructure",
             "ROB": "Robotics", "MOD": "Models and tools", "RES": "Research and science", "LAW": "Ethics and law", "HEA": "Health",
             "SOC": "Society and education", "FUN": "Fun and humour"}
    out = []
    for i in range(1, n + 1):
        c = cats[i % 11]
        imp = 10 if i in (1, 2, 3) else 9 if i < 20 else 7 if i < 45 else 4
        if i in (1, 2):
            c = "MKT"
        out.append({"n": i, "id": f"EVT-{i}", "headline": f"Story {i} {c}", "label": "CRITICAL" if imp == 10 else "HIGH" if imp >= 8 else "MEDIUM" if imp >= 6 else "WATCHLIST",
                    "category": c, "category_name": names[c], "importance": imp, "summary": "s", "key_facts": ["f"], "verification": "REPORTED",
                    "source": "Src", "url": "https://x/1", "fun": c == "FUN", "big_name": i == 5})
    return out


class CardsSelect(unittest.TestCase):
    def test_deck_rules(self):
        with tempfile.TemporaryDirectory() as d:
            ctx = ctx_in(Path(d))
            notes = []
            chosen, teaser = s09_cards_select.select(ctx, items(), notes)
            self.assertEqual(len(chosen), 11)
            self.assertTrue(all(c["importance"] >= 10 for c in chosen[:3]) or chosen[0]["importance"] >= 10)
            self.assertEqual(chosen[-1]["category"], "FUN")
            self.assertLessEqual(sum(1 for c in chosen if c["category"] == "MKT"), 3)
            self.assertTrue(any(c["category"] == "ROB" for c in chosen))
            self.assertTrue(3 <= len(teaser) <= 4)
            self.assertFalse({t["id"] for t in teaser} & {c["id"] for c in chosen})
            order = [c["category"] for c in chosen if c["importance"] < 10 and c["category"] != "FUN" and not c["pick_reason"].startswith("big")]
            keys = ["POL", "MKT", "SEC", "ENE", "ROB", "MOD", "RES", "LAW", "HEA", "SOC"]
            self.assertEqual(order, sorted(order, key=keys.index))


class Fill(unittest.TestCase):
    def test_fill_synthetic_template(self):
        wf = json.loads((PKG / "tests" / "fixtures" / "template_synthetic.json").read_text(encoding="utf-8"))
        pack = {"edition": "2026-09-27", "date_title": "SUN 27 SEP 2026", "lane": "VL1", "cues": {"Anthropic": "an-thropic"},
                "rate_syllables_per_second": 4.4, "prompt_file": "x", "review_status": "Approved by Rafael (test)", "source_check": "test",
                "slots": [{"slot": 1, "kind": "intro", "state": "bypass", "title": "stored intro"},
                          {"slot": 2, "kind": "story", "category": "Politics", "story_id": "EVT-1", "symbol": "a gavel, simple text-free symbol",
                           "script": "In politics. Anthropic says the ban cost it billions of dollars this year."},
                          {"slot": 3, "kind": "teaser", "category": "Teaser", "story_ids": ["EVT-9"], "symbol": "logo",
                           "script": "Also in the full report: two more stories and a robot that folds laundry."}]
                         + [{"slot": s, "kind": "story", "state": "bypass", "title": "unused"} for s in range(4, 13)],
                "card_story_ids": ["EVT-1"], "card_teaser_story_ids": ["EVT-9"]}
        prompt = (PKG / "config" / "headlines_comfy_prompt.txt").read_text(encoding="utf-8")
        out, table, checks = s13_headlines_fill.fill(wf, pack, prompt, "sha", refs_verified=True)
        nodes = {n["id"]: n for n in out["nodes"]}
        self.assertEqual(nodes[213]["widgets_values"][0], round(syllables.count(pack["slots"][1]["script"]) / 4.4, 2))
        self.assertIn('"In politics. Anthropic says', nodes[212]["widgets_values"][0])
        self.assertIn("an-thropic", nodes[212]["widgets_values"][0])
        self.assertEqual(nodes[221]["widgets_values"][0], "video/headlines_27-9-26_C02_VL1_544")
        self.assertEqual(nodes[435]["mode"], 4)
        self.assertEqual(nodes[212]["mode"], 0)
        self.assertEqual(sum(1 for t in table if t[1] == "ACTIVE"), 2)
        self.assertTrue(any("mirror: all agree" in c for c in checks))
        qa = out["extra"]["aind_headlines"]
        self.assertEqual([s["slot"] for s in qa["slots"]], [2, 3])
        self.assertTrue(qa["slots"][0]["narration"].startswith(qa["slots"][0]["intro"]))


class Captions(unittest.TestCase):
    def test_events_inside_clip(self):
        ev = s16_stitch.caption_events("In robotics. A drone takes off from a robot arm, flies its patrol, and is caught by the arm on the way back.", 10.0, 8.0)
        self.assertTrue(ev)
        self.assertGreaterEqual(ev[0][0], 10.0)
        self.assertLessEqual(ev[-1][1], 18.0)
        for a, b, text in ev:
            self.assertLess(a, b)
            self.assertLessEqual(text.count("\\N"), 1)


if __name__ == "__main__":
    unittest.main()
