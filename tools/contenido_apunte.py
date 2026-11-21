"""Apunte de estudio (src/mapas/apunte.json).

Cada sección: clave, unidad, título, fuente principal (con páginas del PDF), otras fuentes y bloques.
Un bloque es (tipo, texto[, etiqueta]). Tipos: p, li, h, callout, table (texto = filas).
Las etiquetas permiten que los mapas mentales citen un bloque: 'fe.def'.
Las páginas son las del PDF de la carpeta de cada unidad, no las del libro impreso.
"""

SECCIONES = []


def S(clave, unidad, titulo, src, orig, bloques):
    SECCIONES.append(dict(clave=clave, unit=unidad, title=titulo, src=src, orig=orig, bloques=bloques))


# ═══════════════════════════ U4 · Ciencia de Datos Aplicada
S('ml', 'u4', 'Machine learning y modelado predictivo', 'Notas de clase, U4', 'Zheng, cap. 1, págs. 2–4 · Notas, U2 (supervisado y no supervisado)', [
    ('p', 'El **modelado predictivo** tiene tres pasos: predecir si un resultado de interés va a ocurrir en el futuro, usar observaciones detalladas para **entrenar** un modelo y hacer una predicción, y **actuar** en base a esa predicción.', 'predictivo'),
    ('li', '**Modelo:** un componente o artefacto de software al que se le hacen llamadas; se puede reentrenar y replicar. Aprende del **historial de datos** cómo se comporta la variable que se quiere predecir, y solo funciona con datos limpios. Si el modelo es preentrenado, hace falta menos historia.', 'modelo'),
    ('li', '**Ventanas:** se divide la historia en ventanas para que el modelo aprenda y se reserva alguna para probar las predicciones y medir el resultado.', 'ventanas'),
    ('li', '**Features:** las columnas que se usan para entrenar; «los data points que entrenan al modelo». No tienen que estar tal cual en el historial: se pueden transformar.', 'features'),
    ('h', 'Supervisado vs no supervisado'),
    ('table', [['', 'Supervisado', 'No supervisado'],
               ['Datos', 'Etiquetados: features + respuesta correcta (ground truth)', 'Sin etiquetar'],
               ['Cómo aprende', 'Una función de pérdida compara la predicción con la etiqueta y ajusta parámetros', 'Busca estructura, similitudes o grupos por sí solo'],
               ['Tareas', 'Clasificación (¿es spam?) y regresión (precio de una casa)', '**Clustering** y reducción de dimensionalidad'],
               ['En clase', '«Sabemos los resultados y entendemos el modelo»', '«No sabemos los resultados y el modelo los propone»']], 'sup'),
    ('callout', '**Clustering es no supervisado.** La P12 del 1er parcial (que entra ahora) afirma que es supervisado: es **falso**.', 'clustering'),
    ('li', '**El ML engineer** casi nunca crea el modelo: busca la forma de que los datos encajen en modelos existentes. Trabaja sobre las capas **Silver o Gold** de una arquitectura Medallion y elige las features entre las columnas de esas tablas.', 'mle'),
    ('callout', '**No entra la matemática.** En clase: «Deja por fuera todo lo que es matemática». Se pregunta qué es, para qué sirve y cómo se relaciona.', 'mate'),
])

S('fe', 'u4', 'Feature y feature engineering', 'Zheng, cap. 1, págs. 2–4 · Ozdemir, cap. 1, págs. 1–4', 'Videos MIT 6.5–6.6 · Notas, U4', [
    ('p', 'Zheng parte de **datos** (observaciones de fenómenos reales, con ruido y faltantes), **tareas** (las preguntas que se quieren responder) y **modelos** (fórmulas que relacionan aspectos de los datos). Los datos pueden ser **incorrectos**, **redundantes** o **faltantes**.', 'datos'),
    ('p', 'Una **feature** es una **representación numérica de datos crudos** (Zheng). Es el puente entre los datos, que muchas veces no son numéricos, y las fórmulas del modelo. También se la describe como una **propiedad medible** de una entidad (edad, monto, frecuencia de compra).', 'def'),
    ('p', '**Feature engineering (Zheng):** el proceso de formular las features más apropiadas **dados los datos, el modelo y la tarea**. **(Ozdemir):** el arte de manipular y transformar datos hacia un formato que represente de forma óptima el problema que el algoritmo intenta modelar y que mitigue las complejidades y sesgos de los datos. **En clase:** manipular + transformar + representar.', 'defe'),
    ('li', '**Cantidad:** con muy pocas features informativas el modelo no cumple la tarea; con demasiadas o irrelevantes se vuelve caro y difícil de entrenar.', 'cantidad'),
    ('li', '**Palanca de doble articulación:** features y modelo se eligen juntos. Buenas features facilitan el modelado; malas features exigen un modelo mucho más complicado para el mismo rendimiento (fig. 1-2: datos crudos → features → modelado → insights).', 'doble'),
    ('h', 'Tipos de features (video MIT 6.6)'),
    ('table', [['Tipo', 'Qué es', 'Ejemplo'],
               ['**Identity**', 'El dato duro de la entidad', 'Género, edad'],
               ['**Transform**', 'Se transforma la columna en categorías u otra forma más útil', 'Día de la semana a partir de la fecha'],
               ['**Aggregate**', 'Funciones de agregación (count, sum)', 'Compras en los últimos 30 días']], 'tipos'),
    ('callout', '**Cómo se pregunta.** P10 del 1er parcial: «cite los tipos de features, seleccione 1 y proponga 1 ejemplo en menos de 50 palabras». P24: solo citarlos. P23: definir feature. P9: «propiedad cuantitativa y medible» → verdadero.', 'examen'),
    ('li', 'Clasificación complementaria por naturaleza del dato (Unidad 2): numéricas (continuas o discretas), categóricas (nominales u ordinales), binarias, temporales, de texto y derivadas o de interacción.', 'otra'),
])

S('mvd', 'u4', 'Model-centric vs data-centric, pipelines y drift', 'Ozdemir, cap. 1, págs. 1–9', 'Notas, U4 (laboratorio Avengers) · fig. 1.1, 1.2 y 1.5', [
    ('table', [['Model-centric', 'Data-centric'],
               ['Cambiar el algoritmo', 'Mejorar la representación'],
               ['Ajustar hiperparámetros', 'Corregir valores faltantes'],
               ['Agregar capas, árboles o complejidad', 'Crear variables útiles'],
               ['Confiar en que el modelo descubra todo', 'Seleccionar señal y reducir ruido']], 'tabla'),
    ('p', 'En clase: el enfoque en el modelo puede funcionar, pero el modelo se fuerza y le cuesta mucho más. El trabajo del científico de datos con feature engineering es **data-centric**. Andrew Ng: «machine learning is basically feature engineering».', 'clase'),
    ('li', '**Conviene data-centric** con pocas observaciones (<10 K), muchas columnas respecto de las filas (**maldición de la dimensionalidad**), cuando importa la interpretabilidad o el dominio es complejo (finanzas).', 'cuando'),
    ('li', '**Laboratorio Avengers:** `threat_per_hero = threat_level / team_size` (9/3 = 3) es una señal más directa que las dos columnas sueltas. Usar «héroes heridos al final de la misión» para predecir antes de empezar es **fuga de datos**. Más columnas pueden empeorar porque meten ruido.', 'lab'),
    ('li', '**Beneficios:** menor complejidad, mejor convergencia, más velocidad, más interpretabilidad. **No puede:** crear señales inexistentes, reemplazar tener datos suficientes (<1.000 filas) ni arreglar un problema mal definido.', 'limites'),
    ('h', 'Pipeline de ML (5 pasos, fig. 1.2)'),
    ('li', '1) Definir el dominio del problema · 2) obtener datos que lo representen (y EDA) · 3) **feature engineering** · 4) selección y entrenamiento del modelo · 5) despliegue y evaluación (detectar *model decay*).', 'pipeline'),
    ('h', 'Pipeline de feature engineering (4 pasos, fig. 1.5)'),
    ('li', '1) **Comprensión** (niveles de datos) → 2) **estructuración** (no estructurado → vectores, por extracción o aprendizaje) → 3) **optimización** (mejora, construcción, extracción, selección) → 4) **evaluación** (comparar contra un baseline con un modelo fijo). En clase: entender → estructurar → optimizar → evaluar.', 'pipfe'),
    ('h', 'Data drift y concept drift'),
    ('table', [['', 'Data drift', 'Concept drift'],
               ['Qué cambia', 'La **distribución** de los datos; el significado sigue igual', 'La **relación** entre features y objetivo (nuestra interpretación)'],
               ['Libro', 'Pandemia: más horas de streaming', 'Aviso «¿seguís mirando?» con documentales para mascotas'],
               ['Clase', 'Amenaza promedio 4,2 → 8,1 en la crisis multiversal', 'Más héroes ya no aumenta el éxito']], 'drift'),
    ('callout', 'Según la clase, el drift lo trabaja **MLOps**.', 'mlops'),
])

S('niveles', 'u4', 'Datos estructurados y los cuatro niveles de datos', 'Ozdemir, cap. 2, págs. 13–23', 'fig. 2.2, 2.5 y 2.6 · Notas, U4', [
    ('p', 'Proceso del libro: 1) diagnosticar si el dataset es **estructurado o no estructurado**, 2) asignar cada feature a un **nivel de datos**, 3) aplicar los tipos de feature engineering según el nivel.', 'proceso'),
    ('table', [['Estructurados', 'No estructurados'],
               ['Filas y columnas, base relacional', 'No entran en una tabla: una «masa» de datos'],
               ['Más fáciles como input de ML', 'Hay que estructurarlos primero'],
               ['Menos almacenamiento', 'Más almacenamiento'],
               ['~20% de los datos de la empresa', '~80% (Gartner)'],
               ['CSV, planillas', 'Texto, audio, video, imágenes']], 'estruct'),
    ('table', [['Nivel', 'Tipo', 'Permite', 'Ejemplo', 'Tratamiento'],
               ['**Nominal**', 'Cualitativo sin orden', 'Moda, conteos, gráfico de barras', 'Tipo de sangre, marca de celular', 'Dummificar (one-hot), agrupar categorías raras'],
               ['**Ordinal**', 'Cualitativo con orden', 'Orden y mediana; no restar', 'Satisfacción, notas A/B/C', 'Enteros crecientes 1, 2, 3'],
               ['**Intervalo**', 'Cuantitativo sin cero verdadero', 'Suma, resta, media, mediana, desvío', 'Temperatura en °C', 'Imputar con media o mediana'],
               ['**Razón**', 'Cuantitativo con cero verdadero', 'Todo lo anterior + multiplicar y dividir', 'Dinero, edad, altura', 'Medias aritmética, geométrica o armónica']], 'tabla'),
    ('li', '**Truco intervalo vs razón:** dividir dos valores; si el cociente tiene sentido aceptado (100 USD es el doble que 50), es razón. 0 °C no es ausencia de temperatura.', 'truco'),
    ('li', '**Medias pitagóricas:** aritmética (aditiva, unidades iguales), geométrica (multiplicativa, escalas distintas, ej. CSAT y NPS) y armónica (razones: velocidades 20, 60 y 70 mph → 37,1 mph, no 50).', 'medias'),
    ('li', '**Outliers:** la media se va hacia los extremos (30…100 → media 56,7, mediana 49). Con muchos outliers, imputar con la mediana.', 'outliers'),
    ('callout', 'Confundir intervalo con razón no es grave; lo grave es tratar como cuantitativo algo cualitativo, o al revés.', 'cuidado'),
])

S('tiposfe', 'u4', 'Los cinco tipos de feature engineering y cómo evaluarlos', 'Ozdemir, cap. 1, pág. 8 · cap. 2, págs. 24–33', 'Notas, U4', [
    ('table', [['Tipo', 'Qué hace', 'Cuándo', 'Ejemplo'],
               ['**Mejora**', 'Transforma features existentes: imputar, estandarizar, normalizar', 'Hay faltantes u outliers', 'Imputar temperaturas faltantes'],
               ['**Construcción**', 'Crea features nuevas e interpretables; une con otras fuentes; bucketing', 'Falta señal; una versión transformada tiene más señal', 'Precio / pies² = precio por pie²'],
               ['**Selección**', 'Elige el mejor subconjunto', 'Maldición de la dimensionalidad, features dependientes, velocidad', 'Eliminar las columnas originales'],
               ['**Extracción**', 'Algoritmos que crean features asumiendo la forma de los datos', 'Datos no estructurados; demasiadas features', 'PCA, SVD, bag-of-words, BERT'],
               ['**Aprendizaje**', 'Deep learning no paramétrico aprende una representación latente', 'No se puede suponer nada de los datos', 'GANs, autoencoders']], 'tabla'),
    ('li', 'La **construcción** es la que más conocimiento del dominio exige. La **extracción** puede empeorar los datos si su supuesto es falso. El **aprendizaje** necesita más datos y da features poco interpretables.', 'matices'),
    ('h', 'Cómo evaluar el feature engineering'),
    ('li', '**1. Métricas de ML:** baseline antes → aplicar FE → comparar contra un umbral (precision, recall; Davies-Bouldin para clustering).', 'm1'),
    ('li', '**2. Interpretabilidad:** poder preguntar «por qué». Mejora, construcción y selección la mantienen; extracción y aprendizaje la reducen.', 'm2'),
    ('li', '**3. Equidad y sesgo:** solo el 38% de los encuestados (2020) atendía fairness.', 'm3'),
    ('li', '**4. Complejidad y velocidad:** un modelo que no predice rápido no llega a producción.', 'm4'),
    ('callout', 'No confundir: **tipos de features** (identity, transform, aggregate; MIT) con **tipos de feature engineering** (mejora, construcción, selección, extracción, aprendizaje; Ozdemir).', 'ojo'),
])

S('texto', 'u4', 'Texto como features (Zheng, cap. 3)', 'Zheng, cap. 3, págs. 40–64', 'fig. 3-1', [
    ('li', '**Bag-of-words (BoW):** el documento se vuelve un **vector plano** de conteos, una dimensión por palabra. No conserva orden ni jerarquía; «not bad» y «toy dog» pierden su sentido. Sirve para clasificar y para recuperar información.', 'bow'),
    ('li', '**Bag-of-n-grams:** cuenta secuencias de n tokens. Más información, pero un espacio más grande, más ralo y más caro.', 'ngram'),
    ('li', '**Filtrado:** stopwords (listas de NLTK), palabras frecuentes del corpus y palabras raras (en Yelp, 189.915 de 357.481 aparecen en una sola reseña; se juntan en un *garbage bin*).', 'filtro'),
    ('li', '**Stemming:** reduce a la raíz (Porter). Puede perjudicar: new y news → new. La **lematización** usa reglas lingüísticas y POS.', 'stem'),
    ('li', '**Parseo y tokenización:** quitar estructura (HTML, email) y cortar el string en tokens; cuidado con Unicode.', 'token'),
    ('li', '**Colocaciones:** frases que significan más que sus partes («strong tea» sí, «cute puppy» no). Se detectan por frecuencia, test de razón de verosimilitud o información mutua puntual. **Chunking** y **POS tagging** arman frases más largas.', 'coloc'),
])

S('nlp', 'u4', 'NLP: tareas, bloques del lenguaje y enfoques', 'Vajjala, cap. 1, págs. 2–31', 'fig. 1-1, 1-2, 1-3, 1-8, 1-11, 1-13 y 1-14 · Notas, U4 · video MIT 1.1', [
    ('p', 'El lenguaje no son solo palabras: es cultura, tradición y comunidad (clase). El NLP resuelve **core tasks**, **aplicaciones generales** e **industry specific** (fig. 1-1).', 'que'),
    ('li', '**De fácil a difícil (fig. 1-2):** spell checking → recuperación por palabra clave → topic modeling → clasificación de texto → extracción de información → agente conversacional de dominio cerrado → resumen → question answering → traducción → agente conversacional de dominio abierto.', 'dificultad'),
    ('table', [['Bloque (fig. 1-3)', 'Qué es', 'Aplicaciones'],
               ['Fonemas', 'Sonidos', 'Speech-to-text, identificación del hablante, text-to-speech'],
               ['Morfemas y lexemas', 'Palabras', 'Tokenización, word embeddings, POS tagging'],
               ['Sintaxis', 'Frases y oraciones', 'Parsing, extracción de entidades y relaciones'],
               ['Contexto', 'Significado', 'Resumen, topic modeling, sentimiento']], 'bloques'),
    ('li', '**Por qué es difícil:** ambigüedad, conocimiento común implícito, creatividad y diversidad entre idiomas.', 'dificil'),
    ('li', '**IA, ML, DL y NLP (fig. 1-8):** ML está dentro de IA y DL dentro de ML; el NLP se superpone con los tres.', 'circulos'),
    ('h', 'Enfoques'),
    ('li', '**Heurísticas o reglas:** diccionarios (WordNet), expresiones regulares, gramáticas (GATE).', 'reglas'),
    ('li', '**ML clásico:** Naive Bayes, **SVM** (límite de decisión con el mayor margen, fig. 1-11), HMM, CRF.', 'mlc'),
    ('li', '**Deep learning:** **RNN** (procesa la secuencia pasando su estado, fig. 1-13; olvida dependencias largas) y **LSTM** (una RNN con celdas y compuertas que recuerda contexto largo, fig. 1-14); CNN, **Transformers** (self-attention, BERT) y autoencoders.', 'dl'),
    ('callout', 'Línea de tiempo de clase: era pre-transformers → llega la atención y los LLMs (2017) → era GenAI (2022–hoy). DL no es bala de plata: pide muchos datos, es caro y poco interpretable.', 'linea'),
])

S('pipnlp', 'u4', 'Pipeline de NLP y preprocesamiento', 'Vajjala, cap. 2, págs. 32–75', 'fig. 2-1, 2-7 y 2-8 · Notas, U4', [
    ('li', '**Etapas (fig. 2-1):** adquisición de datos → limpieza de texto → preprocesamiento → feature engineering → modelado → evaluación → deployment → monitoreo y actualización del modelo.', 'etapas'),
    ('li', '**Adquisición:** datasets públicos, scraping, aumentación (back translation, sinónimos).', 'adq'),
    ('li', '**Limpieza:** HTML, Unicode, ortografía, OCR.', 'limpieza'),
    ('li', '**Preprocesamiento:** segmentar oraciones, tokenizar, minúsculas, sacar puntuación y stopwords, stemming y lematización (fig. 2-8). Avanzado: POS tagging, parsing, coreference resolution, NER.', 'pre'),
    ('table', [['Técnica', 'Qué hace'],
               ['Stemming', 'Recorta sufijos con reglas; puede dar no-palabras (airliner → airlin)'],
               ['Lematización', 'Lleva a la forma base real (better → good, was → be)'],
               ['POS tagging', 'Etiqueta qué es cada palabra'],
               ['Parsing', 'Descompone la oración en su estructura sintáctica'],
               ['Coreference resolution', 'Relaciona expresiones que refieren a lo mismo']], 'tecnicas'),
    ('li', '**Evaluación:** intrínseca (métricas del modelo) y extrínseca (impacto en el negocio).', 'eval'),
])

S('repr', 'u4', 'Representación y clasificación de texto', 'Vajjala, cap. 3, págs. 76–108 · cap. 4, págs. 109–146', 'fig. 4-3', [
    ('li', '**Vectorización básica:** one-hot, bag-of-words, bag-of-n-grams y **TF-IDF** (frecuente en el documento y raro en el corpus pesa más). Problemas: vectores enormes y ralos, sin significado.', 'basica'),
    ('li', '**Embeddings:** vectores densos donde palabras parecidas quedan cerca. **Word2vec** con **CBOW** (contexto → palabra central) y **SkipGram** (palabra central → contexto); Doc2vec para documentos; t-SNE para visualizarlos.', 'emb'),
    ('li', '**Clasificación de texto:** asignar una o varias categorías (spam, sentimiento, tickets). Pipeline (fig. 4-3): datos etiquetados → preprocesamiento y features → entrenar y evaluar → predecir textos nuevos. Algoritmos: Naive Bayes, regresión logística, SVM, CNN, LSTM.', 'clasif'),
    ('li', 'Se evalúa con matriz de confusión, precision y recall. Sin datos etiquetados: reglas, crowdsourcing o **active learning**.', 'evalc'),
])

S('recom', 'u4', 'Sistemas de recomendación, cross validation y RMSE', 'Notas de clase, U4', 'Videos MIT 4.1–4.2 · ejercicio con Surprise (carpeta U4)', [
    ('p', 'Un sistema de recomendación nos ayuda a encontrar lo que buscamos sin pedirlo de forma precisa: el objetivo es semántico. En algunos negocios es el centro (YouTube).', 'que'),
    ('table', [['Modelo (Surprise)', 'Cómo recomienda'],
               ['Aleatorio (NormalPredictor)', 'Rating al azar según la distribución: baseline'],
               ['Filtrado colaborativo usuario-usuario', 'Usuarios con gustos parecidos'],
               ['Filtrado colaborativo ítem-ítem', 'Ítems parecidos a los que el usuario valoró'],
               ['Factorización (SVD, NMF)', 'Factores latentes de la matriz usuarios × ítems']], 'modelos'),
    ('li', '**Active learning:** un humano en el bucle, un oráculo que va diciendo la verdad. Google aprende de cada clic; el peso es inversamente proporcional a la posición mostrada.', 'active'),
    ('li', '**Cross validation:** se entrena con una parte, se valida con otra y se rota la ventana; con k folds, cada parte es validación una vez y se promedia el error.', 'cv'),
    ('li', '**RMSE:** raíz del error cuadrático medio. Mide cuánto se equivoca la predicción en las mismas unidades; más bajo es mejor y castiga más los errores grandes. MAE es la versión sin cuadrado.', 'rmse'),
])

S('dp', 'u4', 'Data products (Strengholt, Data Management at Scale, cap. 4)', 'Strengholt DMS, cap. 4, págs. 1–37', 'fig. 4-1, 4-2, 4-3 y 4-5 · Notas, U4', [
    ('p', 'Hacer responsables a los productores de datos y descentralizar cómo se sirven es una gran forma de escalar.', 'intro'),
    ('table', [['', 'Data as a product', 'Data product'],
               ['Qué es', 'Una **forma de pensar**', 'Un concepto de **arquitectura**'],
               ['Idea', 'Los datos son un producto completo del que el equipo es responsable; el consumidor es un cliente', 'Lo que se construye para exponer datos']], 'vs'),
    ('callout', '**P8 del 1er parcial:** la diferencia es que una se refiere a cómo pensamos los datos y la otra a la arquitectura.', 'examen'),
    ('li', '**Dehghani:** data product = *architectural quantum* que encapsula código, datos y metadata, e infraestructura. **Accenture:** datasets, modelos y dashboards.', 'visiones'),
    ('li', '**Por qué no un contenedor:** en la subasta de flores de Aalsmeer la metadata viaja con cada caja, pero en lo digital la metadata vive aparte (catálogo, lineage). Pegarla a los datos la duplica en cada copia y complica calidad y seguridad.', 'contenedor'),
    ('li', '**Definición de Strengholt:** una **entidad lógica autónoma que describe datos pensados para consumo**, con nombre, relación con el dominio, dueño y referencias a los activos físicos. Se separan dos puntos de vista: datos y tecnología (fig. 4-1). Debajo están los **data elements**.', 'logica'),
    ('h', 'CQRS'),
    ('li', '**CQRS** separa escrituras (comandos) y lecturas (consultas) en dos modelos sincronizados por eventos (fig. 4-2). Escribir exige muchos pasos (bloquear, validar, commit, índices); leer es barato. Beneficios: bases distintas, varias bases de lectura, escalar por separado. Costo: complejidad y latencia.', 'cqrs'),
    ('li', 'Toda lectura desde una réplica, DWH, lake u ODS es una forma de CQRS. **Las arquitecturas de data products siguen la filosofía CQRS**: read stores optimizados para lectura intensiva. Los data products quedan del lado del proveedor y las transformaciones específicas del lado del consumidor (fig. 4-3).', 'replica'),
    ('h', 'Principios de diseño (selección)'),
    ('li', 'Orientados a recursos y optimizados para lectura · datos **inmutables** · **ubiquitous language** · capturar desde la **golden source** · estándares de interoperabilidad · **sin datos crudos** · no conformarse a cada consumidor · no tercerizar la lógica de negocio · defaults claros (9999-12-31) · consistencia semántica · **atomicidad** · compatibilidad y versionado · dato nuevo = nuevo dueño · seguridad por fila y columna · metamodelo · self-service · relaciones entre dominios · consistencia empresarial · historización · modelo operativo (playbooks).', 'principios'),
    ('li', '**Arquitectura (fig. 4-5):** input ports, output ports, capa de metadata, pipeline por capas (Bronze, Silver, Gold), calidad y marketplace.', 'arq'),
])

# ═══════════════════════════ U5 · Arquitecturas e Ingeniería de Datos
S('de', 'u5', 'Qué es la ingeniería de datos', 'Reis, cap. 1, págs. 1–27', 'fig. 1-1, 1-4, 1-5, 1-8 y 1-12 · Notas, U5', [
    ('p', '**Definición (Reis):** la ingeniería de datos es el **desarrollo, implementación y mantenimiento de sistemas y procesos que toman datos crudos y producen información de alta calidad y consistente** que soporta casos de uso downstream, como análisis y machine learning. Es la intersección de seguridad, data management, DataOps, arquitectura de datos, orquestación e ingeniería de software.', 'def'),
    ('callout', '**P1 del parcial 2025** pidió esta definición en formato choice.', 'examen'),
    ('li', 'Un **data engineer** gestiona el ciclo de vida: obtiene datos de los sistemas fuente, los almacena y los prepara para analistas, data scientists y otros.', 'rol'),
    ('li', '**Evolución:** 1980–2000 data warehousing (Inmon acuña «data warehouse» en 1989; Kimball e Inmon; MPP) → 2000s nace la ingeniería de datos contemporánea → 2000s–2010s **big data engineering** (Hadoop, Spark, Kafka) → 2020s **ingeniería del ciclo de vida del dato**.', 'historia'),
    ('li', '**Upstream de la ciencia de datos:** pirámide de Rogati (recolectar → mover/almacenar → explorar/transformar → agregar/etiquetar → aprender/optimizar → IA). Los data scientists pasan 70–80% del tiempo en las tres capas de abajo.', 'piramide'),
    ('li', '**Madurez de datos:** 1) empezar con datos, 2) escalar con datos, 3) liderar con datos.', 'madurez'),
    ('li', '**Tipo A** (*abstraction*: usa herramientas gestionadas) y **tipo B** (*build*: construye herramientas). **Internal-facing** vs **external-facing**.', 'tipos'),
    ('li', '**Stakeholders:** upstream (arquitectos de datos, ingenieros de software, DevOps/SRE) y downstream (analistas, data scientists, ML engineers); y el C-suite: CEO, CIO, CTO, **CDO**, CAO.', 'stake'),
])

S('ciclo', 'u5', 'Ciclo de vida de la ingeniería de datos', 'Reis, cap. 2, págs. 1–33', 'fig. 2-1, 2-2, 2-5, 2-6 y 2-8 · Notas, U5', [
    ('p', '**Cinco etapas:** generación → almacenamiento → ingesta → transformación → servicio. El almacenamiento se dibuja como base porque ocurre en todo el ciclo. Es un subconjunto del ciclo de vida completo del dato (fig. 2-2).', 'etapas'),
    ('p', '**Corrientes subyacentes (undercurrents):** seguridad, data management, DataOps, arquitectura de datos, orquestación e ingeniería de software.', 'corrientes'),
    ('callout', '**P2 del parcial 2025:** «generación, almacenamiento, ingesta, transformación y servicio».', 'examen'),
    ('table', [['Etapa', 'Qué es', 'Claves'],
               ['Generación', 'Sistemas fuente (base de una app, IoT, APIs)', 'Fuera del control del DE'],
               ['Almacenamiento', 'Dónde viven los datos', 'Datos **hot**, **lukewarm** y **cold** según frecuencia de acceso'],
               ['Ingesta', 'Traer datos de las fuentes', 'El mayor cuello de botella; batch vs streaming; push vs pull'],
               ['Transformación', 'Pasar a algo útil', 'Tipos, normalización, lógica de negocio, featurización'],
               ['Servicio', 'Obtener valor', 'Analytics, ML y reverse ETL']], 'tabla'),
    ('h', 'Batch vs streaming'),
    ('li', '**Batch:** procesa por intervalos de tiempo o al llegar a un tamaño, en bloques. Es una «puerta de una vía» porque limita la latencia. Ideal para entrenar modelos y reportes.', 'batch'),
    ('li', '**Streaming:** entrega los datos de forma **continua**, casi en tiempo real. Casi todos los datos son streaming por naturaleza; adoptar tiempo real solo si un caso de negocio lo justifica. Punto medio: micro-batch.', 'stream'),
    ('callout', '**P3 del parcial 2025:** batch procesa periódicamente en bloques; streaming transmite de manera continua.', 'examen3'),
    ('li', '**Push vs pull:** en push la fuente escribe hacia el destino; en pull el sistema de ingesta lee la fuente (la E de ETL). CDC puede ser push o pull.', 'push'),
    ('li', '**Analytics (fig. 2-5):** BI, operacional y embebido. **Reverse ETL (fig. 2-6):** devolver datos procesados a las fuentes (ej. un CRM).', 'serving'),
    ('li', '**DataOps (fig. 2-8):** automatización, observabilidad y monitoreo, respuesta a incidentes.', 'dataops'),
    ('li', '**Data management:** gobierno (descubribilidad, metadata, accountability), calidad, master data, modelado, lineage, integración, ciclo de vida, ética y privacidad.', 'dm'),
])

S('arq', 'u5', 'Arquitectura de datos y sus principios', 'Reis, cap. 3, págs. 1–13', 'fig. 3-1 y 3-2 · Notas, U5', [
    ('p', 'La **arquitectura empresarial** tiene cuatro subconjuntos: **de negocio, técnica, de aplicaciones y de datos** (fig. 3-1). Definición de los autores: el diseño de sistemas para soportar el cambio en la empresa, con decisiones flexibles y reversibles tras evaluar trade-offs.', 'empresarial'),
    ('callout', '**P4 del parcial 2025:** la arquitectura de negocios está al mismo nivel que la de datos dentro de la empresarial; no es parte de la de datos.', 'examen'),
    ('p', '**Arquitectura de datos:** el diseño de sistemas para soportar las necesidades de datos cambiantes de la empresa, con decisiones flexibles y reversibles tras evaluar trade-offs. Es un subconjunto de la empresarial.', 'datos'),
    ('li', '**Operacional vs técnica (fig. 3-2):** la operacional dice **qué** hay que hacer (procesos, calidad, latencia); la técnica, **cómo** (ingesta, almacenamiento, transformación).', 'optec'),
    ('li', '**Puertas de una vía y de dos vías** (Bezos): decisiones casi irreversibles vs fácilmente reversibles.', 'puertas'),
    ('li', '**Buena arquitectura:** sirve al negocio con bloques comunes y reutilizables, es flexible y evoluciona. «La menos mala», no «la mejor». La mala es acoplada, rígida y centralizada.', 'buena'),
    ('li', '**Nueve principios:** 1) elegir componentes comunes con criterio, 2) planificar para la falla, 3) arquitectura para escalar, 4) la arquitectura es liderazgo, 5) arquitecturar siempre, 6) sistemas débilmente acoplados, 7) decisiones reversibles, 8) priorizar la seguridad, 9) adoptar FinOps.', 'principios'),
])

S('patarq', 'u5', 'Warehouse, lake, lakehouse, Lambda y Kappa', 'Reis, cap. 3, págs. 13–34 · Medallion, cap. 1, págs. 5–23', 'fig. 3-10 a 3-15 · fig. 1-4 a 1-8', [
    ('table', [['Patrón', 'Idea'],
               ['**Data warehouse**', 'Hub central que integra fuentes en formato consistente para OLAP; separa analítica de OLTP; ETL o ELT; data marts por área'],
               ['**Data lake**', 'Todo en object storage sin esquema previo; el lake 1.0 se volvió un pantano'],
               ['**Lakehouse**', 'Object storage barato con transacciones ACID (Delta Lake, Iceberg, Hudi + Spark)'],
               ['**Modern data stack**', 'Componentes cloud plug-and-play'],
               ['**Lambda**', 'Batch y streaming en paralelo, unidos en la capa de servicio; dos bases de código'],
               ['**Kappa**', 'Todo pasa por una plataforma de streaming'],
               ['**Dataflow / Beam**', 'Unifica batch y streaming'],
               ['**IoT**', 'Dispositivos → gateway → cola de mensajes → almacenamiento y servicio'],
               ['**Data mesh**', 'Descentralizar por dominios']], 'tabla'),
    ('li', '**Inmon (top-down):** primero un DWH empresarial en 3FN, después data marts en estrella; se carga dos veces. **Kimball (bottom-up):** primero data marts dimensionales (hechos y dimensiones).', 'inmon'),
    ('callout', '**P14 del 1er parcial:** «el DWH es una fuente única de la verdad» → verdadero (integra todo en un hub central). Data Mesh, en cambio, no impone una única fuente de verdad.', 'ssot'),
    ('li', '**Dominios y servicios, sistemas distribuidos, acople (single tier, multitier, monolito, microservicios), single vs multitenant, event-driven, brownfield vs greenfield** completan el capítulo.', 'otros'),
])

S('mesh', 'u5', 'Data Mesh', 'Dehghani, cap. 1, págs. 44–60', 'fig. 1-1, 1-2 y 1-3 · Notas, U5', [
    ('p', '**Data mesh es un enfoque sociotécnico descentralizado para compartir, acceder y gestionar datos analíticos en entornos complejos y de gran escala, dentro o entre organizaciones.**', 'def'),
    ('li', '**Resultados:** responder con gracia al cambio, sostener la agilidad al crecer y aumentar la relación valor/inversión.', 'outcomes'),
    ('table', [['Cambio', 'De', 'A'],
               ['Organizacional', 'Propiedad centralizada en especialistas', 'Propiedad descentralizada en los dominios'],
               ['Arquitectónico', 'Warehouses y lakes monolíticos', 'Malla distribuida de data products'],
               ['Tecnológico', 'Datos como subproducto del código', 'Datos y código como una unidad'],
               ['Operacional', 'Gobierno top-down centralizado', 'Gobierno federado computacional'],
               ['De principios', 'Datos como activo a recolectar', 'Datos como producto'],
               ['De infraestructura', 'Dos infraestructuras fragmentadas', 'Infraestructura integrada']], 'cambios'),
    ('callout', '**P6 del parcial 2025:** citar los cambios. **P7:** citar los principios.', 'examen'),
    ('li', '**1. Domain ownership:** la propiedad de los datos analíticos pasa a los dominios más cercanos a ellos.', 'p1'),
    ('li', '**2. Data as a product:** se comparten como producto. Atributos: descubrible, direccionable, comprensible, confiable y veraz, accesible de forma nativa, interoperable y componible, valioso por sí mismo y seguro. Unidad: **data quantum**.', 'p2'),
    ('li', '**3. Self-serve data platform:** servicios que bajan la carga cognitiva y el costo de la propiedad descentralizada.', 'p3'),
    ('li', '**4. Federated computational governance:** decisiones federadas entre dominios, plataforma y expertos; políticas codificadas y automatizadas.', 'p4'),
    ('li', '**Interplay (fig. 1-2):** los cuatro son colectivamente necesarios y suficientes. El ownership crea silos → lo compensa data as a product; duplica esfuerzo → la plataforma; trae incompatibilidad → el gobierno federado.', 'interplay'),
    ('li', '**Datos operacionales vs analíticos:** los operacionales (OLTP, «data on the inside») hacen funcionar el negocio; los analíticos (OLAP, «data on the outside») son históricos, integrados y agregados. Data mesh se enfoca en los analíticos.', 'datos'),
    ('li', '**Origen:** un cambio de paradigma (Kuhn) que adapta microservicios, Team Topologies y Zero Trust al mundo analítico.', 'origen'),
])

S('medallion', 'u5', 'Arquitectura Medallion', 'Strengholt, Building Medallion Architectures, cap. 1 (págs. 2–24) y cap. 3 (págs. 40–73)', 'fig. 1-1, 1-2, 1-8 y 3-1 · tabla 3-1 · Notas, U5', [
    ('p', '**Una arquitectura Medallion es un patrón de diseño de datos para organizar lógicamente los datos, casi siempre en un lakehouse, en tres capas, para mejorar de forma incremental la estructura y la calidad a medida que fluyen: Bronze ⇒ Silver ⇒ Gold.** La acuñó Databricks; no es una evolución de arquitecturas anteriores.', 'def'),
    ('table', [['Capa', 'Qué contiene', 'Modelo de datos', 'Transformaciones'],
               ['**Bronze**', 'Datos crudos de las fuentes en su estructura original; registro histórico inmutable', 'Esquema del sistema fuente', 'Mínimas: filtros, agregar metadata'],
               ['**Silver**', 'Datos limpios, estandarizados, deduplicados y validados; todavía granulares', 'Espejo de Bronze, por temas, 3FN o Data Vault', 'Historización (SCD2), datos de referencia, feature engineering'],
               ['**Gold**', 'Datos curados y agregados para el negocio', 'Kimball (estrella) u OBT', 'Armonización, agregación, lógica de negocio']], 'capas'),
    ('callout', '**P8 del parcial 2025:** «qué información debe ir en cada capa en menos de 30 palabras».', 'examen'),
    ('li', 'Las capas son **lógicas**: una puede tener varias subcapas físicas. Pueden existir una **landing zone** antes de Bronze y capas **curated, semánticas o Platinum** después de Gold.', 'logicas'),
    ('li', '**Diseño de tres capas (fig. 1-1):** proveedores → plataforma de distribución → consumidores, bajo una capa de metadata y gobierno. Medallion vive en la de distribución (fig. 1-2).', 'tres'),
    ('li', '**Lakehouse (fig. 1-8):** almacenamiento de objetos barato con transacciones ACID; Spark para cómputo y Delta Lake para almacenamiento. Proveedores: Databricks, Microsoft Fabric, Synapse, Cloudera, Dremio, Starburst.', 'lakehouse'),
    ('li', '**Crítica del autor:** no hay consenso sobre qué va en cada capa; hay que definir estándares y no olvidar el modelado de datos.', 'critica'),
])

S('patrones', 'u5', 'Patrones de diseño de ingeniería de datos (Konieczny)', 'Konieczny, caps. 1–10', 'Carpeta U5, marcados «OBLIGATORIO-TPI» · P5 del parcial 2025', [
    ('p', 'Un patrón es una **plantilla predefinida y personalizable para resolver un problema** (la receta del flan): tiene contexto, plantilla, reutilización, consecuencias y da un vocabulario común. Cada patrón del libro sigue el formato problema → solución → consecuencias → ejemplos.', 'def'),
    ('callout', 'La **P5 del parcial 2025** dijo «del libro de Kleppmann», pero el libro de patrones de la U5 es el de Konieczny.', 'kleppmann'),
    ('table', [['Capítulo', 'Patrones'],
               ['2 Ingesta', 'Full Loader, Incremental Loader, Change Data Capture, Passthrough y Transformation Replicator, Compactor, Readiness Marker, External Trigger'],
               ['3 Errores', 'Dead-Letter, Windowed Deduplicator, Late Data Detector, Static y Dynamic Late Data Integrator, Filter Interceptor, Checkpointer'],
               ['4 Idempotencia', 'Fast Metadata Cleaner, Data Overwrite, Merger, Stateful Merger, Keyed Idempotency, Transactional Writer, Proxy'],
               ['5 Valor', 'Static y Dynamic Joiner, Wrapper, Metadata Decorator, Distributed y Local Aggregator, Sessionizers, Orderers'],
               ['6 Flujo', 'Local e Isolated Sequencer, Aligned y Unaligned Fan-In, Parallel Split, Exclusive Choice, Single y Concurrent Runner'],
               ['7 Seguridad', 'Vertical Partitioner, In-Place Overwriter, Fine-Grained Accessor, Encryptor, Anonymizer, Pseudo-Anonymizer, Secrets Pointer, Secretless Connector'],
               ['8 Almacenamiento', 'Horizontal y Vertical Partitioner, Bucket, Sorter, Metadata Enhancer, Dataset Materializer, Manifest, Normalizer, Denormalizer'],
               ['9 Calidad', 'Audit-Write-Audit-Publish, Constraints Enforcer, Schema Compatibility Enforcer, Schema Migrator, Offline y Online Observer'],
               ['10 Observabilidad', 'Flow Interruption, Skew, Lag y SLA Misses Detector, Dataset y Fine-Grained Tracker']], 'catalogo'),
    ('li', '**Dead-Letter (respuesta modelo):** cuando un job no puede procesar un registro, lo captura (try-catch o if-else) y lo envía a otro destino con la metadata del error; el resto sigue. Ejemplo: eventos de Kafka con JSON mal formado van a «visitas_error». Consecuencia: más complejidad y hay que monitorear el destino.', 'deadletter'),
    ('li', '**Change Data Capture:** ingiere continuamente las filas modificadas leyendo el log de commits de la base; baja latencia. **Incremental Loader:** trae solo lo nuevo por una columna delta o por particiones de tiempo.', 'cdc'),
])

# ═══════════════════════════ U6 · Inteligencia Artificial Generativa
S('agentes', 'u6', 'Agentes de IA: definición y cuándo usarlos (Albada, cap. 1)', 'Albada, cap. 1, págs. 3–16', 'tabla 1-2 · P9 del parcial 2025', [
    ('p', '**Los agentes autónomos son sistemas inteligentes diseñados para analizar datos de forma independiente, interpretar su entorno y tomar decisiones basadas en el contexto.** La agencia es un espectro: la prueba de un agente real es que toma decisiones en vez de seguir scripts fijos.', 'def'),
    ('callout', '**P9 del parcial 2025** copiaba esta definición: verdadero.', 'examen'),
    ('li', '**Sistema agéntico:** herramientas, memoria, modelo fundacional, orquestación e infraestructura. Protocolos: MCP (herramientas) y A2A (entre agentes).', 'sistema'),
    ('li', '**Revolución del preentrenamiento:** antes había que juntar datos, entrenar y desplegar; hoy un modelo fundacional se usa con una llamada a una API.', 'pretrain'),
    ('li', '**Tipos (The Information):** de tareas de negocio, conversacionales, de investigación, de analítica, de desarrollo, de dominio específico y que usan el navegador; además, de voz y de video.', 'tipos'),
    ('li', '**De síncrono a asíncrono:** el humano pasa de ejecutor a gestor de tareas.', 'async'),
    ('table', [['Característica', 'Código tradicional', 'Workflow', 'Agente autónomo'],
               ['Input', 'Totalmente predecible', 'Mayormente predecible, ramas finitas', 'No estructurado o novedoso'],
               ['Explicabilidad', 'Total, auditable', 'Rama por rama', 'Caja negra'],
               ['Latencia', 'Ultra baja', 'Moderada', 'Mayor'],
               ['Adaptabilidad', 'Nula', 'Limitada', 'Alta']], 'tabla'),
    ('li', '**Regla:** transformación fija → código; pocas ramas conocidas → workflow; preguntas sobre documentos → chatbot o RAG (no decide acciones); alta variabilidad y planificación de varios pasos → agente.', 'regla'),
    ('li', '**Principios:** escalabilidad, modularidad, aprendizaje continuo, resiliencia y preparación para el futuro. **Frameworks:** LangGraph, AutoGen, CrewAI, OpenAI Agents SDK.', 'principios'),
])

S('disagentes', 'u6', 'Diseño de sistemas de agentes (Albada, cap. 2)', 'Albada, cap. 2, págs. 17–37', 'fig. 2-1', [
    ('p', 'Primer agente del libro: soporte de e-commerce que elige entre `cancel_order`, `issue_refund` y `update_address_for_order`. Clave: **acotar el alcance**. «Un agente no testeado es un agente no confiable».', 'ejemplo'),
    ('li', '**Componentes (fig. 2-1):** la **orquestación** coordina **modelo**, **herramientas**, **memoria** y **base de conocimiento**.', 'componentes'),
    ('li', '**Modelo:** grande para tareas abiertas (más caro y lento), chico para tareas repetitivas; modalidad; abierto vs cerrado.', 'modelo'),
    ('li', '**Herramientas:** locales, basadas en API y basadas en MCP; modulares.', 'tools'),
    ('li', '**Memoria:** corto plazo (sesión, ventana deslizante) y largo plazo (bases, knowledge graphs, fine-tuning).', 'memoria'),
    ('li', '**Trade-offs:** rendimiento (velocidad vs precisión), escalabilidad (GPUs), confiabilidad (tolerancia a fallas) y costos (desarrollo vs operación).', 'tradeoffs'),
    ('li', '**Single-agent** (simple) vs **multiagente** (especialización, paralelismo, escalabilidad, redundancia; contras: coordinación, complejidad, más tokens).', 'arq'),
    ('li', '**Buenas prácticas:** diseño iterativo, estrategia de evaluación (correctitud, casos borde, NPS/CSAT, tareas completadas) y pruebas reales.', 'practicas'),
])

S('rag', 'u6', 'RAG: pipelines y componentes (Kimothi, cap. 2)', 'Kimothi, cap. 2, págs. 1–12', 'fig. 2.1 a 2.7 · P10 del parcial 2025', [
    ('p', 'RAG (*retrieval-augmented generation*) recupera información relevante de una fuente externa y la agrega al prompt para que el LLM responda con contexto. **Cinco pasos:** pregunta → búsqueda → recuperación y aumentación → LLM → respuesta con contexto.', 'def'),
    ('table', [['', 'Indexing pipeline', 'Generation pipeline'],
               ['Para qué', 'Crear y mantener la base de conocimiento', 'Interacción en tiempo real'],
               ['Cuándo', 'Offline, va primero', 'Con cada consulta'],
               ['Componentes', 'Carga → splitting (chunking) → embeddings → base vectorial', 'Retriever → gestión del prompt → LLM']], 'pipelines'),
    ('li', '**Embeddings:** los datos de texto se convierten a formato numérico para la búsqueda y recuperación; los embeddings son el formato que mejor funciona.', 'emb'),
    ('callout', '**P10 del parcial 2025:** embeddings en RAG → verdadero.', 'examen'),
    ('li', 'El **retriever** es el componente más crítico y el que más latencia suma. No todo RAG necesita indexing pipeline: si la búsqueda la hace una API o el usuario aporta el documento.', 'retriever'),
    ('li', '**Componentes extra:** evaluación, monitoreo, caching (caché semántica), guardrails (políticas y ética), seguridad (prompt injection, data poisoning) y orquestación.', 'extras'),
    ('li', '**Tríada de evaluación (TruEra):** context relevance (contexto ↔ consulta), groundedness (respuesta ↔ contexto) y answer relevance (respuesta ↔ consulta).', 'triada'),
    ('li', '**RAGOps:** capas de datos, modelo, prompts, evaluación, orquestación, despliegue, aplicación y monitoreo.', 'ragops'),
])

S('ragret', 'u6', 'RAG: retrieval y evaluación (Huyen, cap. 6)', 'Huyen, AI Engineering, cap. 6, págs. 1–23', 'fig. 6-2 y 6-3', [
    ('p', 'Arquitectura básica (fig. 6-2): un **retriever** sobre memoria externa y un **modelo generativo**. El éxito depende sobre todo del retriever.', 'arq'),
    ('table', [['', 'Por términos (sparse)', 'Por embeddings (dense)'],
               ['Ejemplos', 'TF-IDF, BM25, Elasticsearch', 'Búsqueda vectorial (fig. 6-3)'],
               ['Velocidad', 'Más rápido', 'Más costoso'],
               ['Ajuste', 'Poco para tunear', 'Se puede fine-tunear'],
               ['Punto débil', 'No capta significado', 'Pierde palabras clave exactas']], 'tabla'),
    ('li', '**Evaluar:** context precision (de lo recuperado, cuánto es relevante) y context recall (de lo relevante, cuánto se recuperó); NDCG, MAP y MRR si importa el orden; benchmark MTEB.', 'eval'),
    ('li', '**Optimizar:** chunking, reranking, query rewriting y contextual retrieval. **Más allá del texto:** RAG multimodal y con tablas (text-to-SQL).', 'opt'),
])

S('huyen', 'u6', 'Agentes según Huyen y el rol del AI PM (Nika)', 'Huyen, cap. 6, págs. 23–54 · Nika, cap. 1, págs. 1–19', 'fig. 6-9, 6-12, 6-16 · fig. 1-1 y 1-4', [
    ('p', '**Agente (Huyen):** cualquier cosa que puede percibir su entorno y actuar sobre él. Se define por su **entorno** y sus **herramientas**. ChatGPT y un sistema RAG son agentes.', 'def'),
    ('li', '**Herramientas:** aumento de conocimiento, extensión de capacidades y **acciones de escritura** (las más riesgosas).', 'tools'),
    ('li', '**Planificación:** el modelo es el planificador; conviene desacoplar generar, validar y ejecutar el plan (fig. 6-9). **ReAct** intercala pensamiento, acción y observación (fig. 6-12); **Reflexion** agrega evaluación y autorreflexión.', 'plan'),
    ('li', '**Modos de falla:** de planificación, de herramientas y de eficiencia.', 'fallas'),
    ('li', '**Memoria (fig. 6-16):** conocimiento interno, corto plazo (contexto) y largo plazo (memoria externa con retriever). RAG y agentes son métodos basados en prompt.', 'memoria'),
    ('h', 'El rol del AI PM (Nika)'),
    ('li', '**Cuatro tipos de IA:** tradicional (1950s–hoy), generativa (fines 2010s–hoy), AGI (¿2030s?) y ASI (¿~2040s?).', 'tipos'),
    ('li', '**Rasgos de los productos de IA:** probabilísticos, dependientes de los datos, model drift, interpretabilidad, decisiones automatizadas y escalabilidad.', 'rasgos'),
    ('li', '**Skill set:** product management + fundamentos de ingeniería + liderazgo y colaboración + ciclo de vida de la IA. **Subtipos:** AI experiences PM, AI builder PM y AI-enhanced PM; 0-to-1 vs 1-to-n.', 'skills'),
    ('callout', 'Nika está en la bibliografía 2025 pero no en las notas de clase: prioridad baja hasta confirmarlo.', 'aviso'),
])
