# Metadata — Metadata — Dataset de Precipitación Mensual, Cuenca del Río Lurín

## I. Información general

- **Nombres de archivo:** `precipitacion_lurin_1964_2002.csv` (serie mensual 1964–2002) y `precipitacion_areal_thiessen_promedio_multianual.csv` (climatología areal oficial por método de Thiessen, agregado adicional — ver Sección IV)
- **Ámbito geográfico:** Cuenca del río Lurín y cuencas vecinas (Rímac, Mala) usadas como apoyo regional. Departamento de Lima, Perú.
- **Resolución temporal:** Mensual.
- **Periodo de registro:** 1964-01 a 2002-12 (39 años, 468 meses), igual para las 10 columnas.
- **Desfase respecto al año calendario:** Ninguno; año calendario Ene–Dic.
- **% de completitud:** 100% en todas las columnas (0 valores NA). Ver Sección IV: esta "completitud" es en parte artificial — las series fuente están explícitamente rotuladas como *"Completa y Extendida"*, es decir, ya vienen sin huecos porque fueron rellenadas por el estudio original, no porque no existieran datos faltantes en el registro crudo de SENAMHI.

---

## II. Fuentes de datos originales

| Fuente | Documento | Entidad emisora | Qué aportó |
|---|---|---|---|
| F1 | `Datos_precip.xls`, hojas `manchay`, `antioquia`, `Matucana`, `Langa`, `Tuna`, `Huarochiri`, `Escomarca`, `Parac`, `Chalilla` | SENAMHI (dato base), procesado en el estudio PROFODUA | Series de precipitación total mensual "Completa y Extendida" (mm), 1964–2002, con metadata de código de estación, lat/lon (grados-minutos), altitud y cuenca en cada hoja |
| F2 | `Datos_precip.xls`, hoja `Ppmedia` ("PROMEDIO CUENCA ALTA LURIN") | Estudio PROFODUA (cálculo propio) | Serie mensual etiquetada como precipitación promedio de la cuenca alta, altitud de referencia 3228.30 msnm |
| F3 | `textofinal-lurin.doc` (Informe Final PROFODUA, MOJ, Octubre 2004) | Consultor "MOJ" | Descripción metodológica: análisis de consistencia (saltos/tendencias), método de completación (MISSEL7), ecuación regional de precipitación, mención de métodos Thiessen e isoyetas para precipitación areal |

No se usó `INFORME_FINAL_LURIN.doc` (estudio 2006, Cuenca Alta) en esta entrega, por ser un estudio de alcance y metodología distintos (ver auditoría previa).

---

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `precipitacion_manchaybajo_mm` | `precipitacion_manchaybajo_mm` |
| `precipitacion_antioquia_mm` | `precipitacion_antioquia_mm` |
| `precipitacion_matucana_mm` | `precipitacion_matucana_mm` |
| `precipitacion_langa_mm` | `precipitacion_langa_mm` |
| `precipitacion_santiagodetuna_mm` | `precipitacion_santiagodetuna_mm` |
| `precipitacion_huarochiri_mm` | `precipitacion_huarochiri_mm` |
| `precipitacion_sanlazarodeescomarca_mm` | `precipitacion_sanlazarodeescomarca_mm` |
| `precipitacion_sanjosedeparac_mm` | `precipitacion_sanjosedeparac_mm` |
| `precipitacion_chalilla_mm` | `precipitacion_chalilla_mm` |
| `precipitacion_areal_mm` | `precipitacion_areal_mm` |

---

| Columna | Estación | Cuenca (según fuente) | Unidad | Fuente | Cálculo/origen |
|---|---|---|---|---|---|
| `date` | — | — | YYYY-MM-DD | — | — |
| `precipitacion_manchaybajo_mm` | Manchay Bajo | Lurín | mm | F1 | Completada/extendida (ver Sección IV) |
| `precipitacion_antioquia_mm` | Antioquia | Lurín | mm | F1 | Corregida por salto + completada (ver Sección IV) |
| `precipitacion_matucana_mm` | Matucana | **Rímac** (cuenca vecina, no Lurín) | mm | F1 | Completada (usada como base de correlación regional) |
| `precipitacion_langa_mm` | Langa | Lurín | mm | F1 | Completada/extendida por regresión múltiple |
| `precipitacion_santiagodetuna_mm` | Santiago de Tuna | Lurín | mm | F1 | Estación base de la completación (mayor confiabilidad, ver Sección IV); completada con su propio promedio multianual |
| `precipitacion_huarochiri_mm` | Huarochirí | **Mala** (cuenca vecina) | mm | F1 | Corregida por salto + completada por regresión múltiple |
| `precipitacion_sanlazarodeescomarca_mm` | San Lázaro de Escomarca | Lurín | mm | F1 | Corregida por salto + completada |
| `precipitacion_sanjosedeparac_mm` | San José de Parac | **Rímac** (cuenca vecina) | mm | F1 | Completada por regresión múltiple |
| `precipitacion_chalilla_mm` | Chalilla | Lurín | mm | F1 | Corregida por salto + completada |
| `precipitacion_areal_mm` | "Promedio Cuenca Alta Lurín" (altitud de referencia 3228.30 msnm) | Cuenca alta Lurín | mm | F2 | **Ver hallazgo de QA/QC abajo: en la práctica es una reescala lineal de la serie de Escomarca**, no un promedio ponderado independiente verificable con los datos disponibles |

---

## IV. QA/QC

### Naturaleza de las series — todas son "Completadas y Extendidas"
El título original de cada hoja lo indica explícitamente: *"Precipitación Mensual Completa y Extendida (mm)"*. Según `textofinal-lurin.doc`:
- Se hizo primero un análisis de consistencia (prueba T de Student para la media, prueba F de Fisher para la varianza) y de doble masa, usando **Santiago de Tuna** como estación base (mayor regularidad, menos puntos de quiebre).
- Estaciones **corregidas por salto** (ecuaciones de corrección, Cuadro Nº05 del Anexo I — no accesible como texto): **Antioquia, Huarochirí, San Lázaro de Escomarca, Chalilla** (y también Campo de Marte, no incluida en este dataset).
- **Manchay Bajo** no fue corregida (registro corto).
- Completación de datos faltantes con el programa MISSEL7 (Dr. José Salas, Colorado State University):
  - Santiago de Tuna: completada con su propio promedio multianual.
  - Antioquia, Matucana, San Lázaro de Escomarca: completadas por regresión lineal simple con Santiago de Tuna.
  - Langa, Huarochirí, San José de Parac, Chalilla: completadas por regresión lineal múltiple (confianza 95%) usando las 4 estaciones anteriores.
  - Manchay Bajo: completada por correlación con la estación Campo de Marte (1945–1972) y extendida hasta 2002 asumiendo un registro similar a los últimos años (este último paso es una extrapolación explícita, no una correlación estadística formal).
- El informe **no especifica, año por mes, qué valores puntuales fueron observados vs. generados/corregidos** dentro de cada serie; esa trazabilidad detallada solo estaría en los Cuadros N°I-04 a N°I-12 del Anexo I, que están como imagen (no extraíble como texto en esta entrega).

### Hallazgo de QA/QC — `precipitacion_areal_mm` NO es el promedio Thiessen oficial del estudio (investigado y confirmado con evidencia visual)

**Paso 1 — hallazgo estadístico:** al calcular la correlación y el cociente entre `precipitacion_areal_mm` y cada estación, se encontró una relación **exactamente proporcional y constante** con la estación **San Lázaro de Escomarca**:

> `precipitacion_areal_mm ≈ 0.8265 × precipitacion_sanlazarodeescomarca_mm` (razón prácticamente constante, desviación estándar de la razón = 0.0003, en 265 meses no nulos comparables)

**Paso 2 — verificación contra la fuente original (imagen):** dado que el texto de `textofinal-lurin.doc` menciona que el estudio calculó la precipitación areal por **dos métodos: Thiessen e isoyetas** (Cuadro N°08), se extrajeron y convirtieron a imagen legible los cuadros del Anexo I que estaban incrustados como objetos WMF (no como texto). Se recuperaron **3 tablas oficiales de precipitación areal por el método de Thiessen**, con polígono de área (km²) por estación y ponderación explícita — ver el archivo adjunto `precipitacion_areal_thiessen_promedio_multianual.csv`:

| Subcuenca | Área total (km²) | Estaciones usadas (ponderadas por polígono) | Total anual (mm) |
|---|---|---|---|
| Hasta Puente Antapucro (Cuadro N°1.13) | 1021.80 | Antioquia, Langa, Santiago de Tuna, San Lázaro de Escomarca, Chalilla (5) | 295.86 |
| Hasta Puente Manchay | 1443.53 (coincide con el área de la cuenca colectora de Manchay citada en el texto) | + Manchay Bajo (6) | 238.15 |
| Cuenca total del río Lurín | 1658.19 (coincide exactamente con el área total de drenaje citada en el texto) | Mismas 6 estaciones | 211.57 |

Estas 3 tablas **sí están explícitamente rotuladas "METODO DE THIESEN"** en la imagen original, con el área de cada polígono de Thiessen por estación, lo que confirma que **la metodología narrada en el texto (Thiessen) existe y es verificable**, pero:

- Son **promedios climatológicos multianuales por mes** (una sola fila por subcuenca), **no una serie año por año**. No pueden convertirse en una columna con fecha (`date`) comparable a las demás series de este dataset sin inventar una distribución interanual que la fuente no da.
- **No coinciden con la serie `Ppmedia`** del Excel: al comparar el promedio multianual de enero de `precipitacion_areal_mm` (69.74 mm, calculado sobre 1964–2002) contra el de la tabla Thiessen "hasta Antapucro" (58.59 mm), la diferencia es de ~19%, y el patrón se repite en los demás meses — son dos cálculos distintos, no la misma cifra con más o menos años.

**Conclusión:**
1. El método Thiessen sí fue usado por el estudio y ahora está documentado con datos reales (área de polígono por estación), pero **solo como promedio multianual**, no como serie mensual 1964–2002.
2. La columna `precipitacion_areal_mm` (`Ppmedia`) del Excel **no es ese cálculo Thiessen oficial** — es, según el análisis de razón constante, una reescala lineal de la estación Escomarca sola, de origen no documentado explícitamente en el texto disponible (posiblemente ligada a la ecuación regional altitud-precipitación, pero sin coincidir exactamente con ella tampoco).
3. **No se encontró la tabla de isoyetas** en las imágenes revisadas del Anexo I (solo se hallaron las 3 tablas Thiessen); pudiera existir en otra parte del anexo no revisada o solo como el Gráfico N°12 (mapa de isoyetas, sin tabla numérica asociada).

**Recomendación de uso:** para validación GRACE-FO, se recomienda **no usar `precipitacion_areal_mm` como "verdad de terreno" areal**. Si se necesita una precipitación areal representativa, es preferible usar directamente las 3 tablas Thiessen oficiales (`precipitacion_areal_thiessen_promedio_multianual.csv`) como referencia de climatología, combinadas con las 9 series mensuales estación por estación para años específicos, en vez de la columna `Ppmedia`.

### Valores negativos
0 valores negativos en las 10 columnas (correcto para precipitación).

### Continuidad temporal
Sin meses faltantes en el rango 1964–2002 para ninguna estación.

### Valores atípicos (IQR por mes calendario)
Se calcularon cuartiles por mes calendario para cada estación (no de forma global), dado el fuerte régimen estacional (lluvias concentradas en Ene–Abr, meses secos con muchos valores cero de May–Dic). Conteo de valores fuera de rango intercuartílico:

| Estación | Nº de meses atípicos (de 468) |
|---|---|
| Manchay Bajo | 42 |
| Antioquia | 54 |
| Matucana | 23 |
| Langa | 49 |
| Santiago de Tuna | 42 |
| Huarochirí | 35 |
| San Lázaro de Escomarca | 36 |
| San José de Parac | 31 |
| Chalilla | 18 |
| Precipitación areal | 36 |

**Interpretación:** el número de "atípicos" es relativamente alto porque en los meses secos (mayo–diciembre) la mayoría de los valores es cero o casi cero, por lo que el rango intercuartílico es muy estrecho y cualquier mes con lluvia moderada durante la estación seca se marca como atípico estadísticamente, aunque sea un evento real (lluvia ocasional de estación seca en la sierra). No se trata como error ni se corrige ningún valor; se deja para revisión manual si se requiere.

### Consistencia entre estaciones
La matriz de correlación mensual de cada estación contra `precipitacion_areal_mm` mostró valores entre 0.69 y 0.89 (razonable para estaciones de una misma cuenca con variación altitudinal), salvo Manchay Bajo (correlación negativa débil, -0.28), lo cual es esperable porque Manchay Bajo está en la costa (148 msnm, régimen de lluvia casi nulo) mientras que el resto son estaciones de sierra con régimen de lluvias de verano austral.

### Limitaciones conocidas
- Ninguna de las series es un registro crudo sin intervención: todas pasaron por corrección de saltos y/o completación estadística antes de llegar a este Excel.
- No se puede distinguir, mes a mes, cuáles valores son observados vs. generados/corregidos.
- `precipitacion_areal_mm` no es verificable como promedio Thiessen/isoyetas genuino (ver hallazgo arriba); se recomienda no usarla como "verdad de terreno" independiente para validar TWSA sin esta advertencia.
- Matucana y Parac pertenecen a la cuenca del Rímac, y Huarochirí a la cuenca del Mala — se incluyen porque el estudio las usó como apoyo regional, no porque estén dentro de la cuenca Lurín.

---

## V. Dominio espacial y coordenadas

| Estación | Cuenca | Lat (DMS) | Lon (DMS) | Lat decimal (WGS84, aprox.) | Lon decimal (WGS84, aprox.) | Altitud |
|---|---|---|---|---|---|---|
| Manchay Bajo | Lurín | 12°10' S | 76°52' W | -12.1667 | -76.8667 | 148 msnm |
| Antioquia | Lurín | 12°05' S | 76°30' W | -12.0833 | -76.5000 | 1839 msnm |
| Matucana | Rímac | 11°50' S | 76°22' W | -11.8333 | -76.3667 | 2479 msnm |
| Langa | Lurín | 12°06' S | 76°24' W | -12.1000 | -76.4000 | 2860 msnm |
| Santiago de Tuna | Lurín | 11°59' S | 76°31' W | -11.9833 | -76.5167 | 2921 msnm |
| Huarochirí | Mala | 12°08' S | 76°14' W | -12.1333 | -76.2333 | 3154 msnm |
| San Lázaro de Escomarca | Lurín | 12°11' S | 76°21' W | -12.1833 | -76.3500 | 3600 msnm |
| San José de Parac | Rímac | 11°48' S | 76°15' W | -11.8000 | -76.2500 | 3866 msnm |
| Chalilla | Lurín | 11°56' S | 76°20' W | -11.9333 | -76.3333 | 4050 msnm |
| "Cuenca Alta Lurín" (Ppmedia) | Lurín (agregado) | No aplica (dato areal) | No aplica | — | — | 3228.30 msnm (altitud de referencia declarada) |

Coordenadas dadas solo en grados y minutos en la fuente (sin segundos); la conversión a decimal asume minutos exactos, sin mayor precisión disponible. No se detectaron discrepancias entre fuentes para estas estaciones (a diferencia de Antapucro en el dataset de caudal/volumen).

**Bounding box recomendado para extracción GRACE-FO Mascon** (cubriendo las 9 estaciones + margen 0.5°):

- Lat: de -11.8000 - 0.5 = **-12.30** a -11.8333 + 0.5 = **-11.33**... calculado con extremos reales:
  - Lat mínima (más al sur): -12.1833 (Escomarca) → -0.5° = **-12.6833**
  - Lat máxima (más al norte): -11.8000 (Parac) → +0.5° = **-11.3000**
  - Lon mínima (más al oeste): -76.8667 (Manchay Bajo) → -0.5° = **-77.3667**
  - Lon máxima (más al este): -76.2333 (Huarochirí) → +0.5° = **-75.7333**

**Bounding box final sugerido: Lat -12.68 a -11.30, Lon -77.37 a -75.73**

---

*Elaborado conforme al protocolo del proyecto de auditoría y construcción de datasets hidrológicos — cuenca Lurín.*

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `lurin_precipitacion.csv` a `lurin_precipitacion_multiestacion.csv`.
- Metadata consolidada y reformateada desde `lurin_metadata_precipitacion.md` a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
