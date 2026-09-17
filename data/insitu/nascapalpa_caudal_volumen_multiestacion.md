# Metadata — Metadata e Informe Técnico: Datasets Hidrológicos Multiestación (Sistemas Nasca y Palpa, 1984–2005)

## I. Información general

* **Nombre de archivos de datos:** 
  * `caudal_volumen_sistemas_nasca_palpa_1984_2005.csv` (Dataset consolidado de caudales y volúmenes)
* **Ámbito geográfico:** Cuencas hidrográficas de los sistemas **Nasca** y **Palpa** (pertenecientes a la vertiente del Pacífico y al sistema mayor del Río Grande), Departamento de Ica, Perú.
* **Resolución temporal:** Mensual.
* **Periodo de registro:** Enero de 1984 a Diciembre de 2005 ($N = 264$ registros mensuales cronológicos por estación).
* **Formato temporal:** Columna `date` en formato `YYYY-MM-DD` (fijado estrictamente al día 01 de cada mes).
* **Porcentaje de completitud global:**
  * **Estaciones con 100.0% de completitud (0.0% de vacíos):** *Ingenio*, *Aja*, *Las Trancas*, *Tierras Blancas*, *Taruga*, *Chauchilla*, *Socos*, *Grande* (Est. La Isla), *Viscas* (Est. La Peña), *Palpa* (Est. Casa Blanca) y *Sta. Cruz* (Est. La Peña). Estas series no presentan interrupciones cronológicas, incorporando ceros hidrológicos reales en periodos de estiaje hiperárido.
  * **Estación con baja completitud (27.3% de datos disponibles / 72.7% faltantes `NA`):** *Urupalla*, debido a vacíos severos de aforo en la fuente original.

---

## II. Fuentes de datos originales

* **Archivo principal de datos tabulares:** `Promedios Mensuales Ríos Nasca-Palpa 1968-2005 v2.xls` (Hojas institucionales dedicadas a cada estación fluvial). Proporcionó las series cronológicas mensuales de caudal medio observado (1984–2005).
* **Documentos de soporte y contexto técnico:**
  * *ANEXO 1 HIDROL - NAZCAv2-IF.doc*: Programa de Formalización de Derechos de Uso de Agua (PROFODUA, INRENA, Setiembre 2006). Aportó pruebas de ajuste estadístico (Smirnov-Kolmogorov) y validación de parámetros distribucionales.
  * *Anexo II - Demandas Nazca V2-IF.doc*: Propuesta de Asignación de Aguas, Valle de Nasca, Informe Final (2006). Aportó salidas del modelo CropWat 4.3, requerimientos hídricos y estructura de bloques de riego.
* **Entidad emisora / Responsable institucional:** Administración Local del Agua (ALA) / ATDR Palpa-Nasca y Junta de Usuarios de Palpa y Nasca.

---

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `caudal_ingenio_m3s` | `caudal_ingenio_m3s` |
| `volumen_ingenio_mmc` | `volumen_ingenio_mmc` |
| `caudal_aja_m3s` | `caudal_aja_m3s` |
| `volumen_aja_mmc` | `volumen_aja_mmc` |
| `caudal_lastrancas_m3s` | `caudal_lastrancas_m3s` |
| `volumen_lastrancas_mmc` | `volumen_lastrancas_mmc` |
| `caudal_tierrasblancas_m3s` | `caudal_tierrasblancas_m3s` |
| `volumen_tierrasblancas_mmc` | `volumen_tierrasblancas_mmc` |
| `caudal_taruga_m3s` | `caudal_taruga_m3s` |
| `volumen_taruga_mmc` | `volumen_taruga_mmc` |
| `caudal_chauchilla_m3s` | `caudal_chauchilla_m3s` |
| `volumen_chauchilla_mmc` | `volumen_chauchilla_mmc` |
| `caudal_socos_m3s` | `caudal_socos_m3s` |
| `volumen_socos_mmc` | `volumen_socos_mmc` |
| `caudal_urupalla_m3s` | `caudal_urupalla_m3s` |
| `volumen_urupalla_mmc` | `volumen_urupalla_mmc` |
| `caudal_grande_m3s` | `caudal_grande_m3s` |
| `volumen_grande_mmc` | `volumen_grande_mmc` |
| `caudal_viscas_m3s` | `caudal_viscas_m3s` |
| `volumen_viscas_mmc` | `volumen_viscas_mmc` |
| `caudal_palpa_m3s` | `caudal_palpa_m3s` |
| `volumen_palpa_mmc` | `volumen_palpa_mmc` |
| `caudal_santacruz_m3s` | `caudal_santacruz_m3s` |
| `volumen_santacruz_mmc` | `volumen_santacruz_mmc` |

---

| Columna | Descripción | Unidad | Fuente (Medido / Calculado) | Fórmula / Método |
| :--- | :--- | :--- | :--- | :--- |
| `date` | Fecha del registro mensual | - | Estándar temporal | `YYYY-MM-01` |
| `caudal_[estacion]_m3s` | Caudal medio mensual del río | $	ext{m}^3/	ext{s}$ | Medido | Registros oficiales de aforo de la ATDR |
| `volumen_[estacion]_mmc` | Volumen mensual escurrido | $	ext{MMC}$ (Millones de $	ext{m}^3$) | Calculado | $V = Q_{	ext{prom}} 	imes 2.592 	imes 10^6 / 10^6$ (Asumiendo 30 días/mes; redondeado a 2 decimales) |

**Listado de estaciones y sufijos normalizados (`[estacion]`):**
* `ingenio` (Río Ingenio)
* `aja` (Río Aja)
* `lastrancas` (Río Las Trancas)
* `tierrasblancas` (Río Tierras Blancas)
* `taruga` (Río Taruga)
* `chauchilla` (Quebrada Chauchilla)
* `socos` (Río Socos)
* `urupalla` (Río Urupalla)
* `grande` (Río Grande - Estación La Isla)
* `viscas` (Río Viscas - Estación La Peña)
* `palpa` (Río Palpa - Estación Casa Blanca)
* `santacruz` (Río Santa Cruz - Estación La Peña)

---

## IV. QA/QC

1. **Transformaciones y Cálculos:** Los volúmenes mensuales se derivaron directamente de los caudales medios mensuales multiplicando por el factor de conversión volumétrica estándar ($2.592 	imes 10^6	ext{ segundos}$ por mes teórico de 30 días, expresado en Millones de Metros Cúbicos).
2. **Ceros Físicos vs. Vacíos (`NA`):** 
   * Los valores de $0.00	ext{ m}^3/	ext{s}$ corresponden a estiajes extremos característicos de cuencas costeras hiperáridas y se conservan como datos reales de cero escurrimiento.
   * Las celdas sin información en la fuente original se han etiquetado formalmente como `NA` (sin celdas vacías en el CSV).
3. **Control de Calidad (QA/QC):** Se validó la ausencia de valores negativos imposibles y la consistencia matemática estricta entre la columna de caudal y su respectivo volumen volumétrico. No se detectaron valores atípicos espurios derivados de errores tipográficos en las series principales de 1984–2005.

---

## V. Dominio espacial y coordenadas

* **Ubicación general:** Vertiente del Pacífico, sistemas hidrográficos interconectados de Nasca y Palpa en el sur del Departamento de Ica.
* **Bounding Box recomendado para extracción GRACE-FO Mascon:** 
  Considerando la dispersión espacial de las estaciones de control y aplicando el margen operativo estándar de **0.5°** alrededor de la red hidrográfica:
  * **Latitud Mínima:** `-16.0°` | **Latitud Máxima:** `-13.5°`
  * **Longitud Mínima:** `-76.0°` | **Longitud Máxima:** `-73.5°`
* **Directriz sobre discrepancias:** En cumplimiento con las reglas del proyecto, cualquier posible ambigüedad menor en coordenadas puntuales o altitudes reportadas de forma cruzada en los documentos anexos se documenta de forma literal sin realizar interpolaciones ni selecciones arbitrarias.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `nasca_caudales.csv` a `nascapalpa_caudal_volumen_multiestacion.csv`.
- Metadata consolidada y reformateada desde `nasca_caudales_metadata.md` a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
