import type { ItemDef, UnitKey } from '../lib/quiz'

// Cinco modelos de examen generados con IA (archivo «Notas_de_clase_1.pdf» que pasó Santiago), con su «Clave de respuestas».
// NO son de la cátedra. Enunciados y claves se copian del PDF: solo se quitaron las letras a), b)… de las opciones, que la
// app vuelve a poner, las casillas V ( ) F ( ), que la app muestra como opciones, y el puntaje, que pasa a la fuente.
// Las claves no se contrastaron con los libros: `inf` lo avisa al corregir.

type Cruda = ItemDef & { unit: UnitKey; id: string }

export const MODELOS = [1, 2, 3, 4, 5].map((n) => ({ n, prefijo: `ia${n}`, titulo: `Modelo de examen IA · Parcial ${n}` }))

const src = (parcial: number, p: string, pts: string) => `Modelo de examen generado con IA · Parcial ${parcial} · ${p} (${pts})`
const VF = ['Verdadero ( )', 'Falso ( )']
const base = { inf: true }

export const modelosIA: Cruda[] = [
  // ═══════════ PARCIAL 1
  {
    ...base, id: 'ia1-01', unit: 'u5', t: 'mc', tema: 'Ciclo de vida de la ingeniería de datos', src: src(1, 'Pregunta 1', '0,5'),
    q: 'Un pipeline esperaba la columna customer_id y deja de funcionar porque la aplicación de origen la renombró a client_id. Según Reis et al., ¿con qué concepto de la etapa Generation se relaciona?',
    o: ['Data drift', 'Backfilling', 'Evolución del esquema (schema evolution)', 'Late-arriving data', 'Concept drift', 'Ninguna es correcta'],
    a: 2,
  },
  {
    ...base, id: 'ia1-02', unit: 'u5', t: 'mc', tema: 'Arquitectura Medallion', src: src(1, 'Pregunta 2', '0,5'),
    q: 'Según Strengholt (Building Medallion Architectures), los datos de la capa Bronze deben ser siempre una copia exacta de las estructuras físicas del sistema fuente.',
    o: VF, a: 1,
    e: 'F. Puede haber mediación o preprocesamiento previo (ej.: XML a tabular).',
  },
  {
    ...base, id: 'ia1-03', unit: 'u4', t: 'dev', tema: 'Niveles de datos', src: src(1, 'Pregunta 3', '1'),
    q: 'Clasifique en nominal, ordinal, de intervalo o de razón: (a) grupo sanguíneo, (b) escala de satisfacción «muy insatisfecho … muy satisfecho», (c) temperatura en °C, (d) ingreso mensual en pesos. Explique en menos de 30 palabras por qué no tiene sentido decir que 40 °C es «el doble de caliente» que 20 °C.',
    m: '(a) nominal, (b) ordinal, (c) intervalo, (d) razón. El 0 °C no indica ausencia de temperatura: no hay cero verdadero, así que no hay relaciones multiplicativas.',
  },
  {
    ...base, id: 'ia1-04', unit: 'u5', t: 'rel', tema: 'Patrones de diseño de ingeniería de datos', src: src(1, 'Pregunta 4', '1'),
    q: 'Asocie cada situación con el patrón de Konieczny que la resuelve (sobran patrones).',
    i: [
      ['Dataset de referencia de dispositivos, menos de un millón de filas, cambia pocas veces por semana y no tiene ninguna columna que indique qué fila cambió.', 'Full Loader'],
      ['Replicar cambios de una tabla transaccional a un broker en menos de 30 segundos, incluyendo borrados físicos.', 'Change Data Capture'],
      ['Un job de streaming dejó miles de archivos diminutos en un object store y los jobs batch pasan el 70 % del tiempo listando archivos.', 'Compactor'],
      ['Los consumidores leen el dataset horario antes de que termine de generarse.', 'Readiness Marker'],
    ],
    extra: ['Incremental Loader', 'Passthrough Replicator', 'External Trigger'],
  },
  {
    ...base, id: 'ia1-05', unit: 'u6', t: 'mc', tema: 'Agentes de IA', src: src(1, 'Pregunta 5', '0,5'),
    q: 'Un sistema RAG, a diferencia de un agente autónomo, decide por sí mismo ejecutar acciones posteriores, como abrir una incidencia.',
    o: VF, a: 1,
    e: 'F. Eso lo hace un agente, el RAG solo informa.',
  },
  {
    ...base, id: 'ia1-06', unit: 'u6', t: 'dev', tema: 'RAG: pipelines y componentes', src: src(1, 'Pregunta 6', '1'),
    q: 'Según Kimothi, cite (solo cite) los componentes del pipeline de indexación y los del pipeline de generación de un sistema RAG.',
    m: 'Indexación: Data Loading, Data Splitting (Chunking), Data Conversion (Embeddings), Data Storage (vector DB). Generación: Retriever, Prompt Management, LLM Setup.',
  },
  {
    ...base, id: 'ia1-07', unit: 'u4', t: 'dev', tema: 'Machine learning y modelado predictivo', src: src(1, 'Pregunta 7', '1,5'),
    q: 'Una universidad quiere anticipar, con dos semanas de antelación, qué estudiantes abandonarán un curso durante el mes siguiente. Según el curso del MIT:\n(a) Defina los cuatro componentes de la definición del resultado a predecir.\n(b) Explique qué efecto tiene el lead time sobre el cutoff time.\n(c) Proponga un ejemplo de feature que produciría data leakage.',
    m: '(a) Entidad: estudiante. Columna temporal: timestamps de actividad. Ventana de predicción: el mes siguiente. Función de agregación: ej. conteo de actividad (0 implica abandono) o existencia de evento de baja. (b) El cutoff se desplaza hacia atrás dos semanas: solo se usan datos disponibles hasta ese momento. (c) Accesos durante el mes a predecir, o la nota final del curso.',
  },
  {
    ...base, id: 'ia1-08', unit: 'u5', t: 'rel', tema: 'Data Mesh', src: src(1, 'Pregunta 8', '1'),
    q: 'Según Dehghani, indique qué principio de Data Mesh mitiga cada problema:',
    i: [
      ['(a) La propiedad por dominio genera silos de datos dentro de cada dominio.', 'Data as a Product'],
      ['(b) La propiedad por dominio genera esfuerzo duplicado y mayor costo.', 'Plataforma self-serve'],
      ['(c) La descentralización genera incompatibilidad y desconexión entre dominios.', 'Gobernanza computacional federada'],
    ],
  },
  {
    ...base, id: 'ia1-09', unit: 'u5', t: 'dev', tema: 'Patrones de arquitectura de datos', src: src(1, 'Pregunta 9', '1'),
    q: 'Describa en menos de 60 palabras la diferencia entre la arquitectura Kappa y el modelo Dataflow.',
    m: 'Kappa usa una plataforma de streaming como columna vertebral de todo y reprocesa el histórico reproduciendo eventos almacenados. Dataflow usa un único modelo de programación para batch y streaming: el batch es un stream acotado y solo se cambia la ventana.',
  },
  {
    ...base, id: 'ia1-10', unit: 'u6', t: 'mc', tema: 'RAG: retrieval', src: src(1, 'Pregunta 10', '0,5'),
    q: 'Un retriever barato y rápido (basado en términos) trae candidatos y luego un mecanismo más preciso pero más costoso los reordena. Según Huyen, ese segundo paso se llama:',
    o: ['Chunking', 'Reranking', 'Query rewriting', 'Contextual retrieval', 'Fine-tuning', 'Ninguna'],
    a: 1,
  },
  {
    ...base, id: 'ia1-11', unit: 'u4', t: 'dev', tema: 'Machine learning y modelado predictivo', src: src(1, 'Pregunta 11', '1'),
    q: 'Debe elegir qué cafetera recomendar para maximizar la ganancia esperada. A: 15 % de probabilidad de compra y $20 de ganancia por venta. B: 4 % de probabilidad y $90 por venta. Calcule y justifique. ¿Cambia la respuesta si el objetivo fuera maximizar la probabilidad de compra?',
    m: 'A = 0,15 × 20 = $3. B = 0,04 × 90 = $3,6. Recomendar B. Si el objetivo fuera la probabilidad de compra, recomendar A (15 % > 4 %).',
  },
  {
    ...base, id: 'ia1-12', unit: 'u5', t: 'mc', tema: 'Patrones de diseño de ingeniería de datos', src: src(1, 'Pregunta 12', '0,5'),
    q: 'Según Konieczny, el Anonymizer reemplaza los valores PII por formas utilizables (máscaras, tokens, hashes) para no perder valor analítico, y el Pseudo-Anonymizer los elimina o altera de forma irreversible.',
    o: VF, a: 1,
    e: 'F. Está invertido: el Anonymizer elimina o altera, el Pseudo-Anonymizer usa formas utilizables.',
  },
  {
    ...base, id: 'ia1-13', unit: 'u4', t: 'dev', tema: 'Model-centric vs data-centric', src: src(1, 'Extra', '0,5'),
    q: 'EXTRA. Meme Drake. Arriba (rechaza): «Probar el quinto algoritmo distinto para ver si mejora el F1». Abajo (aprueba): ________ (frase corta)',
    m: '«mejorar las features / los datos» (enfoque data-centric).',
  },

  // ═══════════ PARCIAL 2
  {
    ...base, id: 'ia2-01', unit: 'u5', t: 'mc', tema: 'Ingeniería de datos', src: src(2, 'Pregunta 1', '0,5'),
    q: 'Una startup de seis personas recién empieza a usar datos. Según Reis, ¿cuál es el foco típico del ingeniero de datos en esta etapa?',
    o: [
      'Desplegar catálogos de datos y herramientas de linaje.',
      'Conseguir respaldo de las partes interesadas, definir la arquitectura, auditar los datos y construir una base sólida.',
      'Adoptar DataOps y construir sistemas que respalden ML.',
      'Crear herramientas personalizadas que den ventaja competitiva.',
      'Todas',
      'Ninguna',
    ],
    a: 1,
  },
  {
    ...base, id: 'ia2-02', unit: 'u4', t: 'mc', tema: 'Feature y feature engineering', src: src(2, 'Pregunta 2', '0,5'),
    q: 'Si las features originales no contienen capacidad predictiva sobre la variable de respuesta, una buena ingeniería de características igualmente puede crear ese vínculo.',
    o: VF, a: 1,
  },
  {
    ...base, id: 'ia2-03', unit: 'u4', t: 'dev', tema: 'Representación y clasificación de texto', src: src(2, 'Pregunta 3', '1,5'),
    q: 'Corpus: D1 «perro muerde hombre», D2 «hombre muerde perro». Vocabulario ordenado [perro, muerde, hombre, come, carne].\n(a) Escriba el vector bag-of-words de D1 y de D2.\n(b) ¿Qué limitación evidencia el resultado?\n(c) ¿Qué extensión la alivia parcialmente y a qué costo?',
    m: '(a) D1 = [1,1,1,0,0] y D2 = [1,1,1,0,0]. (b) Pierde el orden: vectores idénticos para significados distintos. (c) Bag-of-n-grams (bigramas: «perro muerde / muerde hombre» frente a «hombre muerde / muerde perro»). Cuesta más: hay muchos más n-gramas que palabras, así que es más caro computar, almacenar y modelar. Normalmente no se pasa de n = 3.',
  },
  {
    ...base, id: 'ia2-04', unit: 'u5', t: 'dev', tema: 'Patrones de diseño de ingeniería de datos', src: src(2, 'Pregunta 4', '1'),
    q: 'Un job diario integra datos tardíos con una ventana fija de 15 días. El negocio pide incorporar todos los datos tardíos, sin importar su antigüedad, y recomputar solo las particiones afectadas. Según Konieczny, ¿qué patrón corresponde y qué estructura adicional necesita?',
    m: 'Dynamic Late Data Integrator. Necesita una estructura que guarde el último momento de ejecución y la última actualización por partición.',
  },
  {
    ...base, id: 'ia2-05', unit: 'u6', t: 'mc', tema: 'Diseño de sistemas de agentes', src: src(2, 'Pregunta 5', '0,5'),
    q: 'En arquitecturas multiagente el consumo de tokens suele ser menor que en un solo agente, porque cada agente se especializa.',
    o: VF, a: 1,
    e: 'F. Suelen ser menos eficientes: más tokens por la comunicación y el contexto compartido.',
  },
  {
    ...base, id: 'ia2-06', unit: 'u6', t: 'dev', tema: 'RAG: retrieval', src: src(2, 'Pregunta 6', '1'),
    q: 'Según Huyen, explique en menos de 80 palabras la diferencia entre recuperación basada en términos y basada en embeddings (una ventaja de cada una) y cómo se combinan en una búsqueda híbrida.',
    m: 'Términos: busca por palabras (con frecuencia e importancia), es más rápida y barata. Embeddings: busca por significado (relaciones semánticas) y tiene más margen de mejora. Híbrida: en secuencia (uno barato trae candidatos y uno preciso reordena) o en paralelo como ensemble (ej.: RRF).',
  },
  {
    ...base, id: 'ia2-07', unit: 'u5', t: 'dev', tema: 'Arquitectura Medallion', src: src(2, 'Pregunta 7', '1'),
    q: 'Los clientes están en un CRM y los pedidos en un ERP. Según Strengholt, ¿en qué capa Medallion los integraría y por qué no en la anterior? Menos de 50 palabras.',
    m: 'En Gold. Silver mantiene los datos separados por sistema fuente para no crear dependencias entre aplicaciones. Gold los combina para tener una vista integrada.',
  },
  {
    ...base, id: 'ia2-08', unit: 'u4', t: 'dev', tema: 'Data products', src: src(2, 'Pregunta 8', '1'),
    q: 'Un equipo publica como «data product» las tablas crudas de su sistema transaccional para que cada dominio consumidor las limpie. ¿Qué principio de diseño de Strengholt viola y qué consecuencia tiene?',
    m: '«No raw data». Obliga a cada dominio consumidor a rehacer el trabajo. También afecta la reutilización.',
  },
  {
    ...base, id: 'ia2-09', unit: 'u5', t: 'dev', tema: 'Ciclo de vida de la ingeniería de datos', src: src(2, 'Pregunta 9', '1'),
    q: 'Alguien propone ingesta en streaming para un reporte que se consulta una vez por semana, «porque es lo más moderno». ¿Qué recomienda Reis al respecto? Menos de 40 palabras.',
    m: 'No implementar streaming solo por ser más avanzado. Debe haber una necesidad que justifique su mayor costo y complejidad. Acá alcanza con batch.',
  },
  {
    ...base, id: 'ia2-10', unit: 'u4', t: 'mc', tema: 'Sistemas de recomendación', src: src(2, 'Pregunta 10', '0,5'),
    q: 'El dataset del Netflix Prize tenía ~100 millones de calificaciones sobre ~500.000 usuarios × 17.000 películas (≈1,2 % de las celdas). ¿Qué implica?',
    o: [
      'La matriz es densa.',
      'La matriz es muy dispersa y la mayoría de las valoraciones deben estimarse.',
      'No hace falta side information.',
      'Se resuelve solo con filtrado por contenido.',
      'Ninguna',
    ],
    a: 1,
  },
  {
    ...base, id: 'ia2-11', unit: 'u6', t: 'dev', tema: 'Rol del AI PM', src: src(2, 'Pregunta 11', '1'),
    q: 'Según Nika, cite (solo cite) cuatro características distintivas de los productos con IA frente al software tradicional.',
    m: 'Cuatro de estas seis: naturaleza probabilística, dependencia de los datos, model drift, interpretabilidad y explicabilidad, toma de decisiones automatizada, escalabilidad.',
  },
  {
    ...base, id: 'ia2-12', unit: 'u5', t: 'mc', tema: 'Patrones de diseño de ingeniería de datos', src: src(2, 'Pregunta 12', '0,5'),
    q: 'En Audit-Write-Audit-Publish (Konieczny), la primera auditoría valida el dataset ya transformado y la segunda valida el dataset de entrada.',
    o: VF, a: 1,
    e: 'F. Está invertido: la primera valida la entrada y la segunda la salida.',
  },
  {
    ...base, id: 'ia2-13', unit: 'u5', t: 'dev', tema: 'Ciclo de vida de la ingeniería de datos', src: src(2, 'Extra', '0,5'),
    q: 'EXTRA. Meme This is fine (perro con café en una habitación en llamas). Cartel: «El pipeline lleva tres días procesando datos vacíos y no falló, pero nadie se enteró hasta que se quejó el consumidor». ¿Qué le faltó al equipo? ________ (frase corta)',
    m: 'observabilidad / monitoreo con alertas.',
  },

  // ═══════════ PARCIAL 3
  {
    ...base, id: 'ia3-01', unit: 'u5', t: 'mc', tema: 'Arquitectura Medallion', src: src(3, 'Pregunta 1', '0,5'),
    q: '¿Cuál NO es una actividad típica de la capa Silver (Strengholt)?',
    o: [
      'Eliminar duplicados',
      'Estandarizar formatos y unidades',
      'Construir esquemas estrella con hechos y dimensiones para reportes de negocio',
      'Tratar valores faltantes',
      'Aplicar MDM',
      'Todas son típicas de Silver',
    ],
    a: 2,
    e: 'c. Es de Gold.',
  },
  {
    ...base, id: 'ia3-02', unit: 'u5', t: 'mc', tema: 'Patrones de arquitectura de datos', src: src(3, 'Pregunta 2', '0,5'),
    q: 'La arquitectura Lambda es una arquitectura de datos completa que reemplaza al data warehouse y al data lake.',
    o: VF, a: 1,
    e: 'F. Es un patrón, no una arquitectura completa.',
  },
  {
    ...base, id: 'ia3-03', unit: 'u4', t: 'dev', tema: 'Machine learning y modelado predictivo', src: src(3, 'Pregunta 3', '1,5'),
    q: 'Sobre el scanning algorithm (MIT):\n(a) Ordene del 1 al 6: ( ) aplicar la función de agregación · ( ) asignar el label · ( ) desplazar la ventana y repetir · ( ) seleccionar una entidad · ( ) guardar el ejemplo · ( ) definir la ventana de predicción.\n(b) Cite (solo cite) las tres decisiones de diseño que surgen al aplicarlo.',
    m: '(a) Entidad = 1, ventana de predicción = 2, función de agregación = 3, label = 4, guardar = 5, desplazar = 6. (b) ¿Múltiples ejemplos por entidad? ¿Separación entre ejemplos? ¿Ventanas superpuestas?',
  },
  {
    ...base, id: 'ia3-04', unit: 'u5', t: 'dev', tema: 'Patrones de diseño de ingeniería de datos', src: src(3, 'Pregunta 4', '1'),
    q: 'Un job batch diario procesa 500 GB–1,5 TB. Para ser idempotente hace DELETE de la corrida anterior y luego INSERT, pero el DELETE es cada vez más lento. Según Konieczny:\n(a) ¿Qué patrón propone y por qué es más rápido?\n(b) ¿Qué patrón usaría si el almacenamiento fuera un object store sin TRUNCATE ni DROP?',
    m: '(a) Fast Metadata Cleaner. Opera en la capa de metadatos (lógica) y no sobre los archivos de datos: ej. tablas por período con TRUNCATE o DROP. (b) Data Overwrite.',
  },
  {
    ...base, id: 'ia3-05', unit: 'u6', t: 'mc', tema: 'RAG: pipelines y componentes', src: src(3, 'Pregunta 5', '0,5'),
    q: 'Según Kimothi, un sistema RAG que obtiene la información directamente de una API de terceros:',
    o: [
      'siempre necesita su pipeline de indexación;',
      'no necesariamente lo necesita, porque la búsqueda y el mantenimiento se delegan a un sistema externo;',
      'no puede usar retriever;',
      'deja de ser RAG;',
      'Ninguna',
    ],
    a: 1,
  },
  {
    ...base, id: 'ia3-06', unit: 'u6', t: 'rel', tema: 'Agentes según Huyen', src: src(3, 'Pregunta 6', '1'),
    q: 'Según Huyen, clasifique cada fallo: herramienta inválida · herramienta válida con parámetros inválidos · herramienta válida con valores incorrectos · error de reflexión · fallo de objetivo (sobra una).',
    i: [
      ['(a) Invoca lbs_to_kg con dos parámetros cuando requiere uno.', 'herramienta válida con parámetros inválidos'],
      ['(b) Invoca lbs_to_kg(lbs=100) cuando el valor correcto era 120.', 'herramienta válida con valores incorrectos'],
      ['(c) Debía asignar 50 personas a 30 habitaciones, asigna a 40 y afirma haber terminado.', 'error de reflexión'],
      ['(d) Le piden un viaje a Hanoi con USD 5.000 y arma uno a Ho Chi Minh.', 'fallo de objetivo'],
    ],
    extra: ['herramienta inválida'],
    e: 'Sobra «herramienta inválida».',
  },
  {
    ...base, id: 'ia3-07', unit: 'u5', t: 'dev', tema: 'Data Mesh', src: src(3, 'Pregunta 7', '1'),
    q: 'Según Dehghani, describa en menos de 80 palabras la diferencia entre datos operacionales y analíticos (propósito, sistema, historia, acceso) y ejemplifique.',
    m: 'Operacional: soporta correr el negocio, estado actual, OLTP, transacciones, lecturas y escrituras constantes. Analítico: vista histórica, integrada y agregada, OLAP, lecturas intensivas y pocos escritores, para ML y reportes. Ej.: la tabla de suscriptores (operacional) frente al historial de escucha que entrena el recomendador (analítico).',
  },
  {
    ...base, id: 'ia3-08', unit: 'u4', t: 'dev', tema: 'Pipeline de NLP', src: src(3, 'Pregunta 8', '1'),
    q: '¿Por qué la lematización suele dar mejores resultados que el stemming y qué ventaja conserva este último? Dé un ejemplo de stemming problemático. Menos de 40 palabras.',
    m: 'La lematización usa la palabra del diccionario, por eso es más precisa, pero es más costosa. El stemming es rápido y simple. Ej.: «New» y «news» comparten raíz.',
  },
  {
    ...base, id: 'ia3-09', unit: 'u5', t: 'dev', tema: 'Ciclo de vida de la ingeniería de datos', src: src(3, 'Pregunta 9', '1'),
    q: 'Según Reis, cite (solo cite) los tres elementos técnicos de DataOps y describa en menos de 40 palabras uno con un ejemplo.',
    m: 'Automatización, observabilidad y monitoreo, respuesta a incidentes. Ej.: una carga nocturna que, si falla o detecta registros incorrectos, dispara una alerta.',
  },
  {
    ...base, id: 'ia3-10', unit: 'u4', t: 'mc', tema: 'Data products', src: src(3, 'Pregunta 10', '0,5'),
    q: 'Según Strengholt, en un diseño inspirado en CQRS los consumidores analíticos deben consultar directamente la base transaccional para tener siempre los datos más frescos.',
    o: VF, a: 1,
    e: 'F. Se generan representaciones optimizadas para lectura.',
  },
  {
    ...base, id: 'ia3-11', unit: 'u6', t: 'rel', tema: 'Agentes de IA', src: src(3, 'Pregunta 11', '1'),
    q: 'Según Albada, elija la solución más adecuada (código simple, workflow determinista, chatbot/RAG o agente autónomo):',
    i: [
      ['(a) Transformar cada noche un CSV con formato siempre idéntico.', 'código simple'],
      ['(b) Responder preguntas de clientes sobre manuales en PDF.', 'chatbot/RAG'],
      ['(c) Aprobar reembolsos con tres ramas de decisión conocidas y auditables.', 'workflow determinista'],
      ['(d) Investigar un incidente combinando logs, tickets y APIs con pasos no enumerables de antemano.', 'agente autónomo'],
    ],
  },
  {
    ...base, id: 'ia3-12', unit: 'u4', t: 'fill', tema: 'NLP: tareas y enfoques', src: src(3, 'Pregunta 12', '0,5'),
    q: 'Complete:',
    i: [
      ['en Seq2Seq el codificador comprimía toda la secuencia en un vector de longitud fija; el mecanismo de ___ permitió al decodificador acceder a los distintos estados ocultos del codificador.', 'atención', ['atencion', 'attention']],
    ],
  },
  {
    ...base, id: 'ia3-13', unit: 'u6', t: 'dev', tema: 'Agentes de IA', src: src(3, 'Extra', '0,5'),
    q: 'EXTRA. Meme Distracted Boyfriend. Novio: el equipo de datos. Novia enojada: «el workflow determinista que ya funciona perfecto». Mujer que pasa: ________ (frase corta)',
    m: '«un agente autónomo con LLM».',
  },

  // ═══════════ PARCIAL 4
  {
    ...base, id: 'ia4-01', unit: 'u4', t: 'mc', tema: 'Model-centric vs data-centric', src: src(4, 'Pregunta 1', '0,5'),
    q: '¿En qué situación es particularmente útil un enfoque centrado en los datos (Ozdemir)?',
    o: [
      '5 millones de filas y pocas columnas.',
      '3.000 filas con 400 columnas, donde la interpretabilidad es clave.',
      'Un problema trivial con datos perfectos.',
      'Cuando el único objetivo es cambiar de algoritmo.',
      'Todas',
      'Ninguna',
    ],
    a: 1,
  },
  {
    ...base, id: 'ia4-02', unit: 'u5', t: 'mc', tema: 'Patrones de diseño de ingeniería de datos', src: src(4, 'Pregunta 2', '0,5'),
    q: 'Según Konieczny, el patrón Bucket sirve para optimizar accesos por una columna de alta cardinalidad (como un user ID), donde particionar horizontalmente generaría demasiadas particiones.',
    o: VF, a: 0,
  },
  {
    ...base, id: 'ia4-03', unit: 'u5', t: 'dev', tema: 'Arquitectura Medallion', src: src(4, 'Pregunta 3', '1'),
    q: 'Según Strengholt, explique en menos de 60 palabras la diferencia entre validación intrusiva y no intrusiva en Bronze y cuándo elegiría cada una.',
    m: 'Intrusiva: detiene el procesamiento o aparta los datos incorrectos para que no avancen. Se usa cuando propagarlos sería grave (esquema roto, archivo truncado). No intrusiva: sigue procesando y conserva los datos problemáticos para tratarlos después. Se usa cuando importa la disponibilidad y el problema es tolerable.',
  },
  {
    ...base, id: 'ia4-04', unit: 'u5', t: 'rel', tema: 'Patrones de diseño de ingeniería de datos', src: src(4, 'Pregunta 4', '1,5'),
    q: 'Asocie con el patrón de Konieczny (Static Joiner · Dynamic Joiner · Wrapper · Metadata Decorator · Local Aggregator):',
    i: [
      ['Enriquecer visitas con una tabla de usuarios estática y de referencia.', 'Static Joiner'],
      ['Enriquecer visitas con perfiles que cambian todo el tiempo y llegan por CDC a un broker.', 'Dynamic Joiner'],
      ['Agregar campos calculados a cada registro manteniendo intacto el original, separados por un envoltorio.', 'Wrapper'],
      ['Agregar la versión del job a cada registro sin exponerla a los usuarios finales.', 'Metadata Decorator'],
    ],
    extra: ['Local Aggregator'],
    e: 'Sobra Local Aggregator.',
  },
  {
    ...base, id: 'ia4-05', unit: 'u4', t: 'mc', tema: 'Machine learning y modelado predictivo', src: src(4, 'Pregunta 5', '0,5'),
    q: 'En el curso del MIT, al introducir un lead time el cutoff time:',
    o: [
      'se desplaza hacia adelante;',
      'se desplaza hacia atrás, hasta el momento en que realmente se necesita predecir;',
      'no cambia;',
      'coincide con el fin de la ventana de predicción;',
      'se elimina',
    ],
    a: 1,
  },
  {
    ...base, id: 'ia4-06', unit: 'u4', t: 'dev', tema: 'Sistemas de recomendación', src: src(4, 'Pregunta 6', '1'),
    q: '¿Por qué un sistema que conecta personas (Tinder, eHarmony) es más complejo que uno que conecta usuarios con productos (Netflix, Amazon)? Menos de 40 palabras.',
    m: 'Los productos no tienen preferencias, las personas sí. Hay que considerar las preferencias de ambas partes.',
  },
  {
    ...base, id: 'ia4-07', unit: 'u6', t: 'rel', tema: 'RAG: pipelines y componentes', src: src(4, 'Pregunta 7', '1'),
    q: 'Según Kimothi, indique qué métrica de la tríada de RAG se degrada en cada caso:',
    i: [
      ['(a) El retriever trae fragmentos de otro tema.', 'Context relevance'],
      ['(b) El LLM inventa datos que no están en el contexto recuperado.', 'Groundedness'],
      ['(c) La respuesta es fiel al contexto pero no responde lo que se preguntó.', 'Answer relevance'],
    ],
  },
  {
    ...base, id: 'ia4-08', unit: 'u6', t: 'dev', tema: 'RAG: retrieval', src: src(4, 'Pregunta 8', '1'),
    q: 'Un equipo parte documentos en chunks de 100 caracteres sin solapamiento y observa pérdida de información. Según Huyen, en menos de 70 palabras: (a) ¿por qué ocurre?, (b) ¿qué ajuste propone?, (c) ¿qué costo trae reducir el tamaño de chunk?',
    m: '(a) Los cortes caen en medio del contexto. (b) Solapamiento (overlap). (c) Más chunks, más embeddings y un espacio de búsqueda mayor: más lento y más caro. También se puede perder información repartida.',
  },
  {
    ...base, id: 'ia4-09', unit: 'u5', t: 'dev', tema: 'Patrones de arquitectura de datos', src: src(4, 'Pregunta 9', '1'),
    q: 'Según Reis, explique en menos de 50 palabras qué intentó resolver el data lakehouse respecto del data lake de primera generación y qué combina.',
    m: 'Resolver las limitaciones del lake de primera generación. Combina controles, administración y estructuras del data warehouse con almacenamiento de objetos y soporte de varios motores de consulta y transformación.',
  },
  {
    ...base, id: 'ia4-10', unit: 'u5', t: 'mc', tema: 'Data Mesh', src: src(4, 'Pregunta 10', '0,5'),
    q: 'Según Dehghani, Data Mesh es una arquitectura puramente técnica, sin dimensión organizacional.',
    o: VF, a: 1,
    e: 'F. Es un enfoque sociotécnico.',
  },
  {
    ...base, id: 'ia4-11', unit: 'u4', t: 'dev', tema: 'Representación y clasificación de texto', src: src(4, 'Pregunta 11', '1'),
    q: 'Corpus de N = 8 documentos. El documento d tiene 20 palabras. «modelo» aparece 5 veces en d y en 2 documentos del corpus; «de» aparece 5 veces en d y en los 8 documentos. Con IDF = log₂(N/df), calcule el TF-IDF de cada una e interprete.',
    m: '«modelo»: TF = 5/20 = 0,25; IDF = log₂(8/2) = 2; TF-IDF = 0,5. «de»: IDF = log₂(8/8) = 0; TF-IDF = 0. TF-IDF reduce el peso de lo común en el corpus y resalta lo que distingue al documento.',
  },
  {
    ...base, id: 'ia4-12', unit: 'u6', t: 'mc', tema: 'Rol del AI PM', src: src(4, 'Pregunta 12', '0,5'),
    q: 'Según Nika, el tipo de AI PM que incorpora herramientas de IA a sus propios flujos de trabajo para ser más productivo es:',
    o: ['AI builder PM', 'AI experiences PM', 'AI-enhanced PM', 'PM generalista', 'Ninguna'],
    a: 2,
  },
  {
    ...base, id: 'ia4-13', unit: 'u4', t: 'dev', tema: 'Data products', src: src(4, 'Extra', '0,5'),
    q: 'EXTRA. Meme Drake. Arriba (rechaza): «Publicar datos crudos y que cada dominio se las arregle». Abajo (aprueba): ________ (frase corta)',
    m: '«datos limpios y listos para consumir (data product)».',
  },

  // ═══════════ PARCIAL 5
  {
    ...base, id: 'ia5-01', unit: 'u5', t: 'mc', tema: 'Patrones de diseño de ingeniería de datos', src: src(5, 'Pregunta 1', '0,5'),
    q: 'Según Konieczny, ¿por qué no alcanzan los patrones de diseño de software clásicos (Gang of Four) en ingeniería de datos?',
    o: [
      'No son reutilizables.',
      'Además del código mantenible, hay que resolver aspectos propios de los datos: fallas, backfilling, idempotencia y corrección.',
      'Solo aplican a lenguajes OOP.',
      'No tienen consecuencias.',
      'Ninguna',
    ],
    a: 1,
  },
  {
    ...base, id: 'ia5-02', unit: 'u5', t: 'mc', tema: 'Ingeniería de datos', src: src(5, 'Pregunta 2', '0,5'),
    q: 'Según Reis, el ingeniero de datos tipo B («build») evita el trabajo pesado indiferenciado y gestiona el ciclo de vida con productos comerciales y servicios administrados.',
    o: VF, a: 1,
    e: 'F. Eso describe al tipo A.',
  },
  {
    ...base, id: 'ia5-03', unit: 'u4', t: 'dev', tema: 'Representación y clasificación de texto', src: src(5, 'Pregunta 3', '1,5'),
    q: 'Hay 5.000 reseñas de clientes sin etiquetar y se quieren descubrir grupos de temas.\n(a) ¿Qué tipo de aprendizaje y qué técnica corresponde?\n(b) ¿Podría usar clasificación? ¿Bajo qué condición?\n(c) Nombre un algoritmo y una representación del texto para alimentarlo.',
    m: '(a) Aprendizaje no supervisado, clustering. (b) La clasificación es supervisada: solo si se etiqueta antes una muestra. (c) K-means con TF-IDF o embeddings.',
  },
  {
    ...base, id: 'ia5-04', unit: 'u5', t: 'rel', tema: 'Patrones de diseño de ingeniería de datos', src: src(5, 'Pregunta 4', '1'),
    q: 'Asocie con el patrón de observabilidad de Konieczny (Flow Interruption Detector · Skew Detector · Lag Detector · SLA Misses Detector · Dataset Tracker):',
    i: [
      ['Un batch procesó un dataset a medio llenar porque el proveedor tuvo problemas de generación.', 'Skew Detector'],
      ['Un job de streaming procesó los registros sin escribirlos en el destino y no falló.', 'Flow Interruption Detector'],
      ['Un job de las 6:00 debe terminar en 40 minutos y hay que avisar si se excede.', 'SLA Misses Detector'],
      ['Se necesita medir cuánto se atrasa un consumidor respecto del productor.', 'Lag Detector'],
    ],
    extra: ['Dataset Tracker'],
  },
  {
    ...base, id: 'ia5-05', unit: 'u6', t: 'mc', tema: 'Agentes de IA', src: src(5, 'Pregunta 5', '0,5'),
    q: 'Según Albada, ¿cuál NO es uno de los factores para elegir entre código, workflow, chatbot/RAG o agente?',
    o: [
      'Variabilidad de las entradas',
      'Complejidad del razonamiento',
      'Restricciones de rendimiento o cumplimiento normativo',
      'Carga de mantenimiento continuo',
      'Popularidad del modelo fundacional en el mercado',
    ],
    a: 4,
  },
  {
    ...base, id: 'ia5-06', unit: 'u5', t: 'dev', tema: 'Arquitectura Medallion', src: src(5, 'Pregunta 6', '1'),
    q: 'Según Strengholt:\n(a) Cite 2 ventajas y 2 desventajas de One Big Table frente al esquema estrella.\n(b) ¿Qué es la granularidad y por qué se define antes de modelar?',
    m: '(a) Ventajas, dos de: estructura inicial simple, fácil implementación, menos JOINs y buen rendimiento en ciertas consultas, cómoda para data scientists. Desventajas, dos de: duplicación de datos, más memoria, dificultad para mantener o actualizar tablas enormes, datos anidados que complican las consultas. (b) Granularidad: qué representa cada registro. Condiciona dimensiones, relaciones y agregaciones.',
  },
  {
    ...base, id: 'ia5-07', unit: 'u6', t: 'rel', tema: 'Agentes según Huyen', src: src(5, 'Pregunta 7', '1'),
    q: 'Según Huyen, clasifique en conocimiento interno, memoria de corto plazo o de largo plazo:',
    i: [
      ['(a) Lo aprendido durante el entrenamiento.', 'conocimiento interno'],
      ['(b) Los mensajes recientes de la conversación actual.', 'memoria de corto plazo'],
      ['(c) Preferencias del usuario guardadas en una base externa y recuperadas en otra sesión.', 'memoria de largo plazo'],
      ['(d) Lo que está limitado por la ventana de contexto.', 'memoria de corto plazo'],
    ],
  },
  {
    ...base, id: 'ia5-08', unit: 'u5', t: 'dev', tema: 'Data Mesh', src: src(5, 'Pregunta 8', '1'),
    q: 'Según Dehghani, cite (solo cite) seis de las ocho características de usabilidad de un data product.',
    m: 'Seis de: discoverable, addressable, understandable, trustworthy and truthful, natively accessible, interoperable and composable, valuable on its own, secure.',
  },
  {
    ...base, id: 'ia5-09', unit: 'u5', t: 'dev', tema: 'Ciclo de vida de la ingeniería de datos', src: src(5, 'Pregunta 9', '1'),
    q: 'Según Reis, describa en menos de 50 palabras qué es Reverse ETL y dé un ejemplo propio (no el del CRM del apunte).',
    m: 'Devolver datos ya procesados a los sistemas de origen u operacionales. Ej.: enviar desde el DW el puntaje de riesgo de abandono a la herramienta de marketing.',
  },
  {
    ...base, id: 'ia5-10', unit: 'u4', t: 'mc', tema: 'Data drift y concept drift', src: src(5, 'Pregunta 10', '0,5'),
    q: 'Data drift significa que cambió lo que los datos permiten predecir, y concept drift significa que cambiaron los datos observados.',
    o: VF, a: 1,
    e: 'F. Está invertido.',
  },
  {
    ...base, id: 'ia5-11', unit: 'u4', t: 'dev', tema: 'Sistemas de recomendación', src: src(5, 'Pregunta 11', '1'),
    q: 'En el Netflix Prize se usó RMSE.\n(a) ¿Qué mide?\n(b) ¿Mejor modelo = RMSE mayor o menor?\n(c) Con la regla «recomendar si la predicción ≥ 4,2», el modelo predice 4,5 y el usuario puntuó 3,0: ¿cuál es el error, cómo aporta al RMSE y qué pasa con la recomendación?',
    m: '(a) La raíz del error cuadrático medio entre valoraciones predichas y reales. (b) Menor. (c) Error = 1,5, al cuadrado 2,25, que entra al promedio antes de la raíz. Se recomendaría igual (4,5 ≥ 4,2) aunque el usuario puntuó 3: falso positivo.',
  },
  {
    ...base, id: 'ia5-12', unit: 'u6', t: 'fill', tema: 'Agentes de IA', src: src(5, 'Pregunta 12', '0,5'),
    q: 'Complete:',
    i: [
      ['a diferencia del software tradicional, que ejecuta de forma síncrona, los agentes autónomos están diseñados para operar de forma ___.', 'asíncrona', ['asincrona']],
    ],
  },
  {
    ...base, id: 'ia5-13', unit: 'u4', t: 'fill', tema: 'Data products', src: src(5, 'Extra', '0,5'),
    q: 'EXTRA. Meme Change my mind (cartel sobre una mesa):',
    i: [['«Los datos son un ___, no un activo para acumular». (una palabra)', 'producto']],
  },
]
