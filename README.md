# hydrology-peru

A Python-based repository for processing and analyzing GRACE/GRACE-FO satellite gravimetry
data applied to hydrological studies in Peru. Developed as part of a doctoral study on the
impact of ENSO (El Niño-Southern Oscillation) on Terrestrial Water Storage (TWS) in Peru
(Universidad Nacional Mayor de San Marcos, UNMSM).

## Contents

- **`notebooks/`** — Sequential, Colab-ready analysis pipeline (01-04). See
  `notebooks/readme.md` for a description of each notebook.
- **`data/raw/`** — Raw GRACE/GRACE-FO JPL RL06.3 mascon NetCDF (2002-2025).
- **`data/processed/`** — IQR-filtered, gap-filled GRACE TWS product used by all downstream
  notebooks.
- **`data/processed_derived/`** — Intermediate tabular products (e.g. GRACE seasonal
  climatology per AAA domain) used for reproducibility and validation.
- **`data/enso/`** — ENSO climate indices (E/C indices, ICEN, ONI, Niño 1+2/3/4/3.4).
- **`data/shapefiles/`** — Peru administrative boundaries and the 14 AAA (Autoridad
  Administrativa del Agua) hydrographic domain polygons used for spatial aggregation.
- **`data/insitu/`** — Standardized in-situ streamflow (caudal) and precipitation records used
  in Notebook 04 to independently validate the GRACE-derived findings. See
  `data/insitu/readme.md` for provenance, domain assignment, and exclusion criteria.

## Reproducing the analysis

Every notebook can be run directly in Google Colab via its "Open in Colab" badge — it clones
this repository and resolves all data paths automatically, no manual setup required.

To run locally, create the conda environment from the repository root:

```bash
conda env create -f environment.yml
conda activate hydrology-peru
```

(a `requirements.txt` is also provided for a plain `pip install -r requirements.txt` setup).

Run the notebooks in order (01 → 04); each of 02-04 depends on outputs produced by the
previous notebook(s).
