# Metadata — Metadata — Precipitación Mensual, Cuenca Jequetepeque (13 estaciones)

## I. Información general

- **Archivo:** `precipitacion_estaciones_jequetepeque.csv`
- **Ámbito geográfico:** Cuenca del río Jequetepeque (parte alta y media), departamentos de Cajamarca y La Libertad, Perú.
- **Departamento / Región:** 12 estaciones en Cajamarca (provincias San Miguel, Cajamarca, Contumazá) y 1 estación (Talla) en La Libertad (provincia Pacasmayo).
- **Resolución temporal:** Mensual, año calendario (Ene–Dic).
- **Periodo de registro:** 1958-01-01 a 2005-12-01 (576 meses). La mayoría de estaciones inicia en 1964; Huacraruro tiene registro desde 1958.
- **Desfase respecto al año calendario:** Ninguno — la fuente ya está en año calendario.
- **% de completitud:** variable por estación, entre 12.5% y 79.3% de datos faltantes (ver tabla en sección IV). **Esta es la serie observada/cruda (no rellenada)**, por decisión explícita del usuario — existe una versión alterna "completada" (ver sección II) que no se usó aquí.

## II. Fuentes de datos originales

| Fuente | Documento / hoja | Entidad emisora | Qué aportó |
|---|---|---|---|
| 1 | `precipitacion_completada_y_preparada_GIS.xls`, hoja **"precipitacion completada y prep"** | Elaboración propia / SENAMHI (según informe técnico asociado) | **Serie mensual observada cruda**, con vacíos reales (NaN) — es la base de este dataset. |
| 2 | `precipitacion_completada_y_preparada_GIS.xls`, hoja "PP completada" (**no usada** en este dataset) | Elaboración propia, aplicando software HEC-4 | Versión de la misma serie con vacíos rellenados estadísticamente. Disponible para una entrega alterna si se solicita. |
| 3 | `precipitacion_completada_y_preparada_GIS.xls`, hoja "Doble masa" | Elaboración propia | Totales anuales por estación para análisis de consistencia por doble masa — usado como insumo de contexto en QA/QC, no como dato de la serie. |
| 4 | `ESTACIONES.xls`, hoja "Hoja1" | PROFODUA (según metadatos del archivo) | Coordenadas geográficas (grados-minutos, aparentemente WGS84), distrito/provincia/departamento y altitud de cada estación. |
| 5 | `ESTACIONES.xls`, hoja "Hoja2" | PROFODUA | Coordenadas UTM (Norte/Este) de cada estación — **no se especifica en el archivo la zona UTM ni el datum**. |
| 6 | `Informe_Final_Asignacion_Alto_Jequetepequef.doc` (2007) | Grupo de Trabajo–Diagnóstico / PROFODUA | Confirma que la precipitación se usó "completada y corregida para el período 1964-2005... completadas con información de SENAMHI" y que la extensión estadística se hizo con software HEC-4 (Cuadro N° 1.3 del informe). Confirma también el orden de magnitud de precipitación anual por estación, coherente con lo extraído. |

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `precipitacion_asuncion_mm` | `precipitacion_asuncion_mm` |
| `precipitacion_chilete_mm` | `precipitacion_chilete_mm` |
| `precipitacion_contumaza_mm` | `precipitacion_contumaza_mm` |
| `precipitacion_granjaporcon_mm` | `precipitacion_granjaporcon_mm` |
| `precipitacion_huacraruro_mm` | `precipitacion_huacraruro_mm` |
| `precipitacion_livis_mm` | `precipitacion_livis_mm` |
| `precipitacion_llapa_mm` | `precipitacion_llapa_mm` |
| `precipitacion_magdalena_mm` | `precipitacion_magdalena_mm` |
| `precipitacion_montegrande_mm` | `precipitacion_montegrande_mm` |
| `precipitacion_quebradahonda_mm` | `precipitacion_quebradahonda_mm` |
| `precipitacion_quilcate_mm` | `precipitacion_quilcate_mm` |
| `precipitacion_sanjuan_mm` | `precipitacion_sanjuan_mm` |
| `precipitacion_talla_mm` | `precipitacion_talla_mm` |

---

| Columna | Descripción | Unidad | Fuente | Fórmula |
|---|---|---|---|---|
| `date` | Primer día del mes calendario | YYYY-MM-DD | — | — |
| `precipitacion_quebradahonda_mm` | Precipitación mensual, estación Quebrada Honda | mm | Medido (SENAMHI) | — |
| `precipitacion_quilcate_mm` | Precipitación mensual, estación Quilcate | mm | Medido | — |
| `precipitacion_granjaporcon_mm` | Precipitación mensual, estación Granja Porcón | mm | Medido | — |
| `precipitacion_llapa_mm` | Precipitación mensual, estación Llapa | mm | Medido | — |
| `precipitacion_livis_mm` | Precipitación mensual, estación Livis (fuente también la nombra "Lives") | mm | Medido | — |
| `precipitacion_asuncion_mm` | Precipitación mensual, estación Asunción | mm | Medido | — |
| `precipitacion_sanjuan_mm` | Precipitación mensual, estación San Juan | mm | Medido | — |
| `precipitacion_magdalena_mm` | Precipitación mensual, estación Magdalena | mm | Medido | — |
| `precipitacion_contumaza_mm` | Precipitación mensual, estación Contumazá | mm | Medido | — |
| `precipitacion_chilete_mm` | Precipitación mensual, estación Chilete | mm | Medido | — |
| `precipitacion_huacraruro_mm` | Precipitación mensual, estación Huacraruro | mm | Medido | — |
| `precipitacion_montegrande_mm` | Precipitación mensual, estación Montegrande | mm | Medido | — |
| `precipitacion_talla_mm` | Precipitación mensual, estación Talla | mm | Medido | — |

*No se generó columna `precipitacion_areal` (promedio de área) en esta entrega — no se recibió una delimitación de área de influencia (polígonos Thiessen u otra) para las 13 estaciones. Puede calcularse en una iteración posterior si se define el método y las áreas de influencia.*

## IV. QA/QC

**% de datos faltantes por estación (sobre 576 meses, 1958-01 a 2005-12):**

| Estación | % faltante |
|---|---|
| Montegrande | 79.3% |
| Huacraruro | 59.4% |
| Asunción | 57.1% |
| Granja Porcón | 38.7% |
| Quilcate | 32.8% |
| Quebrada Honda | 32.6% |
| Talla | 25.4% |
| Chilete | 24.7% |
| Magdalena | 21.9% |
| Contumazá | 21.0% |
| San Juan | 15.5% |
| Llapa | 12.9% |
| Livis | 12.5% |

Los porcentajes altos (Montegrande, Huacraruro, Asunción) se deben en parte a que estas estaciones no tienen registro en varios años completos (p. ej. Montegrande carece de datos 1964-1990 casi en su totalidad; Huacraruro solo tiene datos hasta 1998; Asunción tiene años enteros vacíos entre 1982-1997).

- **Transformaciones aplicadas:**
  - Se excluyeron/marcaron como `NA` los valores registrados en la fuente como **"S/D"** (sin dato, 1 ocurrencia — Contumazá, marzo 2005) y **"T"** (traza, 8 ocurrencias en distintas estaciones/meses). La traza ("T") es una convención meteorológica que indica precipitación no cuantificable (por debajo del umbral de medición del pluviómetro), no un valor nulo real; se marcó como `NA` en vez de asignarle arbitrariamente 0.0 o 0.1 mm, siguiendo la regla del proyecto de no inventar valores. **Se recomienda que el usuario decida el tratamiento de "traza" si se requiere una serie sin vacíos** (alternativas típicas: 0.0 mm o 0.1 mm).
- **Valores negativos:** 0 encontrados (no aplica físicamente para precipitación).
- **Atípicos (IQR por mes calendario):** se detectaron entre 9 y 55 valores atípicos por estación (mayor incidencia en Talla, Contumazá y Magdalena). Dado el fuerte régimen estacional de la cuenca (lluvias intensas nov–abr, prácticamente nulas may–oct, según el informe técnico), varios de estos atípicos son consistentes con eventos El Niño (1983, 1998) mencionados en el informe y **no se han reinterpretado individualmente como errores** — se entregan como alerta para revisión manual si se desea.
- **Continuidad temporal:** 0 meses faltantes en el rango total 1958-01 a 2005-12 (cada mes existe como fila, aunque con `NA` en la mayoría de estaciones para los años sin registro).
- **Valores "corregidos"/"completados" en la fuente:** **no aplica a este archivo**, porque se usó deliberadamente la hoja de datos crudos/observados, no la hoja "PP completada" (que sí contiene valores estimados vía HEC-4). Si en el futuro se solicita la versión completada, debe documentarse fila por fila cuáles meses fueron estimados vs. medidos, ya que la hoja "PP completada" no distingue explícitamente unos de otros en su estructura actual.
- **Limitaciones conocidas:**
  - Nombre de estación "Livis" en el archivo de coordenadas (`ESTACIONES.xls`) vs. "Lives" en la hoja de datos de precipitación — mismo sitio, columna nombrada `precipitacion_livis_mm` (se usó la grafía de `ESTACIONES.xls`).
  - No se recibió información de polígonos de área de influencia por estación, por lo que no se calculó `precipitacion_areal`.
  - Las estaciones cubren predominantemente la cuenca alta y media; no hay estaciones pluviométricas de la cuenca baja (donde se ubica el embalse Gallito Ciego) en este archivo.

## V. Dominio espacial y coordenadas

**Coordenadas en grados-minutos (WGS84 aparente, sin segundos ni datum explícito) — `ESTACIONES.xls`, Hoja1:**

| Estación | Distrito | Provincia | Depto. | Latitud | Longitud | Altitud (msnm) |
|---|---|---|---|---|---|---|
| Quebrada Onda | Llapa | San Miguel | Cajamarca | 06° 54' S | 78° 44' W | 3550 |
| Quilcate | Llapa | San Miguel | Cajamarca | 06° 50' S | 78° 46' W | 3100 |
| Granja Porcón | Cajamarca | Cajamarca | Cajamarca | 07° 02' S | 78° 38' W | 3000 |
| Llapa | Llapa | San Miguel | Cajamarca | 06° 59' S | 78° 49' W | 2798 |
| Livis | Agua Blanca | San Miguel | Cajamarca | 07° 05' S | 78° 02' W | 2000 |
| Asunción | Asunción | Cajamarca | Cajamarca | 07° 19' S | 78° 31' W | 2085 |
| San Juan | San Juan | Cajamarca | Cajamarca | 07° 17' S | 78° 30' W | 2224 |
| Magdalena | Magdalena | Cajamarca | Cajamarca | 07° 16' S | 78° 41' W | 1300 |
| Contumazá | Contumazá | Contumazá | Cajamarca | 07° 22' S | 78° 49' W | 2330 |
| Chilete | Chilete | Contumazá | Cajamarca | 07° 13' S | 78° 51' W | 850 |
| Huacraruro | San Juan | Cajamarca | Cajamarca | 07° 18' S | 78° 26' W | 2800 |
| Montegrande | Yonán | Cajamarca | Cajamarca | 07° 12' S | 79° 19' W | 420 |
| Talla | Guadalupe | Pacasmayo | La Libertad | 07° 16' S | 79° 25' W | 90 |

**Coordenadas UTM alternativas (Norte, Este) — `ESTACIONES.xls`, Hoja2 — zona/datum no especificados en el archivo, se reportan sin conversión ni verificación:**

| Estación | Norte (UTM) | Este (UTM) |
|---|---|---|
| Quebrada Onda | 9,236,701.847 | 750,497.878 |
| Quilcate | 9,244,094.534 | 746,846.213 |
| Granja Porcón | 9,221,896.127 | 761,482.725 |
| Llapa | 9,227,526.018 | 741,240.373 |
| Livis | 9,215,983.134 | 827,803.440 |
| Asunción | 9,190,478.418 | 771,212.320 |
| San Juan | 9,194,156.608 | 776,074.558 |
| Magdalena | 9,196,108.563 | 755,824.669 |
| Contumazá | 9,185,119.012 | 741,038.313 |
| Chilete | 9,201,730.633 | 737,435.350 |
| Huacraruro | 9,192,271.924 | 783,431.924 |
| Montegrande | 9,203,790.603 | 685,885.352 |
| Talla | 9,196,457.404 | 674,813.478 |

**Nota de discrepancia:** las coordenadas UTM de Montegrande (Este 685,885) y Talla (Este 674,813) son notoriamente inconsistentes con las de las demás estaciones (Este entre 737,000 y 828,000) para estar en la misma cuenca — posible error de digitación, zona UTM distinta, o falla en la fuente. **Se reporta tal cual, sin corregir.**

- **Bounding box recomendado para extracción GRACE-FO Mascon** (a partir de las coordenadas grados-minutos, con margen de 0.5° sobre el conjunto de 13 estaciones):
  - Latitud: **6.33° S a 7.87° S** (de 06°50' a 07°22', +0.5°)
  - Longitud: **78.03° W a 79.92° W** (de 78°02' a 79°25', +0.5°)

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `jequetepeque_precipitacion.csv` a `jequetepeque_precipitacion_multiestacion.csv`.
- Metadata consolidada y reformateada desde `jequetepeque_precipitacion_metadata.md` a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
