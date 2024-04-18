
import ddddocr
1
det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)

with open('images/bg.jpg', 'rb') as f:
    target_bytes = f.read()

with open('images/tp.png', 'rb') as f:
    background_bytes = f.read()
res = det.slide_match(target_bytes, background_bytes, simple_target=True)
x = int(res['target'][0] * (300 / 320))
print(res)
print(x)

