# Metadata — METADATOS DEL DATASET DE CAUDALES MULTIESTACIÓN - CUENCA DEL RÍO URUBAMBA (CUSCO)

## I. Información general

Nombre del Archivo: cusco_caudales.csv
Ámbito Geográfico: Cuenca del río Urubamba (ríos Vilcanota y Mapacho), Región Cusco,
Perú.
Resolución Temporal: Mensual.
Periodo de Registro: Enero de 1964 a Diciembre de 2008 (45 años calendario, 540
registros). Cobertura real varía por estación (ver sección IV).
Propósito: Proveer una serie de tiempo continua y multiestación de caudales medios
mensuales, estandarizada en m3/s y en volumen (MMC), para análisis de oferta hídrica
superficial, calibración de modelos lluvia-escurrimiento y balance hídrico de la
cuenca del Urubamba.

## II. Fuentes de datos originales

- Documento de Origen: "Hidrologia_Urubamba_Volumen_II (Anexo)" — Anexo de datos del
  "Estudio Hidrológico de la Cuenca del Río Urubamba", Administración Local de Agua
  (ALA) Cusco / Autoridad Nacional del Agua (ANA).
- Sección Base: tablas "Estación de Aforo Puente Pisac", "Estación de Aforo
  Hidroeléctrica Machupicchu" y "Estación de Aforo Puente Paucartambo" — series
  históricas crudas (año x mes), no las tablas de módulos/percentiles (QM, Q50, Q75,
  Q95) que aparecen en el Volumen I (Memoria) del mismo estudio.
- Operadores históricos: SENAMHI (estaciones Pisac y Paucartambo) y EGEMSA — Empresa
  de Generación Eléctrica Machupicchu (estación de la bocatoma de la Hidroeléctrica
  Machupicchu).
- Nota: el estudio identifica una cuarta estación relevante sobre el río Mapacho,
  "Puente Chacllabamba" (registro discontinuo 2002-2008), pero su serie cruda
  mes-a-mes no fue localizada en el Anexo disponible — solo se encontraron sus
  estadísticos procesados (módulos QM/Q50/Q75/Q95) en el Volumen I. Por eso no forma
  parte de este dataset; queda pendiente si se logra ubicar su tabla fuente.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Date` | `date` |
| `Q_Pisac_m3s` | `caudal_pisac_m3s` |
| `Q_Pisac_MMC` | `caudal_pisac_mmc` |
| `Q_Machupicchu_m3s` | `caudal_machupicchu_m3s` |
| `Q_Machupicchu_MMC` | `caudal_machupicchu_mmc` |
| `Q_Paucartambo_m3s` | `caudal_paucartambo_m3s` |
| `Q_Paucartambo_MMC` | `caudal_paucartambo_mmc` |

---

El dataset contiene 7 columnas, en formato ancho (una fila por mes, una columna por
estación):
1. Date (Formato YYYY-MM-DD):
   Fecha estandarizada que representa el mes de medición (el día se fija en el "01").
2. Q_Pisac_m3s / Q_Pisac_MMC (Numérico, Float):
   Caudal medio mensual y volumen mensual en la Estación Puente Pisac, río Vilcanota
   (parte alta/media de la cuenca, área de drenaje 7,047.4 km2).
3. Q_Machupicchu_m3s / Q_Machupicchu_MMC (Numérico, Float):
   Caudal medio mensual y volumen mensual en la Estación Hidroeléctrica Machupicchu,
   río Vilcanota (parte media de la cuenca, área de drenaje 9,659.7 km2; ubicada
   antes de la captación de la C.H. Machupicchu, localidad de Aguas Calientes,
   distrito de Santa Teresa, provincia de La Convención).
4. Q_Paucartambo_m3s / Q_Paucartambo_MMC (Numérico, Float):
   Caudal medio mensual y volumen mensual en la Estación Puente Paucartambo, río
   Mapacho (área de drenaje 2,443.1 km2).
Todas las variables de caudal están en metros cúbicos por segundo (m3/s); las de
volumen, en Millones de Metros Cúbicos (MMC).

## IV. QA/QC

- Conversión Física: Volumen_MMC = Caudal_m3s × (días del mes × 86 400 s) /
  1 000 000, con el número exacto de días de cada mes calendario (incluye años
  bisiestos). A diferencia de los datasets de Chillón/Chincha, aquí el año en la
  tabla fuente ya es año calendario (Ene-Dic), no año hidrológico, por lo que no fue
  necesario recomponer la fecha entre dos años.
- Cobertura real por estación (con datos, no solo el rango nominal 1964-2008):
  * Pisac: registro discontinuo — huecos en 1964-1965 y otros meses sueltos;
    documentado en la fuente como "periodo 1966-1985" y "periodo 1987-2008".
  * Machupicchu: la más completa — prácticamente continua 1964-2008 (único hueco
    notable: mayo-diciembre de 2000).
  * Paucartambo: solo tiene datos desde 1995 (la estación no existía antes); registro
    además discontinuo dentro de ese rango, con 2004 y 2005 completamente vacíos.
- Valores vacíos: son datos faltantes reales de la tabla fuente, no errores de
  extracción; se dejaron en blanco (no se interpoló ni se rellenó con promedios).
- Corrección aplicada: la tabla fuente de Machupicchu incluye una columna "PROM" que,
  al verificarla, no corresponde a un promedio mensual real (sus valores son ~10
  veces mayores que el promedio de los 12 meses — posible error de etiquetado en el
  documento original). Esa columna fue descartada por completo; cada Volumen_MMC de
  este dataset se calculó directamente desde el caudal mensual de la fuente, no
  desde esa columna.
- Extracción: tablas leídas con `python-docx` conservando la estructura fila/columna
  original (año en filas, meses en columnas), sin reordenar ni reinterpretar valores.

## V. Dominio espacial y coordenadas

El documento fuente no incluye coordenadas UTM ni lat/lon de las estaciones de aforo
en sí (sí las tiene para las unidades hidrográficas, pero no para los puntos de
control). Las coordenadas siguientes provienen de una fuente externa verificada
(SENAMHI, portal de monitoreo de la cuenca Urubamba/Vilcanota), no del documento de
origen de las series:
1. Estación Pisac (SENAMHI, actual):
   Latitud: -13.428°, Longitud: -71.841°, Altitud: 2,791 msnm.
   Provincia Calca, distrito Pisac. Coincide en nombre y ubicación descriptiva con la
   estación de la serie de este dataset.
2. Estación Paucartambo (SENAMHI, actual):
   Latitud: -13.317°, Longitud: -71.597°, Altitud: 2,900 msnm.
   Provincia y distrito Paucartambo. Coincide en nombre y ubicación descriptiva con
   la estación de la serie de este dataset.
3. Estación cercana a Machupicchu:
   ⚠️ No se encontró una estación SENAMHI actual con el nombre exacto "Machupicchu".
   La más cercana en el mismo portal es "Intihuatana Km105" (Lat -13.174°, Lon
   -72.564°, 1,778 msnm, distrito Machupicchu, provincia Urubamba), pero al ser
   administrada por SENAMHI y no por EGEMSA, no se puede confirmar que sea el mismo
   punto físico que la estación de la bocatoma de la Hidroeléctrica Machupicchu
   usada como fuente de este dataset. No se reporta esta coordenada como la de la
   estación del dataset; se deja como referencia aproximada de la zona únicamente.
4. Referencia de la cuenca: los ríos Vilcanota (curso alto/medio del Urubamba) y
   Mapacho discurren íntegramente dentro de la Región Cusco, entre aproximadamente
   -13.0° y -13.6° de latitud sur en el tramo cubierto por estas tres estaciones.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `cusco_caudales.csv` a `urubamba_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `cusco_caudales_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.

**Contenido adicional no clasificado de la fuente original** (preservado para no perder información):

================================================================================
METADATOS DEL DATASET DE CAUDALES MULTIESTACIÓN - CUENCA DEL RÍO URUBAMBA (CUSCO)
================================================================================
