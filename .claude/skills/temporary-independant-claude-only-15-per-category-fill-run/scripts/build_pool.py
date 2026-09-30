"""Step 3. Merge the 16 curators' files into one pool: 15 per category, 10 for The Fun Side.

    python build_pool.py --workdir W [--per-cat 15] [--fun 10]

Reads W/run.json, W/pool/cat_NN.json and yesterday's pool (path in run.json).
Optional editor files in W: drops.json {"drops": [[cat, "title", "why"], ...]} removes a pick.
Name the pick by its exact title (or a unique start of it), as it appears in pool/cat_NN.json;
the pool CSV's pool_rank is NOT the curator's rank, so numbers are unsafe (30 Sep 2026: a
number removed the wrong story in two categories). A number still works for old runs, and the
removed title is always printed. No match, or more than one, stops the script before it writes
anything. dedupe_overrides.json {url: category id} says which category keeps a shared story;
without it the story stays where it is a main pick rather than a backup, then in the lower
category (30 Sep 2026: keeping it in the lower category, where it was only a backup, dropped
the story from the pool altogether).
Writes W/out/AIND_Pool_<edition>.json and .csv (LF line ends) and W/out/build_log.json.
Read build_log.json: near_dupes and similar_to_yesterday need an editor's decision.
"""
import argparse, csv, json, re, sys
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


def read_editor_files(W):
    """drops.json and dedupe_overrides.json, checked; a bad file stops the run with a plain message."""
    overrides, drops = {}, []
    try:
        if (W / 'dedupe_overrides.json').exists():
            raw = json.loads((W / 'dedupe_overrides.json').read_text(encoding='utf-8'))
            overrides = {norm_url(k): int(v) for k, v in raw.items()}
        if (W / 'drops.json').exists():
            drops = json.loads((W / 'drops.json').read_text(encoding='utf-8'))
            if not isinstance(drops, dict) or not isinstance(drops.get('drops'), list):
                raise ValueError('drops.json must look like {"drops": [[category number, "title", "why"], ...]}')
            drops = drops['drops']
            for d in drops:
                if not (isinstance(d, list) and len(d) == 3 and isinstance(d[0], int) and isinstance(d[1], (int, str))):
                    raise ValueError(f'each drop must be [category number, "title", "why"], got {d!r}')
    except (ValueError, KeyError, TypeError, AttributeError) as e:
        sys.exit(f'Editor file problem, nothing written: {e}')
    return overrides, drops


def norm_title(t):
    return re.sub(r'\s+', ' ', str(t)).strip().lower()


def apply_drops(data, drops, log):
    for cid, key, why in drops:
        items = data.get(cid)
        if items is None:
            sys.exit(f'drops.json: there is no category {cid}; nothing written.')
        if isinstance(key, int):
            hit = [i for i in items if i.get("rank") == key]
        else:
            k = norm_title(key)
            hit = [i for i in items if norm_title(i["title"]) == k] or \
                  [i for i in items if norm_title(i["title"]).startswith(k)]
        if len(hit) != 1:
            titles = "\n".join(f"  rank {i.get('rank')}: {i['title']}" for i in items)
            sys.exit(f"drops.json: {len(hit) or 'no'} pick(s) in category {cid} match {key!r}; nothing written.\n"
                     f"Category {cid} picks:\n{titles}")
        it = hit[0]
        print(f"drop, category {cid}: {it['title']} ({why})" + (" [named by number: check this title]" if isinstance(key, int) else ""))
        log["manual_drops"].append((cid, it["title"], why))
        data[cid] = [i for i in items if i is not it]


def keeper(data, key, cids, overrides):
    """Which category keeps a story picked in several: the override, else a main pick before a
    backup, then the lower category number (the rule before 30 Sep 2026 for two main picks)."""
    if key in overrides and overrides[key] in cids:
        return overrides[key]
    if key in overrides:
        print(f"WARNING: dedupe_overrides.json names category {overrides[key]} for a story picked only in {sorted(set(cids))}; ignored")
    def standing(cid):
        it = next(i for i in data[cid] if norm_url(i["url"]) == key)
        return (bool(it.get("backup")), cid)
    return min(sorted(set(cids)), key=standing)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--workdir', required=True)
    ap.add_argument('--per-cat', type=int, default=15)
    ap.add_argument('--fun', type=int, default=10)
    a = ap.parse_args()
    W = Path(a.workdir); run = load_run(W); (W / 'out').mkdir(exist_ok=True)
    start, end = parse_utc(run['start']), parse_utc(run['end'])
    CATS = short_names()
    overrides, drops = read_editor_files(W)

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
    apply_drops(data, drops, log)
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
    # 3. cross-category duplicates by URL: see keeper()
    owner = {}
    for cid in sorted(data):
        for it in data[cid]:
            owner.setdefault(norm_url(it["url"]), []).append(cid)
    for key, cids in owner.items():
        if len(set(cids)) > 1:
            keep = keeper(data, key, cids, overrides)
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
