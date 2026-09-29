"""Step 3. Merge the 16 curators' files into one pool: 15 per category, 10 for The Fun Side.

    python build_pool.py --workdir W [--per-cat 15] [--fun 10]

Reads W/run.json, W/pool/cat_NN.json and yesterday's pool (path in run.json).
Optional editor files in W: drops.json {"drops": [[cat, rank, "why"], ...]} removes a pick;
dedupe_overrides.json {normalised url: category id} says which category keeps a shared story.
Writes W/out/AIND_Pool_<edition>.json and .csv (LF line ends) and W/out/build_log.json.
Read build_log.json: near_dupes and similar_to_yesterday need an editor's decision.
"""
import argparse, csv, json, re
from pathlib import Path

from common import FUN, load_pool_file, load_run, norm_url, parse_utc, pool_path, short_names, similar


def in_window(pub, start, end):
    pub = (pub or "").strip()
    if not pub:
        return False, "no date"
    days = {start.date().isoformat(), end.date().isoformat()}
    if re.match(r"^\d{4}-\d{2}-\d{2}$", pub):
        return pub in days, "date only"
    try:
        dt = parse_utc(pub)
    except ValueError:
        return pub[:10] in days, "unparsed"
    return start <= dt <= end, "datetime"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--workdir', required=True)
    ap.add_argument('--per-cat', type=int, default=15)
    ap.add_argument('--fun', type=int, default=10)
    a = ap.parse_args()
    W = Path(a.workdir); run = load_run(W); (W / 'out').mkdir(exist_ok=True)
    start, end = parse_utc(run['start']), parse_utc(run['end'])
    CATS = short_names()
    overrides = json.loads((W / 'dedupe_overrides.json').read_text()) if (W / 'dedupe_overrides.json').exists() else {}
    drops = json.loads((W / 'drops.json').read_text())['drops'] if (W / 'drops.json').exists() else []

    data = {}
    for cid in CATS:
        f = W / 'pool' / f"cat_{cid:02d}.json"
        if not f.exists():
            print(f'WARNING: {f.name} missing'); data[cid] = []; continue
        raw = f.read_text(encoding='utf-8')
        items = json.loads(raw[raw.find("["):raw.rfind("]") + 1])
        for it in items:
            it["category_id"] = cid
        data[cid] = sorted(items, key=lambda x: x.get("rank", 99))

    log = {"manual_drops": [], "out_of_window": [], "dupe_within": [], "dupe_cross": [], "near_dupes": [],
           "repeat_of_yesterday_url": [], "similar_to_yesterday": []}
    for cid, rank, why in drops:
        log["manual_drops"] += [(cid, i["title"], why) for i in data[cid] if i.get("rank") == rank]
        data[cid] = [i for i in data[cid] if i.get("rank") != rank]
    # 1. out-of-window and within-category duplicates
    for cid, items in data.items():
        kept, seen = [], set()
        for it in items:
            ok, how = in_window(it.get("published"), start, end)
            it["date_check"] = how
            if not ok:
                log["out_of_window"].append((cid, it.get("title"), it.get("published"))); continue
            key = (norm_url(it.get("url")), it.get("title"))
            if key in seen:
                log["dupe_within"].append((cid, it.get("title"))); continue
            seen.add(key); kept.append(it)
        data[cid] = kept
    # 2. never repeat a URL from yesterday's pool
    yday = load_pool_file(run['yesterday']) if run.get('yesterday') else []
    yurls = {norm_url(y["url"]) for y in yday}
    for cid in data:
        log["repeat_of_yesterday_url"] += [(cid, i["title"]) for i in data[cid] if norm_url(i["url"]) in yurls]
        data[cid] = [i for i in data[cid] if norm_url(i["url"]) not in yurls]
    # 3. cross-category duplicates by URL: the override keeps it, else the lower category id
    owner = {}
    for cid in sorted(data):
        for it in data[cid]:
            owner.setdefault(norm_url(it["url"]), []).append(cid)
    for key, cids in owner.items():
        if len(set(cids)) > 1:
            keep = overrides.get(key, cids[0])
            for cid in set(cids) - {keep}:
                data[cid] = [i for i in data[cid] if norm_url(i["url"]) != key]
            log["dupe_cross"].append((key, cids, keep))
    # 4. take the top picks per category (backups move up when a main pick was removed)
    pool = []
    for cid in sorted(data):
        for n, it in enumerate(data[cid][:(a.fun if cid == FUN else a.per_cat)], 1):
            it.update(pool_rank=n, item_id=f"C{cid:02d}-{n:02d}", category=CATS[cid], from_backup=bool(it.get("backup")))
            pool.append(it)
    # 5. flag near-duplicate titles, inside the pool and against yesterday, for the editor
    for i, x in enumerate(pool):
        for y in pool[i + 1:]:
            s = similar(x["title"], y["title"])
            if s >= 0.45:
                log["near_dupes"].append((x["item_id"], y["item_id"], round(s, 2), x["title"], y["title"]))
        for y in yday:
            s = similar(x["title"], y["title"])
            if s >= 0.4:
                log["similar_to_yesterday"].append((x["item_id"], y["item_id"], round(s, 2), x["title"], y["title"]))

    pool_path(W, run).write_text(json.dumps(pool, indent=2, ensure_ascii=False), encoding='utf-8')
    cols = ["item_id", "category_id", "category", "pool_rank", "title", "summary", "source", "url",
            "published", "time_verified", "subcategory", "importance", "also_fits", "label", "from_backup"]
    with open(pool_path(W, run).with_suffix('.csv'), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for it in pool:
            w.writerow(dict(it, also_fits=",".join(str(x) for x in it.get("also_fits") or [])))
    (W / 'out' / 'build_log.json').write_text(json.dumps(log, indent=2, ensure_ascii=False), encoding='utf-8')
    print("TOTAL", len(pool))
    for cid in CATS:
        print(f"{cid:2d} {sum(1 for p in pool if p['category_id'] == cid):2d}  avail={len(data[cid])}  {CATS[cid]}")
    print({k: len(v) for k, v in log.items()})


if __name__ == "__main__":
    main()
