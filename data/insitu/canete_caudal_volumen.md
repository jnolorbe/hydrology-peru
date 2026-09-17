# Metadata — Metadata — Caudal y Volumen mensual, Estación Socsi (Río Cañete)

## I. Información general

- **Ámbito geográfico**: Cuenca del río Cañete, punto de control Estación Socsi (límite cuenca media/baja).
- **Departamento / Provincia / Distrito**: Lima / Cañete / Lunahuaná.
- **Resolución temporal**: Mensual.
- **Periodo de registro**: 1964-08 a 2005-07 (41 años hidrológicos completos: 1964-65 a 2004-05).
- **Desfase respecto al año calendario**: Las fuentes originales presentan la serie en **año hidrológico** (agosto a julio). Se transformó a fecha calendario estándar `YYYY-MM-01` para este dataset (p. ej. "Ago" del año hidrológico 1964-65 → `1964-08-01`; "Ene" del mismo año hidrológico → `1965-01-01`).
- **% de completitud**: 100% (492/492 meses, sin datos faltantes; ver sección IV para reservas sobre la naturaleza de la serie).

## II. Fuentes de datos originales

| Fuente | Documento | Entidad / año | Qué aportó específicamente |
|---|---|---|---|
| Fuente A | `DISPONIBILIDAD_HIDRICA_CUENCA_MEDIA.xls`, hojas `Q aforado` y `V aforado` | Elaboración propia (citada en la hoja), estudio de disponibilidad hídrica cuenca media, s/f | Serie completa de caudal medio mensual aforado (m³/s) y volumen mensual (MMC) ya calculado por la fuente, 1964-65 a 2004-05, Estación Socsi. **Fuente primaria usada para los valores numéricos de caudal en este CSV** (mayor precisión decimal que el documento Word). |
| Fuente B | `INFORME_FINAL_CAÑETE.doc`, Anexo 1 "Caudal medio mensual - histórico aforado (m3/s)" | PROFODUA / ATDR Cañete, informe final de asignación de agua, 2006 | Misma serie de caudal Socsi (1964-65 a 2004-05), reportada con 2 decimales. **Usada exclusivamente para validación cruzada (QA)**, no como fuente de valores. |
| Fuente C (contexto, no incorporada aún) | `ESTUDIO_HIDROLOGICO_CAÑETE.pdf`, Cuadro N°1.4.1 (pág. 7) | INRENA–DGAS–ATDR-MOC, 2004 | Ficha de la estación Socsi (coordenadas, altitud, periodo de operación declarado, entidad operadora SENAMHI). Usada solo para la sección V y para señalar la discrepancia de periodo declarado (ver abajo). No se extrajo su serie de caudal en esta entrega. |

**Discrepancia detectada (no resuelta arbitrariamente):**
- El Cuadro N°1.4.1 del PDF (Fuente C) declara que la Estación Socsi operó "Ene/1965 – Dic/2000" bajo SENAMHI. Sin embargo, las tablas de caudal aforado (Fuentes A y B) cubren 1964-08 a 2005-07, un rango más amplio. No se puede determinar desde estos documentos si la extensión post-2000 corresponde a otro operador, a una reconstrucción, o si el Cuadro 1.4.1 solo describe el periodo de un tramo de la operación. **Se reporta la discrepancia; no se ha asumido cuál periodo es el correcto.**

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `caudal_socsi_m3s` | `caudal_socsi_m3s` |
| `volumen_socsi_mmc` | `volumen_socsi_mmc` |

---

| Columna | Descripción | Unidad | Fuente | Fórmula |
|---|---|---|---|---|
| `date` | Fecha del mes, día fijado en 01 | YYYY-MM-DD | — | Reconstruida a partir del año hidrológico declarado en la fuente |
| `caudal_socsi_m3s` | Caudal medio mensual aforado (medido) en la Estación Socsi | m³/s | Medido (fuente A, validado contra fuente B) | — |
| `volumen_socsi_mmc` | Volumen mensual | MMC (millones de m³) | Calculado | `V = Q_promedio_mensual (m³/s) × (n_días_del_mes × 86,400 s) / 10⁶`, usando los días reales del mes/año (considera años bisiestos), redondeado a 2 decimales |

## IV. QA/QC

1. **Naturaleza de la serie**: es un registro de caudal **aforado** (medido en campo), según lo indican ambas fuentes ("Elaboración Propia" / anexo histórico aforado). No es una serie generada por modelo.
2. **Validación cruzada entre fuentes A y B**: se comparó mes a mes el caudal reportado en el .xls (Fuente A, alta precisión decimal) contra el .doc (Fuente B, 2 decimales). Diferencia máxima encontrada: **0.005 m³/s** en todos los meses — consistente con redondeo, sin discrepancias sustantivas. **Ambas fuentes son consistentes entre sí.**
3. **Discrepancia en el cálculo de volumen de la fuente (hallazgo importante)**: La hoja `V aforado` del .xls trae un volumen mensual ya calculado por la fuente original. Al comparar ese volumen reportado contra el volumen recalculado en este dataset (ver fórmula arriba), se encontraron **10 meses de febrero en años bisiestos** (1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004) con diferencias de entre 2.79 y 28.51 MMC. La causa identificada: **la fuente original usa 28 días fijos para febrero en todos los años**, sin ajustar por año bisiesto (el encabezado de la hoja fija "28" como número de días de febrero para toda la serie). Este dataset **recalculó el volumen de febrero usando 29 días reales en los años bisiestos**, tal como exige el protocolo del proyecto. **El volumen aquí publicado (`volumen_socsi_mmc`) es el recalculado correctamente, no el que aparece literalmente en la hoja fuente `V aforado`.**
4. **Continuidad temporal**: sin meses faltantes en el rango 1964-08 a 2005-07 (492/492).
5. **Valores negativos**: ninguno encontrado (caudal siempre ≥ 0), consistente con lo físicamente esperable.
6. **Valores atípicos (IQR por mes calendario)**: se identificaron 24 meses fuera del rango intercuartílico de su mes calendario correspondiente (p. ej. enero 1970 = 278.48 m³/s, marzo 1972 = 368.25 m³/s, noviembre 1982 y 1984 con valores muy altos). Dado el fuerte régimen estacional del río Cañete (avenidas de verano austral, posible influencia de eventos El Niño en años como 1972-73, 1982-83), **se interpretan como extremos hidrológicos reales y no como errores de digitación**, ya que corresponden a los meses de avenida (Dic-Abr) y son coherentes entre las dos fuentes cruzadas. No se han corregido ni eliminado.
7. **Valores marcados como "corregidos"/"completados" en la fuente**: no se encontró ningún marcado explícito de este tipo en las hojas `Q aforado` / `V aforado` ni en el Anexo 1 del .doc. Si en el estudio original (PDF, sección 2.6 "Análisis de consistencia de caudales - Estación Socsi") se describen correcciones a la serie, **no fueron extraídas ni aplicadas en esta entrega** porque el alcance acordado fue el cruce del .xls con el Anexo 1 del .doc únicamente.
8. **Limitaciones conocidas**:
   - No se incorporó aún el Cuadro 5.2 del PDF (244 pág.), que podría contener la misma serie u otra versión con ajustes de consistencia — pendiente de revisión si se solicita.
   - El "año hidrológico" fue asumido como Ago(año N) a Jul(año N+1), tal como lo etiquetan ambas fuentes; no hay ambigüedad en este caso porque los nombres de mes están explícitos en las columnas.

## V. Dominio espacial y coordenadas

| Estación | Latitud | Longitud | Altitud | Fuente |
|---|---|---|---|---|
| Socsi | 13°00' S | 76°10' W | 350 msnm | Consistente entre Fuente A (.xls) y Fuente B (.doc); coincide también con Cuadro N°1.4.1 del PDF (Fuente C) |

- **Coordenadas decimales (WGS84)**: 13.000° S, 76.167° W *(conversión de 76°10' a decimal; los documentos no especifican los segundos, por lo que este valor tiene una precisión aproximada de ~1.8 km en longitud)*.
- **Bounding box recomendado para extracción GRACE-FO Mascon** (margen 0.5° sobre la estación): 
  - Lat: -13.500° a -12.500°
  - Lon: -76.667° a -75.667°
- No se detectaron discrepancias de coordenadas entre las tres fuentes para esta estación.

---

## Resumen ejecutivo

**Completitud**: 100% (492/492 meses, ago-1964 a jul-2005).

**Tabla de alertas de calidad**

| Alerta | Severidad | Detalle |
|---|---|---|
| Volumen de la fuente no ajustado por año bisiesto | 🟡 Media | Corregido en este dataset; ver nota IV.3. El valor de la fuente original difiere hasta en 28.51 MMC en febreros bisiestos. |
| 24 meses con caudal fuera de rango IQR mensual | 🟢 Baja (interpretados como extremos reales) | Ver nota IV.6. No se modificó ningún valor. |
| Discrepancia en periodo de operación declarado vs. serie de datos | 🟡 Media | El PDF (Cuadro 1.4.1) declara 1965-2000; los datos cubren 1964-2005. No resuelto, reportado para tu decisión. |
| Sin marcas de "corregido"/"completado" en fuente para este tramo | 🟢 Informativo | No aplica ajuste adicional. |

**Alcance y limitaciones de esta entrega**:
- Cubre únicamente **Estación Socsi**, variables caudal y volumen, cruzando el `.xls` de Cuenca Media con el Anexo 1 del `.doc` (PROFODUA 2006).
- **No incluye** aún el Cuadro 5.2 y Anexo 6.2 del PDF (244 pág.), pendientes de tu confirmación si se quiere una tercera fuente de contraste.
- **No incluye** precipitación, evapotranspiración ni nivel freático (fuera del alcance acordado para esta entrega; nivel freático no está disponible en ninguna fuente subida).

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `cañete_caudales.csv` a `canete_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `cañete_caudales_metadata.md` a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
