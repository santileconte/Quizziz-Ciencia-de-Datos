export interface Caso {
  titulo: string
  texto: string
}

// Textos que acompañan a un enunciado. Se muestran arriba de la pregunta.
// El parcial 2025 de Ciencia de Datos no trae casos de estudio: queda vacío.
export const casos: Record<string, Caso> = {}
