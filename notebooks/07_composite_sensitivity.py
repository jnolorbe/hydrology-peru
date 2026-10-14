"""Sensitivity of the notebook-03 ENSO-regime composites (GRACE JPL mascon, % of local sigma).
Regimes: El Nino E, El Nino C, La Nina C and cold-E (E<=-1 & C>-1; exploratory).
Variants: base | linear detrend of each domain series | without the 2023-25 episode (regime months >=2022-10 removed from
the regime masks; neutral kept) | both. Test: circular-shift permutation (all non-zero shifts), two-sided; BH-FDR over
14 domains x 4 regimes = 56 tests (base variant). Group units: NORTE (Jequetepeque-Zarumilla + Huarmey-Chicama),
SUR (Pampas-Apurimac, Urubamba-Vilcanota, Caplina-Ocona, Titicaca) and N-S contrast.
Usage: python 07_composite_sensitivity.py <repo_root> <out_dir>"""
import os, sys, numpy as np, pandas as pd, xarray as xr, geopandas as gpd, rioxarray  # noqa
BASE, OUT = sys.argv[1], sys.argv[2]
ds = xr.open_dataset(os.path.join(BASE, "data/processed/GRACE_Peru_final_IQR1_5.nc"))
if 'month' in ds: ds = ds.drop_vars('month')
x = ds['lwe_thickness_corrected']; x = x - x.mean('time'); x = x.rio.write_crs("EPSG:4326")
Z = ((x / x.std('time')) * 100).rio.write_crs("EPSG:4326")
gdf = gpd.read_file(os.path.join(BASE, "data/shapefiles/hydroAAA_domains/Autoridad_Administrativa_del_Agua.shp"))
if gdf.crs.to_epsg() != 4326: gdf = gdf.to_crs(epsg=4326)
gdf = gdf[~((gdf['NAME_AAA'] == 'UCAYALI') & (gdf['OBJECTID_1'].isin([10, 11])))]
REG = ['JEQUETEPEQUE-ZARUMILLA','HUARMEY-CHICAMA','MARAÑÓN','HUALLAGA','AMAZONAS','CAÑETE-FORTALEZA','MANTARO','CHÁPARRA-CHINCHA',
       'UCAYALI','PAMPAS-APURIMAC','URUBAMBA-VILCANOTA','MADRE DE DIOS','CAPLINA-OCOÑA','TITICACA']
ts = {d: Z.rio.clip(gdf[gdf['NAME_AAA'] == d].geometry, gdf.crs, drop=True).mean(dim=['lat', 'lon']).to_series() for d in REG}
Zd = pd.DataFrame(ts).sort_index()
ec = pd.read_csv(os.path.join(BASE, "data/enso/ecindex_ersstv5.csv"), parse_dates=['time']).set_index('time').sort_index()
ci = ec.index.intersection(Zd.index); ec = ec.loc[ci]; Zd = Zd.loc[ci]
E, C = ec.E_index.values, ec.C_index.values; idx = Zd.index
NORTH = [REG.index(d) for d in ['JEQUETEPEQUE-ZARUMILLA', 'HUARMEY-CHICAMA']]
SOUTH = [REG.index(d) for d in ['PAMPAS-APURIMAC', 'URUBAMBA-VILCANOTA', 'CAPLINA-OCOÑA', 'TITICACA']]
neutral = (np.abs(E) < 0.5) & (np.abs(C) < 0.5)
masks = {'El Nino E': (E >= 1.0) & (C < 1.0), 'El Nino C': (C >= 0.5) & (E < 0.5), 'La Nina C': C <= -1.0,
         'Cold E (E<=-1, C>-1)': (E <= -1.0) & (C > -1.0)}
def runs(m):
    m = m.astype(int); return int(((m[1:] == 1) & (m[:-1] == 0)).sum() + (m[0] == 1))
gap = (idx >= '2017-07-01') & (idx <= '2018-05-31'); late = idx >= '2022-10-01'
info = pd.DataFrame([dict(regime=k, months=int(m.sum()), episodes=runs(m), months_in_GRACE_gap=int((m & gap).sum()),
                          months_from_2022_10=int((m & late).sum())) for k, m in masks.items()])
info.loc[len(info)] = dict(regime='Neutral', months=int(neutral.sum()), episodes=runs(neutral), months_in_GRACE_gap=int((neutral & gap).sum()),
                           months_from_2022_10=int((neutral & late).sum()))
info.to_csv(os.path.join(OUT, 'composite_regime_inventory.csv'), index=False); print(info)
names = REG + ['NORTE', 'SUR', 'N-S']
def test(Zv, mr, mn):
    G = np.column_stack([Zv[:, NORTH].mean(1), Zv[:, SOUTH].mean(1)])
    Y = np.column_stack([Zv, G, G[:, 0] - G[:, 1]])
    f = lambda A: A[mr].mean(0) - A[mn].mean(0)
    obs = f(Y); null = np.array([f(np.roll(Y, k, axis=0)) for k in range(1, len(Y))])
    return obs, (1 + np.sum(np.abs(null) >= np.abs(obs), axis=0)) / len(Y)
def detr(A):
    t = np.arange(len(A)); return np.column_stack([A[:, j] - np.polyval(np.polyfit(t, A[:, j], 1), t) for j in range(A.shape[1])])
V = Zd.values; Vd = detr(V)
variants = {'base': (V, False), 'detrended': (Vd, False), 'without_2023_25': (V, True), 'detrended_without_2023_25': (Vd, True)}
rows = []
for vn, (Zv, drop) in variants.items():
    for rn, mr in masks.items():
        m2 = mr & ~late if drop else mr
        if m2.sum() < 3: continue
        o, p = test(Zv, m2, neutral)
        rows += [dict(variant=vn, regime=rn, unit=n, n_regime_months=int(m2.sum()), composite_pct_sigma=round(float(a), 1), p_perm=round(float(b), 4))
                 for n, a, b in zip(names, o, p)]
R = pd.DataFrame(rows)
def bh(p):
    p = np.asarray(p); k = len(p); o = np.argsort(p); q = np.empty(k); prev = 1.0
    for rank, i in zip(range(k, 0, -1), o[::-1]): prev = min(prev, p[i] * k / rank); q[i] = prev
    return q
R['q_fdr_56'] = np.nan
for vn in variants:
    s = R[(R.variant == vn) & (R.unit.isin(REG))]
    R.loc[s.index, 'q_fdr_56'] = bh(s.p_perm.values).round(4)
R.to_csv(os.path.join(OUT, 'composite_sensitivity.csv'), index=False)
pd.set_option('display.width', 220, 'display.max_rows', 400)
print(R[(R.variant == 'base') & R.unit.isin(REG)].to_string(index=False))
print(R[R.unit.isin(['NORTE', 'SUR', 'N-S'])].to_string(index=False))
