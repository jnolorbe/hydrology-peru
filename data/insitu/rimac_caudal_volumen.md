# Metadata — METADATOS DEL DATASET DE: CAUDALES Y VOLÚMENES MENSUALES - CUENCA DEL RÍO RÍMAC

## I. Información general

Nombre del dataset:      dataset_caudales_rimac_1964_2009_completo.csv
Variable:                Caudal medio mensual (m3/s) y volumen mensual (MMC)
Ámbito:                  Cuenca del río Rímac (Lima, Perú)
Estaciones incluidas:    3 (Chosica, Sheque, Tamboraque)
Periodo temporal:        Enero 1964 - Diciembre 2009 (46 años, 552 registros mensuales)
Resolución temporal:     Mensual
Formato de fecha:        YYYY-MM-DD
Elaborado para:          Control de calidad (QA/QC) y validación de análisis estacional/
                         tendencia de datos TWS de GRACE-FO
Fecha de procesamiento:  Agosto 2026

## II. Fuentes de datos originales

Fuente primaria (dato numérico):
  - Autoridad Nacional del Agua (ANA), Administración Local de Agua Chillón-Rímac-Lurín.
  - Estudio Hidrológico y Ubicación de la Red de Estaciones Hidrométricas en la Cuenca 
    del Río Rímac (Volumen I y II, 2010).
Fuentes de validación:
  - Registros históricos de EDEGEL / ENEL (Estaciones hidrométricas en operación).
  - Modelos de transferencia hidrológica para la extensión de series en puntos de interés
    basados en la estación Chosica.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Date` | `date` |
| `caudal_chosica_m3s` | `caudal_chosica_m3s` |
| `caudal_sheque_m3s` | `caudal_sheque_m3s` |
| `caudal_tamboraque_m3s` | `caudal_tamboraque_m3s` |
| `volumen_chosica_mmc` | `volumen_chosica_mmc` |
| `volumen_sheque_mmc` | `volumen_sheque_mmc` |
| `volumen_tamboraque_mmc` | `volumen_tamboraque_mmc` |

---

Date                          | Fecha (primer día del mes), formato YYYY-MM-DD
caudal_chosica_m3s            | Caudal medio mensual, estación Chosica (río Rímac), m3/s
volumen_chosica_mmc           | Volumen mensual, estación Chosica, millones de m3 (MMC)
caudal_sheque_m3s             | Caudal medio mensual, estación Sheque (río Santa Eulalia), m3/s
volumen_sheque_mmc            | Volumen mensual, estación Sheque, millones de m3 (MMC)
caudal_tamboraque_m3s         | Caudal medio mensual, estación Tamboraque (río Rímac), m3/s
volumen_tamboraque_mmc        | Volumen mensual, estación Tamboraque, millones de m3 (MMC)
Fórmula de conversión caudal -> volumen:
  volumen_mmc = caudal_m3s * dias_del_mes * 86400 / 1,000,000

## IV. QA/QC

1. NATURALIZACIÓN: Las series históricas han sido ajustadas para representar un régimen
   naturalizado, descontando el efecto de trasvases intercuencas (Marcapomacocha) y la
   regulación artificial de lagunas y represas (Yuracmayo, entre otras).
2. COMPLETACIÓN: Las series fueron completadas y extendidas mediante análisis de
   correlación hidrológica y consistencia de doble masa, garantizando un periodo
   homogéneo de 1964-2009.
3. CÁLCULO: Se aplicó el factor de conversión estandarizado según el número de días
   específicos por mes (28, 29, 30 o 31 días) para asegurar el balance volumétrico.

## V. Dominio espacial y coordenadas

Estación     | Lat (dec) | Lon (dec)  | Altitud (m)
Chosica      | -11.9301  | -76.6899   | 906
Sheque       | -11.6667  | -76.5167   | 3,100
Tamboraque   | -11.7667  | -76.3167   | 3,200
Bounding Box (WGS84 aprox.):
  Lat mínima: -12.10° S, Lat máxima: -11.35° S
  Lon mínima: -77.15° W, Lon máxima: -76.15° W

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `rimac_caudales.csv` a `rimac_caudal_volumen.csv`.
- Metadata consolidada y reformateada desde `rimac_caudal_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
