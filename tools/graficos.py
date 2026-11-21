"""Genera todos los gráficos de src/graficos/ (PNG + JSON de huecos). Uso: python3 tools/graficos.py

Cada gráfico está redibujado a partir de una figura o una tabla de los libros de la cátedra (carpetas U4, U5 y U6)
o de las notas de clase; la fuente queda escrita al pie de la imagen y en el campo `fuente` del .json.
"""
from graficos_lib import Diagram, top, bottom, left, right, at, SOFT, HEAD, BG, MUTED, LINE, ACCENT, S, font

U4 = 'U4 · Ciencia de Datos Aplicada'
U5 = 'U5 · Arquitecturas e Ingeniería de Datos'
U6 = 'U6 · Inteligencia Artificial Generativa'
total = 0

BRONZE, SILVER, GOLD = '#f2c79a', '#dfe3ea', '#f7dc6f'
GREEN, VIOLET, BLUE, PINK, YELLOW = '#d9f0e1', '#e9ddf7', '#dce8fb', '#f8dfe3', '#fbf1c7'


def done(d):
    global total
    n = d.save()
    total += n
    print(f'{d.file:40} {n:3} huecos')


def ellipse(d, cx, cy, rx, ry, fill, outline=LINE, width=1.5):
    d.d.ellipse([(cx - rx) * S, (cy - ry) * S, (cx + rx) * S, (cy + ry) * S], fill=fill, outline=outline, width=int(width * S))


def poly(d, pts, fill, outline=LINE, width=1.5):
    d.d.polygon([(x * S, y * S) for x, y in pts], fill=fill, outline=outline, width=int(width * S))


def fila(d, x, y, w, h, gap, items, fill=SOFT, size=15):
    """Cajas en fila unidas por flechas. items: (texto, nivel, otras respuestas)."""
    boxes = []
    for i, (txt, lvl, acc) in enumerate(items):
        b = d.box(x + i * (w + gap), y, w, h, txt, size=size, fill=fill, blank=lvl, accept=acc)
        if boxes:
            d.arrow(right(boxes[-1]), left(b))
        boxes.append(b)
    return boxes


# ═══════════════════════════════════════════ U4
d = Diagram('u4-01-pipeline-ml', 'Pipeline de machine learning en cinco pasos', U4, 10, 1040, 250, 'Ozdemir, cap. 1, fig. 1.2 (pág. 6 del PDF) · Notas U4 («agregar gráfico de ML pipeline»)')
for i in range(5):
    d.text(30 + i * 202 + 85, 30, f'Paso {i + 1}', size=14, weight='b', color=MUTED)
bx = fila(d, 30, 50, 170, 92, 32, [
    ('Definir el dominio del problema', 'clave', ['Definir el problema', 'Dominio del problema']),
    ('Obtener datos + EDA', 'clave', ['Obtener datos', 'Obtención de datos', 'Obtener datos y EDA']),
    ('Feature engineering', 'clave', ['Ingeniería de features', 'Ingeniería de características']),
    ('Selección y entrenamiento del modelo', 'clave', ['Selección del modelo y entrenamiento', 'Entrenamiento del modelo']),
    ('Despliegue y evaluación del modelo', 'clave', ['Despliegue y evaluación', 'Deployment y evaluación']),
])
for b in bx[1:]:
    d.line(bottom(b), (bottom(b)[0], 180), color=MUTED)
d.line((bottom(bx[-1])[0], 180), (bottom(bx[1])[0], 180), color=MUTED)
d.arrow((bottom(bx[0])[0], 180), bottom(bx[0]), color=MUTED)
d.line((bottom(bx[1])[0], 180), (bottom(bx[0])[0], 180), color=MUTED)
d.note(30, 205, 'Se vuelve atrás desde cualquier paso. En el paso 5 se vigilan data drift y concept drift (model decay).', size=13)
done(d)

d = Diagram('u4-02-pipeline-fe', 'Pipeline de feature engineering (cuatro pasos)', U4, 20, 1040, 330, 'Ozdemir, cap. 1, fig. 1.5 (pág. 10 del PDF) · Notas U4 («Flujo de feature engineering»)')
stages = [
    ('Comprensión de features', ['Feature understanding', 'Entender los datos', 'Comprensión'], 'Reconocer el nivel de cada dato', ['Niveles de datos', 'Asignar niveles de datos']),
    ('Estructuración de features', ['Feature structuring', 'Estructurar', 'Estructuración'], 'Pasar lo no estructurado a vectores', ['No estructurado a estructurado', 'Extracción o aprendizaje']),
    ('Optimización de features', ['Feature optimization', 'Optimizar', 'Optimización'], 'Mejora, construcción, extracción y selección', ['Mejorar, construir, extraer y seleccionar']),
    ('Evaluación de features', ['Feature evaluation', 'Evaluar', 'Evaluación'], 'Comparar contra un baseline con un modelo fijo', ['Comparar con baseline', 'Comparar contra baseline']),
]
prev = None
for i, (n, acc, desc, dacc) in enumerate(stages):
    x = 30 + i * 252
    d.text(x + 110, 34, f'{i + 1}', size=20, weight='b', color=ACCENT)
    b = d.box(x, 58, 220, 70, n, size=16, fill=HEAD, blank='clave', accept=acc)
    d.box(x, 150, 220, 80, desc, size=14, weight='r', fill=BG, blank='extra', accept=dacc)
    d.line(bottom(b), (bottom(b)[0], 150), color=MUTED)
    if prev:
        d.arrow(right(prev), left(b))
    prev = b
d.arrow((30 + 3 * 252 + 110, 238), (30 + 2 * 252 + 110, 238), via=[(30 + 3 * 252 + 110, 270), (30 + 2 * 252 + 110, 270)], color=ACCENT)
d.note(560, 292, 'Si no se llega al rendimiento buscado, se vuelve a optimizar (o a estructurar).', size=13)
done(d)

d = Diagram('u4-03-tipos-features', 'Tipos de features (clasificación del video MIT)', U4, 30, 1040, 340, 'Video MIT 6.6 «Feature Types» · Notas U4 («Categorias features») · P10 y P24 del 1er parcial')
d.table(20, 20, [220, 400, 380], [
    ['Tipo', 'Qué es', 'Ejemplo'],
    [('Identity features', 'clave', ['Identity', 'Identidad']), 'El dato duro de la entidad, tal como está', ('Edad o género del cliente', 'extra', ['Edad', 'Género', 'País del cliente'])],
    [('Transform features', 'clave', ['Transform', 'Transformación']), 'Se transforma una o más columnas en algo más útil (categorías, partes de una fecha, ratios)', ('Día de la semana de la fecha de compra', 'extra', ['Día de la semana', 'Rango etario'])],
    [('Aggregate features', 'clave', ['Aggregate', 'Agregación', 'Agregadas']), 'Funciones de agregación sobre varios registros (count, sum, mean)', ('Cantidad de compras en los últimos 30 días', 'extra', ['Cantidad de compras', 'Total gastado'])],
], rowh=[44, 70, 80, 80], size=14)
done(d)

d = Diagram('u4-04-model-vs-data', 'Enfoque model-centric vs data-centric', U4, 40, 1040, 340, 'Ozdemir, cap. 1, fig. 1.1 (pág. 3 del PDF) · Notas U4 (tabla y laboratorio Avengers)')
ellipse(d, 120, 160, 95, 75, '#eef4ff')
d.text(120, 160, 'Un problema potencialmente muy complejo', size=14, maxw=150)
t1 = d.box(290, 40, 260, 70, 'Datos mal extraídos o sin trabajar', size=14, fill=SOFT, blank='extra', accept=['Datos mal extraídos', 'Datos pobres'])
t2 = d.box(680, 40, 320, 70, 'Un modelo complejo y lento', size=15, fill=PINK, blank='clave', accept=['Modelo complejo', 'Modelo complejo y lento'])
b1 = d.box(290, 210, 260, 70, 'Datos bien trabajados con feature engineering', size=14, fill=SOFT, blank='extra', accept=['Datos bien trabajados', 'Feature engineering'])
b2 = d.box(680, 210, 320, 70, 'Un modelo más simple, más rápido y con mejores métricas', size=14, fill=GREEN, blank='clave', accept=['Modelo simple', 'Modelo simple y rápido'])
d.arrow((200, 120), left(t1)); d.arrow((200, 200), left(b1))
d.arrow(right(t1), left(t2)); d.arrow(right(b1), left(b2))
d.text(615, 26, 'Model-centric', size=15, weight='b', color=ACCENT, blank='clave', accept=['Centrado en el modelo'])
d.text(615, 300, 'Data-centric', size=15, weight='b', color=ACCENT, blank='clave', accept=['Centrado en los datos'])
done(d)

d = Diagram('u4-05-niveles-datos', 'Los cuatro niveles de datos', U4, 50, 1040, 450, 'Ozdemir, cap. 2, fig. 2.6 y tabla 2.5 (págs. 15–23 del PDF) · Notas U4 («Niveles de datos»)')
d.text(270, 28, 'Cualitativos (categóricos)', size=16, weight='b', blank='clave', accept=['Cualitativos', 'Categóricos'])
d.text(770, 28, 'Cuantitativos (numéricos)', size=16, weight='b', blank='clave', accept=['Cuantitativos', 'Numéricos'])
cells = [
    (30, 'Nominal', 'Categorías sin orden', 'Tipo de sangre, marca de celular', 'Moda, conteos, gráfico de barras; dummificar', ['Moda y conteos', 'One-hot']),
    (530, 'Intervalo', 'Diferencias con sentido, sin cero verdadero', 'Temperatura en °C', 'Suma, resta, media, mediana, desvío', ['Sumar y restar', 'Media y mediana']),
    (30, 'Ordinal', 'Categorías con orden, sin diferencias medibles', 'Satisfacción, notas A/B/C', 'Orden y mediana; enteros 1, 2, 3', ['Orden', 'Enteros crecientes']),
    (530, 'Razón', 'Tiene cero verdadero', 'Dinero, edad, altura', 'Todo lo anterior + multiplicar y dividir', ['Multiplicar y dividir', 'Media geométrica y armónica']),
]
for k, (x, name, que, ej, ops, acc) in enumerate(cells):
    y = 56 if k < 2 else 236
    d.rect(x, y, 480, 165, fill=SOFT if x == 30 else BLUE)
    d.text(x + 240, y + 26, name, size=18, weight='b', blank='clave', accept={'Razón': ['Ratio', 'Razon'], 'Intervalo': ['Interval'], 'Nominal': [], 'Ordinal': []}[name] or None, minw=160)
    d.text(x + 240, y + 62, que, size=14, maxw=440)
    d.text(x + 240, y + 96, 'Ej.: ' + ej, size=14, color=MUTED, maxw=440)
    d.text(x + 240, y + 135, ops, size=14, weight='m', maxw=440, blank='extra', accept=acc)
d.arrow((1015, 60), (1015, 395), color=ACCENT, width=2)
d.text(900, 422, 'Más operaciones permitidas ↓', size=12, color=ACCENT, anchor='mm')
done(d)

d = Diagram('u4-06-tipos-fe', 'Los cinco tipos de feature engineering', U4, 60, 1040, 470, 'Ozdemir, cap. 1, pág. 8 y cap. 2, págs. 24–30 del PDF · Notas U4 («Tipos de ingeniería de características»)')
d.table(20, 20, [190, 410, 400], [
    ['Tipo', 'Qué hace', 'Ejemplo del libro'],
    [('Mejora', 'clave', ['Feature improvement', 'Improvement']), 'Misma variable, mejor preparada: imputar, estandarizar, normalizar', ('Imputar temperaturas faltantes', 'extra', ['Imputar valores faltantes'])],
    [('Construcción', 'clave', ['Feature construction', 'Construction']), 'Crear features nuevas e interpretables con conocimiento del dominio', ('Precio / pies² = precio por pie²', 'extra', ['Precio por pie cuadrado'])],
    [('Selección', 'clave', ['Feature selection', 'Selection']), 'Quedarse con el mejor subconjunto; sacar lo que mete ruido', ('Eliminar las dos columnas originales', 'extra', ['Eliminar columnas que no aportan'])],
    [('Extracción', 'clave', ['Feature extraction', 'Extraction']), 'Algoritmos que crean features asumiendo la forma de los datos', ('PCA, SVD, bag-of-words, BERT', 'extra', ['PCA', 'BERT'])],
    [('Aprendizaje', 'clave', ['Feature learning', 'Learning', 'Representation learning']), 'Deep learning no paramétrico aprende una representación latente', ('GANs, autoencoders', 'extra', ['GANs', 'Autoencoders'])],
], rowh=[44, 66, 66, 66, 66, 66], size=14)
d.note(20, 430, 'Mejora, construcción y selección mantienen la interpretabilidad; extracción y aprendizaje la reducen.', size=13)
done(d)

d = Diagram('u4-07-bloques-lenguaje', 'Bloques del lenguaje y sus aplicaciones', U4, 70, 1000, 450, 'Vajjala, cap. 1, fig. 1-3 (pág. 7 del PDF) · Notas U4 («gráfico blocks of language»)')
blocks = [
    ('Contexto', 'significado', 'Resumen, topic modeling, análisis de sentimiento', '#dce8fb', ['Context', 'Contexto (significado)']),
    ('Sintaxis', 'frases y oraciones', 'Parsing, extracción de entidades y de relaciones', '#d9f0e1', ['Syntax']),
    ('Morfemas y lexemas', 'palabras', 'Tokenización, word embeddings, POS tagging', '#fbe7cf', ['Morfemas', 'Lexemas', 'Morphemes & lexemes']),
    ('Fonemas', 'habla y sonidos', 'Speech-to-text, identificación del hablante, text-to-speech', '#f8dfe3', ['Phonemes']),
]
for i, (n, sub, app, col, acc) in enumerate(blocks):
    y = 30 + i * 88
    x = 60 + (3 - i) * 0
    w = 260 + i * 40
    d.rect(250 - w / 2 + 60, y, w, 74, fill=col)
    d.text(310, y + 26, n, size=17, weight='b', blank='clave', accept=acc, minw=170)
    d.text(310, y + 54, sub, size=13, color=MUTED)
    d.line((310 + w / 2, y + 37), (560, y + 37), color=MUTED)
    d.text(580, y + 37, app, size=14, anchor='lm', maxw=390, blank='extra')
d.text(310, 395, 'Bloques del lenguaje', size=16, weight='b', color=ACCENT)
d.text(760, 395, 'Aplicaciones', size=16, weight='b', color=ACCENT)
done(d)

d = Diagram('u4-08-ia-ml-dl', 'Relación entre IA, ML, DL y NLP', U4, 80, 900, 440, 'Vajjala, cap. 1, fig. 1-8 (pág. 13 del PDF) · Notas U4 («gráfico círculos IA»)')
ellipse(d, 330, 220, 300, 195, '#dce8fb')
ellipse(d, 250, 250, 180, 130, '#d9f0e1')
ellipse(d, 215, 285, 95, 75, '#fbf1c7')
ellipse(d, 470, 230, 150, 120, '#f8dfe3', outline=ACCENT)
d.text(330, 52, 'Inteligencia artificial', size=16, weight='b', blank='clave', accept=['IA', 'AI', 'Inteligencia artificial (IA)'])
d.text(185, 152, 'Machine learning', size=15, weight='b', blank='clave', accept=['ML', 'Aprendizaje automático'])
d.text(205, 290, 'Deep learning', size=15, weight='b', blank='clave', accept=['DL', 'Aprendizaje profundo'])
d.text(520, 230, 'NLP', size=17, weight='b', blank='clave', accept=['Procesamiento del lenguaje natural', 'PLN'])
d.note(650, 120, 'ML está dentro de IA y DL dentro de ML.', size=14, maxw=240)
d.note(650, 150, 'El NLP se superpone con los tres:', size=14)
d.note(650, 174, 'hay NLP con reglas (IA sin ML),', size=14)
d.note(650, 198, 'con ML clásico y con DL.', size=14)
done(d)

d = Diagram('u4-09-pipeline-nlp', 'Pipeline genérico de NLP', U4, 90, 1040, 320, 'Vajjala, cap. 2, fig. 2-1 (pág. 33 del PDF) · Notas U4 («gráfico generic nlp pipeline»)')
top_row = fila(d, 30, 40, 200, 70, 50, [
    ('Adquisición de datos', 'clave', ['Data acquisition', 'Adquisición']),
    ('Limpieza de texto', 'clave', ['Text cleaning', 'Limpieza']),
    ('Preprocesamiento', 'clave', ['Pre-processing', 'Preprocessing']),
    ('Feature engineering', 'clave', ['Ingeniería de features']),
], fill=BLUE)
bot = []
for i, (txt, acc) in enumerate([('Monitoreo y actualización del modelo', ['Monitoreo', 'Monitoring and model updating']), ('Deployment', ['Despliegue']), ('Evaluación', ['Evaluation']), ('Modelado', ['Modeling', 'Modelo'])]):
    bot.append(d.box(30 + i * 250, 190, 200, 70, txt, size=15, fill=BLUE, blank='clave', accept=acc))
d.arrow(bottom(top_row[-1]), top(bot[-1]))
for a, b in zip(bot[::-1], bot[::-1][1:]):
    d.arrow(left(a), right(b))
d.arrow(top(bot[0]), bottom(top_row[0]), dash=True, color=MUTED)
d.note(70, 150, 'mejorar el modelo', size=12)
done(d)

d = Diagram('u4-10-cross-validation', 'Validación cruzada (k = 5) y RMSE', U4, 100, 1040, 360, 'Notas U4 («Cross Validation», «estudiar cross validation y root mean squared error») · ejercicio Surprise (cross_validate, cv=5)')
for r in range(5):
    y = 30 + r * 52
    d.text(60, y + 21, f'Vuelta {r + 1}', size=14, weight='m', color=MUTED)
    for c in range(5):
        val = c == r
        x = 120 + c * 130
        d.rect(x, y, 122, 42, fill='#f7dc6f' if val else BLUE, r=4)
        lab = 'Validación' if val else 'Entrenamiento'
        if r == 0 and c in (0, 1):
            d.text(x + 61, y + 21, lab, size=13, weight='m', blank='clave', accept=['Prueba', 'Test', 'Validacion'] if val else ['Train', 'Training'])
        else:
            d.text(x + 61, y + 21, lab, size=13)
    d.arrow((775, y + 21), (815, y + 21))
    d.text(860, y + 21, f'Error {r + 1}', size=14)
d.text(900, 300, 'Promedio de los 5 errores', size=15, weight='b', blank='clave', accept=['Promedio', 'Media de los errores'])
d.text(120, 320, 'Métrica del ejercicio:', size=14, anchor='lm')
d.text(320, 320, 'RMSE', size=14, weight='b', blank='extra', accept=['Root mean squared error', 'Raíz del error cuadrático medio'], minw=90)
d.text(375, 320, '(raíz del error cuadrático medio; más bajo = mejor)', size=14, anchor='lm')
done(d)

d = Diagram('u4-11-cqrs', 'CQRS: comandos y consultas separados', U4, 110, 1000, 360, 'Strengholt, Data Management at Scale, cap. 4, fig. 4-2 (pág. 6 del PDF)')
d.rect(20, 20, 960, 300, fill=BG, dash=True)
d.text(500, 42, 'Arquitectura de la aplicación', size=16, weight='b')
d.box(80, 70, 840, 46, 'Interfaz', size=15, fill=BLUE)
c = d.box(80, 220, 260, 80, 'Command store (escrituras, actualizaciones y borrados)', size=14, fill=SOFT, blank='clave', accept=['Command store', 'Base de escritura', 'Modelo de comandos'])
q = d.box(660, 220, 260, 80, 'Query model (lecturas)', size=14, fill=SOFT, blank='clave', accept=['Query model', 'Read store', 'Base de lectura', 'Modelo de consultas'])
d.arrow((210, 116), top(c)); d.arrow(top(c), (210, 116))
d.arrow((790, 116), top(q)); d.arrow(top(q), (790, 116))
d.text(255, 168, 'Comandos', size=14, weight='m', blank='clave', accept=['Commands', 'Escrituras'])
d.text(835, 168, 'Consultas', size=14, weight='m', blank='clave', accept=['Queries', 'Lecturas'])
d.arrow(right(c), left(q))
d.text(500, 245, 'Eventos con los cambios (change feed)', size=14, maxw=280, blank='extra', accept=['Change feed', 'Eventos', 'Sincronización por eventos'])
done(d)

# ═══════════════════════════════════════════ U5
d = Diagram('u5-01-ciclo-vida', 'Ciclo de vida de la ingeniería de datos', U5, 10, 1040, 450, 'Reis, cap. 2, fig. 2-1 (pág. 2 del PDF) y cap. 1, fig. 1-1 · P2 y P3 del parcial 2025 · Notas U5')
d.text(560, 24, 'Ciclo de vida de la ingeniería de datos', size=17, weight='b')
g = d.box(30, 105, 150, 70, 'Generación', size=16, fill=PINK, blank='clave', accept=['Generation', 'Generación (sistemas fuente)'])
d.rect(240, 50, 560, 200, fill=BG, width=3)
ing = d.box(260, 70, 160, 60, 'Ingesta', size=15, fill=GREEN, blank='clave', accept=['Ingestion'])
tra = d.box(430, 70, 180, 60, 'Transformación', size=15, fill=VIOLET, blank='clave', accept=['Transformation'])
srv = d.box(620, 70, 160, 60, 'Servicio', size=15, fill=BLUE, blank='clave', accept=['Serving', 'Servir datos', 'Serving data'])
sto = d.box(260, 160, 520, 60, 'Almacenamiento', size=15, fill=SOFT, blank='clave', accept=['Storage'])
d.arrow(right(g), (240, 140))
outs = []
for i, (t, acc) in enumerate([('Analytics', ['Analítica', 'Análisis']), ('Machine learning', ['ML', 'Aprendizaje automático']), ('Reverse ETL', ['ETL inverso'])]):
    b = d.box(850, 50 + i * 72, 170, 56, t, size=15, fill=YELLOW, blank='clave', accept=acc)
    d.arrow((800, 150), left(b))
d.line((20, 285), (1020, 285), width=2)
d.text(520, 305, 'Corrientes subyacentes', size=15, weight='b', blank='extra', accept=['Undercurrents'])
for i, (t, col, acc) in enumerate([('Seguridad', '#e9ddf7', ['Security']), ('Data management', '#dce8fb', ['Gestión de datos']), ('DataOps', '#fbf1c7', []),
                                   ('Arquitectura de datos', '#d9f0e1', ['Data architecture']), ('Orquestación', '#f8dfe3', ['Orchestration']), ('Ingeniería de software', '#fbe7cf', ['Software engineering'])]):
    d.box(30 + i * 165, 330, 150, 64, t, size=14, fill=col, blank='clave', accept=acc or None)
done(d)

d = Diagram('u5-02-piramide', 'Pirámide de necesidades de la ciencia de datos (Rogati)', U5, 20, 1000, 500, 'Reis, cap. 1, fig. 1-5 (pág. 8 del PDF)')
levels = [('Recolectar', 'instrumentación, logs, sensores, datos externos', ['Collect', 'Recolección']),
          ('Mover / almacenar', 'flujo de datos confiable, infraestructura, pipelines, ETL', ['Move/store', 'Mover y almacenar']),
          ('Explorar / transformar', 'limpieza, detección de anomalías, preparación', ['Explore/transform', 'Explorar y transformar']),
          ('Agregar / etiquetar', 'analytics, métricas, segmentos, features, datos de entrenamiento', ['Aggregate/label', 'Agregar y etiquetar']),
          ('Aprender / optimizar', 'A/B testing, experimentación, algoritmos simples de ML', ['Learn/optimize', 'Aprender y optimizar']),
          ('IA, deep learning', '', ['IA', 'Deep learning', 'AI, deep learning'])]
H, base, cx = 62, 410, 330
for i, (n, desc, acc) in enumerate(levels):
    y1, y0 = base - i * H, base - (i + 1) * H
    w1, w0 = 600 - i * 100, 600 - (i + 1) * 100
    poly(d, [(cx - w1 / 2, y1), (cx + w1 / 2, y1), (cx + w0 / 2, y0), (cx - w0 / 2, y0)], fill='#c9d8c5' if i < 3 else '#e8eef6')
    d.text(cx, (y0 + y1) / 2, n, size=14 if i < 5 else 13, weight='b', blank='clave', accept=acc, minw=120)
    if desc:
        d.text(660, (y0 + y1) / 2, desc, size=13, color=MUTED, anchor='lm', maxw=320)
d.line((20, base), (20, base - 3 * H), color=ACCENT, width=3)
d.text(110, base + 30, 'Ingeniería de datos', size=14, weight='b', color=ACCENT, blank='extra', accept=['Data engineering'], minw=170)
d.text(205, base + 30, '← las tres capas de abajo (70–80% del tiempo de un data scientist)', size=13, color=ACCENT, anchor='lm')
done(d)

d = Diagram('u5-03-arq-empresarial', 'Arquitectura empresarial y arquitectura de datos', U5, 30, 1000, 400, 'Reis, cap. 3, fig. 3-1 y 3-2 (págs. 1 y 5 del PDF) · P4 del parcial 2025 · Notas U5 («gráfico enterprise architecture»)')
d.rect(20, 20, 960, 160, fill=SOFT)
d.text(500, 46, 'Arquitectura empresarial', size=17, weight='b', blank='clave', accept=['Enterprise architecture'])
for i, (t, acc) in enumerate([('De negocio', ['Business', 'Negocio']), ('Técnica', ['Technical', 'Tecnológica']), ('De aplicaciones', ['Application', 'Aplicaciones']), ('De datos', ['Data', 'Datos'])]):
    d.box(45 + i * 235, 80, 205, 70, t, size=16, fill='#d9f0e1' if i == 3 else BG, blank='clave', accept=acc)
d.rect(20, 220, 960, 140, fill=BG)
d.text(500, 244, 'Arquitectura de datos', size=16, weight='b')
d.box(80, 270, 360, 70, 'Operacional: qué hay que hacer', size=15, fill=BLUE, blank='clave', answer='Operacional', accept=['Operational', 'Qué'])
d.box(560, 270, 360, 70, 'Técnica: cómo se hace', size=15, fill=BLUE, blank='clave', answer='Técnica', accept=['Technical', 'Cómo'])
d.arrow((852, 150), (852, 220), color=MUTED)
done(d)

d = Diagram('u5-04-lambda-kappa', 'Arquitecturas Lambda y Kappa', U5, 40, 1040, 440, 'Reis, cap. 3, fig. 3-14 y 3-15 (págs. 29–30 del PDF)')
d.text(70, 30, 'Lambda', size=18, weight='b', color=ACCENT, blank='clave', accept=[])
src = d.box(30, 105, 150, 64, 'Fuentes', size=15)
bt = d.box(270, 60, 200, 56, 'Procesamiento batch', size=15, fill=YELLOW, blank='clave', accept=['Batch', 'Batch processing'])
st = d.box(270, 160, 200, 56, 'Procesamiento stream', size=15, fill=GREEN, blank='clave', accept=['Stream', 'Streaming', 'Stream processing'])
sv = d.box(560, 90, 220, 96, 'Capa de servicio (batch query + stream query)', size=14, fill=BLUE, blank='clave', answer='Capa de servicio', accept=['Serving', 'Serving layer'])
qq = d.box(860, 113, 150, 50, 'Consultas', size=15)
d.arrow(right(src), left(bt)); d.arrow(right(src), left(st)); d.arrow(right(bt), (560, 110)); d.arrow(right(st), (560, 166)); d.arrow(right(sv), left(qq))
d.note(30, 245, 'Dos caminos en paralelo; problema: mantener dos bases de código.', size=13)
d.line((20, 270), (1020, 270), dash=True, color=MUTED)
d.text(70, 300, 'Kappa', size=18, weight='b', color=ACCENT, blank='clave', accept=[])
k = fila(d, 30, 330, 200, 60, 60, [('Fuente de streaming', None, None), ('Procesamiento stream', 'clave', ['Stream', 'Streaming']), ('Capa de servicio', None, None), ('Consultas', None, None)], fill=GREEN)
d.note(560, 300, 'Todo pasa por una plataforma de streaming.', size=13)
done(d)

d = Diagram('u5-05-mesh-principios', 'Los cuatro principios de Data Mesh y cómo se compensan', U5, 50, 1000, 470, 'Dehghani, cap. 1, fig. 1-2 (págs. 48–54 del PDF) · P7 del parcial 2025')
do = d.box(40, 40, 280, 80, 'Propiedad del dominio (domain ownership)', size=15, fill=BLUE, blank='clave', accept=['Domain ownership', 'Propiedad del dominio', 'Propiedad por dominio'])
dp = d.box(680, 40, 280, 80, 'Datos como producto (data as a product)', size=15, fill=YELLOW, blank='clave', accept=['Data as a product', 'Datos como producto'])
fg = d.box(40, 330, 280, 80, 'Gobierno computacional federado', size=15, fill=PINK, blank='clave', accept=['Federated computational governance', 'Gobierno federado'])
sp = d.box(680, 330, 280, 80, 'Plataforma de datos self-serve', size=15, fill=GREEN, blank='clave', accept=['Self-serve data platform', 'Plataforma self-serve', 'Plataforma de autoservicio'])
d.arrow(right(do), left(dp))
d.text(500, 60, 'Evita los silos de datos', size=14, blank='extra', accept=['Silos', 'Prevenir silos'])
d.arrow(at(do, 0.8, 1), at(sp, 0.2, 0))
d.text(530, 200, 'Baja el costo y el esfuerzo duplicado', size=14, maxw=240, blank='extra', accept=['Costo', 'Reduce el costo de propiedad'])
d.arrow(bottom(do), top(fg))
d.text(205, 225, 'Evita la incompatibilidad entre dominios', size=14, anchor='lm', maxw=230, blank='extra', accept=['Incompatibilidad', 'Interoperabilidad'])
d.arrow(right(fg), left(sp), dash=True, color=MUTED)
d.text(500, 390, 'Políticas automatizadas por la plataforma', size=13, color=MUTED)
done(d)

d = Diagram('u5-06-mesh-cambios', 'Las seis dimensiones de cambio de Data Mesh', U5, 60, 1040, 470, 'Dehghani, cap. 1, fig. 1-1 (págs. 45–47 del PDF) · P6 del parcial 2025')
d.table(20, 20, [200, 380, 420], [
    ['Cambio', 'De (antes)', 'A (data mesh)'],
    [('Organizacional', 'clave', ['Organizationally', 'Organizativo']), 'Propiedad centralizada en especialistas', ('Propiedad descentralizada en los dominios de negocio', 'extra', ['Descentralizada', 'Dominios'])],
    [('Arquitectónico', 'clave', ['Architecturally', 'Arquitectural']), 'Warehouses y lakes monolíticos', ('Malla distribuida de data products', 'extra', ['Malla distribuida', 'Distribuida'])],
    [('Tecnológico', 'clave', ['Technologically']), 'Datos como subproducto del código', ('Datos y código como una unidad autónoma', 'extra', ['Una unidad', 'Datos y código juntos'])],
    [('Operacional', 'clave', ['Operationally', 'Operativo']), 'Gobierno top-down centralizado', ('Gobierno federado con políticas computacionales', 'extra', ['Federado', 'Gobierno federado'])],
    [('De principios', 'clave', ['Principally', 'Principios', 'De valores']), 'Datos como activo a recolectar', ('Datos como producto para servir', 'extra', ['Datos como producto'])],
    [('De infraestructura', 'clave', ['Infrastructurally', 'Infraestructura']), 'Dos infraestructuras fragmentadas', ('Infraestructura integrada operacional y analítica', 'extra', ['Integrada', 'Infraestructura integrada'])],
], rowh=[44, 62, 62, 62, 62, 62, 62], size=14)
done(d)

d = Diagram('u5-07-medallion', 'Arquitectura Medallion: Bronze, Silver y Gold', U5, 70, 1040, 430, 'Strengholt, Building Medallion Architectures, cap. 1 (págs. 3–4) y cap. 3, fig. 3-1 y tabla 3-1 (págs. 40–73 del PDF) · P8 del parcial 2025 · Notas U5')
srcs = d.box(20, 60, 120, 200, 'Fuentes (OLTP, ERP, CRM)', size=14)
land = d.box(160, 60, 120, 200, 'Landing zone', size=14, fill=BG, dash=True, blank='extra', accept=['Landing', 'Staging', 'Zona de aterrizaje'])
d.arrow(right(srcs), left(land))
cols = [('Bronze', BRONZE, 'Datos crudos, en su estructura original e inmutables', ['Bronce']),
        ('Silver', SILVER, 'Datos limpios, estandarizados, deduplicados y validados', ['Plata']),
        ('Gold', GOLD, 'Datos agregados con lógica de negocio, listos para consumir', ['Oro'])]
prev = land
for i, (n, col, desc, acc) in enumerate(cols):
    x = 305 + i * 200
    d.rect(x, 60, 180, 200, fill=col)
    d.text(x + 90, 86, n, size=18, weight='b', blank='clave', accept=acc, minw=120)
    d.text(x + 90, 170, desc, size=14, maxw=165, blank='extra')
    d.arrow((prev[0] + prev[2], 160), (x, 160))
    prev = (x, 60, 180, 200)
cons = d.box(905, 60, 115, 200, 'Consumidores (BI, ML, IA)', size=14)
d.arrow((prev[0] + prev[2], 160), left(cons))
d.text(560, 290, 'Mejora incremental de la estructura y la calidad →', size=15, weight='m', color=ACCENT)
d.table(20, 320, [160, 300, 280, 260], [
    ['', 'Bronze', 'Silver', 'Gold'],
    ['Modelo de datos', 'Esquema del sistema fuente', ('3FN o Data Vault', 'extra', ['3NF', 'Data Vault', 'Orientado a temas']), ('Kimball (estrella) u OBT', 'extra', ['Kimball', 'Esquema estrella', 'One big table'])],
], rowh=[36, 50], size=13)
done(d)

# ═══════════════════════════════════════════ U6
d = Diagram('u6-01-codigo-workflow-agente', 'Código tradicional, workflow o agente autónomo', U6, 10, 1040, 330, 'Albada, cap. 1, tabla 1-2 (pág. 12 del PDF)')
d.table(20, 20, [220, 250, 260, 270], [
    ['Característica', ('Código tradicional', 'clave', ['Código', 'Traditional code']), ('Workflow', 'clave', ['Flujo de trabajo']), ('Agente autónomo', 'clave', ['Agente', 'Autonomous agent'])],
    ['Estructura del input', 'Totalmente predecible', 'Mayormente predecible, ramas finitas', ('Muy no estructurado o novedoso', 'extra', ['No estructurado', 'Novedoso'])],
    ['Explicabilidad', ('Total, auditable', 'extra', ['Total']), 'Auditoría rama por rama', 'Caja negra'],
    ['Latencia', 'Ultra baja', 'Moderada', ('Mayor', 'extra', ['Alta'])],
    ['Adaptabilidad', 'Nula', 'Limitada', ('Alta: aprende del feedback', 'extra', ['Alta'])],
], rowh=[50, 60, 54, 48, 54], size=14)
d.note(20, 300, 'Entre workflow y agente está el chatbot o RAG: responde sobre documentos pero no decide acciones.', size=13)
done(d)

d = Diagram('u6-02-componentes-agente', 'Componentes centrales de un sistema de agentes', U6, 20, 1020, 360, 'Albada, cap. 2, fig. 2-1 (págs. 20–27 del PDF)')
u = d.box(30, 140, 130, 70, 'Usuario', size=15)
o = d.box(250, 135, 200, 80, 'Orquestación', size=16, fill=BLUE, blank='clave', accept=['Orchestration', 'Orquestador'])
d.arrow(right(u), left(o))
comps = [('Modelo', 'elige y decide', ['Model', 'Modelo fundacional', 'LLM']), ('Herramientas', 'locales, API o MCP', ['Tools']),
         ('Memoria', 'corto y largo plazo', ['Memory']), ('Base de conocimiento', 'información del dominio', ['Knowledge base'])]
for i, (n, sub, acc) in enumerate(comps):
    b = d.box(560, 25 + i * 80, 220, 62, n, size=15, fill=SOFT, blank='clave', accept=acc)
    d.arrow(right(o), left(b))
    d.text(800, 25 + i * 80 + 31, sub, size=13, color=MUTED, anchor='lm', blank='extra')
done(d)

d = Diagram('u6-03-rag-pipelines', 'Un sistema RAG: indexing pipeline y generation pipeline', U6, 30, 1040, 450, 'Kimothi, cap. 2, fig. 2.1, 2.2, 2.3 y 2.5 (págs. 2–9 del PDF) · P10 del parcial 2025')
d.text(20, 26, 'Indexing pipeline (offline, va primero)', size=16, weight='b', anchor='lm', blank='clave', answer='Indexing pipeline', accept=['Pipeline de indexación', 'Indexación'])
idx = fila(d, 20, 50, 175, 70, 26, [
    ('Fuentes externas', None, None),
    ('Carga: conectar, extraer y parsear', 'clave', ['Carga de datos', 'Data loading', 'Carga']),
    ('Splitting (chunking)', 'clave', ['Chunking', 'Splitting', 'División en chunks']),
    ('Conversión a embeddings', 'clave', ['Embeddings', 'Conversión']),
    ('Base vectorial', 'clave', ['Vector DB', 'Vector database', 'Base de datos vectorial', 'Almacenamiento']),
], fill=GREEN, size=14)
d.text(20, 190, 'Generation pipeline (tiempo real)', size=16, weight='b', anchor='lm', blank='clave', answer='Generation pipeline', accept=['Pipeline de generación', 'Generación'])
gen = fila(d, 20, 215, 175, 70, 26, [
    ('Pregunta del usuario', None, None),
    ('Retriever', 'clave', ['Recuperador', 'Retrieval']),
    ('Prompt: pregunta + contexto recuperado', 'clave', ['Aumentación', 'Prompt management', 'Gestión del prompt']),
    ('LLM', 'clave', ['Modelo de lenguaje', 'LLM setup']),
    ('Respuesta con contexto', None, None),
], fill=BLUE, size=14)
d.arrow(bottom(idx[-1]), top(gen[1]), via=[(bottom(idx[-1])[0], 160), (top(gen[1])[0], 160)], dash=True, color=ACCENT)
d.text(560, 148, 'busca en la base de conocimiento', size=12, color=ACCENT)
d.note(20, 320, 'Componentes de soporte: evaluación, monitoreo, caching (caché semántica), guardrails, seguridad y una capa de orquestación.', size=13)
d.note(20, 345, 'Los cinco pasos: pregunta → búsqueda → recuperación y aumentación → LLM → respuesta.', size=13)
done(d)

d = Diagram('u6-04-triada-rag', 'Tríada de evaluación RAG (TruEra)', U6, 40, 960, 440, 'Kimothi, cap. 2, fig. 2.7 (págs. 9–10 del PDF)')
qx, qy, rx, ry, cx2, cy2 = 480, 70, 170, 330, 790, 330
poly(d, [(qx, qy), (cx2, cy2), (rx, ry)], fill='#f6f8fc', outline='#c96a6a')
d.box(qx - 110, qy - 45, 220, 50, 'Consulta (prompt)', size=15, fill=BLUE, blank='clave', accept=['Query', 'Pregunta', 'Consulta'])
d.box(cx2 - 110, cy2 + 5, 220, 50, 'Contexto recuperado', size=15, fill=GREEN, blank='clave', accept=['Context', 'Contexto'])
d.box(rx - 110, ry + 5, 220, 50, 'Respuesta', size=15, fill=YELLOW, blank='clave', accept=['Answer', 'Response'])
d.text(790, 180, 'Context relevance', size=15, weight='b', blank='clave', accept=['Relevancia del contexto'])
d.text(790, 210, '¿lo recuperado es relevante para la consulta?', size=12, color=MUTED, maxw=200)
d.text(180, 180, 'Answer relevance', size=15, weight='b', blank='clave', accept=['Relevancia de la respuesta'])
d.text(180, 206, '¿la respuesta contesta la consulta?', size=12, color=MUTED, maxw=200)
d.text(480, 360, 'Groundedness', size=15, weight='b', blank='clave', accept=['Fidelidad', 'Faithfulness'])
d.text(480, 386, '¿la respuesta es fiel al contexto?', size=12, color=MUTED)
done(d)

d = Diagram('u6-05-memoria', 'Jerarquía de información de un agente (Huyen)', U6, 50, 960, 400, 'Huyen, AI Engineering, cap. 6, fig. 6-16 (págs. 48–51 del PDF)')
ext = d.box(560, 30, 200, 70, 'Memoria externa', size=15, fill=BLUE)
ret = d.box(580, 140, 160, 50, 'Retriever', size=15, fill=SOFT, blank='extra', accept=['Recuperador'])
mod = d.box(580, 225, 160, 56, 'Modelo', size=16, fill=HEAD)
trn = d.box(560, 310, 200, 60, 'Datos de entrenamiento', size=14, fill=SOFT)
ctx = d.box(320, 228, 150, 50, 'Contexto', size=15, fill=YELLOW)
d.arrow(bottom(ext), top(ret)); d.arrow(bottom(ret), top(mod)); d.arrow(right(ctx), left(mod)); d.arrow(top(trn), bottom(mod))
d.text(860, 65, 'Memoria de largo plazo', size=15, weight='b', maxw=180, blank='clave', accept=['Largo plazo', 'Long-term memory'])
d.text(170, 253, 'Memoria de corto plazo', size=15, weight='b', maxw=200, blank='clave', accept=['Corto plazo', 'Short-term memory'])
d.text(860, 340, 'Conocimiento interno', size=15, weight='b', maxw=180, blank='clave', accept=['Internal knowledge', 'Conocimiento del modelo'])
d.note(30, 60, 'Información poco usada → memoria externa', size=13)
d.note(30, 360, 'Información esencial para muchas tareas → se entrena', size=13)
done(d)

d = Diagram('u6-06-tipos-ia', 'Los cuatro tipos de IA (Nika)', U6, 60, 960, 480, 'Nika, cap. 1, fig. 1-1 (págs. 2–5 del PDF)')
ellipse(d, 420, 220, 400, 200, '#f8dfe3')
ellipse(d, 360, 235, 300, 160, '#fbf1c7')
ellipse(d, 300, 250, 200, 120, '#d9f0e1')
ellipse(d, 230, 265, 110, 75, '#dce8fb')
d.text(720, 220, 'ASI', size=18, weight='b', blank='clave', accept=['Superinteligencia', 'Artificial superintelligence'])
d.text(720, 248, '¿~2040s? Supera a los humanos', size=12, color=MUTED, maxw=130)
d.text(560, 235, 'AGI', size=18, weight='b', blank='clave', accept=['Inteligencia general', 'Artificial general intelligence'])
d.text(560, 263, '¿2030s?', size=12, color=MUTED)
d.text(390, 200, 'IA tradicional', size=16, weight='b', blank='clave', accept=['Traditional AI', 'Tradicional'])
d.text(390, 226, '1950s–hoy', size=12, color=MUTED)
d.text(230, 255, 'IA generativa', size=15, weight='b', blank='clave', accept=['GenAI', 'Generativa', 'IA generativa (GenAI)'])
d.text(230, 280, 'fines 2010s–hoy', size=12, color=MUTED)
d.note(20, 445, 'La figura del libro dibuja GenAI dentro de la IA tradicional, ambas dentro de AGI y ASI.', size=13)
done(d)

print('total de huecos:', total)
