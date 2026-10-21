# -*- coding: utf-8 -*-
"""Funciones comunes del repositorio hydrology-peru (tesis v13).

Cada cálculo que usan los cuadernos 02 a 05 está definido aquí una sola vez:
carga de GRACE y de los índices ENOS, series por ámbito hidrográfico de la ANA,
suavizado y descomposición, clasificación en regímenes, pruebas que consideran
la autocorrelación (grados de libertad efectivos, series sustitutas, desplazamiento
circular, Benjamini–Hochberg), compuestos in situ y análisis por eventos.

Los cuadernos importan este módulo con

    import sys; sys.path.insert(0, os.path.join(REPO_NAME, 'notebooks'))
    from comun import *

Método (tesis v13, decisiones de 2026-10-19):
- Los compuestos por régimen se calculan sobre la anomalía DESESTACIONALIZADA
  (se resta la climatología mensual) y se expresan en % de su desviación estándar
  (sigma interanual), tanto con GRACE como con los registros in situ.
- Los regímenes son excluyentes: El Niño E prevalece sobre La Niña C y El Niño C
  sobre la fase fría de E (`etiquetas_regimen`).
- La versión sin desestacionalizar (método anterior) se conserva como sensibilidad
  (`desestacionalizar=False`).
Los parámetros `seleccion` (series_por_ambito) y `min_periods` (suavizar) conservan
las variantes de implementación de los scripts originales; las tres selecciones de
celdas son equivalentes.
"""
import os
import warnings

import numpy as np
import pandas as pd
import xarray as xr
import geopandas as gpd
import rioxarray  # noqa: F401  (registra el accesor .rio)
from scipy import stats
from statsmodels.tsa.seasonal import seasonal_decompose

warnings.filterwarnings('ignore', category=RuntimeWarning)
warnings.filterwarnings('ignore', message='Geometry is in a geographic CRS')
warnings.filterwarnings('ignore', message='.*extrapolate_trend.*')

# =============================================================================
# 1. Constantes
# =============================================================================
AMBITOS = ['JEQUETEPEQUE-ZARUMILLA', 'HUARMEY-CHICAMA', 'MARAÑÓN', 'HUALLAGA', 'AMAZONAS',
           'CAÑETE-FORTALEZA', 'MANTARO', 'CHÁPARRA-CHINCHA', 'UCAYALI', 'PAMPAS-APURIMAC',
           'URUBAMBA-VILCANOTA', 'MADRE DE DIOS', 'CAPLINA-OCOÑA', 'TITICACA']

NOMBRE_ES = {
    'JEQUETEPEQUE-ZARUMILLA': 'Jequetepeque-Zarumilla', 'HUARMEY-CHICAMA': 'Huarmey-Chicama',
    'CAÑETE-FORTALEZA': 'Cañete-Fortaleza', 'CHÁPARRA-CHINCHA': 'Cháparra-Chincha',
    'CAPLINA-OCOÑA': 'Caplina-Ocoña', 'MARAÑÓN': 'Marañón', 'MANTARO': 'Mantaro',
    'PAMPAS-APURIMAC': 'Pampas-Apurímac', 'TITICACA': 'Titicaca', 'UCAYALI': 'Ucayali',
    'URUBAMBA-VILCANOTA': 'Urubamba-Vilcanota', 'MADRE DE DIOS': 'Madre de Dios',
    'HUALLAGA': 'Huallaga', 'AMAZONAS': 'Amazonas'}

NORTE = ['JEQUETEPEQUE-ZARUMILLA', 'HUARMEY-CHICAMA']
SUR = ['PAMPAS-APURIMAC', 'URUBAMBA-VILCANOTA', 'CAPLINA-OCOÑA', 'TITICACA']

# Regímenes de ENOS (índices E y C de Takahashi et al., 2011). Sección 3.6.1 de la tesis.
REGIMENES = ['El Nino E', 'El Nino C', 'La Nina C', 'Cold E (E<=-1, C>-1)']
UMBRAL_NEUTRO = 0.5          # |E| < 0.5 y |C| < 0.5
UMBRAL_E_NINO = 1.0          # El Niño E: E >= 1.0 y C < 1.0
UMBRAL_C_NINO = 0.5          # El Niño C: C >= 0.5 y E < 0.5
UMBRAL_C_NINA = -1.0         # La Niña C: C <= -1.0
UMBRAL_E_FRIO = -1.0         # fase fría de E: E <= -1.0 y C > -1.0

MAX_DESFASE = 12             # correlación cruzada: desfases de -12 a +12 meses
N_SUSTITUTAS = 5000
SEMILLA = 20251011
INICIO_EPISODIO_2023_25 = '2022-10-01'
BRECHA_GRACE = ('2017-07-01', '2018-05-31')
INICIO_INSITU = '1950-01-01'

EXCLUIDOS_INSITU = {'chili_caudal_volumen.csv',            # años registrados como caudal
                    'rimac_caudal_volumen.csv',             # sin ciclo anual ni autocorrelación
                    'canete_precipitacion_climatologia.csv'}  # meses desfasados seis meses


def ruta(repo, *partes):
    """Ruta dentro del repositorio."""
    return os.path.join(repo, *partes)


# =============================================================================
# 2. GRACE y series por ámbito
# =============================================================================
def cargar_grace(repo):
    """Anomalía de TWS (cm), centrada en la media de todo el registro, por celda y mes."""
    ds = xr.open_dataset(ruta(repo, 'data/processed/GRACE_Peru_final_IQR1_5.nc'))
    if 'month' in ds:
        ds = ds.drop_vars('month')
    x = ds['lwe_thickness_corrected']
    return (x - x.mean('time')).rio.write_crs('EPSG:4326')


def porcentaje_sigma_local(x):
    """Anomalía como % de la desviación estándar temporal de cada celda (ddof = 0)."""
    return ((x / x.std('time')) * 100).rio.write_crs('EPSG:4326')


def quitar_climatologia(x):
    """Anomalía respecto de la climatología mensual: a cada mes se le resta la media de
    ese mes del calendario en todo el registro (por celda)."""
    a = x.groupby('time.month') - x.groupby('time.month').mean('time')
    return a.drop_vars('month', errors='ignore').rio.write_crs('EPSG:4326')


def campo_relativo(repo, desestacionalizar=True):
    """Campo de los compuestos: anomalía de TWS (desestacionalizada por defecto) como % de su
    desviación estándar temporal en cada celda (sigma interanual si está desestacionalizada)."""
    x = cargar_grace(repo)
    if desestacionalizar:
        x = quitar_climatologia(x)
    return porcentaje_sigma_local(x)


def cargar_ambitos(repo):
    gdf = gpd.read_file(ruta(repo, 'data/shapefiles/hydroAAA_domains/Autoridad_Administrativa_del_Agua.shp'))
    if gdf.crs.to_epsg() != 4326:
        gdf = gdf.to_crs(epsg=4326)
    return gdf


def series_por_ambito(campo, repo, seleccion='codigo'):
    """Promedio espacial mensual de `campo` en las celdas cuyo centro cae en cada ámbito.

    seleccion = 'codigo'  : polígono de mayor área de cada CODE_AAA (cuaderno 02, script 05).
                'nombre'  : polígonos de cada NAME_AAA sin los fragmentos 10 y 11 de Ucayali (scripts 06 y 07).
                'puntos'  : centros de celda dentro del polígono de mayor Shape_Area de cada NAME_AAA (script 09).
    Las tres variantes seleccionan las mismas celdas (verificado en la reestructuración).
    """
    gdf = cargar_ambitos(repo)
    ts = {}
    if seleccion == 'codigo':
        da = campo.rio.write_crs('EPSG:4326')
        for code in sorted(gdf['CODE_AAA'].unique()):
            g = gdf[gdf['CODE_AAA'] == code].copy()
            g['a'] = g.geometry.area
            m = g.sort_values('a', ascending=False).iloc[[0]]
            cl = da.rio.clip(m.geometry, m.crs, drop=True, all_touched=False)
            ts[m['NAME_AAA'].iloc[0]] = cl.mean(dim=['lat', 'lon']).to_series()
        df = pd.DataFrame(ts)
        df.index.name = 'Date'
        return df.sort_index()
    if seleccion == 'nombre':
        da = campo.rio.write_crs('EPSG:4326')
        g = gdf[~((gdf['NAME_AAA'] == 'UCAYALI') & (gdf['OBJECTID_1'].isin([10, 11])))]
        for d in AMBITOS:
            m = g[g['NAME_AAA'] == d]
            ts[d] = da.rio.clip(m.geometry, m.crs, drop=True).mean(dim=['lat', 'lon']).to_series()
        return pd.DataFrame(ts).sort_index()
    if seleccion == 'puntos':
        g = gdf.sort_values('Shape_Area', ascending=False).drop_duplicates('NAME_AAA')
        lon, lat = np.meshgrid(campo.lon.values, campo.lat.values)
        pts = gpd.GeoDataFrame({'iy': np.repeat(np.arange(len(campo.lat)), len(campo.lon)),
                                'ix': np.tile(np.arange(len(campo.lon)), len(campo.lat))},
                               geometry=gpd.points_from_xy(lon.ravel(), lat.ravel()), crs=4326)
        j = gpd.sjoin(pts, g[['NAME_AAA', 'geometry']], predicate='within')
        arr = campo.values
        return pd.DataFrame({d: np.nanmean(arr[:, gg.iy.values, gg.ix.values], axis=1)
                             for d, gg in j.groupby('NAME_AAA')},
                            index=pd.to_datetime(campo.time.values))[AMBITOS]
    raise ValueError(seleccion)


def area_ambitos_km2(repo):
    g = cargar_ambitos(repo).sort_values('Shape_Area', ascending=False).drop_duplicates('NAME_AAA')
    return g.set_index('NAME_AAA')['AREA_KM2']


# =============================================================================
# 3. Suavizado, descomposición, estandarización y tendencia
# =============================================================================
def suavizar(df, min_periods=2):
    """Media móvil centrada de 3 meses. min_periods=2 (cuaderno 02) conserva los extremos;
    min_periods=None (script 09) los deja vacíos."""
    return df.rolling(window=3, center=True, min_periods=min_periods).mean()


def descomponer(df):
    """Descomposición aditiva clásica (período 12, tendencia extrapolada en los extremos).
    Devuelve (estacional, desestacionalizada = serie - estacional = tendencia + residuo)."""
    clean = df.dropna()
    seas = pd.DataFrame({c: seasonal_decompose(clean[c], model='additive', period=12,
                                               extrapolate_trend='freq').seasonal for c in clean.columns})
    return seas, df - seas


def estandarizar(s):
    """(s - media) / desviación estándar (ddof = 0), como StandardScaler."""
    s = pd.Series(s).astype(float)
    return (s - s.mean()) / s.std(ddof=0)


def quitar_tendencia_lineal(s, reestandarizar=False):
    t = np.arange(len(s))
    v = np.asarray(s, dtype=float)
    v = v - np.polyval(np.polyfit(t, v, 1), t)
    if reestandarizar:
        v = (v - v.mean()) / v.std(ddof=0)
    return pd.Series(v, index=getattr(s, 'index', None))


def quitar_tendencia_columnas(A):
    """Tendencia lineal eliminada en cada columna de una matriz (meses x series)."""
    t = np.arange(len(A))
    return np.column_stack([A[:, j] - np.polyval(np.polyfit(t, A[:, j], 1), t) for j in range(A.shape[1])])


def series_tws_cuaderno02(repo):
    """Series por ámbito como en el cuaderno 02: anomalía centrada, promedio espacial,
    media móvil de 3 meses y descomposición. Devuelve (suavizada, estacional, desestacionalizada)."""
    df = suavizar(series_por_ambito(cargar_grace(repo), repo, 'codigo'))
    seas, des = descomponer(df)
    return df, seas, des


# =============================================================================
# 4. Índices ENOS
# =============================================================================
def cargar_oni(repo):
    return pd.read_csv(ruta(repo, 'data/enso/oni_2002_2025.csv'), index_col='time', parse_dates=True)


def cargar_icen(repo):
    return pd.read_csv(ruta(repo, 'data/enso/icen_2002_2025.csv'), index_col='time', parse_dates=True)


def cargar_ec(repo, version='v5'):
    """Índices E y C del IGP. v5: ERSSTv5 (2002-), columnas E_index, C_index.
    v6: ERSSTv6 desde 1950, columnas en minúscula e_index, c_index, fechas al primer día del mes."""
    if version == 'v5':
        return pd.read_csv(ruta(repo, 'data/enso/ecindex_ersstv5.csv'), parse_dates=['time']).set_index('time').sort_index()
    v6 = pd.read_csv(ruta(repo, 'data/enso/ecindex_ersstv6.csv'))
    v6.columns = [c.strip().lower() for c in v6.columns]
    v6['time'] = pd.to_datetime(pd.to_datetime(v6['time']).values.astype('datetime64[M]'))
    return v6.set_index('time').sort_index().loc[INICIO_INSITU:]


def ec_desestacionalizados(repo):
    """E y C para la correlación cruzada: relleno cuadrático de los meses faltantes
    (may y ago de 2024 en ERSSTv5), media móvil de 3 meses y desestacionalización."""
    ce = cargar_ec(repo, 'v5').interpolate(method='quadratic')
    ces = ce.rolling(window=3, center=True, min_periods=2).mean().dropna()
    f = lambda s: (lambda r: r.trend + r.resid)(seasonal_decompose(s, model='additive', period=12,
                                                                    extrapolate_trend='freq'))
    return f(ces['C_index']), f(ces['E_index'])


# =============================================================================
# 5. Regímenes de ENOS
# =============================================================================
def mascara_neutro(E, C):
    return (np.abs(E) < UMBRAL_NEUTRO) & (np.abs(C) < UMBRAL_NEUTRO)


def mascara_neutro_estricto(E, C, oni, icen):
    """Neutro estricto (sensibilidad): neutro E/C y además |ONI| < 0.5 y -0.7 < ICEN < +0.4,
    para excluir del comparador los calentamientos y enfriamientos costeros o de cuenca."""
    oni = np.asarray(oni); icen = np.asarray(icen)
    return mascara_neutro(E, C) & (np.abs(oni) < 0.5) & (icen < 0.4) & (icen > -0.7)


def mascaras_regimenes(E, C, prioridad=False):
    """Máscaras booleanas de los cuatro regímenes.

    prioridad=False: reglas aplicadas por separado; un mes puede caer en dos regímenes
    (E >= 1 y C <= -1: El Niño E y La Niña C; E <= -1 y C >= 0.5: fase fría de E y El Niño C).
    prioridad=True : regímenes excluyentes; El Niño E prevalece sobre La Niña C y El Niño C
    sobre la fase fría de E (equivale a `etiquetas_regimen`).
    """
    E = np.asarray(E); C = np.asarray(C)
    if prioridad:
        lab = etiquetas_regimen(E, C)
        return {r: lab == k for k, r in zip((1, 2, 3, 4), REGIMENES)}
    return {'El Nino E': (E >= UMBRAL_E_NINO) & (C < UMBRAL_E_NINO),
            'El Nino C': (C >= UMBRAL_C_NINO) & (E < UMBRAL_C_NINO),
            'La Nina C': C <= UMBRAL_C_NINA,
            'Cold E (E<=-1, C>-1)': (E <= UMBRAL_E_FRIO) & (C > UMBRAL_E_FRIO)}


def etiquetas_regimen(E, C):
    """Una etiqueta por mes: -1 sin régimen, 0 neutro, 1 El Niño E, 2 El Niño C,
    3 La Niña C, 4 fase fría de E (con prioridad: E > La Niña C; El Niño C > fase fría de E)."""
    E = np.asarray(E); C = np.asarray(C)
    lab = np.full(len(E), -1)
    lab[mascara_neutro(E, C)] = 0
    lab[C <= UMBRAL_C_NINA] = 3
    lab[(C >= UMBRAL_C_NINO) & (E < UMBRAL_C_NINO)] = 2
    lab[(E >= UMBRAL_E_NINO) & (C < UMBRAL_E_NINO)] = 1
    lab[(E <= UMBRAL_E_FRIO) & (C > UMBRAL_E_FRIO) & (lab == -1)] = 4
    return lab


def contar_episodios(m):
    """Número de bloques contiguos de meses verdaderos."""
    m = np.asarray(m).astype(int)
    return int(((m[1:] == 1) & (m[:-1] == 0)).sum() + (m[0] == 1))


# =============================================================================
# 6. Inferencia que considera la autocorrelación
# =============================================================================
def correlacion_cruzada(x, y, desfases):
    """r(l) = corr[x(t), y(t+l)] con pares completos; devuelve (r, n de pares)."""
    out, ns = [], []
    for L in desfases:
        s = y.shift(-L)
        m = x.notna() & s.notna()
        ns.append(int(m.sum()))
        out.append(np.corrcoef(x[m], s[m])[0, 1] if m.sum() > 3 else np.nan)
    return np.array(out), np.array(ns)


def correlacion_cruzada_arrays(x, y, desfases):
    n = len(x); out = np.empty(len(desfases))
    for k, L in enumerate(desfases):
        if L >= 0:
            a, b = x[:n - L], y[L:]
        else:
            a, b = x[-L:], y[:n + L]
        out[k] = np.corrcoef(a, b)[0, 1]
    return out


def sustitutas_fase(y, nsur, rng):
    """Series sustitutas con el mismo espectro de potencia y fases aleatorias (Ebisuzaki, 1997)."""
    n = len(y); F = np.fft.rfft(y - y.mean()); amp = np.abs(F)
    ph = rng.uniform(0, 2 * np.pi, size=(nsur, len(F)))
    ph[:, 0] = 0
    if n % 2 == 0:
        ph[:, -1] = 0
    return np.fft.irfft(amp * np.exp(1j * ph), n=n, axis=1)


def ar1(x):
    x = x - x.mean()
    return float(np.sum(x[1:] * x[:-1]) / np.sum(x * x))


def n_efectivo(n, rx, ry):
    """Grados de libertad efectivos (Bretherton et al., 1999): n (1 - rx ry) / (1 + rx ry), mínimo 4."""
    return max(4.0, n * (1 - rx * ry) / (1 + rx * ry))


def fdr_bh(p):
    """Valores q de Benjamini y Hochberg (1995)."""
    p = np.asarray(p); k = len(p); o = np.argsort(p); q = np.empty(k); prev = 1.0
    for rank, i in zip(range(k, 0, -1), o[::-1]):
        prev = min(prev, p[i] * k / rank); q[i] = prev
    return q


def diferencia_regimen(Y, m_reg, m_neu):
    """Compuesto: media en los meses del régimen menos media en los meses neutros (por columna)."""
    return Y[m_reg].mean(0) - Y[m_neu].mean(0)


def p_desplazamiento_circular(Y, m_reg, m_neu, desplazamientos=None):
    """Prueba bilateral por desplazamiento circular de la serie respecto de la clasificación.
    Devuelve (observado, nula, p) con p = (1 + #|nula| >= |obs|) / (n_nula + 1)."""
    Y = np.asarray(Y)
    if desplazamientos is None:
        desplazamientos = range(1, len(Y))
    obs = diferencia_regimen(Y, m_reg, m_neu)
    nula = np.array([diferencia_regimen(np.roll(Y, k, axis=0), m_reg, m_neu) for k in desplazamientos])
    p = (1 + np.sum(np.abs(nula) >= np.abs(obs), axis=0)) / (len(nula) + 1)
    return obs, nula, p


# =============================================================================
# 7. Procedimientos de la tesis (antes scripts 05 a 09)
# =============================================================================
def significancia_tlcc(repo, nsur=N_SUSTITUTAS, quitar_tendencia=False, semilla=SEMILLA):
    """Antes script 05. Máximo |r| de la correlación cruzada entre el TWS desestacionalizado
    de cada ámbito y ONI, ICEN, C y E; prueba t con grados de libertad efectivos, series
    sustitutas sobre el máximo de |r| (incorpora la búsqueda del desfase) y FDR sobre 56 pares.
    Devuelve (tabla, curvas)."""
    rng = np.random.default_rng(semilla)
    _, _, des = series_tws_cuaderno02(repo)
    avail = [d for d in AMBITOS if d in des.columns]
    des = des[avail]
    tws_std = pd.DataFrame({d: estandarizar(des[d]).values for d in avail}, index=des.index)
    oni, icen = cargar_oni(repo), cargar_icen(repo)
    cdes, edes = ec_desestacionalizados(repo)
    idx_series = {'ONI': pd.Series(estandarizar(oni['oni']).values, index=oni.index),
                  'ICEN': pd.Series(estandarizar(icen['icen']).values, index=icen.index)}
    common = cdes.index.intersection(tws_std.index)
    idx_series['C'] = pd.Series(estandarizar(cdes.loc[common]).values, index=common)
    idx_series['E'] = pd.Series(estandarizar(edes.loc[common]).values, index=common)
    tws_std_ce = pd.DataFrame({d: estandarizar(des.loc[common, d]).values for d in avail}, index=common)
    if quitar_tendencia:
        tws_std = tws_std.apply(lambda s: quitar_tendencia_lineal(s, True))
        tws_std_ce = tws_std_ce.apply(lambda s: quitar_tendencia_lineal(s, True))
        idx_series = {k: quitar_tendencia_lineal(v, True) for k, v in idx_series.items()}
    lags = np.arange(-MAX_DESFASE, MAX_DESFASE + 1)
    rows, curvas = [], []
    for name, xs in idx_series.items():
        T = tws_std_ce if name in ('C', 'E') else tws_std
        for dom in avail:
            y = T[dom]
            r, ns = correlacion_cruzada(xs, y, lags)
            k = int(np.nanargmax(np.abs(r)))
            rk, Lk, nk = r[k], int(lags[k]), int(ns[k])
            d = pd.concat([xs.rename('x'), y.rename('y')], axis=1).dropna()
            xa, ya = d['x'].values, d['y'].values
            robs = correlacion_cruzada_arrays(xa, ya, lags)
            S = sustitutas_fase(ya, nsur, rng)
            mx = np.array([np.nanmax(np.abs(correlacion_cruzada_arrays(xa, S[s], lags))) for s in range(nsur)])
            psur = (1 + np.sum(mx >= np.nanmax(np.abs(robs)))) / (nsur + 1)
            rx, ry = ar1(xa), ar1(ya)
            neff = n_efectivo(nk, rx, ry)
            t = rk * np.sqrt((neff - 2) / (1 - rk ** 2))
            pn = 2 * stats.t.sf(abs(t), neff - 2)
            tcrit = stats.t.ppf(0.975, neff - 2); rcrit = tcrit / np.sqrt(neff - 2 + tcrit ** 2)
            pclas = 2 * stats.t.sf(abs(rk * np.sqrt((nk - 2) / (1 - rk ** 2))), nk - 2)
            rows.append(dict(index=name, domain=dom, peak_lag=Lk, peak_r=round(rk, 3), n_pairs=nk,
                             ar1_index=round(rx, 3), ar1_tws=round(ry, 3), n_eff=round(neff, 1),
                             r_crit_neff_05=round(rcrit, 3), p_classic=pclas, p_neff=pn, p_surrogate=psur))
            curvas.append(pd.Series(r, index=lags, name=f"{name}|{dom}"))
    res = pd.DataFrame(rows)
    res['q_fdr_surrogate'] = fdr_bh(res['p_surrogate'].values)
    res['q_fdr_neff'] = fdr_bh(res['p_neff'].values)
    res['signif_classic_05'] = res['p_classic'] < 0.05
    res['signif_neff_05'] = res['p_neff'] < 0.05
    res['signif_surrogate_05'] = res['p_surrogate'] < 0.05
    res['signif_surrogate_fdr10'] = res['q_fdr_surrogate'] < 0.10
    return res, pd.concat(curvas, axis=1).T


def _compuestos_grace(repo, desestacionalizar=True, version='v5'):
    """Matriz (meses x 14 ámbitos) de la anomalía en % de sigma local promediada por ámbito
    y los índices E y C alineados (ERSSTv5 por defecto; 'v6' para la sensibilidad)."""
    Zd = series_por_ambito(campo_relativo(repo, desestacionalizar), repo, 'nombre')
    ec = cargar_ec(repo, version)
    ec.columns = [c.lower() for c in ec.columns]
    ci = ec.index.intersection(Zd.index)
    return Zd.loc[ci], ec.loc[ci, 'e_index'].values, ec.loc[ci, 'c_index'].values


def compuestos_grace_por_ambito(repo, desestacionalizar=True, prioridad=True, version='v5'):
    """Compuesto (% de sigma) por ámbito y régimen, sin prueba (tablas y figuras)."""
    Zd, E, C = _compuestos_grace(repo, desestacionalizar, version)
    neutral = mascara_neutro(E, C)
    masks = mascaras_regimenes(E, C, prioridad)
    return pd.DataFrame({r: pd.Series(diferencia_regimen(Zd.values, m, neutral), index=Zd.columns)
                         for r, m in masks.items()})


def significancia_compuestos(repo, regimenes=tuple(REGIMENES), prioridad=True, desestacionalizar=True):
    """Antes script 06. Compuesto por ámbito y régimen, prueba por desplazamiento circular
    (todos los desplazamientos no nulos) y FDR sobre ámbitos x regímenes (14 x 4 = 56).
    Incluye el contraste norte menos sur. Devuelve (tabla por ámbito, tabla del contraste)."""
    Zd, E, C = _compuestos_grace(repo, desestacionalizar)
    masks = {k: v for k, v in mascaras_regimenes(E, C, prioridad).items() if k in regimenes}
    neutral = mascara_neutro(E, C)
    Zv = Zd.values; n = len(Zd)
    rows = []
    for reg, mr in masks.items():
        obs, nula, p = p_desplazamiento_circular(Zv, mr, neutral)
        for j, d in enumerate(AMBITOS):
            rows.append(dict(regime=reg, domain=d, composite_pct_sigma=round(float(obs[j]), 1),
                             n_regime_months=int(mr.sum()), n_regime_events=contar_episodios(mr),
                             null_sd=round(float(nula[:, j].std()), 1), p_perm=p[j]))
    res = pd.DataFrame(rows)
    res['q_fdr'] = fdr_bh(res['p_perm'].values)
    res['signif_05'] = res['p_perm'] < 0.05
    res['signif_fdr10'] = res['q_fdr'] < 0.10
    iN = [AMBITOS.index(d) for d in NORTE]; iS = [AMBITOS.index(d) for d in SUR]
    crow = []
    for reg, mr in masks.items():
        con = (Zv[:, iN].mean(1) - Zv[:, iS].mean(1))[:, None]
        obs, nula, _ = p_desplazamiento_circular(con, mr, neutral)
        obs, nula = obs[0], nula[:, 0]
        crow.append(dict(regime=reg, north_minus_south_pct_sigma=round(float(obs), 1),
                         north_mean=round(float(diferencia_regimen(Zv[:, iN].mean(1)[:, None], mr, neutral)[0]), 1),
                         south_mean=round(float(diferencia_regimen(Zv[:, iS].mean(1)[:, None], mr, neutral)[0]), 1),
                         null_sd=round(float(nula.std()), 1),
                         p_perm_two_sided=(1 + np.sum(np.abs(nula) >= abs(obs))) / n,
                         p_perm_one_sided_positive=(1 + np.sum(nula >= obs)) / n))
    return res, pd.DataFrame(crow)


def sensibilidad_compuestos(repo, prioridad=True):
    """Antes script 07. Cuatro regímenes; variantes: base (desestacionalizada), sin tendencia
    lineal, sin el episodio 2023-25 (meses de régimen desde oct-2022 retirados; neutros
    conservados), ambas, y sin desestacionalizar (método anterior); ámbitos, NORTE, SUR y N-S;
    FDR sobre 56 contrastes por variante; además, neutro estricto (ONI e ICEN también neutros).
    Devuelve (tabla, inventario)."""
    Zd, E, C = _compuestos_grace(repo, True)
    Zraw = _compuestos_grace(repo, False)[0]
    oni = cargar_oni(repo)['oni'].reindex(Zd.index).values
    icen = cargar_icen(repo)['icen'].reindex(Zd.index).values
    idx = Zd.index
    neutral = mascara_neutro(E, C)
    masks = mascaras_regimenes(E, C, prioridad)
    gap = (idx >= BRECHA_GRACE[0]) & (idx <= BRECHA_GRACE[1]); late = idx >= INICIO_EPISODIO_2023_25
    info = pd.DataFrame([dict(regime=k, months=int(m.sum()), episodes=contar_episodios(m),
                              months_in_GRACE_gap=int((m & gap).sum()), months_from_2022_10=int((m & late).sum()))
                         for k, m in masks.items()])
    info.loc[len(info)] = dict(regime='Neutral', months=int(neutral.sum()), episodes=contar_episodios(neutral),
                               months_in_GRACE_gap=int((neutral & gap).sum()),
                               months_from_2022_10=int((neutral & late).sum()))
    estricto = mascara_neutro_estricto(E, C, oni, icen)
    info.loc[len(info)] = dict(regime='Neutral (strict: ONI, ICEN)', months=int(estricto.sum()),
                               episodes=contar_episodios(estricto), months_in_GRACE_gap=int((estricto & gap).sum()),
                               months_from_2022_10=int((estricto & late).sum()))
    iN = [AMBITOS.index(d) for d in NORTE]; iS = [AMBITOS.index(d) for d in SUR]
    names = AMBITOS + ['NORTE', 'SUR', 'N-S']

    def ampliar(Zv):
        G = np.column_stack([Zv[:, iN].mean(1), Zv[:, iS].mean(1)])
        return np.column_stack([Zv, G, G[:, 0] - G[:, 1]])
    V = Zd.values; Vd = quitar_tendencia_columnas(V)
    variants = {'base': (V, False, neutral), 'detrended': (Vd, False, neutral), 'without_2023_25': (V, True, neutral),
                'detrended_without_2023_25': (Vd, True, neutral), 'strict_neutral': (V, False, estricto),
                'not_deseasonalized': (Zraw.values, False, neutral)}
    rows = []
    for vn, (Zv, drop, mneu) in variants.items():
        Y = ampliar(Zv)
        for rn, mr in masks.items():
            m2 = mr & ~late if drop else mr
            if m2.sum() < 3:
                continue
            o, _, p = p_desplazamiento_circular(Y, m2, mneu)
            rows += [dict(variant=vn, regime=rn, unit=nm, n_regime_months=int(m2.sum()),
                          composite_pct_sigma=round(float(a), 1), p_perm=round(float(b), 4))
                     for nm, a, b in zip(names, o, p)]
    R = pd.DataFrame(rows)
    R['q_fdr_56'] = np.nan
    for vn in variants:
        s = R[(R.variant == vn) & (R.unit.isin(AMBITOS))]
        R.loc[s.index, 'q_fdr_56'] = fdr_bh(s.p_perm.values).round(4)
    return R, info


# ---------------------------------------------------------------- in situ ----
_CLAVES = {"mes", "date", "fecha", "anio", "año", "year", "month"}
_INCLUIR = ["caudal", "volumen", "precipitacion", "precipitación", "pp_"]
_EXCLUIR = ["demanda", "evapo", "etp", "eto"]


def _columnas_valor(df):
    cand = [c for c in df.columns if c not in _CLAVES]
    num = [c for c in cand if pd.api.types.is_numeric_dtype(df[c])]
    inc = [c for c in num if any(k in c.lower() for k in _INCLUIR) and not any(k in c.lower() for k in _EXCLUIR)]
    if inc:
        return inc
    fb = [c for c in num if not any(k in c.lower() for k in _EXCLUIR)]
    return fb if fb else num


def leer_registro(fp):
    """Serie mensual de un archivo in situ con fechas reales (media de sus columnas de valor);
    None si el archivo no tiene fechas (climatologías)."""
    df = pd.read_csv(fp); df.columns = [c.strip().lower() for c in df.columns]
    dc = 'date' if 'date' in df.columns else ('fecha' if 'fecha' in df.columns else None)
    if dc is None:
        return None
    df[dc] = pd.to_datetime(df[dc], errors='coerce'); df = df.dropna(subset=[dc])
    if df.empty:
        return None
    cols = _columnas_valor(df)
    if not cols:
        return None
    df['_v'] = df[cols].mean(axis=1); df['_ym'] = df[dc].values.astype('datetime64[M]')
    s = df.groupby('_ym')['_v'].mean(); s.index = pd.to_datetime(s.index)
    return s


def indice_insitu(repo):
    idx = pd.read_csv(ruta(repo, 'data/insitu/insitu_index.csv'))
    return idx[~idx.archivo.isin(EXCLUIDOS_INSITU)]


def cargar_registros_insitu(repo, tindex, quitar_tendencia=False, corte=None, desestacionalizar=True):
    """Registros con fechas reales ubicados en el calendario de etiquetas `tindex` (desde 1950).
    Cada registro: dict(f, dom, pos, val). quitar_tendencia: tendencia lineal por registro;
    desestacionalizar: se resta a cada registro su climatología mensual (meses desde 1950)."""
    ins = ruta(repo, 'data/insitu')
    idx = indice_insitu(repo)
    files = sorted(f for f in os.listdir(ins) if f.endswith('.csv') and f != 'insitu_index.csv'
                   and f not in EXCLUIDOS_INSITU)
    recs = []
    for f in files:
        s = leer_registro(os.path.join(ins, f))
        if s is None or len(s) < 12:
            continue
        m = idx[idx.archivo == f]; dom = m.dominio_AAA.iloc[0] if len(m) else None
        if dom is None or pd.isna(dom):
            continue
        pos = tindex.get_indexer(s.index); ok = pos >= 0
        if corte:
            ok = ok & (s.index < pd.Timestamp(corte))
        if quitar_tendencia and ok.sum() > 24:
            t = pos[ok].astype(float); vv = s.values[ok].astype(float)
            s = pd.Series(vv - np.polyval(np.polyfit(t, vv, 1), t) + vv.mean(), index=s.index[ok])
            pos = tindex.get_indexer(s.index); ok = pos >= 0
        val = s.values[ok].astype(float)
        if desestacionalizar:
            ser = pd.Series(val, index=s.index[ok])
            val = (ser - ser.groupby(ser.index.month).transform('mean')).values
        recs.append(dict(f=f, dom=dom, pos=pos[ok], val=val))
    return recs


def compuesto_registro(rec, lab):
    """(media del régimen - media neutra) / sigma neutra x 100 para un registro (ddof = 0);
    requiere >= 6 meses neutros y >= 3 meses del régimen."""
    L = lab[rec['pos']]; v = rec['val']; nv = v[L == 0]
    if len(nv) < 6 or nv.std() == 0:
        return {1: np.nan, 2: np.nan, 3: np.nan, 4: np.nan}
    mu, sd = nv.mean(), nv.std(ddof=0)
    out = {}
    for k in (1, 2, 3, 4):
        x = v[L == k]; out[k] = (x.mean() - mu) / sd * 100 if len(x) >= 3 else np.nan
    return out


def compuestos_por_registro(repo, desestacionalizar=True, quitar_tendencia=False):
    """Compuesto de cada registro in situ con fechas reales (% de sigma neutra), por régimen."""
    v6 = cargar_ec(repo, 'v6')
    lab = etiquetas_regimen(v6['e_index'].values, v6['c_index'].values)
    recs = cargar_registros_insitu(repo, v6.index, quitar_tendencia, desestacionalizar=desestacionalizar)
    filas = []
    for r in recs:
        c = compuesto_registro(r, lab)
        filas.append(dict(archivo=r['f'], dominio_AAA=r['dom'], nino_e_pct=c[1], nino_c_pct=c[2],
                          nina_c_pct=c[3], e_frio_pct=c[4]))
    return pd.DataFrame(filas)


def medias_por_ambito(recs, lab):
    res = {}
    for r in recs:
        c = compuesto_registro(r, lab); res.setdefault(r['dom'], []).append([c[1], c[2], c[3], c[4]])
    return {d: np.nanmean(np.array(v), axis=0) for d, v in res.items()}


def media_grupo(d, nombres, k):
    x = [d[n][k] for n in nombres if n in d]
    return np.nanmean(x) if x else np.nan


def _p_nula(nula, o):
    x = nula[~np.isnan(nula)]
    return (1 + np.sum(np.abs(x) >= abs(o))) / (len(x) + 1) if not np.isnan(o) else np.nan


NOMBRES_INSITU = ['El Nino E', 'El Nino C', 'La Nina C', 'E frio']


def compuestos_insitu(repo, quitar_tendencia=False, desestacionalizar=True):
    """Antes script 08. Compuestos in situ (1950-) por registro, ámbito y grupo; nula por
    desplazamiento circular del calendario de etiquetas (12 a T-12 meses); FDR sobre
    ámbitos x regímenes; contraste norte-sur, inversión C-E del sur y grupos por variable.
    Devuelve dict de tablas: dominios, grupos, por_variable, cobertura, etiquetas."""
    v6 = cargar_ec(repo, 'v6')
    lab = etiquetas_regimen(v6['e_index'].values, v6['c_index'].values)
    T = len(lab); tindex = v6.index
    recs = cargar_registros_insitu(repo, tindex, quitar_tendencia, desestacionalizar=desestacionalizar)
    idx = indice_insitu(repo)
    obs = medias_por_ambito(recs, lab); doms = sorted(obs)
    shifts = range(12, T - 12)
    nul = {d: [] for d in doms}; nulS = []; nulN = []
    for sft in shifts:
        st = medias_por_ambito(recs, np.roll(lab, sft))
        for d in doms:
            nul[d].append(st[d])
        nulS.append([media_grupo(st, SUR, k) for k in range(4)])
        nulN.append([media_grupo(st, NORTE, k) for k in range(4)])
    nulS = np.array(nulS); nulN = np.array(nulN)
    rows = []
    for d in doms:
        a = np.array(nul[d])
        for k, name in enumerate(NOMBRES_INSITU):
            x = a[:, k]; x = x[~np.isnan(x)]
            p = (1 + np.sum(np.abs(x) >= abs(obs[d][k]))) / (len(x) + 1)
            rows.append(dict(regime=name, domain=d, insitu_pct=round(obs[d][k], 1), null_sd=round(x.std(), 1),
                             p_perm=round(p, 4), n_files=sum(1 for r in recs if r['dom'] == d)))
    R = pd.DataFrame(rows); R['q_fdr'] = fdr_bh(R.p_perm.values).round(3)
    G = []
    for k, name in enumerate(NOMBRES_INSITU):
        oS = media_grupo(obs, SUR, k); oN = media_grupo(obs, NORTE, k)
        pS = (1 + np.sum(np.abs(nulS[:, k]) >= abs(oS))) / (len(nulS) + 1)
        pN = (1 + np.sum(np.abs(nulN[:, k]) >= abs(oN))) / (len(nulN) + 1)
        diff = nulN[:, k] - nulS[:, k]; oD = oN - oS
        pD = (1 + np.sum(np.abs(diff) >= abs(oD))) / (len(diff) + 1)
        G.append(dict(regime=name, north_mean=round(oN, 1), p_north=round(pN, 4), south_mean=round(oS, 1),
                      p_south=round(pS, 4), north_minus_south=round(oD, 1), p_contrast=round(pD, 4)))
    oR = media_grupo(obs, SUR, 1) - media_grupo(obs, SUR, 0); dR = nulS[:, 1] - nulS[:, 0]
    G = pd.DataFrame(G); G['south_reversal_C_minus_E'] = round(oR, 1)
    G['p_south_reversal'] = round((1 + np.sum(np.abs(dR) >= abs(oR))) / (len(dR) + 1), 4)
    varmap = dict(zip(idx.archivo, idx.variable)); V = []
    for var in ['todas', 'caudal_volumen', 'precipitacion']:
        sub = recs if var == 'todas' else [r for r in recs if varmap.get(r['f']) == var]
        ob = medias_por_ambito(sub, lab); vS = []; vN = []
        for sft in shifts:
            st = medias_por_ambito(sub, np.roll(lab, sft))
            vS.append([media_grupo(st, SUR, k) for k in range(4)]); vN.append([media_grupo(st, NORTE, k) for k in range(4)])
        vS = np.array(vS); vN = np.array(vN)
        for k, name in enumerate(NOMBRES_INSITU):
            oN, oS = media_grupo(ob, NORTE, k), media_grupo(ob, SUR, k)
            V.append(dict(variable=var, regime=name, n_files_north=sum(r['dom'] in NORTE for r in sub),
                          n_files_south=sum(r['dom'] in SUR for r in sub),
                          north_mean=round(oN, 1), p_north=round(_p_nula(vN[:, k], oN), 4),
                          south_mean=round(oS, 1), p_south=round(_p_nula(vS[:, k], oS), 4),
                          north_minus_south=round(oN - oS, 1), p_contrast=round(_p_nula(vN[:, k] - vS[:, k], oN - oS), 4)))
    return dict(dominios=R, grupos=G, por_variable=pd.DataFrame(V), etiquetas=pd.Series(lab, index=tindex),
                n_registros=len(recs))


# ---------------------------------------------------------------- eventos ----
def _ventana(cond, cerca, maxgap=0):
    c = cond.copy()
    if maxgap:
        runs = (c != c.shift()).cumsum()
        for _, g in c.groupby(runs):
            if not g.iloc[0] and len(g) <= maxgap and g.index[0] > c.index[0] and g.index[-1] < c.index[-1]:
                c.loc[g.index] = True
    runs = (c != c.shift()).cumsum()
    w = c[runs == runs.loc[pd.Timestamp(cerca)]]
    assert w.all(), cerca
    return w.index[0], w.index[-1]


def _ventana_segura(cond, cerca, maxgap=0):
    try:
        return _ventana(cond, cerca, maxgap)
    except (AssertionError, KeyError):
        return None


def analisis_eventos(repo):
    """Antes script 09. Ventanas de cinco eventos con ONI e ICEN; cambio del almacenamiento
    dS = media de los 3 últimos meses de la ventana - media de los 3 meses previos (cm y Gt);
    percentil entre ventanas de igual duración (descriptivo); variante sin tendencia;
    sensibilidad con ventanas definidas con E y C.
    Devuelve dict: cambios, ventanas, sensibilidad, serie (D)."""
    D = series_tws_cuaderno02(repo)[2][AMBITOS]   # la misma serie desestacionalizada del cuaderno 02
    x = np.arange(len(D))
    Dd = D.apply(lambda c: c - np.polyval(np.polyfit(x, c.values, 1), x))
    area = area_ambitos_km2(repo)
    rd = lambda f: pd.read_csv(ruta(repo, 'data/enso', f), parse_dates=['time']).set_index('time')
    idx = rd('oni_2002_2025.csv')[['oni']].join(rd('icen_2002_2025.csv')).join(rd('ecindex_ersstv5.csv')).reindex(D.index)
    rawnc = xr.open_dataset(ruta(repo, 'data/raw/GRCTellus.JPL.200204_202511.GLO.RL06.3M.MSCNv04CRI.nc'))
    obs = set(pd.to_datetime(rawnc.time.values).to_period('M'))
    imputed = pd.Series([p not in obs for p in D.index.to_period('M')], index=D.index)
    EV = {'El Niño 2009–10': _ventana(idx.oni >= 0.5, '2009-12-01'),
          'La Niña 2010–12': _ventana(idx.oni <= -0.5, '2010-12-01', maxgap=3),
          'El Niño 2015–16': _ventana(idx.oni >= 0.5, '2015-12-01'),
          'El Niño costero 2017': _ventana(idx.icen >= 0.4, '2017-03-01'),
          'El Niño costero 2023–24': _ventana(idx.icen >= 0.4, '2023-06-01')}
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
            for i, dom in enumerate(AMBITOS):
                rows.append(dict(evento=ev, variante=tag, ambito=dom, dS_cm=dS[dom], dS_Gt=dS[dom] * area[dom] * 1e-5,
                                 percentil=(allc[:, i] <= dS[dom]).mean() * 100))
    res = pd.DataFrame(rows)
    E, C = idx.E_index, idx.C_index
    VAR = {'EC_0.5': {'El Niño 2009–10': _ventana_segura(C >= 0.5, '2009-12-01', 1),
                      'La Niña 2010–12': _ventana_segura(C <= -0.5, '2010-12-01', 3),
                      'El Niño 2015–16': _ventana_segura((E >= 0.5) | (C >= 0.5), '2015-12-01', 1),
                      'El Niño costero 2017': _ventana_segura(E >= 0.5, '2017-03-01'),
                      'El Niño costero 2023–24': _ventana_segura(E >= 0.5, '2023-10-01', 1)},
           'EC_regimen': {'El Niño 2009–10': _ventana_segura(C >= 0.5, '2009-12-01', 1),
                          'La Niña 2010–12': _ventana_segura(C <= -1.0, '2010-12-01', 3),
                          'El Niño 2015–16': _ventana_segura(E >= 1.0, '2015-12-01', 1),
                          'El Niño costero 2017': _ventana_segura(E >= 1.0, '2017-03-01'),
                          'El Niño costero 2023–24': _ventana_segura(E >= 1.0, '2023-10-01', 1)}}
    ref = res[res.variante == 'sin_tendencia'].pivot(index='ambito', columns='evento', values='dS_cm').loc[AMBITOS]
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
    return dict(cambios=res, ventanas=pd.DataFrame(wins), sensibilidad=pd.DataFrame(sens), serie=D,
                eventos=list(EV))


# =============================================================================
# 8. Verificaciones de las cifras que la tesis da como hechos
# =============================================================================
def verificar(repo):
    """Comprueba los conteos básicos citados en la tesis; lanza AssertionError si alguno cambia."""
    x = cargar_grace(repo)
    assert x.sizes['time'] == 288, 'se esperaban 288 meses (2002-01 a 2025-12)'
    gdf = cargar_ambitos(repo)
    assert gdf['NAME_AAA'].nunique() == 14, 'se esperaban 14 ámbitos'
    ec = cargar_ec(repo, 'v5').reindex(pd.to_datetime(x.time.values))
    E, C = ec['E_index'].values, ec['C_index'].values
    mE = mascaras_regimenes(E, C, prioridad=True)['El Nino E']
    assert int(mE.sum()) == 13 and contar_episodios(mE) == 5, 'El Niño E: se esperaban 13 meses en 5 episodios'
    idx = indice_insitu(repo)
    assert len(idx) == 69, 'se esperaban 69 registros in situ'
    print('Verificación correcta: 288 meses, 14 ámbitos, El Niño E 13 meses en 5 episodios, 69 registros in situ.')

# =============================================================================
# 9. Tendencia de largo plazo y coherencia entre ámbitos (descriptivo)
# =============================================================================
def tendencia_lineal(s):
    """Pendiente lineal (cm/año) de una serie mensual, su error estándar y su valor p con
    grados de libertad efectivos n (1 - r1) / (1 + r1), donde r1 es la autocorrelación de
    rezago uno de los residuos. Devuelve (pendiente, error, p, n_ef)."""
    y = np.asarray(s, dtype=float); t = np.arange(len(y)) / 12.0
    b, a = np.polyfit(t, y, 1); r = y - (a + b * t)
    r1 = np.corrcoef(r[:-1], r[1:])[0, 1]
    neff = len(y) * (1 - r1) / (1 + r1)
    se = np.sqrt(np.sum(r ** 2) / (neff - 2) / np.sum((t - t.mean()) ** 2))
    p = 2 * stats.t.sf(abs(b / se), neff - 2)
    return b, se, p, neff


def tendencias_por_ambito(repo):
    """Tendencia lineal 2002-2025 de la serie desestacionalizada de cada ámbito (cuaderno 02),
    con su significancia, y pendientes en 2002-2016 y hasta septiembre de 2022 (sin 2023-25)."""
    des = series_tws_cuaderno02(repo)[2][AMBITOS]
    filas = []
    for d in AMBITOS:
        b, se, p, ne = tendencia_lineal(des[d])
        filas.append(dict(ambito=d, pendiente_cm_anio=b, error_cm_anio=se, p=p, n_ef=ne,
                          pendiente_2002_2016=tendencia_lineal(des[d].loc[:'2016-12'])[0],
                          pendiente_hasta_2022_09=tendencia_lineal(des[d].loc[:'2022-09'])[0]))
    return pd.DataFrame(filas)


def correlacion_entre_ambitos(repo):
    """Matrices de correlación entre las series desestacionalizadas de los 14 ámbitos, con y sin
    tendencia lineal, y promedios norte-norte, sur-sur y norte-sur."""
    des = series_tws_cuaderno02(repo)[2][AMBITOS]
    sin = des.apply(lambda c: pd.Series(quitar_tendencia_lineal(c.values).values, index=des.index))
    res = {}
    for nombre, X in (('con_tendencia', des), ('sin_tendencia', sin)):
        Cm = X.corr()
        res[nombre] = Cm
        res[nombre + '_resumen'] = dict(
            norte_norte=Cm.loc[NORTE[0], NORTE[1]],
            sur_sur=np.mean([Cm.loc[a, b] for i, a in enumerate(SUR) for b in SUR[i + 1:]]),
            norte_sur=Cm.loc[NORTE, SUR].values.mean())
    return res
