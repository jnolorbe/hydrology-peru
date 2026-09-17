# Metadata — Precipitación Areal Thiessen, Promedio Multianual por Subcuenca (Río Lurín)

## I. Información general

- **Archivo de datos:** `lurin_precipitacion_areal_thiessen_multianual.csv`
- **Ámbito geográfico:** Cuenca del Río Lurín, Departamento de Lima, Perú. 3 subcuencas: hasta puente Antapucro, cuenca total Lurín, y una intermedia.
- **Naturaleza:** climatología multianual (formato ancho, una fila por subcuenca, columnas ene_mm...dic_mm + total anual), no una serie temporal fechada.

## II. Fuentes de datos originales

- Sin metadata propia; es un archivo complementario/derivado del mismo procesamiento de `lurin_precipitacion_multiestacion.csv` (ver esa metadata para las fuentes originales y la red de estaciones: Manchay Bajo, Antioquia, Matucana, Langa, Santiago de Tuna, Huarochirí, San Lázaro de Escomarca, San José de Parac, Chalilla).

## III. Diccionario de variables

| Columna | Unidad | Descripción |
|---|---|---|
| `subcuenca` | - | Nombre de la subcuenca o "cuenca_total_lurin" |
| `area_km2` | km² | Área de la subcuenca |
| `ene_mm` ... `dic_mm` | mm | Precipitación areal Thiessen promedio multianual, por mes calendario |
| `total_anual_mm` | mm | Suma anual |
| `n_estaciones` | - | N° de estaciones pluviométricas usadas en el cálculo Thiessen para esa subcuenca |
| `estaciones_incluidas` | - | Nombres de las estaciones incluidas |

## IV. QA/QC

- Se transcribió tal cual desde el archivo original; sin relleno ni corrección de outliers aplicada en esta fase.
- El número de estaciones Thiessen varía por subcuenca (5 para "hasta puente Antapucro", 6 para la cuenca total), consistente con el área de influencia de cada polígono Thiessen.

## V. Dominio espacial y coordenadas

- Ver `lurin_precipitacion_multiestacion.csv` para las coordenadas de las estaciones pluviométricas usadas en el cálculo Thiessen.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Renombrado desde `lurin_precipitacion_areal_thiessen_promedio_multianual.csv`.
- Documentado como dataset complementario ("metadata anexa") de `lurin_precipitacion_multiestacion.csv`, dado que comparte la misma fuente Thiessen y red de estaciones.
- Nombres de columna ya estaban en snake_case; no requirió cambios.
