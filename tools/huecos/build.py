import json, re, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, '.')
from locate import locate
exec(open('trans.py').read())
R = json.load(open('regions.json'))
FIG = {f['id']: f for f in json.load(open('/home/claude/site/cdsite/src/figuras/figuras.json'))['figuras']}
OBJ = json.load(open('/home/claude/site/cdsite/tools/figuras/objetivos.json'))
META = json.load(open('figmeta.json'))
UNIT = lambda tema: 'u4' if int(tema) <= 13 else 'u5' if int(tema) <= 19 else 'u6'
TOPIC = {'u4': 'U4 · Ciencia de Datos Aplicada', 'u5': 'U5 · Arquitecturas e Ingeniería de Datos', 'u6': 'U6 · Inteligencia Artificial Generativa'}
PAD = 4
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15)
report = []
for fid, spec in T.items():
    reg = R[fid]['regions']; hiW, hiH = R[fid]['W'], R[fid]['H']
    hi = Image.open(f'hi/{fid}.png').convert('RGB')
    revW = min(1600, hiW); s = revW / hiW; revH = round(hiH * s)
    im = hi.resize((revW, revH), Image.LANCZOS)
    blanks = []
    for n, (key, ans) in enumerate(spec.items(), 1):
        level = 'clave'
        if ans.startswith('~'): level, ans = 'extra', ans[1:]
        adj = (0, 0, 0, 0)
        if '@' in key:
            key, a = key.split('@'); adj = tuple(int(v) for v in a.split(','))
        if key.startswith('R:'):
            x0, y0, x1, y1 = (int(v) for v in key[2:].split(','))
        else:
            bs = []
            for part in key.split('+'):
                if '.' in part:
                    r, l = part.split('.'); x, y, w, h = reg[int(r)]['lines'][int(l)]; bs.append((x, y, x + w, y + h))
                else:
                    bs.append(tuple(reg[int(part)]['box']))
            x0 = min(b[0] for b in bs) * s; y0 = min(b[1] for b in bs) * s; x1 = max(b[2] for b in bs) * s; y1 = max(b[3] for b in bs) * s
        x0 -= PAD + adj[0]; y0 -= PAD + adj[1]; x1 += PAD + adj[2]; y1 += PAD + adj[3]
        x0, y0 = max(0, round(x0)), max(0, round(y0)); x1, y1 = min(revW, round(x1)), min(revH, round(y1))
        blanks.append({'id': f'b{n}', 'x': x0, 'y': y0, 'w': x1 - x0, 'h': y1 - y0, 'answer': ans, 'level': level})
    f = FIG[fid]; ref = f['refs'][0]; unit = UNIT(f['tema'])
    _, _, _, cap = locate(*OBJ[f['origen']])
    cap = ' '.join(cap.split())
    name = f'{unit}-{fid}'
    im.save(f'out/{name}.webp', 'WEBP', quality=90)
    cfg = {'title': cap, 'topic': TOPIC[unit], 'order': int(f['tema']) * 100 + f['orden'], 'width': revW, 'height': revH,
           'fuente': f"{ref['corto']}, {ref['nota'].lower()}, pág. {ref['pag']} del PDF · «{ref['archivo']}»",
           'figura': fid, 'origen': 'manual', 'blanks': blanks}
    json.dump(cfg, open(f'out/{name}.json', 'w'), ensure_ascii=False, indent=1)
    # hoja de control: huecos tapados con su respuesta
    c = im.copy(); d = ImageDraw.Draw(c)
    for b in blanks:
        d.rectangle([b['x'], b['y'], b['x'] + b['w'], b['y'] + b['h']], fill=(255, 255, 255), outline=(220, 0, 0) if b['level'] == 'clave' else (0, 120, 220), width=2)
        d.text((b['x'] + 3, b['y'] + 2), b['answer'][:int(b['w'] / 8) + 1], fill=(200, 0, 0), font=font)
    c.save(f'chk/{name}.png')
    report.append((name, len(blanks), cap[:70]))
for r in report: print(*r)
print(len(report), sum(r[1] for r in report))
