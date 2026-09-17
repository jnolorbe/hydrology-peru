# Metadata — Metadata — Dataset Caudal y Volumen, Estación El Tigre (Río Tumbes)

## I. Información general

- **Archivo de datos:** `caudal_volumen_eltigre.csv`
- **Ámbito geográfico:** Cuenca del río Tumbes (binacional Perú-Ecuador, cuenca Puyango-Tumbes)
- **Departamento / Región:** Tumbes, Perú (Provincia Tumbes, Distrito San Jacinto)
- **Resolución temporal:** Mensual
- **Periodo de registro:** 1963-01 a 2008-12 (46 años, 552 meses)
- **Desfase respecto al año calendario:** Ninguno — esta serie está en año calendario (ENE-DIC). Nota: existe una segunda fuente de la misma estación organizada en año hidrológico (AGO-JUL, campaña 1963/64 a 2003/04) que **no** se usó como base por decisión del usuario, pero se documenta su existencia en la Sección IV.
- **% de completitud (caudal medio):** 98.7% (545 de 552 meses con dato; 7 meses faltantes, todos en 1997: feb-ago)
- **% de completitud (caudal máximo):** ver Sección IV — falta el primer registro (1963-01) y algunos meses adicionales en años con valores decimales largos post-2000.
- **% de completitud (caudal mínimo):** falta 1963-01 (mismo patrón que máximo).

## II. Fuentes de datos originales

| Fuente | Entidad emisora | Año / periodo cubierto | Qué aportó |
|---|---|---|---|
| `Serie_Caudal_Mensual.xls` (hojas Qmed, Qmax, Qmin) | Proyecto Especial Binacional Puyango Tumbes / INADE (Instituto Nacional de Desarrollo) | Datos 1963-2008 | **Fuente base única** para caudal medio, máximo y mínimo mensual, usada tal cual para este dataset. |
| `1-2-INTROD-OFERTA-2.doc` ("Propuesta de Asignación de Agua en Bloque...", Ing. MSc. Guillermo Vílchez Ochoa, PROFODUA/INRENA) | INRENA / PROFODUA, Perú | Documento sin fecha explícita de emisión (revisiones hasta 2007) | Aportó exclusivamente **contexto y metadata**: coordenadas de mayor precisión de la estación, área de cuenca controlada, entidad operadora, código de estación, y la nota de que el año 1983 fue excluido del análisis hidrológico original del consultor (no de este dataset). **No aportó valores numéricos usados en el CSV.** |
| `Tumbes_C9-c10-c11-ff4.xls` (hoja `Q Tumbes Tigre Cw1`) | PROFODUA (Formalización de Derechos de Agua, 2004) | 1963/64-2003/04 (año hidrológico) | **No se usó como fuente de datos** en este dataset (se descartó por decisión del usuario a favor de `Serie_Caudal_Mensual.xls`). Se cita solo para reportar la discrepancia en la Sección IV. |

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `caudal_eltigre_m3s` | `caudal_eltigre_m3s` |
| `caudal_eltigre_max_m3s` | `caudal_eltigre_max_m3s` |
| `caudal_eltigre_min_m3s` | `caudal_eltigre_min_m3s` |
| `volumen_eltigre_mmc` | `volumen_eltigre_mmc` |

---

| Columna | Descripción | Unidad | Fuente | Fórmula |
|---|---|---|---|---|
| `date` | Fecha del mes (día fijo = 01) | YYYY-MM-DD | — | — |
| `caudal_eltigre_m3s` | Caudal medio mensual, Estación El Tigre | m³/s | Medido (hoja Qmed) | — |
| `caudal_eltigre_max_m3s` | Caudal máximo medio mensual, Estación El Tigre | m³/s | Medido (hoja Qmax) | — |
| `caudal_eltigre_min_m3s` | Caudal mínimo medio mensual, Estación El Tigre | m³/s | Medido (hoja Qmin) | — |
| `volumen_eltigre_mmc` | Volumen mensual equivalente al caudal medio | MMC (millones de m³) | Calculado | V = caudal_eltigre_m3s × (n_días_del_mes × 86,400 s) / 10⁶, redondeado a 2 decimales. **Se usan los días reales de cada mes/año** (28, 29, 30 o 31, considerando años bisiestos), no 30 días fijos. Este es un ajuste solicitado por el usuario respecto a la regla de cálculo estándar del proyecto (30 días/mes), que se documenta aquí como desviación explícita. |

## IV. QA/QC

**Transformaciones aplicadas**
- Se incluyeron caudal máximo y mínimo mensual como columnas adicionales de contexto/QA (no solicitadas explícitamente en las reglas base del proyecto, pero disponibles en la misma fuente auditada y útiles para verificar consistencia interna min≤med≤max).
- Celdas vacías en la fuente → `NA` en el CSV (nunca vacío).
- **Volumen calculado con días reales del mes** (no 30 días fijos): esto corrige el sesgo sistemático de hasta ±3.35% que tenía la primera versión de este dataset. Meses de 31 días quedan ~3.3% por encima del cálculo con 30 días fijos; meses de 28 días quedan ~6.7% por debajo; meses de 29 días (febrero bisiesto) ~3.3% por debajo; meses de 30 días no cambian. Años bisiestos verificados correctamente (ej. 1964, 1968, 2000 con feb=29 días).

**Faltantes**
- 1997: caudal medio, máximo y mínimo faltantes de febrero a julio/agosto (6-8 meses según la variable). No hay ninguna nota en la fuente original que indique la razón (no se encontró texto de "corregido/completado/estimado" asociado).
- 1963-01: falta caudal máximo y mínimo (solo existe el medio).

**Valores atípicos (IQR por mes calendario)**
Se detectaron 33 meses fuera del rango intercuartílico (calculado por mes, no globalmente). La gran mayoría corresponde a dos eventos El Niño extraordinarios bien documentados en la región:
- **1982-11 a 1983-12**: evento El Niño 1982-83, con el pico histórico de la serie (1983-03: 1244.2 m³/s). El propio informe técnico (`1-2-INTROD-OFERTA-2.doc`) indica que *"el año 1983 extraordinario no fue considerado para el análisis de estudio"* por el consultor original — es decir, el valor se mantiene en la fuente y en este dataset (no se elimina, según regla no negociable del proyecto), pero se señala aquí como extremo real conocido, no error.
- **1997-11 a 1998-02**: evento El Niño 1997-98, segundo evento extraordinario de la serie.
- Meses aislados en 1972, 1975, 1987, 1989, 1999, 2006 con valores moderadamente altos, consistentes con la variabilidad interanual típica de la costa norte peruana.
- **Interpretación:** se recomienda tratarlos como extremos climáticos reales, no como errores de medición, salvo indicación contraria del usuario.

**Consistencia caudal medio vs máximo/mínimo**
- 2 inconsistencias detectadas donde `min > med` o `med > max`:
  - 2000-12: min=21.59, med=19.65, max=40.49 → medio menor que el mínimo reportado.
  - 2004-12: min=16.85, med=25.63, max=21.89 → medio mayor que el máximo reportado.
- Estas inconsistencias probablemente derivan de que Qmed, Qmax y Qmin post-2000 tienen decimales largos (indicando reprocesamiento/relleno con otra metodología, posiblemente interpolación o modelo, no lectura directa de limnígrafo) y pudieron mezclarse de fuentes distintas. **No se corrigieron — se documentan aquí para decisión del usuario.**

**Valores marcados como corregidos/completados en la fuente**
- No se encontró ninguna anotación textual explícita de "corregido", "estimado" o "completado" en las hojas de `Serie_Caudal_Mensual.xls`. Sin embargo, se observa un cambio de patrón: años 1963-1999 tienen valores con 1 decimal (lectura/cálculo manual típico), mientras que años 2000-2008 tienen valores con hasta 15 decimales (sugiere reprocesamiento por hoja de cálculo/modelo, no verificado contra fuente primaria). Se reporta como limitación conocida, no se puede confirmar el método sin el informe técnico correspondiente a esos años.

**Discrepancia entre fuentes (reportada, no resuelta)**
- La misma estación El Tigre tiene una segunda serie de caudal medio mensual en `Tumbes_C9-c10-c11-ff4.xls` (hoja `Q Tumbes Tigre Cw1`), organizada en año hidrológico (agosto-julio), periodo 1963/64-2003/04. Al comparar meses equivalentes, se encontraron pequeñas diferencas numéricas no explicadas (ej.: 1981/82 FEB=194.8 en Cw1 vs valores distintos en la serie calendario tras realinear años; 2000-12 y otros meses con diferencias de decimales). No se promediaron ni se eligió una versión como "correcta" — se usó `Serie_Caudal_Mensual.xls` por instrucción explícita del usuario.
- Esa misma fuente (`Tumbes_C9...xls`, hoja `V Tumbes Tigre Cw2-2`) trae también un volumen mensual ya calculado por la fuente original (no por nosotros), que podría usarse para contrastar el volumen calculado en este dataset si se desea en una entrega futura.

**Limitaciones conocidas**
- No se pudo verificar independientemente si los 7 meses faltantes de 1997 corresponden a interrupción real de la estación o solo a laguna de digitalización.
- El origen exacto de las diferencias entre esta serie y la de año hidrológico (`Cw1`) no pudo determinarse con la información disponible.

---

**Resumen ejecutivo migrado desde `tumbes_resumen_ejecutivo_caudales.md`:**

# Resumen Ejecutivo — Dataset Caudal y Volumen, Estación El Tigre

## Alcance de esta entrega
Serie mensual de caudal (medio, máximo, mínimo) y volumen calculado, estación hidrométrica **El Tigre**, río Tumbes. Periodo 1963-2008 (46 años, 552 meses). Fuente única: `Serie_Caudal_Mensual.xls`, por decisión explícita del usuario (se descartó la serie alternativa en año hidrológico del archivo `Tumbes_C9-c10-c11-ff4.xls`).

## % de completitud
| Columna | % completo | Meses faltantes |
|---|---|---|
| `caudal_eltigre_m3s` | 98.7% | 7 (1997, feb-ago) |
| `caudal_eltigre_max_m3s` | ~98.6% | 1963-01 + los mismos de 1997 |
| `caudal_eltigre_min_m3s` | ~98.6% | 1963-01 + los mismos de 1997 |
| `volumen_eltigre_mmc` | 98.7% | Igual que caudal medio (es derivado) |

## Tabla de alertas de calidad

| # | Alerta | Severidad | Detalle |
|---|---|---|---|
| 1 | Discrepancia de coordenadas/altitud entre fuentes | 🟡 Media | 40 msnm (xls) vs 30 msnm (informe técnico); coordenadas difieren en el orden de segundos de arco. No resuelta — decisión pendiente del usuario. |
| 2 | Discrepancia numérica con serie alternativa de la misma estación | 🟡 Media | `Q Tumbes Tigre Cw1` (año hidrológico) difiere levemente de la serie usada en varios meses. No se investigó la causa raíz ni se promedió. |
| 3 | Inconsistencia min/med/max en 2 meses | 🟡 Media | 2000-12 y 2004-12: el caudal medio queda fuera del rango [mín, máx] reportado en la misma fuente. |
| 4 | 7 meses faltantes en 1997 | 🟢 Baja-Media | Sin explicación en la fuente; no se puede distinguir si es interrupción real de estación o vacío de digitalización. |
| 5 | Cambio de patrón de precisión decimal (post-2000) | 🟢 Baja | Sugiere reprocesamiento con otra metodología a partir del año 2000; no confirmado con fuente primaria adicional. |
| 6 | 33 meses marcados como atípicos por IQR mensual | 🟢 Informativa | Mayoritariamente explicados por los eventos El Niño 1982-83 y 1997-98, documentados en el informe técnico. Se recomienda **no** tratarlos como errores. |

## Limitaciones de esta entrega
- No incluye precipitación, evapotranspiración ni nivel freático — esos datasets se construirán en entregas posteriores según el orden acordado.
- No se generó el dataset con la fuente alternativa de año hidrológico; queda disponible si se requiere en el futuro para contraste.

## Actualización (v2)
El volumen (`volumen_eltigre_mmc`) fue recalculado usando los **días reales de cada mes** (incluyendo años bisiestos), a solicitud del usuario, en lugar de asumir 30 días fijos como en la primera versión. El cambio afecta los valores en ±3.3% a ±6.7% según el mes, siendo más precisa esta versión. El CSV entregado ahora refleja este cálculo corregido.


## V. Dominio espacial y coordenadas

**Estación: El Tigre**

| Fuente | Latitud | Longitud | Altitud |
|---|---|---|---|
| `Serie_Caudal_Mensual.xls` (Qmed/Qmax/Qmin) | 3°46' S (≈ -3.7667°) | 80°27' W (≈ -80.4500°) | 40 msnm |
| `1-2-INTROD-OFERTA-2.doc` (informe técnico PROFODUA) | 03°46'09" S (≈ -3.7692°) | 80°27'25" W (≈ -80.4569°) | 30 msnm |

⚠️ **Discrepancia de coordenadas y altitud entre fuentes** — se reportan ambas versiones, no se promedian ni se elige una por defecto, conforme a la regla del proyecto. La diferencia de altitud (40 vs 30 msnm) y de coordenadas (~150-300 m de diferencia aproximada) debe resolverla el usuario.

- **Cuenca controlada por la estación:** ≈4,380 km² (según informe técnico, no verificado por otra fuente).
- **Cuenca binacional Puyango-Tumbes (total):** ≈4,800 km², ~60% en Ecuador, ~40% en Perú.
- **Entidad operadora (según informe):** SENAMHI - Proyecto Binacional Puyango-Tumbes. Código de estación: 2003.
- **Periodo de operación declarado en el informe:** "desde 1963 hasta la fecha" (documento con revisiones hasta 2007) — consistente con el periodo de datos disponible (1963-2008).

**Bounding box recomendado para extracción GRACE-FO Mascon** (margen 0.5° sobre la estación, usando coordenadas del informe técnico como referencia central por ser las más precisas):
- Latitud: -4.2692° a -3.2692°
- Longitud: -80.9569° a -79.9569°

*Nota: si se prefiere usar las coordenadas redondeadas de los archivos .xls como referencia, el bounding box sería prácticamente idéntico dado el margen de 0.5°; la elección no afecta significativamente la extracción GRACE a esta escala.*

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `tumbes_caudales.csv` a `tumbes_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `tumbes_caudales_metadata.md` a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
- Resumen ejecutivo QA (`tumbes_resumen_ejecutivo_caudales.md`) migrado íntegramente a la sección IV de esta metadata; el archivo `.md` independiente se retira.
