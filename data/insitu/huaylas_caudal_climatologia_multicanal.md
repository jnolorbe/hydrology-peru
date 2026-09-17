# Metadata — METADATOS DEL DATASET DE CAUDALES GENERADOS (75% PERSISTENCIA) - HUARAZ

## I. Información general

Nombre del Archivo: huaraz-caudales75.csv
Ámbito Geográfico: Cuenca Alta del Río Santa, Callejón de Huaylas (Comisiones de Regantes Antacocha, San Idelfonso, Rajucolta y Jauna-Olleros).
Departamento del Perú: Ancash.
Resolución Temporal: Mensual.
Periodo de Registro: Año hidrológico genérico (Agosto a Julio). Representa un año climatológico sintético modelado en base a la serie histórica para establecer caudales al 75% de persistencia.

## II. Fuentes de datos originales

- Documentos de Origen: 
  * "Caudales gerenados de las Comisiones.xls" (Datos matriz de caudales mensuales generados).
  * "Coordenadas de las Captaciones.xls" (Ubicación espacial de las fuentes de agua).
  * Informes de Asignación y Bloques de Riego (Cap II Oferta.doc, Cap III Bloques.doc, Cap IV Demanda.doc, Cap V Asignaciones.doc).

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Mes` | `mes` |
| `Antacocha_Puquiales` | `antacocha_puquiales` |
| `Antacocha_Q.MarcaPunku` | `antacocha_qmarcapunku` |
| `Antacocha_Q.RanraUcro` | `antacocha_qranraucro` |
| `Antacocha_Q.Tangra` | `antacocha_qtangra` |
| `Antacocha_Qda.Chiriac` | `antacocha_qdachiriac` |
| `Antacocha_R.Sipchoc` | `antacocha_rsipchoc` |
| `Antacocha_RíoSanta` | `antacocha_riosanta` |
| `Antacocha_lgs.LlacshayTuto` | `antacocha_lgsllacshaytuto` |
| `San idelfonso_Filtraciones` | `san_idelfonso_filtraciones` |
| `San idelfonso_Lag.Queshque` | `san_idelfonso_lagqueshque` |
| `San idelfonso_Lag.Querococha` | `san_idelfonso_lagquerococha` |
| `San idelfonso_Manantiales` | `san_idelfonso_manantiales` |
| `San idelfonso_Qda.Chaupis` | `san_idelfonso_qdachaupis` |
| `San idelfonso_Qda.YacshaHuanca` | `san_idelfonso_qdayacshahuanca` |
| `San idelfonso_RíoNegro` | `san_idelfonso_rionegro` |
| `San idelfonso_RíoPachacoto` | `san_idelfonso_riopachacoto` |
| `San idelfonso_RíoPocrac` | `san_idelfonso_riopocrac` |
| `San idelfonso_RíoShiqui` | `san_idelfonso_rioshiqui` |
| `San idelfonso_RíoYanayacu` | `san_idelfonso_rioyanayacu` |
| `Rajucolta_Qda.Pariac` | `rajucolta_qdapariac` |
| `Olleros_Lag.Shacsha` | `olleros_lagshacsha` |
| `Olleros_PuquialOncor(Olleros)` | `olleros_puquialoncor(olleros)` |
| `Olleros_Qda.Mashuan` | `olleros_qdamashuan` |
| `Olleros_Qda.ChachiPucro` | `olleros_qdachachipucro` |
| `Olleros_Qda.ChucruOcsha` | `olleros_qdachucruocsha` |
| `Olleros_Qda.Huaracayoc(Olleros)` | `olleros_qdahuaracayoc(olleros)` |
| `Olleros_Qda.Lloclla` | `olleros_qdalloclla` |
| `Olleros_Qda.Pumpuyoc` | `olleros_qdapumpuyoc` |

---

El dataset contiene las siguientes columnas:
- Mes: Mes correspondiente al ciclo del año hidrológico (desde Agosto hasta Julio).
- [Comisión]_[Fuente/Captación]: 28 columnas numéricas continuas que representan el volumen mensual de agua ofertado al 75% de persistencia para cada fuente principal.
  Ejemplos: Antacocha_RíoSanta, Rajucolta_Qda.Pariac, San idelfonso_Lag.Querococha.
  * Unidad de medida: Millones de Metros Cúbicos (MMC).

## IV. QA/QC

- Transformación de Unidades: Los datos originales expresados en metros cúbicos por segundo (m³/s) fueron convertidos a Millones de Metros Cúbicos (MMC) considerando los días calendario de cada mes (ej. Febrero = 28 días).
- Agrupación: Se consolidaron las tomas o captaciones secundarias que compartían la misma fuente matriz (ej. múltiples tomas en el Río Santa para una misma comisión se sumaron en una sola estación representativa).
- Filtrado Espacial: Se excluyeron puquiales o fuentes de aporte menor (picos inferiores a 0.1 m³/s) para optimizar el cruce con la resolución macroscópica de la grilla de TWS GRACE-FO.
- Condición de los datos: No corresponden a un registro cronológico continuo interanual, sino a una distribución estadística anual para fines de asignación de licencias de derechos de agua.

## V. Dominio espacial y coordenadas

1. Ubicación Precisa de las estaciones (en coordenadas proyectadas):
   - Sistema de Referencia: UTM WGS84, Zona 18 Sur.
   - Rango Este (X): 220,702.28 m a 277,576.96 m
   - Rango Norte (Y): 8,878,809.42 m a 8,942,049.52 m
2. Bounding Box Recomendado para Extracción Satelital (GRACE NetCDF): (en decimales):
   - Latitud:  -10.1328° a -9.5648°
   - Longitud: -77.5487° a -77.0264°

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `huaraz_caudales75.csv` a `huaylas_caudal_climatologia_multicanal.csv`.
- Metadata consolidada y reformateada desde `huaraz_caudales75_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.

**Contenido adicional no clasificado de la fuente original** (preservado para no perder información):

================================================================================
METADATOS DEL DATASET DE CAUDALES GENERADOS (75% PERSISTENCIA) - HUARAZ
================================================================================
