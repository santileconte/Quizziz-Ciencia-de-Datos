# Repaso · Ciencia de Datos

App para repasar el segundo parcial de Ciencia de Datos (Unidades 4, 5 y 6). Mantiene el diseño, las secciones y los
métodos de estudio de la app de repaso original; todo el contenido es de Ciencia de Datos.

```bash
npm install
npm run dev        # abre el sitio en el navegador
npm run build      # genera dist/, que se puede abrir o subir a cualquier hosting estático
```

Necesita Node 18 o más nuevo. El progreso se guarda en el navegador (localStorage, claves `repaso-cd:*`).
Al hacer push a `main`, `.github/workflows/deploy.yml` publica el sitio en GitHub Pages.

> **Derechos de autor.** `src/figuras/img/` y `src/cuestionarios/img/` tienen recortes de los libros de la cátedra.
> Mantené el repositorio **privado**.

## Secciones

1. **Gráficos.** 24 gráficos para completar (176 huecos), redibujados a partir de las figuras de los libros: pipeline de
   ML y de feature engineering, tipos de features, model-centric vs data-centric, niveles de datos, pipeline de NLP,
   cross validation, ciclo de vida de Reis, arquitectura empresarial, Lambda y Kappa, Data Mesh, Medallion, componentes de
   un agente, pipelines de RAG, tríada de evaluación y más. Cada uno dice en qué libro, figura y página se basa (`fuente`).
   - **Estudio**, **Práctica** (corrección al instante, segunda oportunidad, pistas) y **Simulacro** (sin ayudas).
   - Filtros **Clave**, **Todo** y **Mis errores**. Un concepto queda dominado al acertarlo 2 veces seguidas.
   - **Practicar en serie:** una unidad entera o todo junto.
2. **Cuestionarios.** Por fuente, unidad, tema y formato, en modo práctica o simulacro.
   - **De la cátedra, literales:** el segundo parcial 2025 y las preguntas del 1er parcial que ahora entran. Se copiaron
     como están, incluidos sus errores.
   - **Nuevas de este repaso:** 70 preguntas escritas a partir de los libros, con etiqueta y color propios. Cada una cita
     libro, capítulo y página.
   - Las preguntas con **clave sin verificar** se pueden responder, pero no suman puntaje ni progreso. Hoy son todas las
     de la cátedra, porque el documento no trae respuestas.
3. **Crucigramas.** Uno por mapa mental (16).
4. **Mapas mentales.** 16 mapas. Al tocar un concepto se abre su explicación en el apunte de estudio, con el libro y la
   página de donde sale.
5. **Temario.** Los temas por unidad, con prioridad, bibliografía, notas de clase, libro y páginas, evidencia en las
   consignas reales y pendientes de verificación. Los temas sin material en las carpetas van aparte.
6. **Figuras originales** (`#/figuras`). 63 figuras recortadas de los libros, separadas por tema (`#/figuras/15`, por
   ejemplo), con libro, número de figura y página. El proceso de extracción está en `tools/figuras/`.

## Dónde está el contenido

| Qué | Dónde |
| --- | --- |
| Temas, prioridades y fuentes | `src/temario.ts` |
| Segundo parcial 2025 (literal) | `src/cuestionarios/parcial-2025.ts` |
| Preguntas del 1er parcial que entran ahora (literal) | `src/cuestionarios/primer-parcial.ts` |
| Preguntas nuevas | `src/cuestionarios/propias.ts` |
| Figuras de las preguntas | `src/cuestionarios/img/` |
| Claves confirmadas | `src/cuestionarios/verificadas.ts` |
| Apunte de estudio y mapas | `tools/contenido_apunte.py`, `tools/contenido_mapas.py` → `python3 tools/build_apunte.py` |
| Gráficos | `tools/graficos.py` → `python3 tools/graficos.py` (necesita Pillow) |
| Figuras originales | `tools/figuras/build_figuras.py` → `src/figuras/` (necesita PyMuPDF y los PDF) |
| Crucigramas | `src/crucigramas/datos.ts` |

## Verificar una clave en duda

1. Abrí **Temario → Pendientes de verificación** y anotá el id de la pregunta (por ejemplo `pc25-03`).
2. Confirmá la clave contra el libro o con la cátedra. Si la propuesta estaba mal, corregí el campo `a` en el archivo de
   la pregunta.
3. Agregá el id en `verificadas` (`src/cuestionarios/verificadas.ts`) con quién y cómo la confirmó. Desde ese momento se
   corrige sola, suma puntaje y la nota aparece al corregir.

## Editar los huecos de un gráfico

Con `npm run dev`, abrí el gráfico y entrá a **Editar huecos**. Arrastrás sobre el texto, escribís la respuesta y
**Guardar** escribe el `.json` en `src/graficos/`. Una imagen nueva en `src/graficos/` aparece sola; sus huecos van en un
`.json` con el mismo nombre.
