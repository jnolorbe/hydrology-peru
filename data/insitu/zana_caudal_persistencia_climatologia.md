# Metadata — Climatología de Persistencia de Caudales, Estación El Batán (Río Zaña)

## I. Información general

- **Nombre de archivo:** `zana_caudal_persistencia_climatologia.csv`
- **Ámbito geográfico:** Río Zaña, estación hidrométrica El Batán.
- **Departamento/Región:** Lambayeque, Perú (estación de control principal del río Zaña, aguas arriba del valle agrícola).
- **Resolución temporal:** Climatología mensual (una fila por mes calendario, no serie año-por-año).
- **Periodo base de cálculo:** Año hidrológico 1929/1930 a 2004/2005 (76 años hidrológicos, Ago-Jul), según lo declarado en la fuente.
- **% de completitud:** 100% (12/12 meses) para las 4 métricas (media, 50%, 60% y 75% de persistencia). No aplica el concepto de "meses faltantes" porque es una climatología ya resumida por la fuente, no una serie temporal año-por-año.
- **Naturaleza del dato:** Este dataset **no es una serie de caudal mensual año-por-año**. Es una curva de duración/persistencia (valores estadísticos ya calculados en la fuente original a partir de 76 años de registro), extraída tal cual del anexo — no se recalculó la curva de persistencia, solo se reorganizó de año hidrológico (Ago-Jul) a mes calendario (Ene-Dic) y se tabuló en formato largo.

## II. Fuentes de datos originales

| Documento | Entidad emisora | Año | Aporte específico |
|---|---|---|---|
| `Anexo_3.xls` ("DISTRIBUCION DE FRECUENCIAS DE LAS DESCARGAS DEL RIO ZAÑA", hoja "Hoja1", filas 108-112) | Elaboración del estudio PROFODUA-Zaña (según el estilo y metodología compartida con los demás anexos de este lote) | No se indica fecha de procesamiento explícita en el archivo | Tabla resumen "Caudal (m3/s)": Medio, 50% Persistencia, 60% Persistencia y 75% Persistencia por mes de año hidrológico, ya calculada por la fuente a partir de la distribución de frecuencias completa (76 años clasificados por rango). Única fuente numérica usada en este dataset. |
| `Anexo_3.xls` (misma hoja, filas 6-81) | Idem | Idem | Distribución de frecuencias completa: 76 filas (rango `m` = 1 a 76, frecuencia Weibull `f% = m/(n+1)×100`) con el caudal mensual de cada rango, para los 12 meses del año hidrológico + columna "Anual". **No se usó directamente en este dataset** (son los datos base de los que la fuente derivó las filas 108-112); se revisó únicamente para verificar consistencia (ver Sección IV). |
| `Anexo_3.xls`, hoja "Hoja2" | Idem | Idem | Copia idéntica de la hoja "Hoja1" (mismos encabezados y mismos primeros valores verificados fila a fila donde se comparó). Redundante, no usada como fuente independiente. |

**Advertencia sobre la fuente:** al igual que con `zana_precipitacion.csv`, no se recibieron los capítulos narrativos del informe final (`Cap_4`/`Cap_5-6 INFORME FINAL_Zaña.doc`) ni `Anexo_18.xls`. Esto significa que no se pudo confirmar contra el texto del informe: la entidad exacta que operó la estación El Batán, si "76 años" corresponde estrictamente a 1929/30-2004/05 sin interpolaciones/rellenos previos, ni las coordenadas de la estación (ver Sección V).

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `AGO`…`JUL` (fila "Medio") | `caudal_batan_medio_m3s` |
| `AGO`…`JUL` (fila "50% Persisten.") | `caudal_batan_p50_m3s` |
| `AGO`…`JUL` (fila "60% Persisten.") | `caudal_batan_p60_m3s` |
| `AGO`…`JUL` (fila "75% Persisten.") | `caudal_batan_p75_m3s` |
| (implícito, encabezado de columna en la fuente) | `mes` |

---

| Columna | Descripción | Unidad | Fuente | Fórmula |
|---|---|---|---|---|
| `mes` | Mes calendario (1=enero … 12=diciembre); la fuente organiza el año como hidrológico Ago-Jul, aquí reordenado a calendario | entero 1-12 | — | — |
| `caudal_batan_medio_m3s` | Caudal medio mensual (promedio aritmético de los 76 años de registro) | m³/s | Calculado por la fuente (no recalculado aquí) | Promedio de los 76 valores anuales de cada mes, según distribución de frecuencias de la fuente |
| `caudal_batan_p50_m3s` | Caudal con 50% de persistencia (igualado o superado el 50% del tiempo) | m³/s | Calculado por la fuente | Interpolación lineal sobre la curva de frecuencias empírica (posición de graficado Weibull, `f% = m/(n+1)×100`), tal como aparece en la fuente |
| `caudal_batan_p60_m3s` | Caudal con 60% de persistencia | m³/s | Calculado por la fuente | Idem, interpolado al 60% |
| `caudal_batan_p75_m3s` | Caudal con 75% de persistencia (caudal garantizado usado típicamente para asignación de agua agrícola) | m³/s | Calculado por la fuente | Idem, interpolado al 75% |

## IV. QA/QC

**Transformaciones aplicadas:**
- Se extrajeron únicamente las 4 filas resumen ("Medio", "50% Persisten.", "60% Persisten.", "75% Persisten.") de la tabla "Caudal (m3/s)" (filas 108-112 de "Hoja1").
- Reordenamiento de columnas: la fuente organiza los meses como año hidrológico (Ago, Set, Oct, Nov, Dic, Ene, Feb, Mar, Abr, May, Jun, Jul); aquí se reordenaron a año calendario (Ene→Dic, `mes` 1-12), sin alterar los valores.
- Redondeo a 2 decimales (los valores originales traían hasta 14 decimales por arrastre de cálculo de Excel; se redondeó por legibilidad, sin pérdida de precisión relevante).
- **No se recalculó la curva de persistencia ni la interpolación** — se tomaron los valores ya resueltos por la fuente.

**Verificación de consistencia interna:**
- La fila "Medio" (fila 109) coincide exactamente con la fila "Promedio" (fila 82, al final de la tabla de distribución de frecuencias, filas 6-81) para los 12 meses — confirma que ambas provienen del mismo cálculo interno de la fuente, sin discrepancia.
- La hoja "Hoja2" del mismo archivo es una copia idéntica de "Hoja1" (verificado en los primeros y últimos registros de la tabla de rangos) — no se usó como fuente adicional ni de contraste, ya que no aporta información independiente.
- El número de rangos (`m` = 1 a 76) es consistente con `f% = m/(n+1)×100`: para m=76, f%=98.70 = 76/77×100, confirmando n=76 años — coincide con el periodo declarado en el título del anexo (1929/1930 a 2004/2005 = 76 años hidrológicos).

**Valores atípicos:** no aplica — al ser una climatología de valores ya promediados/interpolados, no hay meses/años individuales que evaluar por IQR.

**Valores "corregidos" o "completados":** no se detectó ninguna marca de este tipo en la fuente para esta tabla resumen.

**Limitaciones conocidas:**
- Esta entrega es una **climatología**, no una serie año-por-año: no permite validación mes-a-mes contra TWSA de GRACE/GRACE-FO, solo sirve como referencia de régimen hidrológico promedio/probabilístico de la cuenca.
- No se dispone de la serie cruda de 76 años (rango `m`=1-76 con año calendario real asociado a cada rango) en este dataset; esos datos existen en la fuente (filas 6-81 de "Hoja1"/"Hoja2") pero no incluyen el año calendario de cada rango `m` (la tabla está ordenada por magnitud del caudal, no cronológicamente), por lo que no se puede reconstruir la serie año-por-año sin información adicional no presente en el archivo.
- No se cuenta con las coordenadas de la estación El Batán en esta fuente (ver Sección V) ni con el informe narrativo que las confirmaría.

## V. Dominio espacial y coordenadas

**Estación hidrométrica El Batán, río Zaña:**
- Coordenadas: **no documentadas en `Anexo_3.xls`** (el archivo no trae encabezado de latitud/longitud, a diferencia de `Anexo_1.xls`). No se inventan coordenadas — pendiente de confirmación con el usuario o de los archivos faltantes (`Cap_4`/`Cap_5-6 INFORME FINAL_Zaña.doc`, `Anexo_18.xls`).
- Ubicación descriptiva (según el nombre y el contexto de los demás anexos del mismo lote, sin coordenadas verificadas): estación de control del río Zaña, aguas arriba del valle agrícola de Zaña, Lambayeque.

**Bounding box recomendado para extracción GRACE-FO Mascon:** pendiente — no se puede calcular sin coordenadas confirmadas de la estación.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Fuente original: `Anexo_3.xls` (recibido en `.xls`, convertido solo para lectura a `.xlsx` con LibreOffice; el archivo fuente original no fue modificado).
- Extraídas únicamente las 4 filas resumen de persistencia (Medio, 50%, 60%, 75%) de la hoja "Hoja1"; se descartó la tabla completa de 76 rangos (filas 6-81) y la hoja duplicada "Hoja2" por ser redundantes.
- Reordenamiento de meses de año hidrológico (Ago-Jul) a año calendario (Ene-Dic, columna `mes` 1-12), siguiendo la convención de climatologías de la guía del proyecto.
- Nombre de archivo asignado siguiendo la convención `<ambito>_<categoria>_<calificador>.csv` → `zana_caudal_persistencia_climatologia.csv` (calificador `climatologia`, análogo a `costaperu_volumen_persistencia_climatologia.csv` ya existente en el proyecto, aunque con metodología de origen distinta: aquí es persistencia empírica por rango/Weibull directa de la fuente, no el método Weibull-75%/año-Q75/ratio de aquella).
- Columnas de valor nombradas `caudal_batan_<metrica>_m3s` siguiendo la convención `<variable>_<estacion>_<unidad>`.
- Pendiente para el usuario: coordenadas de la estación El Batán (Sección V) y confirmación de la entidad emisora/año de elaboración del estudio, ambos dependientes de los archivos faltantes reportados en `zana_precipitacion.md`.
