"""11 Oct headlines: cut the saved API prompt into 10 clip files, then run them one by one.

Each clip file holds only the nodes its two SaveVideo outputs need (544 then its 1088 upscale),
so every job finishes one whole clip before the next starts and a crash costs one clip.
Nothing in the prompts is edited: node values come straight from the saved API prompt.
"""
import json
import os
import time
import urllib.error
import urllib.request
from datetime import datetime

BASE = "http://127.0.0.1:8188"
USER = r"C:\Users\erans\AppData\Local\Comfy-Desktop\ComfyUI-Installs\ComfyUI-refael\ComfyUI\user\default\claude"
API_PATH = os.path.join(USER, "headlines_11-10-26_api.json")
OUT_DIR = r"E:\ComfyUI\output\video"
LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "run_clips_11oct_log.txt")
DATE = "11-10-26"
SLOTS = [(f"C{k:02d}", f"{k}21", f"{k}35") for k in range(2, 12)]
MIN_544 = 500 * 1024
MIN_1088 = 1024 * 1024
MAX_ATTEMPTS = 3
JOB_TIMEOUT = 40 * 60
SERVER_WAIT = 10 * 60


def log(msg):
    line = f"{datetime.now().strftime('%H:%M:%S')} {msg}"
    print(line, flush=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def http_json(method, path, body=None, timeout=20):
    data = None
    headers = {}
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(BASE + path, data=data, method=method, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8") or "null")


def server_up():
    try:
        http_json("GET", "/system_stats", timeout=5)
        return True
    except Exception:
        return False


def wait_for_server(limit):
    t0 = time.time()
    while time.time() - t0 < limit:
        if server_up():
            return True
        time.sleep(10)
    return False


def queue_busy():
    q = http_json("GET", "/queue", timeout=10)
    return len(q.get("queue_running", [])) + len(q.get("queue_pending", [])) > 0


def ancestors(prompt, targets):
    seen = set()
    stack = list(targets)
    while stack:
        nid = stack.pop()
        if nid in seen:
            continue
        seen.add(nid)
        for v in prompt[nid]["inputs"].values():
            if isinstance(v, list) and len(v) == 2 and isinstance(v[0], str) and v[0] in prompt:
                stack.append(v[0])
    return {k: prompt[k] for k in seen}


def output_file(clip, res, started):
    """Newest file for this clip/resolution written after the job started."""
    prefix = f"headlines_{DATE}_{clip}_VL1_{res}_"
    best = None
    for name in os.listdir(OUT_DIR):
        if name.startswith(prefix) and name.endswith(".mp4"):
            p = os.path.join(OUT_DIR, name)
            if os.path.getmtime(p) >= started - 5 and (best is None or os.path.getmtime(p) > os.path.getmtime(best)):
                best = p
    return best


def files_ok(clip, started):
    f544 = output_file(clip, "544", started)
    f1088 = output_file(clip, "1088", started)
    ok544 = bool(f544) and os.path.getsize(f544) >= MIN_544
    ok1088 = bool(f1088) and os.path.getsize(f1088) >= MIN_1088
    return ok544, ok1088, f544, f1088


def split(api):
    """Write one API file per clip (kept if it already exists) and return their paths."""
    paths = {}
    for clip, id544, id1088 in SLOTS:
        path = os.path.join(USER, f"headlines_{DATE}_{clip}_api.json")
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump({"prompt": ancestors(api, [id544, id1088])}, f)
        paths[clip] = path
    return paths


def run_clip(clip, path):
    with open(path, encoding="utf-8") as f:
        sub = json.load(f)["prompt"]
    done544, done1088, _, _ = files_ok(clip, 0)
    if done544 and done1088:
        log(f"{clip}: already done, skipping")
        return "ok"
    for attempt in range(1, MAX_ATTEMPTS + 1):
        if not server_up() and not wait_for_server(SERVER_WAIT):
            log(f"{clip}: server still down after waiting, stopping")
            return "server-down"
        while queue_busy():
            time.sleep(15)
        started = time.time()
        log(f"{clip}: attempt {attempt}, submitting {os.path.basename(path)} ({len(sub)} nodes)")
        try:
            resp = http_json("POST", "/prompt", {"prompt": sub, "client_id": "claude-clip-runner"}, timeout=60)
        except urllib.error.HTTPError as e:
            log(f"{clip}: rejected by server {e.code}: {e.read().decode('utf-8', 'ignore')[:500]}")
            return "rejected"
        except Exception as e:
            log(f"{clip}: submit failed ({e}), retrying")
            continue
        pid = resp["prompt_id"]
        while time.time() - started < JOB_TIMEOUT:
            time.sleep(20)
            if not server_up():
                log(f"{clip}: server went down during job (crash?)")
                break
            try:
                h = http_json("GET", f"/history/{pid}", timeout=20)
            except Exception:
                continue
            if pid in h:
                status = h[pid].get("status", {}).get("status_str")
                log(f"{clip}: job finished with status {status}")
                break
        ok544, ok1088, f544, f1088 = files_ok(clip, started)
        if ok544 and ok1088:
            log(f"{clip}: OK  544={os.path.basename(f544)} {os.path.getsize(f544)//1024}KB  1088={os.path.basename(f1088)} {os.path.getsize(f1088)//1024}KB")
            return "ok"
        log(f"{clip}: files not valid yet (544 ok={ok544}, 1088 ok={ok1088}); retrying this clip")
        time.sleep(30)
    log(f"{clip}: FAILED after {MAX_ATTEMPTS} attempts, moving to next clip")
    return "failed"


def main():
    with open(API_PATH, encoding="utf-8") as f:
        api = json.load(f)["prompt"]
    paths = split(api)
    log(f"start: {len(api)} nodes split into {len(paths)} clip files")
    results = {}
    for clip, _, _ in SLOTS:
        results[clip] = run_clip(clip, paths[clip])
        if results[clip] == "server-down":
            break
    log("summary: " + ", ".join(f"{k}={v}" for k, v in results.items()))


if __name__ == "__main__":
    main()
