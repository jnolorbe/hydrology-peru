# Metadata — Caudal y Volumen Mensual, Estación Puente Colgante-Sibayo (Sistema Regulador MAJES/RESERVA)

## I. Información general

Nombre del dataset: puentecolgantesibayo_caudal_volumen.csv
Región/Cuenca: Estación "PUENTE COLGANTE-SIBAYO" (código SENAMHI 204604), parte del sistema regulador de cabecera del proyecto Majes (carpeta fuente `MAJES/RESERVA`). Río/subcuenca específica no declarado en la fuente (probablemente sobre el río/quebrada que pasa por la localidad de Sibayo, cuenca alta del Colca — no confirmado documentalmente).
Variable(s): Caudal medio mensual (m3/s, calculado como promedio de los días con dato válido de cada mes) y Volumen mensual (MMC, calculado).
Estación: Puente Colgante-Sibayo (código 204604).
Resolución temporal: Mensual.
Cobertura temporal: 1968-09-01 a 1993-03-01, con huecos (ver Sección IV). El archivo fuente en sí contiene registros de Nivel hasta el 31/03/2009, pero el cálculo de Caudal se detiene por completo después de marzo de 1993 (de 1994 en adelante, 0 días con Caudal válido pese a que el Nivel sigue registrado).
Número de registros: 268 meses con dato, todos con **100% de cobertura diaria** (los únicos meses incluidos son los que tienen el mes calendario completo con dato válido; no hay meses con cobertura parcial en este dataset — a diferencia de `angostura_caudal_volumen.csv`).
Valores faltantes: No se incluyen como NaN; los 58 meses sin ningún dato dentro del rango 1966-1993 simplemente no tienen fila (ver lista completa en Sección IV).
Generado el: Fase 2 del flujo de trabajo QA/QC - Proyecto GRACE-FO, carpeta MAJES/RESERVA.
Formato de fecha: YYYY-MM-DD (primer día de cada mes).

**Archivo complementario de QA:** `puentecolgantesibayo_qa_caudal_cobertura_mensual.csv` — mismas columnas de fecha/caudal más `dias_con_dato`, `dias_mes` y `cobertura_pct`; se incluye por consistencia con el resto de datasets diarios-agregados-a-mensual de esta carpeta, aunque en este caso todos los meses incluidos tienen 100% de cobertura.

## II. Fuentes de datos originales

- Archivo de datos: `niveles y caudales.XLS` (exportación HTML de SENAMHI), carpeta `MAJES/RESERVA/Descargas_original_senamhi/`. Columnas: Codigo, Estacion, Fecha Reg, Nivel 06h, Nivel 10h, Nivel 14h, Nivel 18h, Nivel Med, Caudal — 12,026 filas diarias, 01/11/1966 a 31/03/2009, todas para la estación "PUENTE COLGANTE-SIBAYO" (código 204604, sin mezcla con otras estaciones).
- La columna Caudal está poblada (valor numérico, sin código -999 en este archivo) en 8,157 de 12,026 filas (67.8%); el resto está en blanco. No se encontraron fechas duplicadas.
- Se construyó la serie diaria de Caudal filtrando solo los días con valor numérico, y se agregó a caudal medio mensual (promedio de los días válidos del mes) y volumen calculado.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Fecha Reg` | `date` |
| `Caudal` | `caudal_puentecolgantesibayo_m3s` |
| (no existe en la fuente) | `volumen_puentecolgantesibayo_mmc` (calculado) |

---

Columna                                  | Tipo    | Unidad | Descripción
--------------------------------------------|---------|--------|------------------------------------------
date                                        | date    | -      | Primer día del mes calendario (YYYY-MM-DD).
caudal_puentecolgantesibayo_m3s             | float   | m3/s   | Caudal medio mensual, calculado como promedio de los días del mes con dato diario válido.
volumen_puentecolgantesibayo_mmc            | float   | MMC    | Volumen mensual, **calculado** (no medido) como: V(MMC) = caudal_puentecolgantesibayo_m3s x días_del_mes_calendario x 86400 / 1e6.

## IV. QA/QC

1. **Sin duplicados de fecha:** a diferencia de la estación La Angostura (misma carpeta fuente), este archivo no presentó ninguna fecha repetida.
2. **Cobertura mensual excelente en los meses incluidos:** los 268 meses del dataset tienen 100% de los días del mes con dato válido (no hay meses "parciales" incluidos); cuando un mes no tenía el registro completo de Caudal, directamente no aparece en el dataset (ver punto 3).
3. **58 meses completamente ausentes dentro del rango 1966-1993:** todo 1966-11 a 1968-08 (excepto lo indicado), gran parte de 1967 y 1969 (el archivo solo tiene Caudal en fragmentos de esos años), 1970 (mar, abr, nov), 1982 (mar), **todo 1989** (12 meses, año completo sin dato), y 1993 (abr-dic, la serie termina en marzo de ese año). No se interpoló ni estimó ningún valor.
4. **Discontinuación del cálculo de Caudal tras marzo de 1993:** el archivo fuente sigue registrando Nivel (06h/10h/14h/18h) de forma prácticamente continua hasta el 31/03/2009, pero la columna Caudal queda en blanco para todo ese periodo posterior — mismo patrón ya documentado para la estación La Angostura en la misma carpeta (aparente descontinuación del uso de curva de descarga/rating curve en algún momento de los años 90). No se generó ningún dato de caudal para 1994-2009 por no existir en la fuente.
5. **Valor máximo verificado como plausible:** el valor más alto de la serie diaria (443.09 m3/s, 31/01/1978) se revisó en el contexto de los días adyacentes (135→274→265→281→310→**443**→278→238→205→168→108 m3/s entre el 26/01 y 05/02/1978) y corresponde a un pico de avenida con ascenso y descenso graduales típico de un evento de crecida real, no a un valor aislado o inconsistente — no se marca como atípico.
6. **Racha de valor constante 1.75 m3/s (15/11/1983 a 02/12/1983, 18 días consecutivos):** se documenta como posible artefacto de estiaje extremo/límite de la curva de descarga (valor "piso"), sin poder confirmarlo de forma independiente; no se modificó ni excluyó, ya que es un valor plausible de época seca, no un valor imposible.
7. **Nivel NO incluido en este dataset:** igual que en los demás datasets de esta carpeta, el nivel de río de esta estación es nivel hidrométrico (no nivel freático), por lo que queda fuera del alcance definido para este proyecto (caudal/volumen, precipitación, evapotranspiración, nivel freático).
8. **Río/sistema hidrográfico no confirmado:** la fuente no declara a qué río o quebrada pertenece la estación; no se asume para evitar introducir información no verificada.

## V. Dominio espacial y coordenadas

- **Estación Puente Colgante-Sibayo (código SENAMHI 204604):** coordenadas no encontradas en el archivo fuente disponible para esta fase. No se estimaron para evitar introducir un valor no verificado. Nota: existe también una estación pluviométrica llamada "SIBAYO" (archivo `SIBAYO- MES.XLS`, carpeta `RESERVA/Pluviometria/Precip_original_senamhi`, con un código de estación distinto) — se advierte que **no debe confundirse** con esta estación hidrométrica; el ámbito de este dataset se nombró `puentecolgantesibayo` (no solo `sibayo`) precisamente para evitar esa ambigüedad con el futuro dataset de precipitación.
- **Bounding box:** no se propone en esta fase por falta de coordenadas verificadas.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Dataset nuevo, generado a partir de `niveles y caudales.XLS` (carpeta `MAJES/RESERVA/Descargas_original_senamhi/`).
- Serie diaria de Caudal filtrada (excluyendo blancos) y agregada a caudal medio mensual + volumen calculado, siguiendo la misma metodología aplicada a `angostura_caudal_volumen.csv`.
- Se generó un archivo QA complementario `puentecolgantesibayo_qa_caudal_cobertura_mensual.csv` por consistencia con el resto de la carpeta, aunque en este caso todos los meses tienen 100% de cobertura.
- Nombre de ámbito `puentecolgantesibayo` (nombre completo de la estación, sin espacios ni tildes, para evitar confusión con la estación pluviométrica "Sibayo" de la misma zona — ver Sección V); categoría `caudal_volumen` sin calificador adicional.
