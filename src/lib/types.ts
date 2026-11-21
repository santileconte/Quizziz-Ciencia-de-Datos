export type Level = 'clave' | 'extra'

/** Hueco a completar. Coordenadas en píxeles de la imagen original. */
export interface Blank {
  id: string
  x: number
  y: number
  w: number
  h: number
  answer: string
  /** Otras respuestas que también se aceptan como correctas. */
  accept?: string[]
  level?: Level
}

export interface DiagramConfig {
  title?: string
  topic?: string
  width?: number
  height?: number
  /** Tamaño de letra de los huecos, en píxeles de la imagen original. */
  fontSize?: number
  order?: number
  /** De qué figura, apunte o diapositiva sale el gráfico. */
  fuente?: string
  /** Figura original (src/figuras) sobre la que están los huecos. */
  figura?: string
  /** Cómo se obtuvo el texto de los huecos: leído con OCR y revisado, o transcripto a mano. */
  origen?: 'ocr' | 'manual'
  blanks: Blank[]
}

export interface Diagram {
  id: string
  /** Nombre del archivo sin extensión (se usa para guardar el .json). */
  file: string
  image: string
  title: string
  config: DiagramConfig
  configured: boolean
}

export type Grade = 'ok' | 'close' | 'bad'
