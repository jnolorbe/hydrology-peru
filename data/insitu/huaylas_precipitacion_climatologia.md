# Metadata — METADATOS DEL DATASET DE PRECIPITACIÓN (75% PERSISTENCIA) - HUARAZ

## I. Información general

Nombre del Archivo: huaraz_precipitacion75.csv
Ámbito Geográfico: Cuenca Alta del Río Santa, Callejón de Huaylas (aplicable a las Comisiones de Regantes Antacocha, San Idelfonso, Rajucolta y Jauna-Olleros).
Departamento del Perú: Ancash.
Resolución Temporal: Mensual.
Periodo de Registro: 1953/2006. Representa un año climatológico sintético ordenado como año hidrológico genérico (Agosto a Julio) con precipitación al 75% de persistencia.

## II. Fuentes de datos originales

- Documentos de Origen: 
  * "Cuadros Elementos Meteorológicos.xls" (Datos matriz de elementos meteorológicos mensuales).
  * "Cap IV Demanda.doc" (Sustento metodológico y asignación de estaciones por bloque de riego).

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Mes` | `mes` |
| `Estacion_LampasBajo_mm` | `estacion_lampasbajo_mm` |
| `Estacion_Recuay_Ticapampa_SanLorenzo_mm` | `estacion_recuay_ticapampa_sanlorenzo_mm` |

---

El dataset contiene las siguientes columnas:
- Mes: Mes correspondiente al ciclo del año hidrológico (desde Agosto hasta Julio).
- Estacion_LampasBajo_mm: Precipitación mensual al 75% de persistencia para la estación climática Lampas Bajo. Utilizada para los bloques 19, 20 y 21 de San Idelfonso. (Unidad: mm/mes).
- Estacion_Recuay_Ticapampa_SanLorenzo_mm: Precipitación mensual al 75% de persistencia combinada para las estaciones climáticas Recuay, Ticapampa y San Lorenzo. Utilizada para Antacocha y bloques 01 al 18 de San Idelfonso. (Unidad: mm/mes).

## IV. QA/QC

- Ordenamiento Temporal: Se reorganizaron los meses originales (que iniciaban en Enero) para coincidir con el año hidrológico (Agosto a Julio), permitiendo un cruce directo con el dataset de caudales `huaraz-caudales75.csv`.
- Unidad de Medida: Los datos se mantienen en su unidad original de milímetros (mm). Representan altura de lámina de agua de lluvia.
- Datos Faltantes (Huaraz): La estación de Huaraz fue omitida del CSV debido a que la tabla en el documento de origen se encuentra truncada/incompleta para la variable de precipitación al 75%, priorizando las series íntegras verificables en el Excel.

## V. Dominio espacial y coordenadas

1. Ubicación Precisa de la zona de estudio asociada a las estaciones:
   - Sistema de Referencia original de captaciones: UTM WGS84, Zona 18 Sur.
   - Rango Este (X): 220,702.28 m a 277,576.96 m
   - Rango Norte (Y): 8,878,809.42 m a 8,942,049.52 m
2. Bounding Box Recomendado para Extracción Satelital (GRACE NetCDF): (en decimales):
   - Latitud:  -10.1328° a -9.5648°
   - Longitud: -77.5487° a -77.0264°

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `huaraz_precipitacion75.csv` a `huaylas_precipitacion_climatologia.csv`.
- Metadata consolidada y reformateada desde `huaraz_precipitacion75_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.

**Contenido adicional no clasificado de la fuente original** (preservado para no perder información):

================================================================================
METADATOS DEL DATASET DE PRECIPITACIÓN (75% PERSISTENCIA) - HUARAZ
================================================================================
