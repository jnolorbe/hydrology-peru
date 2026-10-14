# Notebooks

Sequential analysis pipeline for the study *Spatio-temporal Analysis of Hydrological Response
in Peru (2002-2025)*. Each notebook is self-contained and Colab-ready (badge cell at the top
clones/pulls this repository and resolves all data paths automatically).

| # | Notebook | Purpose |
|---|----------|---------|
| 01 | `01_data_preprocessing_and_curation.ipynb` | Raw GRACE/GRACE-FO mascon acquisition, spatial masking to Peru, IQR-based outlier filtering, and temporal gap-filling. Produces `data/processed/GRACE_Peru_final_IQR1_5.nc`. |
| 02 | `02_spatiotemporal_trends_and_enso.ipynb` | Spatial aggregation of TWS anomalies into the 14 AAA hydrographic domains, seasonal decomposition (climatology, trend, deseasonalized signal), and cross-domain / ENSO teleconnection analysis. |
| 03 | `03_GRACE_TWS_Composites_by_Asymmetric_ENSO_Regimes.ipynb` | Non-linear ENSO composites (El Niño E / El Niño C / La Niña C vs. neutral baseline) as % of local standard deviation, revealing the north-south TWS dipole and its domain-level ranking. |
| 04 | `04_insitu_validation_seasonality_and_enso_dipole.ipynb` | Independent validation of the seasonality (Notebook 02) and ENSO-regime (Notebook 03) findings against 69 standardized in-situ streamflow/precipitation records (`data/insitu/`; 3 files excluded for quality issues). Validates the three E/C regimes of Notebook 03 — El Niño E (coastal), El Niño C (Central Pacific / Modoki) and La Niña C — classifying in-situ months since 1950 with the IGP E/C index (ERSSTv6). El Niño E dipole validated (8/10 domains); El Niño C partially (5/10) and La Niña C not (2/10), both reported as documented limitations. |

Run them in order the first time (01 → 04); 02-04 each depend on outputs staged by the previous
notebook(s) in `data/`.

## Additions for thesis v13 (robustness and significance)
- 05_tlcc_significance.py: TLCC significance (effective d.o.f., phase-randomized surrogates, BH-FDR).
- 06_composite_significance.py: circular-shift permutation for the regime composites (3 regimes).
- 07_composite_sensitivity.py: GRACE composites for 4 regimes (adds cold E), detrended and without the 2023-25 episode; BH-FDR over 56 tests.
- 08_insitu_composite_significance.py: in-situ composites (1950-), group tests and south reversal; DET=1 detrends each record.
- 09_event_analysis.py: event-based analysis (El Niño 2009-10, La Niña 2010-12, El Niño 2015-16, coastal El Niño 2017 and 2023-24; windows from ONI/ICEN): storage change per domain (cm, Gt) and its percentile among same-length windows. Outputs: data/processed_derived/event_change.csv, event_windows.csv.
- robustness_checks/: exploratory lag/prewhitening/sample-dependence scripts (edit BASE before running).
Derived tables: data/processed_derived/ (composite_sensitivity.csv, composite_regime_inventory.csv, insitu_composite_*.csv, insitu_records_coverage.csv).
Note: in-situ domain values from script 08 can differ slightly from notebook 04 (e.g. Jequetepeque-Zarumilla, El Nino E: +133 vs +116).
