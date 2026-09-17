# Metadata — METADATOS DEL DATASET DE CAUDAL - ESTACIÓN LA FRONTERA

## I. Información general

Nombre del Archivo: caudal_la_frontera.csv
Ámbito Geográfico: Cuenca del río Maure (cuenca de trasvase hacia las cuencas
                    Locumba y Sama a través del Proyecto Derivación Túnel
                    Kovire, vertiente del Titicaca).
Departamento del Perú: Tacna (Provincia de Tarata, Distrito de Tarata).
Resolución Temporal: Mensual.
Periodo de Registro: Enero de 1964 a Diciembre de 2003 (40 años calendario,
                      236 registros mensuales de 480 meses posibles; ~49.2%
                      de completitud, con un vacío extenso entre 1972 y 1990
                      —serie interrumpida durante 19 años—).

## II. Fuentes de datos originales

- Documentos de Origen:
  1. Anexo_2_Estudio_Hidrologico_Locumba_Sama_INF_HIDROMETICA_s-f.docx
     Cuadro N°5.31 "Caudal Medio Mensual (m3/s) - Estación La Frontera"
     (tabla incrustada como imagen EMF, transcrita manualmente).
  2. Estudio_Hidrologico_Locumba_Sama_Informe_Final_Dic_2010.doc
     - Cuadro N°02 "Estaciones con registros de caudales medios mensuales -
       Cuencas Locumba y Sama" (ubicación y coordenadas de la estación,
       fila N°30).
     - Figura N°24 - Análisis de doble masa: Challapalca, Chuapalca, La
       Frontera y Bocatoma (periodo 1963-1981).
  3. Fuente primaria citada en la tabla original: SENAMHI (Servicio Nacional
     de Meteorología e Hidrología del Perú).
- Autor del estudio: Ing. Eduardo Chávarri Velarde, para la Autoridad
  Nacional del Agua (ANA) / Ministerio de Agricultura.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `caudal_la_frontera_m3/s` | `caudal_la_frontera_m3_s` |
| `volumen_la_frontera_MMC` | `volumen_la_frontera_mmc` |

---

El dataset contiene las siguientes columnas:
  - date : Fecha correspondiente al primer día del mes de registro.
           Formato AAAA-MM-DD (ej. 1964-01-01).
  - caudal_la_frontera_m3/s : Caudal medio mensual observado en la estación,
           en metros cúbicos por segundo (m3/s), tal como figura en el
           Cuadro N°5.31 del Anexo 2.
  - volumen_la_frontera_MMC : Volumen mensual equivalente, calculado como
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
- IMPORTANTE: esta serie presenta el vacío más extenso de todas las
  estaciones revisadas (1972-1990, 19 años sin registro), por lo que su uso
  para análisis de tendencia de largo plazo debe hacerse con cautela; es
  más confiable en los sub-periodos 1964-1971 y 1991-2003.
- Se recomienda validar contra el documento fuente (Cuadro N°5.31) antes de
  un uso científico o regulatorio definitivo.
- Cobertura temporal: la serie llega hasta diciembre de 2003, por lo que
  presenta un traslape parcial y muy corto (2002-2003, ~2 años) con la misión
  GRACE (abr-2002 a jun-2017), y NINGÚN traslape con GRACE-FO (may-2018 en
  adelante). Es insuficiente por sí sola para una validación robusta de
  anomalías de TWS; se recomienda complementar con registros más recientes
  de SENAMHI/ANA si la estación sigue operativa.

## V. Dominio espacial y coordenadas

1. Ubicación Precisa de las estaciones (en decimales):
   - Estación La Frontera: Latitud -17.467°, Longitud -69.450°,
     Altitud 4 000 m s.n.m. (Cuenca Maure, Distrito de Tarata, Tacna).
2. Bounding Box Recomendado para Extracción Satelital (GRACE NetCDF):
   (en decimales; buffer amplio dado el tamaño de celda/footprint de GRACE,
   del orden de 1°-3°, y para cubrir en conjunto las cuencas Locumba, Sama
   y Maure usadas como referencia en el estudio):
   - Latitud:  -18.50° a -16.50°
   - Longitud: -71.00° a -69.00°

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `la_frontera_caudal.csv` a `maure_lafrontera_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `la_frontera_caudal_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.

**Contenido adicional no clasificado de la fuente original** (preservado para no perder información):

================================================================================
METADATOS DEL DATASET DE CAUDAL - ESTACIÓN LA FRONTERA
================================================================================
