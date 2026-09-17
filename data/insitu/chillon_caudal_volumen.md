# Metadata — METADATOS DEL DATASET SIMPLIFICADO DE CAUDALES - RÍO CHILLÓN

## I. Información general

Nombre del Archivo: Caudales_Chillon_PteMagdalena_Simplified.csv
Ámbito Geográfico: Cuenca del Río Chillón (parte media y baja), Provincias de Canta y Lima, Región Lima, Perú.
Resolución Temporal: Mensual.
Periodo de Registro: Agosto de 1956 a Julio de 2004 (48 años hidrológicos).
Propósito: Proveer una serie de tiempo continua, estandarizada y optimizada para la evaluación del balance hídrico, estudios de disponibilidad y validación de anomalías de almacenamiento total de agua (TWS) de misiones satelitales como GRACE.

## II. Fuentes de datos originales

- Documentos de Origen: 
  * "TEXTOCHILLON2_2.doc" (Informe Final: Propuesta de Asignación de Agua en Bloques - Valle del Río Chillón, INRENA - IRH - PROFODUA, Diciembre 2004).
  * "ESTUDIO HIDROLOGICO_CHILLON_2.pdf" (Estudio Integral de los Recursos Hídricos de la Cuenca del Río Chillón, INRENA, Octubre 2003).
- Sección Base: Cuadro 2.1 - Descargas medias mensuales en el Río Chillón - Estación Pte. Magdalena.
- Operadores Históricos: 
  * Servicio Nacional de Meteorología e Hidrología - SENAMHI (1948 - 1983).
  * Junta de Usuarios del SubDistrito de Riego Chillón N° 31 (1983 - 2003).

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Date` | `date` |
| `Q_chillon_m3s` | `caudal_chillon_m3s` |
| `Q_chillon_MMC` | `caudal_chillon_mmc` |

---

El dataset contiene las siguientes columnas principales (adaptables según conversión):
1. Date (Formato YYYY-MM-DD): 
   Fecha estandarizada que representa el mes de medición (el día se fija en el "01" para facilitar el indexado en softwares de series de tiempo como Pandas o xarray).
2. Q_PteMagdalena_m3s (Numérico, Float): 
   Caudal medio mensual registrado en la Estación Puente Magdalena. Expresado en metros cúbicos por segundo (m3/s).
3. Q_PteMagdalena_MMC (Numérico, Float): 
   Volumen superficial escurrido mensual. Expresado en Millones de Metros Cúbicos (MMC). (Calculado a partir de Q_PteMagdalena_m3s * segundos del mes / 1,000,000).

## IV. QA/QC

- Extracción y Digitalización: Los registros originales fueron extraídos mediante transcripción manual ("Data Entry") desde una tabla incrustada como objeto OLE (imagen) en el documento fuente original.
- Alteraciones Antrópicas (Régimen Alterado): 
  * Aportes Regulados: Entre los meses de septiembre y noviembre, los caudales incluyen el desembalse de las lagunas reguladas en la parte alta (Chuchón, Leoncocha y Azulcocha), representando un aporte neto aproximado de 8.2 MMC en dicho periodo.
  * Extracciones y Retornos: El caudal medido en esta estación refleja las extracciones aguas arriba y los aportes por aguas de retorno o afloramientos inducidos por el riego.
- Simplificación: Se estructuró en formato tabular de panel largo (Long Format) eliminando cabeceras combinadas o años hidrológicos en texto, dejándolo listo para ingesta en Python, R o MATLAB.

## V. Dominio espacial y coordenadas

Para la extracción de la señal satelital en productos grillados (ej. GRACE / GRACE-FO NetCDF), se define la siguiente caja delimitadora (Bounding Box) que encapsula la gradiente altitudinal de la cuenca del río Chillón, desde la Cordillera de la Viuda hasta el Océano Pacífico:
1. Bounding Box Recomendado (Grados Decimales):
   - Latitud:  [-12.0 , -11.2] (Sur)
   - Longitud: [-77.2 , -76.3] (Oeste)
2. Coordenadas de Estaciones de Control Hidrométrico:
   - Estación Puente Magdalena (950 msnm - Valle Bajo/Medio): Lat -11.700 (11°42' S), Lon -76.850 (76°51' W)
   - Estación Obrajillo (2440 msnm - Valle Medio/Alto): Lat -11.450 (11°27' S), Lon -76.617 (76°37' W)
   - Estación Pariacancha (3800 msnm - Cabecera): Lat -11.383 (11°23' S), Lon -76.517 (76°31' W)
3. Celdas Exactas Recomendadas para GRACE (Centroides 0.5° x 0.5°):
   Para capturar la dinámica de transporte de masa de la cuenca, incluyendo la recarga en las partes altas y la intensa extracción de aguas subterráneas (aprox. 18.5 MMC/año para uso poblacional en el cono norte), se recomienda extraer los datos utilizando los siguientes centroides espaciales:
   - lats_chillon = [-11.75, -11.25]
   - lons_chillon = [-77.25, -76.75]

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `chillon_caudales.csv` a `chillon_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `chillon_caudales_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.

**Contenido adicional no clasificado de la fuente original** (preservado para no perder información):

================================================================================
METADATOS DEL DATASET SIMPLIFICADO DE CAUDALES - RÍO CHILLÓN
================================================================================
