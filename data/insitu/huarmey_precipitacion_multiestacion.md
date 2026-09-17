# Metadata — METADATOS DEL DATASET DE: PRECIPITACION MENSUAL - CUENCA HUARMEY Y ALEDAÑAS

## I. Información general

- Nombre del Dataset: Series Temporales de Precipitación Mensual y Precipitación Areal de la Cuenca Huarmey
- Variable Principal: Precipitación acumulada mensual (mm/mes)
- Periodo Temporal: 1989-01-01 a 2005-12-01 (Paso de tiempo: Mensual, primer día de mes YYYY-MM-DD)
- Región Hidrográfica: Vertiente del Pacífico, Departamento de Ancash, Perú
- Sistema de Coordenadas: WGS84 Geográficas (Latitud/Longitud en Grados Decimales)
- Propósito: Validación y control de calidad (QA/QC) hidrometeorológico para calibración hidrológica y comparación estacional/tendencias con series TWS de GRACE/GRACE-FO.

## II. Fuentes de datos originales

- Entidad Generadora / Operadora: Servicio Nacional de Meteorología e Hidrología del Perú (SENAMHI).
- Fuente de Extracción: Estudio Hidrológico "Propuesta de Asignación de Agua Superficial en Bloques en la Cuenca Alta de Huarmey", PROFODUA Fase 2 - INRENA / ATDR Casma-Huarmey (Mayo 2007).
- Ubicación en Fuente: Anexos 2a, 2b, 2c, 2d, 2e, 2f y 2g.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Date` | `date` |
| `precipitacion_recuay_mm` | `precipitacion_recuay_mm` |
| `precipitacion_cotaparaco_mm` | `precipitacion_cotaparaco_mm` |
| `precipitacion_pira_mm` | `precipitacion_pira_mm` |
| `precipitacion_cajamarquilla_mm` | `precipitacion_cajamarquilla_mm` |
| `precipitacion_aija_mm` | `precipitacion_aija_mm` |
| `precipitacion_malvas_mm` | `precipitacion_malvas_mm` |
| `precipitacion_buena_vista_mm` | `precipitacion_buena_vista_mm` |
| `precipitacion_areal_huarmey_mm` | `precipitacion_areal_huarmey_mm` |

---

1. Date: Fecha en formato ISO 8601 (YYYY-MM-DD), correspondiente al primer día de cada mes de registro.
2. precipitacion_recuay_mm: Precipitación mensual en la estación Recuay (Cuenca Santa / límite, 3394 msnm).
3. precipitacion_cotaparaco_mm: Precipitación mensual en la estación Cotaparaco (Cuenca Huarmey, 3008 msnm).
4. precipitacion_pira_mm: Precipitación mensual en la estación Pira (Cuenca Casma, 3570 msnm).
5. precipitacion_cajamarquilla_mm: Precipitación mensual en la estación Cajamarquilla (Cuenca Huarmey, 3360 msnm).
6. precipitacion_aija_mm: Precipitación mensual en la estación Aija (Cuenca Huarmey, 3360 msnm).
7. precipitacion_malvas_mm: Precipitación mensual en la estación Malvas (Cuenca Huarmey, 3500 msnm).
8. precipitacion_buena_vista_mm: Precipitación mensual en la estación Buena Vista (Cuenca Baja Casma, 419 msnm).
9. precipitacion_areal_huarmey_mm: Precipitación areal ponderada sobre el dominio hidrográfico de la cuenca Huarmey (calculada mediante polígonos de Thiessen / modelo hipsométrico).

## IV. QA/QC

- Control de Calidad (QA/QC): Análisis de consistencia temporal, análisis visual de correlación cruzada inter-estación y completación mediante regresiones mensuales con estaciones vecinas homogéneas.
- Comportamiento Estacional: Marcada estacionalidad típica de los Andes occidentales peruanos con periodo húmedo entre diciembre y abril (máximos en febrero-marzo) y periodo de estiaje severo entre mayo y agosto.
- Respuesta a Eventos ENOS: Se registran anomalías positivas significativas durante eventos El Niño (notablemente 1997-1998 con pulsos pluviales en cuenca baja/costera y variabilidad en la alta cordillera).
- Cálculo de Precipitación Areal: Ponderación espacial aplicada sobre la cuenca Huarmey:
  P_areal = 0.25 * P_Aija + 0.25 * P_Cotaparaco + 0.20 * P_Malvas + 0.20 * P_Cajamarquilla + 0.10 * P_BuenaVista

## V. Dominio espacial y coordenadas

- Cuenca / Dominio de Análisis: Cuenca del Río Huarmey y cuencas aledañas (Casma, Santa).
- Bounding Box Geográfico (WGS84):
  * Latitud Norte (Max Lat):   -9.1000° S
  * Latitud Sur (Min Lat):    -10.1500° S
  * Longitud Oeste (Min Lon): -78.2500° W
  * Longitud Este (Max Lon):  -77.2000° W
- Rango Altitudinal: 0 a 4,850 m.s.n.m.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `huarmey_precipitacion.csv` a `huarmey_precipitacion_multiestacion.csv`.
- Metadata consolidada y reformateada desde `huarmey_precipitacion_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.

**Contenido adicional no clasificado de la fuente original** (preservado para no perder información):

METADATOS DEL DATASET DE: PRECIPITACION MENSUAL - CUENCA HUARMEY Y ALEDAÑAS

**V. INFORMACIÓN DE ESTACIONES**

Estación         Tipo  Cuenca   Dpto.   Provincia   Latitud (S)  Longitud (W)  Lat_Dec     Lon_Dec   Altitud (m)
Recuay           CO    Santa    Ancash  Recuay      09° 43' 00"  77° 27' 00"   -9.7167°    -77.4500° 3394.0
Cotaparaco       PLU   Huarmey  Ancash  Recuay      09° 59' 00"  77° 35' 00"   -9.9833°    -77.5833° 3008.0
Pira             PLU   Casma    Ancash  Huaraz      09° 34' 48"  77° 42' 00"   -9.5800°    -77.7000° 3570.0
Cajamarquilla    PLU   Huarmey  Ancash  Recuay      09° 37' 48"  77° 43' 48"   -9.6300°    -77.7300° 3360.0
Aija             CO    Huarmey  Ancash  Aija        09° 08' 00"  77° 45' 00"   -9.1333°    -77.7500° 3360.0
Malvas           PLU   Huarmey  Ancash  Huarmey     09° 56' 00"  77° 39' 00"   -9.9333°    -77.6500° 3500.0
Buena Vista      CO    Casma    Ancash  Casm        09° 26' 00"  78° 12' 00"   -9.4333°    -78.2000°  419.0
