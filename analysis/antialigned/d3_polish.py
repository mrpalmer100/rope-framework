import numpy as np, pickle, sys, pathlib; sys.path.insert(0,'.')
from benchmarks.foundations import qsweep_stage1 as q1, sparsej_instrument as SJ, truestate_stage2 as S2
CK=pathlib.Path('analysis/antialigned/d3_polish.pkl')
class PD(dict):
    def __setitem__(self,k,v): super().__setitem__(k,v); CK.write_bytes(pickle.dumps(dict(self)))
pol=PD(pickle.loads(CK.read_bytes()) if CK.exists() else {})
T=q1.QTGrid(144,36,4,5); A2=0.02*S2.R2
x=np.asarray(pol['d3']['x'],float) if 'd3' in pol else np.asarray(pickle.load(open('analysis/antialigned_ckpt.pkl','rb'))['aa|5/4|anti|-0.35|gate']['x'],float)
print(f"resume: RMS {T.field_rms(x,'a2',A2):.2e}  it {pol.get('d3',{}).get('it','-')}", flush=True)
sj,_=SJ.make_instrument(T,x,'a2',A2,50.0,cache='analysis/sparsej_pattern_144x36.pkl'); bs=SJ.BandedTorusSolver(144,36,nglob=2)
xn=SJ.gn_sparse(T,x,'a2',A2,sj,bs,rounds=60,st=pol,key='d3',stop_rms=1e-9)
print(f"POLISH: RMS {T.field_rms(xn,'a2',A2):.2e}  clos {T.closure_max(xn):.1e}  om2 {T.geom(xn)[10]:+.6f}", flush=True)
