# Metadata — METADATOS DEL DATASET SIMPLIFICADO DE CAUDALES - RÍO SAN JUAN (CHINCHA)

## I. Información general

Nombre del Archivo: Caudales_SanJuan_Conta.csv
Ámbito Geográfico: Cuenca del Río San Juan (Valle de Chincha), Región Ica (y parte alta en Huancavelica), Perú.
Resolución Temporal: Mensual.
Periodo de Registro: Enero de 1934 a Diciembre de 2003 (70 años continuos).
Propósito: Proveer una serie de tiempo continua, estandarizada en caudales (m3/s) y volúmenes (MMC), optimizada para la evaluación del balance hídrico, modelamiento de disponibilidad y validación de anomalías de almacenamiento total de agua (TWS) de misiones satelitales (GRACE).

## II. Fuentes de datos originales

- Documentos de Origen: 
  * "Caudales San Juan.XLS" (Contiene las series aforadas y naturalizadas).
  * "Calculo Disponibilidad Hidricaf.xls" (Aportes de lagunas y aguas subterráneas).
  * Informes de Evaluación y Ordenamiento de los Recursos Hídricos de la Cuenca del Río San Juan y Pisco (MINAG - INRENA, 2003-2004).
- Secciones Base: Hojas 'Q Aforado' y 'Q Naturalizado'.
- Operadores Históricos: 
  * Servicio Nacional de Meteorología e Hidrología (SENAMHI).
  * Administración Técnica del Distrito de Riego (ATDR) Chincha-Pisco.
  * Junta de Usuarios del SubDistrito de Riego San Juan.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Date` | `date` |
| `Q_Aforado_m3s` | `caudal_aforado_m3s` |
| `Vol_Aforado_MMC` | `volumen_aforado_mmc` |
| `Q_Naturalizado_m3s` | `caudal_naturalizado_m3s` |
| `Vol_Naturalizado_MMC` | `volumen_naturalizado_mmc` |

---

El dataset contiene las siguientes 5 columnas:
1. Date (Formato YYYY-MM-DD): 
   Fecha estandarizada que representa el mes de medición (el día se fija en el "01" para facilitar el indexado en softwares de series de tiempo).
2. Q_Aforado_m3s (Numérico, Float): 
   Caudal medio mensual observado/aforado en la estación Conta. Expresado en metros cúbicos por segundo (m3/s).
3. Vol_Aforado_MMC (Numérico, Float): 
   Volumen superficial escurrido mensual correspondiente al caudal aforado. Expresado en Millones de Metros Cúbicos (MMC).
4. Q_Naturalizado_m3s (Numérico, Float): 
   Caudal medio mensual restituido a régimen natural (sin la alteración de las lagunas reguladas). Expresado en metros cúbicos por segundo (m3/s).
5. Vol_Naturalizado_MMC (Numérico, Float): 
   Volumen superficial escurrido mensual en régimen natural. Expresado en Millones de Metros Cúbicos (MMC).

## IV. QA/QC

- Conversión Física: La transformación de caudales (m3/s) a volúmenes (MMC) se realizó multiplicando el caudal mensual por el número exacto de segundos correspondientes a cada mes calendario (tomando en cuenta años bisiestos).
- Naturalización (Régimen Alterado): El río San Juan tiene un régimen intermitente (con descargas concentradas de Enero a Abril). En la época de estiaje (Agosto a Diciembre), los caudales aforados incluyen el aporte regulado de trasvases e infraestructura de almacenamiento (Lagunas Turpo, Obispo, Ñuñunga, Huichinga en la cuenca propia, y Huarmicocha, Chuncho, Canya por trasvase del Mantaro). La serie "Naturalizada" descuenta estos aportes para reflejar la escorrentía pura.
- Limpieza: Se corrigieron las cabeceras desestructuradas y se consolidó el formato a "Long Panel" (Panel Largo), listo para ingesta programática.

## V. Dominio espacial y coordenadas

Para la extracción de la señal satelital en productos grillados (ej. GRACE NetCDF), se define la siguiente caja delimitadora (Bounding Box) que encapsula la gradiente altitudinal de la cuenca del río San Juan y el valle de Chincha:
1. Bounding Box Recomendado (Grados Decimales):
   - Latitud:  [-13.7 , -13.0] (Sur)
   - Longitud: [-76.3 , -75.3] (Oeste)
2. Coordenadas de Estación de Control Hidrométrico:
   - Estación Conta (Punta de Diamante) (320 msnm - Cabecera del Valle de Chincha, Distrito Alto Larán): 
     Latitud: -13.450° (13º 27' S)
     Longitud: -75.966° (75º 58' W)
     *Nota: Las coordenadas en el documento original presentaban un error tipográfico (latitud y longitud invertidas), las cuales han sido corregidas en esta metadata para reflejar su ubicación real en Perú.
3. Celdas Exactas Recomendadas para GRACE (Centroides 0.5° x 0.5°):
   Para capturar la dinámica completa de transporte de masa de la cuenca (desde la recarga altoandina hasta la extracción intensiva de aguas subterráneas en Chincha Baja, El Carmen y Alto Larán), se recomienda extraer los datos utilizando los siguientes centroides espaciales:
   - lats_chincha = [-13.75, -13.25]
   - lons_chincha = [-76.25, -75.75]

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `chincha_caudales_sanjuan_conta.csv` a `chincha_sanjuan_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `chincha_caudales_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.

**Contenido adicional no clasificado de la fuente original** (preservado para no perder información):

================================================================================
METADATOS DEL DATASET SIMPLIFICADO DE CAUDALES - RÍO SAN JUAN (CHINCHA)
================================================================================
