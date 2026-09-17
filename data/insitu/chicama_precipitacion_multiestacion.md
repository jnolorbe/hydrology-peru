# Metadata — METADATOS DEL DATASET MULTIESTACIÓN DE PRECIPITACIÓN - CUENCA Y VALLE DE CHICAMA

## I. Información general

Nombre del Archivo: Precipitacion_Chicamas_Multistation_Simplified.csv
Ámbito Geográfico: Cuenca del Río Chicama y aledañas, Departamentos de La Libertad y Cajamarca, Perú.
Resolución Temporal: Mensual.
Periodo de Registro: Agosto de 1970 a Julio de 2002 (32 años hidrológicos, 384 registros mensuales).
Propósito: Proveer la serie de tiempo multianual y multiestación de precipitación en lámina mensual (mm) para las 14 estaciones pluviométricas y climatológicas de la cuenca del río Chicama, optimizada para modelos de balance hídrico espacial y validación de anomalías de almacenamiento total de agua (TWS) de satélites GRACE.

## II. Fuentes de datos originales

- Documentos de Origen: 
  * "Estudio Hidrologico del Rio Chicama - Pluviometria.pdf" (Anexo III: Pluviometría).
  * "PRECIPITACION CHICAMA.xls".
- Secciones Base:
  * Hojas individuales de estaciones: OTUZCO, SINSICAP, CONTUMAZA, ASUNCION, CAPACHIQUE, SUNCHUBAMBA, COSPAN, CAMPODEN, COINA, CALLANCAS, SAN BENITO, CASCAS, TAMBO y CASA GRANDE.
- Operadores Históricos: SENAMHI y Junta de Usuarios del Sub Distrito de Riego Chicama.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Date` | `date` |
| `ASUNCION` | `asuncion` |
| `CALLANCAS` | `callancas` |
| `CAMPODEN` | `campoden` |
| `CAPACHIQUE` | `capachique` |
| `CASA GRANDE` | `casa_grande` |
| `CASCAS` | `cascas` |
| `COINA` | `coina` |
| `CONTUMAZA` | `contumaza` |
| `COSPAN` | `cospan` |
| `OTUZCO` | `otuzco` |
| `SAN BENITO` | `san_benito` |
| `SINSICAP` | `sinsicap` |
| `SUNCHUBAMBA` | `sunchubamba` |
| `TAMBO` | `tambo` |

---

El dataset contiene 15 columnas estructuradas en formato ancho (wide-format):
1. Date (Formato YYYY-MM-DD): 
   Fecha estandarizada del mes de registro (fijada en el día 1 de cada mes).
2. ASUNCION (Numérico, Float): Precipitación mensual en mm (Estación Asunción).
3. CALLANCAS (Numérico, Float): Precipitación mensual en mm (Estación Callancas).
4. CAMPODEN (Numérico, Float): Precipitación mensual en mm (Estación Campoden).
5. CAPACHIQUE (Numérico, Float): Precipitación mensual en mm (Estación Capachique).
6. CASA GRANDE (Numérico, Float): Precipitación mensual en mm (Estación Casa Grande).
7. CASCAS (Numérico, Float): Precipitación mensual en mm (Estación Cascas).
8. COINA (Numérico, Float): Precipitación mensual en mm (Estación Coina).
9. CONTUMAZA (Numérico, Float): Precipitación mensual en mm (Estación Contumazá).
10. COSPAN (Numérico, Float): Precipitación mensual en mm (Estación Cospan).
11. OTUZCO (Numérico, Float): Precipitación mensual en mm (Estación Otuzco).
12. SAN BENITO (Numérico, Float): Precipitación mensual en mm (Estación San Benito).
13. SINSICAP (Numérico, Float): Precipitación mensual en mm (Estación Sinsicap).
14. SUNCHUBAMBA (Numérico, Float): Precipitación mensual en mm (Estación Sunchubamba).
15. TAMBO (Numérico, Float): Precipitación mensual en mm (Estación Tambo).

## IV. QA/QC

- Procesamiento: Se extrajeron y tabularon las series mensuales históricas de las 14 estaciones pluviométricas publicadas en el anexo de pluviometría del estudio hidrológico.
- Ciclo Hidrológico: Los registros se alinearon linealmente bajo el año hidrológico (Agosto a Julio), cubriendo desde agosto de 1970 hasta julio de 2002 de forma continua.

## V. Dominio espacial y coordenadas

Para la extracción de productos grillados de precipitación y el modelamiento de anomalías TWS (GRACE NetCDF) en la cuenca del río Chicama:
1. Bounding Box Recomendado (Grados Decimales WGS84):
   - Latitud:  [-8.20 , -7.10] (Sur)
   - Longitud: [-79.30 , -78.10] (Oeste)
2. Celdas Exactas Recomendadas para GRACE (Centroides 0.5° x 0.5°):
   - lats_chicama = [-7.75, -7.25]
   - lons_chicama = [-79.25, -78.75, -78.25]

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `chicama_precipitacion_multistation.csv` a `chicama_precipitacion_multiestacion.csv`.
- Metadata consolidada y reformateada desde `chicama_precipitacion_multistation_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.

**Contenido adicional no clasificado de la fuente original** (preservado para no perder información):

================================================================================
METADATOS DEL DATASET MULTIESTACIÓN DE PRECIPITACIÓN - CUENCA Y VALLE DE CHICAMA
================================================================================

**V. INVENTARIO Y UBICACIÓN DE ESTACIONES (Fuente: PRECIPITACION CHICAMA.xls)**

1. Casa Grande: Climatológica | La Libertad, Ascope, Casa Grande | Alt: 240 msnm | Lat: 7° 45' S, Lon: 79° 11' W
2. Tambo: Pluviométrica | La Libertad, Gran Chimú, Cascas | Alt: 850 msnm | Lat: 7° 34' S, Lon: 78° 42' W
3. Cascas: Climatológica | La Libertad, Gran Chimú, Cascas | Alt: 1330 msnm | Lat: 7° 29' S, Lon: 78° 49' W
4. San Benito: Pluviométrica | La Libertad, Contumazá, San Benito | Alt: 1200 msnm | Lat: 7° 25' S, Lon: 78° 56' W
5. Callancas: Pluviométrica | La Libertad, Otuzco | Alt: 1400 msnm | Lat: 7° 46' S, Lon: 78° 29' W
6. Coina: Pluviométrica | La Libertad, Otuzco | Alt: 1874 msnm | Lat: 7° 48' S, Lon: 78° 22' W
7. Campoden: Pluviométrica | La Libertad | Alt: 2150 msnm | Lat: 7° 31' S, Lon: 78° 31' W
8. Cospan: Climatológica | Cajamarca | Alt: 2450 msnm | Lat: 7° 26' S, Lon: 78° 32' W
9. Sunchubamba: Pluviométrica | La Libertad | Alt: 2400 msnm | Lat: 7° 29' S, Lon: 78° 23' W
10. Capachique: Pluviométrica | La Libertad | Alt: 2880 msnm | Lat: 7° 51' S, Lon: 78° 19' W
11. Asuncion: Climatológica | Jequetepeque / La Libertad | Alt: 2285 msnm | Lat: 7° 19' S, Lon: 78° 31' W
12. Contumaza: Climatológica | Cajamarca | Alt: 2452 msnm | Lat: 7° 21'
