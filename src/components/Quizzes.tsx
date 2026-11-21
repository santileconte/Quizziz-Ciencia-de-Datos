import { useMemo, useState } from 'react'
import { questions, quizUnits } from '../cuestionarios'
import { formatoLabel, mezclar, modalidades, puntua, type Formato, type Modalidad, type UnitKey } from '../lib/quiz'
import { loadRun, saveRun, useQuizStats, type Modo, type Run } from '../lib/quizProgress'
import { ordenTema, temaDe } from '../temario'
import { QuizRun } from './QuizRun'

type Filtro = 'todas' | 'errores' | 'nuevas'

// Solo los formatos que existen en el banco.
const FORMATOS = (Object.keys(formatoLabel) as Formato[]).filter((f) => questions.some((q) => q.t === f))
const FUENTES = modalidades.filter((m) => questions.some((q) => q.modalidad === m.key))
const ORIGINALES = FUENTES.filter((m) => m.original).map((m) => m.key)
const CANTIDADES = [10, 20, 40, 0]

export function Quizzes() {
  const stats = useQuizStats()
  const [run, setRun] = useState<Run | null>(null)
  const [guardada, setGuardada] = useState(() => {
    const r = loadRun()
    return r && !r.submitted ? r : null
  })
  const [fuentes, setFuentes] = useState<Modalidad[]>(ORIGINALES)
  const [unidad, setUnidad] = useState<UnitKey | 'todas'>('todas')
  const [formatos, setFormatos] = useState<Formato[]>(FORMATOS)
  const [modo, setModo] = useState<Modo>('practica')
  const [filtro, setFiltro] = useState<Filtro>('todas')
  const [cantidad, setCantidad] = useState(20)
  const [tema, setTema] = useState<string | null>(null)

  const base = useMemo(
    () => questions.filter((q) => fuentes.includes(q.modalidad) && (unidad === 'todas' || q.unit === unidad)),
    [fuentes, unidad],
  )

  const elegibles = base.filter((q) => {
    if (!formatos.includes(q.t)) return false
    if (tema && q.tema !== tema) return false
    if (filtro === 'errores') return stats[q.id] !== undefined && stats[q.id].last < 1
    if (filtro === 'nuevas') return stats[q.id] === undefined
    return true
  })

  const temas = useMemo(() => {
    const m = new Map<string, { n: number; hechas: number; suma: number }>()
    for (const q of base) {
      const s = m.get(q.tema) ?? { n: 0, hechas: 0, suma: 0 }
      const st = stats[q.id]
      m.set(q.tema, { n: s.n + 1, hechas: s.hechas + (st ? 1 : 0), suma: s.suma + (st?.last ?? 0) })
    }
    // En el orden del temario, que es el de las clases.
    return [...m].sort((a, b) => ordenTema(a[0]) - ordenTema(b[0]) || a[0].localeCompare(b[0], 'es'))
  }, [base, stats])

  const empezar = (ids: string[], titulo: string, m: Modo = modo) => {
    const next: Run = { ids, modo: m, titulo, idx: 0, answers: {}, checked: {}, intento: Date.now() % 100000, elapsed: 0, submitted: false }
    saveRun(next)
    setRun(next)
  }

  const start = () => {
    const ids = mezclar(elegibles).map((q) => q.id)
    const nombre = unidad === 'todas' ? 'Todos los bloques' : unidad.toUpperCase()
    empezar(cantidad ? ids.slice(0, cantidad) : ids, tema ?? nombre)
  }

  if (run) {
    return (
      <QuizRun
        key={run.intento}
        initial={run}
        onExit={() => {
          const r = loadRun()
          setGuardada(r && !r.submitted ? r : null)
          setRun(null)
        }}
        onRepeat={(ids, titulo) => empezar(mezclar(ids), titulo, run.modo)}
      />
    )
  }

  const conPuntaje = questions.filter(puntua)
  const hechas = conPuntaje.filter((q) => stats[q.id]).length
  const dominadas = conPuntaje.filter((q) => stats[q.id]?.last === 1).length
  const reales = questions.filter((q) => q.modalidad === 'parcial').length
  const catedra = questions.filter((q) => q.modalidad !== 'parcial' && modalidades.find((m) => m.key === q.modalidad)?.original).length
  const practica = questions.length - reales - catedra
  const toggleFormato = (f: Formato) =>
    setFormatos((fs) => (fs.includes(f) ? (fs.length > 1 ? fs.filter((x) => x !== f) : fs) : [...fs, f]))
  const toggleFuente = (f: Modalidad) => {
    setFuentes((fs) => (fs.includes(f) ? (fs.length > 1 ? fs.filter((x) => x !== f) : fs) : [...fs, f]))
    setTema(null)
  }
  const a = cantidad ? Math.min(cantidad, elegibles.length) : elegibles.length
  const sinVerificar = elegibles.filter((q) => !puntua(q)).length
  const bloque = quizUnits.find((u) => u.key === unidad)

  return (
    <main className="page">
      <section className="hero">
        <div>
          <p className="eyebrow">Sección 02 — Como en el parcial</p>
          <h1 className="display qz-display">
            Cuestionarios<span className="accent-dot">.</span>
          </h1>
          <p className="lede">
            Las consignas del segundo parcial 2025 y las preguntas del 1er parcial que ahora entran, sin retocar. Aparte,{' '}
            {practica} preguntas de práctica que no son de la cátedra, escritas a partir de los libros. Cada pregunta dice de
            qué pestaña, libro y página sale. Las de la cátedra no traen clave: se pueden responder, pero no suman hasta que
            confirmes su clave.
          </p>
        </div>
        <QuizArt />
      </section>

      <section className="stats">
        <div className="stat">
          <span className="stat-value">{reales}</span>
          <span className="stat-label">consignas del segundo parcial 2025</span>
        </div>
        <div className="stat">
          <span className="stat-value">{catedra}</span>
          <span className="stat-label">preguntas del 1er parcial que entran ahora</span>
        </div>
        <div className="stat">
          <span className="stat-value">
            {dominadas}/{hechas}
          </span>
          <span className="stat-label">perfectas sobre respondidas</span>
        </div>
      </section>

      <section className="setup">
        <div className="setup-row">
          <span className="setup-label">Fuente</span>
          <div className="setup-control">
            <div className="qz-chips">
              {FUENTES.map((f) => (
                <button key={f.key} className={`chip-toggle ${fuentes.includes(f.key) ? 'on' : ''}`} onClick={() => toggleFuente(f.key)} aria-pressed={fuentes.includes(f.key)} title={f.hint}>
                  {f.label}
                </button>
              ))}
            </div>
            <p className="muted small">
              {fuentes.every((f) => ORIGINALES.includes(f))
                ? 'Solo preguntas de la cátedra, con su texto y su clave originales.'
                : fuentes.some((f) => ORIGINALES.includes(f))
                  ? 'Mezcla de preguntas de la cátedra y de práctica. Cada pregunta lleva su etiqueta.'
                  : 'Solo práctica: no son de la cátedra ni cuentan como evidencia de lo que se toma.'}
            </p>
          </div>
        </div>
        <Fila label="Bloque" hint={unidad === 'todas' ? 'Todos juntos, incluidos los temas condicionales y sin confirmar.' : `${bloque?.name ?? ''}${bloque?.aviso ? `. ${bloque.aviso}` : ''}`}>
          <button className={unidad === 'todas' ? 'on' : ''} onClick={() => (setUnidad('todas'), setTema(null))}>
            Todos
          </button>
          {quizUnits.map((u) => (
            <button key={u.key} className={unidad === u.key ? 'on' : ''} onClick={() => (setUnidad(u.key), setTema(null))} title={u.name}>
              {u.unit}
            </button>
          ))}
        </Fila>
        <Fila label="Modo" hint={modo === 'practica' ? 'Corrección y explicación después de cada pregunta.' : 'Sin ayudas ni corrección: el resultado aparece al entregar.'}>
          <button className={modo === 'practica' ? 'on' : ''} onClick={() => setModo('practica')}>
            Práctica
          </button>
          <button className={modo === 'simulacro' ? 'on' : ''} onClick={() => setModo('simulacro')}>
            Simulacro
          </button>
        </Fila>
        <Fila label="Preguntas" hint="Se eligen al azar entre las disponibles.">
          {CANTIDADES.map((c) => (
            <button key={c} className={cantidad === c ? 'on' : ''} onClick={() => setCantidad(c)}>
              {c || 'Todas'}
            </button>
          ))}
        </Fila>
        <Fila label="Cuáles" hint={filtro === 'errores' ? 'Las que tu último intento no fue perfecto.' : filtro === 'nuevas' ? 'Las que todavía no respondiste.' : 'Sin filtrar por tu progreso.'}>
          {(
            [
              ['todas', 'Todas'],
              ['errores', 'Mis errores'],
              ['nuevas', 'Sin responder'],
            ] as const
          ).map(([v, label]) => (
            <button key={v} className={filtro === v ? 'on' : ''} onClick={() => setFiltro(v)}>
              {label}
            </button>
          ))}
        </Fila>
        <div className="setup-row">
          <span className="setup-label">Formatos</span>
          <div className="setup-control qz-chips">
            {FORMATOS.map((f) => (
              <button key={f} className={`chip-toggle ${formatos.includes(f) ? 'on' : ''}`} onClick={() => toggleFormato(f)} aria-pressed={formatos.includes(f)}>
                {formatoLabel[f]}
              </button>
            ))}
          </div>
        </div>
      </section>

      <div className="setup-foot">
        <span className="muted">
          {tema ? `${tema}: ` : ''}
          {a} de {elegibles.length} preguntas disponibles
          {sinVerificar > 0 ? ` · ${sinVerificar} con la clave sin verificar, que no suman puntaje` : ''}
        </span>
        <div className="setup-actions">
          {guardada && (
            <button className="btn ghost" onClick={() => setRun(guardada)}>
              Seguir donde quedaste ({guardada.idx + 1}/{guardada.ids.length})
            </button>
          )}
          <button className="btn primary big" disabled={!elegibles.length} onClick={start}>
            Empezar
          </button>
        </div>
      </div>

      <section className="group">
        <div className="section-head">
          <h2 className="h2">Por tema</h2>
          <span className="muted small">
            En el orden de las clases. Tocá un tema para practicar solo ese ·{' '}
            <a className="link-quiet" href="#/temario">
              Ver temario y prioridades →
            </a>
          </span>
        </div>
        <div className="qz-tema-grid">
          {temas.map(([nombre, s]) => {
            const prio = temaDe(nombre)?.prio
            return (
              <button key={nombre} className={`qz-tema ${tema === nombre ? 'on' : ''}`} onClick={() => setTema(tema === nombre ? null : nombre)} aria-pressed={tema === nombre}>
                <span>
                  {prio && <span className={`prio prio-${prio}`}>{prio === 'Cond' ? 'Cond.' : prio === 'Pend' ? 'Sin conf.' : prio}</span>} {nombre}
                </span>
                <span className="muted small">
                  {s.hechas}/{s.n}
                  {s.hechas ? ` · ${Math.round((s.suma / s.hechas) * 100)}%` : ''}
                </span>
              </button>
            )
          })}
        </div>
      </section>
    </main>
  )
}

function Fila({ label, hint, children }: { label: string; hint: string; children: React.ReactNode }) {
  return (
    <div className="setup-row">
      <span className="setup-label">{label}</span>
      <div className="setup-control">
        <div className="segmented big">{children}</div>
        <p className="muted small">{hint}</p>
      </div>
    </div>
  )
}

function QuizArt() {
  // Una hoja de parcial: consignas, un círculo en la opción elegida y un tilde en rojo de corrección.
  const opciones = [96, 140, 184, 228]
  return (
    <svg className="hero-art" viewBox="0 0 420 340" aria-hidden>
      <rect x="70" y="24" width="280" height="292" rx="14" className="art-line" />
      <rect x="100" y="54" width="200" height="12" rx="6" className="mm-art-branch" />
      {opciones.map((y, i) => (
        <g key={y}>
          <circle cx="116" cy={y + 6} r="11" className={i === 2 ? 'art-dot' : 'art-line faint'} />
          <rect x="144" y={y} width={i % 2 ? 150 : 176} height="12" rx="6" className="mm-art-leaf" />
        </g>
      ))}
      <path d="M322 196 L334 210 L358 176" className="qz-art-check" />
    </svg>
  )
}
