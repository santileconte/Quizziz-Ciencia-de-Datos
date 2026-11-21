/**
 * Estado de verificación de las claves.
 *
 * Mientras una pregunta tenga el campo `dud`, se puede responder y ver la clave propuesta, pero no suma al puntaje
 * ni al progreso. Cuando se confirma la clave, su id va en `verificadas` con quién y cómo la confirmó: pasa a
 * corregirse sola y en la corrección se muestra esa nota. Si la clave propuesta estaba mal, corregí además el campo
 * `a` (o la respuesta modelo `m`) en el archivo de la pregunta.
 *
 * Los ids se ven en la pantalla «Temario». Ejemplo:
 *   'pc25-01': 'Confirmada por Santiago el 22/11/2026 con la revisión del parcial.',
 */
export const verificadas: Record<string, string> = {}

/**
 * Preguntas cuya clave contradice a otra versión de mayor jerarquía. Por ahora no hay ninguna.
 * Jerarquía: parcial real > pregunta de la cátedra de otra instancia > práctica.
 */
export const reemplazadas: Record<string, { por: string; motivo: string }> = {}
