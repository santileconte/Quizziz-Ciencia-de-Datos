"""Genera src/figuras/figuras.json, src/figuras/img/*.webp y src/figuras/thumb/*.webp.

Las figuras se recortaron de los PDF de las carpetas Unidad 4, 5 y 6 con tools/figuras/extraer.py (PyMuPDF):
se busca el epígrafe «Figure X-Y» en la página y se recorta la imagen que está justo encima.
Uso: python3 tools/figuras/build_figuras.py <carpeta con los PNG recortados>
"""
import json, os, sys
from PIL import Image

SRC = sys.argv[1]
ROOT = os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'figuras')

A = {
    'zheng': ('[Caps 1 y 3 OBLIGATORIOS] Zheng - Feature Engineering for ML.pdf', 'Zheng'),
    'ozd': ('[OBLIGATORIO] Ozdemir - Feature Engineering Bookcamp.pdf', 'Ozdemir'),
    'str': ('[OBLIGATORIO] Strengholt - Data Management at Scale - Chapter 4. Data Product Management.pdf', 'Strengholt DMS'),
    'vaj': ('[OBLIGATORIO] Vajjala - Practical NLP.pdf', 'Vajjala'),
    'reis1': ('[OBLIGATORIO] Reis - Fundamentals of Data Engineering. Chapter 1.pdf', 'Reis cap. 1'),
    'reis2': ('[OBLIGATORIO] Reis - Fundamentals of Data Engineering. Chapter 2.pdf', 'Reis cap. 2'),
    'reis3': ('[OBLIGATORIO] Reis - Fundamentals of Data Engineering. Chapter 3.pdf', 'Reis cap. 3'),
    'dm': ('[OBLIGATORIO CAP 1] Data Mesh Delivering Data-Driven Value at Scale (Dehghani, Zhamak).pdf', 'Dehghani'),
    'med': ('[OBLIGATORIO] Strengholt - Building Medallion Architectures.pdf', 'Medallion'),
    'alb': ('[OBLIGATORIO CAP 1 y 2] Michael Albada - Building Applications with AI Agents.pdf', 'Albada'),
    'kim': ('[OBLIGATORIO] Kimothi - A Simple Guide to Retrieval Augmented Generation.pdf', 'Kimothi'),
    'huy': ('[OBLIGATORIO] AI_Engineering_Chapter_6_RAG_and_Agents.pdf', 'Huyen'),
    'nika': ('[OBLIGATORIO] Nika - Chapter 1. The Role of AI Product Managers 2.pdf', 'Nika'),
}

# (png, tema, rank, libro, pág. del PDF, número de figura, título)
# rank: 1 ligada a una consigna real · 2 pedida en clase · 3 figura central del libro · 4 complementaria
F = [
    ('u4_zheng_1-2', '02', 3, 'zheng', 4, 'Figura 1-2', 'El lugar del feature engineering en el flujo de ML'),
    ('u4_ozd_1-2', '04', 2, 'ozd', 6, 'Figura 1.2', 'Pipeline de ML en cinco pasos'),
    ('u4_ozd_1-1', '04', 3, 'ozd', 3, 'Figura 1.1', 'Enfoque model-centric vs data-centric'),
    ('u4_ozd_1-5', '04', 3, 'ozd', 10, 'Figura 1.5', 'Pipeline de feature engineering: comprensión, estructuración, optimización y evaluación'),
    ('u4_ozd_2-13', '04', 3, 'ozd', 33, 'Figura 2.13', 'Enfoque del libro para el feature engineering'),
    ('u4_ozd_1-3', '04', 4, 'ozd', 7, 'Figura 1.3', 'Datos crudos (texto, imágenes) transformados en vectores'),
    ('u4_ozd_2-6', '06', 3, 'ozd', 23, 'Figura 2.6', 'Los cuatro niveles de datos'),
    ('u4_ozd_2-2', '06', 3, 'ozd', 17, 'Figura 2.2', 'Features dummy (one-hot) a partir de una feature nominal'),
    ('u4_ozd_2-5', '06', 4, 'ozd', 21, 'Figura 2.5', 'Medias aritmética, geométrica y armónica'),
    ('u4_zheng_3-1', '08', 3, 'zheng', 41, 'Figura 3-1', 'Texto crudo convertido en un vector bag-of-words'),
    ('u4_vaj_1-2', '09', 2, 'vaj', 6, 'Figura 1-2', 'Tareas de NLP de fácil a difícil'),
    ('u4_vaj_1-3', '09', 2, 'vaj', 7, 'Figura 1-3', 'Bloques del lenguaje y sus aplicaciones'),
    ('u4_vaj_1-8', '09', 2, 'vaj', 13, 'Figura 1-8', 'Relación entre IA, ML, DL y NLP'),
    ('u4_vaj_1-11', '09', 2, 'vaj', 18, 'Figura 1-11', 'SVM: límite de decisión con el mayor margen'),
    ('u4_vaj_1-13', '09', 2, 'vaj', 20, 'Figura 1-13', 'Red neuronal recurrente (RNN) desenrollada'),
    ('u4_vaj_1-14', '09', 2, 'vaj', 21, 'Figura 1-14', 'Celda LSTM'),
    ('u4_vaj_1-1', '09', 3, 'vaj', 3, 'Figura 1-1', 'Tareas y aplicaciones de NLP'),
    ('u4_vaj_2-1', '10', 2, 'vaj', 33, 'Figura 2-1', 'Pipeline genérico de NLP'),
    ('u4_vaj_2-7', '10', 3, 'vaj', 49, 'Figura 2-7', 'Stemming vs lematización'),
    ('u4_vaj_2-8', '10', 4, 'vaj', 51, 'Figura 2-8', 'Pasos comunes de preprocesamiento'),
    ('u4_vaj_4-3', '11', 4, 'vaj', 113, 'Figura 4-3', 'Pipeline de clasificación de texto'),
    ('u4_str_4-1', '13', 1, 'str', 3, 'Figura 4-1', 'Vista de datos y vista tecnológica separadas'),
    ('u4_str_4-2', '13', 3, 'str', 6, 'Figura 4-2', 'CQRS: comandos y consultas separados'),
    ('u4_str_4-3', '13', 3, 'str', 7, 'Figura 4-3', 'Colaboración descentralizada entre proveedores y consumidores'),
    ('u4_str_4-5', '13', 4, 'str', 17, 'Figura 4-5', 'Arquitectura de un data product'),
    ('u5_reis_1-5', '14', 3, 'reis1', 8, 'Figura 1-5', 'Pirámide de necesidades de la ciencia de datos'),
    ('u5_reis_1-8', '14', 3, 'reis1', 10, 'Figura 1-8', 'Modelo de madurez de datos'),
    ('u5_reis_1-12', '14', 4, 'reis1', 19, 'Figura 1-12', 'Stakeholders técnicos de la ingeniería de datos'),
    ('u5_reis_2-1', '15', 1, 'reis2', 2, 'Figura 2-1', 'Ciclo de vida de la ingeniería de datos y sus corrientes subyacentes'),
    ('u5_reis_2-2', '15', 3, 'reis2', 3, 'Figura 2-2', 'El ciclo de la ingeniería de datos dentro del ciclo de vida del dato'),
    ('u5_reis_2-5', '15', 3, 'reis2', 12, 'Figura 2-5', 'Tipos de analytics'),
    ('u5_reis_2-6', '15', 3, 'reis2', 15, 'Figura 2-6', 'Reverse ETL'),
    ('u5_reis_2-8', '15', 3, 'reis2', 25, 'Figura 2-8', 'Los tres pilares de DataOps'),
    ('u5_reis_3-1', '16', 1, 'reis3', 1, 'Figura 3-1', 'La arquitectura de datos, subconjunto de la empresarial'),
    ('u5_reis_3-2', '16', 3, 'reis3', 5, 'Figura 3-2', 'Arquitectura de datos operacional y técnica'),
    ('u5_reis_3-10', '17', 3, 'reis3', 25, 'Figura 3-10', 'Data warehouse básico con ETL'),
    ('u5_reis_3-11', '17', 3, 'reis3', 25, 'Figura 3-11', 'ELT'),
    ('u5_reis_3-12', '17', 3, 'reis3', 26, 'Figura 3-12', 'ETL o ELT con data marts'),
    ('u5_reis_3-14', '17', 3, 'reis3', 29, 'Figura 3-14', 'Arquitectura Lambda'),
    ('u5_reis_3-15', '17', 3, 'reis3', 30, 'Figura 3-15', 'Arquitectura Kappa'),
    ('u5_med_1-4', '17', 3, 'med', 9, 'Figura 1-4', 'Enfoque de Inmon (top-down)'),
    ('u5_med_1-5', '17', 3, 'med', 10, 'Figura 1-5', 'Metodología de Kimball (bottom-up)'),
    ('u5_med_1-8', '17', 3, 'med', 22, 'Figura 1-8', 'Arquitectura lakehouse'),
    ('u5_reis_3-13', '17', 4, 'reis3', 28, 'Figura 3-13', 'Modern data stack'),
    ('u5_med_1-6', '17', 4, 'med', 13, 'Figura 1-6', 'Data lake típico (Hadoop)'),
    ('u5_dm_1-1', '18', 1, 'dm', 47, 'Figura 1-1', 'Dimensiones de cambio de Data Mesh'),
    ('u5_dm_1-2', '18', 1, 'dm', 54, 'Figura 1-2', 'Los cuatro principios de Data Mesh y su interacción'),
    ('u5_dm_1-3', '18', 3, 'dm', 56, 'Figura 1-3', 'Modelo operativo de Data Mesh'),
    ('u5_reis_3-18', '18', 4, 'reis3', 33, 'Figura 3-18', 'Ejemplo simplificado de data mesh'),
    ('u5_med_3-1', '19', 1, 'med', 40, 'Figura 3-1', 'Las tres capas de la arquitectura Medallion'),
    ('u5_med_1-2', '19', 1, 'med', 4, 'Figura 1-2', 'La arquitectura Medallion en la capa de distribución'),
    ('u5_med_1-1', '19', 3, 'med', 2, 'Figura 1-1', 'Diseño de tres capas: proveedores, distribución y consumidores'),
    ('u6_alb_2-1', '22', 3, 'alb', 21, 'Figura 2-1', 'Componentes centrales de un sistema de agentes'),
    ('u6_kim_2-3', '23', 1, 'kim', 6, 'Figura 2.3', 'Indexing pipeline y generation pipeline'),
    ('u6_kim_2-7', '23', 3, 'kim', 10, 'Figura 2.7', 'Tríada de evaluación RAG'),
    ('u6_kim_2-4', '23', 4, 'kim', 6, 'Figura 2.4', 'Componentes de un sistema RAG productivo'),
    ('u6_huy_6-2', '24', 3, 'huy', 4, 'Figura 6-2', 'Arquitectura RAG básica'),
    ('u6_huy_6-3', '24', 3, 'huy', 9, 'Figura 6-3', 'Retriever basado en embeddings'),
    ('u6_huy_6-12', '25', 3, 'huy', 42, 'Figura 6-12', 'Un agente ReAct en acción'),
    ('u6_huy_6-16', '25', 3, 'huy', 50, 'Figura 6-16', 'Jerarquía de información de un agente'),
    ('u6_huy_6-9', '25', 4, 'huy', 31, 'Figura 6-9', 'Planificación desacoplada de la ejecución'),
    ('u6_nika_1-1', '26', 3, 'nika', 3, 'Figura 1-1', 'Los cuatro tipos de IA'),
    ('u6_nika_1-4', '26', 4, 'nika', 13, 'Figura 1-4', 'Skill set del AI PM'),
]
NIVEL = {1: 'Consigna real', 2: 'Pedida en clase', 3: 'Libro obligatorio', 4: 'Complementaria'}
NOTA = {
    'u5_reis_2-1': 'P2 y P3 del parcial 2025 (etapas; batch vs streaming). Las notas piden el «gráfico de ciclo de vida del dato».',
    'u5_reis_3-1': 'P4 del parcial 2025 (arquitectura de negocios vs de datos). Las notas piden el «gráfico enterprise architecture».',
    'u5_dm_1-1': 'P6 del parcial 2025 (cambios de Data Mesh).',
    'u5_dm_1-2': 'P7 del parcial 2025 (principios de Data Mesh).',
    'u5_med_3-1': 'P8 del parcial 2025 (qué va en cada capa). Las notas piden el «gráfico que tiene la medallion arquitectura».',
    'u5_med_1-2': 'P8 del parcial 2025.',
    'u6_kim_2-3': 'P10 del parcial 2025 (embeddings en RAG).',
    'u4_str_4-1': 'P8 del 1er parcial que entra ahora (data as a product vs data product).',
    'u4_ozd_1-2': 'Las notas dicen «*agregar gráfico de ML pipeline».',
    'u4_vaj_1-2': 'Las notas piden el «gráfico flecha de easy a hard».',
    'u4_vaj_1-3': 'Las notas piden el «gráfico blocks of language y sus aplicaciones».',
    'u4_vaj_1-8': 'Las notas piden el «gráfico círculos IA».',
    'u4_vaj_2-1': 'Las notas piden el «gráfico generic nlp pipeline».',
    'u4_vaj_1-11': 'Las notas: «Enfoque ML: Support Vector Machine – *gráfico flujo».',
    'u4_vaj_1-13': 'Las notas: «saber concepto RRN y cómo se relaciona con LSTM».',
    'u4_vaj_1-14': 'Las notas: «saber concepto RRN y cómo se relaciona con LSTM».',
}

os.makedirs(os.path.join(ROOT, 'img'), exist_ok=True)
os.makedirs(os.path.join(ROOT, 'thumb'), exist_ok=True)
figuras, cuenta = [], {}
for png, tema, rank, libro, pag, num, titulo in sorted(F, key=lambda x: (x[1], x[2])):
    cuenta[tema] = cuenta.get(tema, 0) + 1
    fid = f'f{tema}-{cuenta[tema]:02d}'
    im = Image.open(os.path.join(SRC, png + '.png')).convert('RGB')
    im.save(os.path.join(ROOT, 'img', fid + '.webp'), 'WEBP', quality=88)
    th = im.copy(); th.thumbnail((360, 260)); th.save(os.path.join(ROOT, 'thumb', fid + '.webp'), 'WEBP', quality=80)
    archivo, corto = A[libro]
    figuras.append({'id': fid, 'tema': tema, 'orden': cuenta[tema], 'rank': rank, 'nivel': NIVEL[rank], 'title': titulo,
                    'w': im.width, 'h': im.height, 'refs': [{'archivo': archivo, 'corto': corto, 'pag': pag, 'nota': num}],
                    'mostrada': f'{corto}, {num.lower()}, pág. {pag} del PDF', 'tipo': 'Figura del libro', 'nota': NOTA.get(png), 'legib': None,
                    'origen': png})
json.dump({'figuras': figuras, 'tambien': {'19': ['f17-08'], '15': [], '23': ['f24-01']}}, open(os.path.join(ROOT, 'figuras.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(figuras), 'figuras')
for f in figuras: print(f['id'], f['origen'])
