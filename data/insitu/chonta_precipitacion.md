# Metadata — METADATA: precipitacion_huacataz_1977_1987.csv

## I. Información general

* **Nombre de archivo:** `chonta_huacataz_precipitacion.csv`
* **Ámbito geográfico:** Cuenca del Río Chonta[cite: 2].
* **Departamento/Región:** Cajamarca, Perú[cite: 2].
* **Resolución temporal:** Mensual.
* **Periodo de registro:** 1977-01-01 a 1987-12-01 (11 años continuos)[cite: 2].
* **Desfase respecto al año calendario:** No aplica (los datos inician en enero y terminan en diciembre).
* **Completitud:** 100% (132 meses sin lagunas de información).

## II. Fuentes de datos originales

* **Documento base:** "IInformeFinal.pdf" (Inventario Participativo de Fuentes de Agua Superficial de la Cuenca del Río Chonta)[cite: 2].
* **Entidad emisora:** Ministerio de Agricultura (Intendencia de Recursos Hídricos del INRENA y Administración Técnica del Distrito de Riego Cajamarca)[cite: 2].
* **Año de emisión:** 2007 (inferido por el cronograma de actividades documentado)[cite: 2].
* **Aporte específico:** La serie temporal se extrajo del "Cuadro N° 2.5: Datos de Precipitación Mensual (mm), Huacatáz", el cual el informe técnico compiló a partir de la tesis *Estudio Climatológico del Valle de Cajamarca* (1989, Universidad Nacional de Cajamarca)[cite: 2].

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `date` | `date` |
| `precipitacion_huacataz_mm` | `precipitacion_huacataz_mm` |

---

* `date`: Fecha correspondiente al inicio del mes de registro, formato `YYYY-MM-DD` (ej. 1977-01-01 corresponde a enero de 1977).
* `precipitacion_huacataz_mm`: Precipitación total mensual registrada en la estación Huacatáz. Unidad: milímetros (mm). Fuente: Medición in situ[cite: 2].

## IV. QA/QC

* **Transformaciones aplicadas:** Se transpuso la matriz del "Cuadro N° 2.5" de un formato ancho (columnas por mes) a un formato largo/tidy (series de tiempo) apto para análisis.
* **Control de valores negativos:** 0 eventos detectados. Físicamente consistente.
* **Datos marcados/corregidos en fuente:** No existen indicaciones de corrección previa en el cuadro base[cite: 2].
* **Análisis de Valores Atípicos (Outliers):** Calculados mediante el Rango Intercuartílico (IQR) iterando exclusivamente **por mes calendario** (para aislar la estacionalidad de la cuenca). Se detectaron las siguientes anomalías estadísticas:
    * **Febrero:** 1981 (222.6 mm) y 1984 (332.8 mm) superan el límite superior (191.7 mm).
    * **Abril:** 1983 (159.3 mm) supera el límite superior (144.7 mm).
    * **Mayo:** 1978 (75.1 mm) y 1984 (85.4 mm) superan el límite superior (70.1 mm).
    * **Junio:** 1981 (27.3 mm) y 1984 (21.1 mm) superan el límite superior (17.1 mm). 1979 (0.1 mm) cruza el límite inferior (0.17 mm).
    * **Noviembre:** 1980 (201.4 mm) supera el límite superior (127.2 mm). 1979 (33.2 mm) cruza el límite inferior (43.8 mm).
    * *Interpretación y Acción:* Estos valores atípicos representan variaciones climáticas extremas reales (e.g., lluvias anómalas por eventos ENOS, considerando los periodos 1982-1983)[cite: 2]. Los valores registrados coinciden perfectamente con los totales anuales de la tabla original[cite: 2]. **No fueron modificados ni eliminados.**
* **Alcance y Limitaciones:** La serie es temporalmente corta (11 años), finalizando antes del inicio de la misión GRACE (2002). Su valor para validación satelital actual será como generador de climatología base o para forzamiento de modelos hidrológicos retrospectivos.

## V. Dominio espacial y coordenadas

* **Estación:** Huacatáz[cite: 2].
* **Altitud declarada:** 3130 msnm[cite: 2].
* **Coordenadas originales reportadas:** 7°05' Latitud Sur, 78°28' Longitud Oeste[cite: 2].
* **Coordenadas decimales estandarizadas (WGS84):** 
    * Latitud: -7.0833
    * Longitud: -78.4667
* **Bounding Box recomendado (Buffer de 0.5° para extracción GRACE-FO Mascon):**
    * Rango Latitud: [-7.5833, -6.5833]
    * Rango Longitud: [-78.9667, -77.9667]
* **Conflictos espaciales:** No se registran conflictos de ubicación de esta estación específica entre el *Informe Principal.doc* y el *IInformeFinal.pdf*.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `chonta_huacataz_precipitacion.csv` a `chonta_precipitacion.csv`.
- Metadata consolidada y reformateada desde `chonta_precipitacion.md` a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
