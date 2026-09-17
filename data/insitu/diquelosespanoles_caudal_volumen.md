# Metadata — Caudal y Volumen Mensual, Estación Dique Los Españoles (Sistema Regulador MAJES/RESERVA)

## I. Información general

Nombre del dataset: diquelosespanoles_caudal_volumen.csv
Región/Cuenca: Estación "DIQUE LOS ESPAÑOLES" (código SENAMHI 204612), parte del sistema regulador de cabecera del proyecto Majes (carpeta fuente `MAJES/RESERVA`). Río/subcuenca específica no declarado en la fuente.
Variable(s): Caudal medio mensual (m3/s, medido/reportado por la fuente) y Volumen mensual (MMC, calculado).
Estación: Dique Los Españoles (código 204612), variable de fuente "DC201 - DESCARGA MEDIAS MENSUAL".
Resolución temporal: Mensual.
Cobertura temporal: 17 años hidrológicos (Setiembre-Agosto), de 1968-1969 a 1989-1990, con huecos internos (ver Sección IV). Rango de fechas del CSV: 1968-09-01 a 1989-12-01.
Número de registros: 172 meses con dato (de 204 meses posibles en el rango de 17 años hidrológicos completos; 32 meses ausentes).
Valores faltantes: No se incluyen como NaN; los meses sin dato en la fuente simplemente no tienen fila.
Generado el: Fase 2 del flujo de trabajo QA/QC - Proyecto GRACE-FO, carpeta MAJES/RESERVA.
Formato de fecha: YYYY-MM-DD (primer día de cada mes).

## II. Fuentes de datos originales

- Archivo de datos: `dique- datos descarga.XLS` (exportación HTML de SENAMHI), carpeta `MAJES/RESERVA/Descargas_original_senamhi/`.
- **Nota de duplicidad de archivos fuente:** la misma carpeta contiene además `dique- grafico descarga.XLS` y `dique- grafico nivel.XLS`; se verificó por hash MD5 que los 3 archivos son **byte a byte idénticos** (mismo contenido exacto, incluida la tabla "DESCARGA MEDIAS MENSUAL"). El archivo nombrado "grafico nivel" NO contiene en realidad datos de nivel — es una copia exacta de la tabla de descarga, probablemente un error de exportación/nombrado del usuario original de SENAMHI. No existe, por tanto, ningún dato de Nivel disponible para esta estación en esta carpeta.
- Tabla fuente: "Codigo: 204612, Estación: DIQUE LOS ESPAÑOLES, Cod Var: DC201, Variable: DESCARGA MEDIAS MENSUAL", organizada por año hidrológico Set-Ago (columnas Set,Oct,Nov,Dic,Ene,Feb,Mar,Abr,May,Jun,Jul,Ago), 1968-1969 a 1989-1990. La fuente también incluye filas resumen "STD", "Media" y "Suma" (estadísticos por mes calendario a través de los años) que NO se incluyeron en este dataset por no ser observaciones fechadas.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| Fila de año hidrológico, columnas `Set...Ago` | `date` (reconstruida) |
| Valor de descarga de cada mes | `caudal_diquelosespanoles_m3s` |
| (no existe en la fuente) | `volumen_diquelosespanoles_mmc` (calculado) |

---

Columna                             | Tipo    | Unidad | Descripción
--------------------------------------|---------|--------|------------------------------------------
date                                  | date    | -      | Primer día del mes calendario (YYYY-MM-DD).
caudal_diquelosespanoles_m3s          | float   | m3/s   | Caudal (descarga) medio mensual reportado por SENAMHI para la estación Dique Los Españoles.
volumen_diquelosespanoles_mmc         | float   | MMC    | Volumen mensual, **calculado** (no medido) como: V(MMC) = caudal_diquelosespanoles_m3s x días_del_mes_calendario x 86400 / 1e6, según la fórmula estándar de la guía (días reales del mes, ajustado por años bisiestos).

## IV. QA/QC

1. **Reconstrucción de año hidrológico a fecha calendario:** la fuente organiza los datos por año hidrológico "AAAA - AAAA+1" (Set-Ago). Los meses Set-Dic se asignaron al primer año del par; los meses Ene-Ago, al segundo año — mismo criterio ya usado en `camana_majes_caudal_volumen.csv` (aunque ahí el año hidrológico era Ago-Jul, aquí es Set-Ago).
2. **32 meses sin dato dentro del rango 1968-1990:** los años 1972-73 (falta Jul-Ago), 1977-78 (solo 3 meses con dato), 1978-79 (solo 3 meses con dato), 1983-84 (falta Feb-Mar), 1984-85 (solo 3 meses con dato), 1985-86 (falta Dic y Feb-Abr), 1987-88 (falta Feb), y 1989-90 (falta may-ago, la serie termina ahí) tienen huecos. No se interpoló ni estimó ningún valor faltante.
3. **Filas de resumen de la fuente excluidas:** las filas "STD" (desviación estándar por mes calendario), "Media" y "Suma" que trae la tabla original no se incluyeron en el CSV por ser estadísticos agregados entre años, no observaciones de un mes/año específico — coherente con el tratamiento ya dado a estadísticos similares en `camana_majes_caudal_volumen.md` (hojas de persistencia excluidas por la misma razón).
4. **Sin outliers evidentes:** el rango de valores (0.24 a 3.58 m3/s) es consistente año a año, sin valores que se aparten notoriamente del resto de la serie.
5. **Río/sistema hidrográfico no confirmado:** la fuente no declara a qué río o quebrada pertenece la estructura "Dique Los Españoles"; no se asume para evitar introducir información no verificada.

## V. Dominio espacial y coordenadas

- **Estación Dique Los Españoles (código SENAMHI 204612):** coordenadas no encontradas en el archivo fuente disponible para esta fase. No se estimaron para evitar introducir un valor no verificado.
- **Bounding box:** no se propone en esta fase por falta de coordenadas verificadas.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Dataset nuevo, generado a partir de `dique- datos descarga.XLS` (carpeta `MAJES/RESERVA/Descargas_original_senamhi/`).
- Se verificó y documentó que los 3 archivos "dique-" de la carpeta fuente son idénticos byte a byte (ver Sección II); solo se usó uno como fuente.
- Filas de año hidrológico (Set-Ago) transpuestas a fechas calendario `date` (YYYY-MM-DD); columna de descarga renombrada a `caudal_diquelosespanoles_m3s`; columna `volumen_diquelosespanoles_mmc` calculada según la fórmula estándar de la guía.
- Nombre de ámbito `diquelosespanoles` (nombre de la estructura/estación, sin espacios ni tildes); categoría `caudal_volumen` sin calificador adicional.
