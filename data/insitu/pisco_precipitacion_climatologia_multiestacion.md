# Metadata — Precipitación Total Mensual, Climatología (Cuenca del Río Pisco y cuencas vecinas)

## I. Información general

Nombre del dataset: pisco_precipitacion_climatologia_multiestacion.csv
Región/Cuenca: Cuenca del Río Pisco y cuencas vecinas, Departamento de Ica/Huancavelica, Perú.
Variable(s): Precipitación total mensual (mm), 6 estaciones.
Resolución temporal: Climatología mensual (12 filas, "Año Promedio Histórico 1964-2002" — un valor representativo por mes calendario, no serie año-por-año).
Cobertura temporal declarada en la fuente: 1964-2002 (39 años, periodo explícitamente indicado en el título del cuadro fuente).
Número de registros: 12 (uno por mes calendario, Ene-Dic) x 6 estaciones.
Valores faltantes: Ninguno.
Generado el: Fase 2 del flujo de trabajo QA/QC - Proyecto GRACE-FO (hallazgo incidental en fuente de Camaná-Majes).
Formato de fecha: Columna `mes`, entero 1-12 (climatología, no fecha calendario).

## II. Fuentes de datos originales

- Archivo de datos: `VARIABLES_CLIMATICAS.xls`, hoja "C 2.6" — Cuadro N° 2.6: "Precipitación Total Mensual Completada y Consistente (mm) - Año Promedio Histórico 1964-2002. Estaciones de la Cuenca del Río Pisco y Cuencas Vecinas".
- **Nota de procedencia:** este archivo fue entregado por el usuario como parte de las fuentes del informe de disponibilidad hídrica del valle de Camaná-Majes (`INFORME_FINAL_MAJES.doc`), pero la hoja "C 2.6" (junto con otras 7 hojas del mismo workbook) corresponde en realidad a la Cuenca del Río Pisco, una cuenca distinta sin relación geográfica con Camaná-Majes. No se encontró ninguna mención a esta cuenca ni a este cuadro en `INFORME_FINAL_MAJES.doc`; el documento fuente específico de origen (estudio de disponibilidad hídrica de la cuenca del Pisco del cual se extrajo este cuadro) no fue proporcionado, solo el cuadro de resultados ya procesado dentro del archivo Excel.
- Dato de "año promedio histórico 1964-2002" y "completada y consistente" en el título del cuadro indica que la fuente original ya aplicó completación de datos faltantes y análisis de consistencia antes de calcular el promedio climatológico; esos pasos NO fueron realizados por este proceso de estandarización, se hereda el valor ya procesado tal como aparece en el cuadro.
- **Alcance de esta fase:** por decisión explícita del usuario, de las 8 hojas de `VARIABLES_CLIMATICAS.xls` relativas a la cuenca del Pisco solo se digitaliza esta (precipitación), ya que el proyecto acotó el alcance de variables a procesar a: caudal/volumen, precipitación, evapotranspiración y nivel freático. Quedan fuera (no se generan datasets): catálogo de estaciones (hoja "C 1.1"), temperatura media/mín/máx (hojas "C 2.7", "C 2.8 - C 2.9", parte de "C 10, 11, 12"), evaporación de tanque (hoja "C 10, 11, 12", Cuadro 2.11 — nótese que es evaporación de tanque, no evapotranspiración calculada, por lo que no aplica el alcance aprobado), humedad relativa (hoja "C 10, 11, 12", Cuadro 2.12), e inventarios estáticos de fuentes de agua/lagunas/ríos por rango de caudal (hojas "C 2.26", "C 2.27", "C 28-29", que no son series de variable alguna sino conteos de infraestructura hídrica).

## III. Diccionario de variables

| Columna original (fuente) | Columna estandarizada |
|---|---|
| Fila `PISCO` (Cuadro 2.6) | `precipitacion_pisco_mm` |
| Fila `FONAGRO` (Cuadro 2.6) | `precipitacion_fonagro_mm` |
| Fila `BERNALES` (Cuadro 2.6) | `precipitacion_bernales_mm` |
| Fila `HUAMANI` (Cuadro 2.6) | `precipitacion_huamani_mm` |
| Fila `HUANCANO` (Cuadro 2.6) | `precipitacion_huancano_mm` |
| Fila `TICRAPO` (Cuadro 2.6) | `precipitacion_ticrapo_mm` |
| Columnas `Ene...Dic` | `mes` (entero 1-12) |

---

Columna                          | Tipo    | Unidad | Descripción
----------------------------------|---------|--------|------------------------------------------
mes                               | int     | 1-12   | Mes calendario estándar (1=enero...12=diciembre).
precipitacion_pisco_mm            | float   | mm     | Precipitación total media mensual, Estación Pisco (7 msnm).
precipitacion_fonagro_mm          | float   | mm     | Precipitación total media mensual, Estación Fonagro (50 msnm).
precipitacion_bernales_mm         | float   | mm     | Precipitación total media mensual, Estación Bernales (250 msnm).
precipitacion_huamani_mm          | float   | mm     | Precipitación total media mensual, Estación Huamaní (800 msnm).
precipitacion_huancano_mm         | float   | mm     | Precipitación total media mensual, Estación Huancano (1006 msnm).
precipitacion_ticrapo_mm          | float   | mm     | Precipitación total media mensual, Estación Ticrapo (2174 msnm).

## IV. QA/QC

1. **Climatología, no serie año-por-año:** el cuadro fuente está explícitamente etiquetado "AÑO PROMEDIO" para el periodo 1964-2002; cada valor es un promedio climatológico multianual para ese mes calendario, no una observación de un año específico. Dataset de 12 filas, sin fecha calendario real (columna `mes`), siguiendo la misma convención que `camana_balance_hidrico_climatologia.csv` y `chirapiura_climatologia_integrada.csv`.
2. **Gradiente altitudinal coherente:** se observa el patrón esperado en la vertiente occidental de los Andes: las estaciones costeras/bajas (Pisco 7 msnm, Bernales 250 msnm) muestran precipitación prácticamente nula todo el año (totales anuales de 1.4 mm y 0.6 mm respectivamente), mientras que la estación alta Ticrapo (2174 msnm) concentra precipitación estacional de verano (dic-mar, hasta 68.8 mm/mes, total anual 241.9 mm). No se detectaron valores negativos ni inconsistencias evidentes.
3. **"Completada y consistente":** el título del cuadro fuente indica que los datos ya fueron sometidos a completación de vacíos y análisis de consistencia por los autores originales, previo al cálculo del promedio climatológico. No se dispone del detalle de qué meses/años fueron completados ni con qué método, ya que solo se recibió el cuadro de resultados, no el informe/estudio fuente de la cuenca Pisco. Esto se documenta como limitación heredada, no verificable de forma independiente.
4. **Estaciones sin coordenadas completas:** ver Sección V — solo 2 de las 6 estaciones (Pisco, Bernales) tienen coordenadas verificables en el material disponible.
5. **Fuera de alcance (por decisión del usuario):** catálogo de estaciones, temperatura, evaporación de tanque, humedad relativa e inventarios estáticos de fuentes de agua de la misma hoja de cálculo — ver Sección II para el detalle completo de lo excluido.

## V. Dominio espacial y coordenadas

Coordenadas disponibles (fuente: hoja "C 1.1", Cuadro N°1 "Estaciones Hidro-Meteorológicas - Cuenca del Río Pisco", que solo catalogó 4 de las estaciones del workbook, 2 de las cuales coinciden con las 6 de este dataset):

| Estación | Latitud | Longitud | Altitud (msnm, según Cuadro 2.6) | Institución |
|---|---|---|---|---|
| Pisco | 13°45' S (-13.750°) | 76°13' W (-76.217°) | 7 | FAP |
| Bernales | 13°45' S (-13.750°) | 75°57' W (-75.950°) | 250 | SENAMHI |
| Fonagro | No disponible en la fuente | No disponible en la fuente | 50 | No disponible en la fuente |
| Huamaní | No disponible en la fuente | No disponible en la fuente | 800 | No disponible en la fuente |
| Huancano | No disponible en la fuente | No disponible en la fuente | 1006 | No disponible en la fuente |
| Ticrapo | No disponible en la fuente | No disponible en la fuente | 2174 | No disponible en la fuente |

Nota: no se estimaron coordenadas para Fonagro, Huamaní, Huancano ni Ticrapo a partir de ubicaciones aproximadas de localidades homónimas, para evitar introducir un valor no verificado en la fuente — si se requieren, deben obtenerse de una fuente cartográfica/catálogo SENAMHI adicional.

Bounding box: no se propone un bounding box GRACE-FO en esta fase, dado que 4 de las 6 estaciones no tienen coordenadas verificadas; puede calcularse una vez completada esa información.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Dataset nuevo, generado a partir de la hoja "C 2.6" del archivo `VARIABLES_CLIMATICAS.xls` (archivo entregado como fuente de Camaná-Majes, pero identificado como perteneciente a la cuenca del Pisco — ver Sección II).
- Nombre de ámbito `pisco` asignado por corresponder al nombre de la cuenca real de los datos (no al informe de donde se extrajo el archivo).
- Calificador `climatologia_multiestacion` siguiendo el precedente de `cabanillaslampa_precipitacion_climatologia_multiestacion.csv` y `chancayhuaral_precipitacion_multiestacion.csv`.
- Filas de estación (PISCO, FONAGRO, BERNALES, HUAMANI, HUANCANO, TICRAPO) transpuestas a columnas `precipitacion_<estacion>_mm`; columnas de mes en texto abreviado español transpuestas a columna entera `mes` (1-12).
- No se procesaron ni digitalizaron las demás 7 hojas del mismo archivo (catálogo de estaciones, temperatura, evaporación, humedad relativa, inventarios de fuentes de agua) por decisión explícita del usuario de acotar el alcance a caudal/volumen, precipitación, evapotranspiración y nivel freático — documentado en Sección II para referencia futura si se decide retomarlas.
