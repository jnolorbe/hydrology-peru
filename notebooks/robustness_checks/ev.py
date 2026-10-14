"""TLCC significance for TWS (14 AAA domains) vs ONI, ICEN, C, E.
Replicates notebook 02 series construction exactly, then adds:
  (a) t-test with effective degrees of freedom (Bretherton et al. 1999, AR1 approx.)
  (b) phase-randomised surrogate test on the PEAK |r| over lags (handles autocorrelation
      AND the lag search at once)
  (c) Benjamini-Hochberg FDR across the 14 x 4 = 56 peak tests
"""
import os, sys, json
import numpy as np, pandas as pd, xarray as xr, geopandas as gpd, rioxarray  # noqa
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.preprocessing import StandardScaler
from scipy import stats

BASE = "/mnt/user-data/uploads/hydrology-peru"
OUT = "x"
NSUR=0
MAX_LAG = 12
rng = np.random.default_rng(20251011)

# ---------- TWS by domain (as notebook 02) ----------
ds = xr.open_dataset(os.path.join(BASE, "data/processed/GRACE_Peru_final_IQR1_5.nc"))
if 'month' in ds: ds = ds.drop_vars('month')
da = ds['lwe_thickness_corrected']
da = da - da.mean('time')
da = da.rio.write_crs("EPSG:4326")
gdf = gpd.read_file(os.path.join(BASE, "data/shapefiles/hydroAAA_domains/Autoridad_Administrativa_del_Agua.shp"))
if gdf.crs.to_epsg() != 4326: gdf = gdf.to_crs(epsg=4326)
ts = {}
for code in sorted(gdf['CODE_AAA'].unique()):
    g = gdf[gdf['CODE_AAA'] == code].copy()
    g['a'] = g.geometry.area
    m = g.sort_values('a', ascending=False).iloc[[0]]
    cl = da.rio.clip(m.geometry, m.crs, drop=True, all_touched=False)
    ts[m['NAME_AAA'].iloc[0]] = cl.mean(dim=['lat', 'lon']).to_series()
df = pd.DataFrame(ts); df.index.name = 'Date'; df.sort_index(inplace=True)
df = df.rolling(window=3, center=True, min_periods=2).mean()
clean = df.dropna()
seas = {}
for c in clean.columns:
    seas[c] = seasonal_decompose(clean[c], model='additive', period=12, extrapolate_trend='freq').seasonal
df_seas = pd.DataFrame(seas)
df_des = df - df_seas
ORDER = ['JEQUETEPEQUE-ZARUMILLA','HUARMEY-CHICAMA','MARAÑÓN','HUALLAGA','AMAZONAS','CAÑETE-FORTALEZA',
         'MANTARO','CHÁPARRA-CHINCHA','UCAYALI','PAMPAS-APURIMAC','URUBAMBA-VILCANOTA','MADRE DE DIOS',
         'CAPLINA-OCOÑA','TITICACA']
avail = [d for d in ORDER if d in df_des.columns]
missing = [d for d in ORDER if d not in df_des.columns]
print("domains found:", len(avail), "missing:", missing, "| cols:", list(df_des.columns))
df_des = df_des[avail]
print("TWS span:", df_des.index.min().date(), df_des.index.max().date(), "n=", len(df_des),
      "NaN rows:", int(df_des.isna().any(axis=1).sum()))

sc = StandardScaler()
tws_std = pd.DataFrame({d: sc.fit_transform(df_des[[d]].values).ravel() for d in avail}, index=df_des.index)

# ---------- ENSO indices (as notebook 02) ----------
oni = pd.read_csv(os.path.join(BASE, "data/enso/oni_2002_2025.csv"), index_col='time', parse_dates=True)
icen = pd.read_csv(os.path.join(BASE, "data/enso/icen_2002_2025.csv"), index_col='time', parse_dates=True)
ce = pd.read_csv(os.path.join(BASE, "data/enso/ecindex_ersstv5.csv"), index_col='time', parse_dates=True)
ce = ce.interpolate(method='quadratic')
ces = ce.rolling(window=3, center=True, min_periods=2).mean().dropna()
cdes = (lambda r: (r.trend + r.resid))(seasonal_decompose(ces['C_index'], model='additive', period=12, extrapolate_trend='freq'))
edes = (lambda r: (r.trend + r.resid))(seasonal_decompose(ces['E_index'], model='additive', period=12, extrapolate_trend='freq'))
idx_series = {
    'ONI':  pd.Series(sc.fit_transform(oni[['oni']]).ravel(), index=oni.index),
    'ICEN': pd.Series(sc.fit_transform(icen[['icen']]).ravel(), index=icen.index),
}
common = cdes.index.intersection(tws_std.index)
idx_series['C'] = pd.Series(sc.fit_transform(cdes.loc[common].to_frame()).ravel(), index=common)
idx_series['E'] = pd.Series(sc.fit_transform(edes.loc[common].to_frame()).ravel(), index=common)
# NOTE: in notebook 02 the C/E TWS series are standardised over `common_idx`; replicate:
tws_std_ce = pd.DataFrame({d: sc.fit_transform(df_des.loc[common, [d]].values).ravel() for d in avail}, index=common)

DETREND = len(sys.argv) > 4 and sys.argv[4] == 'detrend'
if DETREND:
    def _dt(s):
        t = np.arange(len(s)); v = s.values.astype(float)
        v = v - np.polyval(np.polyfit(t, v, 1), t)
        return pd.Series((v - v.mean())/v.std(ddof=0), index=s.index)
    tws_std = tws_std.apply(_dt); tws_std_ce = tws_std_ce.apply(_dt)
    idx_series = {k: _dt(v) for k, v in idx_series.items()}
    print("** linear detrend applied to all series **")


import warnings; warnings.filterwarnings('ignore')
raw = pd.read_csv(os.path.join(BASE,'data/enso/ecindex_ersstv5.csv'), parse_dates=['time']).set_index('time').sort_index()
oni_r = pd.read_csv(os.path.join(BASE,'data/enso/oni_2002_2025.csv'), index_col='time', parse_dates=True).iloc[:,0]
icen_r = pd.read_csv(os.path.join(BASE,'data/enso/icen_2002_2025.csv'), index_col='time', parse_dates=True).iloc[:,0]
E, C = raw['E_index'], raw['C_index']
mask = ((E>=1.0)&(C<1.0))
idx = raw.index[mask.values]
# runs
runs=[]; cur=[idx[0]]
for t in idx[1:]:
    if (t.year*12+t.month)-(cur[-1].year*12+cur[-1].month)==1: cur.append(t)
    else: runs.append(cur); cur=[t]
runs.append(cur)
NORTHZ = (tws_std['JEQUETEPEQUE-ZARUMILLA']+tws_std['HUARMEY-CHICAMA']+tws_std['MARAÑÓN'])/3
JEQ = tws_std['JEQUETEPEQUE-ZARUMILLA']
print('El Nino E runs:', [(r[0].strftime('%Y-%m'), r[-1].strftime('%Y-%m'), len(r)) for r in runs])
def pk(s, a, b):
    w = s.loc[a:b].dropna()
    return w.idxmax().strftime('%Y-%m') if len(w) else None
rows=[]
for r in runs:
    a = r[0]-pd.DateOffset(months=8); b = r[-1]+pd.DateOffset(months=8)
    rows.append(dict(event=f"{r[0]:%Y-%m}..{r[-1]:%Y-%m}", E=pk(E,a,b), ICEN=pk(icen_r,a,b), ONI=pk(oni_r,a,b), C=pk(C,a,b),
                     TWS_north3=pk(NORTHZ,a,b), TWS_JEQ=pk(JEQ,a,b), TWSnorth_z_at_run=round(float(NORTHZ.loc[r[0]:r[-1]].mean()),2)))
print(pd.DataFrame(rows).to_string(index=False))
