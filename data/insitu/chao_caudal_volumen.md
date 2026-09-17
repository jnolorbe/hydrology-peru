# Metadata — METADATOS DEL DATASET DE CAUDALES - VALLE Y CUENCA DE CHAO (ESTACIÓN CONDORCERRO)

## I. Información general

Nombre del Archivo: chao_caudales.csv
Ámbito Geográfico: Cuenca del Río Chao / Río Santa, Departamento de La Libertad y Ancash, Perú.
Resolución Temporal: Mensual.
Periodo de Registro: Agosto de 1956 a Julio de 2004 (48 años hidrológicos, 576 registros mensuales).
Propósito: Proveer la serie de caudales mensuales (en m3/s y volúmenes estandarizados en Millones de Metros Cúbicos - MMC) de la Estación Condorcerro en el río Santa, principal fuente de trasvase y oferta hídrica regulada para el valle de Chao a través del Proyecto Especial Chavimochic, optimizado para el balance hídrico y la validación de anomalías de almacenamiento total de agua (TWS) de GRACE.

## II. Fuentes de datos originales

- Documentos de Origen: 
  * "Asignación de Agua Chao.doc" (Informe Final PROFODUA / INRENA, Setiembre 2004) [cite: 5].
  * "Anexo 1 Chao, Oferta Hídrica.xls".
- Secciones Base:
  * Cuadro 2.3 / Hoja "Cua-2.3": Descargas Mensuales (m3/s) del Río Santa - Estación Condorcerro (Período 1956/57 - 2003/04) [cite: 5].
- Operadores Históricos: Empresa Duke Energy International EGENOR S.A., Proyecto Especial Chavimochic, SENAMHI, e INRENA [cite: 5].
-Anexo 1 Chao, Oferta Hídrica.xls
- Asignación de Agua Chao.doc

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Date` | `date` |
| `Q_Condorcerro_m3s` | `caudal_condorcerro_m3s` |
| `Q_Condorcerro_MMC` | `caudal_condorcerro_mmc` |

---

El dataset contiene las siguientes 3 columnas:
1. Date (Formato YYYY-MM-DD): 
   Fecha estandarizada del mes de registro (fijada en el día 1 de cada mes).
2. Q_Condorcerro_m3s (Numérico, Float): 
   Caudal medio mensual registrado en la Estación Condorcerro (Río Santa), expresado en metros cúbicos por segundo (m3/s) [cite: 5].
3. Q_Condorcerro_MMC (Numérico, Float): 
   Volumen mensual escurrido calculado multiplicando el caudal medio por el número exacto de segundos del mes correspondiente (considerando años bisiestos), expresado en Millones de Metros Cúbicos (MMC).

## IV. QA/QC

- Ciclo Hidrológico: Las series originales están estructuradas bajo el año hidrológico que inicia en Agosto y culmina en Julio. Se reestructuró la secuencia temporal cronológica lineal desde agosto de 1956 hasta julio de 2004.
- Conversión Física: La transformación a MMC se realizó aplicando el factor temporal exacto diario de cada mes calendario.
- Contexto de Oferta: El valle de Chao opera bajo un sistema no regulado con trasvase de agua del río Santa (Proyecto Chavimochic), donde la Estación Condorcerro representa la fuente mayoritaria de asignación hídrica [cite: 5].

## V. Dominio espacial y coordenadas

1. Ubicación Precisa de la Estación de Control Principal (Estación Condorcerro):
   - Río: Santa [cite: 5]
   - Tipo: Limnigráfica [cite: 5]
   - Ubicación Política: Departamento de Ancash, Provincia Santa, Distrito Macate [cite: 5].
   - Coordenadas Geográficas: 
     * Latitud:  8°39' S [cite: 5]
     * Longitud: 78°15' W [cite: 5]
   - Altitud: 450 msnm [cite: 5]
   - Entidad Operadora: Proyecto Especial Chavimochic / EGENOR [cite: 5].
2. Bounding Box Recomendado para Extracción Satelital (GRACE NetCDF):
   - Latitud:  [-8.90 , -8.10] (Sur)
   - Longitud: [-78.50 , -77.80] (Oeste)

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `chao_caudales.csv` a `chao_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `chao_caudales_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.

**Contenido adicional no clasificado de la fuente original** (preservado para no perder información):

================================================================================
METADATOS DEL DATASET DE CAUDALES - VALLE Y CUENCA DE CHAO (ESTACIÓN CONDORCERRO)
================================================================================
