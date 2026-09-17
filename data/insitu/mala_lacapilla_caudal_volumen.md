# Metadata — Metadata — Caudal y Volumen Mensual, Estación "La Capilla", Río Mala

## I. Información general

- **Archivo de datos:** `mala_lacapilla_rio_mala_caudales.csv`
- **Ámbito geográfico:** Cuenca del río Mala, vertiente del Pacífico
- **Departamento / Provincia:** Lima / Cañete (distrito de Calango)
- **Resolución temporal:** Mensual
- **Periodo de registro:** agosto de 1938 – julio de 2004 (66 años hidrológicos, 792 registros mensuales)
- **Desfase respecto al año calendario:** Sí. La fuente original organiza los datos por **año hidrológico** (agosto–julio). Se reconstruyó a formato calendario estándar: cada valor de agosto-diciembre corresponde al primer año del par (ej. fila "1938 | 1939" → agosto-diciembre son de 1938, enero-julio son de 1939).
- **Completitud:** 100% (0 meses faltantes en el rango declarado)

## II. Fuentes de datos originales

| Documento | Entidad emisora | Año | Uso en este dataset |
|---|---|---|---|
| "Propuesta de Asignaciones de Agua en Bloque... Valles Mala-Omas" (Informe Final + Anexo Nº1, Anexo Nº2) | Ing. Javier Goicochea Ríos / ATDR Mala-Omas-Cañete (PROFODUA) | 2004 | Fuente única de la serie mensual 1938–2004 (Anexo Nº1). Anexo Nº2 es solo el hidrograma gráfico de la misma serie, no aporta datos adicionales. |
| "Evaluación de los Recursos Hídricos de la Cuenca del Río Mala — Estudio Hidrológico" | INRENA / IRH / ATDR Mala-Omas-Cañete | 2007 | Usado solo para metadata de la estación (código, coordenadas, área de cuenca, periodo operativo declarado 1964–2005). No aportó datos numéricos adicionales a la serie 1938–2004 usada aquí. |

Dato original medido en campo por SENAMHI; recopilado por la Sub Administración Técnica del Sub Distrito de Riego Mala-Omas.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `caudal_lacapilla_m3s` | `caudal_lacapilla_m3s` |
| `volumen_lacapilla_mmc` | `volumen_lacapilla_mmc` |

---

| Columna | Descripción | Unidad | Fuente | Método de cálculo |
|---|---|---|---|---|
| `date` | Primer día del mes calendario | YYYY-MM-01 | — | Reconstruido desde año hidrológico |
| `caudal_lacapilla_m3s` | Caudal medio mensual del río Mala en la estación La Capilla | m³/s | Medido (SENAMHI), tal como aparece en Anexo Nº1 | — |
| `volumen_lacapilla_mmc` | Volumen mensual equivalente | MMC (millones de m³) | Calculado | `V = Q_promedio_mensual × 2.592×10⁶ s / 10⁶`, redondeado a 2 decimales. Nota: el factor 2.592×10⁶ s asume 30 días/mes para todos los meses (aproximación estándar de la metodología solicitada); no se ajustó por el número real de días de cada mes (28–31). |

## IV. QA/QC

**Transformaciones aplicadas:**
- Extracción fiel de la tabla original (formato Word/tabla), sin alteración de valores.
- Reconstrucción de fecha calendario a partir del esquema de año hidrológico agosto–julio.
- Cálculo de volumen mensual según fórmula estándar solicitada (ver arriba).

**Valores marcados en la fuente original (negrita en el documento) — no se modificaron, solo se documentan:**
- **Marzo de 1946 = 152.93 m³/s** — marcado explícitamente en la fuente como "valor corregido". El texto del Informe Final confirma: el valor original registrado (179.13 m³/s) fue corregido a 152.93 m³/s tras el análisis de consistencia (prueba T de Student / F de Fischer, 95% confianza) frente a las estaciones Cañete (Socsi) y Lurín (Manchay).
- **Mayo, junio y julio de 1974 = 5.58, 3.63, 2.90 m³/s** — marcados en la fuente junto a la nota "Completados", indicando que son valores estimados/completados, no medidos directamente. No se identificó en el texto del informe el método específico de completación usado para estos tres meses.

**Detección de valores negativos:** Ninguno encontrado (0 de 792 registros).

**Continuidad temporal:** Serie completa sin meses faltantes entre 1938-08 y 2004-07.

**Valores atípicos (outliers):** Se calculó IQR **por mes calendario** (no globalmente), dado que el caudal tiene fuerte estacionalidad (avenidas en verano austral, ene-abr). Se detectaron 36 meses fuera del rango [Q1-1.5·IQR, Q3+1.5·IQR] de su propio mes. La gran mayoría corresponde a años de crecidas documentadas en la literatura hidrológica peruana (1946, 1983-84, 1993-94, 1998), consistentes con eventos El Niño; se interpretan como extremos hidrológicos genuinos, no errores de digitación. El detalle mes a mes está en `qa_per_month.json` (adjunto como referencia interna, no forma parte del entregable final salvo que se solicite).

**Consistencia caudal-volumen:** Por construcción (volumen derivado algebraicamente del caudal), no hay inconsistencias posibles entre ambas columnas.

**Limitaciones conocidas:**
- La fórmula de conversión a MMC usa 2.592×10⁶ s/mes de forma constante (equivalente a 30 días), lo que introduce un sesgo sistemático de hasta ±3.3% en meses de 28, 29 o 31 días. Si se requiere precisión exacta, puede recalcularse usando los días reales de cada mes.
- No se pudo verificar independientemente el método de "completación" de los 3 valores de 1974.
- El periodo operativo de la estación declarado en el estudio de 2007 (1964–2005) no coincide con el rango de esta serie (1938-2004); ambos documentos usan la misma estación pero reportan periodos de inicio distintos — posible diferencia entre "inicio de operación limnimétrica" (1938, según el informe 2004) vs. "inicio como limnigráfica bajo SENAMHI" (1964/1965, según el estudio 2007). Se documenta pero no se resuelve aquí.

---

**Resumen ejecutivo migrado desde `mala_caudales_resumen_ejecutivo.md`:**

# Resumen ejecutivo — Dataset Caudal/Volumen La Capilla (Río Mala)

## Completitud
- **792/792 meses presentes (100.00%)** — agosto 1938 a julio 2004, sin huecos.
- **0 columnas con datos faltantes.**

## Alertas de calidad detectadas

| Alerta | Severidad | Detalle |
|---|---|---|
| 1 valor "corregido" en la fuente | Informativa | Marzo 1946 = 152.93 m³/s (original 179.13, corregido tras análisis de consistencia estadística). No requiere acción; ya viene corregido de la fuente. |
| 3 valores "completados" en la fuente | Media | Mayo–julio 1974. Son estimaciones, no mediciones directas; método de completación no documentado en el informe. Recomendado marcarlos si el dataset se usa para calibración fina de modelos. |
| 36 meses atípicos (IQR por mes) | Baja | Coinciden con crecidas conocidas (1946, 1983-84, 1993-94 El Niño, 1998). Interpretados como extremos reales, no errores. |
| Discrepancia de coordenadas de la estación entre las 2 fuentes | Media | Longitud varía entre 76°29' y 76°33'W; altitud entre 442 y 468 msnm, según el documento. Ver sección V de la metadata. No se resolvió arbitrariamente — queda documentado para que el equipo decida cuál fuente priorizar. |
| Discrepancia en periodo operativo declarado de la estación | Baja | El informe 2004 usa datos desde 1938; el estudio 2007 declara inicio de operación 1964/1965. Ambos se refieren a la misma estación física. |
| Valores negativos | Ninguna | No se encontraron. |
| Consistencia caudal-volumen | Ninguna | Garantizada por construcción (volumen derivado del caudal). |

## Alcance de esta entrega

Este dataset cubre **únicamente** la serie de caudal/volumen de la estación La Capilla (río Mala). Del resto de los documentos analizados (18 estaciones pluviométricas, evapotranspiración, temperatura, agua subterránea) **no se generó dataset** en esta fase porque:
- La precipitación mensual histórica año-por-año no está disponible como texto/tabla en los archivos proporcionados (solo promedios climatológicos 1964–2005; los registros año-por-año referenciados como "Anexo 1.1" aparecen únicamente como gráficos/imágenes, no extraíbles de forma confiable).
- El agua subterránea solo tiene volúmenes anuales agregados (2001-2002), sin serie mensual.
- No se encontró ninguna serie de nivel freático en los documentos.

Si se desea avanzar con evapotranspiración/temperatura (que sí podrían tener series por estación) o con la extracción asistida de las gráficas de precipitación, quedo a la espera de indicación.

## Archivos entregados
1. `caudal_volumen_lacapilla_rio_mala.csv` — dataset (date, caudal_lacapilla_m3s, volumen_lacapilla_mmc)
2. `metadata_caudal_volumen_lacapilla.md` — metadata completa (secciones I-V)
3. Este resumen ejecutivo


## V. Dominio espacial y coordenadas

**Estación:** La Capilla (código SENAMHI 000631), sobre el puente La Capilla, río Mala, distrito de Calango, provincia de Cañete, departamento de Lima.

⚠️ **Discrepancia de coordenadas entre fuentes** (documentada, no resuelta arbitrariamente):

| Fuente | Latitud | Longitud | Altitud |
|---|---|---|---|
| Informe Final PROFODUA (2004) | 12°31'S | 76°33'W | 468 msnm |
| Estudio Hidrológico INRENA (2007) — Cuadro 5.1.1 (estaciones hidrométricas) | 12°31'S | 76°31'W | 468 msnm |
| Estudio Hidrológico INRENA (2007) — Cuadro 1.7.1 (estaciones pluviométricas) y usado en el resto del texto | 12°31'S | 76°29'W | 442 msnm |

- **Coordenadas decimales (WGS84), usando el valor central de las tres fuentes:** Latitud ≈ **-12.517°**, Longitud ≈ **-76.517°** (rango real entre -76.55° y -76.48°)
- **Altitud:** 442–468 msnm (no se puede determinar cuál es la correcta con la información disponible)

**Bounding box recomendado para extracción GRACE-FO Mascon** (margen de ~1.5° sobre la ubicación de la estación, para cubrir la resolución espacial de GRACE ~300 km):

- Latitud: **-14.02° a -11.02°**
- Longitud: **-78.02° a -75.02°**

Nota: este bounding box cubre solo el punto de la estación, no toda la cuenca del río Mala (que se extiende hacia el este hasta ~76°55'W según el estudio 2007, con divisoria en Cerro Chirimaya, 5,851 msnm). Si el objetivo es validar TWSA de toda la cuenca colectora (2,154–2,332 km² según la fuente), se recomienda ampliar el bounding box longitudinal hacia el este hasta cubrir el límite de cuenca reportado (75°55'–76°40'W aprox.), no solo el punto de la estación.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `mala_lacapilla_rio_mala_caudales.csv` a `mala_lacapilla_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `mala_lacapilla_rio_mala_caudales_metadata.md` a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
- Resumen ejecutivo QA (`mala_caudales_resumen_ejecutivo.md`) migrado íntegramente a la sección IV de esta metadata; el archivo `.md` independiente se retira.
