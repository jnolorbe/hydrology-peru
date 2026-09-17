# Metadata — Metadata — Caudal y Volumen, Estación Yonan (Río Jequetepeque)

## I. Información general

- **Archivo:** `caudal_volumen_yonan_jequetepeque.csv`
- **Ámbito geográfico:** Cuenca del río Jequetepeque, estación hidrométrica Yonan (también referida en las fuentes como "Ventanillas - Yonan - Pampalarga").
- **Departamento / Región:** Cajamarca (cuenca alta y media) — la estación de aforo se ubica en el tramo bajo/medio del río Jequetepeque, cerca de la localidad de Yonán, provincia de Contumazá, Cajamarca.
- **Resolución temporal:** Mensual.
- **Periodo de registro:** 1964-08-01 a 2003-07-01 (39 años hidrológicos completos, agosto 1964/65 a julio 2002/03).
- **Desfase respecto al año calendario:** La fuente original organiza los datos por **año hidrológico** (agosto–julio). Se reconstruyó la fecha calendario real de cada mes (`date`, día=01) para cada valor, sin alterar la asociación mes–valor de la fuente.
- **% de completitud:** 100% (468/468 meses, sin vacíos) para ambas columnas.

## II. Fuentes de datos originales

| Fuente | Documento / hoja | Entidad emisora (según metadatos del archivo) | Qué aportó |
|---|---|---|---|
| 1 | `Caudales_Yonan_64-2003.xls`, hoja `Consistencia` (Cuadro N° 5.2: "Análisis de Consistencia de Caudales") | Elaboración propia (PROFODUA-Jequetepeque, según metadatos del archivo) | Caudal medio mensual (m³/s), 39 años, ya sometido a análisis de consistencia/homogeneidad por la fuente. |
| 2 | `Caudales_Yonan_64-2003.xls`, hoja `V mmc` | Elaboración propia (PROFODUA-Jequetepeque) | Volumen mensual (MMC) ya calculado por la fuente para el mismo periodo — usado únicamente para **contraste QA/QC**, no como base del dataset. |
| 3 | `Informe_Final_Asignacion_Alto_Jequetepequef.doc` (2007) | Grupo de Trabajo–Diagnóstico / PROFODUA / INRENA-IRH | Contexto metodológico: confirma que la serie de 39 años (ago.1964–jul.2003) fue homogeneizada y consistenciada, y que no se hallaron saltos ni tendencias significativas en media/desviación estándar (Cuadro N° 2.2 del informe) — no fue necesario corregir la serie.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `caudal_yonan_m3s` | `caudal_yonan_m3s` |
| `volumen_yonan_mmc` | `volumen_yonan_mmc` |

---

| Columna | Descripción | Unidad | Fuente | Fórmula |
|---|---|---|---|---|
| `date` | Primer día del mes calendario correspondiente | YYYY-MM-DD | Calculado a partir del año hidrológico de la fuente | — |
| `caudal_yonan_m3s` | Caudal medio mensual en la estación Yonan | m³/s | Medido/reportado por la fuente (hoja `Consistencia`) | — |
| `volumen_yonan_mmc` | Volumen mensual | MMC (millones de m³) | Calculado | `V = Q × (n_días_del_mes × 86 400) / 10⁶`, usando el número real de días de cada mes/año (considera años bisiestos), redondeado a 2 decimales |

## IV. QA/QC

- **Valores negativos:** 0 encontrados en caudal ni en volumen.
- **Continuidad temporal:** sin meses faltantes en el rango 1964-08 a 2003-07.
- **Atípicos (IQR por mes calendario, no global):** se detectaron 18 valores atípicos altos, concentrados en enero–mayo de 1983, 1984, 1993, 1994, 1997–2001. Estos coinciden con los años de Fenómeno de El Niño mencionados explícitamente en el informe técnico ("el histograma de caudales mensuales permite apreciar algunos valores puntuales altos que coinciden con los eventos ocurridos durante los períodos del Fenómeno de El Niño"). **Interpretación: extremos hidrológicos reales, no errores de dato.** El caudal máximo mensual del registro corresponde a marzo de 1998 (321.45 m³/s), consistente con el volumen anual máximo de la campaña 1997-98 (2,676.60 MMC) reportado en el informe.
- **Consistencia caudal ↔ volumen:** se comparó el volumen calculado (`V = Q×días×86400/1e6`) contra el volumen ya reportado por la fuente en la hoja `V mmc`. La diferencia media es 0.09 MMC/mes. Las diferencias mayores (hasta 16.26 MMC) ocurren **exclusivamente en febrero de años bisiestos** (1972, 1976, 1984, 1988, 1996, 2000): la fuente original calculó el volumen de febrero asumiendo siempre 28 días, mientras que este dataset usa el número real de días de cada año (29 en bisiestos), conforme a la regla de construcción del proyecto. **No se trata de un error, sino de una diferencia metodológica documentada.**
- **Valores "corregidos"/"completados" en la fuente:** el informe técnico indica explícitamente que, tras la prueba de la media y desviación estándar (Cuadro N° 2.2), *"no se ha encontrado saltos ni tendencias en la media ni desviación estándar por lo que no fue necesario corregir la información correspondiente"*. Es decir, la serie de Yonán se usa tal como fue aforada/consistenciada, sin marcas de valores estimados o rellenados.
- **Limitaciones conocidas:**
  - Las coordenadas de la estación presentan una **discrepancia entre fuentes** (ver sección V) que no se resolvió arbitrariamente.
  - No se dispone de la serie diaria, solo mensual.
  - El informe indica una segunda estación de control (San Miguel, aguas arriba, operada por SENAMHI) que "se encuentra inoperativa por deterioros sufridos en las avenidas de Marzo de 2001"; no se recibieron datos numéricos de esa estación, por lo que no se incluye en este dataset.

## V. Dominio espacial y coordenadas

**Discrepancia de coordenadas entre fuentes — se reportan todas, sin promediar:**

| Fuente | Latitud | Longitud | Altitud |
|---|---|---|---|
| `Caudales_Yonan_64-2003.xls`, hoja `Consistencia` | 0° 00' S | 0° 10' W | 420 msnm |
| Informe Word (texto, ítem 1.4.6.1, estación de referencia Yonán / Ventanillas) | 7° 15' S | 79° 06' W | ~600 msnm (aguas arriba de la Presa Gallito Ciego) |
| `ESTACIONES.xls` (estación Montegrande, mismo distrito de Yonán, cuenca Jequetepeque) | 07° 12' S | 79° 19' W | 420 msnm |

La coordenada "0°00'S, 0°10'W" del archivo de caudales es evidentemente un valor placeholder/erróneo (posición nula del globo terráqueo). Las coordenadas del informe (7°15'S, 79°06'W) y de Montegrande (7°12'S, 79°19'W) son cercanas pero no idénticas — es razonable que correspondan a puntos distintos (estación de aforo Yonán vs. estación climatológica Montegrande, ambas en el mismo distrito), pero **no se asume equivalencia sin confirmación**.

- **Bounding box recomendado para extracción GRACE-FO Mascon** (usando las coordenadas del informe técnico, con margen de 0.5° sobre la estación, y hasta que el usuario confirme la coordenada correcta a usar):
  - Latitud: **6.75° S a 7.75° S**
  - Longitud: **78.60° W a 79.60° W**
  - *(Recomendado ampliar este cuadro para cubrir toda la cuenca alta/media del Jequetepeque — ver bounding box conjunto en el archivo de metadata de precipitación, que cubre las 13 estaciones pluviométricas de la cuenca.)*

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `jequetepeque_caudales.csv` a `jequetepeque_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `jequetepeque_caudales_metadata.md` a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
