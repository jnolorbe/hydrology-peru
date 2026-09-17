# Metadata — Precipitación Areal mensual, Cuenca del río Ocoña (completa)

## I. Información general

- **Archivo de datos**: `ocona_precipitacion_areal.csv`
- **Ámbito geográfico**: Cuenca completa del río Ocoña (16,015.61 km² hasta su desembocadura en el Océano Pacífico) — valor areal único por mes, **no** desagregado por subcuenca ni por estación.
- **Departamento / Provincia**: Arequipa y Ayacucho (cuenca del río Ocoña, ATDR Ocoña-Pausa).
- **Resolución temporal**: Mensual.
- **Periodo de registro**: 1965-09 a 2006-08 (41 años hidrológicos: 1965-66 a 2005-06).
- **Desfase respecto al año calendario**: La fuente presenta la serie en **año hidrológico Setiembre–Agosto** (misma convención que `ocona_caudal_volumen.csv`; p. ej. "Sep" del año hidrológico 1965-66 → `1965-09-01`, "Ene" del mismo año hidrológico → `1966-01-01`).
- **% de completitud**: 100% (492/492 meses, sin datos faltantes).
- **Naturaleza del dato**: es una precipitación **areal calculada** (no el registro directo de ninguna estación puntual) — resultado de interpolar espacialmente los registros de 16 estaciones pluviométricas de la red del estudio (Cuadro 3.1) mediante el método de isoyetas/Kriging y promediar ponderando por área sobre el polígono de toda la cuenca. Ver Sección II para el método exacto.

## II. Fuentes de datos originales

| Fuente | Documento | Entidad / año | Qué aportó específicamente |
|---|---|---|---|
| Fuente única | `ESTUDIO_HIDROLOGICO_OCON_A.pdf` ("Evaluación de los Recursos Hídricos de la Cuenca del Río Ocoña" — Estudio Hidrológico), Cuadro 3.8 "Precipitación total mensual de la cuenca del río Ocoña, periodo 1965-2005", pág. 96 (numeración impresa) | INRENA — Intendencia de Recursos Hídricos — ATDR Ocoña-Pausa, enero 2007 | Única tabla de precipitación de todas las fuentes revisadas hasta ahora que es una **serie mensual año-por-año realmente utilizable** (las demás tablas de precipitación encontradas son climatologías o series anuales; ver Sección IV.1 y el inventario reportado al usuario antes de construir este dataset). |

**Método de cálculo declarado por la fuente** (sección 3.4.3 del PDF): la precipitación media mensual sobre la cuenca se calculó mediante isoyetas trazadas por interpolación Kriging (software Surfer 7.0), con correcciones manuales al trazo automático, y luego ponderada por área entre isoyetas consecutivas (fórmula `Pmed_j = Σ(Ai·Pi)/A`, con `Pi` el promedio de alturas entre isoyetas consecutivas). Es decir, **no es un promedio aritmético simple de estaciones**, sino un valor espacialmente ponderado.

**Limitación importante de la fuente, reportada al usuario antes de construir este dataset**: el texto del PDF (pág. 74 e ítem 3.4.3) indica explícitamente que "las series históricas de precipitación mensual por estaciones podemos observarlas en el **Anexo I**" y que "los valores de precipitación anual y mensual completas se presentan en el **Anexo II**" — es decir, el propio estudio afirma tener series reales **por estación** (no solo el areal agregado). **Sin embargo, el archivo PDF entregado (152 páginas) termina en la Bibliografía (pág. 151) y no incluye ningún Anexo I-IX** (tampoco Anexo III de temperatura, ni V-IX). Por lo tanto, **no fue posible extraer las series por estación**; solo se pudo construir el dataset agregado a nivel de cuenca completa (Cuadro 3.8, que sí está en el cuerpo del informe). Si el usuario cuenta con una versión completa del informe que incluya los anexos, se podría ampliar este inventario con series por estación.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| Cuadro 3.8, valor mensual de la fila "Año" correspondiente | `precipitacion_cuencaocona_mm` |

---

| Columna | Descripción | Unidad | Fuente | Fórmula |
|---|---|---|---|---|
| `date` | Fecha del mes, día fijado en 01 | YYYY-MM-DD | — | Reconstruida desde el año hidrológico Sep-Ago declarado en la fuente |
| `precipitacion_cuencaocona_mm` | Precipitación areal media mensual sobre toda la cuenca del río Ocoña | mm | Calculada por la fuente (isoyetas/Kriging ponderado por área, ver Sección II) | — (no se recalculó; se transcribió el valor de la fuente) |

## IV. QA/QC

1. **Clasificación previa de las fuentes de precipitación disponibles (reportada al usuario antes de construir cualquier dataset)**: se inventariaron 4 tablas de precipitación entre las 2 fuentes originales (informe PROFODUA 2004 y estudio hidrológico PDF 2007):
   - Cuadro 3.8 (PDF 2007) — **usada en este dataset**: serie mensual año-por-año real, 1965-2005, agregada a nivel de cuenca completa.
   - Cuadro 3.6 (PDF 2007) — "Precipitación total anual para el periodo 1965-2005": serie año-por-año real, pero de **resolución anual** (no mensual), calculada con 4 métodos de interpolación en paralelo (Media Aritmética, Thiessen, 1/Distancia², Kriging). No incorporada en este dataset por ser de otra resolución temporal; queda como candidata a un dataset complementario, pendiente de decisión del usuario.
   - Cuadro 3.7 (PDF 2007) — "Precipitación total mensual para el año promedio": **climatología** (una sola fila por subcuenca: Parinacochas, Pausa, Cotahuasi, Arma, Ocoña, más el total de cuenca), no serie temporal fechada. No incorporada aquí.
   - Tabla de 13 estaciones (informe 2004, `Anexos.doc` → hoja embebida `oleObject1.xlsx`, Hoja1): **climatología** (una fila por estación: Incuyo, Pausa, Tomepampa, Ocoña, Urayhuma, Lampa, Salamanca, Chinchayllapa, Chaviña, Carhuanillas, Urasqui, Yanaquihua, Lucanas), no serie temporal fechada. No incorporada aquí.
   
   El usuario decidió (chat, 15/16-set-2026) construir primero el Cuadro 3.8 por ser la única serie mensual año-por-año genuina.
2. **Validación cruzada exacta contra las filas estadísticas impresas en la fuente**: se comparó la media mensual (1965-2005, n=41) de este CSV contra la fila "μ" impresa en el Cuadro 3.8. Coincidencia exacta o dentro de error de redondeo de imprenta (±0.1 mm) en los 12 meses — p. ej. ENE: 83.77 (calculado) vs. 83.8 (impreso); FEB: 94.30 vs. 94.3; DIC: 33.01 vs. 33.0. La única diferencia levemente mayor al redondeo es NOV (10.14 calculado vs. 10.2 impreso, diff. 0.06 mm), consistente con acumulación de redondeo de los valores mensuales a 1 decimal en la fuente, no con un error de transcripción.
3. **Extracción con texto vectorial real del PDF**: los valores se extrajeron con `pdftotext -layout` (texto real embebido en el PDF, no OCR ni lectura visual de imagen), lo que permite alta confianza en la fidelidad dígito a dígito frente a la fuente.
4. **No se aplicó ninguna corrección ni relleno**: se transcribieron los 492 valores tal como aparecen impresos, sin interpolar meses ni ajustar outliers.
5. **Extremos de la serie**: el máximo de toda la serie ocurre en el mes de Feb-1973 (hidrológico 1972) = 150.3 mm, coincidente con el evento El Niño 1972-73 documentado en la costa peruana (mismo evento que produce el pico de caudal en `ocona_caudal_volumen.csv`); el mínimo ocurre en el año hidrológico 1992 (El Niño/anomalía seca, mínimos de todos los meses según fila "min" de la fuente). Se interpretan como extremos hidrológicos reales, no como errores.
6. **Consistencia con el dataset de caudal del mismo punto/cuenca**: este dataset comparte exactamente el mismo rango temporal (1965-09 a 2006-08, 492 meses) y la misma convención de año hidrológico que `ocona_caudal_volumen.csv`, lo que facilita el análisis conjunto precipitación-caudal (p. ej. verificar que los picos de precipitación de Feb-1973 y Feb-1999 anteceden o coinciden con los picos de caudal en Puente Ocoña reportados en ese dataset).
7. **Limitación de resolución espacial**: al ser un valor único por mes para toda la cuenca (16,015.61 km²), este dataset **no permite distinguir** la precipitación de la cuenca húmeda alta (~12,171.86 km², >2,000 msnm, que genera la mayor parte de la escorrentía) de la cuenca seca baja/costera. Si se requiere ese detalle, sería necesario el Cuadro 3.7 (climatología por subcuenca) o las series por estación del Anexo I/II, no disponibles en este PDF (ver Sección II).
8. **Pendiente de decisión del usuario**: no se ha decidido aún si construir también el Cuadro 3.6 (anual, 4 métodos), el Cuadro 3.7 (climatología por subcuenca) y/o la tabla de 13 estaciones del informe 2004 (climatología). Se reportan como pendientes, no resueltos unilateralmente.

## V. Dominio espacial y coordenadas

Este dataset es un valor **agregado espacialmente sobre toda la cuenca**, no de una estación puntual. Como referencia geográfica de la cuenca completa (informe PROFODUA 2004, sección 1):

- **Extensión de la cuenca (Informe 2004)**: "Geográficamente se ubica entre el Meridiano 72º20' y 74º00' de Longitud Oeste, y entre el Paralelo 14º15' y 16º30' de Latitud Sur."
- **Área total de la cuenca**: 16,015.61 km² (hasta la desembocadura en el Océano Pacífico).
- Ver `ESTUDIO_HIDROLOGICO_OCON_A.pdf`, Cuadro 3.1 (Sección II de este documento) para la red de 16 estaciones pluviométricas usada como insumo del cálculo de isoyetas (no se reproducen aquí sus coordenadas individuales, ya que el dato de este CSV es el agregado de cuenca, no por estación).
- **Bounding box recomendado para extracción GRACE-FO Mascon** (cuenca completa, sin margen adicional ya que el rango ya cubre holgadamente la cuenca):
  - Lat: -16.50° a -14.25°
  - Lon: -74.00° a -72.33°

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Datos numéricos extraídos con `pdftotext -layout` (texto vectorial real del PDF, no OCR) de la página que contiene el Cuadro 3.8 (pág. 96 impresa) de `ESTUDIO_HIDROLOGICO_OCON_A.pdf`.
- Antes de construir este dataset, se inventariaron y reportaron al usuario las 4 tablas de precipitación encontradas en las 2 fuentes disponibles, clasificándolas en "serie mensual utilizable" (Cuadro 3.8, esta), "serie anual utilizable" (Cuadro 3.6, no construida aún) y "climatología/año promedio" (Cuadro 3.7 y tabla de 13 estaciones del informe 2004, no construidas aún), conforme a la regla del proyecto de inventariar antes de generar.
- **Decisión tomada junto al usuario** (chat, 15/16-set-2026): construir primero el Cuadro 3.8 (única serie mensual año-por-año real), dejando pendientes el resto de los datasets de precipitación para una decisión posterior sobre orden y alcance.
- Se detectó y reportó que los Anexos I y II del PDF (que según el propio texto contendrían series reales por estación) no están incluidos en el archivo PDF entregado.
- Nombre de archivo y columna normalizados a la convención `<ambito>_<categoria>_<calificador>.csv` / `<variable>_<ambito>_<unidad>`.
