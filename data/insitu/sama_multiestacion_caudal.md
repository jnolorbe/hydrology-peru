# Metadata — Caudal Multiestación, Cuenca Sama (Tacna)

## I. Información general

- **Archivo de datos:** `sama_multiestacion_caudal.csv`
- **Ámbito geográfico:** Cuenca Sama, Departamento de Tacna, Perú. 2 estaciones: La Tranca, Yabroco.
- **Resolución temporal:** Mensual.
- **Periodo de registro:** Enero 1993 a Diciembre 1996 (48 meses).

## II. Fuentes de datos originales

- Sin documentación narrativa propia (archivo huérfano en `DATA_INSITU`).
- **Cuenca confirmada por el usuario** mediante `estaciones_hidrometricas_01.xlsx`: La Tranca (cuenca Sama, provincia Tacna, distrito Inclán) y Yabroco (cuenca Sama, provincia/distrito Candarave).

## III. Diccionario de variables

| Columna | Unidad | Descripción |
|---|---|---|
| `date` | - | Fecha (`YYYY-MM-DD`, primer día del mes) |
| `caudal_la_tranca_m3s` | m³/s | Caudal medio mensual, estación La Tranca |
| `caudal_yabroco_m3s` | m³/s | Caudal medio mensual, estación Yabroco |

## IV. QA/QC

- Se transcribió tal cual desde el archivo original; sin relleno, interpolación ni corrección de outliers aplicada.

## V. Dominio espacial y coordenadas (según `estaciones_hidrometricas_01.xlsx`)

| Estación | Provincia | Distrito | Latitud | Longitud | Altitud (msnm) |
|---|---|---|---|---|---|
| La Tranca | Tacna | Inclán | -17.717 | -70.467 | 620 |
| Yabroco | Candarave | Candarave | -17.333 | -70.117 | 3200 |

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- **Separación (acción explícita del usuario):** subconjunto de las 2 columnas de cuenca Sama extraídas de `locumba_sama_caudales.csv` (11 estaciones, 3 cuencas mezcladas). Ver también `locumba_multiestacion_caudal.csv` y `maure_kovirebofedal_caudal.csv`.
- **Referencia cruzada:** no se fusionó con `sama_coruca_caudal_volumen.csv` (misma cuenca, pero red y periodo distintos: estación Coruca, 2005-2008).
- Nombres de columna normalizados a snake_case.
