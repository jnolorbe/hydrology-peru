# Metadata — METADATOS DEL DATASET DE CAUDAL - ESTACIÓN AGUAS CALIENTES

## I. Información general

Nombre del Archivo: caudal_aguas_calientes.csv
Ámbito Geográfico: Cuenca del río Caplina (fuera del ámbito Locumba-Sama;
                    incluida en el estudio como estación de contraste/análisis
                    de doble masa con la cuenca Sama).
Departamento del Perú: Tacna (Provincia de Tacna, Distrito de Pachía).
Resolución Temporal: Mensual.
Periodo de Registro: Enero de 1950 a Diciembre de 1989 (40 años calendario,
                      443 registros mensuales de 480 meses posibles; ~92.3%
                      de completitud, con vacíos dispersos en 1951, 1961,
                      1981-1985 y 1988).

## II. Fuentes de datos originales

- Documentos de Origen:
  1. Anexo_2_Estudio_Hidrologico_Locumba_Sama_INF_HIDROMETICA_s-f.docx
     Cuadro N°5.32 "Caudal Medio Mensual (m3/s) - Estación Aguas Calientes"
     (tabla incrustada como imagen EMF, transcrita manualmente).
  2. Estudio_Hidrologico_Locumba_Sama_Informe_Final_Dic_2010.doc
     - Cuadro N°02 "Estaciones con registros de caudales medios mensuales -
       Cuencas Locumba y Sama" (ubicación y coordenadas de la estación).
     - Figuras N°16, 17 y 18 - Análisis de doble masa: La Tranca y Aguas
       Calientes; La Tranca, Aguas Calientes y Piedras Blancas; La Tranca,
       Puente Viejo y Aguas Calientes (periodos 1963-1989 y 1972-1989).
  3. Fuente primaria citada en la tabla original: SENAMHI (Servicio Nacional
     de Meteorología e Hidrología del Perú).
- Autor del estudio: Ing. Eduardo Chávarri Velarde, para la Autoridad
  Nacional del Agua (ANA) / Ministerio de Agricultura.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `caudal_aguas_calientes_m3/s` | `caudal_aguas_calientes_m3_s` |
| `volumen_aguas_calientes_MMC` | `volumen_aguas_calientes_mmc` |

---

El dataset contiene las siguientes columnas:
  - date : Fecha correspondiente al primer día del mes de registro.
           Formato AAAA-MM-DD (ej. 1950-01-01).
  - caudal_aguas_calientes_m3/s : Caudal medio mensual observado en la
           estación, en metros cúbicos por segundo (m3/s), tal como figura
           en el Cuadro N°5.32 del Anexo 2.
  - volumen_aguas_calientes_MMC : Volumen mensual equivalente, calculado como
           caudal_m3/s × número_de_días_del_mes × 86 400 s, expresado en
           millones de metros cúbicos (MMC).

## IV. QA/QC

- Los datos originales se encontraban incrustados como imagen vectorial (EMF)
  dentro del documento Word (tabla pegada desde Excel); no existía una versión
  en texto/tabla editable. Se realizó conversión EMF→PNG y transcripción
  visual manual de cada celda.
- Las celdas en blanco o resaltadas en celeste en la tabla original (sin
  registro o estación fuera de operación) se omiten en el CSV; no se
  interpolan ni se rellenan con cero.
- No se aplicó ningún proceso de relleno de datos faltantes (gap-filling),
  corrección por consistencia (doble masa), ni control de outliers adicional
  al que ya hubiera aplicado SENAMHI/ANA en la fuente original.
- El volumen mensual (MMC) se calculó usando el número exacto de días de cada
  mes calendario (incluye años bisiestos en febrero).
- Se recomienda validar contra el documento fuente (Cuadro N°5.32) antes de
  un uso científico o regulatorio definitivo, en particular en años con
  crecidas extremas (p. ej. 1952-1955, con valores puntuales >3 m3/s).
- Cobertura temporal: la serie finaliza en 1989 y por lo tanto NO tiene
  traslape con las misiones satelitales GRACE (abr-2002 a jun-2017) ni
  GRACE-FO (may-2018 a la fecha). Su utilidad para validación directa de
  anomalías de TWS es limitada; es más útil para calibración de modelos
  hidrológicos de largo plazo o para análisis de estacionalidad/climatología
  de caudales.

## V. Dominio espacial y coordenadas

1. Ubicación Precisa de las estaciones (en decimales):
   - Estación Aguas Calientes: Latitud -17.850°, Longitud -70.117°,
     Altitud 1 300 m s.n.m. (Cuenca Caplina, Distrito de Pachía, Tacna).
2. Bounding Box Recomendado para Extracción Satelital (GRACE NetCDF):
   (en decimales; buffer amplio dado el tamaño de celda/footprint de GRACE,
   del orden de 1°-3°, y para cubrir en conjunto las cuencas Locumba, Sama
   y Caplina usadas como referencia en el estudio):
   - Latitud:  -18.50° a -16.50°
   - Longitud: -71.00° a -69.00°

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `aguas_calientes_caudal.csv` a `caplina_aguascalientes_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `aguas_calientes_caudal_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.

**Contenido adicional no clasificado de la fuente original** (preservado para no perder información):

================================================================================
METADATOS DEL DATASET DE CAUDAL - ESTACIÓN AGUAS CALIENTES
================================================================================
