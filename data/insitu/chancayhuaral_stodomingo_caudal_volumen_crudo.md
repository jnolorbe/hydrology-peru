# Metadata — Metadata — Caudal y Volumen mensual, Estación Santo Domingo (Cuenca Chancay-Huaral)

## I. Información general

- **Nombre de archivo del dataset:** `caudal_volumen_santodomingo_1922_1999.csv`
- **Ámbito geográfico:** Cuenca del río Chancay-Huaral, hasta la Estación Hidrométrica Santo Domingo (Subcuenca Media, aguas abajo de la confluencia de los ríos Vichaycocha y Baños).
- **Departamento / Región:** Lima, Perú (provincias de Huaral y Canta).
- **Resolución temporal:** mensual.
- **Periodo de registro:** 1922-01 a 1999-12 (78 años, 936 meses).
- **Desfase respecto al año calendario:** ninguno; el año hidrológico usado en la fuente coincide con el año calendario (Ene-Dic).
- **% de completitud:** 99.04% (9 de 936 meses faltantes = 0.96%). Ver detalle de meses faltantes en la sección IV.
- **Versión de la serie:** esta es la serie **histórica sin homogenizar/completar** ("Caudales Históricos de la Estación Hidrométrica Santo Domingo"), tal como aparece en la hoja `Q Med_H Sto Dom` del archivo fuente. **No confundir con la versión "Homogenizada y Completada" (H&C), disponible en la misma fuente para el subperiodo 1960–1999**, que no se construyó en esta entrega (ver Alcance/Limitaciones en el resumen ejecutivo).

## II. Fuentes de datos originales

| Fuente | Entidad / Autor | Año | Qué aportó específicamente |
|---|---|---|---|
| `2_0_Oferta_Hidrica-Balance-Asignacion.xls`, hoja `Q Med_H Sto Dom` | Water & Land (consultora), en el marco del Programa de Formalización de Derechos de Uso de Agua (PROFODUA) — INRENA / Intendencia de Recursos Hídricos | Archivo con última modificación registrada 2006 | Serie mensual de caudales históricos (m³/s) de la Estación Santo Domingo, 1922–2000 (fila 2000 vacía, excluida — ver notas técnicas). |
| `ESTUDIO_HIDROLOGICO_CHANCAY-HUARAL.pdf` — "Evaluación y Ordenamiento de los Recursos Hídricos de la Cuenca Chancay-Huaral" | Autor: jchunga (documento origen "EstudioHidrolo.DOC"); estudio técnico de referencia para la cuenca | Documento generado en PDF en 2008 (estudio con datos y metodología de años anteriores) | Metodología de análisis (doble masa, histogramas, tendencias) y de completación/extensión de caudales; explicación de que los caudales de Santo Domingo **no representan régimen natural** por regulación de lagunas aguas arriba (ver Notas Técnicas); superficie de cuenca hasta Santo Domingo (1850.31 km², con discrepancia respecto al Excel — ver sección V). |

**Nota:** no se usaron para este dataset los archivos `1_1_Precipitacion.xls` (solo climatología, sin dimensión de año) ni `4_0_Informe_No_02...Anexo.doc` (demanda de agua por cultivo, tablas incrustadas no legibles como texto). El archivo `1_0_Precipitacion.xls`, referenciado en las instrucciones del proyecto, no fue recibido en esta entrega.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `caudal_santodomingo_m3s` | `caudal_santodomingo_m3s` |
| `volumen_santodomingo_mmc` | `volumen_santodomingo_mmc` |

---

| Columna | Descripción | Unidad | Fuente | Fórmula |
|---|---|---|---|---|
| `date` | Primer día del mes calendario | YYYY-MM-DD | — | — |
| `caudal_santodomingo_m3s` | Caudal medio mensual histórico registrado en la Estación Santo Domingo | m³/s | Medido (según hoja fuente `Q Med_H Sto Dom`) | — |
| `volumen_santodomingo_mmc` | Volumen mensual equivalente | MMC (millones de m³) | Calculado | `V = Q_promedio_mensual (m³/s) × (n_días_del_mes × 86400 s) / 10⁶`, redondeado a 2 decimales. `n_días_del_mes` considera años bisiestos (28/29 días en febrero). |

## IV. QA/QC

**Transformaciones aplicadas:**
- Se excluyó la fila del año 2000 presente en la hoja fuente porque estaba completamente vacía (sin valores en ningún mes); el propio documento fuente declara el período como "1922–1999" en su encabezado ("PERIODO: 1922 1999"), consistente con esta exclusión.
- El volumen se calculó únicamente a partir del caudal medio mensual reportado; no se aplicó ningún ajuste o corrección adicional.

**Valores marcados/corregidos/completados en la fuente:**
- Esta serie corresponde a la versión **histórica**, es decir, **sin** el proceso de homogenización y completación que sí se aplicó a la serie "H&C" (hoja `Q Med_H&C Sto Dom`, no incluida en este dataset). Por lo tanto, los 9 valores faltantes de esta serie **no fueron completados** — se mantienen como `NA`, fieles a la fuente.
- El estudio hidrológico (PDF, sección 6.4) documenta el método usado para producir la versión H&C (no aplicado aquí): completación manual a nivel mensual cuando los datos diarios faltantes no superaban 3 días, y completación por correlación múltiple con el software HEC4 (Cuerpo de Ingenieros del Ejército de EE.UU.) para el grupo de estaciones Santo Domingo, Pte. Alco, Pte. Magdalena y Tomás Imperial–Socsi, para el subperiodo 1960–1999.
- El estudio también indica textualmente (sección 6.2): "Los Caudales registrados en la estación Hidrométrica de Santo Domingo no obedecen a un régimen natural propiamente dicho debido a que existe la regulación de algunas Lagunas en las nacientes de las Subcuencas de Vichaycocha y Baños", regulación vigente desde antes de 1969 (8 lagunas reguladas por la Junta de Usuarios del Distrito de Riego Chancay-Huaral). **Esto es una limitación relevante para la validación GRACE-FO**: la serie no refleja únicamente la variabilidad hidrológica natural de la cuenca, sino también la operación antrópica de embalses/lagunas.

**Meses faltantes (NA), 9 en total (0.96%):**
| Fecha | Comentario |
|---|---|
| 1925-03, 1925-04, 1925-05, 1925-06 | Bloque de 4 meses consecutivos sin dato |
| 1990-01 | Mes aislado sin dato |
| 1991-09, 1991-11, 1991-12 | 3 meses sin dato (1991-10 sí tiene valor) |
| 1992-02 | Mes aislado sin dato |

**Continuidad temporal:** no se detectan huecos de calendario (todos los meses del rango 1922-01 a 1999-12 existen como fila, con `NA` donde no hay dato). No hay meses "saltados" fuera del rango declarado.

**Valores negativos:** no se encontraron valores negativos en la serie (0 casos), lo cual es físicamente consistente.

**Valores atípicos (IQR por mes calendario, no global):** se identificaron 24 meses fuera del rango intercuartílico (Q1–1.5·IQR, Q3+1.5·IQR) calculado independientemente para cada mes del año. Todos corresponden a **valores altos** (ningún atípico bajo), concentrados en años conocidos como húmedos/El Niño en la costa peruana (p. ej. 1972-73, 1982-83) y en meses de avenida (dic-abr). Interpretación preliminar: **extremos hidrológicos reales más que errores de medición**, dado que son consistentes con la estacionalidad de la cuenca (régimen de lluvias de verano austral) y con eventos climáticos regionales documentados; no se filtraron ni corrigieron. Ejemplos: 1972-03 = 219.4 m³/s (umbral superior del mes ≈109.1 m³/s); 1967-02 = 135.5 m³/s (umbral ≈88.7 m³/s); 1951-11 = 34.3 m³/s (umbral ≈11.6 m³/s). Se recomienda revisión hidrológica experta antes de usarlos como referencia de calibración GRACE si se busca excluir extremos.

**Consistencia caudal–volumen:** por construcción (volumen derivado matemáticamente del caudal con los días reales de cada mes), la consistencia es exacta en el 100% de los meses con dato; no aplica una verificación cruzada independiente porque no existe una fuente de volumen separada para esta estación.

**Limitaciones conocidas:**
- Serie no naturalizada (afectada por regulación de lagunas aguas arriba desde antes de 1969, ver arriba).
- No se dispone de coordenadas exactas de la estación Santo Domingo extraídas como texto (ver sección V).
- No se ha verificado con esta entrega si existen "saltos" (shifts) estadísticamente significativos; el estudio fuente menciona un "CUADRO N°24: ANÁLISIS ESTADÍSTICOS DE SALTOS" pero su contenido no fue extraído como texto (está embebido como tabla/imagen).

## V. Dominio espacial y coordenadas

- **Estación:** Santo Domingo (Estación Hidrométrica), río Chancay-Huaral.
- **Coordenadas (lat/lon WGS84):** **no disponibles en esta fase.** El único documento que debería contenerlas (`ESTUDIO_HIDROLOGICO_CHANCAY-HUARAL.pdf`, CUADRO N°02 "Estaciones Hidrológicas") presenta esa tabla como imagen incrustada, no como texto extraíble; por regla del proyecto no se estiman ni se leen valores de coordenadas desde una imagen sin solicitud explícita. Si se desea, puedo intentar una lectura visual de esa tabla, dejando constancia de menor confiabilidad.
- **Área de drenaje hasta la estación — discrepancia entre fuentes (se reporta, no se resuelve):**
  - `2_0_Oferta_Hidrica-Balance-Asignacion.xls` (hoja `Q_CIA_mm`/`Q_CIA_m3ps`): **1849.54 km²**.
  - `ESTUDIO_HIDROLOGICO_CHANCAY-HUARAL.pdf` (sección 3.4, texto): **1850.31 km²**.
  - Diferencia: 0.77 km² (~0.04%), probablemente redondeo/actualización entre versiones del estudio, pero se reporta sin promediar ni elegir una versión.
- **Bounding box para extracción GRACE-FO Mascon:** no se puede calcular con margen de 0.5° sin coordenadas puntuales confiables de la estación. Referencia aproximada de la cuenca Chancay-Huaral en la literatura pública: cuenca costera de Lima, entre aprox. 11.0°S–11.6°S y 76.4°O–77.2°O (extensión total de la cuenca, no solo hasta Santo Domingo) — **esto es una referencia general, no un dato extraído de la fuente, y debe tratarse como orientativo hasta confirmar coordenadas reales.**

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `santodomingo_caudales_crudos.csv` a `chancayhuaral_stodomingo_caudal_volumen_crudo.csv`.
- Metadata consolidada y reformateada desde `santodomingo_caudales_crudos_metadata.md` a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
