"""Cut the presenter out of the opening (frames 0-5.2 s) with Robust Video Matting; saves one alpha PNG per frame.
The opening never changes, so this matte is reused every day."""
import sys, os, time
R = r'C:\Users\erans\Documents\Codex\2026-09-11\check-if-complete-finishes-it-generation'
sys.path[:0] = [R + r'\video_runtime', R + r'\asr_runtime']
import numpy as np, av, onnxruntime as ort
from PIL import Image
SRC = r'C:\Users\erans\AppData\Local\Temp\aind_drive\AIND_opening_option4_2026-10-03_VL1_1088_FROM_DRIVE.mp4'
MODEL = r'C:\Users\erans\AppData\Local\Temp\aind_rvm\model\rvm_mobilenetv3_fp32.onnx'
OUT = r'C:\Users\erans\AppData\Local\Temp\aind_holo\matte'
os.makedirs(OUT, exist_ok=True)
sess = ort.InferenceSession(MODEL, providers=['CPUExecutionProvider'])
rec = [np.zeros([1, 1, 1, 1], np.float32)] * 4
ratio = np.array([0.25], np.float32)
t0 = time.time()
with av.open(SRC) as c:
    fps = float(c.streams.video[0].average_rate)
    for i, f in enumerate(c.decode(video=0)):
        if i / fps > 5.2:
            break
        a = f.to_ndarray(format='rgb24')[:, 4:1084]               # same 1080 crop as the stitch
        src = (a.astype(np.float32) / 255).transpose(2, 0, 1)[None]
        fgr, pha, *rec = sess.run(None, {'src': src, 'r1i': rec[0], 'r2i': rec[1], 'r3i': rec[2], 'r4i': rec[3], 'downsample_ratio': ratio})
        Image.fromarray((pha[0, 0] * 255).round().astype(np.uint8)).save(os.path.join(OUT, f'pha_{i:04d}.png'))
        if i % 20 == 0:
            print(i, f'{time.time() - t0:.1f}s', flush=True)
print('done', i, 'frames')
