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


import warnings; warnings.filterwarnings('ignore')
rng=np.random.default_rng(3)
oni = pd.read_csv(os.path.join(BASE,"data/enso/oni_2002_2025.csv"), index_col='time', parse_dates=True).iloc[:,0]
lags=np.arange(-12,13)
def curve(a,b):
    n=len(a); o=[]
    for L in lags:
        x,y=(a[:n-L],b[L:]) if L>=0 else (a[-L:],b[:n+L]); o.append(np.corrcoef(x,y)[0,1])
    return np.array(o)
def surr(y,ns):
    n=len(y); yc=y-y.mean(); F=np.fft.rfft(yc); ph=rng.uniform(0,2*np.pi,(ns,len(F))); ph[:,0]=0
    if n%2==0: ph[:,-1]=0
    return np.fft.irfft(np.abs(F)*np.exp(1j*ph),n=n,axis=1)
def ar1(x): x=x-x.mean(); return float(np.sum(x[1:]*x[:-1])/np.sum(x*x))
ORDER=['JEQUETEPEQUE-ZARUMILLA','HUARMEY-CHICAMA','MARAÑÓN','HUALLAGA','AMAZONAS','CAÑETE-FORTALEZA','MANTARO','CHÁPARRA-CHINCHA','UCAYALI','PAMPAS-APURIMAC','URUBAMBA-VILCANOTA','MADRE DE DIOS','CAPLINA-OCOÑA','TITICACA']
Ts={}
for c in ORDER:
    d=seasonal_decompose(clean[c],model='additive',period=12,extrapolate_trend='freq'); Ts[c]=d.trend
Ts=pd.DataFrame(Ts)
for lab,(a,b) in [('2002-04..2016-12 (window of v12)',('2002-04','2016-12')),('2002-01..2025-12 (full)',('2002-01','2025-12'))]:
    print("\n=== trend component T (3MA) vs raw ONI,",lab)
    rows=[]
    for c in ORDER:
        d=pd.concat([oni.rename('o'),Ts[c].rename('t')],axis=1).loc[a:b].dropna()
        x=d.o.values; y=d.t.values; cu=curve(x,y); k=int(np.argmax(np.abs(cu))); r=cu[k]
        S=surr(y,1500); mx=np.array([np.max(np.abs(curve(x,s))) for s in S]); p=(1+np.sum(mx>=abs(r)))/(len(mx)+1)
        rx,ry=ar1(x),ar1(y); neff=len(x)*(1-rx*ry)/(1+rx*ry)
        rows.append((c,int(lags[k]),round(r,2),len(x),round(neff,1),round(p,3)))
    R=pd.DataFrame(rows,columns=['dom','peak_lag','r','n','n_eff','p_surrogate'])
    print(R.to_string(index=False)); print("lag range:",R.peak_lag.min(),R.peak_lag.max(),"| n lag<=-5:",int((R.peak_lag<=-5).sum()),"/14 | p<0.05:",int((R.p_surrogate<0.05).sum()),"/14 | median n_eff", R.n_eff.median())
