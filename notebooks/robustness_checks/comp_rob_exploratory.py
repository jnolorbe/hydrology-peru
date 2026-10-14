import os, sys, numpy as np, pandas as pd, xarray as xr, geopandas as gpd, rioxarray  # noqa
BASE="/mnt/user-data/uploads/hydrology-peru"
ds = xr.open_dataset(os.path.join(BASE,"data/processed/GRACE_Peru_final_IQR1_5.nc"))
print(list(ds.data_vars), ds.sizes)
if 'month' in ds: ds=ds.drop_vars('month')
x=ds['lwe_thickness_corrected']; x=x-x.mean('time'); x=x.rio.write_crs("EPSG:4326")
Z=((x/x.std('time'))*100).rio.write_crs("EPSG:4326")
gdf=gpd.read_file(os.path.join(BASE,"data/shapefiles/hydroAAA_domains/Autoridad_Administrativa_del_Agua.shp"))
if gdf.crs.to_epsg()!=4326: gdf=gdf.to_crs(epsg=4326)
gdf=gdf[~((gdf['NAME_AAA']=='UCAYALI')&(gdf['OBJECTID_1'].isin([10,11])))]
REG=['JEQUETEPEQUE-ZARUMILLA','HUARMEY-CHICAMA','MARAÑÓN','HUALLAGA','AMAZONAS','CAÑETE-FORTALEZA','MANTARO','CHÁPARRA-CHINCHA','UCAYALI','PAMPAS-APURIMAC','URUBAMBA-VILCANOTA','MADRE DE DIOS','CAPLINA-OCOÑA','TITICACA']
ts={}
for d in REG:
    m=gdf[gdf['NAME_AAA']==d]; ts[d]=Z.rio.clip(m.geometry,m.crs,drop=True).mean(dim=['lat','lon']).to_series()
Zd=pd.DataFrame(ts).sort_index()
ec=pd.read_csv(os.path.join(BASE,"data/enso/ecindex_ersstv5.csv"),parse_dates=['time']).set_index('time').sort_index()
common=ec.index.intersection(Zd.index); ec=ec.loc[common]; Zd=Zd.loc[common]
E,C=ec.E_index.values,ec.C_index.values; idx=Zd.index; n=len(Zd)
NORTH=[REG.index(d) for d in ['JEQUETEPEQUE-ZARUMILLA','HUARMEY-CHICAMA']]
SOUTH=[REG.index(d) for d in ['PAMPAS-APURIMAC','URUBAMBA-VILCANOTA','CAPLINA-OCOÑA','TITICACA']]
neutral=(np.abs(E)<0.5)&(np.abs(C)<0.5)
masks={'El Nino E':(E>=1.0)&(C<1.0),'El Nino C':(C>=0.5)&(E<0.5),'La Nina C':(C<=-1.0),'E frio (E<=-1, C>-1)':(E<=-1.0)&(C>-1.0)}
def runs(m):
    m=m.astype(int); return int(((m[1:]==1)&(m[:-1]==0)).sum()+(m[0]==1))
gap=((idx>='2017-07-01')&(idx<='2018-05-31'))
for k,m in masks.items(): print(k,'meses',int(m.sum()),'episodios',runs(m),'en brecha GRACE-FO',int((m&gap).sum()))
def comp(Zv,mr,mn,rolls=None):
    return Zv[mr].mean(0)-Zv[mn].mean(0)
def test(Zv,mr,mn,groups=True):
    """returns obs dict, p dict (circular shift of Zv relative to masks)"""
    G=np.column_stack([Zv[:,NORTH].mean(1),Zv[:,SOUTH].mean(1)])
    Y=np.column_stack([Zv,G,G[:,0]-G[:,1]])   # 14 domains, north, south, N-S
    obs=comp(Y,mr,mn)
    null=np.array([comp(np.roll(Y,k,axis=0),mr,mn) for k in range(1,len(Y))])
    p=(1+np.sum(np.abs(null)>=np.abs(obs),axis=0))/len(Y)
    return obs,p
names=REG+['NORTE','SUR','N-S']
def detr(Zv):
    t=np.arange(len(Zv)); out=Zv.copy()
    for j in range(Zv.shape[1]):
        out[:,j]=Zv[:,j]-np.polyval(np.polyfit(t,Zv[:,j],1),t)
    return out
variants={'base':(Zd.values,{}),'sin tendencia':(detr(Zd.values),{}),}
# leave-2023-out: remove regime months >= 2022-10 from regime masks (keep neutral)
rows=[]
for vn,(Zv,_) in variants.items():
    for rn,mr in masks.items():
        obs,p=test(Zv,mr,neutral)
        for nm,o,pp in zip(names,obs,p): rows.append(dict(variant=vn,regime=rn,unit=nm,comp=round(o,1),p=round(pp,3)))
late=idx>='2022-10-01'
for rn,mr in masks.items():
    m2=mr&~late
    if m2.sum()<3: continue
    for vn,Zv in [('sin 2023-25',Zd.values),('sin 2023-25 y sin tendencia',detr(Zd.values))]:
        obs,p=test(Zv,m2,neutral & ~late if False else neutral)
        for nm,o,pp in zip(names,obs,p): rows.append(dict(variant=vn,regime=rn,unit=nm,comp=round(o,1),p=round(pp,3)))
res=pd.DataFrame(rows); res.to_csv('comp_rob.csv',index=False)
pd.set_option('display.width',200,'display.max_rows',500)
sel=res[res.unit.isin(['JEQUETEPEQUE-ZARUMILLA','MARAÑÓN','NORTE','SUR','N-S'])]
print(sel.pivot_table(index=['regime','unit'],columns='variant',values=['comp','p'],aggfunc='first').to_string())
print({k:int((m&~late).sum()) for k,m in masks.items()})
