# Metadata — Caudal y Volumen Mensual, Ríos Casma y Sechín (Estaciones Tutuma y Quillo)

## I. Información general

- **Archivo de datos:** `casma_sechin_caudal_volumen.csv`
- **Ámbito geográfico:** Cuenca del Río Casma (subcuencas Casma-Grande y Sechín), Departamento de Ancash, Perú.
- **Resolución temporal:** Mensual.
- **Periodo de registro:** Agosto 1973 a Julio 2002 (29 años hidrológicos, 348 meses).
- **Propósito:** Serie continua de caudal y volumen para evaluación del balance hídrico y validación de anomalías TWS (GRACE).

## II. Fuentes de datos originales

- **Documento base:** "INFORME FINAL CASMA 3.doc" (Estudio Hidrológico en la Cuenca del Río Casma, INRENA/ATDR Casma-Huarmey, 2007), Anexo 1a (Estación Tutuma) y Anexo 1b (Estación Quillo).
- **Operadores históricos:** SENAMHI y ATDR Casma-Huarmey.
- **Nota sobre las columnas de caudal (m³/s):** provienen de un segundo archivo (`Caudales_Casma_Sechin_1973_2002.csv`) entregado independientemente en `DATA_INSITU`, sin metadata propia. Se verificó que corresponde a las mismas 2 estaciones y al mismo periodo exacto (1973-08 a 2002-07, 348 meses) que el archivo de volumen documentado arriba, por lo que se fusionaron en un solo archivo.

## III. Diccionario de variables

| Columna | Unidad | Descripción |
|---|---|---|
| `date` | - | Fecha (`YYYY-MM-DD`, primer día del mes) |
| `caudal_tutuma_m3s` | m³/s | Caudal medio mensual, Estación Sector Tutuma (Río Casma-Grande) |
| `volumen_tutuma_mmc` | MMC | Volumen mensual, Estación Tutuma |
| `caudal_quillo_m3s` | m³/s | Caudal medio mensual, Estación Puente Quillo (Río Sechín) |
| `volumen_quillo_mmc` | MMC | Volumen mensual, Estación Quillo |

## IV. QA/QC

- **Conversión física (volumen):** los registros originales estaban en m³/s; se transformaron a MMC multiplicando el caudal mensual por el número exacto de segundos de cada mes calendario (considerando años bisiestos).
- **Integridad:** se mantienen los eventos extremos (anomalías positivas por El Niño 1983 y 1998) sin suavizado estadístico.
- **Verificación de la fusión:** se comprobó, celda por celda, que las columnas de caudal (m³/s) y volumen (MMC) fusionadas en este archivo corresponden exactamente a las mismas fechas y estaciones (Tutuma, Quillo) reportadas de forma independiente en los dos archivos originales; no se detectaron discrepancias.

## V. Dominio espacial y coordenadas

- **Bounding box recomendado (GRACE):** Latitud -9.1° a -9.8° (Sur); Longitud -77.5° a -78.5° (Oeste).
- **Estaciones de control:** Puente Carretera Casma/El Carrizal (60 msnm) Lat -9.482/Lon -78.271; Puente Carretera Sechín (105 msnm) Lat -9.476/Lon -78.291; Sector Tutuma (1200 msnm) Lat -9.536/Lon -77.946; Puente Quillo (1189 msnm) Lat -9.324/Lon -78.045.
- **Centroides 0.5°×0.5° recomendados (matriz 2×2):** `lats_casma = [-9.75, -9.25]`; `lons_casma = [-78.25, -77.75]`.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- **Fusión (acción explícita del usuario):** se combinaron `casma_sechin_caudales.csv` (columnas de volumen, `volumen_Tutuma_MMC`/`volumen_Quillo_MMC`) y `Caudales_Casma_Sechin_1973_2002.csv` (columnas de caudal `Q_Tutuma_m3s`/`Q_Quillo_m3s`, más columnas de fecha redundantes `Actual_Year`/`Month_Num`/`Month` que se descartaron por ser derivables de `date`) en un único archivo `caudal_tutuma_m3s, volumen_tutuma_mmc, caudal_quillo_m3s, volumen_quillo_mmc`.
- La columna `Q_Total_m3s` del segundo archivo (suma Tutuma+Quillo) se descartó por ser trivialmente derivable de las dos columnas de caudal ya incluidas.
- **Nota:** las estaciones Tutuma y Quillo también aparecen en `huarmeyculebras_caudal_volumen_multicuenca.csv` (dataset de Huarmey-Culebras-Casma-Sechín); se verificó que los valores numéricos son distintos entre ambos archivos (no son duplicados), por lo que se mantienen como datasets independientes con esta nota cruzada.
