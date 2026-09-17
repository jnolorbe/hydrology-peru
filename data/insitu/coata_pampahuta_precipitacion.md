# Metadata — Auditoría y Metadata del Dataset Hidrológico — Precipitación Estación Pampahuta

## I. Información general

* **Nombre de archivo:** `precipitacion_pampahuta_mm.csv`
* **Ámbito geográfico:** Cuenca del río Coata (Subcuenca Paratía / Cuenca Alta)
* **Departamento/Región:** Puno, Perú
* **Resolución temporal:** Mensual (formato `YYYY-MM-DD`, con día fijo en `01`)
* **Periodo de registro:** Enero de 1962 a diciembre de 2006 (45 años / 540 registros mensuales)
* **Desfase respecto al año calendario:** Ninguno (Año hidrológico estándar de enero a diciembre, con periodo húmedo concentrado de noviembre a marzo)
* **Porcentaje de completitud:** 100% (completado mediante factores adimensionales y modelos de extensión de series según el protocolo técnico de INRENA)

## II. Fuentes de datos originales

* **Documento principal:** Reporte Técnico Volumen I: *Evaluación de los Recursos Hídricos en las Cuencas de los Ríos Cabanillas y Lampa*.
* **Entidad emisora:** Ministerio de Agricultura, Instituto Nacional de Recursos Naturales (INRENA), Intendencia de Recursos Hídricos, Administración Técnica del Distrito de Riego Juliaca (ATDR Juliaca).
* **Año de publicación:** Diciembre 2007 (Publicación oficial / Enero 2008).
* **Aporte específico de la fuente:** Tablas de precipitación total mensual histórica, climatología multianual (Tabla 3.5), precipitaciones máximas en 24 horas (Tabla 3.7) y validación de consistencia para la estación pluviométrica Pampahuta (Código SENAMHI: CO.115027).

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `precipitacion_pampahuta_mm` | `precipitacion_pampahuta_mm` |

---

* `date`: Fecha de registro mensual en formato `YYYY-MM-DD` (primer día del mes correspondiente). Tipo: Temporal.
* `precipitacion_pampahuta_mm`: Precipitación total mensual registrada y/o completada en la estación Pampahuta, expresada en milímetros ($	ext{mm}$). Tipo: Numérico continuo. Fuente: Registros instrumentales de campo validados por INRENA y completados mediante factor adimensional mensual ($k$).

## IV. QA/QC

* **Transformaciones aplicadas:** Completación de valores ausentes puntuales utilizando factores adimensionales mensuales ($k$) derivados del promedio multianual de años completos con registros consistentes.
* **Valores marcados/corregidos en la fuente:** La serie pasó por un análisis gráfico de consistencia (histogramas), pruebas de doble masa (Bloque II con estación master Pampahuta) y pruebas estadísticas de saltos y tendencias (T de Student y F de Fisher al 95% de confianza), sin rechazo de estabilidad estadística.
* **Valores atípicos y su interpretación:** Los valores máximos se concentran estrictamente en el verano austral (diciembre a marzo), lo cual responde a la estacionalidad climática natural del Altiplano. No se detectaron valores negativos físicamente imposibles.
* **Limitaciones conocidas:** Los registros históricos anteriores a 1965 poseen menor densidad de control instrumental cruzado en la cabecera, aunque la estación Pampahuta destaca por presentar alta consistencia dentro de su bloque.

## V. Dominio espacial y coordenadas

* **Ubicación de la estación (según INRENA, Tablas 2.2):**
  * Latitud Sur: $15^\circ 29' 00.7''$ ($-15.4835^\circ$)
  * Longitud Oeste: $70^\circ 40' 32.8''$ ($-70.6758^\circ$)
  * Altitud: $4,400	ext{ msnm}$
  * Ubicación política: Departamento Puno, Provincia Lampa, Distrito Paratía.
* **Bounding Box recomendado para extracción GRACE-FO Mascon (margen $0.5^\circ$ sobre la estación):**
  * Latitud Superior (Norte): $-14.9835^\circ$
  * Latitud Inferior (Sur): $-15.9835^\circ$
  * Longitud Oeste: $-71.1758^\circ$
  * Longitud Este: $-70.1758^\circ$
* **Discrepancias de coordenadas:** No se registran conflictos tipográficos ni discrepancias entre las tablas del informe y los anexos cartográficos para esta estación.

---

### Alertas de calidad y severidad
* **Completitud global:** 100% (540/540 meses disponibles).
* **Severidad de alertas:** Nula. La serie de la estación Pampahuta no reporta quiebres significativos en las pruebas de doble masa ni rechazo en las pruebas de estabilidad estadística de medias y variancias.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `lampa_precipitacion_pampahuta.csv` a `coata_pampahuta_precipitacion.csv`.
- Metadata consolidada y reformateada desde `lampa_precipitacion_metadata.md` a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
