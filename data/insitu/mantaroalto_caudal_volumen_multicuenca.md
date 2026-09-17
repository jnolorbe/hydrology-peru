# Metadata — METADATOS DEL DATASET DE: CAUDALES Y VOLÚMENES MENSUALES - CUENCA ALTA DEL RÍO MANTARO (SUBCUENCAS SHULLCAS Y CUNAS)

## I. Información general

Nombre del dataset:      caudales_volumenes_mantaro.csv
Variable:                Caudal medio mensual (m3/s) y volumen mensual (MMC)
Ámbito:                  Cuenca alta del río Mantaro - subcuencas de los ríos Cunas y Shullcas
                         (Junín, Perú)
Estaciones incluidas:    3 (Angasmayo y Yanacocha en el río Cunas; Chamisería en el río Shullcas)
Periodo temporal:        Enero 1960 - Diciembre 2007 (48 años, 576 registros mensuales)
Resolución temporal:     Mensual
Formato de fecha:        YYYY-MM-DD (día fijado al 01 de cada mes, convención estándar
                         para series mensuales; no representa una fecha de medición diaria)
Elaborado para:          Control de calidad (QA/QC) y validación de análisis estacional/
                         tendencia de datos TWS de GRACE-FO
Fecha de procesamiento:  Generado a partir de archivos fuente sin fecha de creación propia
                         indicada; el archivo fuente principal corresponde a una corrida del
                         modelo HEC-4 (sin fecha de ejecución consignada en el archivo).

## II. Fuentes de datos originales

Fuente primaria (dato numérico):
  - Data_de_salida_del_HEC-4.txt
    "RECORDED AND RECONSTITUTED FLOWS" - salida del modelo HEC-4 para 3 estaciones
    identificadas en el archivo únicamente con códigos numéricos internos 101, 102, 103.
    Cubre 1960-2007 sin vacíos (la reconstitución del modelo ya rellena los periodos sin
    dato registrado). Cada valor mensual lleva un sufijo "E" cuando es un valor ESTIMADO
    (reconstituido por el modelo) en vez de un valor REGISTRADO directamente.
Fuentes usadas para identificar las estaciones y validar las unidades:
  - Data_de_entrada_al_HEC-4.txt (mismas 3 series, con vacíos codificados -1.0, y con un
    encabezado que asocia cada código interno H101/H102/H103 a un código numérico de 6
    dígitos: 230926, 230945 y 230931 respectivamente)
  - PTM_y_QMM_Completada_y_Extendida.xls, hojas "Angasmayo_QMM" y "Chamiseria_QMM"
    (caudal medio mensual en m3/s, ya en unidades correctas, 1964-2002)
  - Informe_Final_Version__Febrero.doc, Cuadro Nº 2.4 "Características de las Estaciones
    Hidrométricas de la cuenca del río Shullcas y Cunas" (código SENAMHI oficial, ubicación
    política y geográfica de cada estación)

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Date` | `date` |
| `caudal_angasmayo_m3s` | `caudal_angasmayo_m3s` |
| `volumen_angasmayo_mmc` | `volumen_angasmayo_mmc` |
| `caudal_yanacocha_m3s` | `caudal_yanacocha_m3s` |
| `volumen_yanacocha_mmc` | `volumen_yanacocha_mmc` |
| `caudal_chamiseria_m3s` | `caudal_chamiseria_m3s` |
| `volumen_chamiseria_mmc` | `volumen_chamiseria_mmc` |

---

Date                          | Fecha (primer día del mes), formato YYYY-MM-DD
caudal_angasmayo_m3s           | Caudal medio mensual, estación Angasmayo (río Cunas), m3/s
volumen_angasmayo_mmc          | Volumen mensual, estación Angasmayo, millones de m3 (MMC)
caudal_yanacocha_m3s           | Caudal medio mensual, estación Yanacocha (río Cunas), m3/s
volumen_yanacocha_mmc          | Volumen mensual, estación Yanacocha, millones de m3 (MMC)
caudal_chamiseria_m3s          | Caudal medio mensual, estación Chamisería (río Shullcas), m3/s
volumen_chamiseria_mmc         | Volumen mensual, estación Chamisería, millones de m3 (MMC)
Fórmula de conversión caudal -> volumen:
  volumen_mmc = caudal_m3s * dias_del_mes * 86400 / 1,000,000

## IV. QA/QC

1. IDENTIFICACIÓN DE ESTACIONES (código interno -> estación real)
   El archivo fuente HEC-4 solo identifica las series con códigos internos 101/102/103,
   sin nombre de estación. La identidad y el factor de escala se determinaron por
   verificación cruzada con las series "QMM" del Excel (que sí tienen unidades y nombre
   confirmados), comparando valor a valor los años que se traslapan (1964-2002):
     - Estación 102 == Chamisería:  coincidencia exacta mes a mes con la hoja
       "Chamiseria_QMM" (años de prueba 1975, 1976, 1988) al dividir el valor crudo entre 100.
     - Estación 103 == Angasmayo:   coincidencia exacta mes a mes con la hoja
       "Angasmayo_QMM" (mismos años de prueba) al dividir el valor crudo entre 100.
     - Estación 101 == Yanacocha:   no existe hoja "Yanacocha_QMM" para verificación
       exacta, pero (a) es la única estación tributaria restante de las 3 descritas en el
       Cuadro 2.4 del informe, (b) su código de 6 dígitos en el archivo de entrada (230926)
       es el más cercano al código oficial SENAMHI de Yanacocha (230925), y (c) su caudal
       medio del periodo 1960-2007 (5.32 m3/s) coincide con el caudal medio anual de
       Yanacocha reportado en el informe (5.28 m3/s, Cuadro 2.9, periodo 1962-1997/1975-1993).
       Se considera una identificación de alta confianza, aunque no verificada al 100%
       por coincidencia exacta mes a mes como en los otros dos casos.
2. FACTOR DE ESCALA
   Los valores crudos del archivo HEC-4 están en unidades de 0.01 m3/s (es decir, se
   dividieron entre 100 para obtener m3/s). Esto se determinó por el mismo proceso de
   comparación cruzada del punto 1. Los caudales medios resultantes por estación en el
   dataset final (1960-2007) son: Angasmayo 14.63 m3/s, Yanacocha 5.32 m3/s, Chamisería
   4.68 m3/s, consistentes con los valores medios anuales reportados en el informe fuente
   (14.65 / 5.28 / 4.29 m3/s respectivamente, para periodos ligeramente distintos).
3. DATOS ESTIMADOS VS. REGISTRADOS (bandera "E" del HEC-4)
   El archivo fuente distingue valores registrados directamente de valores reconstituidos
   (estimados) por el modelo HEC-4. Proporción de meses estimados por estación en el
   periodo 1960-2007:
     - Angasmayo:   11.1% de los meses son estimados
     - Yanacocha:   25.0% de los meses son estimados
     - Chamisería:  45.1% de los meses son estimados
   Esta bandera NO se incluyó como columna en el CSV (para mantener el archivo limpio y
   puramente numérico según el formato solicitado); se documenta aquí para que el usuario
   pueda ponderar la confiabilidad de cada estación/periodo en el análisis de tendencia.
   Si se requiere la bandera por registro, puede regenerarse a partir del archivo fuente.
4. PERIODO Y ESTACIONES NO INCLUIDAS
   - Se usó el archivo de SALIDA del HEC-4 (ya reconstituido, sin vacíos) en lugar del
     archivo de ENTRADA (con vacíos codificados -1.0) para maximizar cobertura temporal
     continua 1960-2007.
   - Las estaciones principales del cauce del río Mantaro (Upamayo, Puente Stuart, La
     Mejorada, etc., Cuadro 2.1 del informe) NO se incluyeron en este dataset: no se
     encontró ningún archivo de datos numéricos brutos para ellas entre los archivos
     entregados (solo su metadata y caudal medio anual aparecen en el informe, sin serie
     mensual descargable).
   - No se incluyó una columna separada de datos "históricos sin completar" ya que la
     fuente usada (HEC-4 output) llega pre-reconstituida.
5. VALIDACIÓN DE CONSISTENCIA
   Para los años de traslape (1964-2002) las medias mensuales de Angasmayo y Chamisería
   obtenidas de este dataset coinciden exactamente con las hojas "Angasmayo_QMM" y
   "Chamiseria_QMM" del archivo Excel completado y extendido (ver punto 1), lo que valida
   el procesamiento.

## V. Dominio espacial y coordenadas

Sistema de referencia: coordenadas geográficas (grados, minutos), convertidas a decimal.
Hemisferio: Sur (latitud negativa) / Oeste (longitud negativa), Perú.
Estación      | Río     | Provincia | Distrito  | Lat (dec)  | Lon (dec)   | Altitud (m)
Angasmayo     | Cunas   | Chupaca   | Chupaca   | -12.0167   | -75.3833    | 3280
Yanacocha     | Cunas   | Concepción| Concepción| -12.0167   | -75.4667    | 3500
Chamisería    | Shullcas| Huancayo  | Huancayo  | -12.0000   | -75.1667    | 3440
Bounding Box (WGS84 aprox., grados decimales):
  Lat mínima:  -12.0167
  Lat máxima:  -12.0000
  Lon mínima:  -75.4667
  Lon máxima:  -75.1667

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `mantaro_caudales.csv` a `mantaroalto_caudal_volumen_multicuenca.csv`.
- Metadata consolidada y reformateada desde `mantaro_caudales_metadatos.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
