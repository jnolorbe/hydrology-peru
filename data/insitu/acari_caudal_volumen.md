# Metadata — Metadata del Dataset Hidrológico: Cuencas Acarí y Yauca

## I. Información general

* **Nombre del archivo:** `dataset_caudal_volumen_acari_yauca.csv`
* **Ámbito Geográfico:** Cuencas de los Ríos Acarí y Yauca (Departamentos de Arequipa y Ayacucho, Perú).
* **Resolución temporal:** Mensual (agrupado al día 01 de cada mes).
* **Periodo de registro:** Agosto 1960 a Julio 2005 (años hidrológicos 1960/1961 a 2004/2005).
* **Desfase anual:** El año hidrológico inicia en agosto y culmina en julio. 
* **Completitud de la serie:** 100% (540 meses continuos por estación).

## II. Fuentes de datos originales

* **Archivos:** `Oferta y Demanda de Agua Acari.xls`, `ESTUDIO HIDROLOGICO_ACARI.pdf`, `Inventario Superficial Acari.doc`.
* **Entidad emisora / Origen:** Intendencia de Recursos Hídricos - INRENA, basado en el Sistema de Información Hidrológica "SIH" (2004).
* **Aportes de la fuente:**
    * Hoja `Cua-2.1` (.xls): Serie histórica de caudales medios mensuales (m³/s) para la estación Bella Unión (Río Acarí).
    * Hoja `Cua-2.2` (.xls): Serie histórica de caudales medios mensuales (m³/s) para la estación Jaqui (Río Yauca).

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `caudal_bella_union_m3s` | `caudal_bella_union_m3s` |
| `volumen_bella_union_mmc` | `volumen_bella_union_mmc` |
| `caudal_jaqui_m3s` | `caudal_jaqui_m3s` |
| `volumen_jaqui_mmc` | `volumen_jaqui_mmc` |

---

* **`date`**: Fecha de la observación (formato `YYYY-MM-DD`, siempre se usa el primer día del mes).
* **`caudal_bella_union_m3s`**: Caudal medio mensual en la estación Bella Unión, Río Acarí. Unidad: m³/s. Fuente: Medido/Completado.
* **`volumen_bella_union_mmc`**: Volumen mensual escurrido estimado para la estación Bella Unión. Unidad: Millones de Metros Cúbicos (MMC). Fórmula: $V = Q_{promedio} 	imes 2.592$ (asumiendo periodos regulares de 30 días).
* **`caudal_jaqui_m3s`**: Caudal medio mensual en la estación Jaqui, Río Yauca. Unidad: m³/s. Fuente: Medido/Completado.
* **`volumen_jaqui_mmc`**: Volumen mensual escurrido estimado para la estación Jaqui. Unidad: Millones de Metros Cúbicos (MMC). Fórmula: $V = Q_{promedio} 	imes 2.592$.

## IV. QA/QC

* **Alertas de calidad (Severidad Media):** El documento base incluye la nota literal: *"Los valores en negrita son datos faltantes que han sido completados con el promedio mensual multianual"*. Aunque el archivo base se encuentra relleno al 100%, existen meses cuya varianza real ha sido artificialmente aplanada hacia la climatología.
* **Continuidad temporal:** El periodo interanual hidrológico (ej. 60/61) ha sido pivotado y mapeado estrictamente al formato calendario estándar (enero a diciembre).
* **QA/QC - Valores Físicamente Imposibles:** Se registraron **0 valores negativos** para ambas estaciones.
* **QA/QC - Valores Atípicos (Outliers):** Calculados a partir del rango intercuartílico (IQR) evaluando por **mes calendario** para respetar la distribución estacional hidrológica:
    * *Estación Bella Unión:* 17 valores atípicos (3.14% de la serie).
    * *Estación Jaqui:* 22 valores atípicos (4.07% de la serie).
    * *Interpretación:* Estos valores extremos positivos se mantuvieron intactos en el CSV final, asumiéndose como registros reales de avenidas extraordinarias.

## V. Dominio espacial y coordenadas

* **Estación Bella Unión (Río Acarí):** Localizada en la cabecera del valle de Acarí. Según el documento `ESTUDIO HIDROLOGICO_ACARI.pdf`, se ubica en las coordenadas: Latitud **15°27' Sur** (aprox. -15.45°), Longitud **74°38' Oeste** (aprox. -74.633°), Altitud: **70 m.s.n.m.**
* **Estación Jaqui (Río Yauca):** Las coordenadas y altitud exacta no han sido referenciadas en los extractos documentales procesados en esta fase. Queda pendiente su georreferenciación exacta mediante otras fuentes.
* **Bounding Box recomendado para extracción Mascon (GRACE-FO):** Considerando un margen de ~0.5° sobre las estaciones para capturar la cuenca baja e intercuencas, la ventana de extracción base sugerida es entre **14.5°S a 16.0°S** y **73.5°W a 75.2°W**.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `acari_caudales.csv` a `acari_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `acari_caudales_metadata.md` a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
