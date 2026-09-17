# Metadata — Metadata — Precipitación Total Mensual, Estaciones Cuenca Chancay-Huaral y aledañas (H&C, 1960–1999)

## I. Información general

- **Nombre de archivo del dataset:** `precipitacion_mensual_estaciones_chancay_huaral_1960_1999.csv`
- **Ámbito geográfico:** Cuenca Chancay-Huaral (aguas arriba de la Estación Santo Domingo) y cuencas aledañas (Huaura, Chillón, Lomas de Lachay), de donde provienen algunas estaciones usadas como apoyo regional.
- **Departamento / Región:** Lima, Perú (provincias de Huaral, Huaura, Canta).
- **Resolución temporal:** mensual.
- **Periodo de registro:** 1960-01 a 1999-12 (40 años, 480 meses) para todas las columnas, según lo declarado por la fuente ("PERIODO: 1960 1999" en cada hoja de estación).
- **Desfase respecto al año calendario:** ninguno (Ene-Dic = año calendario).
- **% de completitud:** variable por estación — ver tabla en la sección IV. La mayoría de estaciones está en 99.6–100%; la excepción es `precipitacion_carhuacayan_mm`, con 33.1% de datos faltantes (ver nota crítica en la sección IV).

## II. Fuentes de datos originales

| Fuente | Entidad / Autor | Año | Qué aportó específicamente |
|---|---|---|---|
| `1_0_Precipitacion.xls` (hojas `Carac`, `Huaros`, `Huayan`, `Lomas`, `Pachamachay`, `Pallac`, `Picoy`, `Pirca`, `StaCruz`, `Tupe`, `RioPallan`, `Carhua`) | Water & Land (consultora), PROFODUA — INRENA / Intendencia de Recursos Hídricos | Última modificación registrada del archivo: 2006 | Series mensuales de precipitación total mensual (mm), "Homogenizada y Completada", 1960–1999, para 12 estaciones. |
| `1_0_Precipitacion.xls` (hojas `Thiessen` y `Pp media de la Cuenca`) | Misma fuente | Ídem | Cálculo de precipitación areal mensual de la Cuenca Alta Chancay-Huaral (hasta Santo Domingo) por el **Método de Thiessen**, usando 8 de las 12 estaciones (ver Notas Técnicas). |
| `table-1789227983544.csv` (CUADRO N°01 del estudio hidrológico, en texto) | Estudio "Evaluación y Ordenamiento de los Recursos Hídricos de la Cuenca Chancay-Huaral" — datos adquiridos originalmente de estudios previos y SENAMHI | — | Metadata oficial de 10 estaciones meteorológicas: código, tipo, ubicación política y geográfica (coordenadas, altitud), cuenca y años de registro declarados. Reemplaza la lectura visual preliminar hecha directamente sobre la imagen del PDF, con mayor confiabilidad al venir en texto. |
| `table-1789228191652.csv` (CUADRO N°02 del estudio hidrológico, en texto) | Misma fuente | — | Metadata oficial de la estación hidrométrica Santo Domingo y 3 estaciones hidrométricas aledañas (usado para actualizar/confirmar la metadata de los datasets de caudal ya entregados). |
| `1_1_Precipitacion.xls` | Misma fuente | — | **No se usó en este dataset** (solo climatología sin dimensión de año); permanece como referencia de estadísticos descriptivos (promedio, máximo, P75) por estación, coherentes con esta serie mensual (validación cruzada: el promedio histórico de la hoja `Hoja1` de `1_1` coincide con el promedio de esta serie mensual para las 8 estaciones del Thiessen — ver Notas Técnicas). |

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `precipitacion_carac_mm` | `precipitacion_carac_mm` |
| `precipitacion_huaros_mm` | `precipitacion_huaros_mm` |
| `precipitacion_huayan_mm` | `precipitacion_huayan_mm` |
| `precipitacion_lomasdelachay_mm` | `precipitacion_lomasdelachay_mm` |
| `precipitacion_pachamachay_mm` | `precipitacion_pachamachay_mm` |
| `precipitacion_pallac_mm` | `precipitacion_pallac_mm` |
| `precipitacion_picoy_mm` | `precipitacion_picoy_mm` |
| `precipitacion_pirca_mm` | `precipitacion_pirca_mm` |
| `precipitacion_santacruz_mm` | `precipitacion_santacruz_mm` |
| `precipitacion_tupe_mm` | `precipitacion_tupe_mm` |
| `precipitacion_riopallanga_mm` | `precipitacion_riopallanga_mm` |
| `precipitacion_carhuacayan_mm` | `precipitacion_carhuacayan_mm` |
| `precipitacion_areal_thiessen_mm` | `precipitacion_areal_thiessen_mm` |

---

| Columna | Descripción | Unidad | Fuente | Fórmula |
|---|---|---|---|---|
| `date` | Primer día del mes calendario | YYYY-MM-DD | — | — |
| `precipitacion_carac_mm` | Precipitación total mensual, Estación Carac | mm | Medido/Completado (H&C) | — |
| `precipitacion_huaros_mm` | Precipitación total mensual, Estación Huaros | mm | Medido/Completado (H&C) | — |
| `precipitacion_huayan_mm` | Precipitación total mensual, Estación Huayan (climatológica ordinaria) | mm | Medido/Completado (H&C) | — |
| `precipitacion_lomasdelachay_mm` | Precipitación total mensual, Estación Lomas de Lachay | mm | Medido/Completado (H&C) | — |
| `precipitacion_pachamachay_mm` | Precipitación total mensual, Estación Pachamachay | mm | Medido/Completado (H&C) | — |
| `precipitacion_pallac_mm` | Precipitación total mensual, Estación Pallac | mm | Medido/Completado (H&C) | — |
| `precipitacion_picoy_mm` | Precipitación total mensual, Estación Picoy | mm | Medido/Completado (H&C) | — |
| `precipitacion_pirca_mm` | Precipitación total mensual, Estación Pirca | mm | Medido/Completado (H&C) | — |
| `precipitacion_santacruz_mm` | Precipitación total mensual, Estación Santa Cruz | mm | Medido/Completado (H&C) | — |
| `precipitacion_tupe_mm` | Precipitación total mensual, Estación Tupe | mm | Medido/Completado (H&C) | — |
| `precipitacion_riopallanga_mm` | Precipitación total mensual, Estación Río Pallanga | mm | Medido/Completado (H&C) — **estación sin metadata oficial de ubicación** (ver Notas Técnicas) | — |
| `precipitacion_carhuacayan_mm` | Precipitación total mensual, Estación Carhuacayán | mm | Medido/"Homogenizado y Completado" declarado en la fuente, pero **con 33% de datos faltantes reales** (ver Notas Técnicas) — **estación sin metadata oficial de ubicación** | — |
| `precipitacion_areal_thiessen_mm` | Precipitación areal mensual de la Cuenca Alta Chancay-Huaral (hasta Santo Domingo) | mm | Calculado por la fuente | **Método de Thiessen**: promedio ponderado de 8 estaciones (Carac, Huaros, Huayan, Pachamachay, Pallac, Pirca, Santa Cruz, Tupe) según su fracción de área de influencia sobre el total de 1850.3 km² de la cuenca alta. Pesos (fracción de área) declarados en la hoja `Thiessen` de la fuente: Carac 0.1988, Huaros 0.0553, Huayan 0.0322, Pachamachay 0.0425, Pallac 0.2682, Pirca 0.1182, Santa Cruz 0.1913, Tupe 0.0936. |

## IV. QA/QC

**Estaciones incluidas y su rol:**
- **10 estaciones con metadata oficial** (código, coordenadas, altitud) confirmadas en el CUADRO N°01 del estudio hidrológico (ver sección V): Carac, Santa Cruz, Pirca, Pallac, Huayan, Picoy, Tupe, Pachamachay, Huaros, Lomas de Lachay.
- **2 estaciones sin metadata oficial en las fuentes recibidas — Río Pallanga y Carhuacayán.** No aparecen en el CUADRO N°01 del estudio hidrológico ni se mencionan en el cuerpo de texto del PDF. Se incluyen en este dataset porque su serie mensual sí está en `1_0_Precipitacion.xls`, pero **sus coordenadas y altitud no están disponibles** en las fuentes de este proyecto. Si se cuenta con otra ficha de estación para ellas, se debe aportar para completar la sección V.
- **Precipitación areal (Thiessen):** el cálculo de la fuente usa únicamente 8 de las 12 estaciones (excluye Picoy, Lomas de Lachay, Río Pallanga y Carhuacayán) para representar la Cuenca Alta hasta Santo Domingo (1850.3 km² según la hoja `Thiessen`, que es consistente con el área de 1849.54–1850.31 km² ya reportada en los datasets de caudal, con la misma discrepancia menor entre fuentes).

**Valores marcados/corregidos/completados en la fuente:**
- Todas las series de estación llevan el título "Precipitación Homogenizada y Completada" en la hoja de origen. **Sin embargo, no todas están realmente completas:**

| Estación | % faltante real en esta entrega | Observación |
|---|---|---|
| Carac | 0.21% (1 mes) | — |
| Huaros | 0.00% | — |
| Huayan | 0.42% (2 meses) | — |
| Lomas de Lachay | 0.00% | — |
| Pachamachay | 0.21% (1 mes) | — |
| Pallac | 0.21% (1 mes) | — |
| Picoy | 0.00% | — |
| Pirca | 0.00% | — |
| Santa Cruz | 0.00% | — |
| Tupe | 0.00% | — |
| Río Pallanga | 0.00% | — |
| **Carhuacayán** | **33.12% (159 de 480 meses)** | **Discrepancia entre el rótulo de la fuente ("Homogenizada y Completada") y el contenido real**: los años 1960-1968 están enteramente vacíos y hay huecos adicionales dispersos. Se documenta tal cual viene, sin completar ni estimar valores por nuestra parte. |
| Precipitación areal Thiessen | 0.00% | Calculado únicamente a partir de las 8 estaciones sin datos faltantes en el rango usado; no depende de Carhuacayán ni Río Pallanga. |

- No se encontró en el estudio hidrológico (parte de texto extraíble) el detalle metodológico específico de cómo se completaron los pocos meses faltantes de las estaciones de precipitación (a diferencia del caso de caudal, donde sí se documentó el uso de HEC4). El estudio sí describe en general (sección 5.3, "Completación y extensión de la Información Pluviométrica") que existe un proceso análogo, pero el fragmento de texto disponible no fue revisado en profundidad en esta entrega.

**Validación cruzada con la climatología (`1_1_Precipitacion.xls`):** el promedio anual reportado en la hoja `Hoja1` de `1_1_Precipitacion.xls` (`Pm_Anual`) coincide, para las 8 estaciones usadas en el Thiessen, con el promedio de 40 años de esta serie mensual (ej. Carac: 367.94 mm/año en ambas fuentes; Pallac: 271.14 mm/año en ambas), lo que da confianza en que ambos archivos derivan de la misma serie base.

**Continuidad temporal:** sin huecos de calendario en ninguna columna (480/480 fechas presentes en el rango 1960-01 a 1999-12); los faltantes son valores `NA` dentro de fechas existentes, no meses ausentes del calendario.

**Valores negativos:** 0 casos en todas las columnas (consistente físicamente; la precipitación no puede ser negativa).

**Valores atípicos (IQR por mes calendario, no global):** se detectaron entre 5 (Carhuacayán) y 71 (Huayan) meses fuera de rango intercuartílico por columna. **Interpretación importante:** en las estaciones de esta cuenca la precipitación tiene una estacionalidad muy marcada (temporada seca casi nula de mayo a septiembre, con IQR cercano a cero en esos meses), por lo que el método IQR marca como "atípico" cualquier valor apenas distinto de cero en meses secos — esto es una **limitación conocida del método aplicado a series con esa estacionalidad extrema**, no necesariamente un error de dato. La mayoría de los atípicos detectados son de este tipo (valores bajos en meses secos). Se recomienda revisión experta si se requiere depurar la serie antes de calibrar contra GRACE-FO, en particular para separar "atípico por baja varianza estacional" de "atípico real por evento extremo húmedo".

**Consistencia caudal–precipitación:** no se realizó una verificación cruzada cuantitativa en esta entrega entre esta serie de precipitación y las series de caudal de Santo Domingo ya entregadas; podría hacerse como análisis adicional (p. ej. correlación cruzada o balance simplificado) si se solicita.

**Limitaciones conocidas:**
- Carhuacayán: un tercio de los datos faltante; usar con precaución o excluir según el propósito del análisis.
- Río Pallanga y Carhuacayán: sin coordenadas/altitud confirmadas — no se pueden ubicar en el dominio espacial de la sección V.
- No se completó, en esta entrega, un análisis de consistencia (doble masa, tendencias) propio; solo se documentó lo que el estudio ya declara.

## V. Dominio espacial y coordenadas

**Estaciones con metadata oficial (fuente: CUADRO N°01 del estudio hidrológico, confirmado en texto por `table-1789227983544.csv`):**

| Código | Estación | Tipo | Dpto/Prov/Dist | Longitud | Latitud | Altitud (msnm) | Cuenca | Lat. decimal | Lon. decimal |
|---|---|---|---|---|---|---|---|---|---|
| 155203 | Carac | Pluviométrica | Lima/Huaral/27 de Noviembre | 76°47' W | 11°11' S | 2600 | Chancay-Huaral | -11.1833 | -76.7833 |
| 152303 | Santa Cruz | Pluviométrica | Lima/Huaral/Sta. Cruz de A. | 76°38' W | 11°12' S | 3700 | Chancay-Huaral | -11.2000 | -76.6333 |
| 152158 | Pirca | Pluviométrica | Lima/Huaral/Atavillos Alto | 76°39' W | 11°14' S | 3255 | Chancay-Huaral | -11.2333 | -76.6500 |
| 155205 | Pallac | Pluviométrica | Lima/Huaral/Atavillos Bajo | 76°48' W | 11°21' S | 2333 | Chancay-Huaral | -11.3500 | -76.8000 |
| 154109 | Huayan | Climatológica Ordinaria | Lima/Huaral/Huaral | 77°07' W | 11°21' S | 350 | Chancay-Huaral | -11.3500 | -77.1167 |
| 155126 | Picoy | Pluviométrica | Lima/Huaura/Sta. Leonor | 76°44' W | 10°55' S | 2990 | Huaura | -10.9167 | -76.7333 |
| 155219 | Tupe | Pluviométrica | Lima/Huaura/Sta. Leonor | 76°39' W | 11°00' S | 4450 | Huaura | -11.0000 | -76.6500 |
| 155207 | Pachamachay | Pluviométrica | Lima/Huaura/Leoncio Prado | 76°50' W | 11°03' S | 4200 | Huaura | -11.0500 | -76.8333 |
| 155218 | Huaros | Pluviométrica | Lima/Canta/Huaros | 76°34' W | 11°24' S | 3585 | Chillón | -11.4000 | -76.5667 |
| 155133 | Lomas de Lachay | Pluviométrica | Lima/Huaura/Sayán | 77°22' W | 11°22' S | 300 | Lomas de Lachay | -11.3667 | -77.3667 |

**Estaciones sin metadata oficial en las fuentes recibidas:** Río Pallanga, Carhuacayán — coordenadas y altitud **no disponibles**.

**Estación hidrométrica de referencia (ya reportada en los datasets de caudal):** Santo Domingo — 77°03' W, 11°23' S, 697 msnm, lat/lon decimal ≈ -11.3833 / -77.0500 (código 202703, confirmado en texto por `table-1789228191652.csv`, sin ya necesidad de la reserva de "lectura visual" indicada previamente).

**Discrepancia de área de cuenca (persiste, se reporta sin resolver):**
- `2_0_Oferta_Hidrica-Balance-Asignacion.xls`: 1849.54 km².
- `ESTUDIO_HIDROLOGICO_CHANCAY-HUARAL.pdf` (texto): 1850.31 km².
- `1_0_Precipitacion.xls`, hoja `Thiessen`: 1850.3 km² (coincide con el valor del PDF, redondeado).

**Bounding box recomendado para extracción GRACE-FO Mascon** (margen 0.5° sobre las 10 estaciones con coordenadas oficiales + Santo Domingo):
- Latitud: **-11.90° a -10.42°**
- Longitud: **-77.87° a -76.07°**
- Este bounding box es más amplio que el calculado previamente solo con Santo Domingo, porque ahora incorpora estaciones de cuencas aledañas (Huaura, Chillón, Lomas de Lachay) usadas como apoyo en el análisis regional/Thiessen. Si el interés es exclusivamente la Cuenca Chancay-Huaral, puede acotarse usando solo las 5 estaciones propias de esa cuenca (Carac, Santa Cruz, Pirca, Pallac, Huayan) + Santo Domingo — puedo recalcularlo si se prefiere ese alcance más estrecho.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `Copia de chancay_huaral_precipitacion.csv` a `chancayhuaral_precipitacion_multiestacion.csv`.
- Metadata consolidada y reformateada desde `chancay_huaral_precipitacion_metadata.md` a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
