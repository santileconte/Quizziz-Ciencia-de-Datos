import type { Diagram, DiagramConfig } from './types'
import { figuras, imagenDe } from './figuras'
import { temario } from '../temario'

const images = import.meta.glob('../graficos/*.{png,jpg,jpeg,webp,PNG,JPG,JPEG,WEBP}', {
  eager: true,
  query: '?url',
  import: 'default',
}) as Record<string, string>

const configs = import.meta.glob('../graficos/*.json', { eager: true, import: 'default' }) as Record<string, DiagramConfig>

const baseName = (path: string) => path.split('/').pop()!.replace(/\.[^.]+$/, '')

const prettify = (file: string) => {
  const s = file.replace(/[-_]+/g, ' ').trim()
  return s.charAt(0).toUpperCase() + s.slice(1)
}

const slug = (s: string) =>
  s
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '')

const configByName = Object.fromEntries(Object.entries(configs).map(([p, c]) => [baseName(p), c]))

export const diagrams: Diagram[] = Object.entries(images)
  .map(([path, url]) => {
    const file = baseName(path)
    const config = configByName[file] ?? { blanks: [] }
    return {
      id: slug(file),
      file,
      image: url,
      title: config.title || prettify(file),
      config,
      configured: config.blanks.length > 0,
    }
  })
  // Por bloque (B1 antes que B2), después por orden dentro del bloque.
  .sort(
    (a, b) =>
      Number(!a.config.topic) - Number(!b.config.topic) ||
      (a.config.topic ?? '').localeCompare(b.config.topic ?? '', 'es', { numeric: true }) ||
      (a.config.order ?? 999) - (b.config.order ?? 999) ||
      a.title.localeCompare(b.title, 'es'),
  )

/**
 * Figuras originales que se pueden completar (src/figuras/huecos/<figura>.json).
 * Los huecos tapan el texto que se leyó en la figura y se verificó a mano; no se mezclan con los gráficos
 * del inicio: tienen sus propias series por tema (#/serie/fig-<tema>).
 */
const figConfigs = import.meta.glob('../figuras/huecos/*.json', { eager: true, import: 'default' }) as Record<string, DiagramConfig>
const figPorId = new Map(figuras.map((f) => [f.id, f]))

export const figureDiagrams: Diagram[] = Object.values(figConfigs)
  .filter((c) => c.figura && figPorId.has(c.figura) && c.blanks.length > 0)
  .map((c) => {
    const f = figPorId.get(c.figura!)!
    const tema = temario.find((t) => t.n === f.tema)
    const config: DiagramConfig = { ...c, topic: tema ? `Tema ${tema.n} · ${tema.titulo}` : c.topic }
    return { id: `fig-${f.id}`, file: f.id, image: imagenDe(f), title: c.title || f.id, config, configured: true }
  })
  .sort((a, b) => a.file.localeCompare(b.file, 'es', { numeric: true }))

/** Versión para completar de una figura original, si la tiene. */
export const practicaDeFigura = (figuraId: string) => figureDiagrams.find((d) => d.config.figura === figuraId)

export const findDiagram = (id: string) => diagrams.find((d) => d.id === id) ?? figureDiagrams.find((d) => d.id === id)

export const levelOf = (b: { level?: string }) => (b.level === 'extra' ? 'extra' : 'clave')

export interface Group {
  key: string
  unit: string
  name: string
  diagrams: Diagram[]
}

/** Gráficos agrupados por bloque («U5 · Arquitecturas e Ingeniería de Datos» → clave «u5»), en el orden en que aparecen. */
export const groups: Group[] = (() => {
  const map = new Map<string, Diagram[]>()
  for (const d of diagrams) {
    const topic = d.config.topic || 'Otros'
    map.set(topic, [...(map.get(topic) ?? []), d])
  }
  return [...map.entries()].map(([topic, items]) => {
    const [unit, name] = topic.split(' · ')
    return { key: slug(unit), unit: name ? unit : '', name: name ?? topic, diagrams: items }
  })
})()

export const allGroup: Group = { key: 'todo', unit: '', name: 'Todos los gráficos', diagrams: groups.flatMap((g) => g.diagrams) }

/** Series de figuras originales: una por tema, en el orden de prioridad de las figuras. */
export const figureGroups: Group[] = temario
  .map((t) => {
    const items = figuras
      .filter((f) => f.tema === t.n)
      .sort((a, b) => a.orden - b.orden)
      .map((f) => practicaDeFigura(f.id))
      .filter((d): d is Diagram => !!d)
    return { key: `fig-${t.n}`, unit: `Tema ${t.n}`, name: `Figuras originales · ${t.titulo}`, diagrams: items }
  })
  .filter((g) => g.diagrams.length > 0)

export const findGroup = (key: string) =>
  key === allGroup.key ? allGroup : (groups.find((g) => g.key === key) ?? figureGroups.find((g) => g.key === key))
