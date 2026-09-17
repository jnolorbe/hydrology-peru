# Metadata — METADATOS DEL DATASET DE PRECIPITACIÓN AREAL - CUENCA Y VALLE DE CHICAMA

## I. Información general

Nombre del Archivo: Precipitacion_Areal_Chicama_Simplified.csv
Ámbito Geográfico: Cuenca del Río Chicama y aledañas, Departamentos de La Libertad y Cajamarca, Perú.
Resolución Temporal: Mensual.
Periodo de Registro: Agosto de 1970 a Julio de 2002 (32 años hidrológicos, 384 registros mensuales).
Propósito: Proveer la serie de precipitación media areal ($P_{ar}$) en lámina mensual (mm) para la cuenca del río Chicama, obtenida mediante la integración espacial (promedio multiestación de la red de 14 estaciones de la cuenca), indispensable para el cierre del balance hídrico y la validación de anomalías de almacenamiento total de agua (TWS) de GRACE.

## II. Fuentes de datos originales

- Documentos de Origen: 
  * "Estudio Hidrologico del Rio Chicama - Pluviometria.pdf" (Anexo III: Pluviometría).
  * "PRECIPITACION CHICAMA.xls".
- Secciones Base:
  * Registros mensuales históricos de las 14 estaciones pluviométricas y climatológicas de la cuenca.
- Operadores Históricos: SENAMHI y Junta de Usuarios del Sub Distrito de Riego Chicama.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Date` | `date` |
| `Pp_Areal_Mean_mm` | `precipitacion_areal_mean_mm` |

---

El dataset contiene las siguientes 2 columnas:
1. Date (Formato YYYY-MM-DD): 
   Fecha estandarizada del mes de registro (fijada en el día 1 de cada mes).
2. Pp_Areal_Mean_mm (Numérico, Float): 
   Precipitación media areal ponderada de la cuenca, calculada como el promedio aritmético multiestación de la red pluviométrica, expresada en milímetros (mm).

## IV. QA/QC

- Integración Espacial: Calculada a partir de los registros mensuales sincronizados de las 14 estaciones de la red de la cuenca (capturando un gradiente altitudinal desde 240 msnm hasta 2880 msnm).
- Ciclo Hidrológico: Alineado cronológicamente bajo el año hidrológico (Agosto a Julio), cubriendo desde agosto de 1970 hasta julio de 2002.

## V. Dominio espacial y coordenadas

1. Bounding Box Recomendado (Grados Decimales WGS84):
   - Latitud:  [-8.20 , -7.10] (Sur)
   - Longitud: [-79.30 , -78.10] (Oeste)
2. Celdas Exactas Recomendadas para GRACE (Centroides 0.5° x 0.5°):
   - lats_chicama = [-7.75, -7.25]
   - lons_chicama = [-79.25, -78.75, -78.25]

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `chicama_precipitacion_areal.csv` a `chicama_precipitacion_areal.csv`.
- Metadata consolidada y reformateada desde `chicama_precipitacion_areal_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.

**Contenido adicional no clasificado de la fuente original** (preservado para no perder información):

================================================================================
METADATOS DEL DATASET DE PRECIPITACIÓN AREAL - CUENCA Y VALLE DE CHICAMA
================================================================================

**V. INVENTARIO DE ESTACIONES INTEGRADAS**

1. Casa Grande (240 msnm | Lat: 7° 45' S, Lon: 79° 11' W)
2. Tambo (850 msnm | Lat: 7° 34' S, Lon: 78° 42' W)
3. Cascas (1330 msnm | Lat: 7° 29' S, Lon: 78° 49' W)
4. San Benito (1200 msnm | Lat: 7° 25' S, Lon: 78° 56' W)
5. Callancas (1400 msnm | Lat: 7° 46' S, Lon: 78° 29' W)
6. Coina (1874 msnm | Lat: 7° 48' S, Lon: 78° 22' W)
7. Campoden (2150 msnm | Lat: 7° 31' S, Lon: 78° 31' W)
8. Cospan (2450 msnm | Lat: 7° 26' S, Lon: 78° 32' W)
9. Sunchubamba (2400 msnm | Lat: 7° 29' S, Lon: 78° 23' W)
10. Capachique (2880 msnm | Lat: 7° 51' S, Lon: 78° 19' W)
11. Asuncion (2285 msnm | Lat: 7° 19' S, Lon: 78° 31' W)
12. Contumaza (2452 msnm | Lat: 7° 21' S, Lon: 78° 49' W)
13. Sinsicap (2125 msnm | Lat: 7° 51' S, Lon: 78° 45' W)
14. Otuzco (2620 msnm | Lat: 7° 54' S, Lon: 78° 34' W)
