# Metadata — Metadata: Oferta Hídrica (Ríos Moche, Virú, Santa y Chicama)

## I. Información general

* **Nombre del dataset:** `dataset_multiestacion_caudal_volumen.csv`
* **Ámbito geográfico:** Cuencas de los ríos Moche, Virú, Santa y Chicama; Regiones de La Libertad y Áncash, Perú.
* **Resolución temporal:** Mensual.
* **Periodo de registro:** 1956-08-01 al 2004-07-01 (correspondiente a los años hidrológicos 1956/57 hasta 2003/04).
* **Desfase respecto al año calendario:** El año hidrológico reportado inicia convencionalmente en el mes de agosto. Las fechas en la columna `date` fijan el día 01 de cada mes.
* **% de completitud:** 100% (576 meses continuos, 0 valores nulos o vacíos "NA").

## II. Fuentes de datos originales

* **Documento base:** "PROPUESTA DE ASIGNACIONES DE AGUA EN BLOQUE - VOLUMENES ANUALES Y MENSUALES - PARA LA FORMALIZACION DE LOS DERECHOS DE USO DE AGUA EN EL VALLE DE MOCHE - INFORME FINAL".
* **Entidad Emisora:** Ministerio de Agricultura, Instituto Nacional de Recursos Naturales (INRENA), Intendencia de Recursos Hídricos (PROFODUA), Administración Técnica del Distrito de Riego Moche-Virú-Chao.
* **Año de emisión:** Septiembre 2004.
* **Aportes extraídos:**
  * **Estación Quirihuac (Río Moche):** Hoja de cálculo 'Cua-2.1', descargas medias mensuales en m³/s.
  * **Estación Huacapongo (Río Virú):** Hoja de cálculo 'Cua-2.2', descargas medias mensuales en m³/s.
  * **Estación Condorcerro (Río Santa):** Hoja de cálculo 'Cua-2.3', descargas medias mensuales en m³/s.
  * **Estación Salinar (Río Chicama):** Hoja de cálculo 'Cua-2.4 ', descargas medias mensuales en m³/s.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `caudal_quirihuac_m3s` | `caudal_quirihuac_m3s` |
| `volumen_quirihuac_mmc` | `volumen_quirihuac_mmc` |
| `caudal_huacapongo_rio_viru_m3s` | `caudal_huacapongo_rio_viru_m3s` |
| `volumen_huacapongo_rio_viru_mmc` | `volumen_huacapongo_rio_viru_mmc` |
| `caudal_condorcerro_m3s` | `caudal_condorcerro_m3s` |
| `volumen_condorcerro_mmc` | `volumen_condorcerro_mmc` |
| `caudal_salinar_rio_chicama_m3s` | `caudal_salinar_rio_chicama_m3s` |
| `volumen_salinar_rio_chicama_mmc` | `volumen_salinar_rio_chicama_mmc` |

---

| Columna | Descripción | Unidad | Fuente/Método |
| :--- | :--- | :--- | :--- |
| `date` | Fecha del registro mensual (YYYY-MM-DD), fijada al día 01. | Fecha | Parseo de etiquetas de año hidrológico y mes. |
| `caudal_quirihuac_m3s` | Caudal medio mensual del Río Moche en estación Quirihuac. | m³/s | Medido. |
| `volumen_quirihuac_mmc` | Volumen mensual estimado del Río Moche en estación Quirihuac. | MMC | Calculado: $Q \times 2.592$ (asumiendo 30 días/mes). |
| `caudal_huacapongo_rio_viru_m3s` | Caudal medio mensual del Río Virú en estación Huacapongo. | m³/s | Medido. |
| `volumen_huacapongo_rio_viru_mmc` | Volumen mensual estimado del Río Virú. | MMC | Calculado: $Q \times 2.592$ |
| `caudal_condorcerro_m3s` | Caudal medio mensual del Río Santa en estación Condorcerro. | m³/s | Medido. |
| `volumen_condorcerro_mmc` | Volumen mensual estimado del Río Santa. | MMC | Calculado: $Q \times 2.592$ |
| `caudal_salinar_rio_chicama_m3s` | Caudal medio mensual del Río Chicama en estación Salinar. | m³/s | Medido. |
| `volumen_salinar_rio_chicama_mmc` | Volumen mensual estimado del Río Chicama. | MMC | Calculado: $Q \times 2.592$ |

## IV. QA/QC

* **Alertas de Calidad:** Nivel Bajo (óptimo). Las series temporales superaron los test de continuidad cronológica sin requerir interpolaciones artificiales.
* **Correcciones documentadas:** Se identificó y corrigió un error tipográfico de origen en la estructura del documento excel: el ciclo "1982/83" estaba ingresado erróneamente como "1982/53".
* **Análisis de Valores Faltantes y Físicamente Imposibles:** 0% de celdas vacías, 0 valores negativos detectados en la matriz.
* **Valores Atípicos (Outliers):** Se detectaron variaciones intercuartílicas calculadas sobre una base estrictamente mensual para respetar el pulso estacional (ej. Quirihuac=44, Condorcerro=15, Huacapongo=43, Salinar=24). Dichos valores fueron validados como picos hídricos climáticos extremos históricos reales y se mantienen intactos en la serie.
* **Incertidumbre y propagación de errores:** Para cualquier post-procesamiento cruzado o consolidación de estas estaciones hidrológicas con la señal TWSA de GRACE-FO, la obtención de la incertidumbre del promedio histórico se efectuará aplicando rigurosas reglas de propagación matemática de errores, y no simplemente computando el promedio aritmético de las incertidumbres de cada cuenca individual.

## V. Dominio espacial y coordenadas

* **Ubicación de Referencia de Estaciones (según texto original):**
  * **Estación Quirihuac (Río Moche):** Latitud 8° S, Longitud 78° W (aproximación reportada en fuente), Altitud 200 msnm.
  * **Estación Condorcerro (Río Santa):** Distrito de Macate, Provincia de Santa. Altitud 450 msnm.
  * *(Coordenadas exactas en formato decimal WGS84 para Virú y Chicama pendientes de cruce con catastro hidrológico nacional).*
* **Bounding Box Recomendado (Extracción GRACE-FO Mascon):** 
  Con margen de seguridad de 0.5° sobre el gradiente de cuencas costeras:
  * **Latitud:** -7.0° a -9.5° S
  * **Longitud:** -77.5° a -79.5° W

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `moche_caudales.csv` a `mochevirusanta_caudal_volumen_multicuenca.csv`.
- Metadata consolidada y reformateada desde `moche_caudales_metadata.md` a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
