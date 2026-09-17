# Metadata — METADATOS DEL DATASET DE: PRECIPITACION

## I. Información general

- Proyecto: Validación y Calibración Hidrológica de Series Temporales GRACE-FO (TWS)
- Ámbito Geográfico: Cuenca Binacional del Río Zarumilla (Sectores Zarumilla y Matapalo)
- Región Hidrográfica: Pacífico Norte (Vertiente del Pacífico, Tumbes, Perú)
- Periodo Temporal Cubierto: Serie Base / Climatología Mensual (1960-2005) y Serie Diaria Modelo Base
- Entidad Autora / Custodia de Fuentes: Instituto Nacional de Recursos Naturales (INRENA) - PROFODUA / Dirección Regional Agraria Tumbes (DRAT)

## II. Fuentes de datos originales

- Anexo C.doc: Demanda de Agua del Valle de Zarumilla.
- Cuadro C-05: Archivo de Salida del Módulo de Requerimiento de Riego y Balance Hídrico CROPWAT (FAO / INRENA).
- Cap II Oferta.doc: Caracterización Pluviométrica de la Cuenca del Río Zarumilla.

## III. Diccionario de variables

| Columna original | Columna estandarizada |
|---|---|
| `Date` | `date` |
| `precipitacion_total_valle_zarumilla_mm` | `precipitacion_total_valle_zarumilla_mm` |
| `precipitacion_efectiva_valle_zarumilla_mm` | `precipitacion_efectiva_valle_zarumilla_mm` |

---

1. Date: Fecha en formato estándar ISO-8601 (YYYY-MM-DD).
2. precipitacion_total_valle_zarumilla_mm: Precipitación total mensual/diaria registrada en el ámbito del valle agrícola de Zarumilla, expresada en milímetros (mm).
3. precipitacion_efectiva_valle_zarumilla_mm: Precipitación efectiva calculada mediante la metodología USDA Soil Conservation Service integrada en CROPWAT (mm), que representa la fracción de lluvia directamente aprovechable en la zona radicular / almacenamiento superficial del suelo.

## IV. QA/QC

- Metodología de Precipitación Efectiva: Se procesó a partir del algoritmo estándar de la FAO/USDA:
    P_ef = P_tot * (125 - 0.2 * P_tot) / 125  (para P_tot <= 250 mm/mes)
- Régimen Hidrometeorológico: La cuenca baja de Zarumilla exhibe un régimen semiárido hiperestacional:
    * Periodo Lluvioso: Concentrado entre enero y abril (febrero alcanza 42.56 mm y marzo 35.65 mm).
    * Periodo de Estiaje / Seco: Mayo a diciembre con precipitación nula (0.00 mm).
    * Precipitación Anual Acumulada: 88.60 mm (Total) y 83.60 mm (Efectiva).
- Integración con GRACE-FO: La señal de precipitación efectiva y recarga pluviométrica estacional gobierna el pico de llenado de agua en el suelo (Soil Moisture Storage, $\Delta SMS$) entre los meses de febrero y abril, previo a la fase de descarga y agotamiento del acuífero.

## V. Dominio espacial y coordenadas

- Zona de Influencia: Valle de Zarumilla y Matapalo (Margen Izquierda y Derecha del Río Zarumilla).
- Bounding Box:
  * Latitud Norte:  -3.4000° S (03° 24' S)
  * Latitud Sur:    -3.7500° S (03° 45' S)
  * Longitud Oeste: -80.5000° W (80° 30' W)
  * Longitud Este:  -80.1500° W (80° 09' W)
- Rango Altitudinal del Valle Agrícola: 3 a 150 msnm.

## VI. Historial de procesamiento (estandarización INSITU_estandarizado)

- Archivo de datos renombrado desde `zarumilla_precipitacion_diaria.csv` a `zarumilla_precipitacion_diaria.csv`.
- Metadata consolidada y reformateada desde `zarumilla_metadatos_precipitacion.txt` (formato original: texto plano con secciones numeradas en romano) a la plantilla estándar de 6 secciones.
- Nombres de columna normalizados a snake_case; ver tabla de correspondencia en la sección III.
