import { useCallback, useEffect, useMemo, useRef, useState } from 'react'
import { bloques, prioridadLabel, temario, type Tema } from '../temario'
import { diagrams, figureDiagrams, figureGroups, practicaDeFigura } from '../lib/diagrams'
import {
  archivos,
  consignasReales,
  figurasDe,
  imagenDe,
  miniaturaDe,
  niveles,
  relacionadasDe,
  temasPorImportancia,
  tituloDe,
  type Figura,
} from '../lib/figuras'

const corto = (t: Tema) => (t.prio === 'Cond' ? 'Cond.' : t.prio === 'Pend' ? 'Sin conf.' : t.prio)

function Prio({ t }: { t: Tema }) {
  return (
    <span className={`prio prio-${t.prio}`} title={prioridadLabel[t.prio]}>
      {corto(t)}
    </span>
  )
}

/** Referencias de una figura: archivo y página de cada aparición. */
function Refs({ f }: { f: Figura }) {
  return (
    <span className="fg-refs">
      {f.refs.map((r, i) => (
        <span key={i} title={r.corto ? archivos[r.corto] : r.archivo}>
          {r.corto ? `${r.corto}${r.nota ? `, ${r.nota.toLowerCase()}` : ''}, pág. ${r.pag}` : r.archivo}
          {i < f.refs.length - 1 ? ' · ' : ''}
        </span>
      ))}
    </span>
  )
}

/* ---------- Índice: todos los temas, por importancia ---------- */

export function FigurasIndice({ compacto = false }: { compacto?: boolean }) {
  const total = temario.reduce((n, t) => n + figurasDe(t.n).length, 0)
  const contenido = bloques.map((b) => {
    const items = temasPorImportancia(temario.filter((t) => t.bloque === b.key))
    if (!items.length) return null
    return (
      <div key={b.key} className="fg-bloque">
        <h3 className="fg-bloque-titulo">
          <span className="unit">{b.unit}</span> {b.name}
        </h3>
        <ul className="fg-temas">
          {items.map(({ t, figs, rel, reales }) => {
            const examen = figs.filter((f) => f.rank <= 2).length
            const muestra = (figs.length ? figs : rel).slice(0, compacto ? 3 : 4)
            return (
              <li key={t.n}>
                <a className="fg-tema" href={`#/figuras/${t.n}`}>
                  <span className="fg-tema-head">
                    <span className="index">{t.n}</span>
                    <Prio t={t} />
                    <b>{t.titulo}</b>
                  </span>
                  <span className="fg-strip" aria-hidden>
                    {muestra.map((f) => (
                      <img key={f.id} src={miniaturaDe(f)} alt="" loading="lazy" />
                    ))}
                  </span>
                  <span className="muted small">
                    {figs.length ? `${figs.length} ${figs.length === 1 ? 'figura' : 'figuras'}` : `${rel.length} figuras de otros temas`}
                    {examen > 0 && ` · ${examen} de examen o pedidas en clase`}
                    {reales > 0 && ` · ${reales} ${reales === 1 ? 'consigna real' : 'consignas reales'} (parciales 2025)`}
                    {(() => {
                      const n = figs.filter((f) => practicaDeFigura(f.id)).length
                      return n > 0 ? ` · ${n} para completar` : ''
                    })()}
                  </span>
                </a>
              </li>
            )
          })}
        </ul>
      </div>
    )
  })

  if (compacto)
    return (
      <section className="group">
        <div className="section-head">
          <h2 className="h2">Figuras originales por tema</h2>
          <span className="muted small">
            {total} figuras de los libros de la cátedra · <a className="link-quiet" href="#/figuras">Ver todas →</a>
          </span>
        </div>
        {contenido}
      </section>
    )

  return (
    <main className="page">
      <a className="back" href="#/">
        ← Gráficos
      </a>
      <section className="hero hero-small">
        <div>
          <p className="eyebrow">Figuras originales</p>
          <h1 className="display">
            Todas las figuras<span className="accent-dot">.</span>
          </h1>
          <p className="lede">
            Las {total} figuras recortadas de los libros obligatorios de las carpetas U4, U5 y U6, ordenadas por tema. En
            cada unidad van primero los temas de prioridad más alta y los que más se tomaron. Dentro de cada tema, primero las
            figuras ligadas a una consigna real y las que se pidieron en clase. Cada una dice libro, figura y página del PDF.
          </p>
          <p className="lede">
            {figureDiagrams.length > 0
              ? `${figureDiagrams.length} figuras se pueden completar: sus textos se taparon con huecos (${figureDiagrams.reduce((n, d) => n + d.config.blanks.length, 0)} en total) y se practican igual que los gráficos del inicio.`
              : 'Para practicar completando, usá los gráficos del inicio: son estas mismas figuras con el texto tapado.'}
          </p>
        </div>
      </section>
      {contenido}
      <Leyenda />
    </main>
  )
}

function Leyenda() {
  return (
    <section className="group fg-leyenda">
      <div className="section-head">
        <h2 className="h2">Archivos de origen</h2>
      </div>
      <ul className="small">
        {Object.entries(archivos).map(([k, v]) => (
          <li key={k}>
            <b>{k}</b> · {v}
          </li>
        ))}
        <li className="muted">
          Las páginas son las del PDF. Si una figura está igual en varios archivos se muestra una sola vez, con todas sus
          páginas.
        </li>
      </ul>
    </section>
  )
}

/* ---------- Página de un tema ---------- */

export function FigurasTema({ tema }: { tema: Tema }) {
  const propias = useMemo(() => figurasDe(tema.n), [tema.n])
  const rel = useMemo(() => relacionadasDe(tema.n), [tema.n])
  const todas = useMemo(() => [...propias, ...rel.filter((f) => !propias.includes(f))], [propias, rel])
  const [abierta, setAbierta] = useState<number | null>(null)
  const practicar = (tema.graficos ?? []).map((id) => diagrams.find((d) => d.id === id)).filter((d) => !!d)
  const reales = consignasReales(tema)
  const i = temario.indexOf(tema)
  const ant = temario.slice(0, i).reverse().find((t) => figurasDe(t.n).length + relacionadasDe(t.n).length)
  const sig = temario.slice(i + 1).find((t) => figurasDe(t.n).length + relacionadasDe(t.n).length)

  const serie = figureGroups.find((g) => g.key === `fig-${tema.n}`)

  const tarjeta = (f: Figura) => {
    const p = practicaDeFigura(f.id)
    return (
      <div key={f.id} className="fg-item">
        {carta(f)}
        {p && (
          <a className="fg-fill" href={`#/g/${p.id}`}>
            Completar · {p.config.blanks.length} huecos
          </a>
        )}
      </div>
    )
  }

  const carta = (f: Figura) => (
    <button className="fg-card" onClick={() => setAbierta(todas.indexOf(f))}>
      <span className="fg-thumb">
        <img src={miniaturaDe(f)} alt={tituloDe(f)} loading="lazy" width={f.w} height={f.h} />
      </span>
      <span className="fg-body">
        <span className="fg-title">{tituloDe(f)}</span>
        <span className="muted small">{f.tipo}</span>
        <Refs f={f} />
        {f.nota && <span className="fg-nota small">{f.nota}</span>}
        {f.legib && <span className="fg-legib small">{f.legib}</span>}
      </span>
    </button>
  )

  return (
    <main className="page">
      <div className="view-head">
        <a className="back" href="#/figuras">
          ← Todas las figuras
        </a>
        <span className="view-meta">
          {ant && (
            <a className="link-quiet" href={`#/figuras/${ant.n}`}>
              ← {ant.n}
            </a>
          )}
          {sig && (
            <a className="link-quiet" href={`#/figuras/${sig.n}`}>
              {sig.n} →
            </a>
          )}
        </span>
      </div>
      <section className="fg-hero">
        <p className="eyebrow">
          Tema {tema.n} · {bloques.find((b) => b.key === tema.bloque)?.unit} · Figuras
        </p>
        <h1 className="fg-h1">
          <Prio t={tema} /> {tema.titulo}
        </h1>
        <p className="muted small">
          {propias.length} {propias.length === 1 ? 'figura' : 'figuras'}{rel.length ? ` · ${rel.length} de otros temas` : ''} ·{' '}
          {reales ? `${reales} ${reales === 1 ? 'consigna real' : 'consignas reales'} (parciales 2025)` : 'sin consignas reales'} · Libro: {tema.libro}
        </p>
        {(practicar.length > 0 || tema.mapa || serie) && (
          <p className="fg-links small">
            {serie && (
              <a className="link-quiet fg-serie" href={`#/serie/${serie.key}`}>
                Completar las figuras en serie · {serie.diagrams.length} {serie.diagrams.length === 1 ? 'figura' : 'figuras'}
              </a>
            )}
            {practicar.map((d) => (
              <a key={d!.id} className="link-quiet" href={`#/g/${d!.id}`}>
                Completar: {d!.title}
              </a>
            ))}
            {tema.mapa && (
              <a className="link-quiet" href={`#/mapas/${tema.mapa}`}>
                Mapa conceptual
              </a>
            )}
          </p>
        )}
      </section>

      {niveles.map((nv) => {
        const fs = propias.filter((f) => f.rank === nv.rank)
        if (!fs.length) return null
        return (
          <section key={nv.rank} className={`group fg-nivel fg-nivel-${nv.rank}`}>
            <div className="section-head">
              <h2 className="h2">
                <span className="fg-nivel-n">{nv.rank}</span> {nv.titulo}
              </h2>
              <span className="muted small">
                {fs.length} · {nv.detalle}
              </span>
            </div>
            <div className="fg-grid">{fs.map(tarjeta)}</div>
          </section>
        )
      })}

      {rel.length > 0 && (
        <section className="group">
          <div className="section-head">
            <h2 className="h2">De otros temas</h2>
            <span className="muted small">Figuras de otros temas que sirven para repasar este.</span>
          </div>
          <div className="fg-grid">{rel.map(tarjeta)}</div>
        </section>
      )}

      {abierta !== null && (
        <Visor figuras={todas} indice={abierta} onCambiar={setAbierta} onCerrar={() => setAbierta(null)} />
      )}
    </main>
  )
}

/* ---------- Visor con zoom ---------- */

function Visor({
  figuras,
  indice,
  onCambiar,
  onCerrar,
}: {
  figuras: Figura[]
  indice: number
  onCambiar: (i: number) => void
  onCerrar: () => void
}) {
  const f = figuras[indice]
  const marco = useRef<HTMLDivElement>(null)
  const [vista, setVista] = useState({ s: 1, x: 0, y: 0 })
  const [ajuste, setAjuste] = useState(1)
  const punteros = useRef(new Map<number, { x: number; y: number }>())
  const gesto = useRef<{ d: number; s: number } | null>(null)

  const encajar = useCallback(() => {
    const el = marco.current
    if (!el) return
    const s = Math.min(el.clientWidth / f.w, el.clientHeight / f.h, 1.5)
    setAjuste(s)
    setVista({ s, x: (el.clientWidth - f.w * s) / 2, y: (el.clientHeight - f.h * s) / 2 })
  }, [f])

  useEffect(() => {
    encajar()
    window.addEventListener('resize', encajar)
    return () => window.removeEventListener('resize', encajar)
  }, [encajar])

  const zoomEn = useCallback((factor: number, cx?: number, cy?: number) => {
    const el = marco.current
    if (!el) return
    setVista((v) => {
      const s = Math.min(Math.max(v.s * factor, 0.05), 8)
      const px = cx ?? el.clientWidth / 2
      const py = cy ?? el.clientHeight / 2
      return { s, x: px - ((px - v.x) * s) / v.s, y: py - ((py - v.y) * s) / v.s }
    })
  }, [])

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onCerrar()
      else if (e.key === 'ArrowRight' && indice < figuras.length - 1) onCambiar(indice + 1)
      else if (e.key === 'ArrowLeft' && indice > 0) onCambiar(indice - 1)
      else if (e.key === '+' || e.key === '=') zoomEn(1.25)
      else if (e.key === '-') zoomEn(0.8)
      else if (e.key === '0') encajar()
    }
    window.addEventListener('keydown', onKey)
    document.body.style.overflow = 'hidden'
    return () => {
      window.removeEventListener('keydown', onKey)
      document.body.style.overflow = ''
    }
  }, [indice, figuras.length, onCambiar, onCerrar, zoomEn, encajar])

  useEffect(() => {
    const el = marco.current
    if (!el) return
    const onWheel = (e: WheelEvent) => {
      e.preventDefault()
      const r = el.getBoundingClientRect()
      zoomEn(e.deltaY < 0 ? 1.15 : 1 / 1.15, e.clientX - r.left, e.clientY - r.top)
    }
    el.addEventListener('wheel', onWheel, { passive: false })
    return () => el.removeEventListener('wheel', onWheel)
  }, [zoomEn])

  const down = (e: React.PointerEvent) => {
    ;(e.target as Element).setPointerCapture?.(e.pointerId)
    punteros.current.set(e.pointerId, { x: e.clientX, y: e.clientY })
    if (punteros.current.size === 2) {
      const [a, b] = [...punteros.current.values()]
      gesto.current = { d: Math.hypot(a.x - b.x, a.y - b.y), s: vista.s }
    }
  }
  const move = (e: React.PointerEvent) => {
    const prev = punteros.current.get(e.pointerId)
    if (!prev) return
    punteros.current.set(e.pointerId, { x: e.clientX, y: e.clientY })
    if (punteros.current.size === 2 && gesto.current) {
      const [a, b] = [...punteros.current.values()]
      const r = marco.current!.getBoundingClientRect()
      const factor = (gesto.current.s * (Math.hypot(a.x - b.x, a.y - b.y) / gesto.current.d)) / vista.s
      zoomEn(factor, (a.x + b.x) / 2 - r.left, (a.y + b.y) / 2 - r.top)
    } else if (punteros.current.size === 1) {
      setVista((v) => ({ ...v, x: v.x + e.clientX - prev.x, y: v.y + e.clientY - prev.y }))
    }
  }
  const up = (e: React.PointerEvent) => {
    punteros.current.delete(e.pointerId)
    if (punteros.current.size < 2) gesto.current = null
  }

  return (
    <div className="fg-visor" role="dialog" aria-modal="true" aria-label={tituloDe(f)}>
      <div className="fg-visor-bar">
        <div className="fg-visor-info">
          <b>{tituloDe(f)}</b>
          <span className="small">
            {f.nivel} · {f.tipo}
            {f.mostrada && f.refs.length > 1 ? ` · se muestra la de ${f.mostrada}` : ''}
          </span>
          <span className="small">
            <Refs f={f} />
            {f.refs.some((r) => r.nota) && ` · ${f.refs.find((r) => r.nota)!.nota}`}
          </span>
          {f.legib && <span className="small fg-legib">{f.legib}</span>}
        </div>
        <div className="fg-visor-tools">
          <button className="btn" onClick={() => zoomEn(0.8)} aria-label="Alejar">
            −
          </button>
          <span className="fg-zoom small">{Math.round((vista.s / ajuste) * 100)}%</span>
          <button className="btn" onClick={() => zoomEn(1.25)} aria-label="Acercar">
            +
          </button>
          <button className="btn" onClick={encajar}>
            Ajustar
          </button>
          <button
            className="btn"
            onClick={() => {
              const el = marco.current!
              setVista({ s: 1, x: (el.clientWidth - f.w) / 2, y: (el.clientHeight - f.h) / 2 })
            }}
          >
            Tamaño real
          </button>
          {practicaDeFigura(f.id) && (
            <a className="btn" href={`#/g/${practicaDeFigura(f.id)!.id}`}>
              Completar
            </a>
          )}
          <a className="btn" href={imagenDe(f)} target="_blank" rel="noreferrer">
            Abrir original
          </a>
          <button className="btn" onClick={onCerrar} aria-label="Cerrar">
            ✕
          </button>
        </div>
      </div>
      <div
        ref={marco}
        className="fg-visor-marco"
        onPointerDown={down}
        onPointerMove={move}
        onPointerUp={up}
        onPointerCancel={up}
        onDoubleClick={(e) => {
          const r = marco.current!.getBoundingClientRect()
          zoomEn(2, e.clientX - r.left, e.clientY - r.top)
        }}
      >
        <img
          src={imagenDe(f)}
          alt={tituloDe(f)}
          draggable={false}
          style={{ width: f.w, height: f.h, transform: `translate(${vista.x}px, ${vista.y}px) scale(${vista.s})` }}
        />
      </div>
      <div className="fg-visor-nav">
        <button className="btn" disabled={indice === 0} onClick={() => onCambiar(indice - 1)}>
          ← Anterior
        </button>
        <span className="small">
          {indice + 1} de {figuras.length} · arrastrá para mover, rueda o pellizco para ampliar
        </span>
        <button className="btn" disabled={indice === figuras.length - 1} onClick={() => onCambiar(indice + 1)}>
          Siguiente →
        </button>
      </div>
    </div>
  )
}
