# Metadata — METADATOS DEL DATASET DE: CAUDALES Y VOLÚMENES MENSUALES - CUENCA CHIRA-PIURA

## I. Información general

Nombre del dataset: caudales_chira_piura.csv
Región / Cuenca: Cuenca hidrográfica Chira-Piura, Región Piura, Perú
Proyecto de origen: Gestión de la Oferta de Agua en las Cuencas de los Proyectos
Hidráulicos de Costa del INADE (Instituto Nacional de Desarrollo) - Estudio ATA-INADE
(Asesores Técnicos Asociados)
Variable(s): Caudal medio mensual (m3/s) y volumen mensual derivado (MMC - Millones
de Metros Cúbicos)
Resolución temporal: Mensual
Cobertura temporal del dataset combinado: Enero 1937 - Diciembre 2000 (768 meses)
  - Río Chira: Enero 1937 - Diciembre 2000 (64 años, serie completa, sin vacíos)
  - Río Piura: Enero 1953 - Diciembre 2000 (48 años, serie completa, sin vacíos;
    valor 0 registrado en 218 meses, consistente con el régimen estacional/seco del
    río Piura durante meses de estiaje, no representa un dato faltante)
Fecha de generación de este dataset: procesamiento QA/QC realizado en la fecha de
entrega de este documento, a partir de archivos fuente Microsoft Excel (.xls) de 2002
Propósito: Insumo para validación estacional y de tendencia de datos TWS (Terrestrial
Water Storage) de GRACE-FO sobre la cuenca Chira-Piura

## II. Fuentes de datos originales

1. Qmmes_y_Tend__Chira.xls
   - Hoja: "Hoja1"
   - Título original: "RIO CHIRA - CAUDALES MEDIOS MENSUALES - ESTACION PTE.
     SULLANA/ARDILLA (m3/s) - PERIODO: 1937-2000"
   - Contiene además, en filas adicionales no incorporadas a este CSV: promedio,
     desviación estándar, coeficiente de variación, tendencia (1937-2000), caudal
     máximo y caudal mínimo por mes calendario.
2. Qmmobil_Chira.xls
   - Hoja: "Hoja1" (Hoja2 y Hoja3 vacías)
   - Título original: "RIO CHIRA - CAUDALES MEDIOS ANUALES Y MEDIAS MOVILES (m3/s) -
     ESTACION PTE. SULLANA/ARDILLA - PERIODO: 1937-2000"
   - Contiene caudal medio anual y medias móviles de 5, 10 y 15 años. No incorporado
     a este CSV mensual (ver nota en sección IV); disponible para fase de validación
     de tendencias si se requiere.
3. Qmmes_y_Tend_Piura_53-00.xls
   - Hoja: "Hoja1"
   - Título original: "RIO PIURA - CAUDALES MEDIOS MENSUALES - ESTACION PTE. SANCHEZ
     CERRO/EJIDOS (m3/s) - PERIODO: 1953-2000"
   - Contiene las mismas estadísticas descriptivas adicionales que el archivo de Chira.
4. Q_mmovil_Piura__53-00_.xls
   - Hoja: "Q mm"
   - Título original: "RIO PIURA - CAUDALES MEDIOS MENSUALES Y MEDIAS MOVILES (m3/s) -
     ESTACION PTE. SANCHEZ C./EJIDOS - PERIODO: 1953-2000"
   - Caudal medio anual y medias móviles de 5, 10 y 15 años. No incorporado a este CSV.
Todos los archivos fuente fueron creados en Microsoft Excel (formato legacy .xls,
BIFF/Compound Document V2), con última modificación registrada en septiembre de 2002,
autor "usuario", última guardado por "CAR" (Chira) y "CAR"/"ATASA" (Piura), en el
marco del estudio ATA-INADE para el Proyecto Chira-Piura.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Date` | `date` |
| `caudal_rio_chira_m3s` | `caudal_rio_chira_m3s` |
| `caudal_rio_piura_m3s` | `caudal_rio_piura_m3s` |
| `volumen_rio_chira_mmc` | `volumen_rio_chira_mmc` |
| `volumen_rio_piura_mmc` | `volumen_rio_piura_mmc` |

---

| Columna                  | Tipo   | Unidad | Descripción                                                                 |
|---------------------------|--------|--------|-------------------------------------------------------------------------------|
| Date                      | date   | -      | Fecha del registro mensual, formato YYYY-MM-DD (día fijado al 01 del mes)     |
| caudal_rio_chira_m3s      | float  | m3/s   | Caudal medio mensual del río Chira, Estación Pte. Sullana/Ardilla             |
| caudal_rio_piura_m3s      | float  | m3/s   | Caudal medio mensual del río Piura, Estación Pte. Sánchez Cerro/Ejidos        |
| volumen_rio_chira_mmc     | float  | MMC    | Volumen mensual del río Chira, calculado a partir del caudal                  |
| volumen_rio_piura_mmc     | float  | MMC    | Volumen mensual del río Piura, calculado a partir del caudal                  |
Fórmula de conversión caudal -> volumen:
  Volumen (MMC) = Caudal (m3/s) x días_del_mes x 86400 (s/día) / 1 000 000 (m3 -> MMC)
Valores vacíos (celda en blanco en el CSV): ausencia de dato en la fuente original
para ese mes/estación (aplica únicamente a caudal_rio_piura_m3s antes de enero de
1953, dado que la serie de esa estación inicia en 1953; el río Chira no presenta
vacíos en todo el periodo 1937-2000).

## IV. QA/QC

1. Extracción: los archivos .xls (formato legacy) fueron leídos con
   pandas.read_excel(engine="xlrd"). Las tablas originales tienen encabezados y
   bloques de metadatos en las primeras 10-13 filas, que fueron descartados; solo se
   extrajo el bloque de datos "Nro. Ord. | AÑO | ENE...DIC".
2. Reestructuración: los datos originales están en formato ancho (una fila por año,
   una columna por mes). Se transformaron a formato largo (una fila por mes-año) y se
   generó la columna Date en formato ISO 8601 (YYYY-MM-DD).
3. Fusión: las series de Chira y Piura se unieron por fecha mediante un "outer join",
   preservando todos los meses de ambas estaciones (1937-2000 para Chira, 1953-2000
   para Piura); los meses sin dato de Piura (1937-1952) quedan en blanco.
4. Cálculo de volumen: se calculó volumen mensual en MMC multiplicando el caudal
   medio mensual (m3/s) por el número exacto de días de cada mes calendario
   (considerando años bisiestos) y por 86 400 s/día, dividido entre 1x10^6 para
   convertir m3 a millones de m3 (MMC).
5. Validaciones de calidad ejecutadas sobre el dataset final:
   - Sin valores negativos en caudal_rio_chira_m3s ni caudal_rio_piura_m3s.
   - Sin fechas duplicadas (768 filas = 64 años x 12 meses, sin duplicados).
   - Total de filas = 768, conteo esperado verificado (64 años x 12 meses).
   - Vacíos en caudal_rio_piura_m3s: 192 registros (=16 años x 12 meses), todos y
     únicamente correspondientes al periodo 1937-1952, previo al inicio de la serie
     de esa estación — consistente con la fuente, no es un error de procesamiento.
   - Valores de caudal_rio_piura_m3s en 0.000: 218 registros, concentrados en los
     meses de estiaje (setiembre-diciembre principalmente); el propio archivo fuente
     ya registra estos ceros como dato válido, no como celda vacía. Consistente con
     el carácter estacional/intermitente del río Piura descrito en la documentación
     narrativa adjunta (Hidrologia_Cuenca.doc).
   - Valores máximos detectados: Chira 1861.96 m3/s en abril de 1998; Piura 1641.998
     m3/s en marzo de 1998. Ambos coinciden con el Fenómeno El Niño 1997-98,
     mencionado explícitamente en la documentación narrativa como evento hidrológico
     extremo — se interpretan como datos válidos, no outliers de captura, y no fueron
     removidos ni corregidos.
6. No incorporado a este dataset (disponible en archivos fuente para fases
   posteriores si se requiere): caudal medio anual, medias móviles de 5/10/15 años,
   desviación estándar, coeficiente de variación y estadísticos de tendencia
   mensual/anual, presentes en filas adicionales de los 4 archivos fuente.
7. Redondeo: caudal a 3 decimales; volumen a 3 decimales.

## V. Dominio espacial y coordenadas

Estaciones incluidas:
  1. Estación Pte. Sullana / Ardilla — Río Chira
  2. Estación Pte. Sánchez Cerro / Ejidos — Río Piura (también referida como
     "Pte. Sánchez C./Ejidos" en el archivo de medias móviles)
ADVERTENCIA: ninguno de los 8 documentos fuente entregados (4 .doc, 4 .xls) contiene
coordenadas geográficas explícitas (latitud, longitud, UTM ni altitud) para estas
estaciones, ni referencia a distrito/provincia de ubicación exacta. No es posible
construir un bounding box verificado con la información disponible.
Referencia geográfica aproximada (NO georreferenciada en fuente, pendiente de
verificación por el usuario):
  - Puente Sánchez Cerro se ubica sobre el río Piura, en la ciudad de Piura,
    departamento de Piura, Perú (zona urbana de Piura-Castilla).
  - Puente Ardilla / Sullana se ubica sobre el río Chira, en la ciudad de Sullana,
    departamento de Piura, Perú.
  - Bounding box aproximado de la cuenca Chira-Piura completa (referencial, según
    descripciones cualitativas del documento Hidrologia_Cuenca.doc): entre
    aproximadamente 4°30'S y 5°45'S de latitud, y 79°30'W y 81°10'W de longitud,
    departamento de Piura, Perú.
Recomendación: si se cuenta con un documento cartográfico adicional (mapas temáticos
mencionados en las fuentes, p.ej. "Mapa Temático C-08", "V-12A", "V-12C", "V-12D") o
shapefiles de las estaciones hidrométricas del PECHP (Proyecto Especial Chira-Piura),
estos permitirían completar esta sección con coordenadas verificadas.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `chira_piura_caudales.csv` a `chirapiura_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `chira_piura_caudales_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
