# VENDORED COPY. Origin: Google Drive, AI_News_Desk / Blueprint_Library, file
# "AIMD_LV1_Adverts_Automation_Skill_V1_validate_delivery.py" (ChatGPT lane QA tool, 26 Sep 2026 state),
# mirrored 27 Sep 2026 by the Claude lane into v1_workflow/vendor. Unchanged apart from this header.
# s14_validate.py calls it as a subprocess; the Drive file stays the authority. Re-copy when Drive changes.

"""Validate AIND's product folders and the exact current card delivery, without publishing."""
import argparse, hashlib, json, struct, math, re, urllib.request
from pathlib import Path
from datetime import date

def validate(manifest, inventory, cards_dir=None):
    cards = manifest['products']['cards']
    entries = cards['ordered_files']
    assert len(entries) == 15, 'Current card set must contain exactly 15 cards'
    assert len({x['id'] for x in entries}) == 15, 'Duplicate card IDs'
    assert cards['format'] == [1080, 1920], 'Unexpected card format'
    assert [x['order'] for x in entries] == list(range(1, 16)), 'Invalid card order'
    lane = cards.get('producing_lane')
    assert lane in ('VL1', 'VL2'), 'Record the actual producing workflow lane'
    edition = date.fromisoformat(manifest['edition'])
    short_date = f'{edition.day}-{edition.month}-{edition.year % 100:02d}'
    for entry in entries:
        expected_name = f"cards_{short_date}_I{entry['order']:02d}_{lane}.png"
        assert entry['name'] == expected_name, 'Incorrect card filename order, lane or extra version suffix'
    combined = cards['combined_image']
    assert combined['id'] not in {x['id'] for x in entries}, 'Combined image is not a carousel card'
    children = inventory[cards['folder_id']]
    files = [x for x in children if x['file_or_folder'] != 'folder']
    assert {x['id'] for x in files} == {x['id'] for x in entries} | {combined['id']}, 'Extra/missing current card output'
    expected = {x['id']: x for x in entries + [combined]}
    for actual in files:
        item = expected[actual['id']]
        assert actual['title'] == item['name'], 'Filename changed'
        assert int(actual['size']) == item['bytes'], 'Remote size mismatch'
    root = inventory[manifest['daily_folder']['id']]
    assert {x['id'] for x in root if x['file_or_folder'] == 'folder'} == {p['folder_id'] for p in manifest['products'].values()}, 'Unexpected date-root folder'
    assert {x['id'] for x in root if x['file_or_folder'] != 'folder'} == {manifest['manifest_id']}, 'Loose files in date root'
    actual_files = [f for children in inventory.values() for f in children if f['file_or_folder'] != 'folder']
    assert len(actual_files) == len({f['id'] for f in actual_files}), 'Duplicate file identities in delivery tree'
    recorded = manifest['files'] + manifest['source_documents']
    assert {f['id'] for f in actual_files} == {f['id'] for f in recorded} | {manifest['manifest_id']}, 'Unrecorded or missing file'
    for item in recorded:
        matches = [f for f in inventory[item['parent_id']] if f['id'] == item['id']]
        assert len(matches) == 1, 'Wrong parent for ' + item.get('name', item.get('title', item['id']))
        assert matches[0]['title'] == item.get('name', item.get('title')), 'Recorded filename mismatch'
        if item.get('bytes') is not None and matches[0].get('size') is not None:
            assert int(matches[0]['size']) == item['bytes'], 'Recorded byte-size mismatch'
    if cards_dir:
        for item in entries + [combined]:
            data = (Path(cards_dir) / item['name']).read_bytes()
            assert hashlib.sha256(data).hexdigest() == item['sha256'], 'Local card bytes changed'
            if item in entries:
                assert data[:8] == b'\x89PNG\r\n\x1a\n', 'Not a PNG'
                assert list(struct.unpack('>II', data[16:24])) == [1080, 1920], 'Wrong PNG dimensions'
    return {'storage_validation': 'PASS', 'current_cards': 15, 'combined_images': 1,
            'publication_status': cards['publication_status'], 'publication_approval_inferred': False}

def headlines_seconds(syllables):
    """Headlines_Master_Rules_Structure.txt Section B item 1a: seconds = syllables / 4.4, written to two decimals.

    No rounding up to a half second and no added time (Rafael, 25 Sep 2026).
    Pose holds are flexible instructions and never additional duration inputs.
    """
    if type(syllables) is not int or syllables <= 0:
        raise ValueError('Syllable count must be a positive integer')
    return round(syllables / 4.4, 2)


def blueprint_prompt(prompt_text):
    """Headlines_prompt_for_comfy_json.txt (folder Headlines_prompt_for_comfy_json): the only copy of the generation prompt."""
    b2 = prompt_text.strip()
    if b2.count('<article content>') != 2 or '"<article content>"' not in b2:
        raise ValueError('The prompt file must hold exactly two <article content> placeholders, the second one quoted')
    return b2


def validate_headlines(workflow, schema=None, b2=None):
    """Check a reviewed Headlines build; never queue, rewrite, or approve media."""
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)
    nodes = {n['id']: n for n in workflow['nodes']}
    pack = workflow.get('extra', {}).get('aind_headlines')
    if not pack:
        raise ValueError('Missing single-source Headlines pack: extra.aind_headlines')
    # Check the current submission graph, never historical attempt snapshots.
    run = workflow.get('extra', {}).get('aind_run', {})
    current_api = run.get('api_graph', {})
    if 'api_graph' in run:
        require(isinstance(current_api, dict) and bool(current_api), 'Current API graph is empty or invalid')
    if not isinstance(current_api, dict):
        current_api = {}
    def require_api_value(nid, key, expected):
        api_node = current_api.get(str(nid), {})
        inputs = api_node.get('inputs', {}) if isinstance(api_node, dict) else {}
        require(isinstance(inputs, dict) and key in inputs and inputs[key] == expected,
                f'Node {nid}: current API {key} differs from executable UI')
    for nid, key, index in ((6, 'image', 0), (7, 'image', 0), (8, 'audio', 0),
                            (9, 'noise_seed', 0), (10, 'sampler_name', 0),
                            (11, 'scheduler', 0), (11, 'steps', 1), (11, 'denoise', 2),
                            (26, 'noise_seed', 0)):
        if str(nid) in current_api:
            require_api_value(nid, key, nodes[nid]['widgets_values'][index])
    require(len(nodes) == len(workflow['nodes']), 'Duplicate node IDs')
    require(pack.get('edition') is not None, 'Missing edition')
    require(pack.get('timing_decision_confirmed') is True, 'Missing acknowledged boundary rule')
    rate = pack.get('syllables_per_second')
    require(rate == 4.4, 'Timing must use 4.4 syllables/second')
    require(pack.get('timing_formula') == 'syllables / 4.4', 'Rules file Section B item 1a timing formula missing or changed')
    require(pack.get('boundary_hold_duration_is_flexible') is True, 'Boundary pose must not impose exact hold deadlines')
    require(not pack.get('unresolved_issues'), 'Unresolved build issues remain')
    require(nodes[11]['widgets_values'] == ['simple', 6, 1], 'Incorrect base scheduler')
    require(nodes[11]['widgets_values_named'].get('steps') == 6, 'Hidden steps differ')
    require(nodes[9]['widgets_values'][0] == 1060749754396562, 'Anchor seed changed')
    require(nodes[26]['widgets_values'][0] == 1060749754396562, 'Upscale seed changed')
    require(nodes[2]['widgets_values'][1] == 1, 'LoRA strength changed')
    require(nodes[10]['widgets_values'][0] == 'euler', 'Base sampler changed')
    require(nodes[22]['mode'] == 4, 'SigmaShift must remain bypassed')
    require(nodes[29]['widgets_values'][1:3] == [1088, 1920], 'Upscale size changed')
    expected_refs = pack.get('references', [])
    require(len(expected_refs) == 2, 'Exactly two reviewed image references required')
    for ref in expected_refs:
        node = nodes[ref['node_id']]
        require(node['widgets_values'][0] == ref['filename'], 'Reference filename mismatch')
        require(node['widgets_values_named'].get('image') == ref['filename'], 'Hidden reference mismatch')
        require(ref.get('visually_verified') is True, 'Reference pose has not been visually reviewed')
    if expected_refs:
        require(expected_refs[0].get('role') == 'boundary_hands_on_table', 'Picture 1 must define settled hands-on-table pose')
        require(expected_refs[-1].get('role') == 'secondary_gesture', 'Picture 2 must be the reviewed secondary pose')
    links = {link[0]: link for link in workflow['links']}
    require(len(links) == len(workflow['links']), 'Duplicate link IDs')
    for link in workflow['links']:
        lid, source, output, target, inp, _ = link
        require(source in nodes and target in nodes, 'Broken graph endpoint')
        if source in nodes and target in nodes:
            require(output < len(nodes[source].get('outputs', [])), 'Broken output slot')
            require(inp < len(nodes[target].get('inputs', [])), 'Broken input slot')
            if inp < len(nodes[target].get('inputs', [])):
                require(nodes[target]['inputs'][inp].get('link') == lid, 'Input/link disagreement')
            if output < len(nodes[source].get('outputs', [])):
                require(lid in (nodes[source]['outputs'][output].get('links') or []), 'Output/link disagreement')
    slots = pack.get('slots', [])
    active = {row['slot'] for row in slots}
    require(len(active) == len(slots), 'Duplicate story slots')
    require(active.issubset(set(range(2, 12))), 'Unexpected generated slot')
    table = []
    for row in slots:
        slot = row['slot']; base = slot * 100
        prompt = nodes[base + 12]['widgets_values'][0]
        seconds = nodes[base + 13]['widgets_values'][0]
        speech = row['narration']
        require(row.get('generation_prompt') == prompt, f'Slot {slot}: pack prompt differs from executable prompt')
        # A base-only or single-clip API graph is valid; check every included clip.
        if any(str(base + part) in current_api for part in (12, 13, 17, 21, 35)):
            require_api_value(base + 12, 'value', prompt)
            require_api_value(base + 13, 'value', seconds)
        for brand, cue in (('Anthropic', 'an-thropic'), ('NVIDIA', 'N-vidia')):
            spoken = re.search(r'\b' + re.escape(brand) + r'\b', speech, re.IGNORECASE) is not None
            has_cue = re.search(r'\b' + re.escape(cue) + r'\b', prompt, re.IGNORECASE) is not None
            require(not has_cue or spoken, f'Slot {slot}: unused pronunciation cue for {brand}')
            require(not spoken or has_cue, f'Slot {slot}: missing approved pronunciation cue for {brand}')
        intro = row.get('intro', '')
        require(bool(intro) and speech.startswith(intro), f'Slot {slot}: spoken introduction missing')
        require('"' + speech + '"' in prompt, f'Slot {slot}: narration differs from pack')
        audit = row.get('syllable_audit', [])
        tokens = re.findall(r"[A-Za-z]+(?:['-][A-Za-z]+)*", speech)
        require([x['word'] for x in audit] == tokens, f'Slot {slot}: syllable audit omits/changes words')
        require(all(type(x.get('syllables')) is int and x['syllables'] > 0 for x in audit), f'Slot {slot}: invalid syllables')
        count = sum(x['syllables'] for x in audit)
        require(count == row.get('estimated_syllables'), f'Slot {slot}: syllable total mismatch')
        if count > 0:
            expected = headlines_seconds(count)
            require(seconds == expected == row.get('seconds'), f'Slot {slot}: duration differs from established formula for the complete narration')
        require(nodes[base + 12].get('widgets_values_named', {}).get('value') == prompt, f'Slot {slot}: hidden prompt mismatch')
        require(nodes[base + 13].get('widgets_values_named', {}).get('value') == seconds, f'Slot {slot}: hidden duration mismatch')
        for part in (21, 35):
            save = nodes[base + part]
            require(save['widgets_values'][0] == save.get('widgets_values_named', {}).get('filename_prefix'), f'Slot {slot}: hidden output mismatch')
            if str(base + part) in current_api:
                require_api_value(base + part, 'filename_prefix', save['widgets_values'][0])
        require(nodes[base + 15]['widgets_values'][1:3] == [544, 960], f'Slot {slot}: base size changed')
        require(nodes[base + 21]['mode'] == 0, f'Slot {slot}: base output inactive')
        require(nodes[base + 35]['mode'] == 0, f'Slot {slot}: upscale output must be on (rules file, Rafael 25 Sep 2026)')
        if b2 is not None:
            # The prompt must be Headlines_prompt_for_comfy_json.txt with only its two placeholders filled (plus an optional cue line).
            head_b2, rest = b2.split('<article content>', 1)
            mid_b2, tail_b2 = rest.split('"<article content>"', 1)
            require(prompt.startswith(head_b2) and mid_b2 in prompt and ('"' + speech + '"' + tail_b2) in prompt,
                    f'Slot {slot}: prompt is not Headlines_prompt_for_comfy_json.txt')
        require('guaranteed identical' not in prompt.lower(), f'Slot {slot}: unsupported endpoint guarantee')
        table.append({'slot': slot, 'syllables': count, 'seconds': seconds, 'title': row['title']})
    spectrum = [n for n in nodes.values() if n.get('type') == 'SpectrumApplyMiniMaxH3']
    require(len(spectrum) == 1 and spectrum[0]['mode'] == 0, 'SpectrumApplyMiniMaxH3 node missing or not on')
    for row in slots:
        guider = nodes.get(row['slot'] * 100 + 16, {})
        model_in = [i.get('link') for i in guider.get('inputs', []) if i.get('name') == 'model']
        require(bool(spectrum) and model_in and model_in[0] in (spectrum[0]['outputs'][0].get('links') or []),
                f"Slot {row['slot']}: guider model does not come from the Spectrum node")
    for slot in set(range(1, 13)) - active:
        require(all(n['mode'] == 4 for n in nodes.values() if n['id'] // 100 == slot), f'Slot {slot}: inactive branch not bypassed')
    story_ids = {x.get('story_id') for x in slots if x.get('kind') == 'story'}
    for row in slots:
        if row.get('kind') == 'teaser':
            ids = set(row.get('story_ids', []))
            require(ids.issubset(set(pack.get('card_teaser_story_ids', []))), 'Teaser contains non-teaser card items')
            require(not ids.intersection(story_ids | set(pack.get('card_story_ids', []))), 'Teaser repeats story/card items')
    if schema is not None:
        for nid, key in ((1, 'unet_name'), (2, 'lora_name'), (3, 'clip_name'), (4, 'vae_name'), (5, 'vae_name'), (6, 'image'), (7, 'image'), (8, 'audio'), (29, 'model_name')):
            node = nodes[nid]
            definition = schema.get(node['type'], {}).get('input', {}).get('required', {}).get(key)
            choices = None
            if definition:
                choices = definition[0] if isinstance(definition[0], list) else definition[1].get('options')
            require(choices is not None and node['widgets_values'][0] in choices, f'Node {nid}: required file absent from live backend')
    if errors:
        raise ValueError('\n'.join(errors))
    return {'headlines_json': 'PASS', 'live_assets': 'PASS' if schema is not None else 'UNVERIFIED',
            'slots': table, 'content_box_seconds': sum(x['seconds'] for x in table),
            'rendered_speech_and_picture': 'NOT_TESTED', 'generation_authorized': False}



def check_headlines_clips(workflow, clips_dir, ffprobe='ffprobe', ffmpeg='ffmpeg'):
    """Read-only media inventory from enabled save nodes in the supplied workflow.
    Caller resolves the current Drive workflow/rules first and obtains permission
    for this particular local output directory. No history, queue or JSON writes.
    """
    import subprocess
    from pathlib import PurePosixPath
    root = Path(clips_dir).resolve(strict=True)
    if not root.is_dir():
        raise ValueError('--clips-dir must be an existing directory')
    nodes = workflow.get('nodes', [])
    if len({n['id'] for n in nodes}) != len(nodes):
        raise ValueError('Duplicate workflow node IDs')
    expected = []
    prefix_keys = set()
    for node in nodes:
        nid = node.get('id')
        if type(nid) is not int or not 1 <= nid // 100 <= 12:
            continue
        part = nid % 100
        if part not in (21, 35) or node.get('mode', 0) != 0:
            continue
        values = node.get('widgets_values', [])
        prefix = values[0] if values else None
        if not isinstance(prefix, str) or not prefix.strip():
            raise ValueError(f'Enabled save node {nid} has no filename prefix')
        named = node.get('widgets_values_named', {})
        if 'filename_prefix' in named and named['filename_prefix'] != prefix:
            raise ValueError(f'Save node {nid}: visible and hidden prefixes disagree')
        rel = PurePosixPath(prefix.replace('\\', '/'))
        if rel.is_absolute() or '..' in rel.parts or ':' in prefix:
            raise ValueError(f'Save node {nid}: prefix must stay inside the approved output directory')
        key = str(rel).casefold()
        if key in prefix_keys:
            raise ValueError(f'Duplicate enabled output prefix: {prefix}')
        prefix_keys.add(key)
        dims = [544, 960] if part == 21 else [1088, 1920]
        expected.append({'clip_id': f'C{nid // 100:02d}', 'node_id': nid,
                         'resolution': dims, 'filename_prefix': prefix,
                         'relative_prefix': rel})
    if not expected:
        raise ValueError('No enabled Headlines save nodes found; expected nodes ending in 21/35')
    report = []
    inspected = {}
    for item in sorted(expected, key=lambda x: x['node_id']):
        rel = item.pop('relative_prefix')
        folder = root.joinpath(*rel.parts[:-1]).resolve()
        try:
            folder.relative_to(root)
        except ValueError:
            raise ValueError('Output prefix resolves outside the approved output directory')
        matcher = re.compile(re.escape(rel.name) + r'(?:_[0-9]+_?)?\.mp4$', re.IGNORECASE)
        candidates = sorted((f for f in folder.iterdir() if f.is_file() and matcher.fullmatch(f.name)),
                            key=lambda f: f.name) if folder.is_dir() else []
        results = []
        for path in candidates:
            resolved = path.resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                raise ValueError('Output file resolves outside the approved output directory')
            if resolved not in inspected:
                result = {'path': str(path), 'bytes': path.stat().st_size}
                try:
                    if result['bytes'] <= 48:
                        raise ValueError('Empty or incomplete file (48 bytes or smaller)')
                    probe = subprocess.run(
                        [ffprobe, '-v', 'error', '-show_streams', '-show_format', '-of', 'json', str(path)],
                        capture_output=True, text=True, check=False)
                    if probe.returncode != 0:
                        raise ValueError('ffprobe failed: ' + probe.stderr.strip()[:600])
                    metadata = json.loads(probe.stdout)
                    video = next((s for s in metadata.get('streams', []) if s.get('codec_type') == 'video'), None)
                    audio = [s for s in metadata.get('streams', []) if s.get('codec_type') == 'audio']
                    if not video:
                        raise ValueError('No video stream')
                    result['resolution'] = [video.get('width'), video.get('height')]
                    result['duration_seconds'] = float(video.get('duration') or metadata.get('format', {}).get('duration') or 0)
                    if result['duration_seconds'] <= 0:
                        raise ValueError('No positive video duration')
                    if not audio:
                        raise ValueError('No audio stream in generated speech clip')
                    decode = subprocess.run(
                        [ffmpeg, '-nostdin', '-v', 'error', '-xerror', '-i', str(path),
                         '-map', '0:v:0', '-map', '0:a:0', '-f', 'null', '-'],
                        capture_output=True, text=True, check=False)
                    if decode.returncode != 0 or decode.stderr.strip():
                        raise ValueError('Full decode failed: ' + decode.stderr.strip()[:600])
                    digest = hashlib.sha256()
                    with path.open('rb') as stream:
                        for block in iter(lambda: stream.read(1024 * 1024), b''):
                            digest.update(block)
                    result['sha256'] = digest.hexdigest()
                    result['full_decode'] = 'PASS'
                except (ValueError, OSError) as exc:
                    result['error'] = str(exc)
                    result['full_decode'] = 'FAIL'
                inspected[resolved] = result
            result = dict(inspected[resolved])
            if not result.get('error') and result.get('resolution') != item['resolution']:
                result['error'] = 'Decoded resolution differs from this enabled output'
            result['usable_media'] = not bool(result.get('error'))
            results.append(result)
        valid = [r for r in results if r['usable_media']]
        item['status'] = ('AVAILABLE' if len(valid) == 1 else 'AMBIGUOUS' if len(valid) > 1
                          else 'INVALID' if candidates else 'MISSING')
        item['candidates'] = results
        report.append(item)
    return {
        'clip_inventory': 'PASS' if all(x['status'] == 'AVAILABLE' for x in report) else 'INCOMPLETE',
        'expected_outputs': len(report),
        'expected_clip_ids': sorted({x['clip_id'] for x in report}),
        'available_outputs': sum(x['status'] == 'AVAILABLE' for x in report),
        'missing': [x['clip_id'] + ':' + str(x['resolution'][0]) for x in report if x['status'] == 'MISSING'],
        'invalid': [x['clip_id'] + ':' + str(x['resolution'][0]) for x in report if x['status'] == 'INVALID'],
        'ambiguous': [x['clip_id'] + ':' + str(x['resolution'][0]) for x in report if x['status'] == 'AMBIGUOUS'],
        'outputs': report,
        'scope': 'Enabled outputs only; unrelated files cannot satisfy a missing expected output',
        'story_identity_and_generation_provenance': 'UNVERIFIED - compare existing source manifest and generation record',
        'rendered_speech_and_lip_sync': 'NOT_TESTED',
        'files_written': 0, 'generation_queued': False
    }


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--manifest')
    p.add_argument('--inventory', help='Fresh recursive Drive folder listing keyed by folder ID')
    p.add_argument('--cards-dir')
    p.add_argument('--headlines', help='Read-only Headlines workflow validation')
    p.add_argument('--prompt', help='Local copy of Headlines_prompt_for_comfy_json.txt (prompt check)')
    p.add_argument('--comfy-url', help='Existing local ComfyUI backend for asset/schema checks')
    p.add_argument('--clips-dir', help='Read only the explicitly approved output directory; compare enabled workflow outputs')
    p.add_argument('--ffprobe', default='ffprobe', help='Existing ffprobe executable')
    p.add_argument('--ffmpeg', default='ffmpeg', help='Existing ffmpeg executable')
    args = p.parse_args()
    if args.clips_dir and not args.headlines:
        p.error('--clips-dir requires the current --headlines workflow')
    if args.clips_dir:
        try:
            workflow = json.loads(Path(args.headlines).read_text(encoding='utf-8-sig'))
            result = check_headlines_clips(workflow, args.clips_dir, args.ffprobe, args.ffmpeg)
            print(json.dumps(result, indent=2))
        except (ValueError, KeyError, TypeError, OSError) as exc:
            p.exit(1, 'Clip inventory FAILED: ' + str(exc) + '\n')
        raise SystemExit(0 if result['clip_inventory'] == 'PASS' else 1)
    if args.headlines:
        schema = None
        if args.comfy_url:
            if not re.fullmatch(r'http://(?:127\.0\.0\.1|localhost):[0-9]+', args.comfy_url.rstrip('/')):
                p.error('--comfy-url must identify the local backend')
            with urllib.request.urlopen(args.comfy_url.rstrip('/') + '/object_info', timeout=20) as response:
                schema = json.load(response)
        try:
            print(json.dumps(validate_headlines(json.loads(Path(args.headlines).read_text(encoding='utf-8-sig')), schema,
                                                blueprint_prompt(Path(args.prompt).read_text(encoding='utf-8-sig')) if args.prompt else None), indent=2))
        except (ValueError, KeyError, TypeError) as exc:
            p.exit(1, 'Headlines validation FAILED: ' + str(exc) + '\n')
        raise SystemExit(0)
    if not args.manifest or not args.inventory:
        p.error('Use --headlines, or both --manifest and --inventory')
    print(json.dumps(validate(json.loads(Path(args.manifest).read_text(encoding='utf-8')),
                              json.loads(Path(args.inventory).read_text(encoding='utf-8')), args.cards_dir)))
