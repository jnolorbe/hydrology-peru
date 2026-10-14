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


# ================= sequence test =================
rng = np.random.default_rng(7)
lags = np.arange(-12, 13)
def curve(a, b):   # corr(a(t), b(t+L)), a,b aligned arrays
    n = len(a); out = np.empty(len(lags))
    for k, L in enumerate(lags):
        if L >= 0: x, y = a[:n-L], b[L:]
        else:      x, y = a[-L:], b[:n+L]
        out[k] = np.corrcoef(x, y)[0, 1]
    return out
def peak(c): k = int(np.nanargmax(c)); return int(lags[k]), c[k]
def width(c, frac=0.9):
    k = int(np.nanargmax(c)); ok = lags[c >= frac*c[k]]; return int(ok.min()), int(ok.max())
def blocks(n, L=12):
    idx = []; 
    while len(idx) < n:
        s = rng.integers(0, n); idx.extend([(s+j) % n for j in range(L)])
    return np.array(idx[:n])

# common aligned frame: ONI, ICEN, C, E (standardised, as notebook) and TWS (std over full) 
df = pd.concat([idx_series['ONI'].rename('ONI'), idx_series['ICEN'].rename('ICEN'),
                idx_series['C'].rename('C'), idx_series['E'].rename('E')], axis=1)
common2 = df.dropna().index.intersection(tws_std.index)
df = df.loc[common2]
T = tws_std.loc[common2]
T['NORTH'] = (T['JEQUETEPEQUE-ZARUMILLA'] + T['HUARMEY-CHICAMA'])/2
print('n months', len(df), df.index[0].date(), df.index[-1].date())

print('\n== index-index lags (corr(A(t),B(t+L)); L>0 => B lags A) ==')
pairs = [('ICEN','ONI'), ('E','ONI'), ('E','C'), ('ICEN','C'), ('ICEN','E')]
NB = 2000
res = {}
for a, b in pairs:
    x, y = df[a].values, df[b].values; c = curve(x, y); p, r = peak(c)
    bl = [peak(curve(x[i], y[i]))[0] for i in (blocks(len(x)) for _ in range(NB))]
    print(f"{a}->{b}: peak lag {p:+d} r={r:.2f}; 0.9-width {width(c)}; boot lag 5-50-95%:", np.percentile(bl,[5,50,95]))

print('\n== TWS vs index: peak, width, bootstrap lag CI; r at lag 0 and at positive lags ==')
doms = ['HUALLAGA','MARAÑÓN','AMAZONAS','HUARMEY-CHICAMA','JEQUETEPEQUE-ZARUMILLA','NORTH']
rows = []
for d in doms:
    for ix in ['ICEN','ONI','E','C']:
        x, y = df[ix].values, T[d].values; c = curve(x, y); p, r = peak(c)
        bl = []
        for _ in range(NB):
            i = blocks(len(x)); bl.append(peak(curve(x[i], y[i]))[0])
        i0 = list(lags).index(0)
        rows.append(dict(dom=d, idx=ix, peak=p, r=round(r,2), width=width(c), lag_p5_p50_p95=tuple(np.percentile(bl,[5,50,95]).astype(int)),
                         r0=round(c[i0],2), rmax_pos=round(np.nanmax(c[i0+1:]),2), lag_pos=int(lags[i0+1+int(np.nanargmax(c[i0+1:]))])))
R = pd.DataFrame(rows); pd.set_option('display.width',250,'display.max_rows',100)
print(R.to_string(index=False))

print('\n== additivity: lag(TWS,ONI) vs lag(TWS,ICEN)+lag(ICEN,ONI), block-bootstrap of the difference ==')
for d in ['HUALLAGA','MARAÑÓN','AMAZONAS','NORTH']:
    diffs = []
    for _ in range(NB):
        i = blocks(len(df))
        lo = peak(curve(df['ONI'].values[i], T[d].values[i]))[0]
        li = peak(curve(df['ICEN'].values[i], T[d].values[i]))[0]
        io = peak(curve(df['ICEN'].values[i], df['ONI'].values[i]))[0]
        # lag(ICEN->TWS)=li ; lag(ICEN->ONI)=io ; sequence ICEN->TWS->ONI requires lag(TWS->ONI) = io - li >0
        diffs.append((lo, li, io))
    a = np.array(diffs)
    print(d, 'P(TWS leads ONI i.e. lag<0)=%.2f' % np.mean(a[:,0]<0),
          '| P(TWS lags ICEN i.e. lag(ICEN->TWS)>=+1)=%.2f' % np.mean(a[:,1]>=1),
          '| P(TWS strictly between: ICEN leads TWS by>=1 and TWS leads ONI)= %.2f' % np.mean((a[:,1]>=1)&(a[:,0]<0)))
