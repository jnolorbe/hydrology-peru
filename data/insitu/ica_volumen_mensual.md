# Metadata — Volumen Mensual, Río Ica / Sistema Choclococha (Estación La Achirana)

## I. Información general

- **Archivo de datos:** `ica_volumen_mensual.csv`
- **Cuenca:** Cuenca integral del río Ica (incluye trasvase del Sistema Choclococha).
- **Estación de medición:** "La Achirana" (Estación Hidrométrica).
- **Resolución temporal:** Mensual.
- **Periodo cubierto:** Enero 1922 a Diciembre 2005 (84 años, 1 008 meses, sin huecos de mes).
- **Naturaleza:** volumen derivado matemáticamente del caudal diario (`ica_caudal_diario.csv`), no proviene de una tabla fuente independiente; se validó contra la columna "RESUMEN ANUAL (m3)" que el documento original imprime en cada cuadro anual.

## II. Fuentes de datos originales

- Mismo documento fuente que `ica_caudal_diario.csv`: `ANEXO_1_Qdiarios_Ica.doc` (ATDR Ica / Junta de Usuarios Distrito de Riego Ica). Ver esa metadata para el detalle completo del pipeline de extracción (OCR + visión por computadora sobre 91 imágenes WMF).
- El volumen mensual se calculó como Q_medio_mes (m³/s) × días_del_mes × 86 400 / 1×10⁶, usando solo los días con dato disponible ese mes.

## III. Diccionario de variables

| Columna | Unidad | Descripción |
|---|---|---|
| `date` | - | Primer día del mes calendario (`YYYY-MM-DD`) |
| `volumen_rio_ica_achirana_mmc` | MMC | Volumen mensual del río Ica |
| `volumen_sistema_choclococha_achirana_mmc` | MMC | Volumen mensual del aporte del Sistema Choclococha |
| `dias_con_dato_rio_ica` | días | N° de días del mes con dato válido de Río Ica, usados para calcular el volumen de ese mes |
| `dias_con_dato_choclococha` | días | Ídem, para Sistema Choclococha |
| `dias_calendario_mes` | días | N° de días calendario del mes (28-31, considerando bisiestos) |

## IV. QA/QC

- **Interpretación de `dias_con_dato_*`:** un volumen mensual calculado con pocos días de dato (p. ej. 3 de 31) es estadísticamente poco representativo del mes completo. Se recomienda filtrar o ponderar por estas columnas antes de comparar contra series continuas como TWS de GRACE-FO, en vez de asumir igual confiabilidad para todos los meses.
- Mismas validaciones cruzadas y filtro de sanidad física que la serie diaria (ver `ica_caudal_diario.md`, sección IV), heredadas por derivarse de la misma fuente.
- **Archivos de soporte QA** (anexos, no forman parte de este CSV): `ica_qa_caudal_discrepancias_estadisticos.csv`, `ica_qa_caudal_valores_eliminados_sanidad.csv`, `ica_qa_caudal_anios_duplicados.json`.

## V. Dominio espacial y coordenadas

- **Estación La Achirana, río Ica:** Latitud -14.0833°, Longitud -75.7333°, Altitud 398 msnm, Provincia/Distrito Ica-Ica.
- **Bounding box:** punto único; cuenca integral del río Ica ≈ 13°10'-14°53'S y 75°01'-75°54'W (8 103 km²).

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Renombrado desde `volumen_mensual_rio_ica_achirana.csv` (sin cambios de columnas ni de contenido).
- Complementa a `ica_caudal_diario.csv`: juntos reemplazan al archivo híbrido `ica_caudal.csv` (retirado), que mezclaba resolución diaria y mensual en un solo archivo con valores de volumen repetidos en cada día del mes.
- Metadata adaptada desde `ica_caudal_metadata.txt`, separando el contenido relevante a la resolución mensual.
