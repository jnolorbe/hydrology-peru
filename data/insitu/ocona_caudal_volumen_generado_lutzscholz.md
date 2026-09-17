# Metadata — Caudal y Volumen mensual GENERADOS (Modelo Lutz Scholz), Río Ocoña — Cabecera del Valle y Estación Puente Ocoña

## I. Información general

- **Archivo de datos**: `ocona_caudal_volumen_generado_lutzscholz.csv`
- **Ámbito geográfico**: Cuenca del río Ocoña — dos puntos de interés: (a) Cabecera de Riego del Valle Ocoña, (b) punto homólogo al de la Estación Puente Ocoña (SENAMHI).
- **Departamento / Provincia / Distrito**: Arequipa / La Unión-Condesuyos-Camaná / Ocoña (cuenca del río Ocoña, PROFODUA ATDR Ocoña-Pausa).
- **Resolución temporal**: Mensual.
- **Periodo de registro**: 1965-01 a 2002-12 (38 años calendario completos).
- **Convención de año/fecha**: A diferencia del dataset `ocona_caudal_volumen.csv` (que usa año hidrológico Set-Ago), esta fuente organiza la serie por **año calendario Ene-Dic** — la columna "AÑO" del archivo original coincide directamente con el año calendario de las 12 columnas de esa fila. Verificado: no hay desfase que reconstruir.
- **% de completitud**: 100% (456/456 meses × 2 columnas, sin datos faltantes).
- **ADVERTENCIA IMPORTANTE — naturaleza de los datos**: **Ninguna de las dos columnas de caudal de este dataset es un registro aforado (medido).** Ambas son **series sintéticas generadas por el modelo hidrológico Lutz Scholz** (ver Sección II). No deben usarse como sustituto de un registro observado; ver Sección IV para el uso previsto y las limitaciones.

## II. Fuentes de datos originales

| Fuente | Documento | Entidad / año | Qué aportó específicamente |
|---|---|---|---|
| Fuente A | `Actualización al Guerrazo Estudio hidrológico.xls`, hoja `oferta ocoña`, Tabla 1.2 "Caudales Medios Mensuales Generados (m3/s) — Río Ocoña (Cabecera del Valle)", filas 70-107 | ATDR Ocoña-Pausa, s/f (documento de actualización del estudio "Guerrazo") | Serie generada 1965-2002 en el punto **Cabecera de Riego del Valle Ocoña**. Columna `caudal_cabeceravalle_m3s` de este CSV. |
| Fuente B | `Nuevas_Asiganaciones_Valle_Ocoña.xls`, hoja `Pérdidas en el río`, bloque derecho (columnas 16-30, encabezado "Caudales Medios Mensuales Generados (m3/s) — Río Ocoña (Estación Puente Ocoña)"), filas 7-44 | ATDR Ocoña-Pausa, s/f | Serie generada 1965-2002 en un punto identificado por la fuente como el homólogo de la **Estación Puente Ocoña**, usado en esa hoja para calcular las "pérdidas por conducción" del tramo del río entre ambos puntos. Columna `caudal_puenteocona_generado_m3s` de este CSV. **Contenido idéntico** (verificado valor a valor) al bloque de columnas 16-28 de `Nuevas_Asiganaciones_Valle_Chorunga.xls`, hoja `Pérdidas en el río` — ambos archivos comparten esta tabla. |
| Fuente C (contexto del modelo) | `Informe_Final_Validado_Ocoña2.doc` (Informe PROFODUA, Elmer F. Tancayllo Ccalla, ATDR Ocoña-Pausa, diciembre 2004), secciones 2.1 y 2.1.1 | ATDR Ocoña-Pausa, diciembre 2004 | Describe el modelo usado: *"Para estimar la disponibilidad de los caudales y/o volúmenes de escurrimiento de los ríos Ocoña y Chorunga se ha utilizado el Modelo Hidrológico de Transformación de Precipitación - Escorrentía Lutz Scholtz, con el cual se ha generado una serie sintética de descargas en las cabeceras de riego de los Valles Ocoña y Chorunga."* Modelo desarrollado por la Misión Alemana (1979-1980, Plan Meris II). El informe indica además (pág. correspondiente a la sección 2.1.1, párrafo final): *"Los resultados obtenidos mediante el modelamiento hidrológico se ha convalidado con la serie histórica de descargas registradas en la estación del Puente Ocoña"* — es decir, el propio informe reconoce que la serie generada en el punto "Puente Ocoña" es una aproximación validada contra el aforo real, **no el aforo mismo**. |
| Fuente D (cruce/validación cuantitativa) | `acopio_data_ocoña.xlsx` (tabla compilada por el usuario), hoja `Hoja1`, bloques "Ocoña Cabecera del Valle" y "Ocoña Estación Puente Ocoña", 1965-2002 | Compilación del usuario a partir de fuentes de este mismo estudio | Usada solo para validación cruzada. La columna "Cabecera del Valle" coincidía exactamente con la Fuente A. La columna "Estación Puente Ocoña" **no se encontró inicialmente en ningún archivo `Guerrazo.xls`** (se buscó por coincidencia exacta y aproximada en las 4 hojas, sin éxito) — se reportó la discrepancia al usuario, quien proporcionó los archivos "Nuevas Asignaciones" (Fuente B), donde el valor sí se encontró de forma exacta (fila 7, cols 18-19 = 52.07, 149.85 para ene-feb 1965). |

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| Tabla 1.2 "Caudales Medios Mensuales Generados... (Cabecera del Valle)" | `caudal_cabeceravalle_m3s` |
| Bloque "Caudales Medios Mensuales Generados... (Estación Puente Ocoña)" | `caudal_puenteocona_generado_m3s` |
| *(no existen en la fuente)* | `volumen_cabeceravalle_mmc`, `volumen_puenteocona_generado_mmc` |

---

| Columna | Descripción | Unidad | Fuente | Fórmula |
|---|---|---|---|---|
| `date` | Fecha del mes, día fijado en 01 | YYYY-MM-DD | — | Año calendario tal como aparece directamente en la columna "AÑO" de la fuente (sin desfase) |
| `caudal_cabeceravalle_m3s` | Caudal medio mensual **generado por el modelo Lutz Scholz** en el punto Cabecera de Riego del Valle Ocoña | m³/s | Modelado (Fuente A) | — |
| `volumen_cabeceravalle_mmc` | Volumen mensual correspondiente | MMC | Calculado (en esta estandarización) | `V = Q (m³/s) × (n_días_del_mes × 86,400 s) / 10⁶`, con días reales del mes/año (considera años bisiestos), redondeado a 2 decimales |
| `caudal_puenteocona_generado_m3s` | Caudal medio mensual **generado por el modelo Lutz Scholz** en el punto homólogo a la Estación Puente Ocoña | m³/s | Modelado (Fuente B) | — |
| `volumen_puenteocona_generado_mmc` | Volumen mensual correspondiente | MMC | Calculado (en esta estandarización) | Misma fórmula que arriba |

## IV. QA/QC

1. **Naturaleza sintética/modelada de AMBAS columnas — sin excepción**: ni `caudal_cabeceravalle_m3s` ni `caudal_puenteocona_generado_m3s` son mediciones de campo. Ambas provienen del modelo lluvia-escorrentía Lutz Scholz (Misión Alemana, 1979-1980), calibrado/aplicado con la información pluviométrica de la cuenca. Este dataset **no debe combinarse ni promediarse** con series aforadas (p. ej. `ocona_caudal_volumen.csv`, que sí contiene tramos de aforo real) sin dejar explícito en el análisis cuál es cuál.
2. **Dos puntos distintos, no confundir**: `caudal_cabeceravalle_m3s` corresponde al punto "Cabecera de Riego del Valle Ocoña" (área colectora 13,946.19 km², coordenadas 15°51'17.7"S / 73°6'0.6"W, altitud 580 m.s.n.m., según Cuadro/Figura Nº 1.1 del informe PROFODUA). `caudal_puenteocona_generado_m3s` corresponde a un punto ~81.73 km río abajo del anterior (ver ítem 3), que la fuente identifica como homólogo de la Estación Puente Ocoña real (SENAMHI) usada en `ocona_caudal_volumen.csv` — **pero aquí es un valor modelado, no el aforo de esa estación**. No promediar ni sumar ambas columnas como si fueran el mismo punto.
3. **Distancias documentadas en la fuente (hoja "Pérdidas en el río")**: la propia hoja de cálculo declara explícitamente, en celdas separadas, "Distancia respecto al mar" = 85 km para el punto Cabecera del Valle y = 3.27 km para el punto Puente Ocoña, y "Distancia recorrida" (entre ambos puntos) = 81.73 km. Estos valores fueron usados por la fuente para calcular una tabla adicional de "pérdidas por conducción" mes a mes (normalizando por distancia) — **esa tabla de pérdidas no se incorpora a este CSV** (está fuera del alcance de variables del proyecto: caudal, volumen, precipitación, ETP, nivel freático).
4. **Validación cruzada exacta contra las filas "MEDIA" de la fuente**: se comparó la media mensual (1965-2002, n=38) de cada columna de este CSV contra la fila "MEDIA" impresa en `Nuevas_Asiganaciones_Valle_Ocoña.xls` (hoja `Pérdidas en el río`, fila 46) y en `Actualización al Guerrazo...xls` (hoja `oferta ocoña`). Coincidencia **exacta** en los 24 valores (12 meses × 2 columnas), por ejemplo: ENE cabecera = 196.362 m³/s (fuente: 196.36186842105258); ENE Puente Ocoña generado = 145.817 m³/s (fuente: 145.81657894736838); DIC cabecera = 42.913; DIC Puente Ocoña generado = 39.063. Sin discrepancias.
5. **Validación cruzada contra `acopio_data_ocoña.xlsx` (compilación del usuario)**: coincidencia exacta valor a valor para ambas columnas, una vez identificado el archivo fuente correcto de la columna "Puente Ocoña" (ver Fuente D, Sección II) — el usuario había señalado inicialmente `Guerrazo.xls` como posible origen de esa columna, lo cual se verificó exhaustivamente (tolerancia exacta y luego aproximada, en las 4 hojas del archivo) y **no se encontró coincidencia**; se reportó la discrepancia en vez de forzar una atribución, y el usuario proporcionó los archivos "Nuevas Asignaciones" correctos donde sí se confirmó el origen.
6. **Consistencia interna entre archivos**: el bloque "Pérdidas en el río" es **idéntico** (mismos valores, misma estructura) en `Nuevas_Asiganaciones_Valle_Ocoña.xls` y en `Nuevas_Asiganaciones_Valle_Chorunga.xls` — ambos archivos comparten esta tabla de referencia común del valle Ocoña, no son fuentes independientes para este propósito.
7. **Continuidad temporal**: sin meses faltantes en 1965-01 a 2002-12 (456/456, ambas columnas).
8. **Volumen**: siempre calculado (nunca existe en la fuente para ninguno de los dos puntos); fórmula documentada en la Sección III, con manejo explícito de años bisiestos.
9. **Uso previsto / limitación principal**: esta serie generada existe porque, para el punto "Cabecera del Valle" (aguas arriba, sin estación de aforo real), es la única estimación de caudal disponible en las fuentes revisadas. Para el punto "Puente Ocoña" sí existe un aforo real (ver `ocona_caudal_volumen.csv`); la columna generada aquí se conserva porque es la que efectivamente usó el estudio PROFODUA 2004 para su balance hídrico y porque permite reproducir ese balance, no porque sea preferible al aforo real para otros análisis (p. ej. comparación con TWS-GRACE-FO, donde se recomienda preferir el dato aforado cuando esté disponible en el periodo de interés).

## V. Dominio espacial y coordenadas

| Punto | Latitud | Longitud | Altitud | Área colectora | Fuente |
|---|---|---|---|---|---|
| Cabecera de Riego Valle Ocoña | 15° 51' 17.7" S | 73° 6' 0.6" W | 580 msnm | 13,946.19 km² | Informe PROFODUA 2004, Cuadro/Fig. Nº 1.1 |
| "Puente Ocoña" (punto modelado, homólogo a la estación real) | *(no se listó con coordenadas propias en la tabla de cabeceras de la fuente; se identifica con la Estación Puente Ocoña real — ver nota)* | | 23 msnm (referencial) | 15,984.08 km² ("Area Cuenca hasta el Puente Ocoña", Informe PROFODUA 2004, texto sección 1) | Informe PROFODUA 2004 |

- **Coordenadas decimales (WGS84) — Cabecera de Riego Valle Ocoña**: -15.8549, -73.1002 *(conversión de 15°51'17.7" y 73°6'0.6")*.
- **Nota sobre el punto "Puente Ocoña generado"**: el informe PROFODUA 2004 no incluye una fila propia con coordenadas para este punto en su tabla de cabeceras de riego (Sección I, Fig. Nº 1.1, que solo lista Ocoña/Chorunga/Pausa/Cotahuasi). Se asume que corresponde a la misma ubicación física de la Estación Puente Ocoña (SENAMHI) documentada con coordenadas explícitas en el estudio hidrológico 2007 (16.42° S, 73.10° W, 23 msnm — ver `ocona_caudal_volumen.md`, Sección V), dado que el propio informe 2004 dice haber "convalidado" el modelo contra esa estación y que la distancia al mar declarada para este punto (3.27 km) es geográficamente compatible con la desembocadura del río Ocoña cerca de la localidad de Ocoña. **Esta asociación de coordenadas no está confirmada de forma explícita y numérica en la fuente 2004**; se reporta como supuesto razonable, no como dato verificado.
- **Bounding box recomendado para extracción GRACE-FO Mascon** (cubre ambos puntos, margen 0.5°):
  - Lat: -16.35° a -15.35°
  - Lon: -73.60° a -72.60°

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Datos extraídos con `xlrd` (lectura directa de celdas, sin OCR) de `Actualización al Guerrazo Estudio hidrológico.xls` (hoja `oferta ocoña`, filas 70-107) y de `Nuevas_Asiganaciones_Valle_Ocoña.xls` (hoja `Pérdidas en el río`, filas 7-44, columnas 16-30).
- Se generaron `volumen_cabeceravalle_mmc` y `volumen_puenteocona_generado_mmc` con la fórmula estándar del proyecto, calculada en Python con `calendar.monthrange` para el manejo correcto de años bisiestos.
- **Decisión tomada junto al usuario** (chat, 15-set-2026): ante la pregunta de si construir un dataset separado por punto o uno combinado, el usuario decidió unir Cabecera del Valle y Puente Ocoña generado como columnas de un mismo archivo, dado que comparten fuente, modelo y periodo.
- Se verificó la fidelidad de la extracción comparando las medias mensuales de cada columna contra las filas "MEDIA" impresas en la propia fuente (coincidencia exacta en los 24 valores) y contra la compilación independiente del usuario (`acopio_data_ocoña.xlsx`), tras resolver una discrepancia inicial sobre el archivo de origen correcto de la columna Puente Ocoña (ver Sección IV.5).
- Nombre de archivo y columnas normalizados a la convención `<ambito>_<categoria>_<calificador>.csv` / `<variable>_<punto>_<unidad>`.
