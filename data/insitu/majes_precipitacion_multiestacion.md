# Metadata — Precipitación Total Mensual, Multiestación (Sistema Regulador MAJES/RESERVA, cuencas Colca/Chili/Siguas/Angostura)

## I. Información general

Nombre del dataset: majes_precipitacion_multiestacion.csv
Región/Cuenca: Red de 23 estaciones pluviométricas de cabecera de las cuencas Colca, Chili, Siguas y Angostura (sistema regulador del proyecto Majes), carpeta fuente `MAJES/RESERVA/Pluviometria`.
Variable(s): Precipitación total mensual (mm), 23 estaciones.
Resolución temporal: Mensual (serie año por año, NO climatología).
Cobertura temporal: 1963-08-01 a 2009-07-01 (46 años hidrológicos, Ago-Jul), **sin ningún mes faltante para ninguna estación** — ver Sección IV para la limitación importante sobre qué parte de esta cobertura corresponde al periodo de registro real de cada estación.
Número de registros: 552 meses x 23 estaciones (matriz completa, sin celdas vacías).
Valores faltantes: Ninguno en el sentido literal (todas las celdas tienen un valor numérico), pero ver Sección IV — una fracción importante de esos valores no son mediciones directas de la estación en ese momento.
Generado el: Fase 2 del flujo de trabajo QA/QC - Proyecto GRACE-FO, carpeta MAJES/RESERVA.
Formato de fecha: YYYY-MM-DD (primer día de cada mes).

**Archivo complementario de QA (obligatorio de revisar antes de usar este dataset):** `majes_precipitacion_qa_periodo_registro.csv` — misma estructura de fechas, una columna `periodo_<estacion>` por cada estación con uno de estos valores:
- `real`: el mes cae dentro del periodo de registro declarado para esa estación en la hoja "Periodo de Registros" de `Precipitacion Anual Historica.xls`.
- `extendido`: el mes cae FUERA del periodo de registro declarado, es decir, el valor en el CSV principal es una extensión/estimación regionalizada del estudio original, no una lectura directa de esa estación en esa fecha.
- `notacion_compuesta_no_parseada`: la estación tiene una notación de periodo de registro compuesta/intermitente en la fuente (ej. `"1963/82-86/91-93/09"`) que no se intentó interpretar automáticamente por ambigüedad — ver Sección IV, punto 3.
- `sin_catalogo`: la estación (Pampa de Arrieros) no aparece en absoluto en la hoja "Periodo de Registros"; no hay forma de saber qué parte de su serie es real vs. extendida.

## II. Fuentes de datos originales

- Archivo de datos principal: `Pluviometria Completada.xls`, 23 hojas (una por estación), tabla "ANEXO 1.1: PRECIPITACIÓN MENSUAL (mm)" por año hidrológico Ago-Jul, 1963-1964 a 2008-2009 (46 filas por hoja).
- Archivo de catálogo/coordenadas: `Precipitacion Anual Historica.xls`, hoja "Periodo de Registros" — Estación, Cuenca, Latitud, Longitud, Altitud, Periodo de registro, Gestión (Senamhi para todas). Cubre 22 de las 23 estaciones (falta Pampa de Arrieros).
- El mismo archivo `Precipitacion Anual Historica.xls` trae además las hojas "Serie Histórica" y "Serie Completada" (totales **anuales** por estación) — no se usaron como fuente porque son enteramente derivables sumando los 12 meses de `Pluviometria Completada.xls`; se usaron únicamente para una verificación cruzada puntual (ver Sección IV, punto 4).
- **Estaciones NO incluidas en esta fase:** 6 estaciones de la misma carpeta (`RESERVA/Pluviometria/Precip_original_senamhi`) que no forman parte de `Pluviometria Completada.xls` — Aguada Blanca, Casca, Characato, Jollojello, Lluclla (la de lluvia, distinta del dataset de caudal `lluclla_caudal_volumen.csv` ya generado), y Lluta. Por decisión del usuario, se procesarán en una ronda aparte (formato crudo año-calendario, sin relleno, sin coordenadas).

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| Nombre de hoja (estación), columnas `Ago...Jul` | `precipitacion_<estacion>_mm` |
| Columna `Año` (formato "AAAA-AAAA", año hidrológico) | `date` (reconstruida) |

Estaciones (slug de columna): cabanaconde, tisco, huambo, madrigal, chivay, sibayo, chuquibamba, condoroma, crucero (= Crucero Alto), imata, angostura, frayle (= El Frayle), pane (= Pañe), caylloma, yanque, calera, sumbay, visuyo, huanca, aplao, pampademajes (= Pampa de Majes), porpera, pampadearrieros (= Pampa de Arrieros).

---

Columna                              | Tipo    | Unidad | Descripción
----------------------------------------|---------|--------|------------------------------------------
date                                    | date    | -      | Primer día del mes calendario (YYYY-MM-DD).
precipitacion_<estacion>_mm             | float   | mm     | Precipitación total mensual en la estación indicada, según `Pluviometria Completada.xls`. **Puede ser un valor extendido/estimado fuera del periodo real de la estación — consultar siempre el archivo QA `majes_precipitacion_qa_periodo_registro.csv` antes de usar.**

## IV. QA/QC

1. **HALLAZGO PRINCIPAL — "Completada" no es solo relleno de huecos puntuales, sino extensión regionalizada del periodo completo:** se verificó (comparando contra el archivo crudo `chivay-mensual.XLS`) que `Pluviometria Completada.xls` efectivamente contiene valores donde la fuente cruda tiene celdas en blanco. Pero además, se detectó que para varias estaciones el archivo trae valores para **todo** el rango 1963-2009 aunque la propia hoja "Periodo de Registros" declare un periodo de funcionamiento real mucho más corto. Ejemplos verificados con el usuario antes de proceder:
   - Calera: periodo real declarado "1964-1973" (120 meses), pero el archivo tiene 552/552 meses con valor — **432 meses (78%) son extensión fuera del periodo real**.
   - Visuyo: periodo real "1963-1975" (149 meses reales de 552) — 403 meses (73%) extendidos.
   - Condoroma: periodo real "1977-2000" — 264 meses (48%) extendidos.
   - Yanque: periodo real "1963-1997" — 139 meses (25%) extendidos.
   - Angostura: periodo real "1970-2009" — 77 meses (14%) extendidos.
   - Chivay, Sibayo: extensión mínima (5 meses cada una, efecto de borde por el año hidrológico 1963-64 vs. periodo declarado "1964-2009").
   - Cabanaconde, Tisco, Huambo, Madrigal, Crucero Alto, Imata, El Frayle, Sumbay, Aplao, Pampa de Majes, Porpera: 0 meses extendidos, coinciden exactamente con su periodo real declarado.
   No se pudo determinar con qué método se generó esa extensión (probablemente correlación/regresión regional con estaciones vecinas, técnica común en estudios de disponibilidad hídrica, pero no documentada en los archivos disponibles). **Por decisión del usuario, se incluyó la serie completa de 46 años para las 23 estaciones, acompañada del archivo `majes_precipitacion_qa_periodo_registro.csv` que marca, mes a mes y estación por estación, si el valor cae dentro (`real`) o fuera (`extendido`) del periodo de registro declarado**, para que el usuario filtre según el uso que le dé (ej. para comparación con GRACE-FO 2002-2025 puede convenir usar los valores extendidos de todas formas, dado que es posterior al periodo real de varias estaciones).
2. **Fracción de relleno puntual (huecos cortos) dentro del periodo real:** no se cuantificó por separado del punto anterior; el archivo fuente no distingue explícitamente relleno puntual vs. extensión de periodo — ambos casos quedan mezclados bajo "Completada". Ver limitación en Sección I.
3. **4 estaciones con notación de periodo de registro compuesta/intermitente, NO interpretada automáticamente:** Chuquibamba (`"1963/82-86/91-93/09"`), Pañe (`"1963/73-1991/00"`), Caylloma (`"1963/78-2002/09"`), Huanca (`"1964/82-1997/09"`). Estas notaciones parecen indicar periodos de funcionamiento intermitente (con interrupciones), pero el formato exacto (años de 2 dígitos mezclados con rangos) es ambiguo y no se intentó adivinar la regla de expansión — se marcó cada una como `notacion_compuesta_no_parseada` en el archivo QA para las 552 filas de esas 4 estaciones. Si se requiere el detalle fino para estas 4, debe interpretarse manualmente la notación original (columna "Periodos de registro" de la hoja "Periodo de Registros") junto con el usuario.
4. **Pampa de Arrieros sin entrada en el catálogo:** esta estación tiene datos completos en `Pluviometria Completada.xls` pero no aparece en absoluto en la hoja "Periodo de Registros" de `Precipitacion Anual Historica.xls` — no hay forma de saber, para esta estación, qué parte de sus 46 años es periodo real vs. extendido. Se marcó como `sin_catalogo` en las 552 filas correspondientes.
5. **Verificación cruzada contra "Serie Histórica"/"Serie Completada" (totales anuales):** se verificó, para el caso de Chivay, que la suma de los 12 meses del año hidrológico 1964-1965 en `Pluviometria Completada.xls` (317.53 mm) coincide con el valor anual reportado para 1964 en la hoja "Serie Histórica" (139.4 para 1964 corresponde a un año calendario distinto — no se hizo una verificación exhaustiva mes-por-mes/año-por-año de las 23 estaciones contra las series anuales, dado el volumen; se recomienda una verificación más sistemática si se requiere mayor certeza).
6. **Sin outliers evidentes revisados en detalle:** dado el volumen (552 x 23 = 12,696 valores), no se hizo una revisión exhaustiva de outliers como sí se hizo para los datasets de caudal de esta misma carpeta (Angostura, Lluclla); si se detectan valores sospechosos en un análisis posterior, reportarlos para revisión puntual.

## V. Dominio espacial y coordenadas

Fuente: hoja "Periodo de Registros" de `Precipitacion Anual Historica.xls` (coordenadas en formato grados/minutos sexagesimales tal como aparecen en la fuente; no se convirtieron a decimal para evitar introducir un redondeo no verificado — el usuario puede convertir si lo necesita).

| Estación | Cuenca | Latitud Sur | Longitud Oeste | Altitud (msnm) | Periodo declarado |
|---|---|---|---|---|---|
| Cabanaconde | Colca | 15°37' | 71°59' | 3230 | 1963-2009 |
| Tisco | Colca | 15°21' | 71°27' | 4188 | 1963-2009 |
| Huambo | Colca | 15°44' | 72°06' | 3352 | 1963-2009 |
| Madrigal | Colca | 15°36' | 71°48' | 3262 | 1963-2009 |
| Chivay | Colca | 15°38' | 71°37' | 3651 | 1964-2009 |
| Sibayo | Colca | 15°29' | 71°27' | 3847 | 1964-2009 |
| Angostura | Angostura | 15°11' | 71°39' | 4220 | 1970-2009 |
| Chuquibamba | Colca | 15°50' | 72°40' | 2880 | 1963/82-86/91-93/09 (compuesto, no parseado) |
| Condoroma | Colca | 15°23' | 71°06' | 4250 | 1977-2000 |
| Crucero Alto | Colca | 15°46' | 70°55' | 4400 | 1963-2009 |
| Imata | Chili | 15°50' | 71°05' | 4495 | 1963-2009 |
| El Frayle | Chili | 16°09' | 71°11' | 4015 | 1963-2009 |
| Pañe | Colca | 15°25' | 71°04' | 4524 | 1963/73-1991/00 (compuesto, no parseado) |
| Caylloma | Angostura | 15°12' | 71°47' | 4320 | 1963/78-2002/09 (compuesto, no parseado) |
| Yanque | Colca | 15°39' | 71°35' | 3417 | 1963-1997 |
| Calera | Colca | 16°15' | 71°44' | 4450 | 1964-1973 |
| Sumbay | Colca | 15°58' | 71°21' | 4150 | 1963-2009 |
| Visuyo | Angostura | 15°37' | 71°46' | 4630 | 1963-1975 |
| Huanca | Siguas | No disponible en la fuente | No disponible en la fuente | 3080 | 1964/82-1997/09 (compuesto, no parseado) |
| Porpera | Colca | 15°21' | 71°19' | 4000 | 1963-2009 |
| Aplao | Colca | 16°05' | 72°40' | 510 | 1963-2009 |
| Pampa de Majes | Colca | 16°11' | 72°07' | 1440 | 1963-2009 |
| Pampa de Arrieros | **No disponible en la fuente (no está en el catálogo)** | No disponible | No disponible | No disponible | No disponible |

Nota: la columna "Cuenca" de la fuente usa "Angostura" como nombre de subcuenca para 3 estaciones (Angostura, Caylloma, Visuyo) — no confundir con el dataset `angostura_caudal_volumen.csv` de la estación hidrométrica homónima, que es un punto de aforo específico dentro de esta misma subcuenca.

Bounding box: no se calculó en esta fase (rango de coordenadas sexagesimales heterogéneo y con datos faltantes para 2 estaciones); puede derivarse de la tabla anterior si se requiere.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Dataset nuevo, generado a partir de las 23 hojas de `Pluviometria Completada.xls` (carpeta `MAJES/RESERVA/Pluviometria/`).
- Filas de año hidrológico (Ago-Jul) transpuestas a fechas calendario `date`; columnas de estación renombradas a `precipitacion_<estacion>_mm` (snake_case, sin tildes).
- Se generó el archivo QA complementario `majes_precipitacion_qa_periodo_registro.csv`, cruzando cada celda contra la hoja "Periodo de Registros" de `Precipitacion Anual Historica.xls`, por decisión explícita del usuario tras detectar que gran parte de la "completación" es en realidad extensión regionalizada fuera del periodo real de varias estaciones (ver Sección IV, punto 1).
- Se excluyeron del alcance de este dataset las 6 estaciones que no forman parte de `Pluviometria Completada.xls` (Aguada Blanca, Casca, Characato, Jollojello, Lluclla, Lluta) — pendientes para una ronda aparte, por decisión del usuario.
- Nombre de ámbito `majes` (RESERVA es una subcarpeta dentro de MAJES en la estructura de fuentes del usuario; el ámbito correcto es majes, no reserva — la red cubre varias subcuencas distintas: Colca, Chili, Siguas, Angostura, sin un único nombre de cuenca aplicable a las 23 estaciones); categoría `precipitacion`; calificador `multiestacion`, siguiendo el precedente de `huaura_precipitacion_multiestacion.csv` y `chancayhuaral_precipitacion_multiestacion.csv`.
