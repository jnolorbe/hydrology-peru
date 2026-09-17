# Metadata — Metadata — Dataset Precipitación Mensual, Cuenca Tumbes (3 estaciones)

## I. Información general

- **Archivo de datos:** `precipitacion_tumbes.csv`
- **Ámbito geográfico:** Cuenca del río Tumbes / Puyango-Tumbes, Perú
- **Departamento / Región:** Tumbes (Provincia Tumbes y Provincia Zarumilla)
- **Resolución temporal:** Mensual
- **Periodo de registro del archivo:** 1964-01 a 2008-12 (rango que cubre a las 3 estaciones; cada una con su propio periodo real de operación, ver tabla abajo)
- **Desfase respecto al año calendario:** Ninguno (ENE-DIC)
- **% de completitud por estación (dentro de su periodo real de operación):**

| Estación | Periodo de operación en la fuente | Meses en periodo | Faltantes | % completitud |
|---|---|---|---|---|
| El Tigre | 1964-01 a 2008-12 | 540 | 0 | 100% |
| Campamento Sede | 1983-01 a 2008-12 | 312 | 0 | 100% |
| Tumpis (Centro Experimental) | 1985-01 a 2008-12 | 288 | 19 (6.6%) | 93.4% |

Nota: Fuera del periodo real de operación de cada estación, las celdas se marcan `NA` en el CSV (p. ej. Campamento Sede y Tumpis no existen antes de 1983/1985 respectivamente) — esto **no** es una laguna de datos, es la ausencia de la estación misma, y se documenta así para no confundirlo con un vacío real de medición.

## II. Fuentes de datos originales

| Fuente | Entidad emisora | Aportó |
|---|---|---|
| `Serie_Precipitación_Mensual_Est__PLU-PG_El_tigre_.xls` | Proyecto Especial Binacional Puyango Tumbes / INADE | Precipitación total mensual (mm), estación El Tigre, 1964-2008. |
| `Serie_Precipitación_Mensual_diaria_Est__PLU-PG_Camp__Sede_.xls` | Dirección de Estudios y S. (Proyecto Binacional Puyango Tumbes) | Precipitación total mensual (mm), estación Campamento Sede, 1983-2008. (A pesar del nombre del archivo que menciona "diaria", la hoja utilizada `pp mensual` contiene únicamente agregados mensuales, no datos diarios). |
| `Series_Variables_Mensuales_Estación_CIA__Tumpis.xls` (hoja `pp mensual`) | PEBPT (Proyecto Especial Binacional Puyango Tumbes) | Precipitación total mensual (mm), estación Centro Experimental Tumpis, 1985-2008. |

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `precipitacion_eltigre_mm` | `precipitacion_eltigre_mm` |
| `precipitacion_campamentosede_mm` | `precipitacion_campamentosede_mm` |
| `precipitacion_tumpis_mm` | `precipitacion_tumpis_mm` |

---

| Columna | Descripción | Unidad | Fuente | Fórmula |
|---|---|---|---|---|
| `date` | Fecha del mes (día fijo = 01) | YYYY-MM-DD | — | — |
| `precipitacion_eltigre_mm` | Precipitación total mensual, estación El Tigre | mm | Medido | — |
| `precipitacion_campamentosede_mm` | Precipitación total mensual, estación Campamento Sede | mm | Medido | — |
| `precipitacion_tumpis_mm` | Precipitación total mensual, estación Centro Experimental Tumpis | mm | Medido | — |

**No se generó `precipitacion_areal_mm`** — no se recibieron áreas de influencia ni polígonos de Thiessen en los insumos entregados. Se puede calcular en una entrega futura si el usuario aporta esa información o si se solicita un promedio aritmético simple como aproximación (no se asume por defecto).

## IV. QA/QC

**Tratamiento del código "T" (traza)**
Las tres fuentes originales usan el código meteorológico estándar **"T"** para indicar precipitación registrada pero por debajo del umbral medible (convención típica <0.1 mm). Este código apareció en las celdas de dos estaciones:
- **El Tigre:** 18 meses con "T" (1964-1980, ver lista completa abajo).
- **Campamento Sede:** 1 mes con "T" (2004-08).
- **Tumpis:** ninguno.

Por decisión de procesamiento (no es un valor faltante ni inventado, es la traducción numérica de un código meteorológico estándar), estos meses se codificaron como **0.0 mm** en el CSV. **Esta es una transformación, no una medición directa** — se documenta aquí explícitamente para que el usuario pueda revertirla si prefiere tratarlos como `NA` u otro valor.

Meses afectados en El Tigre: 1964-07, 1964-08, 1966-06, 1966-08, 1966-09, 1966-12, 1967-03, 1967-05, 1967-06, 1967-07, 1967-08, 1968-07, 1968-08, 1968-10, 1968-11, 1970-04, 1979-08, 1980-09.
Mes afectado en Campamento Sede: 2004-08.

**Faltantes**
- Tumpis: 19 meses faltantes dentro de su periodo de operación (1985-2008), concentrados en 1986 (todo el año, con un total anual reportado de 0.0 que parece un artefacto de la fuente más que una medición real — se recomienda tratar 1986 completo como no confiable) y 1987 (enero-julio faltantes, solo ago-dic presentes).
- El Tigre y Campamento Sede: sin faltantes dentro de su periodo de operación.

**Valores atípicos (IQR por mes calendario)**
Se detectaron 59 (El Tigre), 33 (Campamento Sede) y 18 (Tumpis) meses fuera de rango intercuartílico. Igual que en el dataset de caudal, la gran mayoría coincide con los eventos El Niño 1982-83 y 1997-98, consistentes entre las tres estaciones simultáneamente (ej. 1983-01 a 1983-07 con valores extremos en las tres series donde hay dato disponible) — refuerza que son extremos climáticos reales, no errores aislados de una sola estación.

**Valores negativos:** ninguno detectado (físicamente imposibles no aplican en este dataset).

**Valores marcados como "corregidos"/"completados" en la fuente:** no se encontró ninguna anotación textual explícita en las hojas de precipitación.

**Consistencia entre estaciones (referencial, sin cálculo formal de correlación en esta entrega):** en los meses donde las tres estaciones tienen dato simultáneo (1985-2008), los valores muestran el mismo patrón estacional (lluvias intensas dic-may, sequía jun-nov) y responden igual a los eventos El Niño, lo cual es consistente con estar en la misma cuenca/microclima.

**Limitaciones conocidas**
- No se cuenta con las áreas de influencia de cada estación, por lo que no se generó `precipitacion_areal`.
- El año 1986 completo en Tumpis debe tratarse con precaución (posible artefacto, ver arriba).
- No se pudo confirmar si Campamento Sede tuvo registro diario que respalde el mensual (el archivo fuente menciona "diaria" en su nombre pero solo se recibió la hoja de agregados mensuales).

---

**Resumen ejecutivo migrado desde `tumbes_resumen_ejecutivo_precipitacion.md`:**

# Resumen Ejecutivo — Dataset Precipitación Mensual (3 estaciones)

## Alcance de esta entrega
Serie mensual de precipitación total (mm) para las 3 estaciones pluviométricas disponibles en la cuenca Tumbes: **El Tigre** (1964-2008), **Campamento Sede** (1983-2008) y **Tumpis** (1985-2008). Rango total del archivo: 1964-01 a 2008-12.

## % de completitud
| Estación | % completitud (en su periodo de operación) |
|---|---|
| El Tigre | 100% |
| Campamento Sede | 100% |
| Tumpis | 93.4% (19 meses faltantes, concentrados en 1986-87) |

## Tabla de alertas de calidad

| # | Alerta | Severidad | Detalle |
|---|---|---|---|
| 1 | Transformación de código "T" (traza) a 0.0 mm | 🟡 Media | 19 meses en total (18 en El Tigre, 1 en Campamento Sede) reclasificados de código meteorológico "T" a valor numérico 0.0. Es una convención estándar, pero se documenta como transformación explícita — revertible si el usuario prefiere otro tratamiento. |
| 2 | Año 1986 en Tumpis probablemente no confiable | 🟡 Media | Todos los meses vacíos excepto un total anual de 0.0 mm, lo cual es climatológicamente inusual para la zona — sugiere problema de digitalización, no una sequía real de 12 meses. |
| 3 | 19 meses faltantes en Tumpis (1986 completo + ene-jul 1987) | 🟢 Baja-Media | Sin explicación en la fuente. |
| 4 | 110 meses atípicos combinados (IQR por mes) entre las 3 estaciones | 🟢 Informativa | Coinciden fuertemente con El Niño 1982-83 y 1997-98 en las tres estaciones simultáneamente — refuerza que son extremos reales, no errores de una sola estación. |
| 5 | Sin `precipitacion_areal` | 🟢 Informativa | No se recibieron áreas de influencia / polígonos de Thiessen; se puede agregar en una entrega posterior si se provee esa información. |

## Limitaciones de esta entrega
- No incluye evapotranspiración ni nivel freático — pendientes según el orden acordado con el usuario.
- La estación Campamento Sede no reporta altitud en la fuente (dato faltante en metadata, no en la serie de datos).
- La discrepancia de coordenadas/altitud de El Tigre reportada en el dataset de caudal aplica también aquí (misma estación).


## V. Dominio espacial y coordenadas

| Estación | Latitud | Longitud | Altitud | Fuente |
|---|---|---|---|---|
| El Tigre | 3°46' S (≈ -3.7667°) | 80°27' W (≈ -80.4500°) | 40 msnm | `Serie_Precipitación..._El_tigre_.xls` (mismas coordenadas redondeadas que en el dataset de caudal; ver discrepancia ya reportada en esa metadata frente al informe técnico: 03°46'09"S / 80°27'25"W / 30 msnm) |
| Campamento Sede | 3°33' S (≈ -3.5500°) | 80°26' W (≈ -80.4333°) | No reportada en la fuente | `Serie_Precipitación..._Camp__Sede_.xls` |
| Tumpis (Centro Experimental) | 3°31' S (≈ -3.5167°) | 80°19' W (≈ -80.3167°) | No reportada en la fuente | `Series_Variables_Mensuales..._Tumpis.xls` |

**Bounding box recomendado para extracción GRACE-FO Mascon** (margen 0.5° sobre el conjunto de las 3 estaciones):
- Latitud: -4.2667° a -3.0167°
- Longitud: -80.9500° a -79.8167°

*Se usó el rango combinado de las 3 estaciones (más al norte/este: Tumpis; más al sur/oeste: El Tigre) más el margen de 0.5° en cada dirección.*

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `tumbes_precipitacion.csv` a `tumbes_precipitacion_multiestacion.csv`.
- Metadata consolidada y reformateada desde `tumbes_precipitacion_metadata.md` a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
- Resumen ejecutivo QA (`tumbes_resumen_ejecutivo_precipitacion.md`) migrado íntegramente a la sección IV de esta metadata; el archivo `.md` independiente se retira.
