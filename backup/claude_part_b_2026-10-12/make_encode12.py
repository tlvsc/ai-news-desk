"""Make final_encode_12oct.py from the approved 11 Oct template (final_encode_11oct_v2.py):
same look; no footage today; C12 gets the clean full-screen "THIS IS NOT FINANCIAL ADVICE" card behind the presenter.
Sources are read from sources_12oct.json so the stitch runs as soon as the outlets are known."""
T = r'E:\Downloads\Claude_temporary_stitching_script_until_merged_to_ChatGPT'
W = r'C:\Users\erans\AppData\Local\Temp\aind_stitch12'
code = open(T + r'\final_encode_11oct_v2.py', encoding='utf-8').read()


def swap(old, new, count=1):
    global code
    assert code.count(old) == count, (old[:70], code.count(old))
    code = code.replace(old, new)


swap('"""11 Oct Headlines final (Claude-V1)', '"""12 Oct Headlines final (Claude-V1, from the approved 11 Oct template; C12 warning card behind the presenter)')
swap("WORK = Path(r'C:\\Users\\erans\\AppData\\Local\\Temp\\aind_stitch11')", "WORK = Path(r'C:\\Users\\erans\\AppData\\Local\\Temp\\aind_stitch12')")
swap("DATE = WORK / 'date_overlay_11-10-26.png'", "DATE = WORK / 'date_overlay_12-10-26.png'")
swap("CARD = Path(r'C:\\Users\\erans\\AppData\\Local\\Temp\\aind_holo\\holo_wall_11oct_overlay.png')", "CARD = WORK / 'holo_wall_12oct_overlay.png'")
swap("OPEN_MATTE = Path(r'C:\\Users\\erans\\AppData\\Local\\Temp\\aind_holo\\matte')", "OPEN_MATTE = Path(r'" + T + r"\opening_matte')")
swap("C09_MATTE = Path(r'C:\\Users\\erans\\AppData\\Local\\Temp\\aind_crab\\matte_c09')                # presenter alpha, C09",
     "C12_MATTE = WORK / 'matte_c12'                                                              # presenter alpha, C12\n"
     "WARN = WORK / 'warning_c12_overlay.png'                                                     # clean warning card")
swap("CRAB_GIF = Path(r'C:\\Users\\erans\\AppData\\Local\\Temp\\aind_crab\\download\\official-jump.gif')  # KingKong Robotics, Apache-2.0\n", "")
swap("CRAB_CREDIT = 'Video: KingKong Robotics (Apache-2.0)'\n", "")
for a, b in (("Headlines_11-10-26_master_audio.wav", "Headlines_12-10-26_master_audio.wav"), ("Headlines_11-10-26_Claude-V1.ass", "Headlines_12-10-26_Claude-V1.ass"),
             ("Headlines_11-10-26_words.json", "Headlines_12-10-26_words.json"),
             ("headlines_11-10-26_VL1.json", "headlines_12-10-26_VL1.json")):
    swap(a, b)
swap("FINAL = Path(r'E:\\Downloads\\Headlines_11-10-26_Claude-V1.mp4')", "FINAL = Path(r'E:\\Downloads\\Headlines_12-10-26_Claude-V1.mp4')")
code = code.replace('Headlines_11-10-26_Claude-V1.srt', 'Headlines_12-10-26_Claude-V1.srt')
swap("    for a, b in (('A I', 'AI'), ('N-vidia', 'NVIDIA'), ('T S M C', 'TSMC'), ('twelve', '12')): t = t.replace(a, b)",
     "    for a, b in (('A I', 'AI'), ('N-vidia', 'NVIDIA'), ('U S', 'US'), ('I M F', 'IMF'), ('the five most', 'the 5 most'),\n"
     "                 ('two top', '2 top'), ('over two hours', 'over 2 hours')): t = t.replace(a, b)")
a = code.index('SOURCES = {'); b = code.index("assert all(SOURCES.values())")
code = code[:a] + "SOURCES = {int(k): v for k, v in json.load(open(WORK / 'sources_12oct.json', encoding='utf-8')).items()}\n" + code[b:]
swap("CLIP_FILES = {9: Path(r'C:\\Users\\erans\\AppData\\Local\\Temp\\aind_stitch11\\fixed\\headlines_11-10-26_C09_VL1_1088_muted_v3.mp4')}",
     "CLIP_FILES = {11: WORK / 'fixed' / 'headlines_12-10-26_C11_VL1_1088_muted_v5.mp4'}")
swap("for c in range(2, 12):", "for c in range(2, 13):")
swap("f = CLIP_FILES.get(c, VIDEO / f'headlines_11-10-26_C{c:02d}_VL1_1088_00001_.mp4')", "f = CLIP_FILES.get(c, VIDEO / f'headlines_12-10-26_C{c:02d}_VL1_1088_00001_.mp4')")
swap("crab = [to_screen(f.copy()) for f in ImageSequence.Iterator(Image.open(CRAB_GIF))]\n", "")
a = code.index("cl = Image.new('RGBA', (1080, 1920)"); b = code.index("def matte(folder, idx):")
code = code[:a] + "warn = np.asarray(Image.open(WARN).convert('RGBA')).astype(np.float32); warn_a = warn[:, :, 3:4] / 255; warn_rgb = warn[:, :, :3]\n" + code[b:]
swap("def crab_alpha(local):\n    return st.smooth_fraction((local - 1.4) / .4) * (1 - st.smooth_fraction((local - 6.8) / .4))",
     "def warn_alpha(local):\n    return st.smooth_fraction((local - .7) / .3) * (1 - st.smooth_fraction((local - 6.1) / .3))")
swap("""    if rows[i]['id'] == 'C09' and crab_alpha(local) > 0:  # C09: crab clip on the whole screen, presenter in front, credit
        k = crab_alpha(local); pha = matte(C09_MATTE, src)
        rgb, al = crab[int((local - 1.4) / 0.08) % len(crab)]
        res = res * (1 - al * k) + rgb * al * k
        res = res * (1 - pha) + orig * pha
        res = res * (1 - credit_a * k) + credit_rgb * credit_a * k""",
     """    if rows[i]['id'] == 'C12' and warn_alpha(local) > 0:  # C12: clean warning card on the whole screen, presenter in front
        k = warn_alpha(local); pha = matte(C12_MATTE, src)
        res = res * (1 - warn_a * k) + warn_rgb * warn_a * k
        res = res * (1 - pha) + orig * pha""")
open(W + r'\final_encode_12oct.py', 'w', encoding='utf-8', newline='\n').write(code)
print('written final_encode_12oct.py')
