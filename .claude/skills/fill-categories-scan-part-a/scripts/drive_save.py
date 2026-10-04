"""Save a Drive file to disk byte for byte, after download_file_content has run for it.

    python drive_save.py FILE_ID OUT_PATH [--md5 HEX] [--size BYTES]

download_file_content returns JSON {"content": base64, "id", "mimeType", "title"}. A large
result is saved to a tool-results file; a small one arrives inline and is kept in the session
transcript. Never retype the base64 by hand: one wrong character corrupts the file (tested
29 Sep 2026). This script finds the newest raw result for FILE_ID in the tool-results files
and transcripts of this machine, decodes it and checks size and md5 when given.
"""
import argparse, base64, glob, hashlib, json, os, re, sys


def walk(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for v in o.values():
            yield from walk(v)
    elif isinstance(o, list):
        for v in o:
            yield from walk(v)


def from_text(text, fid):
    try:
        d = json.loads(text)
        if isinstance(d, dict) and d.get('id') == fid and d.get('content'):
            return d['content']
    except ValueError:
        pass
    m = re.findall(r'"content"\s*:\s*"([A-Za-z0-9+/=\s]+)"\s*,\s*"id"\s*:\s*"' + re.escape(fid) + '"', text)
    return m[-1] if m else None


def find(fid):
    files = glob.glob('/root/.claude/projects/**/*download_file_content*', recursive=True) + \
            glob.glob('/root/.claude/projects/**/*.jsonl', recursive=True)
    for f in sorted(files, key=os.path.getmtime, reverse=True):
        if f.endswith('.jsonl'):
            hit = None
            with open(f, encoding='utf-8', errors='replace') as fh:
                for line in fh:
                    if fid not in line or 'content' not in line:
                        continue
                    try:
                        obj = json.loads(line)
                    except ValueError:
                        continue
                    for s in walk(obj):
                        if fid in s:
                            hit = from_text(s, fid) or hit
            if hit:
                return hit, f
        else:
            hit = from_text(open(f, encoding='utf-8', errors='replace').read(), fid)
            if hit:
                return hit, f
    return None, None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('file_id')
    ap.add_argument('out')
    ap.add_argument('--md5')
    ap.add_argument('--size', type=int)
    a = ap.parse_args()
    b64, src = find(a.file_id)
    if not b64:
        sys.exit(f'No download_file_content result for {a.file_id} found; run that tool for the file first.')
    data = base64.b64decode(re.sub(r'\s', '', b64))
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    open(a.out, 'wb').write(data)
    md5 = hashlib.md5(data).hexdigest()
    ok = (a.md5 is None or md5 == a.md5) and (a.size is None or len(data) == a.size)
    print(f"{'OK' if ok else 'MISMATCH'} {a.out}: {len(data)} bytes, md5 {md5} (from {os.path.basename(src)})")
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
