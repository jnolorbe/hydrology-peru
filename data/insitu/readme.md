# data/insitu — Subconjunto curado de datos in situ para el notebook 04

Este directorio contiene el subconjunto de `INSITU_estandarizado` (carpeta de trabajo doctoral,
no publicada en este repositorio) efectivamente usado en el notebook `04_insitu_validation_seasonality_and_enso_dipole.ipynb`
para validar dos hallazgos obtenidos con GRACE/GRACE-FO (notebooks 02 y 03):

1. La consistencia de la estacionalidad anual del TWS con la climatología in situ de caudal/volumen y precipitación.
2. El dipolo espacial norte-sur de la respuesta del TWS a El Niño E (Pacífico oriental).

## Contenido

- `<archivo>.csv` / `<archivo>.md`: 72 datasets de caudal/volumen y precipitación (de los 75 originales
  filtrados por variable en `INSITU_estandarizado`), cada uno con su metadata de procedencia,
  QA/QC y coordenadas, heredada sin cambios de la fuente original. Se excluyeron 2 datasets adicionales
  (`cabanillaslampa`, `huancanesuches`) por cubrir un único año calendario, insuficiente para una
  climatología o para evaluar cobertura de eventos ENSO.
  Además, 3 archivos se conservan en esta carpeta pero el Notebook 04 los excluye de la validación
  (lista `EXCLUDED_FILES`, que imprime el motivo al ejecutarse), tras un control de calidad de sus
  climatologías:
  - `chili_caudal_volumen.csv`: 4 valores de caudal son años calendario (1925-08 = 1926,
    1954-09 = 1955, 1994-04 = 1995, 1994-06 = 1996 m³/s), error de transcripción al transponer la
    tabla fuente; su climatología resulta en diente de sierra sin estación húmeda/seca.
  - `rimac_caudal_volumen.csv`: sin señal hidrológica; ciclo anual plano (Chosica ≈ 35 m³/s todos los
    meses), valores uniformes entre 15 y 55 m³/s y autocorrelación mensual ≈ 0.06 (ruido aleatorio).
  - `canete_precipitacion_climatologia.csv`: meses mal etiquetados; pico en jun–ago, desfasado ~6 meses
    respecto a la serie mensual de las mismas estaciones (`canete_precipitacion.csv`, pico en feb),
    probablemente columnas en año hidrológico (sep–ago).
- `insitu_index.csv`: índice con el dominio hidrográfico AAA asignado a cada dataset (y el método:
  coordenadas verificadas por point-in-polygon, o nombre de cuenca), el período real de registro,
  y si el dataset se usó en la validación de estacionalidad y/o en la del dipolo ENSO.

## Qué no está aquí

Los 77 datasets completos de `INSITU_estandarizado` (incluyendo pozos, niveles freáticos,
evaporación/evapotranspiración, fuera del alcance de esta validación) permanecen solo en el
entorno de trabajo local, no se publican en este repositorio.

## Metodología de asignación de dominio y clasificación ENSO

Ver el notebook 04, secciones II a IV, para el detalle reproducible.
