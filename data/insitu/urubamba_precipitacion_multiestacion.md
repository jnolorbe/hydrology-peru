# Metadata — METADATOS DEL DATASET DE PRECIPITACIÓN MULTIESTACIÓN - CUENCA DEL RÍO URUBAMBA (CUSCO)

## I. Información general

Nombre del Archivo: cusco_precipitacion.csv
Ámbito Geográfico: Cuenca del río Urubamba (ríos Vilcanota y Mapacho) y zonas
vecinas de cabecera/selva alta, Región Cusco, Perú.
Resolución Temporal: Mensual.
Periodo de Registro: Enero de 1964 a Diciembre de 2008 (45 años, 540 registros),
uniforme en las 21 estaciones.
Propósito: Proveer una serie de tiempo continua y multiestación de precipitación
total mensual, para análisis de variabilidad pluviométrica, cálculo de precipitación
areal por unidad hidrográfica/polígono de Thiessen, y como variable de entrada del
modelo lluvia-escorrentía (Lutz Scholz) usado en el mismo estudio.

## II. Fuentes de datos originales

- Documento de Origen: "Hidrologia_Urubamba_Volumen_II (Anexo)" — Anexo de datos del
  "Estudio Hidrológico de la Cuenca del Río Urubamba", Administración Local de Agua
  (ALA) Cusco / Autoridad Nacional del Agua (ANA).
- Sección Base: 21 tablas "Observatorio [nombre]" — series históricas mensuales de
  precipitación total (mm), ya procesadas (ver sección IV).
- Operador histórico: SENAMHI (Servicio Nacional de Meteorología e Hidrología del
  Perú), red de observatorios pluviométricos de la cuenca Urubamba y cuencas
  vecinas.
- Referencia de altitudes: "Hidrologia_Urubamba_Volumen_I (Memoria)", Cuadro
  "Observatorios Climatológicos – Cuenca río Urubamba".

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Date` | `date` |
| `P_La_Raya_mm` | `precipitacion_la_raya_mm` |
| `P_Llalli_mm` | `precipitacion_llalli_mm` |
| `P_Macusani_mm` | `precipitacion_macusani_mm` |
| `P_Sicuani_mm` | `precipitacion_sicuani_mm` |
| `P_Ccatcca_mm` | `precipitacion_ccatcca_mm` |
| `P_Granja_Kayra_mm` | `precipitacion_granja_kayra_mm` |
| `P_Paruro_mm` | `precipitacion_paruro_mm` |
| `P_Paucartambo_mm` | `precipitacion_paucartambo_mm` |
| `P_Pisac_mm` | `precipitacion_pisac_mm` |
| `P_Pomacanchi_mm` | `precipitacion_pomacanchi_mm` |
| `P_Urubamba_mm` | `precipitacion_urubamba_mm` |
| `P_Cirialo_mm` | `precipitacion_cirialo_mm` |
| `P_Curahuasi_mm` | `precipitacion_curahuasi_mm` |
| `P_Machupicchu_mm` | `precipitacion_machupicchu_mm` |
| `P_Quillabamba_mm` | `precipitacion_quillabamba_mm` |
| `P_Vilcabamba_mm` | `precipitacion_vilcabamba_mm` |
| `P_La_Quebrada_mm` | `precipitacion_la_quebrada_mm` |
| `P_Huyro_mm` | `precipitacion_huyro_mm` |
| `P_Chontachaca_mm` | `precipitacion_chontachaca_mm` |
| `P_Pakitza_mm` | `precipitacion_pakitza_mm` |
| `P_Quincemil_mm` | `precipitacion_quincemil_mm` |

---

El dataset contiene 22 columnas, en formato ancho (una fila por mes, una columna por
estación):
1. Date (Formato YYYY-MM-DD): fecha estandarizada del mes de medición (día = "01").
2-22. P_<Estación>_mm (Numérico, Float): precipitación total mensual en milímetros.
   Estaciones incluidas, con su altitud (msnm) según el Volumen I:
   - P_La_Raya_mm         — La Raya (cabecera de cuenca, límite Cusco-Puno; altitud
     no reportada en el cuadro fuente de altitudes, zona de puna alta)
   - P_Llalli_mm          — Llalli, 3,980 msnm
   - P_Macusani_mm        — Macusani, 4,341 msnm
   - P_Sicuani_mm         — Sicuani, 3,546 msnm
   - P_Ccatcca_mm         — Ccatcca, 3,729 msnm
   - P_Granja_Kayra_mm    — Granja Kayra, 3,238 msnm
   - P_Paruro_mm          — Paruro, 3,092 msnm
   - P_Paucartambo_mm     — Paucartambo, 2,937 msnm
   - P_Pisac_mm           — Pisac, 2,950 msnm
   - P_Pomacanchi_mm      — Pomacanchi, 3,723 msnm
   - P_Urubamba_mm        — Urubamba, 2,884 msnm
   - P_Cirialo_mm         — Cirialo, 900 msnm (selva alta)
   - P_Curahuasi_mm       — Curahuasi, 2,763 msnm
   - P_Machupicchu_mm     — Machupicchu, 2,563 msnm
   - P_Quillabamba_mm     — Quillabamba, 1,022 msnm (selva alta)
   - P_Vilcabamba_mm      — Vilcabamba, 4,000 msnm
   - P_La_Quebrada_mm     — La Quebrada, 1,205 msnm (selva alta)
   - P_Huyro_mm           — Huyro (selva alta, sin altitud reportada en el cuadro)
   - P_Chontachaca_mm     — Chontachaca, 901 msnm (selva alta)
   - P_Pakitza_mm         — Pakitza, 319 msnm (selva baja)
   - P_Quincemil_mm       — Quincemil, 675 msnm (selva baja)

## IV. QA/QC

- ⚠️ IMPORTANTE — Series ya "completadas", no 100% observación cruda: el Volumen I
  (sección 5.3.5 "Completación y Extensión de los Valores Ausentes") documenta que
  el equipo del estudio rellenó los vacíos de cada estación mediante regresión
  múltiple con correlación espacial (software HEC-4), usando como referencia la
  estación de mayor longitud de registro dentro de su mismo "bloque pluviométrico".
  Como resultado, las 21 series de este dataset no tienen ningún valor vacío
  (0% de datos faltantes) en el periodo 1964-2008 — pero una parte de esos valores
  son ESTIMADOS estadísticamente, no medidos directamente en el observatorio. El
  dataset no distingue cuáles meses son observación original y cuáles fueron
  completados; si esa distinción es crítica para el uso previsto, debe solicitarse
  la información de origen (bloques crudos previos a la completación).
- Bloques pluviométricos usados para la completación (agrupación por correlación
  espacial, Volumen I):
  * Bloque I:   La Raya, Llalli, Macusani, Sicuani
  * Bloque II:  Ccatcca, Granja Kayra, Paruro, Paucartambo, Pisac, Pomacanchi,
                Urubamba
  * Bloque III: Cirialo, Curahuasi, Machupicchu, Quillabamba, Vilcabamba,
                La Quebrada, Huyro
  * Bloque IV:  Chontachaca, Machupicchu, Pakitza, Paucartambo, Quincemil
  (Paucartambo y Machupicchu aparecen en dos bloques cada una, al haber servido de
  referencia cruzada entre grupos).
- Extracción: tablas leídas con `python-docx` conservando la estructura fila (año) /
  columna (mes) original, sin reordenar ni reinterpretar valores.
- No se calculó un equivalente en volumen (MMC): a diferencia del caudal, la
  precipitación es una lámina de agua (mm) referida a un punto, no un flujo; para
  convertirla a volumen se requiere el área de influencia de cada estación (p. ej.
  el polígono de Thiessen correspondiente), dato que existe en el Volumen I pero que
  no se incorporó a este archivo.

## V. Dominio espacial y coordenadas

El documento fuente no reporta coordenadas UTM ni lat/lon de los observatorios
pluviométricos individuales, solo su altitud (incluida en la sección III) y su
pertenencia a la cuenca Urubamba o a cuencas vecinas. No se realizó una búsqueda
externa de coordenadas para este dataset — a diferencia de las estaciones de aforo
de caudal (menos numerosas y más fácilmente identificables en portales públicos),
verificar de forma confiable la ubicación exacta de 21 observatorios pluviométricos
excede el alcance de esta entrega. Si se requieren coordenadas precisas, la fuente
recomendada es el portal de SENAMHI o el listado oficial de estaciones del SENAMHI
(shapefile de estaciones hidrometeorológicas).
Referencia general: las estaciones cubren un rango altitudinal muy amplio, desde
zona de puna alta (Macusani, 4,341 msnm) hasta selva baja (Pakitza, 319 msnm),
reflejando el gradiente altitudinal completo de la cuenca del Urubamba, desde su
cabecera en el Nudo de Vilcanota (cerca del Abra La Raya, límite Cusco-Puno) hasta
su tramo de selva en la provincia de La Convención.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `cusco_precipitacion.csv` a `urubamba_precipitacion_multiestacion.csv`.
- Metadata consolidada y reformateada desde `cusco_precipitacion_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.

**Contenido adicional no clasificado de la fuente original** (preservado para no perder información):

================================================================================
METADATOS DEL DATASET DE PRECIPITACIÓN MULTIESTACIÓN - CUENCA DEL RÍO URUBAMBA (CUSCO)
================================================================================
