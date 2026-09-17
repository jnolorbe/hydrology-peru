# Metadata — METADATOS DEL DATASET DE CAUDAL - ESTACIÓN CHUAPALCA

## I. Información general

Nombre del Archivo: caudal_chuapalca.csv
Ámbito Geográfico: Cuenca del río Maure (cuenca de trasvase hacia las cuencas
                    Locumba y Sama a través del Proyecto Derivación Túnel
                    Kovire, vertiente del Titicaca).
Departamento del Perú: Tacna (Provincia de Tarata, Distrito de Tarata).
Resolución Temporal: Mensual.
Periodo de Registro: Enero de 1963 a Diciembre de 2003 (41 años calendario,
                      392 registros mensuales de 492 meses posibles; ~79.7%
                      de completitud, con un vacío extenso entre 1981 y 1987
                      y vacíos puntuales en 1975 y 1980).

## II. Fuentes de datos originales

- Documentos de Origen:
  1. Anexo_2_Estudio_Hidrologico_Locumba_Sama_INF_HIDROMETICA_s-f.docx
     Cuadro N°5.30 "Caudal Medio Mensual (m3/s) - Estación Chuapalca"
     (tabla incrustada como imagen EMF, transcrita manualmente).
  2. Estudio_Hidrologico_Locumba_Sama_Informe_Final_Dic_2010.doc
     - Cuadro N°02 "Estaciones con registros de caudales medios mensuales -
       Cuencas Locumba y Sama" (ubicación y coordenadas de la estación,
       fila N°29).
     - Tabla de estaciones de precipitación (la estación Chuapalca también
       opera como estación pluviométrica, periodo 1964-2009, código PLU).
     - Figura N°24 - Análisis de doble masa: Challapalca, Chuapalca, La
       Frontera y Bocatoma (periodo 1963-1981).
     - Figuras N°26 y N°29 - Análisis de doble masa: Vilacota (Caudal y
       Precipitación), Challapalca, Chuapalca; y Entrada Túnel Kovire,
       Chuapalca.
  3. Fuente primaria citada en la tabla original: SENAMHI (Servicio Nacional
     de Meteorología e Hidrología del Perú).
- Autor del estudio: Ing. Eduardo Chávarri Velarde, para la Autoridad
  Nacional del Agua (ANA) / Ministerio de Agricultura.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `caudal_chuapalca_m3/s` | `caudal_chuapalca_m3_s` |
| `volumen_chuapalca_MMC` | `volumen_chuapalca_mmc` |

---

El dataset contiene las siguientes columnas:
  - date : Fecha correspondiente al primer día del mes de registro.
           Formato AAAA-MM-DD (ej. 1963-01-01).
  - caudal_chuapalca_m3/s : Caudal medio mensual observado en la estación,
           en metros cúbicos por segundo (m3/s), tal como figura en el
           Cuadro N°5.30 del Anexo 2.
  - volumen_chuapalca_MMC : Volumen mensual equivalente, calculado como
           caudal_m3/s × número_de_días_del_mes × 86 400 s, expresado en
           millones de metros cúbicos (MMC).

## IV. QA/QC

- Los datos originales se encontraban incrustados como imagen vectorial (EMF)
  dentro del documento Word (tabla pegada desde Excel); no existía una versión
  en texto/tabla editable. Se realizó conversión EMF→PNG y transcripción
  visual manual de cada celda.
- Las celdas en blanco o resaltadas en celeste en la tabla original (sin
  registro) se omiten en el CSV; no se interpolan ni se rellenan con cero.
- No se aplicó ningún proceso de relleno de datos faltantes (gap-filling),
  corrección por consistencia (doble masa) ni control de outliers adicional
  al que ya hubiera aplicado SENAMHI/ANA en la fuente original.
- El volumen mensual (MMC) se calculó usando el número exacto de días de cada
  mes calendario (incluye años bisiestos en febrero).
- Estación con caudales relativamente altos y variables (crecidas de enero
  1963 con 31.3 m3/s en febrero); se recomienda validar contra el documento
  fuente (Cuadro N°5.30) antes de un uso científico o regulatorio definitivo.
- Cobertura temporal: la serie llega hasta diciembre de 2003, por lo que
  presenta un traslape parcial y muy corto (2002-2003, ~2 años) con la misión
  GRACE (abr-2002 a jun-2017), y NINGÚN traslape con GRACE-FO (may-2018 en
  adelante). Es insuficiente por sí sola para una validación robusta de
  anomalías de TWS; se recomienda complementar con registros más recientes
  de SENAMHI/ANA si la estación sigue operativa.

## V. Dominio espacial y coordenadas

1. Ubicación Precisa de las estaciones (en decimales):
   - Estación Chuapalca: Latitud -17.300°, Longitud -69.650°,
     Altitud 4 158 m s.n.m. (Cuenca Maure, Distrito de Tarata, Tacna).
     [Nota: la estación pluviométrica homónima referenciada en la tabla de
     precipitación figura con Latitud -17.350°, Longitud -69.650°, Altitud
     4 250 m s.n.m.; corresponde a la misma localidad con una diferencia
     menor de georreferenciación entre ambos cuadros del estudio.]
2. Bounding Box Recomendado para Extracción Satelital (GRACE NetCDF):
   (en decimales; buffer amplio dado el tamaño de celda/footprint de GRACE,
   del orden de 1°-3°, y para cubrir en conjunto las cuencas Locumba, Sama
   y Maure usadas como referencia en el estudio):
   - Latitud:  -18.50° a -16.50°
   - Longitud: -71.00° a -69.00°

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `chuapalca_caudal.csv` a `maure_chuapalca_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `chuapalca_caudal_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.

**Contenido adicional no clasificado de la fuente original** (preservado para no perder información):

================================================================================
METADATOS DEL DATASET DE CAUDAL - ESTACIÓN CHUAPALCA
================================================================================
