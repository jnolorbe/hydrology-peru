"""In-situ (1950-) ENSO-regime composites (E, C, La Nina C, cold E), % of local sigma of neutral months, per file then per AAA domain; circular-shift permutation of the monthly regime labels (shifts 12..T-12); BH-FDR over domain x regime; group tests NORTH, SOUTH, N-S and the south C-minus-E reversal. Env DET=1 linearly detrends each record. Final section: the same group tests split by variable type (hydrometric caudal_volumen vs pluviometric precipitacion; column variable of insitu_index.csv) -> insitu_composite_groups_by_variable[_detrended].csv. Usage: python 08_insitu_composite_significance.py <repo_root> <out_dir>"""
import os, re, sys, numpy as np, pandas as pd, warnings
warnings.filterwarnings('ignore')
BASE=sys.argv[1]; OUTD=sys.argv[2]; INS=os.path.join(BASE,'data/insitu')
SUF='_detrended' if os.environ.get('DET')=='1' else ''
GROWS=[]
EXCL={'chili_caudal_volumen.csv','rimac_caudal_volumen.csv','canete_precipitacion_climatologia.csv'}
idx=pd.read_csv(os.path.join(INS,'insitu_index.csv')); idx=idx[~idx.archivo.isin(EXCL)]
files=sorted(f for f in os.listdir(INS) if f.endswith('.csv') and f!='insitu_index.csv' and f not in EXCL)
v6=pd.read_csv(os.path.join(BASE,'data/enso/ecindex_ersstv6.csv')); v6.columns=[c.strip().lower() for c in v6.columns]
v6['time']=pd.to_datetime(pd.to_datetime(v6['time']).values.astype('datetime64[M]')); v6=v6.set_index('time').sort_index().loc['1950-01-01':]
E,C=v6['e_index'].values,v6['c_index'].values
lab=np.full(len(v6),-1)  # -1 unclassified, 0 neutral,1 E,2 niñoC,3 niñaC  (same precedence as notebook)
lab[(np.abs(E)<0.5)&(np.abs(C)<0.5)]=0
lab[(C<=-1.0)]=3
lab[(C>=0.5)&(E<0.5)]=2
lab[(E>=1.0)&(C<1.0)]=1
lab[(E<=-1.0)&(C>-1.0)&(lab==-1)]=4
T=len(lab); tindex=v6.index
print('labels months:',T, tindex[0].date(), tindex[-1].date(), {k:int((lab==k).sum()) for k in (0,1,2,3,4)})
KEY={"mes","date","fecha","anio","año","year","month"}; INC=["caudal","volumen","precipitacion","precipitación","pp_"]; EXC=["demanda","evapo","etp","eto"]
def sel(df,key):
    cand=[c for c in df.columns if c not in key]; num=[c for c in cand if pd.api.types.is_numeric_dtype(df[c])]
    inc=[c for c in num if any(k in c.lower() for k in INC) and not any(k in c.lower() for k in EXC)]
    if inc: return inc
    fb=[c for c in num if not any(k in c.lower() for k in EXC)]; return fb if fb else num
def series(fp):
    df=pd.read_csv(fp); df.columns=[c.strip().lower() for c in df.columns]
    dc='date' if 'date' in df.columns else ('fecha' if 'fecha' in df.columns else None)
    if dc is None: return None
    df[dc]=pd.to_datetime(df[dc],errors='coerce'); df=df.dropna(subset=[dc])
    if df.empty: return None
    cols=sel(df,KEY)
    if not cols: return None
    df['_v']=df[cols].mean(axis=1); df['_ym']=df[dc].values.astype('datetime64[M]')
    s=df.groupby('_ym')['_v'].mean(); s.index=pd.to_datetime(s.index); return s
import os as _o
DET=_o.environ.get('DET')=='1'; CUT=_o.environ.get('CUT')
recs=[]
for f in files:
    s=series(os.path.join(INS,f))
    if s is None or len(s)<12: continue
    m=idx[idx.archivo==f]; dom=m.dominio_AAA.iloc[0] if len(m) else None
    if dom is None or pd.isna(dom): continue
    pos=tindex.get_indexer(s.index)       # position of each obs in label timeline (-1 if outside)
    ok=pos>=0
    if CUT: ok=ok&(s.index<pd.Timestamp(CUT))
    if DET and ok.sum()>24:
        t=pos[ok].astype(float); vv=s.values[ok].astype(float); s=pd.Series(vv-np.polyval(np.polyfit(t,vv,1),t)+vv.mean(),index=s.index[ok]); pos=tindex.get_indexer(s.index); ok=pos>=0
    recs.append(dict(f=f,dom=dom,pos=pos[ok],val=s.values[ok]))
print('usable real-date files:',len(recs))
def comp(rec,lab_vec):
    L=lab_vec[rec['pos']]; v=rec['val']; nv=v[L==0]
    if len(nv)<6 or nv.std()==0: return {1:np.nan,2:np.nan,3:np.nan,4:np.nan}
    mu,sd=nv.mean(),nv.std()   # ddof=0 in notebook via .std(ddof=0): fix below
    sd=nv.std(ddof=0); out={}
    for k in (1,2,3,4):
        x=v[L==k]; out[k]=(x.mean()-mu)/sd*100 if len(x)>=3 else np.nan
    return out
def domain_stats(lab_vec):
    # per-file composites then mean per domain
    res={}
    for r in recs:
        c=comp(r,lab_vec); res.setdefault(r['dom'],[]).append([c[1],c[2],c[3],c[4]])
    return {d:np.nanmean(np.array(v),axis=0) for d,v in res.items()}
obs=domain_stats(lab)
doms=sorted(obs)
SOUTH=['PAMPAS-APURIMAC','URUBAMBA-VILCANOTA','CAPLINA-OCOÑA','TITICACA']; NORTH=['JEQUETEPEQUE-ZARUMILLA','HUARMEY-CHICAMA']
def group(d,names,k): return np.nanmean([d[n][k] for n in names if n in d])
# null: circular shifts of the label timeline (common to all files; preserves ENSO episode structure)
shifts=range(12,T-12)    # exclude |shift|<12 months
nul={d:[] for d in doms}; nulS=[];nulN=[]
for sft in shifts:
    lv=np.roll(lab,sft); st=domain_stats(lv)
    for d in doms: nul[d].append(st[d])
    nulS.append([group(st,SOUTH,k) for k in range(4)]); nulN.append([group(st,NORTH,k) for k in range(4)])
nulS=np.array(nulS); nulN=np.array(nulN)
rows=[]
for d in doms:
    a=np.array(nul[d])
    for k,name in enumerate(['El Nino E','El Nino C','La Nina C','E frio']):
        x=a[:,k]; x=x[~np.isnan(x)]
        p=(1+np.sum(np.abs(x)>=abs(obs[d][k])))/(len(x)+1)
        rows.append(dict(regime=name,domain=d,insitu_pct=round(obs[d][k],1),null_sd=round(x.std(),1),p_perm=round(p,4),n_files=sum(1 for r in recs if r['dom']==d)))
R=pd.DataFrame(rows)
def bh(p):
    p=np.asarray(p);n=len(p);o=np.argsort(p);q=np.empty(n);prev=1
    for rank,i in zip(range(n,0,-1),o[::-1]): prev=min(prev,p[i]*n/rank); q[i]=prev
    return q
R['q_fdr']=bh(R.p_perm.values).round(3)
R.to_csv(os.path.join(OUTD,'insitu_composite_domains'+SUF+'.csv'),index=False)
pd.set_option('display.width',200,'display.max_rows',100); print(R.to_string(index=False))
print('p<0.05:',R.groupby('regime').p_perm.apply(lambda s:int((s<0.05).sum())).to_dict(),'| q<0.10:',R.groupby('regime').q_fdr.apply(lambda s:int((s<0.10).sum())).to_dict())
print('\n-- group tests (in-situ) --')
for k,name in enumerate(['El Nino E','El Nino C','La Nina C','E frio']):
    oS=group(obs,SOUTH,k); oN=group(obs,NORTH,k)
    pS=(1+np.sum(np.abs(nulS[:,k])>=abs(oS)))/(len(nulS)+1)
    pN=(1+np.sum(np.abs(nulN[:,k])>=abs(oN)))/(len(nulN)+1)
    diff=nulN[:,k]-nulS[:,k]; oD=oN-oS; pD=(1+np.sum(np.abs(diff)>=abs(oD)))/(len(diff)+1)
    GROWS.append(dict(regime=name,north_mean=round(oN,1),p_north=round(pN,4),south_mean=round(oS,1),p_south=round(pS,4),north_minus_south=round(oD,1),p_contrast=round(pD,4)))
    print(f"{name}: SOUTH mean={oS:.1f} (p={pS:.3f}) | NORTH mean={oN:.1f} (p={pN:.3f}) | N-S contrast={oD:.1f} (p={pD:.3f})")
# south sign reversal E vs C: statistic = south_C - south_E
oR=group(obs,SOUTH,1)-group(obs,SOUTH,0); dR=nulS[:,1]-nulS[:,0]
print(f"SOUTH reversal (C minus E): obs={oR:.1f}, p={(1+np.sum(np.abs(dR)>=abs(oR)))/(len(dR)+1):.3f}")
# per-domain months used
for k,name in [(1,'E'),(2,'C'),(3,'LaNinaC'),(4,'Efrio')]:
    print(name,'classified months in 1950-:',int((lab==k).sum()), 'episodes:',int(((lab==k)[1:]&(~(lab==k))[:-1]).sum()+(lab[0]==k)))

G=pd.DataFrame(GROWS); G['south_reversal_C_minus_E']=round(oR,1); G['p_south_reversal']=round((1+np.sum(np.abs(dR)>=abs(oR)))/(len(dR)+1),4)
G.to_csv(os.path.join(OUTD,'insitu_composite_groups'+SUF+'.csv'),index=False)

# ---- group tests split by variable type (hydrometric vs pluviometric) ----
# Same per-file composites, domain means, circular-shift null and group statistics as above,
# restricted to the records of one variable type; 'todas' reproduces the group results above.
VARMAP=dict(zip(idx.archivo,idx.variable))
def domain_stats_sub(sub,lab_vec):
    res={}
    for r in sub:
        c=comp(r,lab_vec); res.setdefault(r['dom'],[]).append([c[1],c[2],c[3],c[4]])
    return {d:np.nanmean(np.array(v),axis=0) for d,v in res.items()}
def group_sub(d,names,k):
    x=[d[n][k] for n in names if n in d]; return np.nanmean(x) if x else np.nan
def pval(null,o):
    x=null[~np.isnan(null)]; return (1+np.sum(np.abs(x)>=abs(o)))/(len(x)+1) if not np.isnan(o) else np.nan
VROWS=[]
for var in ['todas','caudal_volumen','precipitacion']:
    sub=recs if var=='todas' else [r for r in recs if VARMAP.get(r['f'])==var]
    ob=domain_stats_sub(sub,lab); vS=[]; vN=[]
    for sft in shifts:
        st=domain_stats_sub(sub,np.roll(lab,sft))
        vS.append([group_sub(st,SOUTH,k) for k in range(4)]); vN.append([group_sub(st,NORTH,k) for k in range(4)])
    vS=np.array(vS); vN=np.array(vN)
    for k,name in enumerate(['El Nino E','El Nino C','La Nina C','E frio']):
        oN,oS=group_sub(ob,NORTH,k),group_sub(ob,SOUTH,k)
        VROWS.append(dict(variable=var,regime=name,n_files_north=sum(r['dom'] in NORTH for r in sub),n_files_south=sum(r['dom'] in SOUTH for r in sub),
            north_mean=round(oN,1),p_north=round(pval(vN[:,k],oN),4),south_mean=round(oS,1),p_south=round(pval(vS[:,k],oS),4),
            north_minus_south=round(oN-oS,1),p_contrast=round(pval(vN[:,k]-vS[:,k],oN-oS),4)))
V=pd.DataFrame(VROWS); V.to_csv(os.path.join(OUTD,'insitu_composite_groups_by_variable'+SUF+'.csv'),index=False)
print('\n-- group tests by variable type --'); print(V.to_string(index=False))
