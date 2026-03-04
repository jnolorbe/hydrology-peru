# Hydrographic Domains: Water Administrative Authorities (AAA) - Peru

This vector dataset contains the boundaries of the Water Administrative Authorities (Autoridades Administrativas del Agua - AAA) of Peru, used for regional spatial analysis of satelital data.

### Technical Metadata
- **Data Source:** National Water Authority (Autoridad Nacional del Agua - ANA), Peru.
- **Coordinate Reference System (CRS):** WGS 84 (EPSG:4326).
- **Last Update/Sync:** July 03, 2020.
- **Processing:** Converted from Multipart to Singlepart features (ArcGIS 10.8).

### Data Dictionary (Attributes)
- `NAME_AAA`: Official name of the Administrative Unit (e.g., Cañete-Fortaleza, Mantaro).
- `AREA_KM2`: Total surface area of the unit in square kilometers.
- `CODE_AAA`: Numeric identification code assigned by ANA.
- `COD_ROMAN`: Official Roman numeral identification code.
- `Pob_2007`: Population data based on the 2007 National Census.

### File Manifest
To ensure full compatibility with Python (`geopandas`) and GIS software (QGIS/ArcGIS), the following extensions are included:
* `.shp`, `.shx`, `.dbf`: Core geometry and attribute data.
* `.prj`: Projection information (WGS84).
* `.cpg`: Character encoding for Spanish characters (accents and "ñ").
* `.xml`: Detailed ESRI metadata.
