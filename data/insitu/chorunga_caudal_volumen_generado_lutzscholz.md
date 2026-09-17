# Metadata — Caudal y Volumen mensual GENERADO (Modelo Lutz Scholz), Río Chorunga — Cabecera de Riego Valle Chorunga

## I. Información general

- **Archivo de datos**: `chorunga_caudal_volumen_generado_lutzscholz.csv`
- **Ámbito geográfico**: Microcuenca Chorunga (subcuenca/tributario de la cuenca del río Ocoña), punto de interés: Cabecera de Riego del Valle Chorunga.
- **Departamento / Provincia**: Arequipa, provincia de Condesuyos (ámbito PROFODUA ATDR Ocoña-Pausa; el Valle de Chorunga constituye una Junta de Usuarios/valle distinto del Valle de Ocoña, dentro de la misma cuenca hidrográfica).
- **Resolución temporal**: Mensual.
- **Periodo de registro**: 1965-01 a 2002-12 (38 años calendario completos).
- **Convención de año/fecha**: Año calendario Ene-Dic (la columna "AÑO" de la fuente coincide directamente con el año calendario de las 12 columnas de esa fila; misma convención que `ocona_caudal_volumen_generado_lutzscholz.csv`, sin desfase que reconstruir).
- **% de completitud**: 100% (456/456 meses, sin datos faltantes).
- **ADVERTENCIA IMPORTANTE — naturaleza de los datos**: **Esta serie NO es un registro aforado (medido).** Es una serie sintética generada por el modelo hidrológico Lutz Scholz (misma familia de modelo y mismo estudio que `ocona_caudal_volumen_generado_lutzscholz.csv`). No existe, en ninguna de las fuentes revisadas hasta ahora, un registro de aforo real para el río Chorunga.
- **Dataset propio (no fusionado con Ocoña)**: por decisión del usuario (chat, 15-set-2026), esta serie se entrega como dataset independiente, ya que Chorunga es un valle/Junta de Usuarios distinto dentro de la misma cuenca Ocoña, aunque comparta fuente, modelo y periodo con `ocona_caudal_volumen_generado_lutzscholz.csv`.

## II. Fuentes de datos originales

| Fuente | Documento | Entidad / año | Qué aportó específicamente |
|---|---|---|---|
| Fuente A | `Actualización al Guerrazo Estudio hidrológico.xls`, hoja `demanda chorunga`, tabla "DISPONIBILIDAD HIDRICA DE LA CUENCA CHORUNGA — Caudales Medios Mensuales Generados (m3/s) — Río Chorunga (Cabecera Valle Chorunga)", filas 357-394 | ATDR Ocoña-Pausa, s/f (documento de actualización del estudio "Guerrazo") | Serie generada 1965-2002 en el punto Cabecera de Riego del Valle Chorunga. Única fuente de valores usada en este CSV. |
| Fuente B (contexto del modelo) | `Informe_Final_Validado_Ocoña2.doc` (Informe PROFODUA, diciembre 2004), secciones 2.1 y 2.1.1 | ATDR Ocoña-Pausa, diciembre 2004 | Describe el modelo Lutz Scholz aplicado conjuntamente "en las cabeceras de riego de los Valles Ocoña **y Chorunga**" (cita textual en Sección II de `ocona_caudal_volumen_generado_lutzscholz.md`). Confirma que la serie de Chorunga proviene del mismo ejercicio de modelamiento que la de Ocoña. |
| Fuente C (cruce/validación cuantitativa) | `acopio_data_ocoña.xlsx` (tabla compilada por el usuario), hoja `Hoja1`, bloque "Chorunga Cabecera Valle Chorunga", 1965-2002 | Compilación del usuario | Usada solo para validación cruzada; coincidencia exacta con la Fuente A en los valores comparados. |

**Nota sobre localización de la tabla fuente**: esta serie se encontró en la hoja `demanda chorunga` de `Guerrazo.xls` (fila 357 en adelante), la cual, pese a su nombre ("demanda"), contiene tanto tablas de demanda agrícola climatológica (fuera de alcance) como esta tabla de **oferta/disponibilidad generada** (dentro de alcance). Se ubicó mediante búsqueda dirigida por valor numérico (año 1965) en todas las celdas de la hoja, ya que un volcado secuencial inicial de la hoja se truncó antes de llegar a la fila 357.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| Tabla "Caudales Medios Mensuales Generados... (Cabecera Valle Chorunga)" | `caudal_cabeceravallechorunga_m3s` |
| *(no existe en la fuente)* | `volumen_cabeceravallechorunga_mmc` |

---

| Columna | Descripción | Unidad | Fuente | Fórmula |
|---|---|---|---|---|
| `date` | Fecha del mes, día fijado en 01 | YYYY-MM-DD | — | Año calendario tal como aparece directamente en la columna "AÑO" de la fuente (sin desfase) |
| `caudal_cabeceravallechorunga_m3s` | Caudal medio mensual **generado por el modelo Lutz Scholz** en el punto Cabecera de Riego del Valle Chorunga | m³/s | Modelado (Fuente A) | — |
| `volumen_cabeceravallechorunga_mmc` | Volumen mensual correspondiente | MMC | Calculado (en esta estandarización) | `V = Q (m³/s) × (n_días_del_mes × 86,400 s) / 10⁶`, con días reales del mes/año (considera años bisiestos), redondeado a 2 decimales |

## IV. QA/QC

1. **Naturaleza sintética/modelada — sin excepción**: toda la columna de caudal es salida del modelo Lutz Scholz, no un registro aforado. No existe estación de aforo conocida en el río Chorunga entre las fuentes revisadas. Cualquier análisis que requiera un dato "observado" para Chorunga no puede satisfacerse con este dataset.
2. **Validación cruzada exacta contra la fila "MEDIA" de la fuente**: se comparó la media mensual (1965-2002, n=38) de este CSV contra la fila "MEDIA" impresa en `Actualización al Guerrazo...xls` (hoja `demanda chorunga`, fila 397). Coincidencia **exacta** en los 12 meses, por ejemplo: ENE = 3.786 m³/s, FEB = 4.027, MAR = 3.284, ..., DIC = 0.518. Sin discrepancias.
3. **Validación cruzada contra `acopio_data_ocoña.xlsx`**: coincidencia exacta valor a valor con la compilación del usuario para este mismo punto.
4. **Régimen extremadamente estacional / valores mínimos muy bajos**: la serie muestra un régimen de escorrentía muy concentrado en Ene-Mar (medias de 3.3 a 4.0 m³/s) frente a un estiaje muy marcado el resto del año (medias de 0.26 a 0.57 m³/s, con años individuales tan bajos como 0.166-0.2 m³/s). Esto es consistente con una microcuenca pequeña (326.61 km², altitud de cabecera 1,300 m.s.n.m.) de régimen pluvial andino. No se han modificado ni suavizado estos valores; se interpretan como el comportamiento real que el modelo reprodujo para esta subcuenca.
5. **Coeficiente de variación (C.V.) alto en algunos meses** (p. ej. AGO = 1.92, ENE = 1.22, según fila "C.V." de la fuente): refleja la alta variabilidad interanual del estiaje, no un error de cálculo; se reporta como característica de la serie, no como hallazgo de calidad a corregir.
6. **Continuidad temporal**: sin meses faltantes en 1965-01 a 2002-12 (456/456).
7. **Volumen**: siempre calculado (nunca existe en la fuente); fórmula documentada en la Sección III, con manejo explícito de años bisiestos.
8. **Relación con `ocona_caudal_volumen_generado_lutzscholz.csv`**: comparte fuente física (`Guerrazo.xls`), modelo (Lutz Scholz) y periodo (1965-2002) con ese dataset, pero corresponde a una subcuenca y valle de riego distintos (Chorunga, tributario de Ocoña); se mantiene como dataset separado por decisión del usuario, ver Sección I.

## V. Dominio espacial y coordenadas

| Punto | Latitud | Longitud | Altitud | Área colectora | Fuente |
|---|---|---|---|---|---|
| Cabecera de Riego Valle Chorunga | 15° 51' 57.6" S | 72° 57' 42.1" W | 1300 msnm | 326.61 km² (Microcuenca Chorunga hasta esta cabecera) | Informe PROFODUA 2004, Cuadro/Fig. Nº 1.1 |

- **Coordenadas decimales (WGS84)**: -15.8660, -72.9617 *(conversión de 15°51'57.6" y 72°57'42.1")*.
- **Bounding box recomendado para extracción GRACE-FO Mascon** (margen 0.5° sobre el punto; nota: la microcuenca es pequeña, 326.61 km², muy por debajo de la resolución nativa de GRACE/GRACE-FO Mascon — cualquier señal TWS extraída para este bounding box reflejará predominantemente la cuenca Ocoña en su conjunto, no exclusivamente Chorunga):
  - Lat: -16.37° a -15.37°
  - Lon: -73.46° a -72.46°

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Datos extraídos con `xlrd` (lectura directa de celdas, sin OCR) de `Actualización al Guerrazo Estudio hidrológico.xls`, hoja `demanda chorunga`, filas 357-394. Localización de la tabla mediante búsqueda dirigida por valor numérico ante un volcado secuencial inicial truncado (ver Sección II).
- Se generó `volumen_cabeceravallechorunga_mmc` con la fórmula estándar del proyecto, calculada en Python con `calendar.monthrange` para el manejo correcto de años bisiestos.
- **Decisión tomada junto al usuario** (chat, 15-set-2026): construir Chorunga como dataset propio, separado de Ocoña, por tratarse de un valle/Junta de Usuarios distinto dentro de la misma cuenca.
- Se verificó la fidelidad de la extracción comparando la media mensual de la columna contra la fila "MEDIA" impresa en la propia fuente (coincidencia exacta en los 12 valores) y contra la compilación independiente del usuario (`acopio_data_ocoña.xlsx`).
- Nombre de archivo y columna normalizados a la convención `<ambito>_<categoria>_<calificador>.csv` / `<variable>_<punto>_<unidad>`.
