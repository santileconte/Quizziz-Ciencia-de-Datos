import json, glob, os, sys
from PIL import Image, ImageDraw, ImageFont
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 17)
only = set(sys.argv[1:])
rows = []
for p in sorted(glob.glob('out/*.json')):
    n = os.path.basename(p)[:-5]
    if only and n not in only:
        continue
    c = json.load(open(p)); im = Image.open(f'out/{n}.webp').convert('RGB')
    for i, b in enumerate(c['blanks'], 1):
        cr = im.crop((b['x'], b['y'], b['x'] + b['w'], b['y'] + b['h']))
        if cr.width > 700: cr = cr.resize((700, max(1, int(cr.height * 700 / cr.width))))
        if cr.height > 160: cr = cr.resize((max(1, int(cr.width * 160 / cr.height)), 160))
        rows.append((f'{n} #{i}', b['answer'], cr))
k = 0; W = 1500
os.makedirs('ver', exist_ok=True)
while rows:
    batch, h = [], 0
    while rows and h + max(rows[0][2].height, 70) + 8 < 1900:
        r = rows.pop(0); batch.append(r); h += max(r[2].height, 70) + 8
    S = Image.new('RGB', (W, h + 200), 'white'); d = ImageDraw.Draw(S); y = 0
    for lab, ans, cr in batch:
        S.paste(cr, (0, y)); d.text((720, y), lab, fill=(0, 0, 200), font=font)
        line = ''; yy = y + 20
        for w in ans.split(' '):
            if len(line) + len(w) > 60: d.text((720, yy), line, fill=(180, 0, 0), font=font); yy += 20; line = ''
            line += w + ' '
        d.text((720, yy), line, fill=(180, 0, 0), font=font)
        y += max(cr.height, yy - y + 22) + 8
        d.line([(0, y - 4), (W, y - 4)], fill=(220, 220, 220))
    S = S.crop((0, 0, W, y)); S.save(f'ver/{k:02d}.png'); k += 1
print(k)
