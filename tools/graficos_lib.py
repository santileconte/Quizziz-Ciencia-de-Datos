"""Dibuja los gráficos de src/graficos/ (PNG) y su archivo de huecos (JSON) a partir de una descripción.

Cada texto marcado como hueco queda registrado con la posición exacta en la que se dibujó, así el .json
siempre coincide con la imagen. Requiere Pillow y la tipografía Inter (o DejaVu Sans como reemplazo).
"""
import json
import math
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(__file__), '..', 'src', 'graficos')

FONT_DIRS = ['/usr/share/fonts/opentype/inter', '/usr/share/fonts/truetype/inter', '/usr/share/fonts/truetype/dejavu']
FONTS = {
    'r': ['Inter-Regular.otf', 'Inter-Regular.ttf', 'DejaVuSans.ttf'],
    'm': ['Inter-Medium.otf', 'Inter-Medium.ttf', 'DejaVuSans.ttf'],
    'b': ['Inter-SemiBold.otf', 'Inter-SemiBold.ttf', 'DejaVuSans-Bold.ttf'],
    'i': ['Inter-Italic.otf', 'Inter-Italic.ttf', 'DejaVuSans-Oblique.ttf'],
}
_cache = {}


def font(weight='r', size=17):
    key = (weight, size)
    if key not in _cache:
        for d in FONT_DIRS:
            for f in FONTS[weight]:
                p = os.path.join(d, f)
                if os.path.exists(p):
                    _cache[key] = ImageFont.truetype(p, size)
                    break
            if key in _cache:
                break
        else:
            _cache[key] = ImageFont.load_default()
    return _cache[key]


INK = '#16181d'
MUTED = '#5c6470'
LINE = '#2a2f38'
SOFT = '#eef1f6'
HEAD = '#dfe5f1'
BG = '#ffffff'
ACCENT = '#2b3bf0'
S = 2  # se dibuja al doble y se reduce, para que las líneas queden suaves


class Diagram:
    def __init__(self, file, title, topic, order, w, h, fuente=''):
        self.file, self.title, self.topic, self.order, self.w, self.h = file, title, topic, order, w, h
        self.fuente = fuente
        self.im = Image.new('RGB', (w * S, h * S), BG)
        self.d = ImageDraw.Draw(self.im)
        self.blanks = []

    # ---------- texto
    def wrap(self, text, f, maxw):
        out = []
        for para in text.split('\n'):
            words, cur = para.split(' '), ''
            for wd in words:
                t = (cur + ' ' + wd).strip()
                if cur and f.getlength(t) > maxw:
                    out.append(cur)
                    cur = wd
                else:
                    cur = t
            out.append(cur)
        return out

    def text(self, x, y, text, size=17, weight='r', color=INK, anchor='mm', maxw=None, blank=None, accept=None, pad=(8, 5), answer=None, minw=0, bg=None):
        """Texto centrado en (x, y) salvo que `anchor` empiece con 'l' (alineado a la izquierda desde x)."""
        f = font(weight, size * S)
        lines = self.wrap(text, f, maxw * S) if maxw else text.split('\n')
        lh = int(size * 1.28 * S)
        tw = max(f.getlength(l) for l in lines)
        th = lh * len(lines)
        x0 = x * S if anchor[0] == 'l' else x * S - tw / 2
        y0 = y * S - th / 2
        if bg:
            bw = max(tw / S + 2 * pad[0], minw)
            bx = x0 / S - pad[0] if anchor[0] == 'l' else x - bw / 2
            self.d.rectangle([bx * S, (y0 / S - pad[1]) * S, (bx + bw) * S, (y0 / S + th / S + pad[1]) * S], fill=bg)
        for i, l in enumerate(lines):
            lx = x0 if anchor[0] == 'l' else x * S - f.getlength(l) / 2
            self.d.text((lx, y0 + i * lh + lh / 2), l, font=f, fill=color, anchor='lm')
        box = [x0 / S - pad[0], y0 / S - pad[1], tw / S + 2 * pad[0], th / S + 2 * pad[1]]
        if box[2] < minw:
            box[0] -= (minw - box[2]) / 2 if anchor[0] != 'l' else 0
            box[2] = minw
        if blank:
            self.blank(box, answer or text.replace('\n', ' '), blank, accept)
        return box

    def blank(self, box, answer, level='clave', accept=None):
        x, y, w, h = box
        x, y = max(1, x), max(1, y)
        b = {'id': f'b{len(self.blanks) + 1}', 'x': round(x), 'y': round(y), 'w': round(min(w, self.w - x - 1)), 'h': round(max(h, 28)), 'answer': answer, 'level': level}
        if accept:
            b['accept'] = accept
        self.blanks.append(b)

    # ---------- formas
    def rect(self, x, y, w, h, fill=SOFT, outline=LINE, width=1.5, r=8, dash=False):
        if dash:
            self.d.rounded_rectangle([x * S, y * S, (x + w) * S, (y + h) * S], r * S, fill=fill)
            for a, b in (((x, y), (x + w, y)), ((x + w, y), (x + w, y + h)), ((x + w, y + h), (x, y + h)), ((x, y + h), (x, y))):
                self.line(a, b, color=outline, width=width, dash=True)
        else:
            self.d.rounded_rectangle([x * S, y * S, (x + w) * S, (y + h) * S], r * S, fill=fill, outline=outline, width=int(width * S))

    def box(self, x, y, w, h, text, size=16, weight='m', fill=SOFT, blank=None, accept=None, r=8, color=INK, outline=LINE, answer=None, dash=False):
        """Caja con texto centrado. Si es hueco, el hueco ocupa el interior de la caja."""
        self.rect(x, y, w, h, fill=fill, outline=outline, r=r, dash=dash)
        self.text(x + w / 2, y + h / 2, text, size=size, weight=weight, color=color, maxw=w - 14)
        if blank:
            self.blank([x + 4, y + 4, w - 8, h - 8], answer or text.replace('\n', ' '), blank, accept)
        return (x, y, w, h)

    def line(self, a, b, color=LINE, width=1.5, dash=False):
        (x1, y1), (x2, y2) = a, b
        if not dash:
            self.d.line([x1 * S, y1 * S, x2 * S, y2 * S], fill=color, width=int(width * S))
            return
        L = math.hypot(x2 - x1, y2 - y1)
        n = max(1, int(L / 9))
        for i in range(n):
            t0, t1 = i / n, (i + 0.55) / n
            self.d.line([(x1 + (x2 - x1) * t0) * S, (y1 + (y2 - y1) * t0) * S, (x1 + (x2 - x1) * t1) * S, (y1 + (y2 - y1) * t1) * S], fill=color, width=int(width * S))

    def arrow(self, a, b, head='open', tail=None, color=LINE, width=1.5, dash=False, via=None):
        """Flecha de a hacia b. head: open (asociación / flujo), tri (herencia), none. tail: diamond (agregación)."""
        pts = [a] + (via or []) + [b]
        ang = math.atan2(pts[-1][1] - pts[-2][1], pts[-1][0] - pts[-2][0])
        end = pts[-1]
        if head == 'tri':
            end = (b[0] - 13 * math.cos(ang), b[1] - 13 * math.sin(ang))
        start = pts[0]
        if tail == 'diamond':
            a0 = math.atan2(pts[1][1] - pts[0][1], pts[1][0] - pts[0][0])
            start = (a[0] + 18 * math.cos(a0), a[1] + 18 * math.sin(a0))
            mid = (a[0] + 9 * math.cos(a0), a[1] + 9 * math.sin(a0))
            px, py = -math.sin(a0) * 5.5, math.cos(a0) * 5.5
            self.d.polygon([(a[0] * S, a[1] * S), ((mid[0] + px) * S, (mid[1] + py) * S), (start[0] * S, start[1] * S), ((mid[0] - px) * S, (mid[1] - py) * S)], fill=BG, outline=color, width=int(width * S))
        seq = [start] + pts[1:-1] + [end]
        for p, q in zip(seq, seq[1:]):
            self.line(p, q, color=color, width=width, dash=dash)
        if head == 'open':
            for da in (2.6, -2.6):
                self.line(b, (b[0] + 11 * math.cos(ang + da), b[1] + 11 * math.sin(ang + da)), color=color, width=width)
        elif head == 'tri':
            px, py = -math.sin(ang) * 7.5, math.cos(ang) * 7.5
            self.d.polygon([(b[0] * S, b[1] * S), ((end[0] + px) * S, (end[1] + py) * S), ((end[0] - px) * S, (end[1] - py) * S)], fill=BG, outline=color, width=int(width * S))

    def gear(self, x, y, color=LINE):
        """Ícono de actividad (dos engranajes)."""
        for cx in (x - 11, x + 11):
            for k in range(8):
                a = k * math.pi / 4
                self.line((cx + 7 * math.cos(a), y + 7 * math.sin(a)), (cx + 12 * math.cos(a), y + 12 * math.sin(a)), color=color, width=3)
            self.d.ellipse([(cx - 8) * S, (y - 8) * S, (cx + 8) * S, (y + 8) * S], outline=color, width=int(1.5 * S), fill=BG)
            self.d.ellipse([(cx - 3) * S, (y - 3) * S, (cx + 3) * S, (y + 3) * S], fill=color)

    # ---------- compuestos
    def table(self, x, y, colw, rows, rowh=None, head=True, size=15, first_col_head=True):
        """Tabla. Cada celda es un texto o una tupla (texto, nivel[, otras respuestas]) que la vuelve hueco."""
        rowh = rowh or [44] * len(rows)
        cy = y
        for r, row in enumerate(rows):
            cx = x
            for c, cell in enumerate(row):
                txt, lvl, acc = (cell, None, None) if isinstance(cell, str) else (cell + (None,))[:3]
                is_head = (head and r == 0) or (first_col_head and c == 0)
                fill = HEAD if (head and r == 0) else (SOFT if is_head else BG)
                self.rect(cx, cy, colw[c], rowh[r], fill=fill, r=0, width=1)
                if txt:
                    self.text(cx + colw[c] / 2, cy + rowh[r] / 2, txt, size=size, weight='b' if is_head else 'r', maxw=colw[c] - 18)
                    if lvl:
                        self.blank([cx + 5, cy + 5, colw[c] - 10, rowh[r] - 10], txt.replace('\n', ' '), lvl, acc)
                cx += colw[c]
            cy += rowh[r]
        return cy

    def note(self, x, y, text, size=13, maxw=None, anchor='lm'):
        self.text(x, y, text, size=size, color=MUTED, anchor=anchor, maxw=maxw)

    def save(self):
        os.makedirs(OUT, exist_ok=True)
        if self.fuente:
            self.text(12, self.h - 13, 'Basado en: ' + self.fuente, size=11, color='#8a919c', anchor='lm')
        self.im.resize((self.w, self.h), Image.LANCZOS).save(os.path.join(OUT, self.file + '.png'), optimize=True)
        cfg = {'title': self.title, 'topic': self.topic, 'order': self.order, 'width': self.w, 'height': self.h, 'fuente': self.fuente, 'blanks': self.blanks}
        with open(os.path.join(OUT, self.file + '.json'), 'w', encoding='utf-8') as fh:
            fh.write(json.dumps(cfg, ensure_ascii=False, indent=2) + '\n')
        return len(self.blanks)


# anclas de cajas (x, y, w, h)
def top(b): return (b[0] + b[2] / 2, b[1])
def bottom(b): return (b[0] + b[2] / 2, b[1] + b[3])
def left(b): return (b[0], b[1] + b[3] / 2)
def right(b): return (b[0] + b[2], b[1] + b[3] / 2)
def at(b, fx, fy): return (b[0] + b[2] * fx, b[1] + b[3] * fy)
