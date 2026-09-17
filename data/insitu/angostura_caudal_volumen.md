# Metadata — Caudal y Volumen Mensual, Estación/Embalse La Angostura (Sistema Regulador MAJES/RESERVA)

## I. Información general

Nombre del dataset: angostura_caudal_volumen.csv
Región/Cuenca: Estación hidrométrica "LA ANGOSTURA" (código SENAMHI 230501), parte del sistema regulador de cabecera del proyecto Majes (carpeta fuente `MAJES/RESERVA`). El río/subcuenca específica no está declarado en ninguno de los archivos fuente disponibles (ver limitación en Sección V).
Variable(s): Caudal medio mensual (m3/s, calculado como promedio de los días con dato válido de cada mes) y Volumen mensual (MMC, calculado).
Estación: LA ANGOSTURA (código 230501).
Resolución temporal: Mensual.
Cobertura temporal: 1965-02-01 a 2010-02-01, con una **discontinuidad total de 10 años sin ningún dato de caudal: 1985-1994** (ver Sección IV), y numerosos meses individuales sin dato dentro de los demás años — ver columna `cobertura_pct` del archivo de QA adjunto.
Número de registros: 362 meses con al menos 1 día de dato válido, de 541 meses posibles en todo el rango 1965-02 a 2010-02 (67% de los meses del rango tienen algún dato; ver detalle de cobertura por mes en el archivo QA).
Valores faltantes: Sin gaps declarados como NaN — solo se incluyen en el CSV los meses con al menos 1 día de dato válido; los meses sin ningún dato simplemente no tienen fila (ver lista completa de meses ausentes en Sección IV).
Generado el: Fase 2 del flujo de trabajo QA/QC - Proyecto GRACE-FO, carpeta MAJES/RESERVA.
Formato de fecha: YYYY-MM-DD (primer día de cada mes).

**Archivo complementario de QA:** `angostura_qa_caudal_cobertura_mensual.csv` — mismo `date` y `caudal_angostura_m3s`, más columnas `dias_con_dato`, `dias_mes` y `cobertura_pct` (0-100%), indicando qué fracción de los días del mes realmente tiene una lectura de caudal detrás del promedio mensual. **190 de los 362 meses (52%) tienen cobertura <50%** — se recomienda filtrar por `cobertura_pct` antes de usar este dataset para validación cuantitativa fina contra GRACE-FO, o al menos ponderar la confianza según ese valor.

## II. Fuentes de datos originales

Se fusionaron 3 archivos fuente (todos de solo lectura, carpeta `MAJES/RESERVA/Descargas_original_senamhi/`), cada uno cubriendo un tramo distinto del periodo total, con solapamientos parciales:

1. **`niveles y caudales la angostura.XLS`** (exportación HTML de SENAMHI): columnas Codigo, Estacion, Fecha Reg, Nivel 06h/10h/14h/18h, Nivel Med, Caudal. Cobertura de fechas: 01/02/1965 a 30/09/2009 (diario), pero la columna Caudal solo está poblada (no `-999` ni vacía) en 1,797 de 12,446 filas (14.4%) — la inmensa mayoría del archivo tiene solo lectura de Nivel, sin caudal calculado. El Caudal útil de este archivo se concentra casi enteramente en 1965-1984 (con huecos); de 1985 en adelante el archivo no vuelve a tener un solo valor de Caudal.
2. **`Q Angostura diario.xlsx`, hoja "Descargas2"**: columnas fecha, lecturas de nivel a 4 horas del día, DESCARGAS (caudal diario, m3/s asumido). Cobertura: bloques no contiguos entre 1982 y 2007 (ver Sección IV para el detalle de años ausentes dentro de este archivo, p.ej. 1985-1994 tampoco aparece aquí). **Se corrigió un bloque de 89 filas con año literal "1882" (01/02 a 30/04) a 1982**, tras confirmar que sus valores de Caudal, una vez reinterpretados como 1982, son consistentes (diferencias <0.02 m3/s en 3 de 4 días comparables, 1 día con diferencia de 2.0 m3/s) con los mismos días en `niveles y caudales la angostura.XLS` — decisión tomada junto con el usuario, no aplicada unilateralmente.
3. **`Q Angostura diario.xlsx`, hoja "Descargas"**: columnas FECHA, 10 lecturas de nivel (cada 2h) y DESCARGAS. Cobertura: 01/01/2006 a 28/02/2010, prácticamente sin huecos (1,399/1,521 días posibles, 92%).
4. **`Qm Angostura diario.xlsx`** (hoja "Diario"): se verificó que sus valores de DESCARGAS coinciden exactamente con los de la hoja "Descargas" de `Q Angostura diario.xlsx` para las mismas fechas — es un extracto/duplicado, **no se usó como fuente independiente** para evitar doble conteo. Su hoja "Calc Mensual" (agregado mensual ya calculado por el autor original) tampoco se usó como fuente; este dataset recalcula el promedio mensual directamente de los datos diarios fuente.

**Regla de prioridad aplicada para fusionar los 3 archivos día por día** (de mayor a menor prioridad, decidida junto con el usuario en los puntos de conflicto):
1. `Descargas` (Q Angostura diario.xlsx) — registro continuo 2006-2010, mayor resolución sub-diaria, sin problemas de orden/duplicados.
2. `Descargas2` (Q Angostura diario.xlsx, con la corrección de año 1882→1982) — cubre 1982/1995-2005 y un fragmento aislado de enero-febrero 2007.
3. `niveles y caudales la angostura.XLS` — usado solo donde ninguno de los dos anteriores tiene dato, principalmente 1965-1984 y parte de 1996.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Fecha Reg` / `fecha` / `FECHA` | `date` |
| `Caudal` / `DESCARGAS` | `caudal_angostura_m3s` |
| (no existe en la fuente) | `volumen_angostura_mmc` (calculado) |

---

Columna                     | Tipo    | Unidad | Descripción
------------------------------|---------|--------|------------------------------------------
date                         | date    | -      | Primer día del mes calendario (YYYY-MM-DD).
caudal_angostura_m3s         | float   | m3/s   | Caudal medio mensual en la estación La Angostura, calculado como el promedio aritmético de los días del mes con dato válido (no de todos los días del mes calendario — ver `cobertura_pct` en el archivo QA).
volumen_angostura_mmc        | float   | MMC    | Volumen mensual, **calculado** (no medido) como: V(MMC) = caudal_angostura_m3s x días_del_mes_calendario x 86400 / 1e6, siguiendo la fórmula estándar de la guía de estandarización (días reales del mes, incluye ajuste por años bisiestos).

## IV. QA/QC

1. **Discontinuidad total 1985-1994:** ninguno de los 3 archivos fuente tiene un solo día con valor de Caudal válido en esos 10 años (aunque `niveles y caudales la angostura.XLS` sí sigue teniendo lecturas de Nivel en ese periodo, sin conversión a caudal). No se estimó ni interpoló caudal alguno para ese periodo — es un vacío real de la fuente, no un error de procesamiento.
2. **Cobertura diaria muy variable dentro de los meses incluidos:** 190 de 362 meses (52%) tienen menos del 50% de los días del mes con dato real detrás del promedio — especialmente todo el periodo 1965-1984, donde la cobertura mensual osciló entre 10% y 61% (ver ejemplos en archivo QA). El volumen calculado para esos meses debe interpretarse con cautela: es una extrapolación de un promedio basado en pocos días a los 28-31 días del mes.
3. **59 meses completamente sin dato** dentro de los años que sí tienen datos en otros meses (no forman parte del vacío 1985-1994): 1965(2), 1969(6), 1970(6), 1971(2), 1972(3), 1973(2), 1974(3), 1975(3), 1977(2), 1978(1), 1979(4), 1980(1), 1982(4), 1984(8), 1995(3), 1996(1), 1999(1), 2003(1), 2007(1), 2008(1), 2009(2). Estos meses simplemente no tienen fila en el CSV (no se marcaron con NaN).
4. **Corrección de año 1882→1982** aplicada en 89 días de la hoja "Descargas2" — decisión tomada junto con el usuario tras verificar consistencia contra `niveles y caudales la angostura.XLS` (ver Sección II, punto 2).
5. **Duplicidad real detectada en "Descargas2", 01/08/2002-31/12/2002** (153 fechas): cada fecha tenía DOS registros de Nivel/Caudal claramente distintos (no redondeo, diferencias de hasta 75% en el valor de Caudal), posible mezcla de dos fuentes/correcciones en la misma hoja. **Por decisión del usuario, se usó el segundo registro de cada fecha duplicada** (el que aparece más abajo en la hoja original); el primero fue descartado. No se pudo determinar cuál de los dos era el correcto de forma independiente.
6. **Conflicto real detectado entre "Descargas" y "Descargas2" para enero-febrero 2007** (28 fechas): valores hasta 3 veces distintos para el mismo día (ej. 2007-02-11: 25.36 vs 73.28 m3/s). **Por decisión del usuario, se usó "Descargas"** (el registro continuo 2006-2010) y se descartó el fragmento correspondiente de "Descargas2" para esas fechas.
7. **Validación cruzada positiva:** donde `niveles y caudales la angostura.XLS` y "Descargas2" sí se solapan con dato válido en ambos (128 días, principalmente 1982 y 1996), 125/128 coinciden con diferencia <0.01 m3/s; solo 3 días muestran diferencias de 0.14 a 2.0 m3/s, sin patrón sistemático — no se investigó individualmente cada caso, se documenta como ruido de dígitos/redondeo entre fuentes.
8. **Nivel del embalse/estación NO incluido en este dataset:** los 3 archivos fuente traen columnas de Nivel (06h/10h/14h/18h y Nivel Med), pero por decisión del usuario el alcance de este proyecto se acotó a caudal/volumen, precipitación, evapotranspiración y nivel freático — el nivel de esta estación es un nivel de río/embalse (hidrométrico), no nivel freático (agua subterránea), por lo que queda fuera de alcance y no se generó un dataset separado para él.
9. **Río/sistema hidrográfico de la estación no confirmado:** ninguno de los archivos fuente declara a qué río o sistema pertenece la estación "La Angostura" (a diferencia de, por ejemplo, `DISPONIBILIDAD_HIDRICA.xls` que sí declaraba "Cuenca: RIO MAJES" para Huatiapa). No se asume ni se infiere el nombre del río para evitar introducir información no verificada en la fuente.

## V. Dominio espacial y coordenadas

- **Estación La Angostura (código SENAMHI 230501):** coordenadas no encontradas en ninguno de los archivos fuente disponibles para esta fase (`niveles y caudales la angostura.XLS`, `Q Angostura diario.xlsx`, `Qm Angostura diario.xlsx`, ni el archivo de precipitación homónimo `LA ANGOSTURA-MES.XLS` de la carpeta Pluviometria, que usa además un código distinto, 000754, propio de la red pluviométrica). No se estimaron coordenadas aproximadas para evitar introducir un valor no verificado.
- **Bounding box:** no se propone bounding box GRACE-FO en esta fase por falta de coordenadas verificadas de la estación.
- Nota de contexto geográfico general (no verificado en fuente, solo para orientar una futura búsqueda): "La Angostura" es un topónimo habitual del sistema regulador de cabecera de la cuenca Colca-Siguas-Chalhuanca que alimenta el proyecto de irrigación Majes; esta asociación NO se confirma con ningún documento de la fuente disponible y no debe tomarse como dato verificado.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Dataset nuevo, generado a partir de 3 archivos fuente de la carpeta `MAJES/RESERVA/Descargas_original_senamhi/` (ver Sección II para el detalle de fusión y prioridad).
- Serie diaria reconstruida internamente (no publicada como CSV aparte en esta fase; el usuario definió alcance mensual para este dataset) y luego agregada a caudal medio mensual + volumen calculado.
- Decisiones tomadas junto con el usuario durante el procesamiento (documentadas en detalle en Sección IV): corrección de año 1882→1982; uso del segundo registro en los duplicados de ago-dic 2002; uso de la hoja "Descargas" por sobre "Descargas2" para el conflicto de enero-febrero 2007.
- Se generó un archivo QA complementario `angostura_qa_caudal_cobertura_mensual.csv` con el detalle de cobertura diaria detrás de cada promedio mensual, siguiendo el precedente de los archivos `ica_qa_caudal_*` ya existentes en INSITU_estandarizado.
- Nombre de ámbito `angostura` (nombre de la estación); categoría `caudal_volumen` sin calificador adicional, siguiendo la convención de la guía.
