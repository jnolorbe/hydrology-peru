# Metadata — METADATOS DEL DATASET DE: PRECIPITACIÓN TOTAL MENSUAL - CUENCA DEL RÍO HUAURA (ESTACIONES REALES SENAMHI, VERSIÓN OBSERVADA Y EXTENDIDA, Y SUBCUENCAS VIRTUALES)

## I. Información general

Nombre del dataset    : precipitacion_cuenca_huaura.csv
Región / Cuenca       : Cuenca del río Huaura (Dpto. Lima, Prov. Huaura y Oyón)
Resolución temporal   : Mensual
Periodo total cubierto: 1963-09 a 2008-12 (varía por estación/subcuenca, ver
                         Sección III)
Unidad                : mm (precipitación total mensual)
Número de series      : 41 (11 estaciones reales SENAMHI -versión observada/
                         cruda- + 11 estaciones reales SENAMHI -versión
                         EXTENDIDA/completada, agregada en esta actualización-
                         + 19 subcuencas húmedas con precipitación areal
                         generada por modelo precipitación-altitud)
Propósito             : Insumo de control de calidad (QA/QC) y análisis de
                         estacionalidad/tendencias para contraste con series de
                         TWS (Total Water Storage) de GRACE-FO.
Fecha de procesamiento: Generado por procesamiento automatizado (Python /
                         pdfplumber / pandas) a partir de TOMO I y TOMO II.

## II. Fuentes de datos originales

FUENTE ÚNICA (no existe información de precipitación mensual comparable en el
informe INRENA 1998-2007; ese informe solo reportaba dos valores anuales
agregados por isoyetas, sin serie temporal):
  "Evaluación de Recursos Hídricos Superficiales en la Cuenca del Río Huaura"
  ANA - DCPRH - ALA Huaura. Lima, Diciembre 2010.
    - TOMO I (Informe Principal): archivo TOMO_I.pdf — Sección IV "Análisis y
      Tratamiento de la Precipitación" (pág. 58-64), metodología de estaciones
      virtuales.
    - TOMO II (Anexo): archivo TOMO_II.pdf
        Cuadro N° 4.1  Estaciones Meteorológicas - SENAMHI (metadata: 11
                        estaciones reales)
        Cuadro N° 4.2  Estaciones Satelitales (29 puntos de grilla climática,
                        NO utilizados como columnas de este dataset — se
                        usaron únicamente como insumo del modelo
                        precipitación-altitud del estudio de origen)
        Cuadros N° 4.3 a 4.13   Precipitación Total Mensual por estación real
                        (serie observada/cruda): Pachangara, Pachamachay,
                        Oyón, Surasaca, Tupe, Parquin, Picoy, Patón, Andajes,
                        Paccho, Pampa Libre.
        Cuadros N° 4.14 a 4.19  Análisis de Doble Masa (consistencia) — NO
                        incorporados como columnas (son gráficos/tablas de
                        control, no series de valor).
        Cuadros N° 4.20 a 4.30  Precipitación Total Mensual EXTENDIDA
                        (completada) por estación — INCORPORADA en esta
                        actualización como columnas "..._extendida_mm"; ver
                        Sección III.C y Sección IV, nota 2 (actualizada).
        Cuadro N° 4.31  Subcuencas (código, nombre, altitud media, área km2)
        Cuadros N° 4.32 a 4.51  Precipitación Total Mensual, Estaciones
                        Virtuales para Subcuencas Húmedas, periodo 1967-2008
                        (19 series, una por subcuenca).

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Date` | `date` |
| `precipitacion_estacion_andajes_mm` | `precipitacion_estacion_andajes_mm` |
| `precipitacion_estacion_pampalibre_mm` | `precipitacion_estacion_pampalibre_mm` |
| `precipitacion_estacion_paccho_mm` | `precipitacion_estacion_paccho_mm` |
| `precipitacion_estacion_pachangara_mm` | `precipitacion_estacion_pachangara_mm` |
| `precipitacion_estacion_pachamachay_mm` | `precipitacion_estacion_pachamachay_mm` |
| `precipitacion_estacion_oyon_mm` | `precipitacion_estacion_oyon_mm` |
| `precipitacion_estacion_surasaca_mm` | `precipitacion_estacion_surasaca_mm` |
| `precipitacion_estacion_tupe_mm` | `precipitacion_estacion_tupe_mm` |
| `precipitacion_estacion_parquin_mm` | `precipitacion_estacion_parquin_mm` |
| `precipitacion_estacion_picoy_mm` | `precipitacion_estacion_picoy_mm` |
| `precipitacion_estacion_paton_mm` | `precipitacion_estacion_paton_mm` |
| `precipitacion_subcuenca_auquimarcabajo_mm` | `precipitacion_subcuenca_auquimarcabajo_mm` |
| `precipitacion_subcuenca_auquimarcaalto_mm` | `precipitacion_subcuenca_auquimarcaalto_mm` |
| `precipitacion_subcuenca_picunchealto_mm` | `precipitacion_subcuenca_picunchealto_mm` |
| `precipitacion_subcuenca_picunchebajo_mm` | `precipitacion_subcuenca_picunchebajo_mm` |
| `precipitacion_subcuenca_pacchobajo_mm` | `precipitacion_subcuenca_pacchobajo_mm` |
| `precipitacion_subcuenca_pacchoalto_mm` | `precipitacion_subcuenca_pacchoalto_mm` |
| `precipitacion_subcuenca_yarucayabajo_mm` | `precipitacion_subcuenca_yarucayabajo_mm` |
| `precipitacion_subcuenca_yarucayaalto_mm` | `precipitacion_subcuenca_yarucayaalto_mm` |
| `precipitacion_subcuenca_checrasbajo_mm` | `precipitacion_subcuenca_checrasbajo_mm` |
| `precipitacion_subcuenca_checrasalto_mm` | `precipitacion_subcuenca_checrasalto_mm` |
| `precipitacion_subcuenca_yuracyacu_mm` | `precipitacion_subcuenca_yuracyacu_mm` |
| `precipitacion_subcuenca_huancoybajo_mm` | `precipitacion_subcuenca_huancoybajo_mm` |
| `precipitacion_subcuenca_huancoyalto_mm` | `precipitacion_subcuenca_huancoyalto_mm` |
| `precipitacion_subcuenca_huauramedio_mm` | `precipitacion_subcuenca_huauramedio_mm` |
| `precipitacion_subcuenca_huauraalto_mm` | `precipitacion_subcuenca_huauraalto_mm` |
| `precipitacion_subcuenca_paton_mm` | `precipitacion_subcuenca_paton_mm` |
| `precipitacion_subcuenca_surasaca_mm` | `precipitacion_subcuenca_surasaca_mm` |
| `precipitacion_subcuenca_cochaquillo_mm` | `precipitacion_subcuenca_cochaquillo_mm` |
| `precipitacion_subcuenca_quichas_mm` | `precipitacion_subcuenca_quichas_mm` |
| `precipitacion_estacion_andajes_extendida_mm` | `precipitacion_estacion_andajes_extendida_mm` |
| `precipitacion_estacion_pampalibre_extendida_mm` | `precipitacion_estacion_pampalibre_extendida_mm` |
| `precipitacion_estacion_paccho_extendida_mm` | `precipitacion_estacion_paccho_extendida_mm` |
| `precipitacion_estacion_pachangara_extendida_mm` | `precipitacion_estacion_pachangara_extendida_mm` |
| `precipitacion_estacion_pachamachay_extendida_mm` | `precipitacion_estacion_pachamachay_extendida_mm` |
| `precipitacion_estacion_oyon_extendida_mm` | `precipitacion_estacion_oyon_extendida_mm` |
| `precipitacion_estacion_surasaca_extendida_mm` | `precipitacion_estacion_surasaca_extendida_mm` |
| `precipitacion_estacion_tupe_extendida_mm` | `precipitacion_estacion_tupe_extendida_mm` |
| `precipitacion_estacion_parquin_extendida_mm` | `precipitacion_estacion_parquin_extendida_mm` |
| `precipitacion_estacion_picoy_extendida_mm` | `precipitacion_estacion_picoy_extendida_mm` |
| `precipitacion_estacion_paton_extendida_mm` | `precipitacion_estacion_paton_extendida_mm` |

---

Date : YYYY-MM-DD (día 1 de mes). Rango: 1963-01-01 a 2008-12-01.
--- A. ESTACIONES PLUVIOMÉTRICAS/CLIMATOLÓGICAS REALES (SENAMHI) ---
(fuente: Cuadros 4.3-4.13, serie observada/cruda, sin relleno)
Columna                                    | Estación     | Tipo | Cobertura real de datos
--------------------------------------------|--------------|------|---------------------------
precipitacion_estacion_andajes_mm           | Andajes      | PLU  | 1963-09 a 2007-12 (huecos internos)
precipitacion_estacion_pampalibre_mm        | Pampa Libre  | CO   | 1969-04 a 2008-12 (huecos internos)
precipitacion_estacion_paccho_mm            | Paccho       | PLU  | 1967-01 a 2008-12
precipitacion_estacion_pachangara_mm        | Pachangara   | PLU  | 1963-09 a 1987-12 (estación desactivada; ver
                                              |              |      | Sección IV, nota 3, sobre dic-1963)
precipitacion_estacion_pachamachay_mm       | Pachamachay  | PLU  | 1988-01 a 2008-12
precipitacion_estacion_oyon_mm              | Oyón         | CO   | 1963-09 a 2008-12
precipitacion_estacion_surasaca_mm          | Surasaca (pluv.)| PLU| 1967-09 a 1997-12
precipitacion_estacion_tupe_mm              | Tupe         | PLU  | 1969-08 a 1991-10
precipitacion_estacion_parquin_mm           | Parquin      | PLU  | 1965-03 a 2008-12 (ver nota 3, may-1965)
precipitacion_estacion_picoy_mm             | Picoy        | CO   | 1967-09 a 2008-12
precipitacion_estacion_paton_mm             | Patón        | PLU  | 1969-08 a 1977-10
--- B. SUBCUENCAS HÚMEDAS - PRECIPITACIÓN AREAL "VIRTUAL" ---
(fuente: Cuadros 4.33-4.51, generada por el estudio ANA-2010 mediante
regresión precipitación-altitud, ver Sección IV nota 1. Cobertura completa
1967-2008 en las 19 series, sin huecos.)
Columna                                       | Subcuenca         | Altitud media (msnm) | Área (km2)
------------------------------------------------|-------------------|------------------------|------------
precipitacion_subcuenca_auquimarcabajo_mm       | Auquimarca Bajo   | 2,869                  | 173.82
precipitacion_subcuenca_auquimarcaalto_mm       | Auquimarca Alto   | 4,372                  | 239.44
precipitacion_subcuenca_picunchealto_mm         | Picunche Alto     | 3,973                  | 23.70
precipitacion_subcuenca_picunchebajo_mm         | Picunche Bajo     | 2,736                  | 33.69
precipitacion_subcuenca_pacchobajo_mm           | Paccho Bajo       | 2,958                  | 36.57
precipitacion_subcuenca_pacchoalto_mm           | Paccho Alto       | 4,176                  | 66.06
precipitacion_subcuenca_yarucayabajo_mm         | Yarucaya Bajo     | 3,052                  | 66.58
precipitacion_subcuenca_yarucayaalto_mm         | Yarucaya Alto     | 4,225                  | 155.67
precipitacion_subcuenca_checrasbajo_mm          | Checras Bajo      | 3,032                  | 123.00
precipitacion_subcuenca_checrasalto_mm          | Checras Alto      | 4,303                  | 340.65
precipitacion_subcuenca_yuracyacu_mm            | Yuracyacu         | 4,516                  | 303.06
precipitacion_subcuenca_huancoybajo_mm          | Huancoy Bajo      | 2,954                  | 43.08
precipitacion_subcuenca_huancoyalto_mm          | Huancoy Alto      | 4,350                  | 150.65
precipitacion_subcuenca_huauramedio_mm          | Huaura Medio      | 3,072                  | 86.16
precipitacion_subcuenca_huauraalto_mm           | Huaura Alto       | 4,436                  | 675.72
precipitacion_subcuenca_paton_mm                | Patón             | 4,604                  | 41.83
precipitacion_subcuenca_surasaca_mm             | Surasaca          | 4,732                  | 52.80
precipitacion_subcuenca_cochaquillo_mm          | Cochaquillo       | 4,696                  | 50.77
precipitacion_subcuenca_quichas_mm              | Quichas           | 4,681                  | 35.62
Área total de las 19 subcuencas húmedas: 2,449.79 km2 (base para ponderar un
promedio areal total de la cuenca húmeda si se requiere una única serie
agregada mediante promedio ponderado por área).
--- C. ESTACIONES REALES - VERSIÓN EXTENDIDA/COMPLETADA (agregado en esta
actualización, a solicitud del usuario) ---
(fuente: Cuadros 4.20-4.30, TOMO II. Cobertura común 1967-2008, sin huecos,
salvo Paccho que se extiende desde 1965)
Columna                                                | Estación     | Cobertura
---------------------------------------------------------|--------------|------------
precipitacion_estacion_andajes_extendida_mm              | Andajes      | 1967-2008
precipitacion_estacion_pampalibre_extendida_mm           | Pampa Libre  | 1967-2008
precipitacion_estacion_paccho_extendida_mm                | Paccho       | 1965-2008
precipitacion_estacion_pachangara_extendida_mm            | Pachangara   | 1967-2008
precipitacion_estacion_pachamachay_extendida_mm           | Pachamachay  | 1967-2008
precipitacion_estacion_oyon_extendida_mm                  | Oyón         | 1967-2008
precipitacion_estacion_surasaca_extendida_mm              | Surasaca     | 1967-2008
precipitacion_estacion_tupe_extendida_mm                  | Tupe         | 1967-2008
precipitacion_estacion_parquin_extendida_mm               | Parquin      | 1967-2008
precipitacion_estacion_picoy_extendida_mm                 | Picoy        | 1967-2008
precipitacion_estacion_paton_extendida_mm                 | Patón        | 1967-2008
Estas 11 columnas son la contraparte SIN huecos de las columnas "estacion_*_mm"
(Sección III.A) para las mismas 11 estaciones — ver Sección IV nota 2 para la
metodología de relleno y la validación cruzada realizada.
Nota: valores vacíos (NaN) = mes sin dato reportado/generado en la fuente
(no implica lluvia cero).

## IV. QA/QC

1. MÉTODO DE PRECIPITACIÓN AREAL USADO POR LA FUENTE (Sección B): el estudio
   ANA-2010 NO usó pesos de Thiessen ni isoyetas manuales para generar las 19
   series de subcuencas — usó un MODELO DE REGRESIÓN PRECIPITACIÓN-ALTITUD
   (relación logarítmica P = a·ln(altitud) + b, ajustada por agrupación de
   subcuencas: Auquimarca, Cuenca Baja, Checras y Alto Huaura) que combina las
   11 estaciones reales SENAMHI y las 29 "estaciones satelitales" (grilla
   climática, Cuadro 4.2) como insumos de calibración. El resultado (series
   1967-2008 por subcuenca) ya viene "arealizado" por el estudio de origen;
   no fue necesario ni se realizó un recálculo adicional de precipitación
   areal en este procesamiento — se tomaron los valores tal como los reporta
   TOMO II (Cuadros 4.33-4.51). Las Láminas N°14 (Isoyetas Medias Anuales) del
   estudio ilustran el resultado final, pero el cálculo tabular fue por
   regresión altitud-precipitación, no por isoyetas trazadas manualmente.
2. VERSIONES "EXTENDIDA/COMPLETADA" (Cuadros 4.20-4.30) — INCORPORADAS EN
   ESTA ACTUALIZACIÓN: TOMO II reporta, para las 11 estaciones reales, tanto
   la serie observada/cruda (Cuadros 4.3-4.13, columnas "estacion_*_mm") como
   una versión con huecos rellenados ("extendida", Cuadros 4.20-4.30, columnas
   "estacion_*_extendida_mm"). Se mantienen AMBAS versiones en el dataset:
     - "estacion_*_mm"            -> trazabilidad directa con la medición,
                                      preserva los huecos reales (recomendada
                                      para QA/QC y detección de anomalías).
     - "estacion_*_extendida_mm"  -> serie continua 1967-2008 sin
                                      discontinuidades (recomendada para
                                      correlación/modelamiento continuo, p.ej.
                                      contraste directo con series mensuales
                                      de TWS de GRACE-FO).
   METODOLOGÍA DE COMPLETACIÓN (según TOMO I, sección 4.2.2): el estudio
   ANA-2010 generó la versión extendida con el software HEC-4 (Hydrologic
   Engineering Center, USACE - Cuerpo de Ingenieros de EE.UU.), estandarizando
   todas las estaciones a un período común 1967-2008 (42 años) mediante
   relleno de datos faltantes y extensión de registros por correlación entre
   estaciones vecinas, tras un análisis de consistencia previo (doble masa,
   Cuadros 4.14-4.19).
   VALIDACIÓN CRUZADA REALIZADA: las 11 series extendidas fueron extraídas de
   forma independiente directamente del PDF (TOMO II) y contrastadas contra
   el archivo `huaura_precipitacion_multiestacion.csv` proporcionado por el
   usuario (que resultó contener exactamente estas mismas series). La
   diferencia máxima encontrada fue 0.00 mm en 10 de las 11 estaciones y
   0.04 mm en Paccho (ruido de redondeo) — confirma que ambas extracciones
   son consistentes entre sí y con el documento fuente.
3. ANOMALÍAS DE CALIDAD DETECTADAS Y TRATAMIENTO:
   a) Estación Pachangara, diciembre de 1963: el valor original en el
      documento fuente (Cuadro N° 4.3, TOMO II) es 494.8 mm, muy por encima
      de cualquier otro diciembre registrado en la serie (máximo histórico
      de la estación: 269.6 mm en dic-1969) y sin columna de TOTAL anual que
      permita verificarlo (la fila 1963 no reporta total). Se decidió
      DESCARTAR este valor puntual (se dejó como NaN en el dataset) por alta
      probabilidad de error de transcripción/OCR en el documento fuente
      (posible confusión con una cifra de total parcial). Se recomienda no
      usar este dato sin verificar contra el documento físico/original si
      está disponible.
   b) Estación Parquin, mayo de 1965: valor de 241.0 mm, varias veces mayor
      que junio del mismo año (34.0 mm) y sin fila de TOTAL para verificar.
      Se PRESERVÓ el valor (no se descartó) por no contar con evidencia
      suficiente para tratarlo como error, pero se deja documentado como
      valor atípico a revisar con criterio hidrológico/experto antes de
      usarlo en análisis de extremos.
   c) Verificación automática: para las filas con columna TOTAL disponible
      en el documento fuente, se comparó la suma de los 12 meses contra el
      total reportado; no se encontraron discrepancias >5% en los casos con
      total disponible, lo que da confianza en la extracción tabular
      (pdfplumber) para el resto de la serie.
4. ESTACIONES REALES CON PERIODO CORTO O DESACTIVADO: Surasaca (pluv.,
   1967-1997), Tupe (1969-1991), Patón (1969-1977) y Pachangara (1963-1987)
   dejaron de operar antes de 2008. Para análisis de tendencia reciente
   (posterior a su cese), estas estaciones no aportan información; se
   recomienda usar Oyón, Paccho, Picoy, Parquin o Pampa Libre, que sí cubren
   hasta 2008-2009.
5. HOMONIMIA DE NOMBRES: "Surasaca", "Patón" y "Paccho/Cochaquillo" existen
   tanto como ESTACIÓN REAL (columnas "estacion_...") como SUBCUENCA VIRTUAL
   (columnas "subcuenca_..."); son series DISTINTAS (la real es la medición
   puntual; la virtual es el valor arealizado por regresión altitud para
   toda la subcuenca) y no deben confundirse ni sumarse.
6. RELACIÓN CON EL DATASET DE CAUDALES (Fase 2): la subcuenca "Surasaca"
   (código 1026, Cuadro 4.31) y la subcuenca "Cochaquillo" (código 1027)
   corresponden aproximadamente a las áreas de aporte de las lagunas
   reguladas Surasaca y Cochaquillo usadas en el dataset de caudales
   (`caudal_laguna_surasaca_m3s`), útiles para cotejar precipitación de
   cabecera vs. descarga regulada de esas lagunas.
7. CONVENCIÓN DE FECHA: cada registro mensual se fecha el día 1 del mes
   correspondiente.

## V. Dominio espacial y coordenadas

Bounding box de la cuenca del río Huaura (referencia general, TOMO I sección
2.2.1): Latitud 10°27'-11°13' S; Longitud 76°32'-77°39' W.
--- A. Coordenadas de las 11 estaciones reales (Cuadro N° 4.1, TOMO II) ---
(grados y minutos según fuente; segundos truncados/no confiables en el
documento original — usar con margen de incertidumbre de ~1')
Estación      | Tipo | Dpto/Prov/Dist              | Longitud | Latitud  | Altitud (msnm)
--------------|------|------------------------------|----------|----------|----------------
Andajes       | PLU  | Lima / Oyón / Andajes        | 76°54' W | 10°47' S | 3,950
Pampa Libre   | CO   | Lima / Huaura / Checras      | 76°58' W | 10°52' S | 1,800
Paccho        | PLU  | Lima / Huaura / Paccho       | 76°56' W | 10°57' S | 3,250
Pachangara    | PLU  | Lima / Oyón / Pachangara     | 76°49' W | 10°47' S | 3,600
Pachamachay   | PLU  | Lima / Huaura / Leoncio Prado| 76°50' W | 11°03' S | 4,200
Oyón          | CO   | Lima / Oyón / Oyón           | 76°46' W | 10°40' S | 3,641
Surasaca      | PLU  | Lima / Oyón / Oyón           | 76°47' W | 10°31' S | 4,553
Tupe          | PLU  | Lima / Huaura / Santa Leonor | 76°39' W | 11°00' S | 4,450
Parquin       | PLU  | Lima / Huaura / Santa Leonor | 76°43' W | 10°58' S | 3,590
Picoy         | CO   | Lima / Huaura / Santa Leonor | 76°44' W | 10°55' S | 2,990
Patón         | PLU  | Lima / Oyón / Oyón           | 76°42' W | 10°40' S | 4,150
Bounding box de las estaciones reales:
    Latitud  : 10°31' S a 11°03' S  (-11.05 a -10.517)
    Longitud : 76°39' W a 76°58' W  (-76.967 a -76.65)
--- B. Coordenadas de las 19 subcuencas virtuales ---
No se reportan centroides lat/long explícitos por subcuenca en TOMO II (solo
código, nombre, altitud media y área). Las subcuencas están anidadas dentro
de la cuenca del Huaura (unidad hidrográfica "Huaura", Cuadro 4.31); para
propósitos de bounding box espacial de estas 19 series, usar el bounding box
general de la cuenca del río Huaura (10°27'-11°13' S / 76°32'-77°39' W). Si
se requiere el polígono exacto de cada subcuenca, debe extraerse del SIG
del estudio (Lámina N°14 Isoyetas Medias Anuales y planos de subcuencas,
TOMO I/II, no incluidos en los PDF entregados como capa vectorial).
--- C. Estaciones satelitales (grilla, Cuadro N° 4.2, NO incluidas como
columnas del dataset, solo insumo del modelo de regresión de la fuente) ---
29 puntos en grilla regular de 0.1667° (10') cubriendo aprox.:
    Latitud  : -11.250 a -10.417
    Longitud : -77.583 a -76.583
FUENTE: ANA-DCPRH-ALA HUAURA, "Evaluación de Recursos Hídricos Superficiales
en la Cuenca del Río Huaura", Diciembre 2010, TOMO I y TOMO II.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `huaura_precipitacionv2.csv` a `huaura_precipitacion_multiestacion.csv`.
- Metadata consolidada y reformateada desde `huaura_precipitacion_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.

**Contenido adicional no clasificado de la fuente original** (preservado para no perder información):

METADATOS DEL DATASET DE: PRECIPITACIÓN TOTAL MENSUAL - CUENCA DEL RÍO HUAURA (ESTACIONES REALES SENAMHI, VERSIÓN OBSERVADA Y EXTENDIDA, Y SUBCUENCAS VIRTUALES)

================================================================================
