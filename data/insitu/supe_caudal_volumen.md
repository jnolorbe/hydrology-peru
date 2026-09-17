# Metadata — Caudal y Volumen Mensual, Estación Caral Las Minas (Río Supe)

## I. Información general

Nombre del archivo: `supe_caudal_volumen.csv`
Ámbito geográfico: Valle y cuenca del río Supe, Distrito de Riego Barranca, provincia de Barranca, departamento de Lima. Cuenca con área de drenaje total de 1,008 km² hasta la desembocadura en el Océano Pacífico y longitud máxima de recorrido de 92 km (dato del propio informe).
Resolución temporal: Mensual.
Periodo de registro: Agosto de 1962 a Julio de 2002 (40 años hidrológicos completos, 480 registros mensuales), sin meses faltantes — las 40 filas del cuadro original tienen valor en las 12 columnas, incluyendo ceros.
NOTA: el encabezado del propio Cuadro N° 2.2-1 indica "Periodo: (1963-2001)", que no coincide con el rango real de filas transcritas (1962/63 a 2001/2002, confirmado también por la fila "Número 1962-02 = 40" impresa al pie del mismo cuadro). Se prefirió el rango real de las filas transcritas, siguiendo el mismo criterio aplicado en `fortaleza_caudal_volumen.md` ante una discrepancia análoga en el informe gemelo de Fortaleza (mismo autor, mismo formato, mismo mes de impresión).

## II. Fuentes de datos originales

- Documento base: "Informe Final: Propuesta de Asignaciones de Agua en Bloque - Volúmenes Anuales y Mensuales para la Formalización de los Derechos de Uso de Agua en el Valle de Supe". PROFODUA (Programa de Formalización de los Derechos de Uso de Agua), Intendencia de Recursos Hídricos (IRH) - INRENA, Ministerio de Agricultura. Autor: Ramón Ochoa A. Barranca, diciembre 2004. Archivo aportado por el usuario: `IF_SUPE_PRINT_01MAR2005.doc` (solo lectura, no modificado).
- Tabla de origen: Cuadro N° 2.2-1, "Estación CARAL LAS MINAS, Caudal Medio Mensual (m³/s)", Anexo 1 - Oferta Hídrica. Fuente primaria de la propia tabla: Sistema de Información Hidrológica (SIH), Dirección General de Aguas y Suelos / INRENA.
- El `.doc` es un archivo binario antiguo (Composite Document V2) sin ninguna tabla nativa de texto: **todas** las tablas y gráficos del informe (incluido el Cuadro N° 2.2-1) están incrustados como objetos de imagen. No existe forma de extraer el cuadro como texto/objeto de datos del archivo original.
- Insumo directo de esta transcripción: el objeto de imagen del Cuadro N° 2.2-1 fue extraído del `.doc` (vía conversión a `.docx` con LibreOffice y extracción del objeto `word/media/image9.wmf`, renderizado a PNG de 794×1123 px — mayor resolución que la exportación HTML por defecto, que reduce la misma imagen a 539×928 px). Se leyó por inspección visual, en 5 bloques de 8 filas con zoom 3x, y se verificó **dos veces de forma independiente** contra la imagen ampliada antes de construir el CSV.
- A diferencia de `fortaleza_caudal_volumen.md` (donde el usuario aportó una captura externa en zoom para la transcripción), aquí no se contó con una imagen externa adicional; se usó la mejor resolución disponible dentro del propio `.doc`. El usuario acordó explícitamente construir la serie con esta transcripción y auditarla/corregirla después.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `fecha` (año hidrológico AGO-JUL, dos columnas "AÑO"/"AÑO") | `date` |
| `Caudal Medio Mensual (m³/s)` | `caudal_supe_m3s` |
| (no existe en la fuente) | `volumen_supe_mmc` (calculado) |

Columna | Tipo | Unidad | Descripción
---|---|---|---
`date` | fecha (YYYY-MM-DD) | - | Primer día del mes calendario. El cuadro original agrupa cada fila como año hidrológico AGO-JUL (p. ej. la fila "1997 1998" contiene agosto-diciembre de 1997 y enero-julio de 1998); se asignó el año calendario real a cada mes.
`caudal_supe_m3s` | float | m³/s | Caudal medio mensual observado en la estación Caral Las Minas, río Supe, tal como aparece impreso en el Cuadro N° 2.2-1. Sin transformación adicional.
`volumen_supe_mmc` | float | Millones de m³ (Hm³ / MMC) | Volumen mensual, **calculado** (no medido): `Volumen (MMC) = Caudal (m³/s) × 86,400 s/día × N_días_del_mes / 1,000,000`. `N_días_del_mes` calculado exactamente para cada mes/año calendario (incluye años bisiestos, p. ej. febrero de 1964, 1968, ..., 2000, vía `calendar.monthrange`).

## IV. QA/QC

1. **Discrepancia no resuelta entre las celdas del Cuadro N° 2.2-1 y su propia fila de estadísticos resumen** (Sumatoria/Media/Máximo/Mínimo, impresa al pie del mismo cuadro, en la misma imagen). Se calculó cada estadístico directamente a partir de las 40 filas transcritas y se comparó contra los valores impresos:

   | Mes | N | Suma (celdas) | Suma (impresa) | Media (celdas) | Media (impresa) | Máx (celdas) | Máx (impreso) | Mín (celdas) | Mín (impreso) |
   |---|---|---|---|---|---|---|---|---|---|
   | AGO | 40 | 14.10 | 16.19 | 0.35 | 0.39 | 2.18 | 2.18 | 0.00 | 0.00 |
   | SEP | 40 | 11.55 | 13.36 | 0.29 | 0.33 | 1.01 | 1.83 | 0.00 | 0.00 |
   | OCT | 40 | 14.01 | 15.83 | 0.35 | 0.39 | 1.61 | 1.85 | 0.00 | 0.00 |
   | NOV | 40 | 15.23 | 17.86 | 0.38 | 0.44 | 1.71 | 2.66 | 0.00 | 0.00 |
   | DIC | 40 | 41.55 | 56.90 | 1.04 | 1.35 | 10.38 | 13.24 | 0.00 | 0.00 |
   | ENE | 40 | 143.89 | 166.06 | 3.60 | 3.64 | 19.10 | 19.10 | 0.00 | 0.00 |
   | FEB | 40 | 304.44 | 321.17 | 7.61 | 7.61 | 27.29 | 27.29 | 0.00 | 0.00 |
   | MAR | 40 | 358.80 | 382.11 | 8.97 | 8.97 | 20.34 | 23.33 | 1.23 | 1.23 |
   | ABR | 40 | 178.85 | 186.82 | 4.47 | 4.47 | 12.80 | 12.80 | 0.57 | 0.57 |
   | MAY | 40 | 56.19 | 56.17 | 1.40 | 1.37 | 5.63 | 5.63 | 0.00 | 0.00 |
   | JUN | 40 | 27.67 | 27.66 | 0.69 | 0.69 | 3.92 | 3.92 | 0.00 | 0.00 |
   | JUL | 40 | 20.22 | 20.20 | 0.51 | 0.51 | 3.50 | 3.50 | 0.00 | 0.00 |

   Observaciones sobre este cuadro de verificación:
   - MAY, JUN, JUL: coinciden con las celdas dentro de ±0.02 (ruido de redondeo esperable).
   - FEB, MAR, ABR: la **Media** y el **Máximo** impresos coinciden exactamente con los calculados a partir de las celdas (evidencia de que la transcripción de esas columnas es correcta), pero la **Sumatoria** impresa NO coincide (321.17 vs 304.44 en FEB; 382.11 vs 358.80 en MAR; 186.82 vs 178.85 en ABR) — matemáticamente, si la media impresa (7.61) es correcta para 40 datos, la suma debería ser 304.4, no 321.17. Es decir, la propia fila de estadísticos es **internamente inconsistente entre sí** en estas columnas.
   - AGO, SEP, OCT, NOV, DIC, ENE: aquí ni la Media ni el Máximo impresos coinciden con las celdas (p. ej. NOV Máximo impreso = 2.66, pero ningún valor transcrito en esa columna supera 1.71; DIC Máximo impreso = 13.24, pero el máximo transcrito es 10.38).
   - **No se ajustó ningún valor de celda para forzar la coincidencia con el resumen impreso.** Los valores de celda fueron verificados dos veces de forma independiente contra la imagen ampliada y se mantienen sin cambios; se documenta la discrepancia como una inconsistencia de la fuente, pendiente de la auditoría del usuario contra el documento original o una imagen de mayor calidad.
   - Hipótesis no confirmada: podría deberse a que la fila de estadísticos fue calculada sobre una versión distinta/anterior de la serie y no se actualizó tras alguna revisión posterior de las celdas — un patrón de manejo de datos consistente con el hallazgo del punto 2 (contaminación cruzada confirmada en el mismo documento).

2. **Contaminación cruzada confirmada en el mismo documento** (mismo tipo de problema ya visto en Casma/Tumbes): lo que el informe etiqueta como "Cuadro N° 2.6-5" y "Gráfico N° 2.6-3" (Anexo 1) son en realidad capturas de pantalla de **otro informe** — la barra de tareas de Windows visible en la captura muestra "IF_PATIVILCA" y el contenido interno dice "Estación YANAPAMPA, Río PATIVILCA", no Supe. No se utilizó ningún valor de esas dos imágenes en este dataset. Se documenta únicamente como antecedente de la calidad de compilación del documento fuente (posible explicación adicional del punto 1).

3. **Ceros en la serie** (meses de estiaje, especialmente AGO-DIC en años secos, ej. 1967/68, 1968/69): consistentes con el texto del informe ("aporte hídrico dado por el río Supe... escorrentía directa sin regulación"; el valle depende de filtraciones en época de estiaje). No se trata de datos faltantes ni error de digitación.

4. **Pruebas de bondad de ajuste y homogeneidad** (realizadas por el propio informe sobre esta serie, capturas de pantalla del "Sistema de Información Hidrológica (Caudales)", Dirección General de Aguas y Suelos, Estación Caral Las Minas, Río Supe, código 202503):
   - Chi-cuadrado: Chi calculado 2.78 < Chi tabular 7.81 → los datos se ajustan a la distribución normal (95% confianza).
   - Smirnov-Kolmogorov: valor calculado 0.13 < valor tabulado 0.2267 → confirma el ajuste normal.
   - Análisis de salto (1963-1981 vs 1982-2001): estadístico |Tc|=3.24 > Tt=1.96 → el informe reporta cambio de media/desviación entre subperiodos, pero el texto principal concluye que "la información no requiere corrección por saltos y tendencias" (no se aplicó ninguna corrección a los datos de este dataset).
   - Análisis de tendencia: |Tc|=3.14 (media) > Tt=1.96 → estadísticamente significativo, pero tampoco se aplicó corrección (se respeta la decisión del informe original de no corregir).

5. **Idoneidad de la estación**: el propio informe señala que "el emplazamiento de esta estación hidrométrica no es la más adecuada, ya que no domina todo el valle" (sección 2.4) y recomienda reubicarla en "Jaiva La Banda" (UTM 241,150E / 8'795,844N). Esta limitación debe considerarse al usar la serie como "verdad de campo" para validar TWS de GRACE-FO.

6. **Datum de las coordenadas no especificado** en la fuente (UTM Este/Norte sin declarar WGS84 o PSAD56); se asumió WGS84 UTM zona 18S para la conversión a decimales (ver Sección V). No se verificó de forma independiente.

7. **Limitación de la transcripción**: leída de un objeto de imagen incrustado, no de una tabla de texto o base de datos digital descargable. Pese a la doble verificación visual independiente, existe riesgo residual de error de dígito en celdas puntuales — se solicita auditoría del usuario contra la imagen adjunta (`image9.wmf`/render PNG) o el documento original.

8. **No incluido en este dataset** (pendiente de decisión del usuario, reportado en el chat antes de generar este archivo):
   - Tabla "Disponibilidad Hídrica Mensual, Valle Supe" (MEDIO + persistencia V50/V60/V75/V95 por mes, en Hm³) — es un agregado climatológico derivado de esta misma serie, no una serie mensual año-por-año nueva.
   - Tabla climática CropWat/ETo de la Estación Paramonga (climatología de un año típico, usada para calcular la demanda de riego) — estación compartida por los 3 valles del PROFODUA (Fortaleza-Pativilca-Supe), ambigua en cuanto a a qué "ámbito" asignarla.
   - Tablas de demanda por bloques de riego y padrón de usuarios no agrarios — datos agrícolas/administrativos, fuera del alcance de variables del proyecto (caudal/volumen/precipitación/evapotranspiración/nivel freático).

## V. Dominio espacial y coordenadas

1. Estación Caral Las Minas (código SIH 202503), río Supe:
   - UTM zona 18S (datum no especificado en fuente, asumido WGS84): Este 231,454 / Norte 8'792,447
   - Decimales (WGS84): Latitud -10.9139, Longitud -77.4568
   - Altitud: 500 msnm
2. Punto de reubicación recomendado por el informe (no utilizado para esta serie, solo referencia): "Jaiva La Banda", UTM 241,150E / 8'795,844N → Latitud -10.8839, Longitud -77.3679 (mismo supuesto de datum).
3. Bounding box recomendado para extracción GRACE/GRACE-FO Mascon, en decimales: la cuenca del río Supe es pequeña (1,008 km², recorrido máx. 92 km), muy por debajo de la resolución nativa de las soluciones GRACE/GRACE-FO (mascones de ~150-300 km de lado). Siguiendo el mismo criterio ya documentado en `fortaleza_caudal_volumen.md` para la unidad hidrográfica costera compartida (Fortaleza-Pativilca-Supe):
   - Latitud: -9.0° a -11.5°
   - Longitud: -79.0° a -76.5°
   Aproximación basada en la traza del río y la ubicación de la estación (no en shapefile oficial). Se recomienda usar el límite oficial de la "Unidad Hidrográfica Cuenca Supe" (ANA/SIAR Lima) para un recorte hidrográficamente exacto antes de la extracción satelital definitiva.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Dataset nuevo. Ámbito `supe`, categoría `caudal_volumen`, sin calificador, siguiendo la convención de la guía.
- Fuente: `IF_SUPE_PRINT_01MAR2005.doc` (solo lectura, no modificado), aportado por el usuario en el chat.
- El `.doc` fue convertido a `.docx` con LibreOffice únicamente para extraer el objeto de imagen `word/media/image9.wmf` (Cuadro N° 2.2-1) a mayor resolución que la exportación HTML por defecto; el archivo fuente original no fue alterado.
- Transcripción del Cuadro N° 2.2-1 por inspección visual en 5 bloques de 8 filas con zoom 3x, verificada dos veces de forma independiente contra la imagen ampliada.
- Volumen calculado (no medido) con la fórmula estándar de la guía: `V(MMC) = Q(m³/s) × días_del_mes × 86400 / 1e6`, manejo de años bisiestos vía `calendar.monthrange` (Python).
- **Se detectó y documentó una discrepancia no resuelta** entre las celdas transcritas y la fila de estadísticos resumen del propio Cuadro N° 2.2-1 (Sección IV.1) — no se corrigió unilateralmente; queda pendiente de la auditoría acordada con el usuario.
- **Se detectó y documentó una contaminación cruzada** con el informe de Pativilca (Cuadro 2.6-5 / Gráfico 2.6-3 mal etiquetados, Sección IV.2) — no utilizada en este dataset.
- Pendiente de decisión del usuario: generar datasets adicionales para (a) la climatología de disponibilidad hídrica mensual derivada, y (b) la climatología ETo/CropWat de la Estación Paramonga (ver Sección IV.8).
