# Metadata — Metadata — Caudal y Volumen mensual, Estación Santo Domingo — serie Homogenizada y Completada (H&C)

## I. Información general

- **Nombre de archivo del dataset:** `caudal_volumen_santodomingo_hc_1960_1999.csv`
- **Ámbito geográfico:** Cuenca del río Chancay-Huaral, hasta la Estación Hidrométrica Santo Domingo (Subcuenca Media).
- **Departamento / Región:** Lima, Perú (provincias de Huaral y Canta).
- **Resolución temporal:** mensual.
- **Periodo de registro:** 1960-01 a 1999-12 (40 años, 480 meses).
- **Desfase respecto al año calendario:** ninguno (Ene-Dic = año calendario).
- **% de completitud:** **100%** (0 de 480 meses faltantes). Esta serie es, por definición, la versión ya completada de la histórica (ver sección IV).
- **Relación con el otro dataset de esta misma estación:** esta serie es la contraparte **homogenizada y completada** de `caudal_volumen_santodomingo_1922_1999.csv` (serie histórica sin corregir, entregada previamente), pero cubre un periodo más corto (1960-1999 vs 1922-1999) porque la fuente solo aplicó el proceso de homogenización/completación a ese subperiodo.

## II. Fuentes de datos originales

| Fuente | Entidad / Autor | Año | Qué aportó específicamente |
|---|---|---|---|
| `2_0_Oferta_Hidrica-Balance-Asignacion.xls`, hoja `Q Med_H&C Sto Dom` | Water & Land (consultora), PROFODUA — INRENA / Intendencia de Recursos Hídricos | Última modificación registrada del archivo: 2006 | Serie mensual de caudales "Homogenizados y Completados" (m³/s) de la Estación Santo Domingo, 1960–1999. |
| `ESTUDIO_HIDROLOGICO_CHANCAY-HUARAL.pdf` — "Evaluación y Ordenamiento de los Recursos Hídricos de la Cuenca Chancay-Huaral", sección 6.4 | jchunga (autor del documento fuente "EstudioHidrolo.DOC") | PDF generado en 2008 | Descripción metodológica exacta del proceso de homogenización y completación aplicado a esta serie (ver sección IV). |

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `caudal_santodomingo_hc_m3s` | `caudal_santodomingo_hc_m3s` |
| `volumen_santodomingo_hc_mmc` | `volumen_santodomingo_hc_mmc` |

---

| Columna | Descripción | Unidad | Fuente | Fórmula |
|---|---|---|---|---|
| `date` | Primer día del mes calendario | YYYY-MM-DD | — | — |
| `caudal_santodomingo_hc_m3s` | Caudal medio mensual homogenizado y completado, Estación Santo Domingo | m³/s | Medido/Completado (ver sección IV) | — |
| `volumen_santodomingo_hc_mmc` | Volumen mensual equivalente | MMC (millones de m³) | Calculado | `V = Q_promedio_mensual (m³/s) × (n_días_del_mes × 86400 s) / 10⁶`, redondeado a 2 decimales, con días reales de cada mes (incluye años bisiestos). |

## IV. QA/QC

**Metodología de homogenización y completación (según el estudio fuente, sección 6.4, texto citado en paráfrasis):**
El estudio explica que, una vez corregida la información, se realizó la completación y extensión de los caudales medios mensuales de Santo Domingo para 1922-1999 en dos etapas: (1) completación manual a nivel mensual cuando los datos diarios faltantes no superaban 3 días, tomando el promedio de los datos existentes; (2) completación de los datos faltantes restantes mediante correlación múltiple con el software HEC4 (Cuerpo de Ingenieros del Ejército de EE.UU.), usando un grupo conformado por las estaciones Santo Domingo, Pte. Alco, Pte. Magdalena y Tomás Imperial–Socsi. El documento aclara que los registros homogenizados y completados se presentan en el "ANEXO I-3" del estudio (anexo no incluido en los archivos recibidos).

**Comparación cuantitativa directa entre la serie histórica y esta serie H&C (calculada por mí, no declarada explícitamente en la fuente), para el subperiodo común 1960–1999:**
De 480 meses, únicamente **6 difieren** entre ambas versiones:

| Fecha | Tipo de cambio | Valor histórico (m³/s) | Valor H&C (m³/s) |
|---|---|---|---|
| 1990-01 | Completado (faltante → valor) | NA | 17.000 |
| 1991-09 | Completado (faltante → valor) | NA | 4.000 |
| 1991-11 | Completado (faltante → valor) | NA | 7.000 |
| 1991-12 | Completado (faltante → valor) | NA | 10.000 |
| 1992-02 | Completado (faltante → valor) | NA | 6.000 |
| 1976-03 | **Ajustado/homogenizado** (no era un faltante) | 47.752 | 43.000 |

Los otros 474 meses del subperiodo 1960-1999 son **idénticos** entre la serie histórica y la H&C. Esto significa que el proceso de homogenización, para esta estación y este subperiodo, fue mínimo: solo rellenó 5 huecos y ajustó 1 valor existente (posible corrección por consistencia estadística/salto, no explicado en detalle en el texto disponible).

**Continuidad temporal:** sin huecos de calendario; 480/480 meses presentes.

**Valores negativos:** 0 casos (consistente físicamente).

**Valores atípicos (IQR por mes calendario):** 15 meses fuera de rango intercuartílico, todos por exceso (ningún atípico bajo). Mismos años/eventos que en la serie histórica (1967, 1970, 1972-73, 1982, 1990, 1993, 1997-98), coherentes con años húmedos/El Niño en la costa peruana. Se interpretan como extremos hidrológicos reales, no errores; no se filtraron.

**Consistencia caudal–volumen:** exacta en el 100% de los meses (volumen derivado matemáticamente del caudal con días reales de cada mes).

**Limitaciones conocidas (heredadas de la fuente, iguales que en la versión histórica):**
- La serie **no representa régimen natural**: el estudio indica que existe regulación de lagunas en las cabeceras de las subcuencas Vichaycocha y Baños desde antes de 1969 (actualmente 8 lagunas reguladas por la Junta de Usuarios del Distrito de Riego Chancay-Huaral). Esta es una limitación central para su uso en validación de TWSA/GRACE-FO, ya que la señal de caudal mezcla variabilidad climática con operación antrópica de embalses.
- No se dispone de coordenadas exactas de la estación (ver sección V).
- El "ANEXO I-3" mencionado por el estudio como soporte detallado de esta completación no fue recibido; por lo tanto, el detalle exacto del ajuste HEC4 para 1976-03 no pudo verificarse más allá de la comparación numérica directa.

## V. Dominio espacial y coordenadas

Idéntico a la versión histórica de esta misma estación (mismo punto de monitoreo físico):

- **Estación:** Santo Domingo (Estación Hidrométrica), río Chancay-Huaral.
- **Coordenadas (lat/lon WGS84):** no disponibles en esta fase — la tabla de estaciones hidrológicas del PDF (CUADRO N°02) está embebida como imagen, no como texto extraíble.
- **Área de drenaje — discrepancia entre fuentes (se reporta, no se resuelve):**
  - Excel (`Q_CIA_mm`/`Q_CIA_m3ps`): **1849.54 km²**.
  - PDF (sección 3.4, texto): **1850.31 km²**.
- **Bounding box GRACE-FO Mascon:** no calculable con confianza sin coordenadas puntuales confirmadas. Pendiente hasta contar con las coordenadas reales de la estación.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `santodomingo_caudales_homogenizados.csv` a `chancayhuaral_stodomingo_caudal_volumen_homogenizado.csv`.
- Metadata consolidada y reformateada desde `santodomingo_caudales_homogenizados_metadata.md` a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
