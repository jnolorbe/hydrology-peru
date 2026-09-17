# Metadata — Metadata — Precipitación total mensual, 6 estaciones (Cuenca del río Cañete)

## I. Información general

- **Ámbito geográfico**: Cuenca alta del río Cañete (estaciones pluviométricas de cabecera de cuenca y cuencas vecinas tributarias).
- **Departamento**: Lima (todas las estaciones).
- **Resolución temporal**: Mensual.
- **Periodo de registro**: 1964-08 a 2005-07 (41 años hidrológicos: 1964-65 a 2004-05), igual periodo que el dataset de caudal/volumen Socsi ya entregado.
- **Desfase respecto al año calendario**: igual que en el dataset de caudal — año hidrológico Ago(año N)–Jul(año N+1), transformado a fecha calendario `YYYY-MM-01`.
- **% de completitud**: 99.7% global. Detalle por columna:

| Columna | % faltante | Nº meses faltantes |
|---|---|---|
| `precipitacion_yauyos_mm` | 0.20% | 1 |
| `precipitacion_tanta_mm` | 0.00% | 0 |
| `precipitacion_carania_mm` | 0.00% | 0 |
| `precipitacion_huangascar_mm` | 0.00% | 0 |
| `precipitacion_vilca_mm` | 0.00% | 0 |
| `precipitacion_yauricocha_mm` | 0.41% | 2 |
| `precipitacion_areal_mm` | 0.00% (calculada con las estaciones disponibles cada mes) | 0 |

## II. Fuentes de datos originales

| Fuente | Documento | Entidad / año | Qué aportó |
|---|---|---|---|
| Única fuente | `INFORME_FINAL_CAÑETE.doc`, Anexos 2.1 a 2.6: "Precipitación total mensual - Estación [Yauyos/Tanta/Carania/Huangáscar/Vilca/Yauricocha] (mm)" | PROFODUA / ATDR Cañete, informe final de asignación de agua, 2006 | Serie completa de precipitación total mensual, 1964-65 a 2004-05, para las 6 estaciones pluviométricas usadas en el balance hídrico del estudio. |

No se cruzó esta variable contra el PDF (`ESTUDIO_HIDROLOGICO_CAÑETE.pdf`, Cuadro N°4.1 / Anexo 4.0), que también reporta precipitación histórica pero para un listado de estaciones distinto (Cañete, Pacarán, Yauyos + red vecina SENAMHI) y no fue extraído en esta entrega — **pendiente si se solicita como validación cruzada**.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `precipitacion_yauyos_mm` | `precipitacion_yauyos_mm` |
| `precipitacion_tanta_mm` | `precipitacion_tanta_mm` |
| `precipitacion_carania_mm` | `precipitacion_carania_mm` |
| `precipitacion_huangascar_mm` | `precipitacion_huangascar_mm` |
| `precipitacion_vilca_mm` | `precipitacion_vilca_mm` |
| `precipitacion_yauricocha_mm` | `precipitacion_yauricocha_mm` |
| `precipitacion_areal_mm` | `precipitacion_areal_mm` |

---

| Columna | Descripción | Unidad | Fuente | Fórmula |
|---|---|---|---|---|
| `date` | Fecha del mes, día fijado en 01 | YYYY-MM-DD | — | Reconstruida desde el año hidrológico |
| `precipitacion_yauyos_mm` | Precipitación total mensual, Estación Yauyos | mm | Medido | — |
| `precipitacion_tanta_mm` | Precipitación total mensual, Estación Tanta | mm | Medido | — |
| `precipitacion_carania_mm` | Precipitación total mensual, Estación Carania | mm | Medido | — |
| `precipitacion_huangascar_mm` | Precipitación total mensual, Estación Huangáscar | mm | Medido | — |
| `precipitacion_vilca_mm` | Precipitación total mensual, Estación Vilca | mm | Medido | — |
| `precipitacion_yauricocha_mm` | Precipitación total mensual, Estación Yauricocha | mm | Medido | — |
| `precipitacion_areal_mm` | Precipitación areal aproximada de la cuenca | mm | Calculado | **Promedio aritmético simple** de las 6 estaciones disponibles ese mes (se ignoran NA en el promedio, no se imputan). *No se aplicó Thiessen ni polígonos de influencia porque el documento fuente no reporta áreas de influencia por estación para esta red — ver limitaciones.* |

## IV. QA/QC

1. **Datos faltantes explícitos en la fuente**: se encontraron 3 celdas marcadas literalmente como **"S/D" (sin dato)** en el documento original:
   - Yauyos, mayo 2004 (año hidrológico 2003-04).
   - Yauricocha, abril 2001 (año hidrológico 2000-01).
   - Yauricocha, setiembre 2003 (año hidrológico 2003-04).
   Estas celdas se codificaron como `NA`, tal como exige el protocolo. **No fueron estimadas ni interpoladas.**
2. **Continuidad temporal**: sin meses faltantes en el rango 1964-08 a 2005-07 para ninguna estación (492/492 filas presentes; los únicos vacíos son los 3 "S/D" puntuales, no huecos de mes completo).
3. **Valores negativos**: ninguno (0 en las 6 estaciones), consistente con lo físicamente esperable para precipitación.
4. **Valores atípicos (IQR por mes calendario, por estación)**: se detectaron 146 casos en total. La gran mayoría corresponde a **meses de estación seca (mayo–setiembre)**, donde la mediana histórica es 0 mm y el rango intercuartílico es muy estrecho o nulo; por lo tanto, **cualquier lluvia ocasional fuera de temporada (aunque sea de pocos mm) se marca estadísticamente como atípica**, sin ser un error de dato — es una característica esperada del régimen de lluvias estacional de la sierra de Lima. Ejemplos de atípicos más relevantes a nivel de magnitud (temporada húmeda, posibles señales de eventos El Niño):
   - Tanta, marzo 1972: 355.0 mm
   - Huangáscar, marzo 1972: 366.0 mm
   - Yauricocha, enero 1987: 315.0 mm
   Estos tres coinciden con años de anomalías climáticas documentadas en la región (1972-73, 1986-87) y aparecen consistentemente elevados en varias estaciones simultáneamente el mismo año, lo que refuerza la interpretación de **extremo real y no error de digitación**. No se modificó ni eliminó ningún valor.
5. **Consistencia entre estaciones**: no se realizó (en esta entrega) un análisis de doble masa entre estaciones; el documento fuente sí lo incluye (Anexo 2.7 "Valores acumulados de precipitación y descargas para el diagrama de doble masa"), pero no fue extraído — **disponible si se solicita**.
6. **Valores marcados como "corregidos"/"completados" en la fuente**: no se encontró ningún marcado de este tipo en los Anexos 2.1–2.6 (solo se encontraron los 3 "S/D" ya documentados). El Cuadro N°1.7 del mismo documento ("Precipitación total mensual completa y consistente - periodo 1964-2005") sugiere que existe una versión ya corregida/rellenada de una red más amplia de estaciones vecinas — **no fue extraído en esta entrega** porque no corresponde a las 6 estaciones aquí trabajadas; si se desea integrarlo, debe tratarse como una fuente aparte y compararse explícitamente contra estos datos.
7. **Limitaciones conocidas**:
   - La columna `precipitacion_areal_mm` usa promedio aritmético simple, no Thiessen, por falta de información de áreas de influencia en la fuente. Esto es una aproximación gruesa y debe usarse con cautela para la validación de TWSA.
   - No se extrajo aún el Cuadro N°4.1/Anexo 4.0 del PDF (244 pág.), que podría tener una red de estaciones distinta o complementaria.

## V. Dominio espacial y coordenadas

| Estación | Latitud | Longitud | Altitud (msnm) |
|---|---|---|---|
| Yauyos | 12°27' S | 75°55' W | 2290 |
| Tanta | 12°08' S | 76°01' W | 4505 |
| Carania | 12°21' S | 75°52' W | 3825 |
| Huangáscar | 12°54' S | 75°50' W | 2556 |
| Vilca | 12°07' S | 75°49' W | 3816 |
| Yauricocha | 12°19' S | 75°43' W | 4522 |

- **Coordenadas decimales aproximadas (WGS84)** (conversión de grados-minutos, sin segundos declarados en la fuente → precisión ~1.8 km):
  - Yauyos: -12.450, -75.917
  - Tanta: -12.133, -76.017
  - Carania: -12.350, -75.867
  - Huangáscar: -12.900, -75.833
  - Vilca: -12.117, -75.817
  - Yauricocha: -12.317, -75.717
- **Bounding box recomendado para extracción GRACE-FO Mascon** (margen 0.5° sobre el conjunto de las 6 estaciones):
  - Lat: -13.400° a -11.633°
  - Lon: -76.517° a -75.217°
- No se detectaron discrepancias de coordenadas para estas estaciones (fuente única).
- **Nota de integración**: este bounding box no coincide exactamente con el de Socsi (dataset de caudal, entregado previamente); Socsi está aguas abajo, mientras estas 6 estaciones son de cabecera. Si se necesita un bounding box único para toda la cuenca, debe definirse explícitamente combinando ambos dominios — no se ha hecho de forma automática.

---

## Resumen ejecutivo

**Completitud**: 99.7% global (3 valores puntuales "S/D" de 2,952 observaciones estación-mes; 0 meses completamente vacíos).

**Tabla de alertas de calidad**

| Alerta | Severidad | Detalle |
|---|---|---|
| 3 valores "S/D" explícitos en la fuente | 🟢 Baja | Codificados como NA, no estimados (ver IV.1). |
| 146 outliers IQR por mes calendario | 🟢 Baja (mayormente esperado) | Concentrados en meses secos con IQR≈0; unos pocos coinciden con eventos El Niño documentados (ver IV.4). |
| Precipitación areal = promedio aritmético, no Thiessen | 🟡 Media | Por falta de áreas de influencia en la fuente; usar con cautela. |
| Sin cruce con el PDF (Cuadro 4.1/Anexo 4.0) | 🟡 Media | Pendiente si se requiere una segunda fuente de validación. |

**Alcance y limitaciones de esta entrega**:
- 6 estaciones pluviométricas de cabecera de la cuenca del Cañete, únicamente desde el `.doc` (PROFODUA 2006).
- No incluye las series cortas (1995-2000) de evaporación/temperatura/humedad/viento de Pacarán y Yauyos — se descartaron explícitamente por decisión tuya en esta ronda.
- No incluye el Cuadro N°1.7 ("completa y consistente") del mismo documento, que parece ser una versión ya tratada de una red más amplia — pendiente de decisión.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `cañete_precipitacion.csv` a `canete_precipitacion.csv`.
- Metadata consolidada y reformateada desde `cañete_metadata_precipitacion.md` a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
