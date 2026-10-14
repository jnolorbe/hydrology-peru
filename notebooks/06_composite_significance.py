"""Significance of the notebook-03 ENSO-regime composites (El Nino E, El Nino C, La Nina C vs neutral)
per AAA domain. Replicates notebook 03 exactly, then tests each composite with a circular-shift
permutation (preserves the temporal clustering of events; exact null from all 287 non-zero shifts),
and applies Benjamini-Hochberg FDR across 14 domains x 3 regimes."""
import os, sys
import numpy as np, pandas as pd, xarray as xr, geopandas as gpd, rioxarray  # noqa
BASE, OUT = sys.argv[1], sys.argv[2]

ds = xr.open_dataset(os.path.join(BASE, "data/processed/GRACE_Peru_final_IQR1_5.nc"))
if 'month' in ds: ds = ds.drop_vars('month')
x = ds['lwe_thickness_corrected']; x = x - x.mean('time')
x = x.rio.write_crs("EPSG:4326")
sig = x.std('time')                       # ddof=0, as notebook
Z = ((x / sig) * 100).rio.write_crs("EPSG:4326")   # % of local sigma, per pixel & month
gdf = gpd.read_file(os.path.join(BASE, "data/shapefiles/hydroAAA_domains/Autoridad_Administrativa_del_Agua.shp"))
if gdf.crs.to_epsg() != 4326: gdf = gdf.to_crs(epsg=4326)
gdf = gdf[~((gdf['NAME_AAA'] == 'UCAYALI') & (gdf['OBJECTID_1'].isin([10, 11])))]
REG = ['JEQUETEPEQUE-ZARUMILLA','HUARMEY-CHICAMA','MARAÑÓN','HUALLAGA','AMAZONAS','CAÑETE-FORTALEZA','MANTARO',
       'CHÁPARRA-CHINCHA','UCAYALI','PAMPAS-APURIMAC','URUBAMBA-VILCANOTA','MADRE DE DIOS','CAPLINA-OCOÑA','TITICACA']
ts = {}
for d in REG:
    m = gdf[gdf['NAME_AAA'] == d]
    cl = Z.rio.clip(m.geometry, m.crs, drop=True)
    ts[d] = cl.mean(dim=['lat', 'lon']).to_series()      # linear => mean of pixel-% composites
Zd = pd.DataFrame(ts).sort_index()

ec = pd.read_csv(os.path.join(BASE, "data/enso/ecindex_ersstv5.csv"), parse_dates=['time']).set_index('time').sort_index()
common = ec.index.intersection(Zd.index)
ec = ec.loc[common]; Zd = Zd.loc[common]
E, C = ec['E_index'], ec['C_index']
masks = {
    'El Nino E':  ((E >= 1.0) & (C < 1.0)).values,
    'El Nino C':  ((C >= 0.5) & (E < 0.5)).values,
    'La Nina C':  (C <= -1.0).values,
}
neutral = ((E.abs() < 0.5) & (C.abs() < 0.5)).values
n = len(Zd)
def runs(m):
    m = m.astype(int); return int(((m[1:] == 1) & (m[:-1] == 0)).sum() + (m[0] == 1))
info = {k: dict(months=int(v.sum()), events=runs(v)) for k, v in masks.items()}
info['Neutral'] = dict(months=int(neutral.sum()), events=runs(neutral))
print("n months:", n, "| range", Zd.index[0].date(), Zd.index[-1].date()); print(info)

def stat(Zv, mr, mn):  # Zv: (n, ndomains)
    return Zv[mr].mean(0) - Zv[mn].mean(0)

Zv = Zd.values
rows = []
for reg, mr in masks.items():
    obs = stat(Zv, mr, neutral)
    null = np.array([stat(np.roll(Zv, k, axis=0), mr, neutral) for k in range(1, n)])  # (n-1, nd)
    for j, d in enumerate(REG):
        p = (1 + np.sum(np.abs(null[:, j]) >= abs(obs[j]))) / (n - 1 + 1)
        rows.append(dict(regime=reg, domain=d, composite_pct_sigma=round(float(obs[j]), 1),
                         n_regime_months=info[reg]['months'], n_regime_events=info[reg]['events'],
                         null_sd=round(float(null[:, j].std()), 1), p_perm=p))
res = pd.DataFrame(rows)
def bh(p):
    p = np.asarray(p); k = len(p); o = np.argsort(p); q = np.empty(k); prev = 1.0
    for rank, i in zip(range(k, 0, -1), o[::-1]):
        prev = min(prev, p[i]*k/rank); q[i] = prev
    return q
res['q_fdr'] = bh(res['p_perm'].values)
res['signif_05'] = res['p_perm'] < 0.05
res['signif_fdr10'] = res['q_fdr'] < 0.10
res.to_csv(OUT, index=False, float_format='%.4g')
pd.set_option('display.width', 220, 'display.max_rows', 100)
print(res.to_string(index=False))
for r in masks:
    s = res[res.regime == r]; print(r, 'p<0.05:', int(s.signif_05.sum()), '/14 | FDR<0.10:', int(s.signif_fdr10.sum()), '/14')

# ---------- dipole contrast: single pre-specified North-minus-South test ----------
NORTH = ['JEQUETEPEQUE-ZARUMILLA', 'HUARMEY-CHICAMA']
SOUTH = ['PAMPAS-APURIMAC', 'URUBAMBA-VILCANOTA', 'CAPLINA-OCOÑA', 'TITICACA']
iN = [REG.index(d) for d in NORTH]; iS = [REG.index(d) for d in SOUTH]
def contrast(Zv_):
    return Zv_[:, iN].mean(1) - Zv_[:, iS].mean(1)
crow = []
for reg, mr in masks.items():
    obs = stat(contrast(Zv)[:, None], mr, neutral)[0]
    nul = np.array([stat(contrast(np.roll(Zv, k, axis=0))[:, None], mr, neutral)[0] for k in range(1, n)])
    crow.append(dict(regime=reg, north_minus_south_pct_sigma=round(float(obs), 1),
                     north_mean=round(float(stat(Zv[:, iN].mean(1)[:, None], mr, neutral)[0]), 1),
                     south_mean=round(float(stat(Zv[:, iS].mean(1)[:, None], mr, neutral)[0]), 1),
                     null_sd=round(float(nul.std()), 1),
                     p_perm_two_sided=(1 + np.sum(np.abs(nul) >= abs(obs))) / n,
                     p_perm_one_sided_positive=(1 + np.sum(nul >= obs)) / n))
cdf = pd.DataFrame(crow); print("\nDIPOLE CONTRAST (North = Jequetepeque-Zarumilla+Huarmey-Chicama; South = Pampas-Apurimac+Urubamba+Caplina+Titicaca)")
print(cdf.to_string(index=False)); cdf.to_csv(OUT.replace('.csv', '_dipole.csv'), index=False, float_format='%.4g')
