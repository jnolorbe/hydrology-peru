# Metadata — Caudal y Volumen mensual, Estación Puente Ocoña (Río Ocoña)

## I. Información general

- **Archivo de datos**: `ocona_caudal_volumen.csv`
- **Ámbito geográfico**: Cuenca del río Ocoña, punto de control Estación Puente Ocoña (SENAMHI).
- **Departamento / Provincia / Distrito**: Arequipa / Camaná / Ocoña.
- **Resolución temporal**: Mensual.
- **Periodo de registro**: 1965-09 a 2006-08 (41 años hidrológicos: 1965-66 a 2005-06).
- **Desfase respecto al año calendario**: La fuente presenta la serie en **año hidrológico Setiembre–Agosto** (p. ej. "Sep" del año hidrológico 1965-66 → `1965-09-01`; "Ene" del mismo año hidrológico → `1966-01-01`). Se verificó esta convención cruzando los meses de pico de caudal con eventos El Niño documentados (1972-73 y 1997-98, con máximos en Ene-Mar del año calendario siguiente al de la fila).
- **% de completitud**: 100% (492/492 meses, sin datos faltantes).
- **Advertencia importante sobre este dataset**: no es una transcripción literal del "Cuadro 6.3" de la fuente (ver Sección II) — es una **reconstrucción realizada en esta estandarización**, por decisión explícita del usuario, ante una discrepancia detectada en la fuente original (ver Sección IV.1).

## II. Fuentes de datos originales

| Fuente | Documento | Entidad / año | Qué aportó específicamente |
|---|---|---|---|
| Fuente A | `ESTUDIO_HIDROLOGICO_OCON_A.pdf` ("Evaluación de los Recursos Hídricos de la Cuenca del Río Ocoña" — Estudio Hidrológico, Informe Final), Cuadro 6.3 "Caudales medios mensuales para la cuenca del río Ocoña (calc.+obs.)", pág. 121 | INRENA — Intendencia de Recursos Hídricos — ATDR Ocoña-Pausa, enero 2007 | Serie reconstruida 1965-2005 (año hidrológico). **Usada en este dataset solo para el tramo 1965-1997** (33 años hidrológicos), etiquetado en la fuente como "calculado" (modelo GR2M, ver Fuente C). |
| Fuente B | Mismo PDF, Cuadro 5.3 "Caudales medios mensuales corregidos de la estación Puente Ocoña", pág. 114 | INRENA / SENAMHI, enero 2007 | Caudal medio mensual **aforado y corregido** en Puente Ocoña, 1998-2005. El informe corrigió tramos con registros incoherentes (Ene-Feb 1998 y Feb-Dic 2001) mediante correlación lineal con la estación Huatiapa (cuenca Camaná-Majes, R²=0.887). **Usada en este dataset para el tramo 1998-2005** (8 años hidrológicos), en lugar del valor que aparece impreso en el Cuadro 6.3 para esos mismos años (ver IV.1). |
| Fuente C (contexto, no incorporada directamente) | Mismo PDF, Cuadro 6.2 "Caudales medios mensuales calculados a partir del modelo GR2M para la estación Puente Ocoña", pág. 119 | INRENA, enero 2007 | Resultado del modelo lluvia-escorrentía GR2M (Mouelhi, 2003) calibrado contra el aforo de Puente Ocoña 1998-2005 (criterio de Nash=81%, balance=99.9%). No se incorpora como fuente de valores en este CSV; se usó solo para diagnosticar la discrepancia de IV.1. |

**Discrepancia detectada en la fuente (reportada, no resuelta unilateralmente por el equipo de estandarización):**
El texto del informe (pág. 120) afirma: *"hemos decidido usar los caudales de la serie construida para los años 1965-1997 y para el periodo 1998-2005 la serie de caudales observados"*, y la nota al pie del Cuadro 6.3 dice *"Azul=Caudales calculados; Rojo=Caudales observados"*. Sin embargo, al extraer el texto exacto del PDF (no por lectura visual) se comprobó que los valores impresos en el Cuadro 6.3 para 1998-2005 son **numéricamente idénticos** a los del Cuadro 6.2 (el resultado del modelo GR2M), y **no** coinciden con los del Cuadro 5.3 (el aforo corregido) — p. ej., para 2003, Cuadro 6.3 trae Ene=113.6 m³/s (igual a Cuadro 6.2), mientras que Cuadro 5.3 trae Ene=130.1 m³/s para el mismo mes. Es decir, el Cuadro 6.3 tal como está impreso **no hace lo que el propio texto dice que hace**. Esta discrepancia fue presentada al usuario, quien decidió (chat, 15-set-2026) que este dataset se construyera **según lo que el texto narra** (empalmando 1965-1997 del Cuadro 6.3 con 1998-2005 del Cuadro 5.3), y no replicando el Cuadro 6.3 tal cual aparece impreso. Por lo tanto, **este CSV difiere del Cuadro 6.3 publicado en los años 1998-2005.**

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Q m3/s` (Cuadro 6.3 / Cuadro 5.3) | `caudal_puenteocona_m3s` |
| *(no existe en la fuente para este punto)* | `volumen_puenteocona_mmc` |
| *(construida en esta estandarización)* | `tipo_dato_caudal` |

---

| Columna | Descripción | Unidad | Fuente | Fórmula |
|---|---|---|---|---|
| `date` | Fecha del mes, día fijado en 01 | YYYY-MM-DD | — | Reconstruida desde el año hidrológico Sep-Ago declarado en la fuente |
| `caudal_puenteocona_m3s` | Caudal medio mensual en la Estación Puente Ocoña | m³/s | 1965-09 a 1997-08: calculado (modelo GR2M, Cuadro 6.3); 1998-09 a 2005-08 (fila hidrológica 1998-2005): observado/aforado y corregido (Cuadro 5.3) | — |
| `volumen_puenteocona_mmc` | Volumen mensual | MMC (millones de m³) | Calculado (en esta estandarización) | `V = Q (m³/s) × (n_días_del_mes × 86,400 s) / 10⁶`, con días reales del mes/año (considera años bisiestos), redondeado a 2 decimales |
| `tipo_dato_caudal` | Origen del valor de caudal de esa fila | categórica: `calculado_gr2m` / `observado_corregido` | Documentación de procedencia | — |

## IV. QA/QC

1. **Discrepancia Cuadro 6.3 vs. 6.2 vs. 5.3**: descrita en la Sección II. Se reportó al usuario en vez de resolverla por criterio propio; la decisión tomada (reconstruir según el texto, usando 5.3 para el tramo observado) queda documentada en la columna `tipo_dato_caudal` mes a mes, de modo que quien use este dataset pueda revertir a la versión "tal como fue impresa" si lo prefiere (bastaría con sustituir las filas `observado_corregido` por los valores del Cuadro 6.2/6.3 impreso).
2. **Naturaleza mixta de la serie**: 396 de 492 meses (1965-09 a 1997-08) son **calculados** por el modelo GR2M — no existe registro aforado alternativo para ese tramo con el cual contrastarlos, más allá de la propia calibración del modelo contra 1998-2005 (Nash=81%, balance=99.9%, R²=0.81 entre observado y calculado en el año promedio, según el informe). Los restantes 96 meses (1998-09 a 2005-08) sí son aforo real corregido.
3. **Corrección de la fuente en el tramo observado**: el informe indica que corrigió los registros de Puente Ocoña de Ene-Feb 1998 y Feb-Dic 2001 (identificados como "incoherentes" frente a la precipitación y frente al caudal de la estación vecina Huatiapa) mediante una regresión lineal Huatiapa→Puente Ocoña (y=1.3546x+20.637, R²=0.887). Esta corrección ya viene aplicada en el Cuadro 5.3 usado aquí; no se aplicó ninguna corrección adicional en esta estandarización.
4. **Continuidad temporal**: sin meses faltantes en 1965-09 a 2006-08 (492/492).
5. **Valores extremos**: los máximos de la serie coinciden con eventos El Niño documentados en la costa peruana — p. ej. Feb-1973 (hidrológico 1972) = 710.5 m³/s (calculado) y Feb-1999 (hidrológico 1998) = 683.0 m³/s (observado corregido). Se interpretan como extremos hidrológicos reales, no como errores; no se han modificado.
6. **Volumen**: siempre calculado (nunca medido en la fuente para este punto); fórmula documentada en la Sección III, con manejo explícito de años bisiestos (verificado p. ej. en feb-1996, feb-2000 y feb-2004, todos con 29 días).
7. **Efecto de la reconstrucción sobre la climatología**: al reemplazar el tramo 1998-2005 "calculado" (Cuadro 6.3 impreso) por el "observado corregido" (Cuadro 5.3), la media climatológica mensual resultante de este dataset difiere levemente de la media publicada en el Cuadro 6.3 original — la diferencia más notoria es en enero (183.7 m³/s publicado vs. ~173.5 m³/s en este dataset) y en diciembre (56.6 vs. ~59.1 m³/s). Esto es un efecto esperado de la reconstrucción, no un error.

## V. Dominio espacial y coordenadas

| Estación | Latitud | Longitud | Altitud | Área de cuenca | Fuente |
|---|---|---|---|---|---|
| Puente Ocoña | 16.42° S | 73.10° W | 23 msnm | 15,998.12 km² (hasta esta estación, Cuadro 5.1) | PDF 2007, Cuadros 1.3/5.1/5.2 |

- **Coordenadas decimales (WGS84)**: -16.420, -73.100 (ya reportadas en decimal por la fuente).
- Nota: el informe 2004 (PROFODUA) reporta para el mismo punto un área de cuenca ligeramente distinta (15,984.08 km² "hasta el Puente Ocoña"); ambas cifras se reportan como referencia, sin resolver cuál es más precisa.
- **Bounding box recomendado para extracción GRACE-FO Mascon** (margen 0.5° sobre la estación):
  - Lat: -16.92° a -15.92°
  - Lon: -73.60° a -72.60°

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Datos numéricos extraídos con `pdftotext -layout` (texto vectorial real del PDF, no OCR ni lectura visual) de las páginas que contienen el Cuadro 5.3 (pág. 114) y el Cuadro 6.3 (pág. 121) de `ESTUDIO_HIDROLOGICO_OCON_A.pdf`.
- Se generó `volumen_puenteocona_mmc` con la fórmula estándar del proyecto (ver Sección III), calculada en Python con `calendar.monthrange` para manejar correctamente los años bisiestos.
- Se añadió la columna `tipo_dato_caudal` para dejar explícito, mes a mes, el origen del valor de caudal.
- **Decisión tomada junto al usuario** (chat, 15-set-2026): ante la discrepancia de la Sección II/IV.1, se optó por reconstruir la serie tal como la describe el texto del informe (empalmando Cuadro 6.3 para 1965-1997 con Cuadro 5.3 para 1998-2005), en lugar de transcribir literalmente el Cuadro 6.3 impreso.
- Nombre de archivo y columnas normalizados a la convención `<ambito>_<categoria>.csv` / `<variable>_<estacion>_<unidad>`.
