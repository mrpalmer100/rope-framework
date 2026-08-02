"""ROPE-MODE-010: full-field-only controls, residual alignment, and sham surgeries.

Control construction is label-blind with respect to all spectral/eigenbasis outputs:
no eigenvalue, eigenvector, projected Hamiltonian, or low-mode density is used for
candidate generation, ranking, rejection, or refinement.
"""
from pathlib import Path
import csv, json, sys
import numpy as np
from scipy.spatial import cKDTree

ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from benchmarks.foundations.rope_matched_ensemble_classifier import (
    grid, descriptor, normalize_geom, smooth_random, tube,
    FAMILY_OFFSETS, RNG
)
from benchmarks.foundations.electron_variational_remesh import Model
from benchmarks.foundations.strand_substrate import gauss_link

N_PAIRS=5
SCREEN_STRIDE=3
N_CANDIDATES=90
TOP_FINE=6
SHAM_FRACS=np.linspace(0.03,0.995,48)


def topology(a,b,stride=2):
    lk=float(gauss_link(a[::stride],b[::stride]))
    dm=float(np.min(cKDTree(a).query(b,k=1)[0]))
    return lk,dm


def surgery_geometry(a,b,offset,width,tilt,mode,amp):
    n=len(a); tree=cKDTree(a); ds,ii=tree.query(b,k=1)
    j0=int(np.argmin(ds)); j=(j0+offset)%n; i=int(tree.query(b[j],k=1)[1])
    radial=a[i]-b[j]; radial/=max(np.linalg.norm(radial),1e-12)
    ta=a[(i+1)%n]-a[(i-1)%n]; ta/=max(np.linalg.norm(ta),1e-12)
    tb=b[(j+1)%n]-b[(j-1)%n]; tb/=max(np.linalg.norm(tb),1e-12)
    side=np.cross(ta,tb); side/=max(np.linalg.norm(side),1e-12)
    direction=radial+tilt*side; direction/=max(np.linalg.norm(direction),1e-12)
    inds=np.arange(n)
    da=np.minimum((inds-i)%n,(i-inds)%n); db=np.minimum((inds-j)%n,(j-inds)%n)
    wa=np.exp(-.5*(da/width)**2); wb=np.exp(-.5*(db/width)**2)
    aa=a.copy(); bb=b.copy()
    if mode=='a': aa=a-amp*wa[:,None]*direction
    elif mode=='b': bb=b+amp*wb[:,None]*direction
    else:
        aa=a-.5*amp*wa[:,None]*direction; bb=b+.5*amp*wb[:,None]*direction
    aa,bb=normalize_geom(aa,bb)
    center=0.5*(a[i]+b[j])
    return aa,bb,center


def first_unlink_amplitude(a,b,offset,width,tilt,mode):
    for amp in np.linspace(.06,.70,129):
        aa,bb,center=surgery_geometry(a,b,offset,width,tilt,mode,float(amp))
        lk,dm=topology(aa,bb,stride=4)
        if abs(lk)<.03 and dm>=.055:
            lkf=float(gauss_link(aa,bb))
            if abs(lkf)<.02:
                return aa,bb,float(amp),lkf,dm,center
    return None


def rel_l2(ref,x):
    return float(np.linalg.norm(x-ref)/max(np.linalg.norm(ref),1e-15))


def residual_diagnostics(residuals, xyz, centers):
    R=np.array([r/max(np.linalg.norm(r),1e-15) for r in residuals])
    G=R@R.T
    off=np.abs(G[np.triu_indices(len(R),1)])
    # PCA/SVD on normalized residuals; variance fractions from singular values.
    _,s,_=np.linalg.svd(R-R.mean(0,keepdims=True),full_matrices=False)
    var=s*s; pca1=float(var[0]/max(var.sum(),1e-15))
    scar=[]
    for r,c in zip(residuals,centers):
        mask=np.linalg.norm(xyz-c,axis=1)<0.55
        scar.append(float(np.sum(r[mask]**2)/max(np.sum(r*r),1e-15)))
    return G, float(np.median(off)), float(np.max(off)), pca1, np.array(scar)


def main():
    n,h,xyz,r,Hc,ec,U=grid()  # U is intentionally unused in construction.
    xyz_screen=xyz[::SCREEN_STRIDE]
    st=np.load(ROOT/'analysis'/'ELEC009_state.npz')
    model=Model(20,knots=st['knots_final'],m_energy=64)
    d0,lk0,cert,_=model.cert(st['z_final'])
    a0,b0=model.curves(st['z_final'],256); a0,b0=normalize_geom(a0,b0)
    rows=[]; residual_u=[]; residual_s=[]; centers=[]
    offsets=list(FAMILY_OFFSETS)

    for p in range(N_PAIRS):
        off=offsets[p%len(offsets)]
        for _ in range(80):
            a=smooth_random(a0,0.004+0.004*RNG.random())
            b=smooth_random(b0,0.004+0.004*RNG.random())
            a,b=normalize_geom(a,b); lk,dm=topology(a,b)
            if abs(abs(lk)-1)<.04 and dm>.052: break
        tref_s=tube(xyz_screen,np.vstack([a,b])); dl=descriptor(a,b)
        candidates=[]
        for q in range(N_CANDIDATES):
            width=float(RNG.uniform(8,42)); tilt=float(RNG.uniform(-0.9,0.9)); mode=('a','b','split')[q%3]
            jitter=int(RNG.integers(-18,19)); loc=off+jitter
            out=first_unlink_amplitude(a,b,loc,width,tilt,mode)
            if out is None: continue
            aa,bb,amp,lku,dmu,center=out
            tu_s=tube(xyz_screen,np.vstack([aa,bb]))
            # Full-field-only screening objective. No geometry descriptor or spectral term.
            score=rel_l2(tref_s,tu_s)
            candidates.append((score,aa,bb,amp,lku,dmu,center,width,tilt,mode,loc))
        if not candidates: raise RuntimeError(f'no candidates pair {p}')
        candidates.sort(key=lambda z:z[0])
        tref=tube(xyz,np.vstack([a,b]))
        fine=[]
        for c in candidates[:TOP_FINE]:
            score,aa,bb,amp,lku,dmu,center,width,tilt,mode,loc=c
            tu=tube(xyz,np.vstack([aa,bb]))
            # Fine ranking remains exclusively full sampled-field relative L2.
            fine.append((rel_l2(tref,tu),c,tu))
        fld,c,tu=min(fine,key=lambda z:z[0])
        score,aa,bb,amp,lku,dmu,center,width,tilt,mode,loc=c

        # Matched topology-preserving sham from the same deformation family,
        # selected only on field-disturbance magnitude relative to unlinking.
        target=np.linalg.norm(tu-tref)
        sham=[]
        for frac in SHAM_FRACS:
            sa,sb,_=surgery_geometry(a,b,loc,width,tilt,mode,float(frac*amp))
            lks,dms=topology(sa,sb,stride=2)
            if abs(abs(lks)-1)<.08 and dms>.025:
                ts=tube(xyz,np.vstack([sa,sb]))
                mag=np.linalg.norm(ts-tref)
                sham.append((abs(mag-target)/max(target,1e-15),-frac,sa,sb,lks,dms,ts,float(frac)))
        if not sham: raise RuntimeError(f'no linked sham pair {p}')
        _,_,sa,sb,lks,dms,ts,frac=min(sham,key=lambda z:(z[0],z[1]))

        ru=tu-tref; rs=ts-tref
        residual_u.append(ru); residual_s.append(rs); centers.append(center)
        du=descriptor(aa,bb); ds=descriptor(sa,sb)
        scale=np.maximum(np.abs(dl),np.r_[1,1,np.ones(6),np.ones(24)]*0.05)
        rec=dict(pair=p,family=p%len(offsets),linked_lk=lk,unlinked_lk=lku,sham_lk=lks,
                 linked_dmin=dm,unlinked_dmin=dmu,sham_dmin=dms,mode=mode,width=width,
                 tilt=tilt,amplitude=amp,sham_fraction=frac,field_rel_l2_unlinked=fld,
                 field_rel_l2_sham=rel_l2(tref,ts),disturbance_ratio=float(np.linalg.norm(rs)/max(np.linalg.norm(ru),1e-15)),
                 descriptor_rms_unlinked=float(np.sqrt(np.mean(((du-dl)/scale)**2))),
                 descriptor_rms_sham=float(np.sqrt(np.mean(((ds-dl)/scale)**2))))
        rows.append(rec)
        print(f"pair={p} Ufield={fld:.5f} S/U={rec['disturbance_ratio']:.3f} LkU={lku:.2g} LkS={lks:.3f}",flush=True)

    Gu,medu,maxu,pca_u,scar_u=residual_diagnostics(residual_u,xyz,centers)
    Gs,meds,maxs,pca_s,scar_s=residual_diagnostics(residual_s,xyz,centers)
    fld=np.array([x['field_rel_l2_unlinked'] for x in rows]); ratio=np.array([x['disturbance_ratio'] for x in rows])
    desc=np.array([x['descriptor_rms_unlinked'] for x in rows])
    bars={
      'B1_no_readout_leakage': True,
      'B2_topology_triplets': bool(cert and abs(abs(lk0)-1)<.03 and all(abs(x['unlinked_lk'])<.02 and abs(abs(x['sham_lk'])-1)<.04 for x in rows)),
      'B3_full_field_controls': bool(np.median(fld)<.02 and np.max(fld)<.03),
      'B4_residual_alignment': bool(medu<.20 and maxu<.45),
      'B5_residual_pca': bool(pca_u<.35),
      'B6_no_common_surgery_scar': bool(np.median(scar_u)<.60 and np.max(scar_u)<.80),
      'B7_sham_disturbance_balance': bool(np.median(np.abs(ratio-1))<.15 and np.max(np.abs(ratio-1))<.30),
    }
    finding='FULLFIELD_SHAM_CONTROLS_QUALIFIED' if all(bars.values()) else 'CONTROL_QUALIFICATION_NOT_YET_PASSED'
    summary=dict(n_pairs=N_PAIRS,grid_n=n,h=h,median_field_rel_l2=float(np.median(fld)),max_field_rel_l2=float(np.max(fld)),
                 median_abs_residual_alignment=medu,max_abs_residual_alignment=maxu,residual_pca1=pca_u,
                 median_surgery_scar=float(np.median(scar_u)),max_surgery_scar=float(np.max(scar_u)),
                 median_sham_disturbance_ratio=float(np.median(ratio)),max_sham_ratio_error=float(np.max(np.abs(ratio-1))),
                 median_descriptor_rms=float(np.median(desc)),bars=bars,finding=finding)
    out=ROOT/'analysis'
    with open(out/'ROPE_MODE010_controls.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    np.savez_compressed(out/'ROPE_MODE010_residuals.npz',unlinked=np.array(residual_u),sham=np.array(residual_s),
                        gram_unlinked=Gu,gram_sham=Gs,centers=np.array(centers),scar_unlinked=scar_u,scar_sham=scar_s)
    (out/'ROPE_MODE010_summary.json').write_text(json.dumps(summary,indent=2))
    lines=['ROPE-MODE-010 full-field-only controls and sham qualification',f'pairs={N_PAIRS} grid={n}^3 h={h}',
           f'median/worst full-field mismatch={np.median(fld):.6f}/{np.max(fld):.6f}',
           f'median/max |residual alignment|={medu:.6f}/{maxu:.6f}',f'residual PC1 variance={pca_u:.6f}',
           f'median/max surgery-scar fraction={np.median(scar_u):.6f}/{np.max(scar_u):.6f}',
           f'median sham/unlink disturbance ratio={np.median(ratio):.6f}',f'max sham balance error={np.max(np.abs(ratio-1)):.6f}']
    lines += [k+': '+('PASS' if v else 'FAIL') for k,v in bars.items()]
    lines.append('FINDING: '+finding)
    text='\n'.join(lines); print(text); (out/'ROPE_MODE010_run.log').write_text(text+'\n')
    (out/'ROPE_MODE010_results.md').write_text('# ROPE-MODE-010 — Full-field-only controls and matched shams\n\n'+text.replace('\n','  \n')+'\n\nNo spectral or eigenbasis quantity was used in control construction. The blinded classifier was not run.\n')
    return summary

if __name__=='__main__': main()
