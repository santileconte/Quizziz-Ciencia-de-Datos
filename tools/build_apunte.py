"""Genera src/mapas/apunte.json y src/mapas/mapas.json.

El apunte sale de contenido_apunte.py y los mapas de contenido_mapas.py. Cada concepto de un mapa cita
bloques del apunte por etiqueta ('ml.def', o 'arq.tabla:2' para la fila 2 de una tabla); acá se
traducen a ids ('s01.3', 's03.2:2') y se corta con error si alguna etiqueta no existe.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from contenido_apunte import SECCIONES  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), '..', 'src', 'mapas')


def limpio(t):
    t = re.sub(r'`([^`]*)`', r'\1', t)
    return re.sub(r'(?<!\*)\*(?!\*)([^*]+)\*(?!\*)', r'\1', t)


etiquetas = {}
secciones = []
for n, s in enumerate(SECCIONES, 1):
    sid = f's{n:02d}'
    blocks = []
    for k, b in enumerate(s['bloques'], 1):
        tipo, cuerpo = b[0], b[1]
        bid = f'{sid}.{k}'
        if len(b) > 2:
            etiquetas[f"{s['clave']}.{b[2]}"] = bid
        if tipo == 'table':
            blocks.append({'id': bid, 't': 'table', 'rows': [[limpio(c) for c in r] for r in cuerpo], 'head': True})
        else:
            blocks.append({'id': bid, 't': tipo, 'text': limpio(cuerpo)})
    secciones.append({'id': sid, 'clave': s['clave'], 'unit': s['unit'], 'title': s['title'], 'src': s['src'], 'orig': s['orig'], 'blocks': blocks})

json.dump(secciones, open(os.path.join(OUT, 'apunte.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('secciones', len(secciones), 'bloques', sum(len(s['blocks']) for s in secciones))

try:
    from contenido_mapas import MAPAS  # noqa: E402
except ImportError:
    MAPAS = []


def ref(label, donde):
    base, _, fila = label.partition(':')
    if base not in etiquetas:
        raise SystemExit(f'Etiqueta inexistente {label!r} en {donde}')
    return etiquetas[base] + (f':{fila}' if fila else '')


mapas, cuenta = [], {}
for m in MAPAS:
    cuenta[m['unit']] = cuenta.get(m['unit'], 0) + 1

    def rama(r):
        label, hojas = r
        return {'label': label, 'leaves': [{'term': t, 'text': x, 'refs': [ref(e, f"{m['id']}/{label}/{t}") for e in rs.split()]} for t, x, rs in hojas]}

    mapas.append({'id': m['id'], 'unit': m['unit'], 'num': f"{cuenta[m['unit']]:02d}", 'title': m['title'], 'subtitle': m['subtitle'],
                  'kicker': m['kicker'], 'center': m['center'], 'recordar': m['recordar'],
                  'left': [rama(r) for r in m['left']], 'right': [rama(r) for r in m['right']]})
json.dump(mapas, open(os.path.join(OUT, 'mapas.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mapas', len(mapas), 'conceptos', sum(len(b['leaves']) for m in mapas for b in m['left'] + m['right']))
usados = {r.split(':')[0] for m in mapas for b in m['left'] + m['right'] for l in b['leaves'] for r in l['refs']}
sin = [s['clave'] for s in secciones if not any(b['id'] in usados for b in s['blocks'])]
print('secciones sin mapa:', sin)
