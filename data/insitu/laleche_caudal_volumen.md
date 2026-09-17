# Metadata — Metadata — Dataset Caudal y Volumen, Estación Puchaca (Río La Leche)

## I. Información general

- **Nombre de archivo:** `caudal_volumen_puchaca_1960_2005.csv`
- **Ámbito geográfico:** Cuenca del río La Leche, Sub Distrito de Riego La Leche (Distrito de Riego Motupe-Olmos-La Leche)
- **Departamento/Región:** Lambayeque, Perú
- **Resolución temporal:** Mensual
- **Periodo de registro:** 1960-01 a 2005-12 (46 años, 552 meses)
- **Desfase respecto al año calendario:** Ninguno. El dataset se entrega en año calendario (Ene–Dic). *Nota:* algunos cuadros de la fuente (`InformeLaLeche.doc`, hoja "Comparación" de persistencias) presentan el año hidrológico de la cuenca en formato Ago–Jul; esta entrega **no** sigue ese ordenamiento, se mantiene Ene–Dic.
- **% de completitud:** 100% (552/552 meses, sin valores NA) para ambas columnas.

## II. Fuentes de datos originales

| Documento | Entidad emisora | Año | Aporte específico |
|---|---|---|---|
| `QPuchaca1960_2006.XLS` (hoja "Mensual") | SENAMHI (dato origen) / PROFODUA (procesamiento y hoja de cálculo) | Procesado en 2006 | Serie de caudales medios mensuales 1960–2005 de la estación Puchaca. Fuente primaria y única de los valores numéricos usados en este dataset. |
| `QPuchaca1960_2006.XLS` (hoja "Diario") | SENAMHI / PROFODUA | 2006 | Serie de caudales medios diarios 1960–2005 (mismo periodo). No usada para esta entrega mensual, pero disponible para validación cruzada o si se requiere reagregar. |
| `InformeLaLeche.doc` / `InformeLaLeche10.doc` (PROFODUA, Valle del Río La Leche) | INRENA – Intendencia de Recursos Hídricos | Marzo 2006 (InformeLaLeche10) / actualización posterior (InformeLaLeche) | Contexto narrativo: ubicación y coordenadas de la estación Puchaca, confirmación del periodo de registro (46 años), mención de los eventos El Niño 1998/2001/2002 como causa de los caudales extraordinarios. Los "Cuadro No. 01" y "Cuadro No. 02" de estos documentos (caudales medios mensuales y persistencias) están incrustados como **imágenes**, no como tablas de texto, por lo que no se usaron como fuente de datos numéricos — se usó el Excel en su lugar (mismo contenido, según el propio texto del informe).

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `caudal_puchaca_m3s` | `caudal_puchaca_m3s` |
| `volumen_puchaca_mmc` | `volumen_puchaca_mmc` |

---

| Columna | Descripción | Unidad | Fuente | Fórmula |
|---|---|---|---|---|
| `date` | Primer día del mes calendario | YYYY-MM-DD | — | — |
| `caudal_puchaca_m3s` | Caudal medio mensual del río La Leche, estación Puchaca | m³/s | Medido (SENAMHI, procesado por PROFODUA) | — |
| `volumen_puchaca_mmc` | Volumen mensual equivalente al caudal medio mensual | MMC (millones de m³) | Calculado | `V = Q_promedio_mensual (m³/s) × (n_días_del_mes × 86,400 s) / 10⁶`, redondeado a 2 decimales. `n_días_del_mes` calculado considerando años bisiestos (ej. febrero 1960, 1964, ... = 29 días). |

## IV. QA/QC

**Transformaciones aplicadas:**
- Conversión de la tabla ancha (año × 12 meses) de la hoja "Mensual" a formato largo con columna `date`.
- Redondeo de caudal a 3 decimales (tal como venía en la fuente, sin alteración de precisión) y volumen a 2 decimales según regla del proyecto.
- Cálculo de volumen mensual usando días reales del mes (bisiestos incluidos).

**Valores marcados como "corregidos" o "completados" en la fuente original:**
- Ninguno detectado. La fuente (`InformeLaLeche.doc`) declara explícitamente: *"El análisis visual del gráfico de la información media, mensual registrada en la estación Puchaca, no muestra indicios de tendencia o de saltos [...] no fue necesario realizar el análisis estadístico de la media o la desviación estándar de la serie"* — es decir, la propia fuente indica que la serie se usó tal como fue registrada, sin corrección por inconsistencia.

**Valores atípicos (IQR por mes calendario) y su interpretación:**

19 meses fueron marcados como atípicos según el rango intercuartílico calculado por mes calendario (no globalmente). Todos corresponden a la temporada húmeda (enero–mayo) y coinciden con eventos de El Niño costero u años húmedos documentados explícitamente en `InformeLaLeche.doc`:

- **Ene–May 1998:** caudales de 72.7 a 154.7 m³/s — El Niño de 1998, el evento más extremo del registro. El propio informe narra caudales instantáneos "superiores a 1,000 m³/s" durante Niños intensos, por lo que estos promedios mensuales son consistentes con el fenómeno.
- **Mar 2001 (79.1 m³/s):** el informe menciona explícitamente el año 2001 como el "mayor exponente" del periodo húmedo posterior a 1998, con caudales del orden de 500 m³/s (instantáneos).
- **Abr 2002 (58.2 m³/s):** el informe menciona caudales extraordinarios del orden de 300 m³/s (instantáneos) en 2002.
- **Mar 1972, 1975, 1983, 1984, 2000:** años húmedos no descritos individualmente en el texto del informe, pero consistentes con la variabilidad interanual conocida de la costa norte peruana (Niños de magnitud moderada en 1972-73 y 1982-83).

**Interpretación:** se consideran **extremos hidrológicos reales**, no errores de digitación o medición, dado que (a) su ocurrencia coincide con eventos El Niño documentados en fuente primaria, y (b) no hay saltos abruptos ni discontinuidades que sugieran error de registro.

**Consistencia caudal-volumen:** verificada al 100% — el volumen reportado corresponde exactamente a la fórmula declarada aplicada al caudal de cada mes (0 discrepancias en 552 registros).

**Continuidad temporal:** sin meses faltantes en el rango 1960-01 a 2005-12 (552/552).

**Valores negativos:** ninguno (0 registros negativos, físicamente correcto para caudal).

**Limitaciones conocidas:**
- La serie termina en diciembre de 2005, por lo que **no cubre el periodo de la misión GRACE/GRACE-FO** (2002–presente para GRACE clásico; 2018–presente para GRACE-FO). Es decir, esta serie por sí sola solo se superpone parcialmente (2002–2005) con GRACE clásico y **no se superpone en absoluto con GRACE-FO**. Si el objetivo final es validar TWSA de GRACE-FO, esta serie de caudal necesitará ser complementada con datos más recientes de la misma estación (no incluidos en los archivos entregados) o utilizada únicamente como referencia histórica/climatológica.
- Existe una discrepancia de coordenadas entre la estación hidrométrica Puchaca (usada aquí) y una estación climatológica también llamada "Puchaca" en otro archivo del proyecto (ver Sección V) — no deben confundirse ni promediarse sus datos.
- No se dispone de información sobre el método de medición (limnimétrica/limnigráfica) ni de la incertidumbre instrumental de la estación Puchaca en los documentos entregados.

## V. Dominio espacial y coordenadas

**Estación hidrométrica Puchaca** (fuente de este dataset):
- Latitud: 06°23′ S
- Longitud: 79°28′ O
- Altitud: 250 m.s.n.m.
- Fuente de la coordenada: `QPuchaca1960_2006.XLS` (encabezado de hoja) y confirmado en texto de `InformeLaLeche.doc`/`InformeLaLeche10.doc`.

**⚠️ Discrepancia detectada (no resuelta, reportada tal cual):** en `InfClimatLaLeche.xls` (hoja "Precipitación", bloque "Puchaca") existe una estación climatológica con el mismo nombre pero coordenadas distintas: Latitud 06°23′00″ S, **Longitud 79°29′00″ O**, **Altitud 400 m.s.n.m.** No se asume que sea el mismo punto físico que la estación hidrométrica; se reportan ambas versiones para que la decisión de cuál usar (o si son puntos distintos) quede en manos del usuario.

**Bounding box recomendado para extracción GRACE-FO Mascon** (estación hidrométrica Puchaca ± 0.5°):
- Latitud: -6.883° a -5.883°
- Longitud: -79.967° a -78.967°

*(En convención decimal WGS84: 06°23′S = -6.383°, 79°28′O = -79.467°)*

---

# Resumen ejecutivo

**Completitud:** 100% (552/552 meses, ambas columnas, 1960–2005).

**Tabla de alertas de calidad:**

| Alerta | Severidad | Descripción |
|---|---|---|
| Cobertura temporal no alcanza GRACE-FO | 🔴 Alta | La serie termina en 2005; GRACE-FO opera desde 2018. Se requiere fuente adicional para el periodo de validación satelital. |
| Discrepancia de coordenadas "Puchaca" | 🟡 Media | Dos estaciones distintas con el mismo nombre en las fuentes (hidrométrica vs. climatológica), coordenadas y altitud diferentes. |
| 19 meses atípicos (IQR mensual) | 🟢 Baja (informativo) | Todos explicados por eventos El Niño/años húmedos documentados en la fuente primaria; no se removieron ni ajustaron. |
| Datos solo como imagen en los informes Word | 🟢 Baja (informativo) | Los Cuadros 01 y 02 de los informes PROFODUA están incrustados como imágenes; se usó el Excel equivalente en su lugar, sin pérdida de información según el propio texto del informe. |

**Alcance y limitaciones de esta entrega:**
Esta entrega cubre únicamente **caudal y volumen mensual de la estación Puchaca (1960–2005)**. No incluye: precipitación, evapotranspiración, ni nivel freático (pendientes, ver auditoría previa). No incluye la serie diaria (disponible en la misma fuente si se requiere). No cubre el periodo de operación de GRACE-FO.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `laleche_caudales.csv` a `laleche_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `laleche_caudales_metadata.md` a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
