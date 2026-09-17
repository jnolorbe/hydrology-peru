# Metadata — METADATOS DEL DATASET DE: CAUDALES Y VOLÚMENES MENSUALES - CUENCA CAMANÁ-MAJES

## I. Información general

Nombre del dataset: caudales_camana_majes.csv
Región/Cuenca: Valle de Camaná-Majes, cuenca del río Camaná-Majes-Colca
Variable(s): Caudal medio mensual (m3/s) y Volumen mensual (MMC)
Estación: Huatiapa (única estación con registro histórico continuo utilizado en el estudio)
Río: Majes (aguas arriba de la confluencia que da origen al río Camaná)
Resolución temporal: Mensual
Cobertura temporal: 1951-08-01 a 2004-07-01 (53 años hidrológicos, año hidrológico Agosto-Julio)
Número de registros: 636 (53 años x 12 meses)
Valores faltantes: Ninguno (serie completa, sin gaps)
Generado el: Fase 2 del flujo de trabajo QA/QC - Proyecto GRACE-FO Camaná
Formato de fecha: YYYY-MM-DD (primer día de cada mes, representando el valor medio mensual)

## II. Fuentes de datos originales

- Documento base: "INFORME_FINAL_CAMANA-2.doc" (Estudio de Disponibilidad y Demanda Hídrica,
  Valle de Camaná-Majes), Anexo 1.1 (Caudal Medio Mensual - Histórico Aforado) y
  Anexo 1.2 (Volumen Mensual - Histórico Aforado).
- Archivo de datos: "DISPONIBILIDAD_HIDRICA.xls", hojas "Q aforado" y "V aforado".
- Fuente primaria citada en el informe: ATDR CAMANA-MAJES, 2004 - Información de caudales
  de la estación Huatiapa.
- Los registros de caudal provienen del promedio aritmético de tres observaciones diarias
  (7:00 a.m., 12:00 m. y 6:00 p.m.) en la estación Huatiapa, operada por SENAMHI.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Date` | `date` |
| `caudal_rio_majes_huatiapa_m3s` | `caudal_rio_majes_huatiapa_m3s` |
| `volumen_rio_majes_huatiapa_mmc` | `volumen_rio_majes_huatiapa_mmc` |

---

Columna                              | Tipo    | Unidad | Descripción
--------------------------------------|---------|--------|------------------------------------------
Date                                  | date    | -      | Fecha del registro mensual (YYYY-MM-DD),
                                       |         |        | primer día del mes calendario correspondiente.
caudal_rio_majes_huatiapa_m3s         | float   | m3/s   | Caudal medio mensual aforado en la estación
                                       |         |        | Huatiapa, río Majes.
volumen_rio_majes_huatiapa_mmc        | float   | MMC    | Volumen mensual, calculado como:
                                       |         |        | V(MMC) = Q(m3/s) x días_del_mes x 86400 / 1e6

## IV. QA/QC

1. Conversión de año hidrológico a fecha calendario: la fuente original organiza los datos
   por "año hidrológico" (Agosto-Julio, ej. "1951-52"). Se reconstruyó la fecha calendario
   real: los meses Ago-Dic se asignan al primer año del par (1951) y los meses Ene-Jul al
   segundo año (1952).
2. Cálculo de volumen (MMC): se recalculó el volumen mensual a partir del caudal medio
   mensual y del número REAL de días del mes calendario (incluyendo años bisiestos),
   usando la fórmula: V = Q x días x 86400 s/día / 1,000,000 m3/MMC.
3. HALLAZGO DE QA/QC - Discrepancia por año bisiesto: se detectó que la hoja fuente
   "V aforado" calculó el volumen de TODOS los meses de febrero usando un valor fijo de
   28 días, sin ajustar por años bisiestos. Esto genera una subestimación sistemática del
   volumen reportado en la fuente original para los 14 meses de febrero bisiestos dentro
   de la serie (1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996,
   2000, 2004), con diferencias de hasta ~42.7 MMC en el caso de mayor caudal (febrero 1984,
   Q=494.15 m3/s). El presente dataset usa el cálculo corregido (29 días en años bisiestos),
   por lo que el volumen de este dataset puede diferir levemente del reportado en el
   documento original del informe para esos meses específicos.
4. Validaciones aplicadas: se verificó (a) ausencia de fechas duplicadas, (b) ausencia de
   valores nulos, (c) caudales estrictamente positivos, (d) continuidad de la serie mensual
   sin gaps, y (e) número total de registros = 636 (53 años x 12 meses), consistente con el
   periodo declarado en el informe (53 años hidrológicos).
5. Estaciones NO incluidas en este dataset (limitación multiestación):
   - Estación "Pte. Carretera-Camaná" (río Camaná, limnimétrica, ATDR): el propio informe
     la describe como información "insuficiente e incompleta"; no se adjuntó archivo de
     datos crudos y no fue utilizada en el estudio original.
   - Estación "Pampatá" (río Camaná, SENAMHI): sin coordenadas ni periodo de registro
     verificable en la fuente; sin archivo de datos crudos.
   - Río Camaná (tramo bajo, aguas abajo de la confluencia): el informe SOLO proporciona
     estadísticos agregados (media, mínimo, máximo y caudal al 75% de persistencia) del
     caudal remanente del río Majes tras satisfacer la demanda del valle de Majes
     (hoja "resumen" de DISPONIBILIDAD_HIDRICA.xls). Esto NO constituye una serie mensual
     fechada real, sino un análisis estadístico de persistencia; por lo tanto no se incluye
     en este CSV para no introducir fechas ficticias. Si se requiere, puede generarse un
     dataset estadístico separado (no serie temporal) bajo pedido explícito.
6. Software y método de referencia: el informe original realiza además un análisis de
   persistencia de caudales y volúmenes (hojas "Q persistencia" / "V persistencia"),
   ordenando los 53 valores históricos de cada mes de mayor a menor y calculando la
   probabilidad de excedencia (P% = m/(N+1)). Esta información NO forma parte del presente
   dataset de serie temporal (es un análisis estadístico transversal, no una serie por
   fecha), pero está disponible en la fuente original si se requiere en una fase posterior.

## V. Dominio espacial y coordenadas

Estación Huatiapa (único punto de medición usado):
  Latitud:   16°00' S  (-16.000°)
  Longitud:  72°28' W  (-72.467°)
  Altitud:   700 msnm
  Distrito:  Aplao
  Provincia: Castilla
  Departamento: Arequipa
  País: Perú
Bounding box referencial del Valle de Camaná (área de estudio, para contexto espacial
de validación de TWS-GRACE-FO):
  Latitud:  16°30' S a 16°40' S  (-16.667° a -16.500°)
  Longitud: 72°40' W a 72°50' W  (-72.833° a -72.667°)
Nota: la estación Huatiapa (punto de aforo) se ubica físicamente aguas arriba del valle
de Camaná propiamente dicho (en la cuenca del río Majes, distrito de Aplao, provincia de
Castilla), fuera del bounding box del valle de Camaná. Se reporta por separado para evitar
ambigüedad espacial en el análisis de TWS.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `camana_majes_caudales.csv` a `camana_majes_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `camana_majes_metadatos.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
