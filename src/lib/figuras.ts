import data from '../figuras/figuras.json'
import { figura } from '../cuestionarios'
import { questions } from '../cuestionarios'
import { temario, type Tema, type Prioridad } from '../temario'

/**
 * Figuras originales de los libros de la cátedra (carpetas Unidad 4, 5 y 6), agrupadas por tema.
 *
 * Se recortan de los PDF con `tools/figuras/extraer.py` y se arman con `tools/figuras/build_figuras.py`.
 * Cada figura cita libro, número de figura y página del PDF.
 *
 * Orden dentro de cada tema (`rank`):
 *   1 · Ligada a una consigna real: explica algo que se preguntó en el parcial 2025 o en el 1er parcial que entra ahora.
 *   2 · Pedida en clase: las notas de clase piden ese gráfico o su concepto.
 *   3 · Figura central de un libro obligatorio.
 *   4 · Complementaria.
 */

export interface Ref {
  archivo: string
  corto?: string
  pag?: number
  nota?: string
}

export interface Figura {
  id: string
  tema: string
  orden: number
  rank: 1 | 2 | 3 | 4 | 5
  nivel: string
  title: string | null
  w: number
  h: number
  refs: Ref[]
  /** Archivo de la página que se muestra (cuando la figura está en varias). */
  mostrada?: string
  tipo: string
  nota?: string | null
  legib?: string | null
  /** Figuras que vienen de una pregunta (están en src/cuestionarios/img). */
  qimg?: string
  preguntas?: string[]
}

const full = import.meta.glob('../figuras/img/*.webp', { eager: true, query: '?url', import: 'default' }) as Record<string, string>
const thumbs = import.meta.glob('../figuras/thumb/*.webp', { eager: true, query: '?url', import: 'default' }) as Record<string, string>

export const figuras = (data as { figuras: Figura[] }).figuras
const tambien = (data as { tambien: Record<string, string[]> }).tambien

export const imagenDe = (f: Figura) => (f.qimg ? figura(f.qimg) : full[`../figuras/img/${f.id}.webp`])
export const miniaturaDe = (f: Figura) => thumbs[`../figuras/thumb/${f.id}.webp`] ?? imagenDe(f)

const porId = new Map(figuras.map((f) => [f.id, f]))

/** Figuras propias del tema, ya ordenadas por prioridad. */
export const figurasDe = (n: string) => figuras.filter((f) => f.tema === n).sort((a, b) => a.orden - b.orden)

/** Figuras de otros temas que también sirven para este (por ejemplo, los cinco flujos en el repaso). */
export const relacionadasDe = (n: string) => (tambien[n] ?? []).map((id) => porId.get(id)!).filter(Boolean)

export const niveles: { rank: Figura['rank']; titulo: string; detalle: string }[] = [
  { rank: 1, titulo: 'Ligadas a una consigna real', detalle: 'Explican lo que se preguntó en el parcial 2025 o en las preguntas del 1er parcial que entran ahora.' },
  { rank: 2, titulo: 'Pedidas en clase', detalle: 'Las notas de clase piden ese gráfico o el concepto que muestra.' },
  { rank: 3, titulo: 'Figuras centrales del libro', detalle: 'Resumen un tema de un libro obligatorio de las carpetas U4, U5 o U6.' },
  { rank: 4, titulo: 'Complementarias', detalle: 'Amplían el tema; disponibles para consultar.' },
  { rank: 5, titulo: 'Otras', detalle: 'Sin uso por ahora.' },
]

export const archivos: Record<string, string> = Object.fromEntries(
  figuras.flatMap((f) => f.refs.map((r) => [r.corto ?? r.archivo, r.archivo])),
)

const PRIO_ORDEN: Record<Prioridad, number> = { A: 0, B: 1, C: 2, Cond: 3, Pend: 4 }

/** Consignas del parcial 2025 y del 1er parcial que entran ahora, de cada tema. */
export const consignasReales = (t: Tema) =>
  questions.filter((q) => t.temas.includes(q.tema) && (q.modalidad === 'parcial' || q.modalidad === 'primero')).length

/** Temas con figuras, ordenados por importancia: prioridad, consignas reales, figuras de examen y orden de clase. */
export const temasPorImportancia = (lista: Tema[] = temario) =>
  lista
    .map((t) => ({ t, figs: figurasDe(t.n), rel: relacionadasDe(t.n), reales: consignasReales(t) }))
    .filter((x) => x.figs.length + x.rel.length > 0)
    .sort(
      (a, b) =>
        PRIO_ORDEN[a.t.prio] - PRIO_ORDEN[b.t.prio] ||
        b.reales - a.reales ||
        b.figs.filter((f) => f.rank <= 2).length - a.figs.filter((f) => f.rank <= 2).length ||
        temario.indexOf(a.t) - temario.indexOf(b.t),
    )

export const tituloDe = (f: Figura) => f.title ?? `Figura ${f.orden} · ${f.tipo.toLowerCase()}`
