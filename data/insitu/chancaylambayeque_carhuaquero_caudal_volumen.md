# Metadata — Caudal y Volumen Mensual, Estación Carhuaquero/Raca Rumi (Río Chancay-Lambayeque)

**⚠️ Nota de ámbito:** este dataset **no pertenece a la cuenca del río Zaña**. Llegó en el mismo lote de archivos ("Anexo_2.xls") junto con las fuentes de Zaña, pero es del río **Chancay-Lambayeque**, cuenca vecina (departamento Lambayeque, sistema Tinajones). Se procesa como dataset independiente, sin fusionarlo con nada de Zaña, y sin relación con `chancayhuaral_stodomingo_caudal_volumen_crudo/homogenizado.csv` ya existentes en el proyecto — esos son del río **Chancay-Huaral** (departamento Lima, cuenca completamente distinta que solo comparte el nombre "Chancay"). Verificado: no hay superposición ni riesgo de contaminación entre ambos.

## I. Información general

- **Nombre de archivo:** `chancaylambayeque_carhuaquero_caudal_volumen.csv`
- **Ámbito geográfico:** Cuenca del río Chancay-Lambayeque, estación hidrométrica Carhuaquero / Raca Rumi (la fuente cita ambos nombres juntos, probablemente estructura de derivación/bocatoma Raca Rumi asociada a la central hidroeléctrica Carhuaquero).
- **Departamento/Región:** Lambayeque, Perú.
- **Resolución temporal:** Mensual.
- **Periodo de registro:** 1930-01 a 2004-12 (75 años, 900 meses). **Nota:** el encabezado de la fuente dice "SERIE HOMOGENIZADA Y COMPLETADA - PERIODO 1914 / 2004", pero la tabla de datos empieza en la fila correspondiente a 1930, no 1914. Discrepancia de la fuente, reportada tal cual, no resuelta unilateralmente.
- **Desfase respecto al año calendario:** Ninguno. Año calendario (Ene-Dic).
- **% de completitud:** 100% (900/900 meses, sin valores "S/D" ni vacíos).
- **Versión de la serie:** la fuente indica explícitamente "serie homogenizada y completada" — es decir, **ya viene procesada** (huecos rellenados y datos homogenizados) por el estudio de origen, no es la serie cruda/histórica sin procesar. No se dispone en este lote de la versión cruda para contraste.

## II. Fuentes de datos originales

| Documento | Entidad emisora | Año | Aporte específico |
|---|---|---|---|
| `Anexo_2.xls` (hoja "Hoja1") | No se declara explícitamente en el archivo; pie de página cita: *"Propuesta de Asignaciones de Agua en Bloque (Volúmenes Anuales y Mensuales) para la Formalización de los Derechos de Uso de Agua en el Valle Chancay-Lambayeque - PROFODUA"* | No se indica año de procesamiento explícito | Serie de caudales medios mensuales naturales, 1930-2004, ya homogenizada y completada por el estudio de origen. Fuente primaria y única de los valores numéricos usados en este dataset. |

**Advertencia sobre la fuente:** no se recibieron los capítulos narrativos del informe final del lote de Zaña ni `Anexo_18.xls`; en cualquier caso, este dataset es de una cuenca distinta (Chancay-Lambayeque, no Zaña), por lo que es poco probable que esos archivos faltantes hubieran aportado contexto adicional para esta estación específica.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `AÑO` + columnas `ENE`…`DIC` | `date` + `caudal_carhuaquero_m3s` |
| *(no existía en la fuente)* | `volumen_carhuaquero_mmc` |

---

| Columna | Descripción | Unidad | Fuente | Fórmula |
|---|---|---|---|---|
| `date` | Primer día del mes calendario | YYYY-MM-DD | — | — |
| `caudal_carhuaquero_m3s` | Caudal medio mensual "natural" (homogenizado y completado por la fuente), estación Carhuaquero/Raca Rumi | m³/s | Medido/procesado por la fuente (homogenización ya aplicada, metodología no detallada en este archivo) | — |
| `volumen_carhuaquero_mmc` | Volumen mensual equivalente | MMC (millones de m³) | **Calculado** (no venía en la fuente) | `V = Q_promedio_mensual (m³/s) × (n_días_del_mes × 86 400) / 10⁶`, usando el número real de días de cada mes/año (considera años bisiestos), redondeado a 2 decimales. Caudal redondeado a 3 decimales (precisión cercana a la original de la fuente). |

## IV. QA/QC

**Transformaciones aplicadas:**
- Conversión de la tabla ancha (año × 12 meses, filas 6-80 de "Hoja1") a formato largo con columna `date`.
- Cálculo de volumen mensual (MMC) a partir del caudal, ya que la fuente **no trae volumen**, usando días reales del mes (bisiestos incluidos) — documentado aquí como valor derivado, no medido.

**Valores "S/D" o faltantes:** ninguno (900/900 meses completos), consistente con que la fuente ya declara la serie como "completada".

**Continuidad temporal:** sin huecos de calendario en el rango 1930-01 a 2004-12.

**Valores negativos:** ninguno (0 registros negativos).

**Rango de valores:** mínimo 1.457 m³/s (septiembre 1997), máximo 160.436 m³/s (marzo 1971).

**Valores atípicos (IQR por mes calendario, no global):** 30 meses fuera de rango intercuartílico, todos por exceso (ningún atípico bajo). Concentrados en años húmedos/El Niño conocidos de la costa norte peruana:
- **Marzo:** 1971 (160.4 m³/s), 1975 (149.8 m³/s) — muy por encima del límite superior (127.15 m³/s).
- **Abril-mayo:** 1998 (136.5 / 74.4 m³/s, El Niño 1997-98), 1973, 1975, 1976, 1983 (El Niño 1982-83), 1999-2000 (post-Niño húmedo), 1941.
- **Junio-julio:** 1999 (42.9 / 30.7 m³/s), 1973, 1975, 1984.
- **Agosto-octubre:** 1971, 1974, 1975, 1947.
- **Noviembre-diciembre:** 1947 (56.1 m³/s), 1982, 1970.

**Interpretación:** consistentes con eventos El Niño documentados (1972-73, 1982-83, 1997-98) y años húmedos regionales (1971, 1975, 1947), igual que en los datasets de cuencas vecinas ya estandarizados (La Leche, Jequetepeque, Zaña). No se removieron ni ajustaron estos valores — la fuente ya viene "homogenizada y completada" por el estudio de origen, y esta entrega no aplicó ninguna corrección adicional propia.

**Nota metodológica no verificable con esta fuente:** al no contar con el informe narrativo, no se pudo confirmar qué método de homogenización/completación se aplicó (p. ej. si es un método análogo a HEC4 usado en Chancay-Huaral) ni si existió un proceso de "naturalización" del caudal (remoción de efectos de regulación/derivación antrópica aguas arriba, dado que la fuente llama a la serie "descargas... naturales").

## V. Dominio espacial y coordenadas

**Estación Carhuaquero/Raca Rumi, río Chancay-Lambayeque:**
- Coordenadas: **no documentadas en `Anexo_2.xls`** (el archivo no trae encabezado de latitud/longitud). No se inventan coordenadas.
- **Referencia cruzada no verificada para esta fuente:** el dataset ya existente `costaperu_volumen_persistencia_climatologia.md` (de otro estudio, "Estudio General de la Oferta de Agua Superficial de los ríos de la Costa") cita una estación **"Chancay-Lambayeque | Racarrumi | 325 msnm | 06°39'S, 79°22'W | periodo 1914-2000"**. El nombre coincide (Racarrumi) y el periodo nominal "1914" también coincide exactamente con el que aparece (aunque sin datos tabulados hasta ahí) en el encabezado de este Anexo 2, lo cual sugiere razonablemente que es la misma estación o el mismo punto de control. **No se asume la equivalencia como confirmada** — se deja para que el usuario decida si usar esa coordenada (325 msnm, 06°39'S, 79°22'W) para este dataset, dado que proviene de un documento distinto al de esta fuente.

**Bounding box recomendado para extracción GRACE-FO Mascon** (si se acepta la coordenada de referencia cruzada anterior, ± 0.5°, **pendiente de confirmación del usuario**):
- Latitud: -6.15° a -7.15°
- Longitud: -78.87° a -79.87°

*(En convención decimal WGS84, si se confirma: 06°39'S = -6.65°, 79°22'W = -79.367°)*

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Fuente original: `Anexo_2.xls` (recibido en `.xls`, convertido solo para lectura a `.xlsx` con LibreOffice; el archivo fuente original no fue modificado).
- Se procesó como dataset **separado e independiente de Zaña**, por tratarse de otra cuenca (ver advertencia al inicio de este documento), a solicitud explícita del usuario tras reportarse la ambigüedad.
- Se verificó explícitamente que no hay superposición con `chancayhuaral_stodomingo_caudal_volumen_crudo/homogenizado.csv` ya existentes: aquellos son del río Chancay-**Huaral** (Lima), este es del río Chancay-**Lambayeque** (Lambayeque) — cuencas distintas, sin relación hidrológica ni de nomenclatura real más allá del nombre compartido "Chancay".
- Volumen mensual (MMC) calculado a partir del caudal (no venía en la fuente), documentado como valor derivado en Sección III.
- Nombre de archivo asignado siguiendo la convención `<ambito>_<calificador_estacion>_<categoria>.csv` (mismo patrón usado en `chancayhuaral_stodomingo_caudal_volumen_*.csv`) → `chancaylambayeque_carhuaquero_caudal_volumen.csv`.
- Columnas de valor nombradas `caudal_carhuaquero_m3s` / `volumen_carhuaquero_mmc` siguiendo la convención `<variable>_<estacion>_<unidad>`.
- Pendiente para el usuario: confirmar si se acepta la coordenada de referencia cruzada de Sección V, y si el "1914" del encabezado de la fuente amerita alguna nota adicional o gestión (p. ej. solicitar la tabla completa 1914-1929 si existe en otro archivo no recibido).
