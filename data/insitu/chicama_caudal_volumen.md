# Metadata — METADATOS DEL DATASET DE CAUDALES - CUENCA Y VALLE DE CHICAMA (ESTACIÓN SALINAR)

## I. Información general

Nombre del Archivo: chicama_caudales.csv
Ámbito Geográfico: Cuenca del Río Chicama, Departamento de La Libertad, Perú.
Resolución Temporal: Mensual.
Periodo de Registro: Agosto de 1969 a Julio de 2003 (34 años hidrológicos, 408 registros mensuales).
Propósito: Proveer la serie de caudales mensuales (en m3/s y volúmenes estandarizados en Millones de Metros Cúbicos - MMC) de la Estación Hidrométrica Salinar en el río Chicama, principal punto de aforo y control hidrológico de la cuenca, optimizado para el balance hídrico y la validación de anomalías de almacenamiento total de agua (TWS) de GRACE.

## II. Fuentes de datos originales

- Documentos de Origen: 
  * "CHICAMA.xls" (Informe Final PROFODUA / INRENA - ATDR Chicama, Octubre 2004).
  * "DISPONIBILIDAD HIDRICA SALINAR.xls".
- Secciones Base:
  * Hoja "Q aforado": Anexo 1.1 - Caudal Medio Mensual Histórico Aforado (m3/s) en la Estación Salinar (Periodo 1969/70 - 2002/03).
- Operadores Históricos: SENAMHI, Junta de Usuarios del Sub Distrito de Riego Chicama, Empresa Casa Grande y Proyecto Especial Chavimochic.
- DISPONIBILIDAD HIDRICA SALINAR.xls
- Oferta Hidrométrica (Caudales):
Archivo: DISPONIBILIDAD HIDRICA SALINAR.xls
PDF
Hoja base: Q aforado (Anexo 1.1: Caudal Medio Mensual Histórico Aforado en m3/s de la Estación Salinar, periodo 1969/70–2002/03).  
PDF
Archivo: CHICAMA.xls
DOC
Informe base: "Propuesta de Asignaciones de Agua en Bloque - Cuenca Alta de Chicama (Usquil)" (INRENA / PROFODUA, Octubre 2004).  
DOC
Precipitación Multiestación:
Archivo: PRECIPITACION CHICAMA.xls
PDF
Hojas base: Hojas individuales de las 14 estaciones meteorológicas e hidrométricas de la cuenca (Otuzco, Sinsicap, Contumaza, Asuncion, Capachique, Sunchubamba, Cospan, Campoden, Coina, Callancas, San Benito, Cascas, Tambo, Casa Grande) y hoja de RESUMEN.  
PDF
Archivo: Estudio Hidrologico del Rio Chicama - Pluviometria.pdf (Anexo III: Pluviometría con tablas completas de validación histórica).  
PDF

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Date` | `date` |
| `Q_Salinar_m3s` | `caudal_salinar_m3s` |
| `Q_Salinar_MMC` | `caudal_salinar_mmc` |

---

El dataset contiene las siguientes 3 columnas:
1. Date (Formato YYYY-MM-DD): 
   Fecha estandarizada del mes de registro (fijada en el día 1 de cada mes).
2. Q_Salinar_m3s (Numérico, Float): 
   Caudal medio mensual registrado en la Estación Salinar (Río Chicama), expresado en metros cúbicos por segundo (m3/s).
3. Q_Salinar_MMC (Numérico, Float): 
   Volumen mensual escurrido calculado multiplicando el caudal medio por el número exacto de segundos del mes correspondiente (considerando años bisiestos), expresado en Millones de Metros Cúbicos (MMC).

## IV. QA/QC

- Ciclo Hidrológico: Las series originales están estructuradas bajo el año hidrológico que inicia en Agosto y culmina en Julio. Se reestructuró la secuencia temporal cronológica lineal desde agosto de 1969 hasta julio de 2003.
- Conversión Física: La transformación a MMC se realizó aplicando el factor temporal exacto diario de cada mes calendario.
- Contexto Hidrológico: El sistema de oferta hídrica de la cuenca corresponde a un régimen no regulado propio, midiendo la escorrentía total de la cuenca alta y media antes de su ingreso al valle agrícola.

## V. Dominio espacial y coordenadas

1. Ubicación Precisa de la Estación de Control Principal (Estación Salinar):
   - Río: Chicama
   - Tipo: Limnimétrica
   - Ubicación Política: Departamento de La Libertad, Provincia Ascope, Distrito Ascope.
   - Coordenadas Geográficas: 
     * Latitud:  7° 40' S
     * Longitud: 78° 58' W
   - Altitud: 350 msnm
2. Bounding Box Recomendado para Extracción Satelital (GRACE NetCDF):
   - Latitud:  [-8.10 , -7.20] (Sur)
   - Longitud: [-79.30 , -78.10] (Oeste)

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `chicama_caudales.csv` a `chicama_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `chicama_caudales_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.

**Contenido adicional no clasificado de la fuente original** (preservado para no perder información):

================================================================================
METADATOS DEL DATASET DE CAUDALES - CUENCA Y VALLE DE CHICAMA (ESTACIÓN SALINAR)
================================================================================
