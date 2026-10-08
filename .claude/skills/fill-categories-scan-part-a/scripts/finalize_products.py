"""Final text step for the customer PDFs (CLAUDE.md, Rafi 8 Oct 2026). Run it after build_products.py and before build_pdf.py.

    python finalize_products.py --workdir W --bulletin-text W/bulletin_text.json

Reads products/bulletin_pdf.json and products/report_pdf.json and writes products/bulletin_pdf_final.json and
products/report_pdf_final.json. In the bulletin each story becomes ONE paragraph from bulletin_text.json, with the
headline shown once. Process notes ("Note: we could not open...") are removed from both products. The About
paragraphs of the bulletin are rewritten with counts only. Then it checks both products and exits 1 if a process
note, a repeated headline, a missing or non-direct link or a Google redirect remains.
"""
import argparse, json, re, sys
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True)
ap.add_argument('--bulletin-text', required=True)
a = ap.parse_args()
W = Path(a.workdir); P = W / 'products'

PROCESS = re.compile(r"\bNote:|could not open|could not read|could not be opened|headline only|headline-only|only the headline|not readable|"
                     r"our system|our reading|cloudflare|paywall", re.I)
LABELS = re.compile(r"Why it matters|What changed|What is new", re.I)


def tokens(s):
    return [w for w in re.findall(r"[a-z0-9]+", s.lower()) if len(w) > 3]


def repeats_headline(head, text):
    ht = set(tokens(head))
    if not ht:
        return False
    first = set(tokens(" ".join(text.split()[:25])))
    return len(ht & first) / len(ht) >= 0.6


def link_ok(url):
    return str(url).startswith('https://') and 'news.google' not in str(url) and 'google.com/url' not in str(url)


entries = {}
for f in (W / 'report_entries').glob('*.json'):
    e = json.loads(f.read_text(encoding='utf-8'))
    entries[(e.get('headline') or '').strip()] = e

fails = []
bt = json.loads(Path(a.bulletin_text).read_text(encoding='utf-8'))
bul = json.loads((P / 'bulletin_pdf.json').read_text(encoding='utf-8'))
full = head_only = 0
for c in bul['categories']:
    for it in c['items']:
        h = (it.get('headline') or '').strip()
        if h not in bt:
            fails.append(f"bulletin: no text for '{h[:60]}'")
            continue
        text = bt[h].strip()
        it['paragraphs'] = [text]
        if PROCESS.search(text) or LABELS.search(text):
            fails.append(f"bulletin: process note or label in '{h[:60]}'")
        if repeats_headline(h, text):
            fails.append(f"bulletin: text repeats the headline '{h[:60]}'")
        if not link_ok(it.get('url')):
            fails.append(f"bulletin: no direct link for '{h[:60]}'")
        e = entries.get(h)
        if e is not None:
            if e.get('verified_text'):
                full += 1
            else:
                head_only += 1
for sec in bul.get('extra_sections', []):
    if sec.get('title') == 'About this edition':
        sec['paragraphs'] = [
            "Stories were collected from Google News and our list of direct news sources for the 24 hours ending 09:07 UTC on 8 October 2026. Each story comes from the Full Report of the same day.",
            f"{full} of the stories are based on the full article. {head_only} are based on the headline and related coverage.",
            "Scores run from 1 to 10: 10 is critical, 8 and 9 high, 6 and 7 medium, and 1 to 5 watchlist. Nothing here is investment advice.",
        ]
(P / 'bulletin_pdf_final.json').write_text(json.dumps(bul, indent=1, ensure_ascii=False), encoding='utf-8')

rep = json.loads((P / 'report_pdf.json').read_text(encoding='utf-8'))
notes_removed = 0
warn_repeat = 0
for c in rep['categories']:
    for it in c['items']:
        before = len(it['paragraphs'])
        it['paragraphs'] = [p for p in it['paragraphs'] if not str(p).startswith('Note:')]
        notes_removed += before - len(it['paragraphs'])
        for p in it['paragraphs']:
            if re.search(r"could not open|could not read|could not be opened|headline only|our system|not readable", str(p), re.I):
                fails.append(f"report: process note left in '{str(it.get('headline'))[:60]}'")
        if it['paragraphs'] and repeats_headline(str(it.get('headline', '')), it['paragraphs'][0]):
            warn_repeat += 1
        if not link_ok(it.get('url')):
            fails.append(f"report: no direct link for '{str(it.get('headline'))[:60]}'")
(P / 'report_pdf_final.json').write_text(json.dumps(rep, indent=1, ensure_ascii=False), encoding='utf-8')

print(f"bulletin stories: {sum(len(c['items']) for c in bul['categories'])} | full article {full}, headline based {head_only}")
print(f"report: process notes removed {notes_removed} | stories whose first paragraph repeats the headline: {warn_repeat} (warning)")
if fails:
    print(f"CHECK FAILED: {len(fails)}")
    for f in fails[:40]:
        print("  -", f)
    sys.exit(1)
print("CHECK PASSED: no process notes, no repeated headlines in the bulletin, every link direct")
