# Notebooks

Sequential analysis pipeline for the study *Spatio-temporal Analysis of Hydrological Response
in Peru (2002-2025)*. Each notebook is self-contained and Colab-ready (badge cell at the top
clones/pulls this repository and resolves all data paths automatically).

| # | Notebook | Purpose |
|---|----------|---------|
| 01 | `01_data_preprocessing_and_curation.ipynb` | Raw GRACE/GRACE-FO mascon acquisition, spatial masking to Peru, IQR-based outlier filtering, and temporal gap-filling. Produces `data/processed/GRACE_Peru_final_IQR1_5.nc`. |
| 02 | `02_spatiotemporal_trends_and_enso.ipynb` | Spatial aggregation of TWS anomalies into the 14 AAA hydrographic domains, seasonal decomposition (climatology, trend, deseasonalized signal), and cross-domain / ENSO teleconnection analysis. |
| 03 | `03_GRACE_TWS_Composites_by_Asymmetric_ENSO_Regimes.ipynb` | Non-linear ENSO composites (El Niño E / El Niño C / La Niña C vs. neutral baseline) as % of local standard deviation, revealing the north-south TWS dipole and its domain-level ranking. |
| 04 | `04_insitu_validation_seasonality_and_enso_dipole.ipynb` | Independent validation of the seasonality (Notebook 02) and ENSO-regime (Notebook 03) findings against 69 standardized in-situ streamflow/precipitation records (`data/insitu/`; 3 files excluded for quality issues). Validates the three E/C regimes of Notebook 03 — El Niño E (Eastern Pacific), El Niño C (Central Pacific) and La Niña C — classifying in-situ months since 1950 with the IGP E/C index (ERSSTv6). El Niño E dipole validated (8/10 domains); El Niño C partially (5/10) and La Niña C not (2/10), both reported as documented limitations. |

Run them in order the first time (01 → 05); 02-05 each depend on outputs staged by the previous
notebook(s) in `data/`.

| # | Notebook | Purpose |
|---|----------|---------|
| 05 | `05_analisis_por_eventos.ipynb` | Event-based analysis (El Niño 2009–10, La Niña 2010–12, El Niño 2015–16, coastal El Niño 2017 and 2023–24; windows from ONI/ICEN): storage change per domain (cm, Gt), its percentile among same-length windows (descriptive), detrended variant and sensitivity to E/C-defined windows. |

## Shared functions: `comun.py`

`comun.py` is not an analysis step: it is the module of functions that notebooks 02–05 import
(`from comun import *`), so that every calculation used in the thesis is defined once — GRACE
loading, domain series, smoothing and decomposition, ENSO indices, regime classification,
autocorrelation-aware tests (effective degrees of freedom, phase-randomised surrogates,
circular-shift permutation, Benjamini–Hochberg FDR), in-situ composites and event analysis.
`verificar()` checks the basic counts quoted in the thesis (288 months, 14 domains, 13 El Niño E
months in 5 episodes, 69 in-situ records).

## Significance, sensitivity and events (thesis v13)

The former scripts 05–09 are now sections of the notebooks and call `comun.py`; their outputs in
`data/processed_derived/` are unchanged.

| Former script | Now | Outputs (`data/processed_derived/`) |
|---|---|---|
| 05 TLCC significance | Notebook 02, Section VIII | `tlcc_significance_base*.csv`, `tlcc_significance_detrended*.csv` |
| 06 composite significance | Notebook 03, Section VI (6.1) | `composite_significance_by_domain.csv`, `composite_significance_dipole_contrast.csv` |
| 07 composite sensitivity | Notebook 03, Section VI (6.2) | `composite_sensitivity.csv`, `composite_regime_inventory.csv` |
| 08 in-situ composites | Notebook 04, Section VI | `insitu_composite_*.csv` |
| 09 event analysis | Notebook 05 | `event_windows.csv`, `event_change.csv`, `event_sensitivity_EC.csv` |

- `robustness_checks/`: exploratory lag/prewhitening/sample-dependence scripts written while
  preparing the thesis; not part of the pipeline (edit BASE before running).
- `insitu_records_coverage.csv` and `grace_tws_climatology_by_domain.csv` in
  `data/processed_derived/` are reference tables produced during thesis preparation.
- In-situ domain values in Notebook 04, Section VI (used by the tests) can differ slightly from
  those of Section IV of the same notebook (e.g. Jequetepeque-Zarumilla, El Niño E: +133 vs +116).
