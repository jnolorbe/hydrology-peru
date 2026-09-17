# Metadata — Caudal y Volumen Mensual, Estación Coruca (Cuenca Sama, Tacna)

## I. Información general

- **Archivo de datos:** `sama_coruca_caudal_volumen.csv`
- **Ámbito geográfico:** Cuenca Sama, Departamento de Tacna, Perú.
- **Resolución temporal:** Mensual.
- **Periodo de registro:** Junio 2005 a Diciembre 2008 (40 meses).

## II. Fuentes de datos originales

- Sin documentación narrativa propia (archivo huérfano en `DATA_INSITU`, sin metadata asociada ni archivo con el que emparejarlo por contenido).
- **Cuenca y ubicación confirmadas por el usuario** mediante `estaciones_hidrometricas_01.xlsx` (tabla "ESTACIONES HIDROMÉTRICAS"): estación Coruca, cuenca Sama, provincia Tacna, distrito Inclán, Latitud -17.500°, Longitud -70.383°, Altitud 856 msnm. (La celda "Departamento" de esa fila del Excel dice "PUNO", lo que es inconsistente con el resto de la fila — provincia Tacna, distrito Inclán son ambos de la región Tacna, no Puno; se documenta tal cual el Excel pero se interpreta como un posible error de tipeo en la fuente del usuario, no corregido unilateralmente.)

## III. Diccionario de variables

| Columna | Unidad | Descripción |
|---|---|---|
| `date` | - | Fecha (`YYYY-MM-DD`, primer día del mes) |
| `caudal_coruca_m3s` | m³/s | Caudal medio mensual, estación Coruca |
| `volumen_coruca_mmc` | MMC | Volumen mensual, estación Coruca |

## IV. QA/QC

- Se transcribió tal cual desde el archivo original; sin relleno, interpolación ni corrección de outliers aplicada en esta fase.
- No se cuenta con información sobre la fórmula de conversión caudal→volumen usada en el archivo original; los valores de volumen se conservaron tal cual venían.

## V. Dominio espacial y coordenadas

- Estación Coruca: Latitud -17.500°, Longitud -70.383°, Altitud 856 msnm, Provincia Tacna, Distrito Inclán (ver nota sobre el campo "Departamento" en la Sección II).

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- **Resolución de caso pendiente (con el usuario):** este archivo no tenía ámbito identificable desde su propio contenido; el usuario aportó `estaciones_hidrometricas_01.xlsx`, que permitió confirmar la cuenca Sama y las coordenadas de la estación.
- Renombrado desde `coruca_caudal.csv` a `sama_coruca_caudal_volumen.csv`.
- **Referencia cruzada:** no se fusionó con `sama_multiestacion_caudal.csv` (misma cuenca, pero red y periodo distintos: 1993-1996 vs. 2005-2008).
- Nombres de columna normalizados a snake_case.
