# Metadata — METADATOS DEL DATASET DE CAUDAL - ESTACIÓN PUENTE VIEJO

## I. Información general

Nombre del Archivo: caudal_puente_viejo.csv
Ámbito Geográfico: Cuenca del río Locumba (estación de control ubicada aguas
                    abajo, cerca de la desembocadura, integra las descargas
                    de los ríos Curibaya —Est. Ticapampa— e Ilabaya —Est. El
                    Cairo—).
Departamento del Perú: Tacna (Provincia de Jorge Basadre, Distrito de
                        Locumba).
Resolución Temporal: Mensual.
Periodo de Registro: Enero de 1972 a Diciembre de 1999 (28 años calendario,
                      335 registros mensuales de 336 meses posibles; ~99.7%
                      de completitud, prácticamente sin vacíos —único mes
                      faltante: agosto de 1980—).

## II. Fuentes de datos originales

- Documentos de Origen:
  1. Anexo_2_Estudio_Hidrologico_Locumba_Sama_INF_HIDROMETICA_s-f.docx
     Cuadro N°5.16 "Caudal Medio Mensual (m3/s) - Estación Puente Viejo"
     (tabla incrustada como imagen EMF, transcrita manualmente).
  2. Estudio_Hidrologico_Locumba_Sama_Informe_Final_Dic_2010.doc
     - Cuadro N°02 "Estaciones con registros de caudales medios mensuales -
       Cuencas Locumba y Sama" (ubicación y coordenadas de la estación,
       fila N°15).
     - Cuadro comparativo: "Río Ilabaya (Est. El Cairo), Río Curibaya (Est.
       Ticapampa) → Río Locumba (Est. Puente Viejo)".
     - Figura N°18 - Análisis de doble masa: La Tranca, Puente Viejo y
       Aguas Calientes (periodo 1972-1989).
  3. Fuente primaria citada en la tabla original: SENAMHI (Servicio Nacional
     de Meteorología e Hidrología del Perú).
- Autor del estudio: Ing. Eduardo Chávarri Velarde, para la Autoridad
  Nacional del Agua (ANA) / Ministerio de Agricultura.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `caudal_puente_viejo_m3/s` | `caudal_puente_viejo_m3_s` |
| `volumen_puente_viejo_MMC` | `volumen_puente_viejo_mmc` |

---

El dataset contiene las siguientes columnas:
  - date : Fecha correspondiente al primer día del mes de registro.
           Formato AAAA-MM-DD (ej. 1972-01-01).
  - caudal_puente_viejo_m3/s : Caudal medio mensual observado en la estación,
           en metros cúbicos por segundo (m3/s), tal como figura en el
           Cuadro N°5.16 del Anexo 2.
  - volumen_puente_viejo_MMC : Volumen mensual equivalente, calculado como
           caudal_m3/s × número_de_días_del_mes × 86 400 s, expresado en
           millones de metros cúbicos (MMC).

## IV. QA/QC

- Los datos originales se encontraban incrustados como imagen vectorial (EMF)
  dentro del documento Word (tabla pegada desde Excel); no existía una versión
  en texto/tabla editable. Se realizó conversión EMF→PNG y transcripción
  visual manual de cada celda.
- La única celda en blanco de toda la serie (agosto de 1980) se omite en el
  CSV; no se interpola ni se rellena con cero.
- No se aplicó ningún proceso de relleno de datos faltantes (gap-filling),
  corrección por consistencia (doble masa) ni control de outliers adicional
  al que ya hubiera aplicado SENAMHI/ANA en la fuente original.
- El volumen mensual (MMC) se calculó usando el número exacto de días de cada
  mes calendario (incluye años bisiestos en febrero).
- Esta es la serie de caudal más completa y continua de todo el estudio
  (28 años consecutivos casi sin interrupciones), lo que la hace la mejor
  candidata dentro del conjunto de estaciones revisadas para análisis de
  tendencia y climatología de caudales de la cuenca Locumba.
- Se recomienda validar contra el documento fuente (Cuadro N°5.16) antes de
  un uso científico o regulatorio definitivo, en particular los valores pico
  de crecida (p. ej. octubre de 1985 con 10.07 m3/s).
- Cobertura temporal: la serie finaliza en diciembre de 1999, previo al
  inicio de la misión GRACE (abr-2002); por lo tanto NO tiene traslape con
  GRACE ni con GRACE-FO (may-2018 en adelante). Su utilidad para validación
  directa de anomalías de TWS es limitada; es más útil para calibración de
  modelos hidrológicos de largo plazo o climatología de caudales, y como
  referencia de línea base pre-satelital.

## V. Dominio espacial y coordenadas

1. Ubicación Precisa de las estaciones (en decimales):
   - Estación Puente Viejo: Latitud -17.617°, Longitud -70.767°,
     Altitud 550 m s.n.m. (Cuenca Locumba, Distrito de Locumba, Tacna).
2. Bounding Box Recomendado para Extracción Satelital (GRACE NetCDF):
   (en decimales; buffer amplio dado el tamaño de celda/footprint de GRACE,
   del orden de 1°-3°, y para cubrir en conjunto las cuencas Locumba, Sama
   y Caplina usadas como referencia en el estudio):
   - Latitud:  -18.50° a -16.50°
   - Longitud: -71.00° a -69.00°

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `puente_viejo_caudal.csv` a `locumba_puenteviejo_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `puente_viejo_caudal_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.

**Contenido adicional no clasificado de la fuente original** (preservado para no perder información):

================================================================================
METADATOS DEL DATASET DE CAUDAL - ESTACIÓN PUENTE VIEJO
================================================================================
