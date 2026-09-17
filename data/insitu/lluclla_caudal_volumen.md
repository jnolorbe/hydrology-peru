# Metadata — Caudal y Volumen Mensual, Estación Lluclla (Sistema Regulador MAJES/RESERVA)

## I. Información general

Nombre del dataset: lluclla_caudal_volumen.csv
Región/Cuenca: Estación "LLUCLLA" (código SENAMHI 204714), parte del sistema regulador de cabecera del proyecto Majes (carpeta fuente `MAJES/RESERVA`). Río/subcuenca específica no declarado en la fuente (probablemente asociado a la Laguna Lluclla, sin confirmar).
Variable(s): Caudal medio mensual (m3/s, medido/reportado por la fuente) y Volumen mensual (MMC, calculado).
Estación: Lluclla (código 204714), variable de fuente "DC201 - DESCARGA MEDIAS MENSUAL".
Resolución temporal: Mensual.
Cobertura temporal: 10 años hidrológicos (Setiembre-Agosto), de 1977-1978 a 1986-1987, con huecos internos (ver Sección IV). Rango de fechas del CSV: 1977-09-01 a 1986-10-01.
Número de registros: 90 meses con dato (de 120 meses posibles en el rango de 10 años hidrológicos completos; 30 meses ausentes).
Valores faltantes: No se incluyen como NaN; los meses sin dato en la fuente simplemente no tienen fila.
Generado el: Fase 2 del flujo de trabajo QA/QC - Proyecto GRACE-FO, carpeta MAJES/RESERVA.
Formato de fecha: YYYY-MM-DD (primer día de cada mes).

## II. Fuentes de datos originales

- Archivo de datos: `lluclla - datos descarga.XLS` (exportación HTML de SENAMHI), carpeta `MAJES/RESERVA/Descargas_original_senamhi/`.
- **Nota de duplicidad de archivos fuente:** la misma carpeta contiene además `lluclla - grafico  descarga.XLS` y `lluclla - grafico  nivel.XLS`; se verificó por hash MD5 que los 3 archivos son **byte a byte idénticos**, igual que se documentó para Dique Los Españoles. El archivo "grafico nivel" tampoco contiene datos de Nivel reales — es copia exacta de la tabla de descarga. No hay dato de Nivel disponible para esta estación en esta carpeta.
- Tabla fuente: "Codigo: 204714, Estación: LLUCLLA, Cod Var: DC201, Variable: DESCARGA MEDIAS MENSUAL", organizada por año hidrológico Set-Ago, 1977-1978 a 1986-1987. Incluye filas resumen "STD"/"Media"/"Suma" excluidas de este dataset (ver Sección IV).

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| Fila de año hidrológico, columnas `Set...Ago` | `date` (reconstruida) |
| Valor de descarga de cada mes | `caudal_lluclla_m3s` |
| (no existe en la fuente) | `volumen_lluclla_mmc` (calculado) |

---

Columna                     | Tipo    | Unidad | Descripción
------------------------------|---------|--------|------------------------------------------
date                         | date    | -      | Primer día del mes calendario (YYYY-MM-DD).
caudal_lluclla_m3s           | float   | m3/s   | Caudal (descarga) medio mensual reportado por SENAMHI para la estación Lluclla.
volumen_lluclla_mmc          | float   | MMC    | Volumen mensual, **calculado** (no medido) como: V(MMC) = caudal_lluclla_m3s x días_del_mes_calendario x 86400 / 1e6, según la fórmula estándar de la guía.

## IV. QA/QC

1. **Reconstrucción de año hidrológico a fecha calendario:** mismo criterio que en `diquelosespanoles_caudal_volumen.csv` (Set-Dic → primer año del par, Ene-Ago → segundo año).
2. **30 meses sin dato dentro del rango 1977-1987:** 1981-82 (falta Jun), 1983-84 (falta Dic-Mar y Jun-Ago), 1984-85 (solo 2 meses con dato), 1985-86 (falta Nov-Dic), 1986-87 (solo 2 meses con dato, la serie termina ahí). No se interpoló ni estimó ningún valor faltante.
3. **VALOR ATÍPICO — marzo 1983-84 = 48.064 m3/s:** este valor es 20 a 40 veces más alto que el resto de los valores de marzo en toda la serie (rango normal de marzo: 1.25 a 2.74 m3/s en los demás años). Los meses adyacentes del mismo año hidrológico también están elevados (abril 1984 = 9.923, mayo 1984 = 5.349), lo que podría indicar un evento real de avenida extraordinaria, pero también podría ser un error de transcripción en la fuente original (ej. un dígito de más). **Por decisión explícita del usuario, se incluye el valor literal de la fuente sin corregir ni excluir**, documentado aquí como no verificado de forma independiente. Nótese que las propias filas resumen de la fuente ("STD"=15.70, "Media"=9.54 para marzo, muy por encima del resto de meses) confirman que este valor también distorsiona fuertemente los estadísticos calculados por el autor original — es decir, el valor ya estaba presente (sin corregir) en la fuente tal como se recibió.
4. **Filas de resumen de la fuente excluidas:** igual que en `diquelosespanoles_caudal_volumen.csv`, las filas "STD"/"Media"/"Suma" no se incluyeron por ser estadísticos agregados entre años.
5. **Río/sistema hidrográfico no confirmado:** la fuente no declara el río/quebrada de la estación "Lluclla"; se asume asociación con la Laguna Lluclla solo como referencia de contexto (topónimo compartido), sin verificación documental — no debe tomarse como dato confirmado.

## V. Dominio espacial y coordenadas

- **Estación Lluclla (código SENAMHI 204714):** coordenadas no encontradas en el archivo fuente disponible para esta fase. No se estimaron para evitar introducir un valor no verificado.
- **Bounding box:** no se propone en esta fase por falta de coordenadas verificadas.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Dataset nuevo, generado a partir de `lluclla - datos descarga.XLS` (carpeta `MAJES/RESERVA/Descargas_original_senamhi/`).
- Se verificó y documentó que los 3 archivos "lluclla" de la carpeta fuente son idénticos byte a byte (ver Sección II); solo se usó uno como fuente.
- Filas de año hidrológico (Set-Ago) transpuestas a fechas calendario `date`; columna de descarga renombrada a `caudal_lluclla_m3s`; columna `volumen_lluclla_mmc` calculada según la fórmula estándar de la guía.
- Valor atípico de marzo 1983-84 (48.064 m3/s) mantenido sin modificar por decisión explícita del usuario — ver Sección IV, punto 3.
- Nombre de ámbito `lluclla` (nombre de la estación); categoría `caudal_volumen` sin calificador adicional.
