"""ROPE-MODE-013: matched topology-preserving sham spectral test.

For several independently fixed local deformation families, bracket the topology
transition, then choose a linked sham just below and an unlinked state just above
the transition. Pair selection uses geometry and the full sampled tubular field
only. Spectral quantities are computed only after all pairs are frozen.
"""
from pathlib import Path
import csv, json, sys, time
import numpy as np
from scipy.sparse import diags, eye, kron
from scipy.sparse.linalg import eigsh
from scipy.spatial import cKDTree

ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from benchmarks.foundations.electron_variational_remesh import Model
from benchmarks.foundations.rope_matched_ensemble_classifier import normalize_geom, tube
from benchmarks.foundations.rope_fullfield_sham_controls import surgery_geometry, topology
from benchmarks.foundations.rope_topology_fingerprint import lap1
from benchmarks.foundations.rope_topology_transition_path import FAMILIES, find_transition, sector

BOXES=(4.0,5.0)
H=0.25
ALPHA=12.0; EPS=0.30; BETA=0.50
N_EIG=4; OUTER=0.50
# symmetric distances considered around the transition; selection is field/geometry only
DELTA_FRACS=np.array([0.03,0.045,0.06,0.08,0.10,0.14,0.20])


def build_grid(box):
    n=int(round(2*box/H))-1; h=2*box/(n+1)
    x=np.linspace(-box,box,n+2)[1:-1]
    X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
    xyz=np.column_stack([X.ravel(),Y.ravel(),Z.ravel()])
    I=eye(n,format='csr'); L=lap1(n,h)
    H0=kron(kron(L,I),I)+kron(kron(I,L),I)+kron(kron(I,I),L)
    r=np.linalg.norm(xyz,axis=1); Vc=-ALPHA/np.sqrt(r*r+EPS*EPS)
    return n,h,xyz,H0,Vc,r


def solve(grid,pts):
    n,h,xyz,H0,Vc,r=grid
    T=tube(xyz,pts)
    M=H0+diags(Vc-BETA*T,0,format='csr')
    vals,vecs=eigsh(M,k=N_EIG,which='SA',tol=8e-8,maxiter=16000)
    o=np.argsort(vals); vals=vals[o]; vecs=vecs[:,o]
    p=np.abs(vecs)**2; outer=p[r>(BOX_CURRENT-OUTER)].sum(0)/np.maximum(p.sum(0),1e-15)
    return vals,vals-vals[0],outer


def rel(a,b): return float(np.linalg.norm(a-b)/max(np.linalg.norm(a),1e-15))


def choose_pair(a,b,fam,tc,xyz):
    scale=max(tc,0.1); best=None
    for frac in DELTA_FRACS:
        ams=max(0.0,tc-frac*scale); amu=tc+frac*scale
        sa,sb,c=surgery_geometry(a,b,*fam,float(ams)); ua,ub,_=surgery_geometry(a,b,*fam,float(amu))
        lks,dms=topology(sa,sb,stride=1); lku,dmu=topology(ua,ub,stride=1)
        if sector(lks)!='linked' or sector(lku)!='unlinked' or min(dms,dmu)<0.001: continue
        Ts=tube(xyz,np.vstack([sa,sb])); Tu=tube(xyz,np.vstack([ua,ub]))
        # directly match sham and unlink fields, with a small preference for proximity to transition
        fld=rel(Ts,Tu)
        geom=float(np.sqrt(np.mean(np.sum((np.vstack([sa,sb])-np.vstack([ua,ub]))**2,axis=1))))
        score=fld+0.25*geom+0.02*frac
        rec=(score,frac,sa,sb,ua,ub,c,lks,lku,dms,dmu,fld,geom,Ts,Tu)
        if best is None or score<best[0]: best=rec
    return best


def main():
    global BOX_CURRENT
    grids={b:build_grid(b) for b in BOXES}
    fine=grids[BOXES[-1]]
    st=np.load(ROOT/'analysis'/'ELEC009_state.npz')
    model=Model(20,knots=st['knots_final'],m_energy=64)
    d0,lk0,cert,_=model.cert(st['z_final'])
    a,b=model.curves(st['z_final'],256); a,b=normalize_geom(a,b); original=np.vstack([a,b])
    frozen=[]
    for fi,fam in enumerate(FAMILIES):
        tr=find_transition(a,b,fam)
        if tr is None: continue
        tc=tr[0]; q=choose_pair(a,b,fam,tc,fine[2])
        if q is None: continue
        score,frac,sa,sb,ua,ub,c,lks,lku,dms,dmu,fld,geom,Ts,Tu=q
        frozen.append(dict(family=fi,fam=fam,tc=tc,frac=frac,sham=np.vstack([sa,sb]),unlink=np.vstack([ua,ub]),lks=lks,lku=lku,dms=dms,dmu=dmu,field_pair=fld,geom_pair=geom))
        print(f'freeze family={fi} frac={frac:.4f} LkS={lks:.5f} LkU={lku:.5f} field={fld:.6g} geom={geom:.6g}',flush=True)
    if len(frozen)<3: raise RuntimeError('insufficient frozen sham/unlink pairs')

    rows=[]; spectral=[]
    for box in BOXES:
        BOX_CURRENT=box; grid=grids[box]
        # shared original solve
        t=time.time(); vo,go,oo=solve(grid,original); print(f'box={box} original {time.time()-t:.1f}s gaps={go[1:]}',flush=True)
        for rec in frozen:
            vals={}; gaps={}; outs={}
            for kind in ('sham','unlink'):
                t=time.time(); v,g,o=solve(grid,rec[kind]); vals[kind]=v; gaps[kind]=g; outs[kind]=o
                print(f"box={box} family={rec['family']} {kind} {time.time()-t:.1f}s gaps={g[1:]}",flush=True)
            ds=gaps['sham']-go; du=gaps['unlink']-go; top=gaps['unlink']-gaps['sham']
            spectral.append((box,rec['family'],ds.copy(),du.copy(),top.copy(),outs['sham'].copy(),outs['unlink'].copy(),oo.copy()))
            for m in range(N_EIG):
                rows.append(dict(box=box,family=rec['family'],mode=m,original_gap=go[m],sham_gap=gaps['sham'][m],unlink_gap=gaps['unlink'][m],sham_minus_original=ds[m],unlink_minus_original=du[m],unlink_minus_sham=top[m],original_outer=oo[m],sham_outer=outs['sham'][m],unlink_outer=outs['unlink'][m]))

    coarse,finebox=BOXES
    coarse_map={f:t for b,f,ds,du,t,os,ou,oo in spectral if b==coarse}
    fine_records=[x for x in spectral if x[0]==finebox]
    tops=np.array([x[4][1:] for x in fine_records]); shams=np.array([x[2][1:] for x in fine_records])
    unlinks=np.array([x[3][1:] for x in fine_records])
    unc=np.array([np.abs(x[4][1:]-coarse_map[x[1]][1:]) for x in fine_records])
    sig=np.abs(tops)>3*np.maximum(unc,1e-6)
    # topology residual should be consistently nonzero and exceed matched sham disturbance
    ratios=np.abs(tops)/np.maximum(np.abs(shams),1e-6)
    consistent=[]
    for m in range(3):
        good=np.where(sig[:,m])[0]
        if len(good)>=3:
            s=np.sign(tops[good,m]); consistent.append(max(np.sum(s>0),np.sum(s<0))>=3)
        else: consistent.append(False)
    max_outer=max(float(np.max(np.r_[x[5],x[6],x[7]])) for x in fine_records)
    field=np.array([r['field_pair'] for r in frozen]); geom=np.array([r['geom_pair'] for r in frozen])
    bars={
      'B1_reference_and_triplets_certified': bool(cert and abs(abs(lk0)-1)<.03 and len(frozen)>=3 and all(abs(abs(r['lks'])-1)<.15 and abs(r['lku'])<.15 for r in frozen)),
      'B2_sham_unlink_field_matched': bool(np.median(field)<.012 and np.max(field)<.025),
      'B3_boundary_leakage': bool(max_outer<.001),
      'B4_domain_stable_contrasts': bool(np.max(unc)<.001),
      'B5_topology_residual_significant': bool(np.sum(np.any(sig,axis=0))>=2),
      'B6_topology_residual_consistent': bool(any(consistent)),
      'B7_topology_exceeds_sham_disturbance': bool(np.median(ratios)>1.0),
    }
    finding='MATCHED_SHAM_TOPOLOGY_RESIDUAL_DETECTED' if all(bars.values()) else 'MATCHED_SHAM_DOES_NOT_ISOLATE_TOPOLOGY'
    summary=dict(n_families=len(frozen),grid_boxes=BOXES,h=H,median_pair_field_mismatch=float(np.median(field)),max_pair_field_mismatch=float(np.max(field)),median_pair_geometry_rms=float(np.median(geom)),max_outer_probability=max_outer,max_domain_contrast_drift=float(np.max(unc)),median_abs_topology_residual=float(np.median(np.abs(tops))),median_topology_to_sham_ratio=float(np.median(ratios)),consistent_modes=[bool(x) for x in consistent],bars=bars,finding=finding)
    out=ROOT/'analysis'
    with open(out/'ROPE_MODE013_spectrum.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    with open(out/'ROPE_MODE013_controls.csv','w',newline='') as f:
        rr=[]
        for r in frozen: rr.append(dict(family=r['family'],offset=r['fam'][0],width=r['fam'][1],tilt=r['fam'][2],move=r['fam'][3],transition_amplitude=r['tc'],delta_fraction=r['frac'],sham_lk=r['lks'],unlink_lk=r['lku'],sham_dmin=r['dms'],unlink_dmin=r['dmu'],field_pair_mismatch=r['field_pair'],geometry_pair_rms=r['geom_pair']))
        w=csv.DictWriter(f,fieldnames=list(rr[0].keys())); w.writeheader(); w.writerows(rr)
    (out/'ROPE_MODE013_summary.json').write_text(json.dumps(summary,indent=2))
    lines=['ROPE-MODE-013 matched topology-preserving sham test',f"families={len(frozen)} boxes={BOXES} h={H}",f"median/max sham-unlink field mismatch={np.median(field):.6g}/{np.max(field):.6g}",f"median geometry RMS={np.median(geom):.6g}",f"max outer probability={max_outer:.6g}",f"max domain contrast drift={np.max(unc):.6g}",f"median |unlink-sham spectral residual|={np.median(np.abs(tops)):.6g}",f"median topology/sham effect ratio={np.median(ratios):.6g}",f"consistent modes={consistent}"]
    lines += [k+': '+('PASS' if v else 'FAIL') for k,v in bars.items()]
    lines.append('FINDING: '+finding)
    text='\n'.join(lines); print(text); (out/'ROPE_MODE013_run.log').write_text(text+'\n')
    (out/'ROPE_MODE013_results.md').write_text('# ROPE-MODE-013 — Matched topology-preserving sham test\n\n'+text.replace('\n','  \n')+'\n\nControls were frozen using geometry and full-field information only. Spectra were computed afterward; no classifier was trained.\n')
    return summary

if __name__=='__main__': main()
