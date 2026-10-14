"""Significance of the notebook-03 ENSO-regime composites (El Nino E, El Nino C, La Nina C vs neutral)
per AAA domain. Replicates notebook 03 exactly, then tests each composite with a circular-shift
permutation (preserves the temporal clustering of events; exact null from all 287 non-zero shifts),
and applies Benjamini-Hochberg FDR across 14 domains x 3 regimes."""
import os, sys
import numpy as np, pandas as pd, xarray as xr, geopandas as gpd, rioxarray  # noqa
BASE="/mnt/user-data/uploads/hydrology-peru"

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

import warnings; warnings.filterwarnings('ignore')
NORTH = ['JEQUETEPEQUE-ZARUMILLA', 'HUARMEY-CHICAMA']
SOUTH = ['PAMPAS-APURIMAC', 'URUBAMBA-VILCANOTA', 'CAPLINA-OCOÑA', 'TITICACA']
iN = [REG.index(d) for d in NORTH]; iS = [REG.index(d) for d in SOUTH]
def contrast_series(Zv_): return Zv_[:, iN].mean(1) - Zv_[:, iS].mean(1)
cs = contrast_series(Zv)
def test(mr, label):
    mr = np.asarray(mr); mn = neutral
    if mr.sum() < 2: print(label, 'n<2'); return
    obs = cs[mr].mean() - cs[mn].mean()
    nul = np.array([ (np.roll(cs,k)[mr].mean() - np.roll(cs,k)[mn].mean()) for k in range(1,n)])
    p = (1+np.sum(np.abs(nul)>=abs(obs)))/n
    nm = Zv[:, iN][mr].mean() - Zv[:, iN][mn].mean(); sm = Zv[:, iS][mr].mean() - Zv[:, iS][mn].mean()
    print(f"{label:55s} months={int(mr.sum()):3d} events={runs(mr)} north={Zv[mr][:,iN].mean()-Zv[mn][:,iN].mean():7.1f} south={Zv[mr][:,iS].mean()-Zv[mn][:,iS].mean():7.1f} contrast={obs:7.1f} p2={p:.3f}")
Ev, Cv = E.values, C.values
print("-- threshold sensitivity (C<1.0 as in notebook) --")
for th in [0.5, 0.7, 0.8, 0.9, 1.0, 1.2]:
    test((Ev>=th)&(Cv<1.0), f"E>={th}")
print("-- exclude months that are also La Nina C (C<=-1.0) --")
for th in [0.7, 0.8, 1.0]:
    test((Ev>=th)&(Cv<1.0)&(Cv>-1.0), f"E>={th} & -1<C<1.0")
print("-- leave-one-episode-out at E>=1.0 --")
base = (Ev>=1.0)&(Cv<1.0)
idx = np.where(base)[0]; groups=[]; cur=[idx[0]]
for i in idx[1:]:
    if i-cur[-1]==1: cur.append(i)
    else: groups.append(cur); cur=[i]
groups.append(cur)
for g in groups:
    m = base.copy(); m[g]=False
    test(m, f"without episode starting {Zd.index[g[0]]:%Y-%m}")
print("-- 2017 months directly (Jan-Apr 2017) and episode lists --")
ti = [Zd.index.get_loc(pd.Timestamp(f'2017-0{k}-01')) for k in (1,2,3,4)]
print("north z contrast Jan-Apr 2017 mean: north=%.1f south=%.1f" % (Zv[ti][:,iN].mean()-Zv[neutral][:,iN].mean(), Zv[ti][:,iS].mean()-Zv[neutral][:,iS].mean()))
