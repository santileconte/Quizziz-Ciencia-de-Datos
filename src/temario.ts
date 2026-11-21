import type { UnitKey } from './lib/quiz'

// Temario del segundo parcial de Ciencia de Datos (Unidades 4, 5 y 6).
// Sigue el orden de las unidades y el hilo de la pestaña «Notas de clase» del documento de la materia.
// Las fuentes citan libro, capítulo y página del PDF de la carpeta de la unidad (no la página impresa del libro):
//   Zheng = «[Caps 1 y 3 OBLIGATORIOS] Zheng - Feature Engineering for ML.pdf» (cap. 1: págs. 2–4; cap. 3: págs. 40–64)
//   Ozdemir = «[OBLIGATORIO] Ozdemir - Feature Engineering Bookcamp.pdf» (cap. 1: págs. 1–12; cap. 2: págs. 13–34)
//   Strengholt DMS = «… Data Management at Scale - Chapter 4. Data Product Management.pdf»
//   Vajjala = «[OBLIGATORIO] Vajjala - Practical NLP.pdf» (caps. 1–4)
//   Reis 1/2/3 = «[OBLIGATORIO] Reis - Fundamentals of Data Engineering. Chapter N.pdf»
//   Dehghani = «[OBLIGATORIO CAP 1] Data Mesh … (Dehghani, Zhamak).pdf» (cap. 1: págs. 44–60)
//   Medallion = «[OBLIGATORIO] Strengholt - Building Medallion Architectures.pdf»
//   Konieczny N = «[OBLIGATORIO-TPI] Konieczny - Data Engineering Design Patterns - Chapter N.pdf»
//   Albada = «[OBLIGATORIO CAP 1 y 2] Michael Albada - Building Applications with AI Agents.pdf» (cap. 1: 3–16; cap. 2: 17–37)
//   Kimothi = «[OBLIGATORIO] Kimothi - A Simple Guide to Retrieval Augmented Generation.pdf» (cap. 2)
//   Huyen = «[OBLIGATORIO] AI_Engineering_Chapter_6_RAG_and_Agents.pdf»
//   Nika = «[OBLIGATORIO] Nika - Chapter 1. The Role of AI Product Managers 2.pdf»
//   Notas = pestaña «Notas de clase» · Biblio = pestaña «Bibliografía» (2025) · Parcial 2025 = pestaña del modelo de parcial

export const bloques: { key: UnitKey; unit: string; name: string; aviso?: string }[] = [
  { key: 'u4', unit: 'U4', name: 'Ciencia de Datos Aplicada' },
  { key: 'u5', unit: 'U5', name: 'Arquitecturas e Ingeniería de Datos' },
  { key: 'u6', unit: 'U6', name: 'Inteligencia Artificial Generativa' },
  {
    key: 'pend',
    unit: 'S/C',
    name: 'Sin confirmar o sin material',
    aviso: 'Temas nombrados en las notas o en la bibliografía de 2025 que no se pueden estudiar con los libros de las carpetas, o cuya inclusión no está confirmada.',
  },
]

/** A: muy probable · B: probable · C: alcanza con reconocerlo · Cond: condicional · Pend: sin confirmar. */
export type Prioridad = 'A' | 'B' | 'C' | 'Cond' | 'Pend'

export const prioridadLabel: Record<Prioridad, string> = {
  A: 'Prioridad A',
  B: 'Prioridad B',
  C: 'Prioridad C',
  Cond: 'Condicional',
  Pend: 'Sin confirmar',
}

export interface Tema {
  n: string
  bloque: UnitKey
  titulo: string
  prio: Prioridad
  /** Qué dice la bibliografía de 2025 sobre la fuente del tema. */
  biblio: string
  /** Por qué tiene esa prioridad: lo que dijo el profesor o lo que se tomó, con su fuente. */
  nota?: string
  fijar: string
  /** Qué hay sobre el tema en la pestaña «Notas de clase». */
  notas: string
  /** Libro de la cátedra, capítulo y páginas del PDF. */
  libro: string
  /** Nombres de tema que usan las preguntas de Cuestionarios. */
  temas: string[]
  mapa?: string
  graficos?: string[]
}

export const temario: Tema[] = [
  // ═══════════ U4 · Ciencia de Datos Aplicada
  { n: '01', bloque: 'u4', titulo: 'Machine learning y modelado predictivo', prio: 'B', biblio: 'Videos MIT (obligatorios) · Zheng cap. 1',
    nota: 'La clase dejó fuera la matemática: «No entra en el parcial: deja por fuera todo lo que es matemática» (Notas, U4). Clustering como no supervisado fue la P12 del 1er parcial, que ahora entra.',
    fijar: 'Modelado predictivo, modelo como artefacto, supervisado vs no supervisado y dónde trabaja el ML engineer.',
    notas: 'U4: predictive modeling, técnicas supervisadas y no supervisadas', libro: 'Zheng cap. 1, págs. 2–4 · Notas U2 (Huyen cap. 2) para supervisado/no supervisado',
    temas: ['Machine learning y modelado predictivo'], mapa: 'u4-ml', graficos: ['u4-01-pipeline-ml'] },
  { n: '02', bloque: 'u4', titulo: 'Feature y feature engineering', prio: 'A', biblio: 'Zheng caps. 1 y 3 · Ozdemir (obligatorios)',
    nota: 'Definir feature fue la P23 y «propiedad cuantitativa y medible» la P9 de las preguntas del 1er parcial que entran ahora.',
    fijar: 'Definición de feature (Zheng) y de feature engineering (Zheng y Ozdemir); cantidad de features; doble articulación.',
    notas: 'U4: features como data points que entrenan al modelo; feature engineering = manipular + transformar + representar', libro: 'Zheng cap. 1, págs. 3–4 · Ozdemir cap. 1, págs. 1–4',
    temas: ['Feature y feature engineering'], mapa: 'u4-fe', graficos: ['u4-02-pipeline-fe'] },
  { n: '03', bloque: 'u4', titulo: 'Tipos de features (MIT)', prio: 'A', biblio: 'Videos MIT 6.5 y 6.6 (obligatorios)',
    nota: 'Citar los tipos y dar un ejemplo fue la P10 (1,5 pts) y citarlos la P24 de las preguntas del 1er parcial que entran ahora. La fuente es el video MIT 6.6, no un PDF.',
    fijar: 'Identity, transform y aggregate, con un ejemplo propio de cada uno.',
    notas: 'U4: «Categorias features: identity, transform, aggregate»', libro: 'Video MIT 6.6 «Feature Types» (no está en PDF) · Notas U4',
    temas: ['Tipos de features'], mapa: 'u4-fe', graficos: ['u4-03-tipos-features'] },
  { n: '04', bloque: 'u4', titulo: 'Model-centric vs data-centric y pipeline de ML', prio: 'A', biblio: 'Ozdemir (obligatorio)',
    nota: 'El profesor trabajó el contraste con el laboratorio Avengers (Notas, U4).',
    fijar: 'Comparar los dos enfoques, los 5 pasos del pipeline de ML y los 4 del de feature engineering; qué NO puede hacer el FE.',
    notas: 'U4: tabla model-centric vs data-centric, lab Avengers, beneficios y límites, flujo de FE', libro: 'Ozdemir cap. 1, págs. 1–9 (fig. 1.1, 1.2 y 1.5)',
    temas: ['Model-centric vs data-centric'], mapa: 'u4-fe', graficos: ['u4-04-model-vs-data', 'u4-01-pipeline-ml', 'u4-02-pipeline-fe'] },
  { n: '05', bloque: 'u4', titulo: 'Data drift y concept drift', prio: 'B', biblio: 'Ozdemir (obligatorio)',
    fijar: 'Distinguir cambio de distribución y cambio de relación feature-objetivo, con un ejemplo de cada uno.',
    notas: 'U4: data drift vs concept drift con ejemplos de los Avengers; «MLOps es el que trabaja esto»', libro: 'Ozdemir cap. 1, págs. 6–7',
    temas: ['Data drift y concept drift'], mapa: 'u4-fe' },
  { n: '06', bloque: 'u4', titulo: 'Datos estructurados y niveles de datos', prio: 'A', biblio: 'Ozdemir (obligatorio)',
    fijar: 'Nominal, ordinal, intervalo y razón: qué operaciones admite cada uno y cómo se trata.',
    notas: 'U4: «Niveles de datos: nominal (frecuencia, moda, gráficos de barra, one-hot)… ordinal, intervalo, razón»', libro: 'Ozdemir cap. 2, págs. 13–23 (fig. 2.6)',
    temas: ['Niveles de datos'], mapa: 'u4-niveles', graficos: ['u4-05-niveles-datos'] },
  { n: '07', bloque: 'u4', titulo: 'Tipos de feature engineering y evaluación', prio: 'A', biblio: 'Ozdemir (obligatorio)',
    nota: 'No confundir con los tipos de features del video MIT (tema 03).',
    fijar: 'Mejora, construcción, selección, extracción y aprendizaje; las cuatro formas de evaluar.',
    notas: 'U4: los 5 tipos y «¿Cómo evaluamos la ingeniería de características?»', libro: 'Ozdemir cap. 2, págs. 24–34',
    temas: ['Tipos de feature engineering'], mapa: 'u4-niveles', graficos: ['u4-06-tipos-fe'] },
  { n: '08', bloque: 'u4', titulo: 'Texto como features (Zheng cap. 3)', prio: 'B', biblio: 'Zheng cap. 3 (obligatorio)',
    fijar: 'Bag-of-words, n-gramas, stopwords, filtrado por frecuencia, stemming, colocaciones.',
    notas: 'Resumen del cap. 3 en las notas', libro: 'Zheng cap. 3, págs. 40–64 (fig. 3-1)',
    temas: ['Texto como features'], mapa: 'u4-texto' },
  { n: '09', bloque: 'u4', titulo: 'NLP: tareas, bloques del lenguaje y enfoques', prio: 'A', biblio: 'Vajjala (obligatorio, «ver qué caps son») · Video MIT 1.1',
    nota: 'En clase se marcaron cuatro gráficos: tareas de fácil a difícil, bloques del lenguaje, círculos IA/ML/DL/NLP y pipeline genérico (Notas, U4).',
    fijar: 'Tareas de fácil a difícil, bloques del lenguaje y sus aplicaciones, relación IA/ML/DL/NLP, RNN y LSTM.',
    notas: 'U4 Minería de texto: core tasks / general / industry specific; gráficos; POS, parsing, coreference; RNN y LSTM', libro: 'Vajjala cap. 1, págs. 2–31',
    temas: ['NLP: tareas y enfoques'], mapa: 'u4-nlp', graficos: ['u4-07-bloques-lenguaje', 'u4-08-ia-ml-dl'] },
  { n: '10', bloque: 'u4', titulo: 'Pipeline de NLP y preprocesamiento', prio: 'A', biblio: 'Vajjala (obligatorio)',
    fijar: 'Las ocho etapas del pipeline genérico; stemming vs lematización; POS, parsing y correferencia.',
    notas: 'U4: «gráfico generic nlp pipeline», stemming/lemmatization', libro: 'Vajjala cap. 2, págs. 32–75 (fig. 2-1, 2-7, 2-8)',
    temas: ['Pipeline de NLP'], mapa: 'u4-nlp', graficos: ['u4-09-pipeline-nlp'] },
  { n: '11', bloque: 'u4', titulo: 'Representación y clasificación de texto', prio: 'C', biblio: 'Vajjala (obligatorio)',
    nota: 'Las notas mencionan «Vajjala - Practical NLP (Capítulo 1 a 4)» y los word embeddings, sin desarrollar estos capítulos.',
    fijar: 'BoW/TF-IDF vs embeddings (CBOW y SkipGram); pipeline de clasificación.',
    notas: 'U4: «Text Classification: Word Embeddings»', libro: 'Vajjala cap. 3, págs. 76–108 · cap. 4, págs. 109–146',
    temas: ['Representación y clasificación de texto'], mapa: 'u4-nlp' },
  { n: '12', bloque: 'u4', titulo: 'Sistemas de recomendación, cross validation y RMSE', prio: 'B', biblio: 'Videos de recomendación 4.1–4.2 (obligatorios)',
    nota: 'Las notas dicen «Estudiar cross validation y root mean squared error».',
    fijar: 'Filtrado colaborativo usuario-usuario e ítem-ítem, active learning, cross validation y RMSE.',
    notas: 'U4: sistemas de recomendación, active learning, cross validation, RMSE', libro: 'Videos MIT 4.1–4.2 (no están en PDF) · Ejercicio Surprise (notebook de la carpeta U4) · Zheng cap. 1, pág. 3',
    temas: ['Sistemas de recomendación'], mapa: 'u4-recom', graficos: ['u4-10-cross-validation'] },
  { n: '13', bloque: 'u4', titulo: 'Data products (Strengholt)', prio: 'A', biblio: 'Strengholt DMS cap. 4 (obligatorio)',
    nota: 'Data as a product vs data product fue la P8 de las preguntas del 1er parcial que entran ahora.',
    fijar: 'Mindset vs arquitectura; definición lógica; CQRS; principios de diseño.',
    notas: 'Resumen del cap. 4 en las notas (marcado «no terminado»)', libro: 'Strengholt DMS cap. 4, págs. 1–37 (fig. 4-1, 4-2, 4-3, 4-5)',
    temas: ['Data products'], mapa: 'u4-dp', graficos: ['u4-11-cqrs'] },

  // ═══════════ U5 · Arquitecturas e Ingeniería de Datos
  { n: '14', bloque: 'u5', titulo: 'Qué es la ingeniería de datos', prio: 'A', biblio: 'Reis cap. 1 (obligatorio)',
    nota: 'La definición fue la P1 del parcial 2025.',
    fijar: 'Definición textual, evolución, madurez de datos, tipos A y B, stakeholders.',
    notas: 'U5: «Que hace un ingeniero de datos?»; «mucha info falta acá, ver del libro»', libro: 'Reis cap. 1, págs. 1–27 (fig. 1-1, 1-5, 1-8, 1-12)',
    temas: ['Ingeniería de datos'], mapa: 'u5-de', graficos: ['u5-01-ciclo-vida', 'u5-02-piramide'] },
  { n: '15', bloque: 'u5', titulo: 'Ciclo de vida y corrientes subyacentes', prio: 'A', biblio: 'Reis cap. 2 (obligatorio)',
    nota: 'Las etapas fueron la P2 y batch vs streaming la P3 del parcial 2025. Las notas piden el «gráfico de ciclo de vida del dato».',
    fijar: 'Cinco etapas, seis corrientes, batch vs streaming, push vs pull, tipos de analytics, reverse ETL, pilares de DataOps.',
    notas: 'U5: «*grafico de ciclo de vida del dato»', libro: 'Reis cap. 2, págs. 1–33 (fig. 2-1, 2-2, 2-5, 2-6, 2-8)',
    temas: ['Ciclo de vida de la ingeniería de datos'], mapa: 'u5-ciclo', graficos: ['u5-01-ciclo-vida'] },
  { n: '16', bloque: 'u5', titulo: 'Arquitectura de datos y sus principios', prio: 'A', biblio: 'Reis cap. 3 (obligatorio)',
    nota: 'La arquitectura de negocios como parte de la de datos fue la P4 del parcial 2025. Las notas piden el «gráfico enterprise architecture».',
    fijar: 'Arquitectura empresarial y sus subconjuntos; operacional vs técnica; los 9 principios; puertas de una y dos vías.',
    notas: 'U5: «grafico enterprise architecture (entenderlo como se relacionan todas las arquitecturas)»', libro: 'Reis cap. 3, págs. 1–13 (fig. 3-1, 3-2)',
    temas: ['Arquitectura de datos'], mapa: 'u5-arq', graficos: ['u5-03-arq-empresarial'] },
  { n: '17', bloque: 'u5', titulo: 'Warehouse, lake, lakehouse, Lambda y Kappa', prio: 'A', biblio: 'Reis cap. 3 · Medallion cap. 1 (obligatorios)',
    nota: '«Data Warehouse = fuente única de la verdad» fue la P14 de las preguntas del 1er parcial que entran ahora.',
    fijar: 'DWH (ETL/ELT, data marts), data lake, lakehouse, Inmon vs Kimball, Lambda vs Kappa, modern data stack.',
    notas: 'U5: patrones de diseño arquitecturales', libro: 'Reis cap. 3, págs. 23–34 (fig. 3-10 a 3-15) · Medallion cap. 1, págs. 5–23 (fig. 1-4 a 1-8)',
    temas: ['Patrones de arquitectura de datos'], mapa: 'u5-arq', graficos: ['u5-04-lambda-kappa'] },
  { n: '18', bloque: 'u5', titulo: 'Data Mesh', prio: 'A', biblio: 'Dehghani cap. 1 (obligatorio)',
    nota: 'Citar los cambios (P6) y los principios (P7) valieron 3 puntos en el parcial 2025.',
    fijar: 'Definición, tres resultados, seis cambios, cuatro principios y cómo se compensan.',
    notas: 'U5: «Data mesh»', libro: 'Dehghani cap. 1, págs. 44–60 (fig. 1-1, 1-2, 1-3)',
    temas: ['Data Mesh'], mapa: 'u5-mesh', graficos: ['u5-05-mesh-principios', 'u5-06-mesh-cambios'] },
  { n: '19', bloque: 'u5', titulo: 'Arquitectura Medallion', prio: 'A', biblio: 'Medallion (obligatorio, «ver qué caps son»)',
    nota: 'Qué va en cada capa fue la P8 del parcial 2025 (1,5 pts). Las notas piden el «gráfico que tiene la medallion arquitectura».',
    fijar: 'Bronze, Silver y Gold: contenido, modelo de datos y transformaciones; landing y capas extra.',
    notas: 'U5: «*grafico que tiene la medalloin arquitectura»; U1: esquema Medallion', libro: 'Medallion cap. 1, págs. 2–4 y 21–24 · cap. 3, págs. 40–73 (fig. 1-2, 3-1, tabla 3-1)',
    temas: ['Arquitectura Medallion'], mapa: 'u5-medallion', graficos: ['u5-07-medallion'] },
  { n: '20', bloque: 'u5', titulo: 'Patrones de diseño de ingeniería de datos', prio: 'B', biblio: 'No figura en la bibliografía 2025: la carpeta los marca «OBLIGATORIO-TPI»',
    nota: 'La P5 del parcial 2025 pidió «1 patrón de data engineering del libro de Kleppmann»; el único libro de patrones de la U5 es el de Konieczny.',
    fijar: 'Qué es un patrón (receta del flan) y poder describir uno en menos de 50 palabras con un ejemplo.',
    notas: 'No figura', libro: 'Konieczny caps. 1–10 (cap. 1: págs. 1–6; Dead-Letter en cap. 3)',
    temas: ['Patrones de diseño de ingeniería de datos'], mapa: 'u5-patrones' },

  // ═══════════ U6 · Inteligencia Artificial Generativa
  { n: '21', bloque: 'u6', titulo: 'Agentes de IA: definición y cuándo usarlos', prio: 'A', biblio: 'Albada caps. 1 y 2 (obligatorio)',
    nota: 'La definición de agente autónomo de Albada fue la P9 del parcial 2025.',
    fijar: 'Definición literal, tipos de agentes, código vs workflow vs RAG vs agente, principios y frameworks.',
    notas: 'U6: «Ai as a service y otros dos» (sin desarrollar)', libro: 'Albada cap. 1, págs. 3–16 (tabla 1-2)',
    temas: ['Agentes de IA'], mapa: 'u6-agentes', graficos: ['u6-01-codigo-workflow-agente'] },
  { n: '22', bloque: 'u6', titulo: 'Diseño de sistemas de agentes', prio: 'B', biblio: 'Albada caps. 1 y 2 (obligatorio)',
    fijar: 'Componentes centrales, tipos de herramientas, memoria corta y larga, trade-offs, single vs multiagente.',
    notas: 'No hay notas específicas', libro: 'Albada cap. 2, págs. 17–37 (fig. 2-1)',
    temas: ['Diseño de sistemas de agentes'], mapa: 'u6-agentes', graficos: ['u6-02-componentes-agente'] },
  { n: '23', bloque: 'u6', titulo: 'RAG: pipelines y componentes', prio: 'A', biblio: 'Kimothi (obligatorio)',
    nota: 'Embeddings en RAG fue la P10 del parcial 2025. Las notas nombran «Cuando y porque utilizar RAG (pirámide)» y «RAG 1.0, RAG 2.0», que no están en los libros (ver S/C).',
    fijar: 'Los cinco pasos, indexing vs generation pipeline, componentes, tríada de evaluación y RAGOps.',
    notas: 'U6: RAG (pirámide, RAG 1.0 y 2.0)', libro: 'Kimothi cap. 2, págs. 1–12 (fig. 2.1 a 2.7)',
    temas: ['RAG: pipelines y componentes'], mapa: 'u6-rag', graficos: ['u6-03-rag-pipelines', 'u6-04-triada-rag'] },
  { n: '24', bloque: 'u6', titulo: 'RAG: retrieval y evaluación (Huyen)', prio: 'B', biblio: 'AI Engineering cap. 6 (obligatorio)',
    nota: 'Está en la bibliografía 2025 y en la carpeta U6; las notas no lo nombran.',
    fijar: 'Retrieval por términos vs por embeddings, context precision/recall, chunking, reranking, query rewriting.',
    notas: 'No figura por nombre', libro: 'Huyen cap. 6, págs. 1–23 (fig. 6-2, 6-3)',
    temas: ['RAG: retrieval'], mapa: 'u6-rag' },
  { n: '25', bloque: 'u6', titulo: 'Agentes según Huyen: herramientas, planificación y memoria', prio: 'B', biblio: 'AI Engineering cap. 6 (obligatorio)',
    nota: 'Está en la bibliografía 2025 y en la carpeta U6; las notas no lo nombran.',
    fijar: 'Definición (entorno + acciones), tres tipos de herramientas, ReAct y Reflexion, modos de falla, jerarquía de memoria.',
    notas: 'No figura por nombre', libro: 'Huyen cap. 6, págs. 23–52 (fig. 6-9, 6-12, 6-16)',
    temas: ['Agentes según Huyen'], mapa: 'u6-huyen', graficos: ['u6-05-memoria'] },
  { n: '26', bloque: 'u6', titulo: 'El rol del AI Product Manager', prio: 'C', biblio: 'Nika cap. 1 (obligatorio)',
    nota: 'Está en la bibliografía 2025 y en la carpeta U6, pero las notas de clase no lo mencionan: prioridad baja hasta confirmarlo.',
    fijar: 'Los cuatro tipos de IA, rasgos de los productos de IA, skill set y subtipos de AI PM.',
    notas: 'No figura', libro: 'Nika cap. 1, págs. 1–19 (fig. 1-1, 1-4)',
    temas: ['Rol del AI PM'], mapa: 'u6-huyen', graficos: ['u6-06-tipos-ia'] },

  // ═══════════ Sin confirmar o sin material
  { n: 'P1', bloque: 'pend', titulo: 'Temas de clase que no están en los libros', prio: 'Pend', biblio: 'No figuran',
    nota: 'Salen de las diapositivas, que no están en las carpetas: data fabric («integrated layer of connected data»), «AI as a service y otros dos», la pirámide de cuándo usar RAG y RAG 1.0 / RAG 2.0. Hace falta el material de clase para estudiarlos.',
    fijar: 'Solo con el material de clase.', notas: 'U5 y U6 (menciones sueltas)', libro: '—', temas: ['Sin material'] },
  { n: 'P2', bloque: 'pend', titulo: 'Libros nombrados en las notas que no están en las carpetas', prio: 'Pend', biblio: 'No figuran',
    nota: 'Las notas citan «Designing LLM applications, RAGs (capítulo 12) forma parte de la unidad 6» y «O\'reilly del canguro (CAP 1)». Ninguno está en la carpeta U6 y no se pudo identificar el segundo.',
    fijar: 'Solo si la cátedra lo confirma.', notas: 'Final de la pestaña de notas', libro: '—', temas: ['Sin material'] },
]

/** Orden del temario para listar los temas de las preguntas. */
const orden = new Map(temario.flatMap((t, i) => t.temas.map((x, k) => [x, i * 10 + k] as const)))
export const ordenTema = (tema: string) => orden.get(tema) ?? 9999
export const temaDe = (tema: string) => temario.find((t) => t.temas.includes(tema))
