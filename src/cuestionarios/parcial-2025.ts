import type { ItemDef, UnitKey } from '../lib/quiz'

// Segundo Examen Parcial – Ciencia de Datos. UTN – Facultad Regional Resistencia · Fecha: 25/11/2025.
// Transcripción literal de la pestaña «Parcial» (modelo de parcial del año pasado) del documento de la materia.
// Solo se quitaron las barras invertidas que agrega la exportación de Google Docs (\- y 1\.) y las letras «a)», «b)»…
// de las opciones, que la app vuelve a poner. No se corrigió ortografía, puntuación ni contenido.
//
// El documento NO trae las claves: la transcripción aclara que copia las consignas «sin tener en cuenta las respuestas
// que aparecen marcadas en la hoja». Por eso todas llevan `dud`: se pueden responder y muestran una clave propuesta
// con su fuente, pero no suman puntaje ni progreso hasta que las confirmes en `verificadas.ts`.
const SRC = 'Segundo parcial 25/11/2025 (pestaña «Parcial» del documento de la materia)'
const src = (p: string, pts: string) => `${SRC} · ${p} (${pts})`
const SIN_CLAVE = 'el documento no trae las respuestas marcadas en la hoja; la clave propuesta sale del libro citado'

export const parcial2025: (ItemDef & { unit: UnitKey; id: string })[] = [
  {
    id: 'pc25-01', unit: 'u5', t: 'mc', tema: 'Ingeniería de datos', src: src('Pregunta 1', '0,5 puntos'),
    q: 'Según el libro de Reis et al., ¿cómo se define la ingeniería de datos?',
    o: [
      'Como el proceso de análisis de grandes volúmenes de datos mediante aprendizaje automático.',
      'Como la ciencia que se dedica a visualizar datos de forma eficiente.',
      'Como el desarrollo, implementación y mantenimiento de sistemas de inteligencia analítica.',
      'Como el conjunto de herramientas para crear dashboards interactivos.',
      'Todas las anteriores en conjunto definen a la ingeniería de datos.',
      'Ninguna es correcta.',
    ],
    a: 2,
    dud: `${SIN_CLAVE} (Reis, cap. 1, pág. 2).`,
    e: 'Reis: «Data engineering is the development, implementation, and maintenance of systems and processes that take in raw data and produce high-quality, consistent information…». La opción c es la única que retoma «desarrollo, implementación y mantenimiento», aunque el libro dice «sistemas y procesos», no «sistemas de inteligencia analítica». Por esa diferencia, alguien podría defender «Ninguna es correcta»: confirmalo con la corrección del parcial.',
    ref: 'Reis, cap. 1, pág. 2 del PDF (Data Engineering Defined).',
  },
  {
    id: 'pc25-02', unit: 'u5', t: 'mc', tema: 'Ciclo de vida de la ingeniería de datos', src: src('Pregunta 2', '0,5 puntos'),
    q: 'Según el libro de Reis et al., ¿cuáles son las etapas del Data Engineering Lifecycle?',
    o: [
      'Captura, almacenamiento, visualización, modelado y consumo.',
      'Generación, almacenamiento, ingesta, transformación y servicio (serving).',
      'Extracción, limpieza, modelado, entrenamiento y despliegue (deployment).',
      'Obtención, normalización, validación, presentación y explotación.',
      'Ninguna es correcta.',
    ],
    a: 1,
    dud: `${SIN_CLAVE} (Reis, cap. 1, pág. 3, y cap. 2, pág. 1).`,
    e: 'Las cinco etapas son generation, storage, ingestion, transformation y serving data.',
    ref: 'Reis, cap. 1, pág. 3 y cap. 2, págs. 1–2 del PDF (fig. 1-1 y 2-1).',
  },
  {
    id: 'pc25-03', unit: 'u5', t: 'mc', tema: 'Ciclo de vida de la ingeniería de datos', src: src('Pregunta 3', '1 punto'),
    q: 'Según el libro de Reis et al., ¿qué diferencia existe entre batch ingestion y streaming ingestion?',
    o: [
      'Batch procesa datos en tiempo real; streaming agrupa datos en lotes.',
      'Batch procesa datos periódicamente en bloques; streaming los transmite de manera continua.',
      'Streaming se usa solo en IoT; batch solo en cloud.',
      'No hay diferencias técnicas, solo de nombre.',
      'Ninguna es correcta.',
    ],
    a: 1,
    dud: `${SIN_CLAVE} (Reis, cap. 2, págs. 8–9).`,
    e: 'Batch ingiere por intervalo de tiempo o al llegar a un tamaño; streaming entrega los datos de forma continua, casi en tiempo real.',
    ref: 'Reis, cap. 2, págs. 8–9 del PDF (Batch versus streaming).',
  },
  {
    id: 'pc25-04', unit: 'u5', t: 'mc', tema: 'Arquitectura de datos', src: src('Pregunta 4', '0,5 puntos'),
    q: 'Según el libro de Reis et al., la arquitectura de negocios (business architecture) debe considerarse como parte de la arquitectura de datos de la organización.',
    o: ['Verdadero ( )', 'Falso ( )'],
    a: 1,
    dud: `${SIN_CLAVE} (Reis, cap. 3, pág. 1, fig. 3-1).`,
    e: 'En la fig. 3-1 la arquitectura empresarial tiene cuatro subconjuntos al mismo nivel: de negocio, técnica, de aplicaciones y de datos. La de negocio no está dentro de la de datos. Ojo: la de datos sí debe servir a los objetivos del negocio, y por eso la consigna puede leerse de otra forma.',
    ref: 'Reis, cap. 3, págs. 1–4 del PDF (fig. 3-1).',
  },
  {
    id: 'pc25-05', unit: 'u5', t: 'dev', tema: 'Patrones de diseño de ingeniería de datos', src: src('Pregunta 5', '1,5 puntos'),
    q: 'Describa en menos de 50 palabras 1 patrón de data engineering del libro de Kleppmann. Además, elabore un ejemplo para explicar su uso.',
    m: 'Ejemplo con el patrón Dead-Letter (Konieczny, cap. 3): cuando un job no puede procesar un registro, en lugar de fallar entero lo captura (try-catch o if-else) y lo envía a otro destino con metadata del error para analizarlo después; el resto sigue procesándose. Ejemplo: un job de streaming lee visitas de Kafka; los eventos con JSON mal formado van a la tabla «visitas_error» con el mensaje de la excepción y se monitorea su cantidad.',
    k: ['Nombre del patrón y el problema que resuelve', 'La solución en menos de 50 palabras', 'Un ejemplo concreto de uso', 'Alguna consecuencia o costo (opcional)'],
    dud: 'el documento no trae la respuesta y la consigna nombra a Kleppmann, pero el libro de patrones de la U5 es el de Konieczny: falta confirmar qué libro esperaba la cátedra.',
    nota: 'Se conserva «Kleppmann» tal como figura en la transcripción. Kleppmann (Designing Data-Intensive Applications) es bibliografía de las Unidades 1 y 2, que no está en estas carpetas.',
    ref: 'Konieczny, cap. 1 (qué es un patrón) y cap. 3 (Dead-Letter).',
  },
  {
    id: 'pc25-06', unit: 'u5', t: 'dev', tema: 'Data Mesh', src: src('Pregunta 6', '1,5 puntos'),
    q: 'Cite (solo cite) los cambios (en TI) propuestos por Data Mesh.',
    recon: 'según la transcripción, la expresión entre paréntesis «(en TI)» es la parte menos legible de la fotografía.',
    m: 'Organizacional, arquitectónico, tecnológico, operacional, de principios (valores) y de infraestructura. (Dehghani: «organizationally, architecturally, technologically, operationally, principally, infrastructurally».)',
    k: ['Organizacional', 'Arquitectónico', 'Tecnológico', 'Operacional', 'De principios', 'De infraestructura'],
    dud: `${SIN_CLAVE} (Dehghani, cap. 1, págs. 45–46, fig. 1-1).`,
    ref: 'Dehghani, cap. 1, págs. 45–47 del PDF (The Shifts, fig. 1-1).',
  },
  {
    id: 'pc25-07', unit: 'u5', t: 'dev', tema: 'Data Mesh', src: src('Pregunta 7', '1,5 puntos'),
    q: 'Cite (solo cite) los principios en los que se basa Data Mesh.',
    m: 'Propiedad del dominio (domain ownership), datos como producto (data as a product), plataforma de datos self-serve y gobierno computacional federado.',
    k: ['Domain ownership', 'Data as a product', 'Self-serve data platform', 'Federated computational governance'],
    dud: `${SIN_CLAVE} (Dehghani, cap. 1, págs. 48–52).`,
    ref: 'Dehghani, cap. 1, págs. 48–54 del PDF (The Principles, fig. 1-2).',
  },
  {
    id: 'pc25-08', unit: 'u5', t: 'dev', tema: 'Arquitectura Medallion', src: src('Pregunta 8', '1,5 puntos'),
    q: 'Describa en menos de 30 palabras qué información debe ir en cada una de las capas de una arquitectura medallón.',
    m: 'Bronze: datos crudos de las fuentes, en su estructura original e inmutables. Silver: datos limpios, estandarizados, deduplicados y validados, todavía granulares. Gold: datos agregados y enriquecidos con lógica de negocio, listos para reportes y decisiones.',
    k: ['Bronze: crudos, como vienen de la fuente', 'Silver: limpios, validados y estandarizados', 'Gold: agregados y optimizados para el negocio', 'Menos de 30 palabras por capa'],
    dud: `${SIN_CLAVE} (Strengholt, Building Medallion Architectures, cap. 3, págs. 40–41).`,
    ref: 'Medallion, cap. 1, págs. 3–4 y cap. 3, págs. 40–41 del PDF (fig. 3-1, tabla 3-1).',
  },
  {
    id: 'pc25-09', unit: 'u6', t: 'mc', tema: 'Agentes de IA', src: src('Pregunta 9', '1 punto'),
    q: 'Según el autor Albada, los agentes autónomos son sistemas inteligentes diseñados para analizar datos de forma independiente, interpretar su entorno y tomar decisiones basadas en el contexto.',
    o: ['Verdadero ( )', 'Falso ( )'],
    a: 0,
    dud: `${SIN_CLAVE} (Albada, cap. 1, pág. 3).`,
    e: 'Es casi la definición textual: «Autonomous agents are intelligent systems designed to independently analyze data, interpret their environment, and make context-driven decisions».',
    ref: 'Albada, cap. 1, pág. 3 del PDF (Defining AI Agents).',
  },
  {
    id: 'pc25-10', unit: 'u6', t: 'mc', tema: 'RAG: pipelines y componentes', src: src('Pregunta 10', '0,5 puntos'),
    q: 'En los sistemas RAG usan un proceso llamado embeddings para convertir los datos textuales a un formato numérico para los cálculos de búsqueda y recuperación.',
    o: ['Verdadero ( )', 'Falso ( )'],
    a: 0,
    dud: `${SIN_CLAVE} (Kimothi, cap. 2, págs. 7–8).`,
    e: 'Kimothi: los datos de texto deben convertirse a formato numérico para la búsqueda y recuperación, y los embeddings son el formato que mejor funciona. En rigor, el embedding es el formato (la conversión la hace un modelo de embeddings), pero la afirmación coincide con el libro.',
    ref: 'Kimothi, cap. 2, págs. 7–8 del PDF (Data conversion).',
  },
  {
    id: 'pc25-extra', unit: 'u6', t: 'dev', tema: 'Agentes de IA', src: src('Extra', '0,5 puntos'),
    q: 'Por un bonus de 0,5 puntos, complete el meme. Debe representar lo que se ha dado en clase y no puede ser una explicación de múltiples palabras.',
    recon: 'la transcripción no incluye la imagen del meme.',
    m: 'No hay respuesta modelo: falta la imagen del meme. Cualquier concepto de clase en una o dos palabras (por ejemplo «Bronze → Silver → Gold» o «Garbage in, garbage out»).',
    dud: 'falta la imagen del meme en el documento.',
    ref: 'Sin fuente: depende de la imagen.',
  },
]
