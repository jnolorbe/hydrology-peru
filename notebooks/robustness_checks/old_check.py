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
from scipy import stats as st
# ---- national series (pixels inside Peru boundary) ----
pe = gpd.GeoDataFrame(geometry=[gdf.geometry.union_all()], crs=gdf.crs)
nat = da.rio.clip(pe.geometry, pe.crs, drop=True).mean(dim=['lat','lon']).to_series()
nat.index.name='Date'; nat = nat.sort_index()
nat3 = nat.rolling(3,center=True,min_periods=2).mean()
print("NATIONAL months:", len(nat), nat.index[0].date(), nat.index[-1].date())
# FFT national
x = nat.values - nat.values.mean(); f = np.fft.rfftfreq(len(x), 1.0); P = np.abs(np.fft.rfft(x))**2
top = np.argsort(P[1:])[::-1][:4]+1
print("FFT top periods (months):", [round(1/f[i],1) for i in top], "share top:", round(P[top[0]]/P[1:].sum(),2))
# national annual means and slopes in v12 periods (annual means, calendar years)
ann = nat.groupby(nat.index.year).mean()
def slope_ann(y0,y1):
    s = ann.loc[y0:y1]; r = np.corrcoef(s.index, s.values)[0,1]; m = np.polyfit(s.index, s.values,1)[0]; return round(m,2), round(r,3), len(s)
print("national annual: 2005-2009", slope_ann(2005,2009), "| 2010-2015", slope_ann(2010,2015), "(slope cm/yr, r, n)")
print("national annual means:", ann.round(1).to_dict())
# how special are those windows? all 5-yr windows of annual means
wins=[]
for y in range(2002,2022):
    s=ann.loc[y:y+4]; 
    if len(s)==5: wins.append((y, np.corrcoef(s.index,s.values)[0,1], np.polyfit(s.index,s.values,1)[0]))
w=pd.DataFrame(wins,columns=['y0','r','m']); print("5-yr windows: share with |r|>0.9:", round((w.r.abs()>0.9).mean(),2), "| share r>0.9:", round((w.r>0.9).mean(),2), "| slopes range", w.m.min().round(2), w.m.max().round(2))
# monthly national regression in the two v12 periods + effective n
def reg(s,a,b):
    z=s.loc[a:b].dropna(); t=np.arange(len(z)); m,c=np.polyfit(t,z.values,1); r=np.corrcoef(t,z.values)[0,1]
    res=z.values-(m*t+c); r1=np.corrcoef(res[1:],res[:-1])[0,1]; neff=len(z)*(1-r1)/(1+r1)
    return round(m*12,2), round(r,3), len(z), round(neff,1)
print("national monthly 3MA regression (cm/yr, r, n, n_eff of residuals): P1 2005-07..2009-07", reg(nat3,'2005-07','2009-07'), "| P2 2010-09..2015-05", reg(nat3,'2010-09','2015-05'))

# ---- domain series, trend component, rates ----
areas = {'AMAZONAS':280658.67,'UCAYALI':232744.49,'HUALLAGA':85599.39,'MARAÑÓN':89416.23,'MADRE DE DIOS':111932.53,'JEQUETEPEQUE-ZARUMILLA':62155.67,'URUBAMBA-VILCANOTA':58734.93,'HUARMEY-CHICAMA':37109.68,'CAÑETE-FORTALEZA':39936.85,'MANTARO':34363.18,'PAMPAS-APURIMAC':64373.15,'CHÁPARRA-CHINCHA':48478.90,'TITICACA':46581.65,'CAPLINA-OCOÑA':93130.28}
old1 = {'AMAZONAS':454.8,'UCAYALI':317.2,'HUALLAGA':101.0,'MARAÑÓN':91.1,'MADRE DE DIOS':69.6,'JEQUETEPEQUE-ZARUMILLA':46.5,'URUBAMBA-VILCANOTA':38.0,'HUARMEY-CHICAMA':30.6,'CAÑETE-FORTALEZA':16.1,'MANTARO':8.4,'PAMPAS-APURIMAC':4.4,'CHÁPARRA-CHINCHA':0.7,'TITICACA':-5.1,'CAPLINA-OCOÑA':-8.9}
old2 = {'AMAZONAS':526.5,'UCAYALI':465.5,'HUALLAGA':123.3,'MARAÑÓN':100.8,'MADRE DE DIOS':271.0,'JEQUETEPEQUE-ZARUMILLA':46.2,'URUBAMBA-VILCANOTA':115.2,'HUARMEY-CHICAMA':38.6,'CAÑETE-FORTALEZA':42.1,'MANTARO':44.6,'PAMPAS-APURIMAC':104.3,'CHÁPARRA-CHINCHA':54.5,'TITICACA':85.2,'CAPLINA-OCOÑA':129.2}
rows=[]
for c in df.columns:
    d = seasonal_decompose(clean[c], model='additive', period=12, extrapolate_trend='freq')
    T = d.trend
    out={'dom':c}
    for lab,(a,b),old in [('P1',('2005-07','2009-07'),old1),('P2',('2010-09','2015-05'),old2)]:
        z=T.loc[a:b]; t=np.arange(len(z)); m=np.polyfit(t,z.values,1)[0]; r=np.corrcoef(t,z.values)[0,1]
        out[lab+'_cm_mes']=round(m,3); out[lab+'_Mt']=round(m/100*areas[c]*1e6*1/1e3*1e-3*1e3/1e3,1)  # placeholder, fixed below
        out[lab+'_Mt']=round(m*1e-2*areas[c]*1e6*1000/1e9,1)   # cm->m, km2->m2, kg/m3 ; Mt = 1e9 kg
        out[lab+'_r']=round(r,2); out[lab+'_old']=old[c]
    rows.append(out)
R=pd.DataFrame(rows); pd.set_option('display.width',250); print(R.to_string(index=False))
# ---- pairwise correlation raw(3MA) vs deseasonalised ----
cr = clean.corr().values; iu=np.triu_indices(14,1)
dd = df_des.corr().values
print("pairwise r, 3MA series incl. seasonal cycle: min/median/max", cr[iu].min().round(2), np.median(cr[iu]).round(2), cr[iu].max().round(2))
print("pairwise r, deseasonalised (trend+resid):     min/median/max", dd[iu].min().round(2), np.median(dd[iu]).round(2), dd[iu].max().round(2))
# ---- seasonal climatology timing from seasonal components ----
sc = df_seas.groupby(df_seas.index.month).mean()
print("peak month:", sc.idxmax().to_dict()); print("min month:", sc.idxmin().to_dict())
print("first positive month (onset of charge):", {c: int(next(m for m in [12,1,2,3,4,5,6] if sc.loc[m,c]>0 and sc.loc[(m-2)%12+1 if m>1 else 12,c]<=0)) if True else None for c in sc.columns})
# ---- v12 % variation baseline: Vi by phase ----
base_years=[y for y in list(range(2002,2009))+[2012,2013,2014]]
b = df[df.index.year.isin(base_years)]
Vi_rech = b[b.index.month.isin(range(1,7))].mean(); Vi_disc = b[b.index.month.isin(range(7,13))].mean()
print("Vi recharge (cm):", Vi_rech.round(2).to_dict()); print("Vi discharge (cm):", Vi_disc.round(2).to_dict())
