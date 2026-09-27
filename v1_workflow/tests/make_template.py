"""Synthetic ComfyUI master template with the node-id pattern of the real one (slot k owns 100k..100k+99; script +12,
seconds +13, base save +21, upscale save +35) and every field the QA tool (vendor/validate_delivery.py) inspects.
It is NOT the production template (Drive ID 1iGUq1LtGtVm1toPhDTqhWOC4qIjIe2xV); it only lets s13 and s14 run here.

    python tests/make_template.py [--out tests/fixtures/template_synthetic.json]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SEED = 1060749754396562


def node(nid, typ, widgets=None, named=None, inputs=None, outputs=None, mode=0, title=None):
    return {"id": nid, "type": typ, "title": title or typ, "mode": mode, "pos": [0, 0], "size": [200, 100],
            "inputs": inputs or [], "outputs": outputs or [], "widgets_values": widgets or [],
            **({"widgets_values_named": named} if named is not None else {})}


def build() -> dict:
    nodes, links = [], []
    lid = [0]

    def link(src, src_slot, dst, dst_slot, typ="*"):
        lid[0] += 1
        links.append([lid[0], src, src_slot, dst, dst_slot, typ])
        return lid[0]

    def out(names):
        return [{"name": n, "type": n, "links": []} for n in names]

    def inp(names):
        return [{"name": n, "type": n, "link": None} for n in names]

    nodes += [node(1, "UNETLoader", ["minimax_h3.safetensors", "default"], {"unet_name": "minimax_h3.safetensors", "weight_dtype": "default"}, outputs=out(["MODEL"])),
              node(2, "LoraLoaderModelOnly", ["h3_turbo.safetensors", 1], {"lora_name": "h3_turbo.safetensors", "strength_model": 1}, inputs=inp(["model"]), outputs=out(["MODEL"])),
              node(3, "CLIPLoader", ["clip.safetensors", "minimax"], {"clip_name": "clip.safetensors", "type": "minimax"}, outputs=out(["CLIP"])),
              node(4, "VAELoader", ["vae.safetensors"], {"vae_name": "vae.safetensors"}, outputs=out(["VAE"])),
              node(5, "VAELoader", ["vae_audio.safetensors"], {"vae_name": "vae_audio.safetensors"}, outputs=out(["VAE"])),
              node(6, "LoadImage", ["ref01_hands_on_table.png", "image"], {"image": "ref01_hands_on_table.png", "upload": "image"}, outputs=out(["IMAGE", "MASK"])),
              node(7, "LoadImage", ["ref01_hands_on_table.png", "image"], {"image": "ref01_hands_on_table.png", "upload": "image"}, outputs=out(["IMAGE", "MASK"])),
              node(8, "LoadAudio", ["voice_sample.wav", None, None], {"audio": "voice_sample.wav"}, outputs=out(["AUDIO"])),
              node(9, "RandomNoise", [SEED, "fixed"], {"noise_seed": SEED}, outputs=out(["NOISE"])),
              node(10, "KSamplerSelect", ["euler"], {"sampler_name": "euler"}, outputs=out(["SAMPLER"])),
              node(11, "BasicScheduler", ["simple", 6, 1], {"scheduler": "simple", "steps": 6, "denoise": 1}, inputs=inp(["model"]), outputs=out(["SIGMAS"])),
              node(22, "SigmaShift", [3.0], {"shift": 3.0}, inputs=inp(["model"]), outputs=out(["MODEL"]), mode=4),
              node(26, "RandomNoise", [SEED, "fixed"], {"noise_seed": SEED}, outputs=out(["NOISE"])),
              node(29, "UpscaleSettings", ["mmh3_upscale.safetensors", 1088, 1920], {"model_name": "mmh3_upscale.safetensors", "width": 1088, "height": 1920}, outputs=out(["UPSCALE"])),
              node(30, "SpectrumApplyMiniMaxH3", [True], {"enabled": True}, inputs=inp(["model"]), outputs=out(["MODEL"]))]
    by = {n["id"]: n for n in nodes}
    l = link(1, 0, 2, 0, "MODEL"); by[2]["inputs"][0]["link"] = l; by[1]["outputs"][0]["links"].append(l)
    l = link(2, 0, 30, 0, "MODEL"); by[30]["inputs"][0]["link"] = l; by[2]["outputs"][0]["links"].append(l)
    l = link(2, 0, 11, 0, "MODEL"); by[11]["inputs"][0]["link"] = l; by[2]["outputs"][0]["links"].append(l)
    l = link(2, 0, 22, 0, "MODEL"); by[22]["inputs"][0]["link"] = l; by[2]["outputs"][0]["links"].append(l)
    groups = []
    for s in range(1, 13):
        b = s * 100
        mode = 4 if s in (1, 12) else 0
        sn = [node(b + 12, "PrimitiveStringMultiline", [""], {"value": ""}, outputs=out(["STRING"]), mode=mode, title=f"C{s:02d} script"),
              node(b + 13, "PrimitiveFloat", [0.0], {"value": 0.0}, outputs=out(["FLOAT"]), mode=mode, title=f"C{s:02d} seconds"),
              node(b + 15, "EmptyMiniMaxLatent", ["x", 544, 960, 1], {"mode": "x", "width": 544, "height": 960, "batch": 1}, outputs=out(["LATENT"]), mode=mode),
              node(b + 16, "BasicGuider", [], {}, inputs=inp(["model", "conditioning"]), outputs=out(["GUIDER"]), mode=mode),
              node(b + 17, "SamplerCustomAdvanced", [], {}, inputs=inp(["noise", "guider", "sampler", "sigmas", "latent_image"]), outputs=out(["LATENT", "LATENT"]), mode=mode),
              node(b + 21, "SaveVideo", ["video/slot"], {"filename_prefix": "video/slot"}, inputs=inp(["video"]), mode=mode),
              node(b + 32, "MiniMaxUpscale", [], {}, inputs=inp(["latent", "settings"]), outputs=out(["LATENT"]), mode=mode),
              node(b + 35, "SaveVideo", ["video/slot_1088"], {"filename_prefix": "video/slot_1088"}, inputs=inp(["video"]), mode=mode)]
        nodes += sn
        for n in sn:
            by[n["id"]] = n
        l = link(30, 0, b + 16, 0, "MODEL"); by[b + 16]["inputs"][0]["link"] = l; by[30]["outputs"][0]["links"].append(l)
        l = link(b + 16, 0, b + 17, 1, "GUIDER"); by[b + 17]["inputs"][1]["link"] = l; by[b + 16]["outputs"][0]["links"].append(l)
        l = link(b + 15, 0, b + 17, 4, "LATENT"); by[b + 17]["inputs"][4]["link"] = l; by[b + 15]["outputs"][0]["links"].append(l)
        l = link(b + 17, 0, b + 32, 0, "LATENT"); by[b + 32]["inputs"][0]["link"] = l; by[b + 17]["outputs"][0]["links"].append(l)
        l = link(29, 0, b + 32, 1, "UPSCALE"); by[b + 32]["inputs"][1]["link"] = l; by[29]["outputs"][0]["links"].append(l)
        groups.append({"title": f"CLIP {s:02d}", "bounding": [0, s * 400, 1200, 380]})
    nodes += [node(9990, "MarkdownNote", ["template note"], {"text": "template note"}),
              node(9991, "Note", ["protected note"], None)]
    return {"id": "00000000-0000-0000-0000-000000000000", "revision": 0, "last_node_id": 9991, "last_link_id": lid[0],
            "nodes": nodes, "links": links, "groups": groups, "config": {}, "extra": {}, "version": 0.4}


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--out", default=str(Path(__file__).parent / "fixtures" / "template_synthetic.json"))
    a = p.parse_args()
    wf = build()
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(wf, indent=1), encoding="utf-8")
    print(f"wrote {a.out}: {len(wf['nodes'])} nodes, {len(wf['links'])} links")
