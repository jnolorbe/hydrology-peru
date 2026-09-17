# Metadata — METADATOS DEL DATASET DE: CAUDALES Y VOLUMENES MENSUALES

## I. Información general

- Proyecto: Validación y Calibración Hidrológica de Series Temporales GRACE-FO (TWS)
- Ámbito Geográfico: Cuenca Binacional del Río Zarumilla y Cuenca del Río Tumbes
- Región Hidrográfica: Vertiente del Pacífico (Pacífico Norte, Perú - Ecuador)
- Periodo Temporal Cubierto: 1960-01-01 a 2005-12-01 (Paso de tiempo mensual)
- Sistema Geodésico y Proyección: WGS84 / Coordenadas Geográficas (EPSG:4326)
- Entidad Autora / Custodia de Fuentes: Instituto Nacional de Recursos Naturales (INRENA) - PROFODUA / SENAMHI / PEBPT

## II. Fuentes de datos originales

- Cap II Oferta.doc: Estudio de Disponibilidad Hídrica Superficial Valle Zarumilla (PROFODUA - IRH - INRENA).
- Anexo A.doc: Registros Históricos de Caudales Mensuales (Cuadros A-01, A-02, A-03).
- Anexo B.doc & CUADB-~3.XLS: Registros Completados y Extendidos mediante el Modelo Estocástico HEC-4 (Cuadros B-03 a B-09).
- Cuadros - Oferta.xls: Matrices de consistencia, análisis de doble masa y pruebas de homogeneidad de t de Student y F de Fisher.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Date` | `date` |
| `caudal_puente_bolsico_m3s` | `caudal_puente_bolsico_m3s` |
| `volumen_puente_bolsico_mmc` | `volumen_puente_bolsico_mmc` |
| `caudal_la_palma_m3s` | `caudal_la_palma_m3s` |
| `volumen_la_palma_mmc` | `volumen_la_palma_mmc` |
| `caudal_puente_tumbes_m3s` | `caudal_puente_tumbes_m3s` |
| `volumen_puente_tumbes_mmc` | `volumen_puente_tumbes_mmc` |
| `caudal_matapalo1_m3s` | `caudal_matapalo1_m3s` |
| `volumen_matapalo1_mmc` | `volumen_matapalo1_mmc` |
| `caudal_matapalo2_m3s` | `caudal_matapalo2_m3s` |
| `volumen_matapalo2_mmc` | `volumen_matapalo2_mmc` |
| `caudal_matapalo3_m3s` | `caudal_matapalo3_m3s` |
| `volumen_matapalo3_mmc` | `volumen_matapalo3_mmc` |

---

1. Date: Fecha en formato estándar ISO-8601 (YYYY-MM-DD), correspondiente al primer día de cada mes (YYYY-MM-01).
2. caudal_puente_bolsico_m3s: Caudal medio mensual en la estación hidrométrica Puente Bolsico (Río Zarumilla), en metros cúbicos por segundo (m³/s).
3. volumen_puente_bolsico_mmc: Volumen mensual escurrido en Puente Bolsico, en Millones de Metros Cúbicos (MMC).
4. caudal_la_palma_m3s: Caudal medio mensual completado y extendido en la estación hidrométrica La Palma (Río Zarumilla), en m³/s.
5. volumen_la_palma_mmc: Volumen mensual escurrido en La Palma, en MMC.
6. caudal_puente_tumbes_m3s: Caudal medio mensual en la estación hidrométrica Puente Tumbes / Puente Carretera (Río Tumbes), en m³/s.
7. volumen_puente_tumbes_mmc: Volumen mensual escurrido en Puente Tumbes, en MMC.
8. caudal_matapalo1_m3s: Caudal medio mensual natural en el punto de control Matapalo 1 (Quebrada Faical), en m³/s.
9. volumen_matapalo1_mmc: Volumen mensual escurrido en Matapalo 1, en MMC.
10. caudal_matapalo2_m3s: Caudal medio mensual natural en el punto de control Matapalo 2 (Río Zarumilla Alto), en m³/s.
11. volumen_matapalo2_mmc: Volumen mensual escurrido en Matapalo 2, en MMC.
12. caudal_matapalo3_m3s: Caudal medio mensual natural en el punto de control Matapalo 3 (Río Zarumilla Medio), en m³/s.
13. volumen_matapalo3_mmc: Volumen mensual escurrido en Matapalo 3, en MMC.

## IV. QA/QC

- Conversión Volumétrica: Se utilizó la formulación exacta en función del número de días de cada mes calendario:
    Volumen (MMC) = (Caudal [m³/s] * 86400 s/día * días_mes) / 10^6
  Se contemplan explícitamente los años bisiestos (febrero de 29 días: 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004).
- Extensión y Reconstitución (HEC-4): Las series de Puente Bolsico y La Palma fueron completadas y extendidas hidrológicamente con base en la estación patronal consistente Puente Tumbes.
- Eventos Extremos: La base de datos refleja con total precisión los pulsos hidroclimáticos de El Niño Oscilación del Sur (ENSO) de 1982-1983 y 1997-1998, fundamentales para la correlación y descomposición de señales de almacenamiento total de agua (TWS) de gravimetría satelital (GRACE/GRACE-FO).
- Tratamiento de Vacíos (Gaps): Periodos no monitoreados para subcuencas afluentes específicas (ej. Matapalo fuera del periodo 1964/65-1999/2000) se conservan como NaN / vacíos para prevenir sesgos en análisis estadísticos o espectrales.

## V. Dominio espacial y coordenadas

- Estación Puente Bolsico: Latitud 03° 26' S (-3.4333°), Longitud 80° 27' W (-80.4500°), Altitud: 3 msnm.
- Estación La Palma: Latitud 03° 27' S (-3.4500°), Longitud 80° 13' W (-80.2167°), Altitud: 40 msnm.
- Estación Puente Tumbes: Latitud 03° 26' S (-3.4333°), Longitud 80° 28' W (-80.4667°), Altitud: 3 msnm.
- Estación Matapalo 1 (Qda. Faical): Latitud 03° 43' S (-3.7167°), Longitud 80° 14' W (-80.2333°), Altitud: 150 msnm.
- Estación Matapalo 2 (Río Zarumilla): Latitud 03° 41' S (-3.6833°), Longitud 80° 12' W (-80.2000°), Altitud: 100 msnm.
- Estación Matapalo 3 (Río Zarumilla): Latitud 03° 38' S (-3.6333°), Longitud 80° 11' W (-80.1833°), Altitud: 140 msnm.
- Bounding Box Regional:
  * Latitud Norte:  -3.4000° S
  * Latitud Sur:    -3.7500° S
  * Longitud Oeste: -80.5000° W
  * Longitud Este:  -80.1500° W

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `zarumilla_caudales.csv` a `zarumilla_caudal_volumen_multiestacion.csv`.
- Metadata consolidada y reformateada desde `zarumilla_caudales_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
