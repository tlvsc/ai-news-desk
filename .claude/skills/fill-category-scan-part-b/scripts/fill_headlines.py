#!/usr/bin/env python3
"""Fill the 13-slot Headlines ComfyUI template from the day's pack (Fill_category_scan_Part_B, step 6).

    python fill_headlines.py --pack W/headlines_work/headlines_D-M-YY_pack.json \
        --template B/assets/Aind_headlines_comfy_template_13slots.json --out W/products/headlines_D-M-YY_VL1.json

Same filling as the 2 and 3 Oct 2026 scripts. Changes ONLY: slot scripts (node N12), seconds (N13), output prefixes
(N21, N35), slot modes, group titles, MarkdownNote 9990, workflow id; plus Rafi's 2 Oct settings: 8 sampler steps
(node 11) and the 4 second voice sample by name (node 8; the audio file itself stays on Rafi's PC in ComfyUI/input).
Never touches LoRA, seed, references, links or node count. Box seconds = syllables / 4.4, rounded UP to the next half
second (CLAUDE.md rule 16, Rafi 3 Oct 2026); no clip may pass 12 s (Drive Headlines Master Section B item 1).
Prints the slot table, the config line, the mirror check, the stale-word scan and the smoke-test line.
"""
import json, re, sys, uuid, copy, os, hashlib, math
from datetime import datetime

AUDIO = 'AIND_anchor_voice_sample_4s.wav'   # Rafi, 2 Oct 2026: 4 second reference, not 8
PROMPT = "A photorealistic television news anchor speaks directly to camera in a modern broadcast studio. The anchor and studio remain exactly as the reference start frame: same man, bald head, trimmed styled beard, dark navy suit, white shirt, dark tie, seated at the curved desk on the left of the frame, same lighting, same navy-blue-and-cyan newsroom, same rear displays. The glass hologram panel on the right of the frame stays in place, with its thin glowing blue border always visible, and the logo \n<0.5s> logo on blue holographic screen change slowly and shows {symbol}, one simple bold picture inside the blue border at the logo's place and size, never beyond the border and never above the top rail. No people, no faces. No readable text, no letters, no numbers, no company names or logos, no flags, no dates. <for 5 seconds>, then goes back to start point with the  same logo as started. <0.5 second> At same time The anchor says exactly, in natural English, at a natural, unhurried pace, in an authoritative and informative news presenter tone, clear and easy to understand, never rushed, and with hands, body and head movements that fits the context: \"{script}\" at the end of the sentence he puts his hands on the table and move back to the same position he started <reference image 01>. \nHe holds steady professional news energy. He stays the same person in one continuous stable broadcast. In the final second he settles and rests his hands together on the desk. \nStatic camera, locked framing, no camera movement. Natural subtle head and hand movement only. Accurate lip synchronization to the spoken words. Natural eyes, natural skin. \nAudio: the anchor's voice only, with quiet professional studio ambience. No music. \nExclusions: no captions, no subtitles, no lower thirds, no ticker, no on-screen text, no date, no logo redesign, no second person, no camera shake, no zoom, no cuts, no scene change, no morphing, no plastic skin, no hollow eyes."

# Pronunciations use the current Drive Headlines scripts/syl.py, with current-story additions.
OVR = {"raphael":3,"rafael":3,"contractors":3,"borrowed":2,"regulators":4,"nvidias":3,"anthropics":3,"loans":1,"build-out":2,"buildout":2,"cranes":1,"business":2,"hopes":1,"comes":1,"openais":4,"quietly":3,"websites":2,"minneapolis":5,"rules":1,"antibiotic":5,"slovenias":4,"mcmaster":3,"stanford":2,"thanksgiving":3,"investigating":5,"satellite":3,"orbit":2,"pinky":2,"dynamics":3,"liable":3,"intelligence":4,"copilot":3,"desktop":2,"apps":1,"emergencies":4,"emergency":4,"pennsylvania":4,"proposes":3,"fingered":2,"four-fingered":3,"ai":2,"a.i.":2,"ai's":2,"xi":1,"jinping":2,"akamai":3,"anthropic":3,"salesforce's":3,"salesforce":2,"oracle":3,"waymo's":2,"waymo":2,"alphafold":3,"deepmind's":2,"netflix's":3,"wonka":2,"gene":1,"wilder's":2,"ghoulish":2,"deepseek's":2,"deepseek":2,"mexico":3,"pipeline":2,"twenty-seven":3,"seventy":3,"eighty-two":3,"hijack":2,"customer":3,"database":3,"prepare":2,"pandemic":3,"attorneys":3,"general":3,"overriding":4,"states'":1,"reviewer":3,"ghoulishly":3,"structures":2,"flaws":1,"fixed":1,"leader":2,"control":2,"specific":3,"offered":2,"president":3,"nations":2,"billion":2,"dollar":2,"computing":3,"company":3,"shares":1,"jumped":1,"percent":2,"researchers":3,"showed":1,"hidden":2,"agents":2,"steal":1,"warned":1,"delay":2,"payments":2,"center":2,"because":2,"slipped":1,"driverless":3,"driven":2,"hundred":2,"million":2,"miles":1,"injury":3,"crashes":2,"drivers":2,"protein":2,"virus":2,"thousand":2,"predicted":3,"pairs":1,"scientists":3,"twenty-six":3,"asked":1,"congress":2,"regulate":3,"without":2,"own":1,"laws":1,"critics":2,"panned":1,"uses":2,"copy":2,"voice":1,"called":1,"also":2,"full":1,"report":2,"revenue":3,"tops":1,"factory":3,"robots":2,"record":2,"five":1,"bigger":2,"picture":2,"money":2,"keeps":1,"flowing":2,"power":2,"delays":2,"costlier":3,"debt":1,"testing":2,"eleven":3,"point":1,"six":1,"seven-year":3,"deal":1,"rent":1,"cloud":1,"whose":1,"about":2,"twenty":2,"white":1,"house":1,"models":2,"british":2,"testers":2,"holds":1,"new":1,"hit":1,"us":2,"openai":4,"ftc":3,"qwen":1,"skydio":3,"skydios":3,"nethack":2,"microsoft":3,"copilot":3,"autopilot":4,"gigawatts":3,"capacity":4,"operating":4,"companies":3,"politics":3,"appeals":2,"pentagons":3,"defense":2,"systems":2,"reportedly":4,"earlier":3,"dozens":2,"outside":2,"computer":3,"months":1,"analysts":3,"expansion":3,"centres":2,"launches":2,"patrol":2,"catches":2,"returns":2,"rebuilt":2,"around":2,"working":2,"youre":1,"science":2,"particle":3,"physics":2,"calculation":4,"human":2,"reaching":2,"physicists":3,"federal":3,"commission":3,"independent":4,"actors":2,"cannot":2,"lighter":2,"gamings":2,"games":1,"hardest":2,"attempt":2,"alibabas":4,"ninety":2,"states":1,"prices":2,"risen":2,"blacklist":2,"broke":1,"groups":1,"those":1,"research":2,"chatgpt":4,"gemini":3,"amodei":3,"bytedance":2,"alibaba":4,"dubai":2,"scenarios":4,"openai's":4,"mckinsey":3,"twelvefold":2,"paying":2,"doubled":2,"created":3,"january":4,"unites":2,"spying":2,"ais":2,"while":1,"drones":1,"headlines":2,"every":2}  # 1 Oct 2026: words the vowel-group counter reads wrongly

def syllables(text, cues):
    t = text
    for cue, real in cues.items():
        t = t.replace(cue, real)
    t = t.replace('37signals', 'thirty seven signals').replace('90 seconds', 'ninety seconds').replace("'", '').replace('’', '')
    total = 0
    for token in re.findall(r"[A-Za-z]+", t):
        word = token.lower()
        if word in OVR:
            total += OVR[word]
            continue
        if token.isupper() and len(token) <= 4:
            total += len(token)
            continue
        n = len(re.findall(r'[aeiouy]+', word))
        if word.endswith('e') and not word.endswith(('le', 'ee', 'ye')) and n > 1:
            n -= 1
        if word.endswith('ed') and not word.endswith(('ted', 'ded')) and n > 1:
            n -= 1
        total += max(1, n)
    return total

def box_seconds(syl, rate, floor, hold):
    if rate != 4.4 or floor != 0 or hold != 0:
        raise ValueError('Use syllables / 4.4 only: no floor or extra hold.')
    speech = round(syl / rate, 2)
    box = math.ceil(speech * 2 - 1e-9) / 2   # Rafael, 30 Sep 2026: round up to the next half second (8.4 -> 8.5, 8.6 -> 9.0)
    return box, speech

def main():
    import argparse
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--pack', required=True); ap.add_argument('--template', required=True); ap.add_argument('--out', required=True)
    a = ap.parse_args()
    tpl_path = a.template; wf = json.load(open(tpl_path, encoding='utf-8')); orig = copy.deepcopy(wf)
    pack = json.load(open(a.pack, encoding='utf-8'))
    nodes = {n['id']: n for n in wf['nodes']}
    # Rafi, 2 Oct 2026: 8 steps (fixed the stuttering voice) and the 4 second voice sample, not the 8 second one
    nodes[11]['widgets_values'][1] = 8; nodes[11]['widgets_values_named']['steps'] = 8
    nodes[8]['widgets_values'][0] = AUDIO; nodes[8]['widgets_values_named']['audio'] = AUDIO
    y, mo, dd = map(int, pack['edition'].split('-'))
    date = pack['date_title']; edition = f'{dd}-{mo}-{y % 100}'; lane = pack['lane']
    table = []; old_scripts = []; longest_tpl = 0.0
    # template facts before touching anything
    for s in range(1, 14):
        n13 = nodes.get(s*100+13)
        if n13: longest_tpl = max(longest_tpl, float(n13['widgets_values'][0]))
    n11 = nodes.get(11); steps = 8
    lora = next((n['widgets_values'][0] for n in wf['nodes'] if n.get('type','').lower().startswith('loraloader') or 'lora' in n.get('type','').lower()), '?')
    seed = next((v for n in wf['nodes'] for v in n.get('widgets_values', []) if v == 1060749754396562), 'NOT FOUND')

    def set_widget(node, idx, value):
        old = node['widgets_values'][idx]; node['widgets_values'][idx] = value
        named = node.get('widgets_values_named')
        if isinstance(named, dict):
            key = {'PrimitiveStringMultiline': 'value', 'PrimitiveFloat': 'value',
                   'SaveVideo': 'filename_prefix', 'MarkdownNote': 'text'}.get(node['type'])
            if idx == 0 and key in named:
                named[key] = value
            else:
                for k, v in named.items():
                    if v == old: named[k] = value
        return old

    for slot in pack['slots']:
        s = slot['slot']; ids = {o: nodes.get(s*100+o) for o in (12, 13, 21, 35)}
        active = slot.get('state') != 'bypass'
        for n in wf['nodes']:
            if s*100 <= n['id'] < s*100+100: n['mode'] = 0 if active else 4
        if active:
            syl = syllables(slot['script'], pack['cues'])
            box, speech = box_seconds(syl, pack['rate_syllables_per_second'], pack['floor_seconds'], pack['hold_seconds'])
            assert box <= 12.0, f'Slot {s} runs {box}s: Headlines Master Section B item 1 allows 12 s at most'
            prompt = slot['prompt'] if slot.get('prompt') else PROMPT.format(symbol=slot['symbol'].rstrip('.'), script=slot['script'])
            old_scripts.append(set_widget(ids[12], 0, prompt)); set_widget(ids[13], 0, box)
            set_widget(ids[21], 0, f'video/headlines_{edition}_C{s:02d}_{lane}_544')
            set_widget(ids[35], 0, f'video/headlines_{edition}_C{s:02d}_{lane}_1088')
            kind = slot['kind']; name = slot.get('category', kind)
        else:
            syl = 0; box = 0.0; speech = 0.0; kind = slot['kind']; name = slot.get('title', 'bypassed')
            old_scripts.append(set_widget(ids[12], 0, '')); set_widget(ids[13], 0, 0.0)
            set_widget(ids[21], 0, ''); set_widget(ids[35], 0, '')
        for n in (ids[12], ids[13], ids[21], ids[35]):
            n['title'] = f'{date} C{s:02d} {name}'
        for g in wf.get('groups', []):
            if re.search(rf'\bCLIP\s*0*{s}\b', g.get('title', ''), re.I):
                g['title'] = f'{date} CLIP {s:02d} {name} {box:.2f}s' if active else f'{date} CLIP {s:02d} BYPASSED'
        table.append((s, 'ACTIVE' if active else 'BYPASS', box, syl, speech, kind, name))

    wf['id'] = str(uuid.uuid4())
    wf.setdefault('extra', {})['aind_fill'] = {
        'edition': pack['edition'],
        'template_sha256': hashlib.sha256(open(tpl_path, 'rb').read()).hexdigest(),
        'blueprint': 'Headlines_Master_Rules_Structure.txt',
        'prompt_file': pack['prompt_file'],
        'review_status': pack['review_status'],
        'source_check': pack['source_check'],
        'generation_authorized': False,
        'bigger_picture': pack.get('bigger_picture')
    }
    if 9990 in nodes:
        note = f"{date} Headlines fill (Claude lane). Slots: " + '; '.join(f"C{t[0]:02d} {t[6]} {t[2]:.2f}s" for t in table)
        note += '\nC01 and C13 reuse stored opening and ending. The Bigger Picture: ' + ((pack.get('bigger_picture') or {}).get('file') or 'generated in C12')
        note += '\n' + pack['review_status'] + '\n' + pack['source_check']
        set_widget(nodes[9990], 0, note)
    out = a.out
    original_nodes = {n['id']: n for n in orig['nodes']}
    protected = [n['id'] for n in orig['nodes'] if (n['id'] < 100 or n['id'] == 9991) and n['id'] not in (8, 11)]  # 8 and 11 changed on Rafi's order, 2 Oct 2026
    assert all(nodes[i] == original_nodes[i] for i in protected), 'Protected configuration changed'
    assert wf['links'] == orig['links'] and len(wf['nodes']) == len(orig['nodes']), 'Topology changed'
    assert nodes[11]['widgets_values'][1] == nodes[11]['widgets_values_named']['steps'] == 8
    assert nodes[8]['widgets_values'][0] == nodes[8]['widgets_values_named']['audio'] == AUDIO
    assert (nodes[6]['widgets_values'][0], nodes[7]['widgets_values'][0]) == ('AIND_codex_frame_hologram_matched_4K_6_final_preview_v6.png', 'AIND_Comfy_reference_3_2160x3840_smile_v4.png'), 'Reference images are not the 29 Sep pair (1 = final_preview_v6, 2 = smile_v4)'
    links = {l[0]: l for l in wf['links']}
    spectrum_node = next(n for n in wf['nodes'] if n['type'] == 'SpectrumApplyMiniMaxH3')
    assert spectrum_node['mode'] == 0 and spectrum_node['widgets_values'][0] is True
    spectrum_id = spectrum_node['id']
    assert links[spectrum_node['inputs'][0]['link']][1] == 2, 'Spectrum input must follow LoRA'
    for row in pack['slots']:
        base = row['slot'] * 100
        active = row.get('state') != 'bypass'
        expected_mode = 0 if active else 4
        assert all(n['mode'] == expected_mode for n in wf['nodes'] if base <= n['id'] < base + 100)
        if active:
            guider_model = next(i['link'] for i in nodes[base+16]['inputs'] if i['name'] == 'model')
            latent_link = next(i['link'] for i in nodes[base+32]['inputs'] if i['name'] == 'latent')
            assert links[guider_model][1] == spectrum_id, 'Generation bypasses Spectrum'
            assert links[latent_link][1] == base+17, 'Upscale must follow generated latent'
            assert nodes[base+13]['widgets_values'][0] == math.ceil(round(syllables(row['script'], pack['cues']) / 4.4, 2) * 2 - 1e-9) / 2
            if not row.get('prompt'):  # slots with their own full prompt (the 28 Sep opening) keep its wording
                assert 'hands, body and head movements' in nodes[base+12]['widgets_values'][0]
            assert '<reference image 01>' in nodes[base+12]['widgets_values'][0]
        for offset, key in ((12,'value'),(13,'value'),(21,'filename_prefix'),(35,'filename_prefix')):
            node = nodes[base+offset]
            assert node['widgets_values_named'][key] == node['widgets_values'][0], 'Visible/named mismatch'
    assert not os.path.exists(out), 'Existing output must be reviewed before replacement'
    json.dump(wf, open(out, 'x', encoding='utf-8'), ensure_ascii=False, indent=2)

    # checks
    print(f'\nWRITTEN {out}\nnodes {len(wf["nodes"])} (template {len(orig["nodes"])}), links {len(wf.get("links", []))} (template {len(orig.get("links", []))})')
    print(f'CONFIG  lora={lora} steps={steps} (template had 6) seed={seed} audio={AUDIO} (template had AIND_anchor_voice_sample_8s.mp3)')
    spectrum=[n['id'] for n in wf['nodes'] if 'spectrum' in n.get('type','').lower()]
    print('SPECTRUM ' + (f'CONNECTED and enabled, node {spectrum}' if spectrum else 'MISSING: run this script against headlines_23-9-26_VL1.json, which carries the Spectrum node'))
    print('\nSLOT  STATE   BOX   SYL  SPEECH  KIND            NAME')
    for t in table: print(f'C{t[0]:02d}   {t[1]:6} {t[2]:6.2f} {t[3]:4d} {t[4]:6.2f}  {t[5]:15} {t[6]}')
    gen = sum(t[2] for t in table if t[1] == 'ACTIVE'); print(f'TOTAL generated {gen:.1f}s over {sum(1 for t in table if t[1]=="ACTIVE")} boxes')
    longest_new = max(t[2] for t in table); print(f'SMOKE   template longest box {longest_tpl:.1f}s, new longest {longest_new:.1f}s ->',
          'LONGER THAN TEMPLATE; generation remains pending spoken-copy approval' if longest_new > longest_tpl else 'inside the template range')
    newly = [t[0] for t in table if t[1]=='ACTIVE' and orig and nodes.get(t[0]*100+12) and next((n['mode'] for n in orig['nodes'] if n['id']==t[0]*100+12), 0) == 4]
    print('NEWLY ACTIVE SLOTS vs template:', newly or 'none', '(generation remains pending spoken-copy approval)')
    bad = [n['id'] for n in wf['nodes'] if isinstance(n.get('widgets_values_named'), dict) and n.get('widgets_values')
           and not all(v in n['widgets_values'] for v in n['widgets_values_named'].values() if isinstance(v,(str,int,float)))]
    print('MIRROR  ' + ('ALL AGREE' if not bad else f'MISMATCH on nodes {bad}'))
    dump = json.dumps(wf, ensure_ascii=False)
    hits = sorted({w for o in old_scripts if o for w in re.findall(r'"([^"]{20,})"', o) if w in dump and w not in json.dumps(pack)})
    print('STALE   ' + ('none' if not hits else f'OLD SCRIPT TEXT STILL PRESENT: {hits[:3]}'))
    print('CUES    ' + ', '.join(f'{c} in C{t[0]:02d}' for t in table for c in pack['cues'] if t[1]=='ACTIVE' and c in next(sl['script'] for sl in pack['slots'] if sl['slot']==t[0])))
    print('VISUAL  story-visual clip: ' + ', '.join(f'C{sl["slot"]:02d}' for sl in pack['slots'] if sl.get('story_visual')))

if __name__ == '__main__': main()
