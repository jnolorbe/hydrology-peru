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

**E and C indices.** E describes Eastern Pacific / coastal El Niño (Niño 1+2 warming); C describes
Central Pacific El Niño (Modoki). Positive C is the Central Pacific El Niño; only its negative
extreme corresponds to the Central Pacific La Niña (Takahashi et al., 2011; Cai et al., 2020).

Reference: Takahashi, K., Montecinos, A., Goubanova, K., & Dewitte, B. (2011). ENSO regimes:
Reinterpreting the canonical and Modoki El Niño. *Geophysical Research Letters*, 38, L10704.
https://doi.org/10.1029/2011GL047364
