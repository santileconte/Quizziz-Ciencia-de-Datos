import mapasData from './mapas.json'
import apunteData from './apunte.json'
import { bloques } from '../temario'

// mapas.json y apunte.json los genera tools/build_apunte.py a partir de tools/contenido_apunte.py y
// tools/contenido_mapas.py. Cada concepto del mapa guarda en `refs` los bloques del apunte de estudio que lo
// explican: "s03.2" es un párrafo y "s03.4:1" es la fila 1 de una tabla.

export interface Leaf {
  term: string
  text: string
  refs: string[]
}

export interface Branch {
  label: string
  leaves: Leaf[]
}

export interface MindMapDef {
  id: string
  unit: string
  num: string
  title: string
  subtitle: string
  kicker: string
  center: string
  recordar: string
  left: Branch[]
  right: Branch[]
}

export type Block =
  | { id: string; t: 'h' | 'p' | 'li' | 'callout'; text: string }
  | { id: string; t: 'table'; rows: string[][]; head: boolean }

export interface Section {
  id: string
  unit: string
  title: string
  /** Fuente principal, con páginas: «Reis, cap. 2, págs. 1–9». */
  src: string
  /** Figuras del libro o pestañas del documento de la materia que también se usaron. */
  orig: string
  blocks: Block[]
}

export const mindMaps = mapasData as MindMapDef[]
export const sections = apunteData as Section[]

export const mapUnits = bloques
  .map((u) => ({ ...u, maps: mindMaps.filter((m) => m.unit === u.key) }))
  .filter((u) => u.maps.length > 0)

export const findMindMap = (id: string) => mindMaps.find((m) => m.id === id)

const sectionById = new Map(sections.map((s) => [s.id, s]))
const blockById = new Map(sections.flatMap((s) => s.blocks.map((b) => [b.id, { section: s, block: b }] as const)))

export interface Excerpt {
  ref: string
  section: Section
  block: Block
  /** Fila de la tabla, si la referencia apunta a una sola fila. */
  row?: number
}

export function resolveRef(ref: string): Excerpt | undefined {
  const [id, row] = ref.split(':')
  const hit = blockById.get(id)
  if (!hit) return undefined
  return { ref, section: hit.section, block: hit.block, row: row === undefined ? undefined : Number(row) }
}

/** Conceptos en orden de lectura: ramas de la izquierda de arriba abajo y después las de la derecha. */
export const leavesOf = (m: MindMapDef) =>
  [...m.left.map((b) => ({ b, side: 'left' as const })), ...m.right.map((b) => ({ b, side: 'right' as const }))].flatMap(
    ({ b, side }) => b.leaves.map((leaf) => ({ leaf, branch: b, side })),
  )

/** Secciones del apunte que usa un grupo de conceptos, en el orden del apunte. */
export const sectionsOf = (leaves: Leaf[]) =>
  [...new Set(leaves.flatMap((l) => l.refs.map((r) => r.split('.')[0])))]
    .sort()
    .map((id) => sectionById.get(id)!)
    .filter(Boolean)
