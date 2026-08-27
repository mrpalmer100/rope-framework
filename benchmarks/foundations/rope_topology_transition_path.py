"""ROPE-MODE-012: continuous near-crossing topology-transition path test.

Tests whether low bound-state excitation gaps exhibit a discontinuity or non-smooth
feature when a smooth local deformation crosses from the linked to unlinked sector.
No classifier is trained. Geometry and field paths are fixed before spectral solves.
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

BOX=4.0
H=0.25
ALPHA=12.0
EPS=0.30
BETA=0.50
N_EIG=4
SIGMA=0.16
# Independent deformation families: offset, width, tilt, moved strand.
FAMILIES=[
    (0,18.0,-0.65,'a'),
    (-52,38.0665422445,-0.6509443677,'split'),
    (-30,40.5072345966,0.0878828015,'a'),
    (-39,26.7003733344,-0.1390074445,'b'),
    (97,37.6131351141,0.9683059999,'split'),
]
DELTA_FRACS=np.array([0.015,0.03,0.06,0.10])
LINK_TOL=0.15
UNLINK_TOL=0.15


def build_grid():
    n=int(round(2*BOX/H))-1
    h=2*BOX/(n+1)
    x=np.linspace(-BOX,BOX,n+2)[1:-1]
    X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
    xyz=np.column_stack([X.ravel(),Y.ravel(),Z.ravel()])
    I=eye(n,format='csr'); L=lap1(n,h)
    H0=kron(kron(L,I),I)+kron(kron(I,L),I)+kron(kron(I,I),L)
    r=np.linalg.norm(xyz,axis=1)
    Vc=-ALPHA/np.sqrt(r*r+EPS*EPS)
    return n,h,xyz,H0,Vc,r


def solve(H0,Vc,xyz,a,b):
    T=tube(xyz,np.vstack([a,b]))
    Hm=H0+diags(Vc-BETA*T,0,format='csr')
    vals=eigsh(Hm,k=N_EIG,which='SA',tol=8e-8,maxiter=12000,return_eigenvectors=False)
    vals=np.sort(vals)
    return vals, vals-vals[0], T


def sector(lk):
    if abs(abs(lk)-1)<LINK_TOL: return 'linked'
    if abs(lk)<UNLINK_TOL: return 'unlinked'
    return 'transition'


def find_transition(a,b,fam):
    off,width,tilt,mode=fam
    amps=np.linspace(0.0,0.8,321)
    vals=[]
    for amp in amps:
        aa,bb,c=surgery_geometry(a,b,off,width,tilt,mode,float(amp))
        lk,dm=topology(aa,bb,stride=2)
        vals.append((amp,lk,dm,aa,bb,c))
    # first robust unlinked state following linked states
    idx=None
    for i in range(1,len(vals)):
        if sector(vals[i-1][1])=='linked' and sector(vals[i][1])=='unlinked': idx=i; break
    if idx is None:
        # broader bracket: last linked before first unlinked
        li=max([i for i,v in enumerate(vals) if sector(v[1])=='linked'],default=None)
        ui=min([i for i,v in enumerate(vals) if sector(v[1])=='unlinked' and (li is None or i>li)],default=None)
        if li is None or ui is None: return None
    else: li,ui=idx-1,idx
    lo,hi=vals[li][0],vals[ui][0]
    # Binary search sector boundary. Intermediate values can be transition/intersection.
    for _ in range(18):
        mid=0.5*(lo+hi)
        aa,bb,c=surgery_geometry(a,b,off,width,tilt,mode,float(mid))
        lk,dm=topology(aa,bb,stride=1)
        if sector(lk)=='linked': lo=mid
        else: hi=mid
    return 0.5*(lo+hi), lo, hi


def linear_intercept(x,y):
    # y shape (m,3); independent linear fit for each mode.
    A=np.column_stack([np.ones_like(x),x])
    coef=np.linalg.lstsq(A,y,rcond=None)[0]
    return coef[0],coef[1]


def main():
    n,h,xyz,H0,Vc,r=build_grid()
    st=np.load(ROOT/'analysis'/'ELEC009_state.npz')
    model=Model(20,knots=st['knots_final'],m_energy=64)
    d0,lk0,cert,_=model.cert(st['z_final'])
    a0,b0=model.curves(st['z_final'],256); a0,b0=normalize_geom(a0,b0)
    rows=[]; summaries=[]
    print(f'ROPE-MODE-012 grid={n}^3 h={h:.6f} reference cert={cert} Lk={lk0:.8f} dmin={d0:.8f}',flush=True)
    for fi,fam in enumerate(FAMILIES):
        trans=find_transition(a0,b0,fam)
        if trans is None:
            print(f'family {fi}: no transition',flush=True); continue
        tc,lo,hi=trans
        scale=max(tc,0.1)
        xs=[]; gaps=[]; fields=[]
        for sign in (-1,1):
            for frac in DELTA_FRACS:
                amp=max(0.0,tc+sign*frac*scale)
                aa,bb,c=surgery_geometry(a0,b0,*fam,float(amp))
                lk,dm=topology(aa,bb,stride=1)
                t0=time.time(); vals,g,T=solve(H0,Vc,xyz,aa,bb)
                x=(amp-tc)/scale
                xs.append(x); gaps.append(g[1:]); fields.append(T)
                rows.append(dict(family=fi,offset=fam[0],width=fam[1],tilt=fam[2],mode=fam[3],tc=tc,x=x,amplitude=amp,lk=lk,dmin=dm,sector=sector(lk),E0=vals[0],gap1=g[1],gap2=g[2],gap3=g[3],elapsed=time.time()-t0))
                print(f'family={fi} x={x:+.4f} Lk={lk:+.4f} dmin={dm:.5f} gaps={g[1:]}',flush=True)
        xs=np.array(xs); gaps=np.array(gaps); fields=np.array(fields)
        neg=xs<0; pos=xs>0
        iL,sL=linear_intercept(xs[neg],gaps[neg]); iR,sR=linear_intercept(xs[pos],gaps[pos])
        jump=iR-iL
        # Local smoothness scale: expected variation across smallest symmetric interval.
        fmin=DELTA_FRACS.min()
        gneg=gaps[np.argmin(np.abs(xs+fmin))]; gpos=gaps[np.argmin(np.abs(xs-fmin))]
        cross=gpos-gneg
        # Curvature/nonlinearity estimate from residuals to side fits.
        predL=iL[None,:]+xs[neg,None]*sL[None,:]
        predR=iR[None,:]+xs[pos,None]*sR[None,:]
        fit_rms=np.sqrt(np.mean(np.vstack([gaps[neg]-predL,gaps[pos]-predR])**2,axis=0))
        # Field continuity at nearest symmetric pair.
        Tneg=fields[np.argmin(np.abs(xs+fmin))]; Tpos=fields[np.argmin(np.abs(xs-fmin))]
        field_rel=float(np.linalg.norm(Tpos-Tneg)/max(np.linalg.norm(0.5*(Tpos+Tneg)),1e-15))
        summaries.append(dict(family=fi,tc=tc,jump1=jump[0],jump2=jump[1],jump3=jump[2],fit_rms1=fit_rms[0],fit_rms2=fit_rms[1],fit_rms3=fit_rms[2],cross1=cross[0],cross2=cross[1],cross3=cross[2],field_near_rel=field_rel,slope_change_norm=float(np.linalg.norm(sR-sL))))

    if not summaries: raise RuntimeError('No valid transition paths')
    J=np.array([[s['jump1'],s['jump2'],s['jump3']] for s in summaries])
    R=np.array([[s['fit_rms1'],s['fit_rms2'],s['fit_rms3']] for s in summaries])
    C=np.array([[s['cross1'],s['cross2'],s['cross3']] for s in summaries])
    # A discontinuity is meaningful only if extrapolated jump exceeds both fit error and local smooth change.
    excess=np.abs(J)/np.maximum(3*R+0.25*np.abs(C),1e-7)
    significant=excess>1.0
    # Require same mode/sign in at least 3 families for a topology-boundary feature.
    robust=[]
    for m in range(3):
        sig=np.where(significant[:,m])[0]
        if len(sig)>=3:
            signs=np.sign(J[sig,m]); robust.append(max(np.sum(signs>0),np.sum(signs<0))>=3)
        else: robust.append(False)
    max_field=max(s['field_near_rel'] for s in summaries)
    bars={
      'B1_reference_and_paths_certified': bool(cert and abs(abs(lk0)-1)<.03 and len(summaries)>=3),
      'B2_both_topology_sectors_sampled': bool(all(any(r['family']==s['family'] and r['sector']=='linked' for r in rows) and any(r['family']==s['family'] and r['sector']=='unlinked' for r in rows) for s in summaries)),
      'B3_field_path_continuous_near_transition': bool(max_field<0.08),
      'B4_spectral_discontinuity_detected': bool(any(robust)),
      'B5_discontinuity_robust_across_families': bool(any(robust)),
    }
    finding='TOPOLOGY_TRANSITION_SPECTRAL_NONSMOOTHNESS_DETECTED' if bars['B4_spectral_discontinuity_detected'] and bars['B5_discontinuity_robust_across_families'] else 'SPECTRUM_CONTINUOUS_THROUGH_TOPOLOGY_TRANSITION'
    summary=dict(grid_n=n,h=h,n_families=len(summaries),max_near_transition_field_rel=max_field,max_jump=float(np.max(np.abs(J))),median_jump=float(np.median(np.abs(J))),max_excess_ratio=float(np.max(excess)),robust_modes=robust,bars=bars,finding=finding)
    out=ROOT/'analysis'
    with open(out/'ROPE_MODE012_path.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    with open(out/'ROPE_MODE012_families.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(summaries[0].keys())); w.writeheader(); w.writerows(summaries)
    # numpy>=2 portability (2026-08-19): np.bool_/np.float64 scalars are not
    # JSON-serializable under stdlib json; .item() unwraps them. Physics
    # upstream of this line is untouched -- this is the artifact writer.
    (out/'ROPE_MODE012_summary.json').write_text(json.dumps(
        summary, indent=2,
        default=lambda o: o.item() if hasattr(o, 'item') else str(o)))
    lines=['ROPE-MODE-012 continuous topology-transition path test',f'grid={n}^3 h={h:.6f} families={len(summaries)}',f'max near-transition field relative difference={max_field:.6g}',f'median/max extrapolated spectral jump={np.median(np.abs(J)):.6g}/{np.max(np.abs(J)):.6g}',f'max jump excess ratio={np.max(excess):.6g}',f'robust discontinuity modes={robust}']
    lines += [k+': '+('PASS' if v else 'FAIL') for k,v in bars.items()]
    lines.append('FINDING: '+finding)
    text='\n'.join(lines); print(text)
    (out/'ROPE_MODE012_run.log').write_text(text+'\n')
    (out/'ROPE_MODE012_results.md').write_text('# ROPE-MODE-012 — Continuous topology-transition path\n\n'+text.replace('\n','  \n')+'\n\nThe spectral readout was evaluated only after each deformation path and transition bracket were fixed. No classifier was trained.\n')
    return summary

if __name__=='__main__': main()
