# Metadata — Precipitación Mensual, Estación Cayaltí (Valle del Río Zaña)

## I. Información general

- **Nombre de archivo:** `zana_precipitacion.csv`
- **Ámbito geográfico:** Valle del río Zaña, Comisión de Regantes Cayaltí (estación climatológica Cayaltí, categoría SENAMHI "CO").
- **Departamento/Provincia/Distrito:** Lambayeque / Chiclayo / Cayaltí.
- **Resolución temporal:** Mensual.
- **Periodo de registro:** 1977-01 a 1987-12 (11 años, 132 meses).
- **Desfase respecto al año calendario:** Ninguno. Se entrega en año calendario (Ene–Dic), tal como está organizada en la fuente.
- **% de completitud:** 100% (132/132 meses, sin valores "S/D") para precipitación.

## II. Fuentes de datos originales

| Documento | Entidad emisora | Año | Aporte específico |
|---|---|---|---|
| `Anexo_1.xls` (hoja "Hoja1", bloque "PRECIPITACION, Total Mensual (mm)", filas 131-147) | SENAMHI (dato origen, según nota "Fuente: SENAMHI" al pie de la hoja) | Sin fecha de procesamiento explícita en el archivo (anexo de un estudio PROFODUA del Valle Zaña) | Precipitación total mensual de la estación Cayaltí, 1977-1987. Fuente primaria y única de los valores numéricos usados en este dataset. |
| `Anexo_1.xls` (hoja "Hoja1", bloques de Temperatura, Humedad Relativa, Horas de Sol y Viento 07h/13h/19h/media, filas 7-129) | SENAMHI | Idem | Misma estación y mismo periodo, pero para otras variables climáticas (1975-1987, 13 años). **No incluidas en esta entrega** por alcance solicitado (solo precipitación); quedan disponibles en la fuente para una entrega futura si se requiere. |
| `Anexo_1.xls` (hoja "Hoja2", "PARAMETROS METEOROLOGICOS DE LA ESTACION CAYALTI") | SENAMHI / elaboración del estudio | Idem | Climatología mensual (promedios) de todas las variables de la Hoja1, incluida precipitación. Es un resumen derivado de la misma serie de Hoja1 (coincide exactamente con la fila "Prom." de Hoja1) — **no se usó como fuente independiente**, es redundante con los datos año-por-año ya usados aquí. |

**Advertencia sobre la fuente:** no se recibieron (o no llegaron adjuntos) los capítulos narrativos del informe final del estudio (`Cap_4`/`Cap_5-6 INFORME FINAL_Zaña.doc`, ni `Anexo_18.xls`), que en otros ámbitos ya estandarizados (ej. La Leche) aportaron contexto sobre la entidad emisora exacta, el año de procesamiento y advertencias de calidad. Por ahora, la única atribución disponible es la nota "Fuente: SENAMHI" impresa en la propia hoja de cálculo.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Año` + columnas `Ene.`…`Dic.` (bloque "PRECIPITACION, Total Mensual (mm)") | `date` + `precipitacion_cayalti_mm` |

---

| Columna | Descripción | Unidad | Fuente | Fórmula |
|---|---|---|---|---|
| `date` | Primer día del mes calendario | YYYY-MM-DD | — | — |
| `precipitacion_cayalti_mm` | Precipitación total mensual, estación Cayaltí | mm | Medido (SENAMHI) | — |

## IV. QA/QC

**Transformaciones aplicadas:**
- Conversión de la tabla ancha (año × 12 meses) del bloque "PRECIPITACION, Total Mensual (mm)" (filas 134-144 de la hoja "Hoja1") a formato largo con columna `date`.
- Sin redondeo adicional: los valores se mantienen con la precisión decimal original de la fuente.

**Valor ambiguo resuelto con el usuario:**
- Junio de 1983: el valor original en la fuente está escrito como `7..2` (doble punto decimal, error evidente de tecleo). Se consultó al usuario, quien confirmó la transcripción como **7.2 mm**. Documentado aquí como decisión conjunta, no como lectura automática.

**Valores "S/D" o faltantes:** ninguno dentro del rango 1977-1987 (132/132 meses completos).

**Cobertura temporal:** la fuente trae temperatura/humedad/viento/horas de sol desde 1975, pero el bloque de precipitación específicamente **empieza en 1977** (no hay datos de precipitación de 1975-1976 en esta fuente).

**Valores atípicos (IQR por mes calendario, no global):**

Se detectaron atípicos altos en varios meses, concentrados sobre todo en **1983**:

| Mes | Valor atípico | Q3 del mes | Límite superior IQR |
|---|---|---|---|
| Ene | 1983: 53.1 mm | 9.20 | 23.00 |
| Mar | 1981: 53.7 mm; 1983: 199.3 mm | 19.20 | 42.08 |
| Abr | 1983: 184.6 mm; 1987: 20.5 mm | 6.85 | 16.82 |
| May | 1983: 66.3 mm | 2.75 | 6.50 |
| Jun | 1983: 7.2 mm; 1984: 3.5 mm | 0.70 | 1.75 |
| Jul | 1984: 4.3 mm; 1987: 28.0 mm | 0.40 | 1.00 |
| Ago | 1983: 0.6 mm; 1986: 1.4 mm | 0.10 | 0.25 |
| Set | 1977: 4.0 mm; 1978: 2.7 mm | 0.85 | 2.12 |
| Oct | 1982: 6.7 mm; 1984: 7.5 mm | 2.20 | 4.75 |
| Dic | 1982: 6.9 mm | 2.70 | 6.75 |

**Interpretación:** los meses de **enero-mayo de 1983** son consistentes con el Fenómeno El Niño extraordinario de 1982-83, documentado ampliamente para la costa norte peruana (mismo evento que aparece como atípico en `laleche_caudal_volumen.md` y `jequetepeque_caudal_volumen.md` del mismo periodo). La propia fuente lo confirma explícitamente: incluye una fila "Promedio sin considerar el año 1983 (Fenómeno El Niño)" con un promedio mensual alternativo, lo que indica que los autores del estudio ya identificaban 1983 como año anómalo a excluir de climatologías. **No se removió ni ajustó ningún valor** — el dataset entrega la serie completa tal cual, incluido 1983. El resto de atípicos menores (1977, 1978, 1981, 1982, 1984, 1986, 1987) no tienen mención explícita individual en la fuente, pero son de magnitud moderada y consistentes con la variabilidad interanual conocida de la costa norte peruana.

**Valores negativos:** ninguno (0 registros negativos, físicamente correcto para precipitación).

**Limitaciones conocidas:**
- La serie termina en diciembre de 1987, muy anterior al periodo de operación de GRACE (2002+) y GRACE-FO (2018+). No se superpone con ninguna de las dos misiones — solo sirve como referencia histórica/climatológica de la zona.
- No se recibieron los capítulos narrativos del informe final ni el Anexo 18 (ver Sección II), por lo que no se pudo verificar contexto adicional sobre la estación (año de instalación, metodología, posibles interrupciones no reflejadas en la tabla).
- No se incluyen en este archivo las demás variables climáticas de la misma estación y periodo (temperatura, humedad relativa, viento, horas de sol) — disponibles en la misma fuente (`Anexo_1.xls`, hoja "Hoja1") si se requieren en una entrega posterior.

## V. Dominio espacial y coordenadas

**Estación climatológica Cayaltí** (fuente de este dataset):
- Latitud: 06°53'53.7'' S
- Longitud: 79°33'33.7" O
- Altitud: 102.3 m.s.n.m.
- Categoría: "CO" (Climatológica Ordinaria, SENAMHI)
- Fuente de la coordenada: `Anexo_1.xls`, encabezado de la hoja "Hoja1"/"Hoja2" (única fuente de coordenadas disponible; no hay informe narrativo para contrastar, ver advertencia en Sección II).

**Bounding box recomendado para extracción GRACE-FO Mascon** (estación Cayaltí ± 0.5°):
- Latitud: -7.398° a -6.398°
- Longitud: -80.059° a -79.059°

*(En convención decimal WGS84: 06°53'53.7"S = -6.8983°, 79°33'33.7"O = -79.5594°)*

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Fuente original: `Anexo_1.xls` (recibido en formato `.xls`, convertido solo para lectura a `.xlsx` con LibreOffice; el archivo fuente original no fue modificado).
- Extraído únicamente el bloque "PRECIPITACION, Total Mensual (mm)" de la hoja "Hoja1" (filas 131-147), a pedido explícito del usuario — se excluyeron deliberadamente temperatura, humedad relativa, horas de sol y viento, presentes en la misma fuente.
- Valor de junio 1983 (`7..2` en la fuente) transcrito como `7.2` tras confirmación explícita del usuario (ver Sección IV).
- Nombre de archivo asignado siguiendo la convención `<ambito>_<categoria>.csv` → `zana_precipitacion.csv`.
- Columna de valor nombrada `precipitacion_cayalti_mm` siguiendo la convención `<variable>_<estacion>_<unidad>`.
- Pendiente para el usuario: confirmar si se desea una entrega adicional con las otras variables climáticas de Cayaltí (temperatura, humedad, viento, horas de sol), y si se recuperan los archivos faltantes (`Anexo_18.xls`, `Cap_4`/`Cap_5-6 INFORME FINAL_Zaña.doc`) para enriquecer el contexto de este y otros datasets de Zaña.
