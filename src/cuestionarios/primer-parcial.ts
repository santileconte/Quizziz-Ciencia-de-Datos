import type { ItemDef, UnitKey } from '../lib/quiz'

// Preguntas que un compañero marcó en la pestaña «Parcial» del documento de la materia con la nota
// «preguntas de 1er parcial que entran ahora» (comentario de Matias Rodriguez Scornik). Se copian con su número y su
// puntaje tal como figuran. Solo se quitaron las barras invertidas de la exportación de Google Docs, los asteriscos de
// negrita (preguntas 23 y 24) y las letras «a)», «b)»… de las opciones.
//
// El documento no trae claves: todas llevan `dud` hasta que las confirmes.
const SRC = 'Pestaña «Parcial», bloque «preguntas de 1er parcial que entran ahora»'
const SIN_CLAVE = 'el documento no trae la respuesta; la clave propuesta sale de la fuente citada'

export const primerParcial: (ItemDef & { unit: UnitKey; id: string })[] = [
  {
    id: 'pp-08', unit: 'u4', t: 'mc', tema: 'Data products', src: `${SRC} · Pregunta 8 (0.5 punto)`,
    q: 'Según el autor Strengholt, en el capítulo 4 del libro Data Management at Scale ¿Qué diferencia principal existe entre "data as a product" y "data product"? (0.5 punto)',
    o: [
      'Una se refiere a como pensamos los datos y la otra a la arquitectura.',
      'Son sinónimos.',
      '"Data product" describe solo datasets físicos.',
      '"Data as a product" incluye únicamente el código fuente.',
      'El libro no trata este tema',
    ],
    a: 0,
    dud: `${SIN_CLAVE} (Strengholt, Data Management at Scale, cap. 4, pág. 1 del PDF).`,
    e: '«Data as a product» describe una forma de pensar; «data product» aborda la arquitectura.',
    ref: 'Strengholt DMS, cap. 4, págs. 1–2 del PDF.',
  },
  {
    id: 'pp-09', unit: 'u4', t: 'mc', tema: 'Feature y feature engineering', src: `${SRC} · Pregunta 9 (0.5 punto)`,
    q: 'Una feature en el ámbito de feature engineering es una propiedad cuantitativa y medible de una entidad particular ¿verdadero o falso? (0.5 punto)',
    o: ['Verdadero', 'Falso'],
    a: 0,
    dud: `${SIN_CLAVE} (videos MIT 6.5–6.6 y Zheng, cap. 1).`,
    e: 'Zheng la define como una representación numérica de datos crudos; en clase y en el material de la Unidad 2 se la describe como una propiedad medible de una entidad (edad, monto, frecuencia de compra). Las dos definiciones apuntan a lo mismo.',
    ref: 'Zheng, cap. 1, pág. 3 del PDF · Notas, U2 («¿Qué es una feature?»).',
  },
  {
    id: 'pp-10', unit: 'u4', t: 'dev', tema: 'Tipos de features', src: `${SRC} · Pregunta 10 (1.5 puntos)`,
    q: 'En el ámbito de Feature Engineering, cite los tipos de features que existen. Seleccione 1 de ellos y proponga 1 ejemplo. Explique en menos de 50 palabras este ejemplo. (1.5 puntos)',
    m: 'Identity features, transform features y aggregate features. Ejemplo (aggregate): para predecir si un cliente abandona, se cuenta cuántas compras hizo en los últimos 30 días. Cada compra suelta no dice mucho; el conteo resume su comportamiento reciente y da una señal directa de abandono.',
    k: ['Identity', 'Transform', 'Aggregate', 'Un ejemplo de uno de ellos', 'Explicación de menos de 50 palabras'],
    dud: `${SIN_CLAVE} (video MIT 6.6 «Feature Types» y Notas, U4). El video no está en PDF y no se pudo cotejar.`,
    ref: 'Video MIT 6.6 · Notas, U4 («Categorias features»).',
  },
  {
    id: 'pp-12', unit: 'u4', t: 'mc', tema: 'Machine learning y modelado predictivo', src: `${SRC} · Pregunta 12 (0.5 punto)`,
    q: 'Clustering es una disciplina que trata de crear agrupaciones de datos de acuerdo con similaridades siguiendo un enfoque de aprendizaje supervisado ¿verdadero o falso? (0.5 punto)',
    o: ['Verdadero', 'Falso'],
    a: 1,
    dud: `${SIN_CLAVE} (Notas, U2 y U4; Ozdemir, cap. 1).`,
    e: 'El clustering trabaja con datos sin etiquetar: es aprendizaje no supervisado.',
    ref: 'Notas, U2 (supervisado vs no supervisado) y U4 · Ozdemir, cap. 2, pág. 32 (métricas no supervisadas para clustering).',
  },
  {
    id: 'pp-14', unit: 'u5', t: 'mc', tema: 'Patrones de arquitectura de datos', src: `${SRC} · Pregunta 14 (0.5 punto)`,
    q: 'Una arquitectura de Data Warehouse representa un enfoque de fuente única de la verdad para la gestión de los datos. ¿verdadero o falso? (0.5 punto)',
    o: ['Verdadero', 'Falso'],
    a: 0,
    dud: `${SIN_CLAVE}. El tema es de la Unidad 2 (Kleppmann), que no está en estas carpetas.`,
    e: 'El DWH integra los datos de todas las fuentes en un formato consistente y funciona como hub central (Strengholt, Medallion, cap. 1). Ojo: Data Mesh rechaza la idea de una única fuente de verdad (Dehghani).',
    ref: 'Medallion, cap. 1, pág. 7 del PDF · Notas, U2 (Data Warehouse vs Data Lake).',
  },
  {
    id: 'pp-23', unit: 'u4', t: 'dev', tema: 'Feature y feature engineering', src: `${SRC} · Pregunta 23 (1 punto)`,
    q: 'Defina una feature en el ámbito de Feature Engineering. (1 punto)',
    m: 'Una feature es una representación numérica de los datos crudos (Zheng): una propiedad medible de una entidad que el modelo usa como entrada. Las buenas features son relevantes para la tarea y fáciles de ingerir para el modelo.',
    k: ['Representación numérica de datos crudos', 'Propiedad medible de una entidad u observación', 'Es la entrada del modelo'],
    dud: `${SIN_CLAVE} (Zheng, cap. 1, pág. 3).`,
    ref: 'Zheng, cap. 1, pág. 3 del PDF.',
  },
  {
    id: 'pp-24', unit: 'u4', t: 'dev', tema: 'Tipos de features', src: `${SRC} · Pregunta 24 (0.5 punto)`,
    q: 'En el ámbito de Feature Engineering, cite los tipos de features que existen. (0.5 punto)',
    m: 'Identity features, transform features y aggregate features.',
    k: ['Identity', 'Transform', 'Aggregate'],
    dud: `${SIN_CLAVE} (video MIT 6.6 y Notas, U4).`,
    ref: 'Video MIT 6.6 · Notas, U4.',
  },
]
