# Metadata — Caudal Multiestación, Cuenca Locumba (Tacna)

## I. Información general

- **Archivo de datos:** `locumba_multiestacion_caudal.csv`
- **Ámbito geográfico:** Cuenca Locumba, Departamento de Tacna, Perú. 8 estaciones: Aricota La Yesera, Candarave, Coranchay, El Cairo, Jarumas, Mullini, Qda. Honda, Ticapampa.
- **Resolución temporal:** Mensual.
- **Periodo de registro:** Enero 1993 a Diciembre 1996 (48 meses).

## II. Fuentes de datos originales

- Sin documentación narrativa propia (archivo huérfano en `DATA_INSITU`, sin metadata asociada).
- **Cuenca de cada estación confirmada por el usuario** mediante el archivo `estaciones_hidrometricas_01.xlsx` (tabla "ESTACIONES HIDROMÉTRICAS"), que identifica explícitamente estas 8 estaciones con cuenca = LOCUMBA, departamento Tacna, provincias Candarave/Jorge Basadre/Tarata.

## III. Diccionario de variables

| Columna | Unidad | Descripción |
|---|---|---|
| `date` | - | Fecha (`YYYY-MM-DD`, primer día del mes) |
| `caudal_aricota_yesera_m3s` | m³/s | Caudal medio mensual, estación Aricota La Yesera |
| `caudal_candarave_m3s` | m³/s | Caudal medio mensual, estación Candarave |
| `caudal_coranchay_m3s` | m³/s | Caudal medio mensual, estación Coranchay |
| `caudal_el_cairo_m3s` | m³/s | Caudal medio mensual, estación El Cairo |
| `caudal_jarumas_m3s` | m³/s | Caudal medio mensual, estación Jarumas |
| `caudal_mullini_m3s` | m³/s | Caudal medio mensual, estación Mullini |
| `caudal_qda_honda_m3s` | m³/s | Caudal medio mensual, estación Quebrada Honda |
| `caudal_ticapampa_m3s` | m³/s | Caudal medio mensual, estación Ticapampa |

## IV. QA/QC

- Se transcribió tal cual desde el archivo original; sin relleno, interpolación ni corrección de outliers aplicada en esta fase.
- Solo se reportan caudales (m³/s); no se calculó volumen (MMC) por no contar con confirmación de la fórmula/criterio usado en la fuente original.

## V. Dominio espacial y coordenadas (según `estaciones_hidrometricas_01.xlsx`)

| Estación | Provincia | Distrito | Latitud | Longitud | Altitud (msnm) |
|---|---|---|---|---|---|
| Aricota La Yesera | Candarave | Quilahuani | -17.300 | -70.250 | 2839 |
| Candarave | Candarave | Candarave | -17.117 | -70.283 | 4100 |
| Coranchay | Candarave | Candarave | -17.117 | -70.283 | 4100 |
| El Cairo | Jorge Basadre | Ilabaya | -17.467 | -70.533 | 1130 |
| Jarumas | Candarave | Candarave | -17.333 | -70.233 | 2950 |
| Mullini | Candarave | Candarave | -17.333 | -70.233 | 2950 |
| Qda. Honda | Candarave | Camilaca | -17.167 | -70.517 | 4200 |
| Ticapampa | Jorge Basadre | Ilabaya | -17.467 | -70.533 | 1120 |

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- **Separación (acción explícita del usuario):** este archivo es un subconjunto de las 8 columnas de cuenca Locumba extraídas de `locumba_sama_caudales.csv`, que mezclaba 11 estaciones de 3 cuencas distintas (Locumba, Sama, Maure) bajo un solo nombre. Ver también `sama_multiestacion_caudal.csv` y `maure_kovirebofedal_caudal.csv` para las otras dos cuencas separadas del mismo archivo original.
- **Referencia cruzada:** no se fusionó con `locumba_puenteviejo_caudal_volumen.csv` (estación de control aguas abajo del mismo río, con datos 1972-1999) por tratarse de una red y un periodo distintos.
- Nombres de columna normalizados a snake_case.
