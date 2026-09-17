# Metadata — Precipitación Total Mensual, Estaciones Adicionales Crudas (Sistema Regulador MAJES/RESERVA)

## I. Información general

Nombre del dataset: majes_precipitacion_estaciones_adicionales_multiestacion.csv
Región/Cuenca: 6 estaciones pluviométricas de la carpeta `MAJES/RESERVA/Pluviometria/Precip_original_senamhi` que NO forman parte del archivo consolidado `Pluviometria Completada.xls` (ver `majes_precipitacion_multiestacion.csv` para las otras 23 estaciones). Cuenca/subcuenca de cada estación no especificada en ningún archivo disponible para esta fase.
Variable(s): Precipitación total mensual (mm), 6 estaciones: Aguada Blanca, Casca, Characato, Jollojello, Lluclla, Lluta.
Resolución temporal: Mensual, serie año-por-año (año calendario Ene-Dic, NO año hidrológico como en `majes_precipitacion_multiestacion.csv`).
Cobertura temporal: distinta y en general corta para cada estación — ver tabla en Sección IV. Rango total de unión: 1961-03 a 2000-03.
Número de registros: 381 filas (unión de fechas de las 6 estaciones), con muchas celdas vacías por estación (los periodos no se superponen en su mayoría) — ver conteo de meses válidos por estación en Sección IV.
Valores faltantes: se dejan celdas vacías (no NaN explícito) donde la estación no tiene dato ese mes.
Generado el: Fase 2 del flujo de trabajo QA/QC - Proyecto GRACE-FO, carpeta MAJES/RESERVA.
Formato de fecha: YYYY-MM-DD (primer día de cada mes).

## II. Fuentes de datos originales

- 6 archivos de datos, exportaciones HTML de SENAMHI, carpeta `MAJES/RESERVA/Pluviometria/Precip_original_senamhi/`:
  - `AGUADA BLANCA-MES.XLS` (código estación 000797)
  - `CASCA-MES.XLS` (código 000707)
  - `CHARACATO-MES.XLS` (código 000836)
  - `JOLLOJELLO-MES.XLS` (código 152168)
  - `LLUCLLA-MES.XLS` (código 152169) — **nombre compartido con, pero independiente de**, la estación hidrométrica "LLUCLLA" (código 204714) del dataset `lluclla_caudal_volumen.csv` ya generado; son dos estaciones distintas de la misma red SENAMHI (una pluviométrica, una hidrométrica), no deben confundirse ni fusionarse.
  - `LLUTA -MES.XLS` (código 158202)
- Cada archivo trae, sin relleno de huecos ni consolidación: Código, Estación, Año (calendario), Ene...Dic.
- **A diferencia de `Pluviometria Completada.xls`, estos 6 archivos son crudos**: no hay evidencia de relleno ni de extensión de periodo — los años/meses sin registro simplemente no tienen valor.
- No se encontró ninguna tabla de coordenadas para estas 6 estaciones en ningún archivo de la carpeta `MAJES/RESERVA` disponible para esta fase (la hoja "Periodo de Registros" de `Precipitacion Anual Historica.xls`, usada para las otras 23 estaciones, no incluye a ninguna de estas 6).

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| Columna `Año` (año calendario) + `ENE...DIC` | `date` (reconstruida) |
| Valor de precipitación de cada mes, por estación | `precipitacion_<estacion>_mm` |

---

Columna                                  | Tipo    | Unidad | Descripción
--------------------------------------------|---------|--------|------------------------------------------
date                                        | date    | -      | Primer día del mes calendario (YYYY-MM-DD).
precipitacion_aguadablanca_mm               | float   | mm     | Precipitación total mensual, Estación Aguada Blanca (código 000797).
precipitacion_casca_mm                      | float   | mm     | Precipitación total mensual, Estación Casca (código 000707).
precipitacion_characato_mm                  | float   | mm     | Precipitación total mensual, Estación Characato (código 000836).
precipitacion_jollojello_mm                 | float   | mm     | Precipitación total mensual, Estación Jollojello (código 152168).
precipitacion_lluclla_mm                    | float   | mm     | Precipitación total mensual, Estación Lluclla — pluviométrica, código 152169 (NO confundir con la estación hidrométrica homónima).
precipitacion_lluta_mm                      | float   | mm     | Precipitación total mensual, Estación Lluta (código 158202).

## IV. QA/QC

1. **Cobertura real por estación (meses con dato / rango de fechas):**

   | Estación | Meses con dato | Rango |
   |---|---|---|
   | Aguada Blanca | 111 | 1991-01 a 2000-03 |
   | Casca | 50 | 1977-09 a 1981-10 |
   | Characato | 186 | 1961-03 a 1997-07 (con una interrupción total 1971-1977 y años 1978-1987 con filas presentes en la fuente pero totalmente vacías — ver punto 2) |
   | Jollojello | 47 | 1977-09 a 1981-07 |
   | Lluclla (pluviométrica) | 127 | 1977-09 a 1989-01 |
   | Lluta | 111 | 1963-11 a 1973-01 |

2. **Characato — años con fila presente pero enteramente vacía:** la fuente trae filas para los años 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1986 y 1987 (con el código y el año, pero sin un solo valor mensual); no se incluyen en este dataset por no aportar ningún dato, pero se documenta su ausencia como parte del hueco 1971-1990 de esta estación.
3. **Sin relleno de huecos aplicado por este proceso:** se transcribieron los valores tal como aparecen, sin ningún tipo de interpolación o estimación propia.
4. **Periodos muy cortos y sin solapamiento entre sí:** las 6 estaciones cubren tramos temporales casi disjuntos (ver tabla del punto 1); este dataset combinado en formato ancho tendrá, por tanto, muchas celdas vacías simultáneamente — es normal y no indica un error de construcción.
5. **Sin coordenadas ni información de cuenca para ninguna de las 6 estaciones** — ver Sección V.
6. **Sin revisión de outliers detallada** dado el volumen relativamente pequeño y disperso de esta fuente; si se detecta algún valor sospechoso en uso posterior, reportar para revisión puntual.

## V. Dominio espacial y coordenadas

No se encontraron coordenadas para ninguna de las 6 estaciones en los archivos disponibles para esta fase. Solo se dispone del código de estación SENAMHI de cada una (ver Sección II). No se estimaron coordenadas aproximadas para evitar introducir un valor no verificado — si se requieren, deben obtenerse de un catálogo SENAMHI adicional no incluido en esta carpeta.

Bounding box: no se propone en esta fase por falta de coordenadas.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Dataset nuevo, generado a partir de 6 archivos individuales de la carpeta `MAJES/RESERVA/Pluviometria/Precip_original_senamhi/`, identificados en la fase anterior como las estaciones que no forman parte de `Pluviometria Completada.xls`.
- Filas de año calendario (Ene-Dic) transpuestas directamente a fechas `date` (sin necesidad de conversión de año hidrológico, a diferencia de `majes_precipitacion_multiestacion.csv`).
- Las 6 estaciones se combinaron en un solo archivo ancho (`precipitacion_<estacion>_mm` por columna), siguiendo el mismo patrón que `majes_precipitacion_multiestacion.csv`, pese a la baja superposición temporal entre ellas — por decisión del usuario de tratarlas como una ronda separada pero consistente en formato con el dataset hermano de las 23 estaciones.
- Nombre de ámbito `majes` (RESERVA es una subcarpeta dentro de MAJES en la estructura de fuentes del usuario; el ámbito correcto es majes, no reserva); categoría `precipitacion`; calificador `estaciones_adicionales_multiestacion` para distinguirlo de `majes_precipitacion_multiestacion.csv` (las 23 estaciones de "Completada").
