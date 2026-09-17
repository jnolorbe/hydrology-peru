# Metadata — METADATOS DEL DATASET DE: CAUDALES Y VOLÚMENES MEDIOS MENSUALES - CUENCA DEL RÍO HUAURA Y CUENCAS VECINAS (PATIVILCA, CHANCAY-HUARAL)

## I. Información general

Nombre del dataset   : caudales_volumenes_cuenca_huaura.csv
Región / Cuenca      : Cuenca del río Huaura (con estaciones de referencia en
                        las cuencas vecinas de Pativilca y Chancay-Huaral,
                        usadas por el estudio de origen para fines de
                        regionalización y análisis comparativo)
País                 : Perú (Dpto. Lima; una estación -Yanapampa- en Dpto.
                        Áncash)
Resolución temporal  : Mensual
Periodo total cubierto: 1911-09 a 2008-12 (varía por estación, ver Sección III)
Unidades             : Caudal en m3/s (medias mensuales); Volumen en MMC
                        (Millones de Metros Cúbicos)
Número de estaciones/series: 6 (5 fluviométricas + 1 de descarga de laguna
                        regulada)
Propósito            : Insumo de control de calidad (QA/QC) y análisis de
                        tendencias/estacionalidad para contraste con series
                        de TWS (Total Water Storage) de GRACE-FO.
Fecha de procesamiento: Generado por procesamiento automatizado (Python /
                        pandas) a partir de las fuentes documentales listadas
                        en la Sección II.

## II. Fuentes de datos originales

FUENTE PRIORITARIA (2010, más reciente y de mayor cobertura):
  "Evaluación de Recursos Hídricos Superficiales en la Cuenca del Río Huaura"
  Ministerio de Agricultura - Autoridad Nacional del Agua (ANA) - Dirección de
  Conservación y Planeamiento de Recursos Hídricos - Administración Local de
  Agua (ALA) Huaura. Lima, Diciembre 2010.
    - TOMO I (Informe Principal): archivo TOMO_I.pdf
    - TOMO II (Anexo): archivo TOMO_II.pdf
        Cuadro N° 5.1 Estaciones Hidrométricas
        Cuadro N° 5.2 Descargas Medias Mensuales - Río Huaura - Estación Alco
                       Sayán (Fuente: ALA Huaura) [serie observada, 1967-2008]
        Cuadro N° 5.3 Descargas Medias Mensuales - Chancay Huaral - Estación
                       Santo Domingo (Fuente: ALA Chancay-Huaral) [1967-2008]
        Cuadro N° 5.4 Descargas Medias Mensuales - Río Pativilca - Estación
                       Yanapampa (Fuente: ALA Barranca) [1967-2008]
        Cuadro N° 5.5 Descargas Medias Mensuales - Río Huaura - Estación Alco
                       Sayán, versión "completado WEAP" [NO utilizada como
                       columna independiente; ver Sección IV, nota 3]
        Cuadro N° 5.6 Descargas Medias Mensuales - Río Chico - Punto de Aforo
                       Río Chico (Fuente: Junta de Usuarios Huaura,
                       "Completado WEAP") [1967-2008]
FUENTES COMPLEMENTARIAS (usadas solo para extender periodos NO cubiertos por
la fuente prioritaria, o para variables que la fuente prioritaria no
reporta):
  "Informe Final - Valle de Huaura" (INRENA - ATDR Huaura - J.U. Huaura,
  estudio de 1998, actualizado hasta 2004-2007). Archivos originales:
    - INFORME_FINAL1_VALLE_DE_HUAURA.doc
    - CUADRO_Nº_2_3___CAUDALES_HISTÓRICOS_RÍO_HUAURA.xls
        Hoja "CAUDAL HISTÓRICO": Caudal medio mensual (m3/s) Estación Alco
        Sayán, Periodo 1911-1997 (Fuente: SENAMHI - J.U. Huaura). Usada
        ÚNICAMENTE para completar 1911-1966 (periodo no cubierto por TOMO
        II).
    - CUADRO_Nº_2_3__2_5__CAUDALES_HISTÓRICOS_actualizado_RÍO_HUAURA.xls
        Hoja "SURASACA": Caudal medio mensual (m3/s) Estación Laguna
        Surasaca (salida de laguna, régimen regulado), Periodo 1967-1989
        (Fuente: SENAMHI). No existe equivalente en TOMO I/II; se mantiene
        como fuente única.
    - CUADRO_Nº_2_7__GRAFICO_Nº_2_1__REGIMEN_NATURAL_HUAURA.xls
        Hoja "CAUDAL NATURAL año calen": Caudal medio mensual (m3/s)
        restituido a régimen natural, Estación Alco Sayán, Periodo
        1911-2004 (metodología propia del estudio INRENA 1998, con
        actualización 1998-2004 por J.U. Huaura y ATDR). Sin equivalente en
        TOMO I/II; se mantiene como fuente única.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Date` | `date` |
| `caudal_rio_huaura_alco_sayan_m3s` | `caudal_rio_huaura_alco_sayan_m3s` |
| `volumen_rio_huaura_alco_sayan_mmc` | `volumen_rio_huaura_alco_sayan_mmc` |
| `caudal_natural_rio_huaura_alco_sayan_m3s` | `caudal_natural_rio_huaura_alco_sayan_m3s` |
| `volumen_natural_rio_huaura_alco_sayan_mmc` | `volumen_natural_rio_huaura_alco_sayan_mmc` |
| `caudal_rio_chico_m3s` | `caudal_rio_chico_m3s` |
| `volumen_rio_chico_mmc` | `volumen_rio_chico_mmc` |
| `caudal_rio_pativilca_yanapampa_m3s` | `caudal_rio_pativilca_yanapampa_m3s` |
| `volumen_rio_pativilca_yanapampa_mmc` | `volumen_rio_pativilca_yanapampa_mmc` |
| `caudal_rio_chancay_huaral_santo_domingo_m3s` | `caudal_rio_chancay_huaral_santo_domingo_m3s` |
| `volumen_rio_chancay_huaral_santo_domingo_mmc` | `volumen_rio_chancay_huaral_santo_domingo_mmc` |
| `caudal_laguna_surasaca_m3s` | `caudal_laguna_surasaca_m3s` |
| `volumen_laguna_surasaca_mmc` | `volumen_laguna_surasaca_mmc` |

---

Columna                                          | Unidad | Cobertura temporal      | Fuente prioritaria
--------------------------------------------------|--------|--------------------------|--------------------------------
Date                                              | YYYY-MM-DD (día 1 de mes)| 1911-01 a 2008-12       | -
caudal_rio_huaura_alco_sayan_m3s                  | m3/s   | 1911-09 a 2008-12        | TOMO II Cuadro 5.2 (1967-2008);
                                                    |        |                          | INFORME_FINAL Cuadro 2.3 (1911-1966)
volumen_rio_huaura_alco_sayan_mmc                 | MMC    | 1911-09 a 2008-12        | Calculado (ver Sección IV)
caudal_natural_rio_huaura_alco_sayan_m3s          | m3/s   | 1911-09 a 2004-05        | INFORME_FINAL Cuadro 2.7 (única
                                                    |        |                          | fuente; TOMO I/II no la reporta)
volumen_natural_rio_huaura_alco_sayan_mmc         | MMC    | 1911-09 a 2004-05        | Calculado
caudal_rio_chico_m3s                              | m3/s   | 1967-01 a 2008-12        | TOMO II Cuadro 5.6 ("Completado WEAP")
volumen_rio_chico_mmc                             | MMC    | 1967-01 a 2008-12        | Calculado
caudal_rio_pativilca_yanapampa_m3s                | m3/s   | 1967-01 a 2008-12        | TOMO II Cuadro 5.4
volumen_rio_pativilca_yanapampa_mmc               | MMC    | 1967-01 a 2008-12        | Calculado
caudal_rio_chancay_huaral_santo_domingo_m3s       | m3/s   | 1967-01 a 2008-12        | TOMO II Cuadro 5.3
volumen_rio_chancay_huaral_santo_domingo_mmc      | MMC    | 1967-01 a 2008-12        | Calculado
caudal_laguna_surasaca_m3s                        | m3/s   | 1967-01 a 1989-08        | INFORME_FINAL hoja SURASACA (única
                                                    |        |                          | fuente; TOMO I/II no la reporta)
volumen_laguna_surasaca_mmc                       | MMC    | 1967-01 a 1989-08        | Calculado
Notas de columnas:
- "alco_sayan" corresponde al río Huaura (estación histórica compuesta, ver
  Sección IV).
- "natural" = caudales restituidos a régimen natural (remueve el efecto de
  operación de los embalses de Surasaca y Cochaquillo aguas arriba); útil
  para comparar contra la señal hidrológica "natural" que podría reflejar
  TWS de GRACE-FO sin intervención antrópica de regulación.
- "pativilca_yanapampa" y "chancay_huaral_santo_domingo" son estaciones de
  CUENCAS VECINAS (no pertenecen a la cuenca del Huaura), incluidas porque
  el estudio ANA 2010 las usa como referencia regional; útiles para
  contraste de patrones estacionales/regionales pero no deben sumarse a la
  oferta hídrica del valle de Huaura.
- Valores vacíos (NaN en el CSV) indican mes sin dato reportado en la fuente
  (falta de registro), no un caudal de cero.

## IV. QA/QC

1. PRIORIZACIÓN DE FUENTES: Conforme a instrucción del usuario, se priorizó
   TOMO I/II (ANA, 2010) sobre el informe INRENA (1998-2007) en todo periodo
   de traslape. Se verificó consistencia en el año de traslape 1997 (Estación
   Alco Sayán): los 12 valores mensuales de TOMO II Cuadro 5.2 coinciden
   exactamente con los del archivo INFORME_FINAL, lo que confirma que ambas
   fuentes documentan el mismo registro histórico oficial para ese periodo.
2. ESTACIÓN ALCO-SAYÁN - DISCONTINUIDAD FÍSICA: la serie histórica de esta
   estación (1911-2008) corresponde en realidad a 6 emplazamientos físicos
   sucesivos con distintos métodos de aforo (ver informe INRENA, sección
   2.4.1: Puente Sayán 1911-1938, Tomas de Cañas 1938-1948, Ferrocarril
   1948-1953, Quintay 1953-1980, Puente Alco 1960-1997, Puente Sayán actual
   1995-a la fecha). Se recomienda tratar el periodo pre-1960 con precaución
   adicional en el análisis de tendencias/homogeneidad.
3. VERSIÓN "COMPLETADO WEAP" (Cuadro 5.5) NO INCLUIDA COMO COLUMNA
   INDEPENDIENTE: TOMO II reporta dos versiones de la serie de Alco Sayán:
   (a) Cuadro 5.2, fuente "ALA Huaura" (observada/cruda), y (b) Cuadro 5.5,
   "completado WEAP" (rellenada mediante modelamiento hidrológico WEAP). Se
   utilizó la versión (a) -observada- como columna principal del dataset
   para mantener trazabilidad con el dato medido. La comparación entre ambas
   versiones muestra pequeñas diferencias (ej. Ene-1967: 35.7 m3/s observado
   vs 34.2 m3/s completado WEAP), producto del relleno de huecos y ajustes
   del modelo. Si se requiere la versión gap-filled para continuidad total
   de la serie sin NaN, puede solicitarse como columna adicional.
4. RÍO CHICO - DATO YA GAP-FILLED EN ORIGEN: el Cuadro 5.6 de TOMO II
   indica explícitamente "Completado WEAP", es decir, ya es una serie
   rellenada por modelamiento (no 100% observación directa) en los periodos
   sin aforo. Se decidió mantenerla igualmente como mejor serie disponible
   por su cobertura (1967-2008, muy superior a la fuente INRENA que solo
   cubría 1994-2004), pero se marca esta salvedad para el análisis de
   incertidumbre.
5. CÁLCULO DE VOLUMEN MENSUAL (MMC): 
   Volumen (MMC) = Caudal (m3/s) x N_días_del_mes x 86,400 (s/día) / 1,000,000
   N_días_del_mes calculado con el calendario estándar (28/29 días en
   febrero, con base en el año calendario correspondiente; no se aplicó
   ajuste especial para años bisiestos más allá del cálculo estándar de
   calendario).
6. VALORES FALTANTES INTERNOS: existen meses individuales sin dato dentro de
   series por lo demás continuas (ej. Yanapampa dic-1974; Santo Domingo
   mar-1995, nov-1995, jul-1997; Yanapampa may-2000 y jun-2000). Estos se
   preservan como NaN; NO se interpoló ni se rellenó ningún valor faltante
   en este procesamiento (el dataset refleja fielmente lo reportado en las
   fuentes, no aplica relleno adicional de Claude).
7. CONVENCIÓN DE FECHA: cada registro mensual se fecha el día 1 del mes
   correspondiente (año calendario, no año hidrológico).
8. LIMITACIÓN CONOCIDA: la estación "Río Chico" (punto de aforo, progresiva
   078+000 del canal Río Chico) no cuenta con coordenadas geográficas
   explícitas en ninguna de las dos fuentes; ver Sección V.
9. UNIDADES ORIGINALES: todas las fuentes reportan caudal ya en m3/s
   (caudal medio mensual); no fue necesaria conversión de unidades de
   caudal, solo el cálculo derivado de volumen.

## V. Dominio espacial y coordenadas

Cuenca de referencia principal: Río Huaura
  Bounding box de la cuenca (INFORME TOMO I, sección 2.2.1):
    Latitud  : 10°27' S  a  11°13' S
    Longitud : 76°32' W  a  77°39' W
  (UTM referencial: 8,756,028 - 8,847,692 Norte; 212,856 - 328,988 Este)
Coordenadas puntuales de cada estación de la serie (grados/minutos y
equivalente en grados decimales, WGS84 asumido salvo indicación contraria):
  Estación         | Río / Cuerpo de agua | Lat            | Lon            | Altitud | Dpto/Prov/Dist
  -----------------|-----------------------|----------------|----------------|---------|------------------------
  Alco Sayán        | Río Huaura            | 11°02' S (-11.0333) | 77°06' W (-77.1000) | 1,000 msnm | Lima / Huaura / Sayán
  Surasaca (laguna) | Laguna Surasaca (Río Huaura, cabecera) | 10°31' S (-10.5167)* | 76°47' W (-76.7833)* | 4,400 msnm | Lima / Oyón / Oyón
  Yanapampa         | Río Pativilca (cuenca vecina) | 10°40' S (-10.6667) | 77°35' W (-77.5833) | 859 msnm | Áncash / Bolognesi / Cochas
  Santo Domingo     | Río Chancay-Huaral (cuenca vecina) | 11°23' S (-11.3833) | 77°03' W (-77.0500) | 697 msnm | Lima / Huaral / Huaral
  Río Chico         | Río Chico (afluente Huaura) | No georreferenciada explícitamente (punto de aforo: progresiva 078+000,00 del canal Río Chico) | - | - | Lima / Huaura
  * Coordenada de Surasaca según archivo fuente INRENA (notación original
    "10º312´S", interpretada como 10°31' S por consistencia con Cuadro N°4.1
    "Estaciones Meteorológicas SENAMHI" de TOMO I, que reporta la estación
    pluviométrica Surasaca en 10°31' S / 76°47' W).
Bounding box combinado de TODAS las estaciones de este dataset (incluye
estaciones de cuencas vecinas usadas como referencia regional):
    Latitud  : -11.3833 (Santo Domingo, sur) a -10.5167 (Surasaca, norte)
    Longitud : -77.5833 (Yanapampa, oeste)   a -76.7833 (Surasaca, este)
NOTA: El bounding box combinado es más amplio que el de la cuenca Huaura
propiamente dicha, porque incluye las estaciones Yanapampa (cuenca
Pativilca) y Santo Domingo (cuenca Chancay-Huaral), usadas únicamente como
series de referencia/regionalización. Para un análisis de TWS de GRACE-FO
estrictamente acotado a la cuenca del Huaura, usar el bounding box de la
cuenca (10°27'-11°13' S / 76°32'-77°39' W) y las columnas
"alco_sayan", "natural_...alco_sayan" y "rio_chico" únicamente.
FUENTE: ESTUDIO ANA-DCPRH-ALA HUAURA (2010) Y ESTUDIO INRENA-ATDR HUAURA-J.U.
HUAURA (1998, actualizado 2004-2007).

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `huaura_caudales.csv` a `huaura_caudal_volumen_multicuenca.csv`.
- Metadata consolidada y reformateada desde `huaura_caudales_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.

**Contenido adicional no clasificado de la fuente original** (preservado para no perder información):

METADATOS DEL DATASET DE: CAUDALES Y VOLÚMENES MEDIOS MENSUALES - CUENCA DEL RÍO HUAURA Y CUENCAS VECINAS (PATIVILCA, CHANCAY-HUARAL)

================================================================================
