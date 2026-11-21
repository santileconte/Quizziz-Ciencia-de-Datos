# Huecos de los gráficos

Los gráficos de `src/graficos/` son las figuras originales de los libros, recortadas del PDF a 400 dpi y reducidas a
1600 px de ancho. Cada hueco tapa un texto de la figura; la respuesta es ese texto copiado tal cual.

Orden de los scripts (se corren dentro de una carpeta de trabajo, con los PDF en `/mnt/user-data/uploads/2do Ciencia/`):

1. `ocr.py` recorta cada figura (usa `locate.py` y `tools/figuras/objetivos.json`) y guarda `hi/<figura>.png`.
2. `ocr2.py` lee el texto con Tesseract (solo como ayuda para ubicar los textos).
3. `prep.py` detecta las zonas con texto (`regions.py`) y arma hojas numeradas para revisar.
4. `trans.py` es la transcripción hecha a mano mirando cada figura: zona → texto exacto. El OCR no se usa como respuesta.
5. `build.py` genera `out/<id>.webp` y `out/<id>.json`; `verify.py` arma hojas que muestran cada recorte al lado de su
   respuesta para cotejarlas una por una.
