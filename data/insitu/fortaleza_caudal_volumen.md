# Metadata — METADATOS DEL DATASET DE CAUDALES MENSUALES HISTÓRICOS - RÍO FORTALEZA

## I. Información general

Nombre del Archivo: fortaleza_caudales_historico.csv
Ámbito Geográfico: Valle y cuenca del río Fortaleza, Distrito de Riego Barranca
Departamento del Perú: Lima (curso medio y bajo, provincia de Barranca); la cuenca
                       alta se origina en el departamento de Áncash (estribaciones
                       de la Cordillera Negra)
Resolución Temporal: Mensual
Periodo de Registro: Agosto de 1963 a Julio de 2003 (40 años hidrológicos,
                      480 registros mensuales)
NOTA: la plantilla de referencia indicaba "Agosto 1969 a Julio 2003 (34 años
hidrológicos, 408 registros)". Ese rango NO corresponde a los datos realmente
transcritos del Cuadro N° 2.2-1 (Anexo 1), que cubre 40 años hidrológicos
completos (1963/64 a 2002/03, 480 meses, sin vacíos). Se corrigió el campo para
reflejar fielmente el dataset entregado. Si el periodo 1969-2003 responde a un
recorte deliberado (p. ej. para alinear con otra fuente), se puede generar un
subconjunto filtrado a pedido.

## II. Fuentes de datos originales

- Documento base:
  "Informe Final: Propuesta de Asignaciones de Agua en Bloque - Volúmenes
  Anuales y Mensuales para la Formalización de los Derechos de Uso de Agua en
  el Valle de Fortaleza". PROFODUA (Programa de Formalización de los Derechos
  de Uso de Agua), Intendencia de Recursos Hídricos (IRH) - INRENA, Ministerio
  de Agricultura. Autor: Ramón Ochoa A. Barranca, diciembre 2004.
  Archivo: IF_FORTALEZA_PRINT_01MAR2005.doc
- Tabla de origen: Cuadro N° 2.2-1 "Estación LA RINCONADA, Caudal Medio
  Mensual (m³/s)", Anexo 1 - Oferta Hídrica. Fuente primaria de la propia
  tabla: Sistema de Información Hidrológica (SIH), Dirección General de
  Aguas y Suelos / INRENA.
- Insumo directo de esta transcripción: captura de imagen del Cuadro N° 2.2-1
  aportada por el usuario (archivo 1786414517165_image.png), leída mediante
  inspección visual ampliada (zoom por bloques de filas) dado que la tabla no
  existe como texto/objeto extraíble en el .doc original.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `fecha` | `date` |
| `caudal_fortaleza_m3s` | `caudal_fortaleza_m3s` |
| `volumen_fortaleza_MMC` | `volumen_fortaleza_mmc` |

---

El dataset contiene las siguientes columnas:
1. fecha
   Tipo: Fecha (YYYY-MM-DD)
   Descripción: Mes calendario del registro. Se fija el día en "01" como
   convención para representar el mes completo (el dato original es un
   promedio/total mensual, no un valor diario).
   Ejemplo: 1997-02-01 representa febrero de 1997.
2. caudal_estacion_m3s
   Tipo: Numérico (float), unidad m³/s
   Descripción: Caudal medio mensual observado en la estación hidrométrica
   La Rinconada, río Fortaleza, tal como aparece impreso en el Cuadro N° 2.2-1.
   Sin transformación adicional.
3. volumen_estacion_MMC
   Tipo: Numérico (float), unidad Millones de m³ (Hm³ / MMC)
   Descripción: Volumen mensual equivalente, calculado a partir del caudal:
       Volumen (MMC) = Caudal (m³/s) × 86,400 s/día × N_días_del_mes / 1,000,000
   N_días_del_mes se calculó exactamente para cada mes/año calendario
   (incluye años bisiestos, p. ej. febrero de 1968, 1972, ..., 2000).

## IV. QA/QC

- Convención de año hidrológico: cada fila del cuadro original agrupa
  AGO-DIC del "año 1" con ENE-JUL del "año 2" (p. ej. la fila "1996 1997"
  contiene agosto-diciembre de 1996 y enero-julio de 1997). Esta convención
  se resolvió correctamente al asignar el año calendario real a cada mes.
- Cobertura: 40 filas del cuadro original (años hidrológicos 1963/64 a
  2002/03) × 12 meses = 480 registros mensuales, sin datos faltantes (todas
  las celdas del cuadro original tenían un valor, incluyendo ceros).
- Valores en cero (0.00 m³/s): corresponden a meses de estiaje severo donde
  el río no registró escorrentía superficial en la estación (coherente con
  lo señalado en el informe: "en los meses de junio a octubre no llega a
  desembocar en el Océano Pacífico" en años secos). No se trata de datos
  faltantes ni de error de digitación.
- Verificación cruzada: la media de los 480 valores mensuales transcritos
  (3.57 m³/s) es consistente con la media reportada por el propio informe
  para el subperiodo 1964-2002 (3.548 m³/s, calculada en el Anexo 1 mediante
  la prueba de Smirnov-Kolmogorov); la pequeña diferencia se explica porque
  este dataset incluye además el año hidrológico 1963/64 y el 2002/03, que
  quedan fuera de esa ventana de 39 años usada en las pruebas estadísticas
  del informe.
- Limitaciones conocidas:
  a) La transcripción se hizo por lectura visual de una imagen (zoom manual),
     no por extracción automática de una hoja de cálculo o base de datos
     digital; existe riesgo residual de error de dígito en celdas puntuales,
     aunque los valores fueron cotejados contra el texto que acompañaba la
     imagen y coincidieron en su totalidad.
  b) El informe original señala que la estación La Rinconada "no domina todo
     el valle" y recomienda reubicarla (Puente Malvado, UTM 212,468E -
     8'856,638N); esto debe considerarse al usar la serie como referencia de
     "verdad de campo" para validar TWS de GRACE-FO.
  c) No se dispone de la incertidumbre instrumental ni del método de aforo
     mes a mes (el informe indica que en la mayoría de canales de reparto se
     afora por el método del flotador, no con aforadores Parshall).
  d) El año hidrológico 2002/03 extiende la serie un año más allá del rango
     usado en las pruebas de consistencia/homogeneidad (1964-2002) del
     informe original; ese último año no fue sometido a las mismas pruebas
     estadísticas de bondad de ajuste.

## V. Dominio espacial y coordenadas

1. Ubicación precisa de la estación (en decimales, WGS84):
   Estación La Rinconada (código 202301), río Fortaleza
   Latitud:  -10.4333
   Longitud: -77.7333
   Altitud:  300 msnm
   (Coordenadas originales del informe: 10°26' S, 77°44' O)
   Referencia adicional - desembocadura del río Fortaleza (Paramonga):
   Latitud:  -10.6482
   Longitud: -77.8609
2. Bounding Box recomendado para extracción satelital (GRACE / GRACE-FO
   NetCDF), en decimales:
   La cuenca del río Fortaleza es pequeña (~2,300 km², recorrido ~100 km,
   desde la Cordillera Negra en Áncash hasta el Pacífico en Paramonga), muy
   por debajo de la resolución nativa de las soluciones de GRACE/GRACE-FO
   (mascones de ~150-300 km de lado). Se recomienda un box ampliado con
   margen de "leakage" para no perder señal, e idealmente promediar junto
   con las cuencas vecinas (Pativilca, Supe) que comparten la misma unidad
   hidrográfica costera:
   - Latitud:   -9.0° a -11.5°
   - Longitud:  -79.0° a -76.5°
   Este box es una aproximación basada en la traza del río y la ubicación
   de la estación/desembocadura (no en un shapefile oficial de cuenca). Para
   un recorte hidrográficamente exacto se recomienda usar el límite oficial
   de la "Unidad Hidrográfica Cuenca Fortaleza" de la Autoridad Nacional del
   Agua (ANA) / SIAR Lima antes de la extracción satelital definitiva.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `fortaleza_caudales.csv` a `fortaleza_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `fortaleza_caudales_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.

**Contenido adicional no clasificado de la fuente original** (preservado para no perder información):

================================================================================
METADATOS DEL DATASET DE CAUDALES MENSUALES HISTÓRICOS - RÍO FORTALEZA
================================================================================
