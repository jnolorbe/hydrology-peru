# Notebooks

Sequential analysis pipeline for the study *Spatio-temporal Analysis of Hydrological Response
in Peru (2002-2025)*. Each notebook is self-contained and Colab-ready (badge cell at the top
clones/pulls this repository and resolves all data paths automatically).

| # | Notebook | Purpose |
|---|----------|---------|
| 01 | `01_data_preprocessing_and_curation.ipynb` | Raw GRACE/GRACE-FO mascon acquisition, spatial masking to Peru, IQR-based outlier filtering, and temporal gap-filling. Produces `data/processed/GRACE_Peru_final_IQR1_5.nc`. |
| 02 | `02_spatiotemporal_trends_and_enso.ipynb` | Spatial aggregation of TWS anomalies into the 14 AAA hydrographic domains, seasonal decomposition (climatology, trend, deseasonalized signal), and cross-domain / ENSO teleconnection analysis. |
| 03 | `03_GRACE_TWS_Composites_by_Asymmetric_ENSO_Regimes.ipynb` | Non-linear ENSO composites (El Niño E / El Niño C / La Niña C vs. neutral baseline) as % of local standard deviation, revealing the north-south TWS dipole and its domain-level ranking. |
| 04 | `04_insitu_validation_seasonality_and_enso_dipole.ipynb` | Independent validation of the seasonality (Notebook 02) and El Niño Costero dipole (Notebook 03) findings against 72 standardized in-situ streamflow/precipitation records (`data/insitu/`). Reports the La Niña C discrepancy as a documented, unresolved limitation rather than a validated result. |

Run them in order the first time (01 → 04); 02-04 each depend on outputs staged by the previous
notebook(s) in `data/`.
