# Metadata — Metadata — Dataset Precipitación, Estaciones La Viña y Puchaca (Cuenca La Leche)

## I. Información general

- **Nombre de archivo:** `precipitacion_lavina_puchaca_1964_1982.csv`
- **Ámbito geográfico:** Cuenca del río La Leche
- **Departamento/Región:** Lambayeque, Perú
- **Resolución temporal:** Mensual
- **Periodo de registro:** 1964-01 a 1982-12 (19 años, 228 meses) para ambas estaciones
- **Desfase respecto al año calendario:** Ninguno (Ene–Dic).
- **% de completitud:**
  - `precipitacion_lavina_mm`: 100% (228/228)
  - `precipitacion_puchaca_mm`: 99.56% (227/228 — 1 valor NA por dato ilegible en la fuente)

## II. Fuentes de datos originales

| Documento | Entidad emisora | Año | Aporte específico |
|---|---|---|---|
| `InfClimatLaLeche.xls` (hoja "Precipitación") | DEPOLTI (Dirección Ejecutiva del Proyecto Olmos-Tinajones), datos operados originalmente por el Proyecto Olmos | Compilado en 2005–2006 | Única fuente de los valores numéricos de precipitación mensual de ambas estaciones. |
| `InformeLaLeche.doc` (PROFODUA) | INRENA – Intendencia de Recursos Hídricos | 2006 | Confirma el periodo empleado para La Viña (1964–1982), que la estación está **actualmente desactivada**, y que la serie **no mostró saltos ni tendencias, por lo que se usó tal como aparece en el registro, sin corrección por inconsistencia**. No se usó como fuente de datos numéricos (los cuadros correspondientes están incrustados como imágenes en el Word). |

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `precipitacion_lavina_mm` | `precipitacion_lavina_mm` |
| `precipitacion_puchaca_mm` | `precipitacion_puchaca_mm` |

---

| Columna | Descripción | Unidad | Fuente | Fórmula |
|---|---|---|---|---|
| `date` | Primer día del mes calendario | YYYY-MM-DD | — | — |
| `precipitacion_lavina_mm` | Precipitación mensual acumulada, estación La Viña | mm | Medido (DEPOLTI / Proyecto Olmos) | — |
| `precipitacion_puchaca_mm` | Precipitación mensual acumulada, estación Puchaca (climatológica) | mm | Medido (DEPOLTI / Proyecto Olmos) | — |

No se incluye `precipitacion_areal_*` en esta entrega: la fuente no documenta un método de ponderación por área de influencia (Thiessen, polígonos, promedio aritmético) para estas dos estaciones. Si se desea, puedo calcular un promedio aritmético simple explícitamente etiquetado como tal, pero no se debe interpretar como una precipitación areal validada sin ese cálculo documentado por el estudio original.

## IV. QA/QC

**Transformaciones aplicadas:**
- Conversión de la tabla ancha (año × 12 meses) por estación a formato largo con columna `date`.
- Las dos estaciones se combinaron en un único CSV mediante `date` (unión externa/outer join), ya que ambas cubren exactamente el mismo rango 1964–1982.

**Dato ilegible/ambiguo — regla no negociable aplicada:**
- **Puchaca, febrero de 1973:** el valor en la fuente aparece escrito como `"125,,7"` (doble coma, formato corrupto/ambiguo — podría ser 125.7, 1257, u otro error de digitación/exportación). **No se estimó ni se interpretó el valor.** Se registró como `NA` en `precipitacion_puchaca_mm`, según la regla no negociable del proyecto de no inventar ni "adivinar" valores ilegibles.

**Valores marcados como "corregidos" o "completados" en la fuente original:**
- Ninguno detectado. `InformeLaLeche.doc` declara explícitamente para La Viña: *"no muestran saltos ni tendencias por lo que no se precisó de correcciones por inconsistencia, empleándose la información tal como aparece en el registro."* No hay declaración equivalente específica para la serie de precipitación de Puchaca, pero tampoco se encontró ninguna marca de corrección en la hoja de origen.

**Valores atípicos (IQR por mes calendario) y su interpretación:**
Se calcularon límites IQR por mes calendario (no globalmente), dado que la precipitación en esta zona costera árida es fuertemente estacional (lluvias concentradas en enero–abril, prácticamente nulas en junio–septiembre). Esto produce un patrón esperado y **no un indicio de error**: en los meses secos, la mediana y el IQR son ≈0, por lo que **cualquier registro de lluvia, incluso pequeño (ej. 0.5–2 mm en julio), se marca estadísticamente como "atípico"** aunque sea un valor perfectamente plausible. Por esta razón, la lista completa de atípicos detectados (30 en La Viña, 24 en Puchaca) se interpreta con cautela y se resume así:
- **Atípicos en meses secos (Jun–Sep), magnitud pequeña (<10 mm):** consistentes con lluvias esporádicas ocasionales típicas de la costa norte peruana; no se consideran errores.
- **Atípicos de magnitud mayor en meses lluviosos (Ene–Abr), notablemente:**
  - Puchaca, marzo 1972: **486.4 mm** — el valor máximo de toda la serie.
  - Puchaca, marzo 1971: 360.3 mm; marzo 1975: 307.4 mm; enero 1973: 160.0 mm; enero 1976: 133.3 mm.
  - La Viña, marzo 1972: 239.3 mm; marzo 1971: 144.7 mm; marzo 1975: 110.9 mm.

  Estos meses (1971, 1972, 1975-76) corresponden a años con anomalías cálidas moderadas documentadas en la costa norte del Perú (Niños de magnitud moderada/débil en 1972-73 y 1976); no se encontró en las fuentes entregadas una narrativa específica que discuta estos años puntuales para precipitación (a diferencia del caudal de Puchaca, donde sí se documentó explícitamente 1998, 2001 y 2002), por lo que se marcan como **extremos plausibles pero sin confirmación textual directa en la fuente** — se recomienda verificarlos contra un registro independiente de SENAMHI si se requiere alta confianza en años específicos.

**Continuidad temporal:** sin meses faltantes en el rango 1964-01 a 1982-12 (228/228) para ambas estaciones.

**Valores negativos:** ninguno (correcto, la precipitación no puede ser negativa).

**Limitaciones conocidas:**
- El periodo (1964–1982) **no se superpone en absoluto con GRACE ni GRACE-FO** (GRACE: 2002–2017; GRACE-FO: 2018–presente). Esta serie es útil como referencia climatológica/histórica de la cuenca, pero **no sirve directamente para validación de anomalías TWSA satelitales** sin datos de precipitación más recientes (no incluidos en los archivos entregados).
- La estación La Viña está actualmente desactivada según `InformeLaLeche.doc`.
- No se cuenta con información sobre el instrumento de medición (pluviómetro/pluviógrafo) ni su incertidumbre.

## V. Dominio espacial y coordenadas

| Estación | Latitud | Longitud | Altitud | Fuente |
|---|---|---|---|---|
| La Viña | 06°23′00″ S | 79°46′00″ O | 53 m.s.n.m. | `InfClimatLaLeche.xls`, hoja "Precipitación" |
| Puchaca (climatológica) | 06°23′00″ S | 79°29′00″ O | 400 m.s.n.m. | `InfClimatLaLeche.xls`, hoja "Precipitación" |

**⚠️ Discrepancia ya reportada en el dataset de caudal:** esta estación "Puchaca" climatológica (lon 79°29′O, alt 400 msnm) **no tiene las mismas coordenadas/altitud** que la estación hidrométrica "Puchaca" usada en el dataset de caudal/volumen (lon 79°28′O, alt 250 msnm). Se mantienen como registros distintos; no se promedian ni se asume que sean el mismo punto físico.

**Bounding box recomendado para extracción GRACE-FO Mascon** (cubriendo ambas estaciones de precipitación ± 0.5°):
- Latitud: -6.883° a -5.883°
- Longitud: -80.267° a -78.983°

*(La Viña: -6.383°, -79.767° | Puchaca-clima: -6.383°, -79.483°)*

---

# Resumen ejecutivo

**Completitud:** 100% (La Viña) / 99.56% (Puchaca-clima, 1 NA de 228).

**Tabla de alertas de calidad:**

| Alerta | Severidad | Descripción |
|---|---|---|
| Sin superposición temporal con GRACE/GRACE-FO | 🔴 Alta | Periodo 1964–1982 termina 20+ años antes del lanzamiento de GRACE (2002). No sirve para validación directa sin datos más recientes. |
| Valor ilegible en fuente (Puchaca, feb-1973) | 🟡 Media | Registrado como `"125,,7"` en el Excel original; marcado como NA, no estimado. |
| Discrepancia de coordenadas "Puchaca" | 🟡 Media | Ya reportada en el dataset de caudal — estación climatológica ≠ estación hidrométrica del mismo nombre. |
| Numerosos "atípicos" IQR en meses secos | 🟢 Baja (informativo) | Artefacto esperado de la fuerte estacionalidad/aridez de la zona; no indica error de datos. |
| Extremos de marzo 1971/1972/1975 sin confirmación textual | 🟡 Media | A diferencia de El Niño 1998 (caudal), estos años no fueron discutidos explícitamente en los informes narrativos entregados; se recomienda verificación cruzada si es crítico para el análisis. |

**Alcance y limitaciones de esta entrega:**
Cubre precipitación mensual de las dos únicas estaciones con serie de texto extraíble en la cuenca La Leche (La Viña y Puchaca-clima), 1964–1982. No incluye precipitación areal (no documentada en fuente). No incluye estaciones fuera de la cuenca (ej. Cuadrado, usada solo para humedad/viento/sol). Pendiente: evapotranspiración, nivel freático, y clima complementario (temperatura, humedad relativa, viento, horas de sol), según lo acordado en la auditoría inicial.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `laleche_precipitacion.csv` a `laleche_precipitacion.csv`.
- Metadata consolidada y reformateada desde `laleche_precipitacion_metadata.md` a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
