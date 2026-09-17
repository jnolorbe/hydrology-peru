# Metadata — Climatología de Caudales Multicuenca, Costa de Ancash (Sechín, Casma-Grande, Yautan, Casma, Huarmey, Nepeña)

## I. Información general

- **Archivo de datos:** `ancashcosta_caudal_climatologia_multicuenca.csv`
- **Ámbito geográfico:** 7 sistemas hídricos de la costa de Ancash: Río Sechín (2 puntos: Quillo y Puente Sechín), Río Casma-Grande/Tutuma, Río Yautan (confluencia con Casma), Río Casma (Puente Carretera), Río Huarmey/Huamba, Río Nepeña (San Jacinto).
- **Resolución temporal:** Climatología mensual (12 filas, mes 1-12), con estadísticos de persistencia (media, Q2, Q3, min, max) por sistema.
- **Formato de origen:** archivo Apple Numbers (`casma_climatologia.numbers`), convertido a CSV con `numbers-parser`.

## II. Fuentes de datos originales

- Documentación parcial en `casma_climatologia_metadata.txt`. **Advertencia de calidad de la fuente:** este `.txt` está incompleto (campo "Ámbito Geográfico" vacío, sección II "Fuentes documentales" vacía) y, al verificarlo contra otros metadatos del proyecto, se detectó que su sección III (diccionario de variables) está **contaminada con contenido copiado de la metadata de otro dataset** (`tumbes_climatologia.csv`): describe variables `oferta_Q3_tigre_MMC` y `demanda_valle_tumbes_MMC` de la Estación El Tigre / Valle de Tumbes, que no existen en este archivo ni tienen relación con las cuencas de Ancash. Esa sección de la fuente **no se usó**.
- Sí se usó la sección IV del `.txt` (coordenadas de estaciones), cuyo contenido — Puente Sechín, Puente Carrizal, Puente Quillo, Poctao, Sector Tutuma, Puente Yaután, San Jacinto (río Nepeña), Buenavista-Casma — es consistente con las 7 series de este dataset y sí se considera confiable.

## III. Diccionario de variables

Estructura general por sistema hídrico: `caudal_medio_<sistema>`, `caudal_Q2_<sistema>` (mediana), `caudal_Q3_<sistema>` (75% persistencia), `caudal_min_<sistema>`, `caudal_max_<sistema>` (m³/s; no todos los sistemas tienen las 5 variantes).

| Columna | Descripción |
|---|---|
| `mes` | Mes calendario (1-12) |
| `caudal_*_rio_sechin_quillo` | Estadísticos de caudal, Río Sechín en estación Quillo |
| `caudal_*_rio_casmagrande_tutuma` | Estadísticos de caudal, Río Casma-Grande en estación Tutuma |
| `caudal_*_rio_yautan` | Estadísticos de caudal, confluencia del río Yautan con el río Casma |
| `caudal_*_rio_casma` | Estadísticos de caudal, Río Casma en Puente Carretera |
| `caudal_*_rio_huarmey_huamba` | Estadísticos de caudal, Río Huarmey en estación Huamba |
| `caudal_*_rio_sechin_puente_sechin` | Estadísticos de caudal, Río Sechín en Puente Sechín (punto distinto de Quillo) |
| `caudal_*_rio_nepeña_san_jacinto` | Estadísticos de caudal, Río Nepeña en estación San Jacinto |
| `demanda_valle_casma_mmc`, `demanda_valle_sechin_mmc`, `demanda_valle_yautan_mmc` | Demanda hídrica agrícola mensual por valle, MMC |
| `etp_buenavista_mm` | Evapotranspiración potencial, estación Buenavista-Casma, mm |

## IV. QA/QC

- Se transcribió tal cual desde el archivo `.numbers` de origen; no se aplicó relleno, interpolación ni corrección de outliers en esta fase.
- Ver advertencia de contaminación cruzada de la fuente narrativa en la Sección II — se recomienda no usar la descripción de variables del `.txt` original si se recupera en el futuro sin antes verificarla contra este documento.

## V. Dominio espacial y coordenadas

Coordenadas de estaciones (tomadas de `casma_climatologia_metadata.txt`, sección IV, no contaminada):
- Puente Sechín: -9.4758°S, -78.2913°W
- Puente Carrizal: -9.4822°S, -78.2708°W
- Puente Quillo: -9.3242°S, -78.0445°W
- Sector Tutuma: -9.5362°S, -77.9455°W
- Puente Yaután: -9.5090°S, -77.9982°W
- San Jacinto (Nepeña): -9.16°S, -78.25°W (aprox.)
- Buenavista-Casma: -9.43°S, -78.20°W, 419 msnm

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Convertido desde formato Apple Numbers a CSV; columna de mes (texto Ene-Dic) convertida a entero `mes` (1-12); resto de columnas normalizadas a snake_case.
- **Hallazgo de auditoría reportado al usuario:** contenido cruzado/copiado por error entre `casma_climatologia_metadata.txt` y la metadata original de `tumbes_climatologia.csv` (ver Sección II). Se excluyó el contenido contaminado de esta metadata.
- Renombrado desde `casma_climatologia.numbers` (sin nombre de `.csv` previo, ya que no existía en ese formato en `DATA_INSITU`).
