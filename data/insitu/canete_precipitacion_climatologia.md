# Metadata — Climatología Multianual "Completa y Consistente" de Precipitación, 6 Estaciones (Cuenca del Río Cañete)

## I. Información general

- **Archivo de datos:** `canete_precipitacion_climatologia.csv`
- **Ámbito geográfico:** Cuenca del río Cañete, Departamento de Lima, Perú (estaciones pluviométricas de cabecera de cuenca).
- **Resolución temporal:** Climatología multianual (formato ancho: una fila por estación, columnas `ene_mm`...`dic_mm` + `total_anual_mm`), no una serie temporal fechada.
- **Periodo base:** 1964-1965 a 2004-2005 (41 años hidrológicos), mismo periodo que `canete_precipitacion.csv` (serie mensual, 6 estaciones).
- **Naturaleza del dato — importante:** este archivo corresponde al **Cuadro N°1.7 ("Precipitación total mensual, completa y consistente, periodo 1964-2005")** del documento fuente, **no** a un promedio simple recalculado a partir de la serie cruda. Ver Sección IV para la verificación de esto y sus implicancias.

## II. Fuentes de datos originales

| Fuente | Documento | Aportó |
|---|---|---|
| Cuadro N°1.7 | `INFORME_FINAL_CAÑETE.doc` (PROFODUA / ATDR Cañete, 2006) | Ciclo anual "completo y consistente" (ya corregido/homogeneizado) por estación, para las mismas 6 estaciones de `canete_precipitacion.csv`. |
| Cuadro N°1.4.1 | `ESTUDIO_HIDROLOGICO_CAÑETE.pdf` (2004) | Ficha catastral de 20 estaciones hidrometeorológicas de la cuenca (tipo, altitud, coordenadas con segundos, operador, periodo declarado) — usada para completar la Sección V. |

- **Complementa a:** `metadata_precipitacion_canete.md` (= `cañete_metadata_precipitacion.md` en `DATA_INSITU`, base de la serie mensual `canete_precipitacion.csv`). Este dataset fue investigado como un intento de *ampliar* esa serie mensual con más estaciones o años a partir del PDF; el resultado de esa investigación (documentado íntegramente aquí) es que **no fue posible ampliar la serie**, pero sí se obtuvo información valiosa de validación cruzada y de catastro de estaciones.
- **Intento de ampliación fallido — Anexo 4.0 del PDF vacío:** se intentó extraer las tablas y gráficos de precipitación del PDF (Anexo 4.0, Cuadros 4.1–4.16, pág. ~76–129) con `pypdf` y `pdfplumber`, y también se renderizaron páginas como imagen para inspección visual (ej. pág. 81 y 105). **Las páginas están literalmente en blanco** (solo encabezado/pie institucional), lo que indica que las figuras y cuadros numéricos originales no se conservaron en la conversión a PDF del documento fuente. No se extrajo ni se estimó ningún valor adicional a partir de esas páginas.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `estacion` | `estacion` |
| `altitud_msnm` | `altitud_msnm` |
| `ene_mm` ... `dic_mm` | `ene_mm` ... `dic_mm` |
| `total_anual_mm` | `total_anual_mm` |

| Columna | Unidad | Descripción |
|---|---|---|
| `estacion` | - | Nombre de la estación pluviométrica (Vilca, Huangáscar, Carania, Tanta, Yauyos, Yauricocha) |
| `altitud_msnm` | msnm | Altitud de la estación |
| `ene_mm` ... `dic_mm` | mm | Precipitación mensual del ciclo anual "completo y consistente" (Cuadro N°1.7), mes calendario |
| `total_anual_mm` | mm | Suma anual del ciclo, tal como reportada en el Cuadro N°1.7 |

## IV. QA/QC

- **Validación cruzada realizada (hallazgo principal de esta investigación):** se comparó el promedio anual multianual (1964-65 a 2004-05) calculado a partir de la serie mensual ya entregada en `canete_precipitacion.csv`, contra los totales anuales de este Cuadro N°1.7:

| Estación | Media anual calculada desde la serie mensual (mm) | Cuadro N°1.7 = este archivo (mm) | Diferencia |
|---|---|---|---|
| Yauyos | 286.8 | 285.7 | +0.4% |
| Tanta | 1006.9 | 1006.9 | 0.0% |
| Carania | 663.9 | 663.9 | 0.0% |
| Huangáscar | 263.7 | 263.7 | 0.0% |
| Vilca | 779.4 | 779.4 | 0.0% |
| Yauricocha | 992.3 | 993.4 | -0.1% |

  **Conclusión:** la serie mensual ya entregada (`canete_precipitacion.csv`) coincide casi exactamente con este ciclo "completo y consistente". Esto implica que la serie mensual entregada **ya incorpora las correcciones por saltos/discontinuidades** descritas abajo, es decir, **no es la serie cruda original sino la versión ya homogeneizada** por el consultor (software SIH/HEC4).

- **Correcciones de consistencia aplicadas por el consultor en la fuente (documentadas explícitamente, no realizadas por este proyecto), pág. 91-92 del PDF:**
  - Yauyos: periodo inconsistente 1964–1973; consistente 1974–2000. Salto en media y desviación estándar.
  - Tanta: periodo inconsistente 1978–1992; consistente 1964–1977. Salto en media y desviación estándar.
  - Carania: periodo inconsistente 1976–1995; consistente 1964–1975. Salto en media y desviación estándar; no se consideraron los datos de 1986-1989, por muy inconsistentes.
  - Huantán: no se consideran los datos de 1981–1989 (estación sin serie mensual entregada — ver Sección V).
  - Vilca: presenta salto en la desviación estándar, pero no significativo; no se corrigió.
- **Magnitud de la corrección/completación** (pág. 115 del PDF), comparando serie histórica original vs. serie consistente y completada: Huantán = 41.0% | Yauyos = 22.6% | Tanta = 19.6% | Carania = 18.9% | Vilca = 14.8%.
- **Implicancia para el usuario:** los valores de Yauyos (años 1964-1973), Tanta (1978-1992) y Carania (1976-1995, excluyendo 1986-1989) en `canete_precipitacion.csv` **son valores corregidos/ajustados por análisis de saltos y tendencias, no mediciones crudas de esos periodos**. Vilca no requirió corrección significativa. Huangáscar y Yauricocha no fueron mencionadas en el listado de saltos, por lo que se asume que su serie es la original sin ajuste (no confirmado explícitamente en el texto fuente).
- **Discrepancia de periodo operativo no resuelta:** el PDF (2004) declara periodo operativo SENAMHI "Ene/1964 – Dic/2000" para las 6 estaciones; el `.doc` (2006) reporta datos hasta jul-2005. No se pudo determinar si la extensión 2000→2005 proviene de otra fuente o de una reconstrucción. Se reporta, no se resuelve.
- **Typo detectado en la fuente:** el Cuadro N°1.7 tiene un error tipográfico en el nombre de la estación Carania (aparece como "Catania" en el documento original); se usó "Carania" en este archivo, consistente con el resto del dataset.
- No se aplicó relleno, interpolación ni corrección adicional en esta fase; los valores se transcribieron tal cual del Cuadro N°1.7.

## V. Dominio espacial y coordenadas

**Catálogo completo de 20 estaciones hidrometeorológicas de la cuenca (Cuadro N°1.4.1 del PDF)** — incluye tanto las 6 con serie mensual entregada como 14 adicionales sin serie disponible en las fuentes subidas:

| Estación | Tipo | Altitud (msnm) | Latitud | Longitud | Operador | Periodo declarado | ¿Serie disponible? |
|---|---|---|---|---|---|---|---|
| Imperial | HM | 250 | 13°02' | 76°11' | SENAMHI | Ene/1926–Abr/1968 | No |
| Socsi | HM/LM | 350 | 13°00' | 76°10' | SENAMHI | Ene/1965–Dic/2000 | Sí (caudal/volumen, `canete_caudal_volumen.csv`) |
| Chavín | HM/LG | 1414 | 12°43' | 75°56' | ELECTROPERÚ | Jun/1986–Dic/1997 | No |
| Tinco | HM/LG | 3150 | 12°17' | 75°48' | ELECTROPERÚ | Feb/1986–Dic/1997 | No |
| Aguas Calientes | HM/LG | 4180 | 12°05' | 75°67'* | ELECTROPERÚ | Jul/1986–Dic/1997 | No |
| Tanta (HM/LM) | HM/LM | 4275 | 12°07' | 76°00' | ELECTROPERÚ | Jul/1986–Dic/1997 | No (estación hidrométrica, distinta de la pluviométrica homónima) |
| Tanta (PLU) | PLU | 4505 | 12°07'48" | 76°01'00" | SENAMHI | Ene/1964–Dic/2000 | **Sí** |
| Carania | PLU | 3825 | 12°21'00" | 75°52'10" | SENAMHI | Ene/1964–Dic/2000 | **Sí** |
| Vilca | PLU | 3816 | 12°07'00" | 75°50'00" | SENAMHI | Ene/1964–Dic/2000 | **Sí** |
| Huangáscar | PLU | 2556 | 12°54'10" | 75°50'00" | SENAMHI | Ene/1965–Dic/2000 | **Sí** |
| Yauyos | PE | 2290 | 12°24'30" | 75°54'35" | SENAMHI | Ene/1964–Dic/2000 | **Sí** (ver discrepancia de coordenadas abajo) |
| Huantán | PLU (desactivada) | 3272 | 12°27'48" | 75°49'00" | SENAMHI | Ene/1964–Dic/1989 | No |
| Colonia | PLU (paralizada) | 3379 | 12°38'05" | 75°53'40" | SENAMHI | Ene/1964–Dic/1987 | No |
| Cañete | CO | 150 | 13°04'00" | 76°21'30" | SENAMHI | Abr/1936–Dic/2000 | No |
| Pacarán | CAO | 710 | 12°52'20" | 76°03'20" | SENAMHI | Ene/1964–Dic/1968 | No (solo temperatura/evaporación 1995-2000, fuera de alcance) |
| Yauricocha | PLU | 4522 | 12°19'00" | 75°43'00" | SENAMHI | Ene/1943–Dic/2000 | **Sí** |
| Siria | PLU (desactivada) | 3680 | 12°14'10" | 75°44'07" | SENAMHI | Ene/1947–1968 | No |
| Sunca | PLU (desactivada) | 3845 | 12°16'30" | 75°42'10" | SENAMHI | Ene/1945–1968 | No |
| Catahuasi | PLU (desactivada) | 1369 | 12°48'00" | 75°53'30" | SENAMHI | Ene/1964–1968 | No |

*(el valor "75°67'" para Aguas Calientes aparece así literalmente en el PDF fuente; 67' no es válido en notación sexagesimal, probablemente error tipográfico del documento original — se reporta tal cual, sin corregir.)*

- **Estaciones sin serie mensual disponible en ninguna fuente subida:** Imperial, Chavín, Tinco, Aguas Calientes, Tanta (HM/LM), Huantán, Colonia, Cañete, Pacarán (precipitación), Siria, Sunca, Catahuasi (12 estaciones). Sus coordenadas quedan en la tabla anterior por si se consigue su serie en otra fuente; no se estimó ningún valor para ellas.
- **Discrepancias de coordenadas detectadas entre el `.doc` (grados-minutos, usado en `canete_precipitacion.md`) y el PDF (Cuadro 1.4.1, con segundos) — no resueltas, reportadas para decisión del usuario:**

| Estación | Coord. `.doc` | Coord. PDF (con segundos) | Diferencia aprox. |
|---|---|---|---|
| Yauyos | 12°27' S, 75°55' W | 12°24'30" S, 75°54'35" W | **~4.6 km en latitud** (la más relevante) |
| Vilca | 12°07' S, 75°49' W | 12°07'00" S, 75°50'00" W | ~1.8 km en longitud |
| Tanta | 12°08' S, 76°01' W | 12°07'48" S, 76°01'00" W | ~0.4 km (redondeo, no relevante) |
| Carania | 12°21' S, 75°52' W | 12°21'00" S, 75°52'10" W | ~0.3 km (redondeo, no relevante) |
| Huangáscar | 12°54' S, 75°50' W | 12°54'10" S, 75°50'00" W | ~0.3 km (redondeo, no relevante) |
| Yauricocha | 12°19' S, 75°43' W | 12°19'00" S, 75°43'00" W | Sin diferencia |

  La discrepancia de Yauyos (~4.6 km) es la única con magnitud suficiente para afectar el bounding box de extracción GRACE-FO si se usa esa estación como referencia puntual. No se ha asumido cuál de las dos coordenadas es correcta.
- Para el bounding box recomendado de extracción GRACE-FO Mascon y las coordenadas decimales de las 6 estaciones con serie, ver `canete_precipitacion.md` (Sección V).

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Renombrado desde `cañete_precipitacion_climatologia.csv` a `canete_precipitacion_climatologia.csv`; nombres de columna ya estaban en snake_case (sin cambios).
- Metadata completamente reescrita a partir de `cañete_precipitacion_climatologia.md` original en `DATA_INSITU`, el cual es en realidad un **"Addendum de metadata"** (informe de investigación de QA/QC) y no seguía la plantilla de secciones I-VI esperada — de ahí que la generación automática por lotes produjera varias secciones "no documentado"; esta versión fue redactada a mano para incorporar la totalidad de su contenido.
- Se verificó, mediante los valores exactos del CSV, que este archivo corresponde al Cuadro N°1.7 ("completa y consistente") citado en el Addendum, y no a un recálculo independiente — ver Sección IV para la validación cruzada completa.
- No se generó ningún archivo adicional: el Addendum original mencionaba un archivo nuevo `precipitacion_climatologia_referencia_canete.csv`, que corresponde exactamente a este dataset (mismos valores) entregado bajo el nombre `cañete_precipitacion_climatologia.csv` — no hay un archivo separado que integrar.
