# Metadata — Metadata — Dataset de Caudal y Volumen, Cuenca del Río Lurín

## I. Información general

- **Nombre de archivo:** `caudal_volumen_lurin_1964_2002.csv`
- **Ámbito geográfico:** Cuenca del río Lurín, cabecera de valle (estación Antapucro) y control aguas abajo (Puente Manchay).
- **Departamento / Región:** Lima, Perú (Provincias de Lima y Huarochirí, Distrito de Riego Lurín-Chilca).
- **Resolución temporal:** Mensual.
- **Periodo de registro:** 1964-01 a 2002-12 (39 años, 468 meses).
- **Desfase respecto al año calendario:** Ninguno para este CSV (se usa año calendario Ene–Dic). Nota: en la fuente original, algunos cuadros de persistencia usan año hidrológico Ago–Jul; ese formato **no** se usó aquí, se homogeneizó a año calendario.
- **% de completitud:** 100% en ambas columnas de caudal y sus volúmenes derivados (0 valores NA, 0 meses faltantes en el rango). Ver Sección IV sobre la naturaleza de esa "completitud" (parte de la serie es generada/completada, no observada).

---

## II. Fuentes de datos originales

| Fuente | Documento | Entidad emisora / autor | Año | Qué aportó |
|---|---|---|---|---|
| F1 | `Caudales_ANTAPUCRO.XLS`, hoja "Q Aforado" | ATDR / elaboración propia (archivo interno) | Sin fecha explícita en el archivo (última edición 2006) | Serie de caudal medio mensual histórico, estación Antapucro, 1964–2002 |
| F2 | `Datos_precip.xls`, hoja "Q Antapucro" | Ídem F1 (serie idéntica, verificada valor a valor) | — | Duplicado de F1, usado solo para verificación cruzada |
| F3 | `Datos_precip.xls`, hoja "Q Pte manchay" | ATDR / SENAMHI (según texto del informe) | — | Serie de caudal medio mensual, estación Puente Manchay, 1964–2002 |
| F4 | `textofinal-lurin.doc` (texto del informe PROFODUA, "Informe Final, MOJ, Octubre 2004", PROFODUA/IRH/INRENA) | Consultor "MOJ" | Octubre 2004 | Descripción metodológica: origen de las series (medida/generada/completada), coordenadas de Manchay, fórmulas |
| F5 | `anexosfinal-lurin.doc` | Mismo estudio que F4 | Octubre 2004 | Solo aportó títulos de cuadros/gráficos; los cuadros numéricos de anexo (I.1 a I.16, persistencia, saltos) están como **imagen incrustada (WMF)**, no se pudieron extraer como texto en esta entrega |
| F6 | `INFORME_FINAL_LURIN.doc` (Ing. Cayo Leonidas Ramos Taipe, Mayo 2006, estudio de la Cuenca Alta) | Consultor independiente | Mayo 2006 | **No usado en esta entrega** — es un estudio distinto (otro alcance geográfico y otra metodología, basada en SIG/escorrentía). Pendiente de revisión si se solicita. |

No se mezclaron datos de F6 con F1–F4 para evitar combinar dos estudios con supuestos y periodos potencialmente distintos.

---

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `caudal_antapucro_m3s` | `caudal_antapucro_m3s` |
| `volumen_antapucro_mmc` | `volumen_antapucro_mmc` |
| `caudal_manchay_m3s` | `caudal_manchay_m3s` |
| `volumen_manchay_mmc` | `volumen_manchay_mmc` |

---

| Columna | Descripción | Unidad | Fuente | Fórmula / cálculo |
|---|---|---|---|---|
| `date` | Fecha del mes, día fijo = 01 | YYYY-MM-DD | — | — |
| `caudal_antapucro_m3s` | Caudal medio mensual, río Lurín, estación Antapucro (cabecera de valle) | m³/s | F1/F2 — **ver Sección IV: mayormente generado por modelo, no medido** | Medido (solo 1970–1971) / Generado (resto del periodo) mediante modelo Determinístico-Estocástico de Lutz Scholz, calibrado con la estación Manchay |
| `volumen_antapucro_mmc` | Volumen mensual equivalente al caudal de Antapucro | MMC (millones de m³) | Calculado | `V = Q_promedio_mensual (m³/s) × (n_días_del_mes × 86 400 s) / 10⁶`, redondeado a 2 decimales, con n_días real de cada mes/año (incluye años bisiestos) |
| `caudal_manchay_m3s` | Caudal medio mensual, río Lurín, estación Puente Manchay | m³/s | F3 — **ver Sección IV: parcialmente completado por correlación** | Medido (1972–2002 dentro de este rango) / Completado por correlación lineal con estación La Capilla, río Mala (periodo 1962–1971, que incluye 1964–1971 de este CSV) |
| `volumen_manchay_mmc` | Volumen mensual equivalente al caudal de Manchay | MMC | Calculado | Misma fórmula que `volumen_antapucro_mmc` |

**Verificación del cálculo de volumen:** Los valores de `volumen_antapucro_mmc` obtenidos con la fórmula anterior fueron contrastados contra la hoja "Vol Aforado" del archivo `Caudales_ANTAPUCRO.XLS` (que trae volúmenes ya calculados por la fuente original) — coinciden exactamente (ej. enero 1964: 5.233 m³/s × 31 días → 14.02 MMC calculado vs. 14.0161 MMC en la fuente, diferencia solo de redondeo).

---

## IV. QA/QC

### Origen real de los datos — ALERTA IMPORTANTE

Esta es la advertencia más importante de todo el dataset, documentada textualmente en `textofinal-lurin.doc`:

- **Antapucro:** la estación hidrométrica solo tiene **2 años de registro real: 1970–1971**. El resto de la serie 1964–2002 (37 de 39 años) es **generada mediante el modelo matemático Determinístico-Estocástico de Lutz Scholz** (balance hídrico + proceso markoviano), calibrado con los registros de la estación Manchay. El texto lo indica así: *"Puesto que se dispone de información hidrométrica únicamente de 02 años en la Estación Antapucro [...] fue necesario generar caudales medios mensuales mediante el modelo Determinístico – Estocástico de Lutz Scholz"*. Recomendación: para validación GRACE-FO, tratar esta columna como **serie modelada/sintética**, no como observación directa, y considerar usar `caudal_manchay_m3s` como referencia primaria si se requiere una serie más "observada".
- **Manchay:** el registro real cubre 1938–1961 y 1972–2003. El tramo **1962–1971 fue completado por correlación lineal simple** con la estación La Capilla (cuenca del río Mala, registro 1960–1992), usando el software MISSEL7 (Dr. José Salas, Colorado State University). Dentro del rango de este CSV (1964–2002), los años **1964 a 1971** corresponden a datos **completados**, no medidos directamente en Manchay.
- No fue posible identificar en la fuente disponible una tabla año-por-año que indique exactamente qué meses individuales fueron "generados" vs. "observados" dentro de esos rangos (los Cuadros I.2/I.3 del Anexo I que documentarían esto están como imagen, ver Sección II).

### Transformaciones aplicadas
- Cálculo de volumen mensual a partir de caudal medio mensual (fórmula estándar, días reales del mes, incluye bisiestos).
- Homogenización de encabezados de mes (Ene–Dic) a formato de fecha ISO.
- Sin relleno de valores faltantes propio de esta entrega (0 huecos detectados en el rango 1964–2002 para ambas estaciones).

### Valores atípicos (IQR por mes calendario)
Se calcularon cuartiles e IQR por mes calendario (no global) para cada columna de caudal. Se detectaron 24 valores fuera de rango intercuartílico (12 en Antapucro, 12 en Manchay), concentrados en:
- Febrero 1967 (caudal excepcionalmente alto en ambas estaciones: 30.9 y 32.5 m³/s — coincide en ambas series, consistente con un evento de avenida extrema real, no error de digitación).
- Meses de estiaje/transición (agosto, septiembre, octubre, noviembre, diciembre) en años específicos (1966, 1970, 1981, 1984, 1990, 1999, 2000, 2001, 2002).

**Interpretación:** dado que los picos coinciden entre ambas estaciones (misma cuenca, mismo evento hidrológico) y son consistentes con el régimen torrentoso de la costa peruana descrito en el informe (*"régimen de descargas irregulares y de carácter torrentoso"*), se interpretan como **extremos hidrológicos reales**, no errores. No se eliminó ni corrigió ningún valor.

### Consistencia caudal–volumen
Verificada: todos los volúmenes fueron derivados directamente del caudal reportado con la fórmula estándar; no hay incoherencias internas.

### Valores negativos
No se encontraron valores negativos en ninguna columna (0 casos).

### Continuidad temporal
Sin meses faltantes dentro del rango 1964-01 a 2002-12 para ninguna de las dos estaciones.

### Limitaciones conocidas
- La columna `caudal_antapucro_m3s` no debe interpretarse como observación directa fuera de 1970–1971 (ver arriba).
- La columna `caudal_manchay_m3s` incluye un tramo completado (1964–1971) por correlación con otra cuenca (río Mala).
- No se dispone de una fecha exacta de emisión de los archivos Excel (metadata del archivo indica última edición 2004–2006).
- El Anexo I (persistencia, análisis de salto/tendencia, cuadros de completación año por mes) no pudo auditarse porque está incrustado como imagen (WMF), no como tabla de texto.
- No se ha incorporado en esta entrega el estudio de 2006 de la Cuenca Alta (`INFORME_FINAL_LURIN.doc`), que podría tener series o periodos parcialmente distintos para puntos similares.

---

## V. Dominio espacial y coordenadas

| Estación | Fuente | Latitud | Longitud | Altitud | Observación |
|---|---|---|---|---|---|
| Puente Manchay | Texto del informe (`textofinal-lurin.doc`, párrafo citado dos veces, valor consistente) | 12°08' S | 76°49' W | 206 msnm | Única fuente de coordenadas de Manchay encontrada; consistente entre las dos citas del texto. |
| Antapucro | `Caudales_ANTAPUCRO.XLS`, hoja "Q Aforado" | (no da lat/lon, solo etiqueta "Latitud:", "Longitud:" vacías) | — | 2200 msnm | Cuenca declarada: LURIN |
| Antapucro | `Caudales_ANTAPUCRO.XLS`, hoja "Vol Aforado" (misma serie de datos, encabezado distinto) | 75°58' "S" | 13°27' "W" | 320 msnm | Estación declarada: "CONTA"; Cuenca declarada: ANTAPUCRO. Los valores de lat/lon están etiquetados con las letras cardinales cruzadas (S en la columna de longitud, W en la de latitud) y las magnitudes no corresponden a Perú tal como están escritas — **posible transposición de columnas** (si se interpretan como Lat 13°27'S / Lon 75°58'W, sí sería geográficamente plausible en el Perú andino, pero esto es una inferencia, no un dato confirmado). |

**No se promedia ni se elige una versión** — se reportan ambas conforme a la regla del proyecto. Se recomienda confirmar la ubicación real de Antapucro con el Anexo III (Plano N°03 "Ubicación de estaciones hidro-meteorológicas"), no incluido de forma legible en los archivos entregados (está como imagen dentro de `anexosfinal-lurin.doc`).

**Bounding box recomendado para extracción GRACE-FO Mascon** (margen 0.5° sobre las estaciones, usando la única coordenada confiable — Manchay — y un margen adicional generoso para cubrir Antapucro en cualquiera de sus dos hipótesis de ubicación):

- Usando solo Manchay (12°08'S, 76°49'W) ± 0.5°: **Lat -12.63 a -11.63, Lon -77.32 a -76.32**
- Si se usa la hipótesis de Antapucro transpuesta (13°27'S, 75°58'W) ± 0.5°, el bounding box combinado que cubre ambas estaciones sería aproximadamente: **Lat -13.95 a -11.63, Lon -77.32 a -75.47**

Se recomienda decidir el bounding box definitivo una vez confirmada la coordenada real de Antapucro.

---

*Elaborado conforme al protocolo del proyecto de auditoría y construcción de datasets hidrológicos — cuenca Lurín.*

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `lurin_caudales.csv` a `lurin_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `lurin_caudales_metadata.md` a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
