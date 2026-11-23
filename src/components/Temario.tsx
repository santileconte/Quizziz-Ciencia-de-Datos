import { questions, historicas } from '../cuestionarios'
import { figurasDe, relacionadasDe } from '../lib/figuras'
import { diagrams } from '../lib/diagrams'
import { puntua, type Question } from '../lib/quiz'
import { findMindMap } from '../mapas'
import { bloques, prioridadLabel, temario, type Tema } from '../temario'

const de = (t: Tema) => questions.filter((q) => t.temas.includes(q.tema))
const cuenta = (qs: Question[], pred: (q: Question) => boolean) => qs.filter(pred).length
const esParcial = (q: Question) => q.modalidad === 'parcial'
const esPrimero = (q: Question) => q.modalidad === 'primero'

/** Registros del documento de la materia (pestañas de Google Docs) y cómo se usó cada uno. */
const REGISTROS: { archivo: string; tipo: string; detalle: string; n: () => number | string }[] = [
  {
    archivo: 'Foto del segundo parcial 2025 (Drive)',
    tipo: 'Parcial real',
    detalle:
      '10 consignas y un punto extra, con su puntaje, copiadas de la foto del examen: solo se quitaron las letras de las opciones y las casillas V ( ) F ( ). El examen no trae clave oficial. El meme del punto extra está recortado de la foto.',
    n: () => cuenta(questions, esParcial),
  },
  {
    archivo: 'Pestaña «Parcial» · «preguntas de 1er parcial que entran ahora»',
    tipo: 'Pregunta de la cátedra (1er parcial)',
    detalle:
      'Bloque que un compañero marcó con ese comentario. Se copiaron las consignas que pertenecen a U4–U6 o que sus libros cubren; las que dependen de la Unidad 2 se marcan como tales. Sin claves.',
    n: () => cuenta(questions, esPrimero),
  },
  {
    archivo: 'Pestaña «Notas de clase»',
    tipo: 'Filtro de temas y prioridades',
    detalle:
      'Lo que el profesor remarcó en clase por unidad. Decide qué temas entran y con qué prioridad; no aporta preguntas.',
    n: () => `${temario.filter((t) => t.prio !== 'Pend').length} temas`,
  },
  {
    archivo: 'Pestaña «Bibliografía» (2025)',
    tipo: 'Filtro de libros y capítulos',
    detalle:
      'Qué libros y capítulos son obligatorios en cada unidad. Los libros que nombra y no están en las carpetas Unidad 4, 5 y 6 figuran en «Sin confirmar o sin material».',
    n: () => `${temario.filter((t) => t.prio === 'Pend').length} temas sin material`,
  },
  {
    archivo: 'Carpetas Unidad 4, Unidad 5 y Unidad 6 (PDF)',
    tipo: 'Fuente de contenido',
    detalle:
      'Los libros de la cátedra. De acá salen las explicaciones, las figuras (con su número y página) y las preguntas nuevas, cada una con libro, capítulo y página del PDF.',
    n: () => `${cuenta(questions, (q) => q.modalidad === 'propia')} preguntas nuevas`,
  },
]

/** Decisiones tomadas al armar el repaso. */
const DECISIONES: { titulo: string; texto: string; ids?: string }[] = [
  {
    titulo: 'Las consignas de la cátedra no suman hasta que confirmes su clave',
    texto:
      'El documento no trae respuestas. Cada pregunta real muestra una clave propuesta con su fuente, pero queda fuera del puntaje y del progreso. Para habilitarla, agregá su id en src/cuestionarios/verificadas.ts.',
  },
  ...historicas.map((h) => ({
    titulo: `${h.id} se practica como ${h.por}`,
    texto: h.motivo,
    ids: `${h.por} (se practica) · ${h.id} (registro)`,
  })),
  {
    titulo: 'Texto literal, incluso con errores',
    texto:
      'Las consignas reales se copian como están, con sus errores de redacción. Cuando algo choca con el libro (por ejemplo, la pregunta 4 se puede leer de dos formas según la fig. 3-1 de Reis), la diferencia va en la nota de la pregunta, no en el enunciado.',
    ids: 'pc25-05',
  },
  {
    titulo: 'Preguntas nuevas, marcadas aparte',
    texto:
      'Las preguntas de práctica no son de la cátedra: llevan la etiqueta «Pregunta nueva» y otro color, y su clave sale del libro citado en cada una.',
  },
]

/** Notas sobre el material que no dependen de una pregunta puntual. */
const NOTAS: string[] = [
  'Los videos del MIT (6.5, 6.6 y los de recomendación) son obligatorios según la bibliografía, pero no están en PDF: lo que dicen se toma de las notas de clase y no se pudo cotejar.',
  'Data fabric, IA como servicio, la pirámide de RAG y RAG 1.0/2.0 aparecen solo en las notas de clase (diapositivas); ningún libro de las carpetas los desarrolla.',
  '«Designing LLM applications», cap. 12, y el «O\'Reilly del canguro» están nombrados en las notas pero no están en las carpetas.',
  'Las páginas citadas son las del PDF de la carpeta, no la página impresa del libro.',
]

export function Temario() {
  const confirmados = temario.filter((t) => t.prio !== 'Pend' && t.prio !== 'Cond')
  const conReal = temario.filter((t) => de(t).some((q) => esParcial(q) || esPrimero(q)) && t.prio !== 'Pend')
  const dudosas = questions.filter((q) => !puntua(q))
  const reconstruidas = questions.filter((q) => q.recon)

  return (
    <main className="page">
      <section className="hero">
        <div>
          <p className="eyebrow">Sección 05 — Qué entra y de dónde sale</p>
          <h1 className="display">
            Temario<span className="accent-dot">.</span>
          </h1>
          <p className="lede">
            Los temas de las unidades 4, 5 y 6, con la prioridad de cada uno, dónde leerlo y qué se tomó. La base son las notas
            de clase y la bibliografía; las prioridades se contrastaron con el segundo parcial 2025 y con las preguntas del 1er
            parcial que ahora entran.
          </p>
        </div>
      </section>

      <section className="stats">
        <div className="stat">
          <span className="stat-value">{confirmados.length}</span>
          <span className="stat-label">temas con material en los libros</span>
        </div>
        <div className="stat">
          <span className="stat-value">{conReal.length}</span>
          <span className="stat-label">con consignas reales de la cátedra</span>
        </div>
        <div className="stat">
          <span className="stat-value">{dudosas.length}</span>
          <span className="stat-label">claves pendientes de verificación</span>
        </div>
      </section>

      <section className="tm-legend">
        <p>
          <span className="prio prio-A">A</span> muy probable · <span className="prio prio-B">B</span> probable ·{' '}
          <span className="prio prio-C">C</span> alcanza con reconocerlo · <span className="prio prio-Cond">Cond.</span> condicional ·{' '}
          <span className="prio prio-Pend">Sin conf.</span> sin confirmar
        </p>
        <p className="muted small">
          Evidencia: «real» cuenta las consignas del segundo parcial 2025 (P) y las del 1er parcial que ahora entran (1P); las
          preguntas nuevas no cuentan como evidencia. Fuentes: Notas es la pestaña «Notas de clase»; Biblio, la pestaña
          «Bibliografía»; Libro, el PDF de la carpeta de la unidad con capítulo y página.
        </p>
      </section>

      {bloques.map((b) => {
        const items = temario.filter((t) => t.bloque === b.key)
        return (
          <section key={b.key} className="group">
            <div className="section-head">
              <h2 className="h2">
                <span className="unit">{b.unit}</span> {b.name}
              </h2>
              <span className="muted small">{b.aviso ?? `${items.length} temas`}</span>
            </div>
            <ol className="tm-list">
              {items.map((t) => (
                <Fila key={t.n} t={t} />
              ))}
            </ol>
          </section>
        )
      })}

      <section className="group">
        <div className="section-head">
          <h2 className="h2">Registros analizados</h2>
          <span className="muted small">Qué es cada fuente y qué aportó</span>
        </div>
        <ul className="tm-list">
          {REGISTROS.map((r) => (
            <li key={r.archivo} className="tm-item">
              <div className="tm-main">
                <p className="tm-title">{r.archivo}</p>
                <p className="muted small">{r.detalle}</p>
              </div>
              <div className="tm-side small">
                <span className="tag">{r.tipo}</span>
                <span className="muted">{typeof r.n() === 'number' ? `${r.n()} preguntas` : r.n()}</span>
              </div>
            </li>
          ))}
        </ul>
      </section>

      <section className="group">
        <div className="section-head">
          <h2 className="h2">Pendientes de verificación</h2>
          <span className="muted small">No suman puntaje hasta que su id figure en src/cuestionarios/verificadas.ts</span>
        </div>
        <ul className="tm-list">
          {dudosas.length === 0 && (
            <li className="tm-item">
              <div className="tm-main">
                <p className="small">No quedan claves pendientes: todas las preguntas suman al puntaje.</p>
              </div>
            </li>
          )}
          {agrupar(dudosas).map(([motivo, qs]) => (
            <li key={motivo} className="tm-item">
              <div className="tm-main">
                <p className="tm-title">Clave sin verificar · {qs.length === 1 ? qs[0].src : `${qs.length} preguntas`}</p>
                <p className="muted small">{motivo[0].toUpperCase() + motivo.slice(1)}</p>
                <p className="small tm-ids">{qs.map((q) => q.id).join(' · ')}</p>
              </div>
            </li>
          ))}
        </ul>
      </section>

      <section className="group">
        <div className="section-head">
          <h2 className="h2">Decisiones tomadas</h2>
          <span className="muted small">Cómo se trató el material</span>
        </div>
        <ul className="tm-list">
          {DECISIONES.map((d) => (
            <li key={d.titulo} className="tm-item">
              <div className="tm-main">
                <p className="tm-title">{d.titulo}</p>
                <p className="muted small">{d.texto}</p>
                {d.ids && <p className="small tm-ids">{d.ids}</p>}
              </div>
            </li>
          ))}
        </ul>
      </section>

      <section className="group">
        <div className="section-head">
          <h2 className="h2">Limitaciones del material</h2>
          <span className="muted small">Texto reconstruido que no se puede cotejar: queda marcado</span>
        </div>
        <ul className="tm-list">
          {reconstruidas.map((q) => (
            <li key={q.id} className="tm-item">
              <div className="tm-main">
                <p className="tm-title">Texto reconstruido · {q.src}</p>
                <p className="muted small">
                  {q.recon![0].toUpperCase() + q.recon!.slice(1)} {puntua(q) ? q.nota?.match(/Se puntúa:.*$/)?.[0] ?? '' : 'No suma puntaje.'}
                </p>
                <p className="small tm-ids">{q.id}</p>
              </div>
            </li>
          ))}
          {NOTAS.map((d) => (
            <li key={d} className="tm-item">
              <div className="tm-main">
                <p className="small">{d}</p>
              </div>
            </li>
          ))}
        </ul>
      </section>
    </main>
  )
}

/** Junta las preguntas que comparten el mismo motivo de duda (salvo la referencia entre paréntesis). */
function agrupar(qs: Question[]) {
  const m = new Map<string, Question[]>()
  for (const q of qs) {
    const k = q.dud!.replace(/\s*\([^)]*\)\.?$/, '.')
    m.set(k, [...(m.get(k) ?? []), q])
  }
  return [...m]
}

function Fila({ t }: { t: Tema }) {
  const qs = de(t)
  const p = cuenta(qs, esParcial)
  const p1 = cuenta(qs, esPrimero)
  const practica = qs.length - p - p1
  const mapa = t.mapa ? findMindMap(t.mapa) : undefined
  const graficos = (t.graficos ?? []).map((id) => diagrams.find((d) => d.id === id)).filter((d) => !!d)
  const corto = t.prio === 'Cond' ? 'Cond.' : t.prio === 'Pend' ? 'Sin conf.' : t.prio

  return (
    <li className="tm-item">
      <span className="index">{t.n}</span>
      <div className="tm-main">
        <p className="tm-title">
          <span className={`prio prio-${t.prio}`} title={prioridadLabel[t.prio]}>
            {corto}
          </span>{' '}
          {t.titulo}
        </p>
        <p className="small">{t.fijar}</p>
        {t.nota && <p className="small tm-nota">{t.nota}</p>}
        <p className="muted small">
          Biblio: {t.biblio} · Notas: {t.notas}
          {t.libro ? ` · Libro: ${t.libro}` : ''}
        </p>
      </div>
      <div className="tm-side small">
        <span className={p + p1 > 0 ? 'tm-real' : 'muted'}>
          {p + p1 > 0 ? `Real: ${[p ? `${p} P` : '', p1 ? `${p1} 1P` : ''].filter(Boolean).join(' + ')}` : 'Sin consignas reales'}
        </span>
        <span className="muted">Nuevas: {practica}</span>
        <span className="tm-links">
          {mapa && (
            <a className="link-quiet" href={`#/mapas/${mapa.id}`}>
              Mapa
            </a>
          )}
          {figurasDe(t.n).length + relacionadasDe(t.n).length > 0 && (
            <a className="link-quiet" href={`#/figuras/${t.n}`}>
              Figuras ({figurasDe(t.n).length || relacionadasDe(t.n).length})
            </a>
          )}
          {graficos.map((d, i) => (
            <a key={d!.id} className="link-quiet" href={`#/g/${d!.id}`} title={d!.title}>
              Gráfico{graficos.length > 1 ? ` ${i + 1}` : ''}
            </a>
          ))}
        </span>
      </div>
    </li>
  )
}
