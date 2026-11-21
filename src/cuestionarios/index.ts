import type { ItemDef, Modalidad, Question, UnitKey } from '../lib/quiz'
import { parcial2025 } from './parcial-2025'
import { primerParcial } from './primer-parcial'
import { propias } from './propias'
import { verificadas, reemplazadas } from './verificadas'
import { bloques } from '../temario'

export { casos } from './casos'

export const quizUnits = bloques

type Cruda = ItemDef & { unit: UnitKey; id?: string }

/** Las preguntas con clave en duda dejan de estarlo cuando su id figura en `verificadas.ts`. */
const armar = (modalidad: Modalidad, prefijo: string, items: Cruda[]): Question[] =>
  items.map((item, i) => {
    const id = item.id ?? `${prefijo}-${String(i + 1).padStart(2, '0')}`
    const q = { ...item, id, modalidad } as Question
    if (q.dud && verificadas[id]) {
      delete q.dud
      q.verif = verificadas[id]
    }
    return q
  })

// Cada pregunta figura una sola vez.
const todas: Question[] = [
  ...armar('parcial', 'pc25', parcial2025),
  ...armar('primero', 'pp', primerParcial),
  ...armar('propia', 'n', propias),
]

/** Versiones reemplazadas por otra de mayor jerarquía (ver `verificadas.ts`): se conservan como registro, no se practican. */
export const historicas: (Question & { por: string; motivo: string })[] = todas
  .filter((q) => reemplazadas[q.id])
  .map((q) => ({ ...q, ...reemplazadas[q.id] }))

export const questions: Question[] = todas.filter((q) => !reemplazadas[q.id])

const porId = new Map(questions.map((q) => [q.id, q]))
export const findQuestion = (id: string) => porId.get(id)

const figuras = import.meta.glob('./img/*.{png,jpg,jpeg,webp}', { eager: true, query: '?url', import: 'default' }) as Record<string, string>

/** URL de una figura de `src/cuestionarios/img/`. */
export const figura = (file: string) => figuras[`./img/${file}`]
