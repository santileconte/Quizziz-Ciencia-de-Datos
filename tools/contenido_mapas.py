"""Mapas mentales (src/mapas/mapas.json). Uno por tema del temario (algunos agrupan dos temas).

Cada concepto es (término, texto corto, etiquetas del apunte separadas por espacio).
Las etiquetas se definen en contenido_apunte.py; build_apunte.py falla si alguna no existe.
"""

MAPAS = []


def M(id, unit, title, subtitle, kicker, center, recordar, left, right):
    MAPAS.append(dict(id=id, unit=unit, title=title, subtitle=subtitle, kicker=kicker, center=center, recordar=recordar, left=left, right=right))


# ═══════════ U4
M('u4-ml', 'u4', 'Machine learning y modelado predictivo', 'Qué es un modelo, supervisado vs no supervisado', 'ML', 'Predecir y actuar',
  'Clustering = no supervisado. La matemática no entra.',
  [('Modelado predictivo', [('Tres pasos', 'Predecir un resultado futuro, entrenar con observaciones, actuar.', 'ml.predictivo'),
                            ('Modelo', 'Artefacto de software: se llama, se reentrena y se replica.', 'ml.modelo'),
                            ('Ventanas', 'Unas para entrenar y otra para probar y medir.', 'ml.ventanas')]),
   ('Features', [('Qué son', 'Las columnas que entrenan al modelo.', 'ml.features'),
                 ('Dónde se buscan', 'En Silver o Gold de un Medallion.', 'ml.mle')])],
  [('Supervisado', [('Datos', 'Etiquetados: features + respuesta correcta.', 'ml.sup:1'),
                    ('Tareas', 'Clasificación y regresión.', 'ml.sup:3')]),
   ('No supervisado', [('Datos', 'Sin etiquetas: el modelo propone la estructura.', 'ml.sup:1 ml.sup:4'),
                       ('Tareas', 'Clustering y reducción de dimensionalidad.', 'ml.sup:3 ml.clustering')]),
   ('Para el parcial', [('Sin matemática', 'Qué es, para qué sirve y cómo se relaciona.', 'ml.mate')])])

M('u4-fe', 'u4', 'Feature engineering', 'Definiciones, tipos de features, enfoques, pipelines y drift', 'FEATURES', 'Datos → features → modelo',
  'Feature = representación numérica de datos crudos. Tipos MIT: identity, transform, aggregate.',
  [('Definiciones', [('Feature', 'Representación numérica de datos crudos; propiedad medible.', 'fe.def'),
                     ('FE según Zheng', 'Formular las features más apropiadas dados datos, modelo y tarea.', 'fe.defe'),
                     ('FE según Ozdemir', 'Transformar datos para representar el problema y mitigar sesgos.', 'fe.defe'),
                     ('Doble articulación', 'Features y modelo se eligen juntos.', 'fe.doble')]),
   ('Tipos de features (MIT)', [('Identity', 'El dato duro: edad, género.', 'fe.tipos:1'),
                                ('Transform', 'Categorías o partes de una fecha.', 'fe.tipos:2'),
                                ('Aggregate', 'Count, sum: compras en 30 días.', 'fe.tipos:3')]),
   ('Datos según Zheng', [('Problemas', 'Incorrectos, redundantes o faltantes.', 'fe.datos')])],
  [('Model vs data-centric', [('Model-centric', 'Cambiar algoritmo, hiperparámetros, complejidad.', 'mvd.tabla'),
                              ('Data-centric', 'Mejorar la representación y reducir ruido.', 'mvd.tabla mvd.clase'),
                              ('Lab Avengers', 'threat_per_hero; heridos al final = fuga de datos.', 'mvd.lab'),
                              ('Límites', 'No crea señal ni reemplaza datos.', 'mvd.limites')]),
   ('Pipelines', [('ML (5 pasos)', 'Dominio, datos, FE, modelo, despliegue.', 'mvd.pipeline'),
                  ('FE (4 pasos)', 'Comprender, estructurar, optimizar, evaluar.', 'mvd.pipfe')]),
   ('Drift', [('Data drift', 'Cambia la distribución.', 'mvd.drift:1'),
              ('Concept drift', 'Cambia la relación feature-objetivo.', 'mvd.drift:1'),
              ('Quién', 'MLOps.', 'mvd.mlops')])])

M('u4-niveles', 'u4', 'Niveles de datos y tipos de feature engineering', 'Qué se puede hacer con cada dato y cómo se transforma', 'NIVELES', 'Nominal → razón',
  'Si el cociente tiene sentido es razón. Mejora, construcción y selección son interpretables; extracción y aprendizaje no.',
  [('Estructurados o no', [('Estructurados', 'Filas y columnas, ~20%.', 'niveles.estruct'),
                           ('No estructurados', 'Texto, audio, video, ~80%.', 'niveles.estruct')]),
   ('Cualitativos', [('Nominal', 'Sin orden; moda; dummificar.', 'niveles.tabla:1'),
                     ('Ordinal', 'Con orden; enteros crecientes.', 'niveles.tabla:2')]),
   ('Cuantitativos', [('Intervalo', 'Sin cero verdadero; sumar y restar.', 'niveles.tabla:3'),
                      ('Razón', 'Cero verdadero; dividir y multiplicar.', 'niveles.tabla:4 niveles.truco'),
                      ('Medias', 'Aritmética, geométrica y armónica.', 'niveles.medias')])],
  [('Tipos de FE', [('Mejora', 'Imputar, estandarizar, normalizar.', 'tiposfe.tabla:1'),
                    ('Construcción', 'Features nuevas con conocimiento del dominio.', 'tiposfe.tabla:2'),
                    ('Selección', 'El mejor subconjunto.', 'tiposfe.tabla:3'),
                    ('Extracción', 'PCA, SVD, BERT: asume la forma de los datos.', 'tiposfe.tabla:4'),
                    ('Aprendizaje', 'GANs, autoencoders: representación latente.', 'tiposfe.tabla:5')]),
   ('Evaluar', [('Métricas de ML', 'Contra un baseline.', 'tiposfe.m1'),
                ('Interpretabilidad', 'Poder preguntar por qué.', 'tiposfe.m2'),
                ('Fairness', 'Sesgos de los datos.', 'tiposfe.m3'),
                ('Velocidad', 'Listo para producción.', 'tiposfe.m4')])])

M('u4-texto', 'u4', 'Texto como features', 'Bag-of-words, n-gramas y filtrado (Zheng, cap. 3)', 'TEXTO', 'Texto → vector plano',
  'BoW pierde el orden; n-gramas lo conservan a costa de espacio.',
  [('Representar', [('Bag-of-words', 'Vector plano de conteos.', 'texto.bow'),
                    ('Bag-of-n-grams', 'Secuencias de n tokens; más ralo.', 'texto.ngram')]),
   ('Atomizar', [('Tokenización', 'Cortar el string en tokens.', 'texto.token'),
                 ('Colocaciones', 'Frases con significado propio.', 'texto.coloc')])],
  [('Filtrar', [('Stopwords', 'Palabras vacías.', 'texto.filtro'),
                ('Frecuentes y raras', 'Garbage bin para las raras.', 'texto.filtro'),
                ('Stemming', 'Reduce a la raíz; new y news.', 'texto.stem')])])

M('u4-nlp', 'u4', 'NLP', 'Tareas, bloques del lenguaje, enfoques y pipeline (Vajjala, caps. 1–4)', 'NLP', 'Lenguaje → máquina',
  'Gráficos de clase: fácil→difícil, bloques del lenguaje, círculos IA/ML/DL, pipeline genérico.',
  [('Qué resuelve', [('Tres niveles', 'Core tasks, generales e industry specific.', 'nlp.que'),
                     ('Fácil a difícil', 'De spell checking a agente de dominio abierto.', 'nlp.dificultad'),
                     ('Por qué es difícil', 'Ambigüedad, sentido común, creatividad.', 'nlp.dificil')]),
   ('Bloques del lenguaje', [('Fonemas', 'Speech-to-text.', 'nlp.bloques:1'),
                             ('Morfemas y lexemas', 'Tokenización, POS.', 'nlp.bloques:2'),
                             ('Sintaxis', 'Parsing.', 'nlp.bloques:3'),
                             ('Contexto', 'Resumen, sentimiento.', 'nlp.bloques:4')]),
   ('Enfoques', [('Reglas', 'WordNet, regex.', 'nlp.reglas'),
                 ('ML clásico', 'Naive Bayes, SVM.', 'nlp.mlc'),
                 ('RNN y LSTM', 'LSTM recuerda contexto largo.', 'nlp.dl')])],
  [('Pipeline', [('Etapas', 'Adquisición … monitoreo.', 'pipnlp.etapas'),
                 ('Preprocesamiento', 'Tokenizar, stopwords, stemming.', 'pipnlp.pre'),
                 ('Stemming vs lematización', 'Recortar vs forma real.', 'pipnlp.tecnicas:1 pipnlp.tecnicas:2'),
                 ('POS, parsing, correferencia', 'Análisis más profundo.', 'pipnlp.tecnicas:3 pipnlp.tecnicas:5')]),
   ('Representación', [('TF-IDF', 'Frecuente en el doc, raro en el corpus.', 'repr.basica'),
                       ('Embeddings', 'CBOW y SkipGram.', 'repr.emb'),
                       ('Clasificación', 'Etiquetas → features → entrenar.', 'repr.clasif')])])

M('u4-recom', 'u4', 'Sistemas de recomendación', 'Filtrado colaborativo, active learning, cross validation y RMSE', 'RECOM', 'Encontrar sin pedir',
  'Cross validation: rotar la ventana de validación. RMSE: más bajo = mejor.',
  [('Modelos', [('Baseline', 'Predicción aleatoria.', 'recom.modelos:1'),
                ('Usuario-usuario', 'Gustos parecidos.', 'recom.modelos:2'),
                ('Ítem-ítem', 'Ítems parecidos.', 'recom.modelos:3')]),
   ('Active learning', [('Humano en el bucle', 'Un oráculo que corrige.', 'recom.active')])],
  [('Evaluar', [('Cross validation', 'k folds rotando la validación.', 'recom.cv'),
                ('RMSE', 'Raíz del error cuadrático medio.', 'recom.rmse')])])

M('u4-dp', 'u4', 'Data products', 'Strengholt, Data Management at Scale, cap. 4', 'DATA PRODUCT', 'Datos listos para consumir',
  'Data as a product = mindset. Data product = arquitectura. Sigue la filosofía CQRS.',
  [('Dos conceptos', [('Data as a product', 'Forma de pensar.', 'dp.vs:1'),
                      ('Data product', 'Arquitectura.', 'dp.vs:1'),
                      ('Visiones', 'Dehghani (quantum) y Accenture.', 'dp.visiones')]),
   ('Definición lógica', [('Entidad lógica', 'Describe datos para consumo.', 'dp.logica'),
                          ('Por qué no contenedor', 'La metadata se duplicaría.', 'dp.contenedor')])],
  [('CQRS', [('Separa', 'Comandos y consultas.', 'dp.cqrs'),
             ('Read replicas', 'Data products = read stores.', 'dp.replica')]),
   ('Principios', [('Selección', 'Inmutables, sin raw, atómicos, golden source.', 'dp.principios'),
                   ('Arquitectura', 'Input y output ports, metadata.', 'dp.arq')])])

# ═══════════ U5
M('u5-de', 'u5', 'Qué es la ingeniería de datos', 'Reis, cap. 1', 'DATA ENG.', 'Datos crudos → información de calidad',
  'Desarrollo, implementación y mantenimiento de sistemas y procesos (P1 2025).',
  [('Definición', [('Reis', 'Sistemas y procesos de datos crudos a información de calidad.', 'de.def'),
                   ('Data engineer', 'Gestiona el ciclo de vida.', 'de.rol')]),
   ('Historia', [('Evolución', 'DWH → big data → ciclo de vida.', 'de.historia')])],
  [('Contexto', [('Pirámide de Rogati', 'DE sostiene las capas de abajo.', 'de.piramide'),
                 ('Madurez', 'Empezar, escalar, liderar.', 'de.madurez')]),
   ('Roles', [('Tipo A y B', 'Abstraction vs build.', 'de.tipos'),
              ('Stakeholders', 'Upstream, downstream, C-suite.', 'de.stake')])])

M('u5-ciclo', 'u5', 'Ciclo de vida de la ingeniería de datos', 'Reis, cap. 2', 'CICLO', 'Generación → servicio',
  'Cinco etapas + seis corrientes. Batch = bloques; streaming = continuo.',
  [('Etapas', [('Generación', 'Sistemas fuente.', 'ciclo.tabla:1'),
               ('Almacenamiento', 'Hot, lukewarm, cold.', 'ciclo.tabla:2'),
               ('Ingesta', 'Cuello de botella.', 'ciclo.tabla:3'),
               ('Transformación', 'Donde se crea valor.', 'ciclo.tabla:4'),
               ('Servicio', 'Analytics, ML, reverse ETL.', 'ciclo.tabla:5 ciclo.serving')]),
   ('Ingesta', [('Batch', 'Bloques periódicos.', 'ciclo.batch'),
                ('Streaming', 'Continuo.', 'ciclo.stream'),
                ('Push y pull', 'Quién inicia.', 'ciclo.push')])],
  [('Corrientes', [('Las seis', 'Seguridad, DM, DataOps, arquitectura, orquestación, software.', 'ciclo.corrientes'),
                   ('DataOps', 'Automatización, observabilidad, incidentes.', 'ciclo.dataops'),
                   ('Data management', 'Gobierno, calidad, lineage.', 'ciclo.dm')]),
   ('Encuadre', [('Subconjunto', 'Del ciclo de vida del dato.', 'ciclo.etapas')])])

M('u5-arq', 'u5', 'Arquitectura de datos y patrones', 'Reis, cap. 3 · Medallion, cap. 1', 'ARQUITECTURA', 'Decisiones flexibles y reversibles',
  'Negocio, técnica, aplicaciones y datos: subconjuntos de la empresarial (P4 2025).',
  [('Definiciones', [('Empresarial', 'Cuatro subconjuntos.', 'arq.empresarial'),
                     ('De datos', 'Necesidades de datos cambiantes.', 'arq.datos'),
                     ('Operacional vs técnica', 'Qué vs cómo.', 'arq.optec')]),
   ('Principios', [('Nueve', 'Falla, escala, acople, reversibles, FinOps…', 'arq.principios'),
                   ('Puertas', 'Una vía vs dos vías.', 'arq.puertas'),
                   ('La menos mala', 'No la mejor.', 'arq.buena')])],
  [('Patrones', [('DWH', 'Hub central, ETL/ELT, marts.', 'patarq.tabla:1 patarq.ssot'),
                 ('Lake y lakehouse', 'Object storage; ACID.', 'patarq.tabla:2 patarq.tabla:3'),
                 ('Lambda', 'Batch + stream.', 'patarq.tabla:5'),
                 ('Kappa', 'Solo stream.', 'patarq.tabla:6'),
                 ('Inmon y Kimball', 'Top-down vs bottom-up.', 'patarq.inmon')])])

M('u5-mesh', 'u5', 'Data Mesh', 'Dehghani, cap. 1', 'DATA MESH', 'Descentralizar los datos analíticos',
  'Seis cambios y cuatro principios (P6 y P7 2025).',
  [('Qué es', [('Definición', 'Enfoque sociotécnico descentralizado.', 'mesh.def'),
               ('Resultados', 'Cambio, agilidad, valor.', 'mesh.outcomes'),
               ('Datos analíticos', 'No operacionales.', 'mesh.datos')]),
   ('Seis cambios', [('Organizacional', 'Dominios.', 'mesh.cambios:1'),
                     ('Arquitectónico', 'Malla distribuida.', 'mesh.cambios:2'),
                     ('Tecnológico', 'Datos + código.', 'mesh.cambios:3'),
                     ('Operacional', 'Gobierno federado.', 'mesh.cambios:4'),
                     ('Principios', 'Datos como producto.', 'mesh.cambios:5'),
                     ('Infraestructura', 'Integrada.', 'mesh.cambios:6')])],
  [('Cuatro principios', [('Domain ownership', 'Propiedad en los dominios.', 'mesh.p1'),
                          ('Data as a product', 'Ocho atributos, data quantum.', 'mesh.p2'),
                          ('Self-serve platform', 'Baja el costo.', 'mesh.p3'),
                          ('Gobierno federado', 'Políticas automatizadas.', 'mesh.p4')]),
   ('Interplay', [('Se compensan', 'Silos, costo, incompatibilidad.', 'mesh.interplay')])])

M('u5-medallion', 'u5', 'Arquitectura Medallion', 'Strengholt, Building Medallion Architectures', 'MEDALLION', 'Bronze ⇒ Silver ⇒ Gold',
  'Crudo → limpio → agregado para el negocio (P8 2025).',
  [('Qué es', [('Definición', 'Patrón para ordenar datos en un lakehouse.', 'medallion.def'),
               ('Capas lógicas', 'Landing y Platinum posibles.', 'medallion.logicas'),
               ('Tres capas', 'Medallion en la distribución.', 'medallion.tres')])],
  [('Capas', [('Bronze', 'Crudo, inmutable.', 'medallion.capas:1'),
              ('Silver', 'Limpio, validado.', 'medallion.capas:2'),
              ('Gold', 'Agregado, negocio.', 'medallion.capas:3')]),
   ('Contexto', [('Lakehouse', 'ACID sobre object storage.', 'medallion.lakehouse'),
                 ('Crítica', 'Falta consenso.', 'medallion.critica')])])

M('u5-patrones', 'u5', 'Patrones de diseño de ingeniería de datos', 'Konieczny (TPI)', 'PATRONES', 'Recetas para problemas de datos',
  'Saber describir uno en menos de 50 palabras con un ejemplo (P5 2025).',
  [('Qué es un patrón', [('Definición', 'Plantilla personalizable.', 'patrones.def'),
                         ('Cómo explicarlo', 'En pocas palabras y con un ejemplo: Dead-Letter.', 'patrones.kleppmann')])],
  [('Ejemplos', [('Dead-Letter', 'Desviar registros que fallan.', 'patrones.deadletter'),
                 ('CDC e Incremental', 'Ingerir cambios.', 'patrones.cdc'),
                 ('Catálogo', 'Diez capítulos.', 'patrones.catalogo')])])

# ═══════════ U6
M('u6-agentes', 'u6', 'Agentes de IA', 'Albada, caps. 1 y 2', 'AGENTES', 'Decidir, no solo ejecutar',
  'Analizar datos, interpretar el entorno y decidir según el contexto (P9 2025).',
  [('Qué son', [('Definición', 'Sistemas que deciden con contexto.', 'agentes.def'),
                ('Sistema agéntico', 'Herramientas, memoria, modelo, orquestación.', 'agentes.sistema'),
                ('Tipos', 'Siete tipos + voz y video.', 'agentes.tipos')]),
   ('Cuándo usar', [('Código', 'Input predecible.', 'agentes.tabla:1 agentes.regla'),
                    ('Workflow', 'Ramas finitas.', 'agentes.regla'),
                    ('RAG', 'Preguntas sobre documentos.', 'agentes.regla'),
                    ('Agente', 'Variabilidad alta.', 'agentes.tabla:4')])],
  [('Diseño', [('Componentes', 'Orquestación + 4.', 'disagentes.componentes'),
               ('Memoria', 'Corto y largo plazo.', 'disagentes.memoria'),
               ('Herramientas', 'Locales, API, MCP.', 'disagentes.tools')]),
   ('Decisiones', [('Trade-offs', 'Velocidad, escala, confiabilidad, costo.', 'disagentes.tradeoffs'),
                   ('Single vs multi', 'Simplicidad vs especialización.', 'disagentes.arq'),
                   ('Principios', 'Escalabilidad, modularidad…', 'agentes.principios')])])

M('u6-rag', 'u6', 'RAG', 'Kimothi, cap. 2 · Huyen, cap. 6', 'RAG', 'Recuperar y generar',
  'Indexing (offline) + generation (tiempo real). Embeddings = texto a números (P10 2025).',
  [('Pipelines', [('Cinco pasos', 'Pregunta … respuesta.', 'rag.def'),
                  ('Indexing', 'Carga, chunking, embeddings, vector DB.', 'rag.pipelines:3'),
                  ('Generation', 'Retriever, prompt, LLM.', 'rag.pipelines:3 rag.retriever')]),
   ('Componentes', [('Embeddings', 'Formato numérico.', 'rag.emb'),
                    ('Extras', 'Caché, guardrails, seguridad.', 'rag.extras')])],
  [('Evaluar', [('Tríada', 'Contexto, fidelidad, respuesta.', 'rag.triada'),
                ('Precision y recall', 'Del retriever.', 'ragret.eval')]),
   ('Retrieval', [('Sparse', 'BM25, términos.', 'ragret.tabla:1'),
                  ('Dense', 'Embeddings.', 'ragret.tabla:1'),
                  ('Optimizar', 'Chunking, reranking.', 'ragret.opt')]),
   ('LLMs', [('Transformer', 'Tokens, embeddings y atención; genera de a un token.', 'llm.transformer'),
             ('BERT vs GPT', 'Entender y vectorizar vs generar texto.', 'llm.bert llm.gpt'),
             ('Prompting, RAG o fine-tuning', 'Orientar, consultar fuentes o reentrenar.', 'llm.prompting'),
             ('MLOps y LLMOps', 'Operar el ciclo de vida de los modelos.', 'llm.mlops')])])

M('u6-huyen', 'u6', 'Agentes según Huyen y AI PM', 'Huyen, cap. 6 · Nika, cap. 1', 'HUYEN · NIKA', 'Entorno + herramientas',
  'ReAct = pensar, actuar, observar. Memoria: interna, corto, largo plazo.',
  [('Agentes', [('Definición', 'Percibe y actúa sobre su entorno.', 'huyen.def'),
                ('Herramientas', 'Conocimiento, capacidades, escritura.', 'huyen.tools'),
                ('Planificación', 'ReAct y Reflexion.', 'huyen.plan'),
                ('Memoria', 'Tres niveles.', 'huyen.memoria')])],
  [('AI PM', [('Cuatro tipos de IA', 'Tradicional, GenAI, AGI, ASI.', 'huyen.tipos'),
              ('Rasgos', 'Probabilísticos, drift.', 'huyen.rasgos'),
              ('Skills y subtipos', 'Builder, experiences, enhanced.', 'huyen.skills')])])
