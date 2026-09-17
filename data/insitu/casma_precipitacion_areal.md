# Metadata — METADATOS DEL DATASET PRECIPITACIÓN AREAL TOTAL - CUENCA CASMA

## I. Información general

Nombre del Archivo: Precipitacion_Areal_Casma_Total_1966_2005.csv
Ámbito Geográfico: Cuenca del Río Casma (Incluyendo la subcuenca Sechín y todos sus afluentes), Departamento de Ancash, Perú.
Área Total de la Cuenca: 2990.8 km²
Resolución Temporal: Mensual.
Periodo de Registro: Enero de 1966 a Diciembre de 2005 (40 años o 492 meses).
Propósito: Proveer una serie de tiempo continua de la precipitación areal (media espacial ponderada) de toda la cuenca, como ingreso principal (input P) para la ecuación de balance hídrico y validación satelital (GRACE).

## II. Fuentes de datos originales

- Archivos Origen: "ANEXO 06-PRECIPITACION POR UH.xls" y "areas.xlsx".
- Procesamiento Espacial: La precipitación total de la cuenca no es una simple suma, sino un promedio espacial ponderado. Se extrajo la serie de tiempo de precipitación calculada por el método de isoyetas para cada una de las 9 unidades hidrográficas (UH) no superpuestas que componen el sistema:
  1. Alto Casma (177.8 km²)
  2. Río Pira (164.8 km²)
  3. Medio Alto Casma (4.0 km²)
  4. Río Vado (163.7 km²)
  5. Medio Casma (492.5 km²)
  6. Río Yaután (352.0 km²)
  7. Medio Bajo Casma (487.8 km²)
  8. Río Sechín (729.5 km²)
  9. Bajo Casma (418.7 km²)
- Consolidación: Cada registro mensual fue multiplicado por el área de su UH respectiva, sumado globalmente y dividido entre el área total (2990.8 km²) para obtener la lámina de lluvia (mm). El volumen (MMC) se calculó multiplicando la lámina por el área total de la cuenca.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Date` | `date` |
| `P_Total_mm` | `precipitacion_total_mm` |
| `P_Total_MMC` | `precipitacion_total_mmc` |

---

1. Date (Formato YYYY-MM-DD): Fecha estandarizada que representa el mes de medición.
2. P_Total_mm (Numérico, Float): Precipitación Areal Media Ponderada sobre toda la Cuenca. Expresada en milímetros (mm).
3. P_Total_MMC (Numérico, Float): Volumen total de precipitación ingresado al sistema a nivel de cuenca entera. Expresado en Millones de Metros Cúbicos (MMC).

## IV. QA/QC

- Integridad: La estructura matricial del archivo de Excel original garantizó el correcto alineamiento de los meses nulos (0.00 mm en época seca). No hubo corrimientos de datos.
- Dinámica del Sistema: Como ingreso primario de masa al sistema, estos datos capturan fielmente los eventos extremos, como las intensas lluvias durante los fenómenos El Niño (FEN) de 1982-1983 y 1997-1998, críticos para la detección gravimétrica.

## V. Dominio espacial y coordenadas

Para la extracción de la señal satelital en productos grillados (ej. GRACE NetCDF), se define la siguiente caja delimitadora (Bounding Box) que encapsula la gradiente altitudinal de la cuenca del río Casma y sus afluentes, desde sus nacientes en la Cordillera Negra hasta su desembocadura en el Océano Pacífico:
1. Bounding Box Recomendado (Grados Decimales):
   - Latitud:  [-9.8 , -9.1] (Sur)
   - Longitud: [-78.5 , -77.5] (Oeste)
2. Celdas Exactas Recomendadas para GRACE (Centroides 0.5° x 0.5°):
   Para capturar la dinámica completa de transporte de masa (desde la recarga pluvial en 
   las cabeceras hasta la desembocadura, incluyendo la recarga de acuíferos), se recomienda 
   extraer los datos del NetCDF utilizando los siguientes centroides espaciales con el 
   método nearest de xarray:
   - lats_casma = [-9.75, -9.25]
   - lons_casma = [-78.25, -77.75]

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `casma_precipitacion_areal_total_1966_2005.csv` a `casma_precipitacion_areal.csv`.
- Metadata consolidada y reformateada desde `casma_precipitacion_areal_total_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.

**Contenido adicional no clasificado de la fuente original** (preservado para no perder información):

================================================================================
METADATOS DEL DATASET PRECIPITACIÓN AREAL TOTAL - CUENCA CASMA
================================================================================

**III. RED DE ESTACIONES PLUVIOMÉTRICAS**

Las isoyetas y la precipitación areal fueron modeladas a partir de la siguiente red de estaciones meteorológicas operadas por SENAMHI (convertidas a grados decimales):
   - Estación Recuay (3394 msnm): Lat -9.717, Lon -77.450
   - Estación Pira (3570 msnm): Lat -9.567, Lon -77.700
   - Estación Cajamarquilla (3028 msnm): Lat -9.617, Lon -77.733
   - Estación Pariacoto (2000 msnm): Lat -9.550, Lon -77.883
   - Estación Buena Vista (419 msnm): Lat -9.433, Lon -78.200
   - Estación Malvas (3500 msnm): Lat -9.933, Lon -77.650
*(Nota: Cotaparaco fue excluida en los análisis hidrológicos originales por anomalías de depresión topográfica).*
