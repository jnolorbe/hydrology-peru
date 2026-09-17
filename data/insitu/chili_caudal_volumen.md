# Metadata — METADATOS DEL CONJUNTO DE DATOS: CAUDALES MENSUALES DE LA CUENCA DEL RÍO CHILI

## I. Información general

- Nombre del archivo: chilli_caudales_long.csv
- Título del Dataset: Series de Tiempo de Caudales Medios Mensuales Históricos de la Cuenca del Río Chili.
- Resolución Temporal: Mensual.
- Estructura: Formato largo (Long format / Tidy data).
- Idioma: Español.

## II. Fuentes de datos originales

- Documento Fuente: Volumen_Dos.pdf (Anexo A, Cuadros 2-12, 2-13 y tabulados anexos).
- Estudio de Referencia: "Informe Final de los Valles Chili Regulado y Chili No Regulado".
- Entidad: Ministerio de Agricultura / Instituto Nacional de Recursos Naturales (INRENA) - ATDR Chili (Administración Técnica del Distrito de Riego Chili).
- Autor/Compilador Original: Ing. Juan Manuel Oviedo T.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `caudal_m3_s` | `caudal_m3_s` |
| `volumen_mmc` | `volumen_mmc` |

---

1. date
   - Descripción: Fecha correspondiente al registro mensual. Se ha fijado el primer día del mes para estandarizar la serie de tiempo.
   - Tipo de dato: Cadena (String) / Formato Fecha (Date).
   - Formato: YYYY-MM-DD (Estándar ISO 8601).
2. caudal_m3_s
   - Descripción: Caudal medio mensual registrado en la estación o punto de control (principalmente Charcani).
   - Tipo de dato: Numérico continuo (Flotante).
   - Unidad de medida: Metros cúbicos por segundo (m³/s).
3. volumen_mmc
   - Descripción: Volumen mensual escurrido total.
   - Tipo de dato: Numérico continuo (Flotante).
   - Unidad de medida: Millones de Metros Cúbicos (MMC).

## IV. QA/QC

- Transformación de Estructura: Los datos originales tabulados en matriz ancha (Años en filas, Meses en columnas) fueron transpuestos (Melt) a un formato largo para facilitar la ingesta en software estadístico y bases de datos.
- Cálculo de Volúmenes: El volumen (MMC) se derivó del caudal medio mensual multiplicándolo por la cantidad exacta de segundos en cada mes (considerando los 28, 29, 30 o 31 días según correspondiese el año, incluyendo años bisiestos).
- Control de Calidad y Vacíos: Se filtraron años y registros que presentaban celdas en blanco o vacíos en el documento original para evitar errores de tipo `NaN` durante el modelamiento numérico de series continuas.
- Cálculo de Incertidumbre: Para análisis posteriores con estos datos, se hace la acotación matemática rigurosa de que la incertidumbre de cualquier promedio histórico debe determinarse aplicando las leyes de propagación de errores y no mediante el promedio aritmético simple de las incertidumbres individuales.

## V. Dominio espacial y coordenadas

- Área de Estudio: Cuenca del Río Chili, Región Arequipa, Perú.
- Punto de Control Principal: Estación Charcani.
- Coordenadas Referenciales de la Estación Charcani (Aproximadas):
  * Latitud: -16.36 (Sur)
  * Longitud: -71.50 (Oeste)
  * Altitud: ~ 4401 m.s.n.m. (según Cuadro 2-1).
- Bounding Box Regional (Cuenca aproximada):
  * Límite Norte: -15.75
  * Límite Sur: -16.75
  * Límite Este: -71.00
  * Límite Oeste: -72.00

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `chilli_caudales.csv` a `chili_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `chilli_caudales_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.

**Contenido adicional no clasificado de la fuente original** (preservado para no perder información):

=============================================================================
METADATOS DEL CONJUNTO DE DATOS: CAUDALES MENSUALES DE LA CUENCA DEL RÍO CHILI
=============================================================================
