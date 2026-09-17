# Metadata — Caudal Diario, Río Ica / Sistema Choclococha (Estación La Achirana)

## I. Información general

- **Archivo de datos:** `ica_caudal_diario.csv`
- **Cuenca:** Cuenca integral del río Ica (incluye trasvase del Sistema Choclococha).
- **Estación de medición:** "La Achirana" (Estación Hidrométrica).
- **Resolución temporal:** Diaria.
- **Periodo cubierto:** 1922-01-01 a 2005-12-31 (84 años, 30 681 días, sin huecos de fecha).
- **Completitud:** Caudal diario Río Ica 18 521/30 681 días con dato (60.4%); Sistema Choclococha 1 288/30 681 (4.2%). Los huecos corresponden, en su gran mayoría, a meses que el documento fuente simplemente no reporta (típicamente estiaje), no a fallas de extracción.

## II. Fuentes de datos originales

- **Documento fuente:** `ANEXO_1_Qdiarios_Ica.doc` — "RÍO ICA - CAUDALES MEDIOS DIARIOS - ESTACIÓN HIDROMÉTRICA 'LA ACHIRANA' - PERIODO DE REGISTRO: 1922-2005". Documento Word legado (.doc, OLE2) con 91 objetos gráficos WMF incrustados — cada tabla anual ("Cuadro N° A1-1" a "A1-84") es una imagen, no texto ni hoja de cálculo nativa.
- **Institución:** ATDR Ica / Junta de Usuarios Distrito de Riego Ica.
- **Método de extracción (pipeline de visión por computadora):** (a) conversión de cada objeto WMF a PDF vectorial y luego PNG a 300 dpi; (b) detección automática de líneas de grilla (OpenCV) para ubicar celdas; (c) OCR (Tesseract, español) por columna sobre bandas verticales (31 días + 3 filas de estadísticos); (d) detección dinámica de encabezados de mes y sub-columnas Río Ica/Sistema Choclococha (la estructura de columnas no es uniforme entre años).

## III. Diccionario de variables

| Columna | Unidad | Descripción |
|---|---|---|
| `date` | - | Fecha calendario diaria continua (`YYYY-MM-DD`) |
| `caudal_rio_ica_achirana_m3s` | m³/s | Caudal medio diario del río Ica, estación La Achirana. Vacío = sin dato en la fuente |
| `caudal_sistema_choclococha_achirana_m3s` | m³/s | Caudal medio diario del aporte del Sistema Choclococha, reportado por separado solo cuando el cuadro original lo diferencia explícitamente (prácticamente vacío antes de 1993-1995, mezclado con Río Ica en esos años) |

*(Las columnas de volumen mensual y de control de días con dato se separaron a `ica_volumen_mensual.csv`, de resolución mensual, para no mezclar dos resoluciones temporales distintas en un mismo archivo.)*

## IV. QA/QC

- **Validación cruzada (auto-QA):** de 1 097 columnas año-mes-fuente extraídas, 1 029 (93.8%) sin discrepancia (>15%) contra los estadísticos que el propio documento imprime al pie de cada tabla; 68 (6.2%) con discrepancia señalada, concentradas en columnas nov/oct/dic de años con peor calidad de escaneo (1962-1986), mayormente por error de OCR en el punto decimal (ej. "4.63" leído como "463"). Detalle en `ica_qa_caudal_discrepancias_estadisticos.csv` (anexo).
- **Limitación conocida:** la validación no detecta errores estructurales donde una columna completa se fusionó por error de grilla (caso confirmado: febrero-2005, sub-columnas Río Ica/Choclococha leídas como una sola). Se recomienda verificación puntual contra las imágenes fuente para uso científico de alta exigencia.
- **Filtro de sanidad física:** se eliminaron 53 valores diarios fuera del rango físicamente plausible [0, 1200] m³/s (máximo histórico documentado: 1050 m³/s en 1998), en su mayoría errores de OCR que mezclaron dígitos de la columna "RESUMEN ANUAL". Detalle en `ica_qa_caudal_valores_eliminados_sanidad.csv` (anexo).
- **Años con doble cuadro en la fuente (1995-2001):** el documento original tiene dos cuadros por año (combinado vs. diferenciado); se usó la versión más desagregada. Caso especial año 2000: los dos totales anuales difieren (408.49 MMC "combinada"/Quilloay vs. 332.50 MMC "diferenciada"/La Achirana); se usó la versión diferenciada por consistencia con el resto de la serie, lo que puede implicar una subestimación de dicho año si la intención original era reportar Quilloay. Mapeo año→imagen fuente en `ica_qa_caudal_anios_duplicados.json` (anexo).
- **No incorporado:** el Anexo 2 (aforos horarios complementarios, meses sueltos 1995-1998) no se incorporó por su cobertura extremadamente dispersa; disponible como fuente secundaria de validación puntual.

## V. Dominio espacial y coordenadas

- **Estación La Achirana, río Ica:** Latitud -14.0833° (14°05'S), Longitud -75.7333° (75°44'W), Altitud 398 msnm, Provincia/Distrito Ica-Ica.
- **Bounding box:** punto único (Lat -14.0833, Lon -75.7333); si se requiere área de influencia, la cuenca integral del río Ica cubre aproximadamente 13°10'-14°53'S y 75°01'-75°54'W (8 103 km²).

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Renombrado desde `caudal_diario_rio_ica_achirana.csv` (sin cambios de columnas ni de contenido: mismo archivo, solo nombre nuevo).
- Se retiró `ica_caudal.csv`, que combinaba esta serie diaria con las columnas de volumen mensual (repetidas en cada día) y las columnas de control de calidad `dias_con_dato_*`; esas columnas ahora viven, sin repetición redundante, en `ica_volumen_mensual.csv`.
- Metadata adaptada desde `ica_caudal_metadata.txt` (que documentaba el archivo consolidado híbrido `caudal_rio_ica_achirana_CONSOLIDADO.csv`), separando el contenido relevante a la resolución diaria; ver `ica_volumen_mensual.md` para la contraparte mensual.
