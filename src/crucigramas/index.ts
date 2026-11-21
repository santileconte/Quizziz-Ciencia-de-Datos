import type { PuzzleDef } from '../lib/crossword'
import { bloques } from '../temario'
import { crucigramas } from './datos'

export interface CrosswordUnit {
  key: string
  unit: string
  name: string
  puzzles: PuzzleDef[]
}

// Para sumar un crucigrama: agregarlo en datos.ts, dentro de su bloque.
export const crosswordUnits: CrosswordUnit[] = bloques
  .map((b) => ({ key: b.key, unit: b.unit, name: b.name, puzzles: crucigramas[b.key] ?? [] }))
  .filter((u) => u.puzzles.length > 0)

const all = crosswordUnits.flatMap((u) => u.puzzles.map((p, i) => ({ def: p, unit: u, index: i })))

export const findPuzzle = (id: string) => all.find((p) => p.def.id === id)
