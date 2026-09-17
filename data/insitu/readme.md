# data/insitu — Subconjunto curado de datos in situ para el notebook 04

Este directorio contiene el subconjunto de `INSITU_estandarizado` (carpeta de trabajo doctoral,
no publicada en este repositorio) efectivamente usado en el notebook `04_insitu_validation_seasonality_and_enso_dipole.ipynb`
para validar dos hallazgos obtenidos con GRACE/GRACE-FO (notebooks 02 y 03):

1. La consistencia de la estacionalidad anual del TWS con la climatología in situ de caudal/volumen y precipitación.
2. El dipolo espacial norte-sur de la respuesta del TWS a El Niño costero (tipo E).

## Contenido

- `<archivo>.csv` / `<archivo>.md`: 72 datasets de caudal/volumen y precipitación (de los 75 originales
  filtrados por variable en `INSITU_estandarizado`), cada uno con su metadata de procedencia,
  QA/QC y coordenadas, heredada sin cambios de la fuente original. Se excluyeron 2 datasets adicionales
  (`cabanillaslampa`, `huancanesuches`) por cubrir un único año calendario, insuficiente para una
  climatología o para evaluar cobertura de eventos ENSO.
- `insitu_index.csv`: índice con el dominio hidrográfico AAA asignado a cada dataset (y el método:
  coordenadas verificadas por point-in-polygon, o nombre de cuenca), el período real de registro,
  y si el dataset se usó en la validación de estacionalidad y/o en la del dipolo ENSO.

## Qué no está aquí

Los 77 datasets completos de `INSITU_estandarizado` (incluyendo pozos, niveles freáticos,
evaporación/evapotranspiración, fuera del alcance de esta validación) permanecen solo en el
entorno de trabajo local, no se publican en este repositorio.

## Metodología de asignación de dominio y clasificación ENSO

Ver el notebook 04, secciones II a IV, para el detalle reproducible.
