# ENSO indices

Monthly indices used to classify ENSO phases. All files share the same layout: a `time` column
(`YYYY-MM-DD`, first day of the month) followed by the index columns.

| File | Period | Content | Used in |
|---|---|---|---|
| `ecindex_ersstv5.csv` | 2002-01 → 2026-02 | IGP E and C indices (Takahashi et al., 2011) from ERSSTv5 | Notebook 03; GRACE composites in Notebook 04 |
| `ecindex_ersstv6.csv` | 1850-01 → 2026-09 | IGP E and C indices (Takahashi et al., 2011) from ERSSTv6, no smoothing | Month-by-month classification of in-situ records (1950+) in Notebook 04 |
| `oni_2002_2025.csv` | 2002 → 2025 | NOAA Oceanic Niño Index | Notebook 02 |
| `icen_2002_2025.csv` | 2002 → 2025 | ENFEN Índice Costero El Niño (ICEN) | Notebook 02 |
| `ninodata_1982_2025.csv` | 1982 → 2025 | Niño 1+2, 3, 4 and 3.4 SST and anomalies | Notebook 02 |

**E and C indices.** Uncorrelated indices obtained by rotating by 45° the first two principal
components of equatorial Pacific SST anomalies (Takahashi et al., 2011): E = (PC1 − PC2)/√2,
C = (PC1 + PC2)/√2. E describes the **extreme warm events of the Eastern Pacific** (R = 0.94 with
Niño 1+2); C describes the **cold and moderate warm events of the Central Pacific** (R = 0.98 with
Niño 4). Takahashi et al. (2011) show that the two EOF modes are not distinct phenomena (canonical
vs. "Modoki" El Niño) but the nonlinear evolution of ENSO. Regime names used in the thesis:
**El Niño E (Eastern Pacific)**, **El Niño C (Central Pacific)**, **La Niña C** and the **cold
phase of E**. *Coastal El Niño* is reserved for events defined by the ENFEN ICEN (e.g. 2017,
2023–24); the E regime is not equivalent to it. The IGP series are computed from ERSSTv5
(Huang et al., 2017) and ERSSTv6.

Reference: Takahashi, K., Montecinos, A., Goubanova, K., & Dewitte, B. (2011). ENSO regimes:
Reinterpreting the canonical and Modoki El Niño. *Geophysical Research Letters*, 38, L10704.
https://doi.org/10.1029/2011GL047364
