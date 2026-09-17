# Metadata — METADATOS DEL DATASET DE: CAUDALES Y VOLUMENES MULTIESTACION

## I. Información general

- Nombre del Dataset: Series temporales mensuales de caudales y volúmenes aforados de los ríos Huarmey, Culebras, Casma y Sechín.
- Período de Registro: 1973 - 2002 (Variable según estación).
- Frecuencia: Mensual.
- Unidades de medida: Metros cúbicos por segundo (m³/s) y Millones de metros cúbicos (MMC).

## II. Fuentes de datos originales

- Archivo "DISPONIBILIDAD HIDRICA HUAMBA.xls" (Hoja "Q aforado").
- Archivo "DISPONIBILIDAD HIDRICA RAIPA.xls" (Hoja "Q aforado").
- Archivo "Doblemasa Casma-Huarmey-Sechin.xls" (Hojas "CASMA" y "SECHIN").

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Date` | `date` |
| `caudal_huamba_m3s` | `caudal_huamba_m3s` |
| `volumen_huamba_mmc` | `volumen_huamba_mmc` |
| `caudal_raipa_m3s` | `caudal_raipa_m3s` |
| `volumen_raipa_mmc` | `volumen_raipa_mmc` |
| `caudal_tutuma_m3s` | `caudal_tutuma_m3s` |
| `volumen_tutuma_mmc` | `volumen_tutuma_mmc` |
| `caudal_quillo_m3s` | `caudal_quillo_m3s` |
| `volumen_quillo_mmc` | `volumen_quillo_mmc` |

---

- Date: Fecha correspondiente al mes de registro en formato YYYY-MM-DD (día 01 del mes).
- caudal_huamba_m3s: Caudal medio mensual, estación Huamba (río Huarmey) [m³/s].
- volumen_huamba_mmc: Volumen mensual acumulado, estación Huamba [MMC].
- caudal_raipa_m3s: Caudal medio mensual, estación Raipa (río Culebras) [m³/s].
- volumen_raipa_mmc: Volumen mensual acumulado, estación Raipa [MMC].
- caudal_tutuma_m3s: Caudal medio mensual, estación Tutuma (río Casma) [m³/s].
- volumen_tutuma_mmc: Volumen mensual acumulado, estación Tutuma [MMC].
- caudal_quillo_m3s: Caudal medio mensual, estación Pte. Quillo (río Sechín) [m³/s].
- volumen_quillo_mmc: Volumen mensual acumulado, estación Pte. Quillo [MMC].

## IV. QA/QC

- Transposición de datos: Los datos matriciales originales (Años x Meses) fueron transvasados a un formato longitudinal (tidy).
- Tratamiento de Fechas: Se asignó el día '01' de cada mes como estándar referencial para las marcas de tiempo.
- Cálculo de Volúmenes: Volumen (MMC) = Caudal (m³/s) * 86400 (s/día) * (días del mes) / 1,000,000.
- Valores nulos (gaps): Las celdas sin datos (por falta de aforo en ciertos períodos) se mantienen como NaN.

## V. Dominio espacial y coordenadas

- Estación Huamba (Río Huarmey): 09º32'10” S, 77º56'44” W, Altitud 1200 msnm.
- Estación Raipa (Río Culebras): 09º19'27” S, 78º02'40” W, Altitud 1200 msnm.
- Estación Tutuma (Río Casma): Aprox. 09°29'00" S, 78°13'00" W, Altitud 830 msnm.
- Estación Pte. Quillo (Río Sechín): 09°12'00" S, 78°04'48" W, Altitud 200 msnm (oficial) / 1189 msnm (control de cabecera).
- Región: Áncash, Perú.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `huarmey_caudales.csv` a `huarmeyculebras_caudal_volumen_multicuenca.csv`.
- Metadata consolidada y reformateada desde `huarmey_caudales_metadata.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
