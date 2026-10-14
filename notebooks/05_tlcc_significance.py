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

BASE = sys.argv[1]
OUT = sys.argv[2]
NSUR = int(sys.argv[3]) if len(sys.argv) > 3 else 5000
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

# ---------- helpers ----------
def tlcc(x, y, lags):
    """corr(x(t), y(t+lag)) with pairwise-complete obs (same as notebook: x.corr(y.shift(-lag)))."""
    out, ns = [], []
    for L in lags:
        s = y.shift(-L)
        m = x.notna() & s.notna()
        ns.append(int(m.sum()))
        out.append(np.corrcoef(x[m], s[m])[0, 1] if m.sum() > 3 else np.nan)
    return np.array(out), np.array(ns)

def lagcorr_arrays(x, y, lags):
    n = len(x); out = np.empty(len(lags))
    for k, L in enumerate(lags):
        if L >= 0: a, b = x[:n-L], y[L:]
        else:      a, b = x[-L:], y[:n+L]
        out[k] = np.corrcoef(a, b)[0, 1]
    return out

def phase_surrogates(y, nsur):
    n = len(y); yc = y - y.mean()
    F = np.fft.rfft(yc)
    amp = np.abs(F)
    ph = rng.uniform(0, 2*np.pi, size=(nsur, len(F)))
    ph[:, 0] = 0
    if n % 2 == 0: ph[:, -1] = 0
    S = np.fft.irfft(amp * np.exp(1j*ph), n=n, axis=1)
    return S

def ar1(x):
    x = x - x.mean()
    return float(np.sum(x[1:]*x[:-1]) / np.sum(x*x))

def bh(p):
    p = np.asarray(p); n = len(p); o = np.argsort(p); q = np.empty(n)
    prev = 1.0
    for rank, i in zip(range(n, 0, -1), o[::-1]):
        prev = min(prev, p[i]*n/rank); q[i] = prev
    return q

lags = np.arange(-MAX_LAG, MAX_LAG+1)
rows = []
fullcurves = []
for name, xs in idx_series.items():
    T = tws_std_ce if name in ('C', 'E') else tws_std
    for dom in avail:
        y = T[dom]
        r, ns = tlcc(xs, y, lags)
        kpk = int(np.nanargmax(np.abs(r)))
        rk, Lk, nk = r[kpk], int(lags[kpk]), int(ns[kpk])
        # contiguous aligned arrays for surrogate test
        d = pd.concat([xs.rename('x'), y.rename('y')], axis=1).dropna()
        xa, ya = d['x'].values, d['y'].values
        robs = lagcorr_arrays(xa, ya, lags)
        S = phase_surrogates(ya, NSUR)
        mx = np.empty(NSUR)
        for s in range(NSUR):
            mx[s] = np.nanmax(np.abs(lagcorr_arrays(xa, S[s], lags)))
        psur = (1 + np.sum(mx >= np.nanmax(np.abs(robs)))) / (NSUR + 1)
        # effective dof t-test at the peak lag
        rx, ry = ar1(xa), ar1(ya)
        neff = max(4.0, nk * (1 - rx*ry) / (1 + rx*ry))
        t = rk*np.sqrt((neff-2)/(1-rk**2))
        pn = 2*stats.t.sf(abs(t), neff-2)
        tcrit = stats.t.ppf(0.975, neff-2); rcrit = tcrit/np.sqrt(neff-2+tcrit**2)
        pclas = 2*stats.t.sf(abs(rk*np.sqrt((nk-2)/(1-rk**2))), nk-2)
        rows.append(dict(index=name, domain=dom, peak_lag=Lk, peak_r=round(rk, 3), n_pairs=nk,
                         ar1_index=round(rx, 3), ar1_tws=round(ry, 3), n_eff=round(neff, 1),
                         r_crit_neff_05=round(rcrit, 3), p_classic=pclas, p_neff=pn, p_surrogate=psur))
        fullcurves.append(pd.Series(r, index=lags, name=f"{name}|{dom}"))
res = pd.DataFrame(rows)
res['q_fdr_surrogate'] = bh(res['p_surrogate'].values)
res['q_fdr_neff'] = bh(res['p_neff'].values)
res['signif_classic_05'] = res['p_classic'] < 0.05
res['signif_neff_05'] = res['p_neff'] < 0.05
res['signif_surrogate_05'] = res['p_surrogate'] < 0.05
res['signif_surrogate_fdr10'] = res['q_fdr_surrogate'] < 0.10
res.to_csv(OUT, index=False, float_format='%.4g')
pd.concat(fullcurves, axis=1).T.to_csv(OUT.replace('.csv', '_curves.csv'), float_format='%.4f')
pd.set_option('display.width', 250, 'display.max_rows', 100)
print(res[['index','domain','peak_lag','peak_r','n_pairs','n_eff','r_crit_neff_05','p_classic','p_neff','p_surrogate','q_fdr_surrogate']].to_string(index=False))
print("\nSummary:")
for k in ['signif_classic_05','signif_neff_05','signif_surrogate_05','signif_surrogate_fdr10']:
    print(k, int(res[k].sum()), '/', len(res))
