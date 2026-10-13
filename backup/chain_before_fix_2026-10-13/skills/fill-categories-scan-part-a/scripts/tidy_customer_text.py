"""Customer text rules for the Daily Bulletin and the Full Report (Rafi, 8 Oct 2026). New script; run after build_products.py.

    python tidy_customer_text.py --workdir W --bulletin-in W/products/bulletin_pdf_before_rewrite_old.json \
        --report-in W/products/report_pdf.json

Rules applied, and nothing else is rewritten:
- Headline once. The first paragraph may repeat the headline once; no later paragraph may repeat it or the first paragraph.
- A sentence of a later paragraph is deleted when at least 60 percent of its longer words already appear in the headline or the first paragraph.
- Bulletin: at most 2 paragraphs per story. Full Report: at most 3.
- Process wording is deleted from the text (sentences about our reading, blocked sites, 401/403 errors, paywalls, "headline only").
- Every story keeps its direct https link to the source.
- The bulletin About paragraph and purpose line lose internal wording (test edition, source counts, cutoffs).
It writes products/bulletin_pdf_final.json, products/report_pdf_final.json and products/customer_text_changes.json (every deletion), then checks both and exits 1 if a rule fails.
"""
import argparse, json, re, sys
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True)
ap.add_argument('--bulletin-in', required=True)
ap.add_argument('--report-in', required=True)
a = ap.parse_args()
W = Path(a.workdir); P = W / 'products'

PROCESS = re.compile(r"could not open|could not read|could not be opened|could not be read|headline only|headline-only|"
                     r"only the headline|our system|our reading|not readable|cloudflare|paywall|\b40[13]\b|\bHTTP\b|"
                     r"test edition|source list", re.I)
LABEL = re.compile(r"^(What changed|What is new|What is new today)\s*:\s*", re.I)


def toks(s):
    return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if len(w) > 3}


def sentences(text):
    return [s for s in re.split(r'(?<=[.!?])\s+(?=[A-Z"“(\'])', text.strip()) if s]


LABEL_ANY = re.compile(r"\b(Why it matters|What changed|What is new today|What is new)\s*:\s*", re.I)


def repeats(sent, against):
    st = toks(LABEL_ANY.sub("", sent))
    if len(st) < 4:
        return False
    return len(st & against) / len(st) >= 0.6


changes = []  # (product, headline, kind, text)


def tidy_story(prod, head, paras):
    paras = [p for p in paras if not str(p).startswith('Note:')]
    if not paras:
        return paras
    head_t = toks(head)
    out = []
    first_t = set()
    for i, p in enumerate(paras):
        kept = []
        for s in sentences(str(p)):
            if PROCESS.search(s):
                changes.append((prod, head, 'process wording deleted', s)); continue
            if i > 0:
                if repeats(s, head_t | first_t):
                    changes.append((prod, head, 'repeated sentence deleted', s)); continue
            kept.append(s)
        text = " ".join(kept).strip()
        if i > 0:
            text = re.sub(r"\b(What changed|What is new today|What is new)\s*:\s*", "", text, flags=re.I).strip()
        if text and text != "Why it matters:":
            out.append(text)
        if i == 0:
            first_t = toks(" ".join(kept))
    return out


def check_product(name, data, max_paras):
    bad = []
    for c in data['categories']:
        for it in c['items']:
            h = it.get('headline', '')
            paras = it['paragraphs']
            if len(paras) > max_paras:
                bad.append(f"{name}: {len(paras)} paragraphs in '{h[:50]}'")
            if len(paras) > 1 and any(repeats(s, toks(h) | toks(paras[0])) for s in sentences(paras[1])):
                bad.append(f"{name}: a later paragraph repeats '{h[:50]}'")
            for p in paras:
                if PROCESS.search(str(p)):
                    bad.append(f"{name}: process wording in '{h[:50]}'")
            url = str(it.get('url', ''))
            if not url.startswith('https://') or 'news.google' in url:
                bad.append(f"{name}: no direct link for '{h[:50]}'")
    return bad


bul = json.loads(Path(a.bulletin_in).read_text(encoding='utf-8'))
for c in bul['categories']:
    for it in c['items']:
        it['paragraphs'] = tidy_story('bulletin', it['headline'], it['paragraphs'])
for sec in bul.get('extra_sections', []):
    if sec.get('title') == 'About this edition':
        before = " ".join(sec['paragraphs'])
        sec['paragraphs'] = [
            "Stories were collected from Google News and from direct news sources for the 24 hours ending 09:07 UTC on 8 October 2026.",
            "Scores run from 1 to 10: 10 is critical, 8 and 9 high, 6 and 7 medium, and 1 to 5 watchlist. Nothing here is investment advice.",
        ]
        changes.append(('bulletin', 'About this edition', 'rewritten: test edition, source count and reading counts removed', before[:160]))
bul['purpose'] = "A concise selection of the day's most important AI developments, taken from the Full Report."
changes.append(('bulletin', 'Purpose line', 'cutoff details removed', 'score cutoffs by section'))

rep = json.loads(Path(a.report_in).read_text(encoding='utf-8'))
for c in rep['categories']:
    for it in c['items']:
        it['paragraphs'] = tidy_story('report', it.get('headline', ''), it['paragraphs'])
rep['purpose'] = rep.get('purpose', '').replace('every story we kept from today\'s pool', 'every story we kept today')

fails = check_product('bulletin', bul, 2) + check_product('report', rep, 3)
(P / 'bulletin_pdf_final.json').write_text(json.dumps(bul, indent=1, ensure_ascii=False), encoding='utf-8')
(P / 'report_pdf_final.json').write_text(json.dumps(rep, indent=1, ensure_ascii=False), encoding='utf-8')
(P / 'customer_text_changes.json').write_text(json.dumps(
    [{"product": p, "story": h, "change": k, "text": t} for p, h, k, t in changes], indent=1, ensure_ascii=False), encoding='utf-8')

from collections import Counter
print("changes:", dict(Counter(k for _, _, k, _ in changes)))
print("bulletin stories:", sum(len(c['items']) for c in bul['categories']),
      "| paragraphs per story:", dict(Counter(len(it['paragraphs']) for c in bul['categories'] for it in c['items'])))
print("report stories:", sum(len(c['items']) for c in rep['categories']),
      "| paragraphs per story:", dict(Counter(len(it['paragraphs']) for c in rep['categories'] for it in c['items'])))
if fails:
    print(f"CHECK FAILED: {len(fails)}")
    for f in fails[:30]:
        print("  -", f)
    sys.exit(1)
print("CHECK PASSED: paragraph limits, no repeats, no process wording, every story has a direct link")
