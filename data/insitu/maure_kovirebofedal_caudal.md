# Metadata — Caudal, Estación Kovire Bofedal (Cuenca Maure, Tacna)

## I. Información general

- **Archivo de datos:** `maure_kovirebofedal_caudal.csv`
- **Ámbito geográfico:** Cuenca Maure, Departamento de Tacna, Perú. 1 estación: Kovire Bofedal.
- **Resolución temporal:** Mensual.
- **Periodo de registro:** Enero 1993 a Diciembre 1996 (48 meses).

## II. Fuentes de datos originales

- Sin documentación narrativa propia (archivo huérfano en `DATA_INSITU`).
- **Cuenca confirmada por el usuario** mediante `estaciones_hidrometricas_01.xlsx`: Kovire Bofedal, cuenca Maure, provincia Tarata, distrito Ticaco, -17.2°/-69.917°, 4350 msnm.

## III. Diccionario de variables

| Columna | Unidad | Descripción |
|---|---|---|
| `date` | - | Fecha (`YYYY-MM-DD`, primer día del mes) |
| `caudal_kovire_bofedal_m3s` | m³/s | Caudal medio mensual, estación Kovire Bofedal |

## IV. QA/QC

- Se transcribió tal cual desde el archivo original; sin relleno, interpolación ni corrección de outliers aplicada.

## V. Dominio espacial y coordenadas

- Estación Kovire Bofedal: Latitud -17.200°, Longitud -69.917°, Altitud 4350 msnm, Provincia Tarata, Distrito Ticaco.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- **Separación (acción explícita del usuario):** columna única de cuenca Maure extraída de `locumba_sama_caudales.csv` (11 estaciones, 3 cuencas mezcladas). Ver también `locumba_multiestacion_caudal.csv` y `sama_multiestacion_caudal.csv`.
- **Referencia cruzada:** no se fusionó con `maure_chuapalca_caudal_volumen.csv` ni `maure_lafrontera_caudal_volumen.csv` (misma cuenca, pero estaciones, redes y periodos distintos).
- Nombre de columna normalizado a snake_case.
