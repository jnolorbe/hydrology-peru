"""Análisis por eventos ENOS del TWS (GRACE JPL mascon RL06.3Mv04) en los 14 ámbitos de la ANA (tesis v13, Sección 3.6.9).

Series por ámbito como en el cuaderno 02: media de las celdas cuyo centro cae en el polígono (polígono mayor
en Ucayali), anomalía centrada, media móvil centrada de 3 meses y descomposición aditiva (periodo 12);
D = tendencia + residuo (serie desestacionalizada, cm).

Ventanas de evento definidas por los índices, no por el TWS:
  El Niño 2009-10 y 2015-16 (eventos de cuenca)  : bloque contiguo de meses con ONI >= +0.5
  La Niña 2010-12                                 : bloque contiguo con ONI <= -0.5 (se unen interrupciones <= 3 meses)
  El Niño costero 2017 y 2023-24                  : bloque contiguo con ICEN >= +0.4 (criterio del ENFEN)

Métrica: cambio del almacenamiento durante el evento,
  dS = media de D en los 3 últimos meses de la ventana - media de D en los 3 meses previos al inicio  [cm]
  en Gt: dS * área (1 cm sobre 1 km2 = 1e-5 Gt).
Contexto descriptivo (no es una prueba de hipótesis): percentil de dS entre todas las ventanas de igual
duración del período 2002-2025. Variante sin tendencia lineal de D (los percentiles no cambian, porque una
tendencia lineal desplaza por igual a todas las ventanas de la misma duración).
Caracterización del tipo de evento: extremos de los índices E y C (Takahashi et al., 2011; ERSSTv5) en cada ventana.
Sensibilidad: ventanas definidas con E y C (umbral 0.5, y umbrales de los regímenes de la tesis); se reporta la
correlación entre ámbitos con los cambios de las ventanas ONI/ICEN y el número de ámbitos con el mismo signo.
Uso: python 09_event_analysis.py <repo_root> <out_dir>
"""
import os, sys, warnings
import numpy as np, pandas as pd, xarray as xr, geopandas as gpd
from statsmodels.tsa.seasonal import seasonal_decompose
warnings.filterwarnings('ignore')

BASE, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
ORDER = ['JEQUETEPEQUE-ZARUMILLA', 'HUARMEY-CHICAMA', 'MARAÑÓN', 'HUALLAGA', 'AMAZONAS', 'CAÑETE-FORTALEZA',
         'MANTARO', 'CHÁPARRA-CHINCHA', 'UCAYALI', 'PAMPAS-APURIMAC', 'URUBAMBA-VILCANOTA', 'MADRE DE DIOS',
         'CAPLINA-OCOÑA', 'TITICACA']

# ---------- series por ámbito ----------
ds = xr.open_dataset(os.path.join(BASE, 'data/processed/GRACE_Peru_final_IQR1_5.nc'))
tws = ds['lwe_thickness_corrected']; tws = tws - tws.mean('time')
gdf = gpd.read_file(os.path.join(BASE, 'data/shapefiles/hydroAAA_domains/Autoridad_Administrativa_del_Agua.shp')).to_crs(4326)
gdf = gdf.sort_values('Shape_Area', ascending=False).drop_duplicates('NAME_AAA')
lon, lat = np.meshgrid(tws.lon.values, tws.lat.values)
pts = gpd.GeoDataFrame({'iy': np.repeat(np.arange(len(tws.lat)), len(tws.lon)),
                        'ix': np.tile(np.arange(len(tws.lon)), len(tws.lat))},
                       geometry=gpd.points_from_xy(lon.ravel(), lat.ravel()), crs=4326)
j = gpd.sjoin(pts, gdf[['NAME_AAA', 'geometry']], predicate='within')
area = gdf.set_index('NAME_AAA')['AREA_KM2']
arr = tws.values
raw = pd.DataFrame({d: np.nanmean(arr[:, g.iy.values, g.ix.values], axis=1) for d, g in j.groupby('NAME_AAA')},
                   index=pd.to_datetime(tws.time.values))[ORDER]
sm = raw.rolling(3, center=True).mean().dropna()
D = pd.DataFrame({d: (lambda r: r.trend + r.resid)(seasonal_decompose(sm[d], model='additive', period=12,
                                                                         extrapolate_trend='freq')) for d in ORDER})
x = np.arange(len(D))
Dd = D.apply(lambda c: c - np.polyval(np.polyfit(x, c.values, 1), x))

# ---------- índices y ventanas ----------
rd = lambda f: pd.read_csv(os.path.join(BASE, 'data/enso', f), parse_dates=['time']).set_index('time')
idx = rd('oni_2002_2025.csv')[['oni']].join(rd('icen_2002_2025.csv')).join(rd('ecindex_ersstv5.csv')).reindex(D.index)
rawnc = xr.open_dataset(os.path.join(BASE, 'data/raw/GRCTellus.JPL.200204_202511.GLO.RL06.3M.MSCNv04CRI.nc'))
obs = set(pd.to_datetime(rawnc.time.values).to_period('M'))
imputed = pd.Series([p not in obs for p in D.index.to_period('M')], index=D.index)

def window(cond, near, maxgap=0):
    c = cond.copy()
    if maxgap:
        runs = (c != c.shift()).cumsum()
        for _, g in c.groupby(runs):
            if not g.iloc[0] and len(g) <= maxgap and g.index[0] > c.index[0] and g.index[-1] < c.index[-1]:
                c.loc[g.index] = True
    runs = (c != c.shift()).cumsum()
    w = c[runs == runs.loc[pd.Timestamp(near)]]
    assert w.all(), near
    return w.index[0], w.index[-1]

EV = {'El Niño 2009–10': window(idx.oni >= 0.5, '2009-12-01'),
      'La Niña 2010–12': window(idx.oni <= -0.5, '2010-12-01', maxgap=3),
      'El Niño 2015–16': window(idx.oni >= 0.5, '2015-12-01'),
      'El Niño costero 2017': window(idx.icen >= 0.4, '2017-03-01'),
      'El Niño costero 2023–24': window(idx.icen >= 0.4, '2023-06-01')}

# ---------- cambio durante el evento y percentil ----------
rows, wins = [], []
for ev, (a0, b0) in EV.items():
    a, b = D.index.get_loc(a0), D.index.get_loc(b0); L = b - a + 1
    sub = idx.iloc[a:b + 1]
    wins.append(dict(evento=ev, inicio=a0.strftime('%Y-%m'), fin=b0.strftime('%Y-%m'), meses=L,
                     imputados=int(imputed.iloc[a:b + 1].sum()),
                     E_max=sub.E_index.max(), E_min=sub.E_index.min(), C_max=sub.C_index.max(), C_min=sub.C_index.min()))
    for tag, X in [('base', D), ('sin_tendencia', Dd)]:
        dS = X.iloc[b - 2:b + 1].mean() - X.iloc[a - 3:a].mean()
        allc = np.array([(X.iloc[k + L - 3:k + L].mean() - X.iloc[k - 3:k].mean()).values
                         for k in range(3, len(X) - L + 1)])
        for i, dom in enumerate(ORDER):
            rows.append(dict(evento=ev, variante=tag, ambito=dom, dS_cm=dS[dom], dS_Gt=dS[dom] * area[dom] * 1e-5,
                             percentil=(allc[:, i] <= dS[dom]).mean() * 100))
res = pd.DataFrame(rows)
pd.DataFrame(wins).to_csv(os.path.join(OUT, 'event_windows.csv'), index=False)
res.to_csv(os.path.join(OUT, 'event_change.csv'), index=False)
D.to_csv(os.path.join(OUT, 'tws_deseasonalized_by_domain.csv'))
print(pd.DataFrame(wins).round(2).to_string(index=False))

# ---------- sensibilidad: ventanas definidas con E y C ----------
E, C = idx.E_index, idx.C_index
def safe(cond, near, maxgap=0):
    try: return window(cond, near, maxgap)
    except (AssertionError, KeyError): return None
VAR = {'EC_0.5': {'El Niño 2009–10': safe(C >= 0.5, '2009-12-01', 1), 'La Niña 2010–12': safe(C <= -0.5, '2010-12-01', 3),
                  'El Niño 2015–16': safe((E >= 0.5) | (C >= 0.5), '2015-12-01', 1),
                  'El Niño costero 2017': safe(E >= 0.5, '2017-03-01'), 'El Niño costero 2023–24': safe(E >= 0.5, '2023-10-01', 1)},
       'EC_regimen': {'El Niño 2009–10': safe(C >= 0.5, '2009-12-01', 1), 'La Niña 2010–12': safe(C <= -1.0, '2010-12-01', 3),
                      'El Niño 2015–16': safe(E >= 1.0, '2015-12-01', 1),
                      'El Niño costero 2017': safe(E >= 1.0, '2017-03-01'), 'El Niño costero 2023–24': safe(E >= 1.0, '2023-10-01', 1)}}
ref = res[res.variante == 'sin_tendencia'].pivot(index='ambito', columns='evento', values='dS_cm').loc[ORDER]
sens = []
for vname, evs in VAR.items():
    for ev, w in evs.items():
        if w is None:
            sens.append(dict(variante=vname, evento=ev, ventana='no detectado')); continue
        a, b = D.index.get_loc(w[0]), D.index.get_loc(w[1])
        dS = Dd.iloc[b - 2:b + 1].mean() - Dd.iloc[a - 3:a].mean()
        r0 = ref[ev]
        same = ((np.sign(dS) == np.sign(r0)) | ((dS.abs() < 1) & (r0.abs() < 1))).sum()
        sens.append(dict(variante=vname, evento=ev, ventana=f"{w[0]:%Y-%m}/{w[1]:%Y-%m}",
                         r=np.corrcoef(dS, r0)[0, 1], mismo_signo=int(same)))
sens = pd.DataFrame(sens); sens.to_csv(os.path.join(OUT, 'event_sensitivity_EC.csv'), index=False)
print(sens.round(2).to_string(index=False))
print(res[res.variante == 'sin_tendencia'].pivot(index='ambito', columns='evento', values='dS_cm').loc[ORDER, list(EV)].round(1))
print(res.groupby(['variante', 'evento'], sort=False).dS_Gt.sum().round(1).unstack()[list(EV)])
