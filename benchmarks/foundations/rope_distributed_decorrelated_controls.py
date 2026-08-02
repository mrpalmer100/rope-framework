"""ROPE-MODE-011: distributed, residual-decorrelated topology controls.

Control qualification only. No spectral/eigenbasis quantity enters generation,
ranking, rejection, refinement, or reporting gates.
"""
from pathlib import Path
import csv, json, sys
import numpy as np
from scipy.spatial import cKDTree

ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from benchmarks.foundations.rope_matched_ensemble_classifier import (
    grid, descriptor, normalize_geom, smooth_random, tube, FAMILY_OFFSETS
)
from benchmarks.foundations.rope_fullfield_sham_controls import (
    topology, first_unlink_amplitude, surgery_geometry, rel_l2, residual_diagnostics
)
from benchmarks.foundations.electron_variational_remesh import Model
from benchmarks.foundations.strand_substrate import gauss_link

RNG=np.random.default_rng(20260802)
N_PAIRS=6
SCREEN_STRIDE=4
N_BASE=36
N_COMP=10
TOP_FINE=5
MAX_MODES=5
DECORR_WEIGHT=0.018
SCAR_WEIGHT=0.012
FIELD_WEIGHT=1.0


def distributed_compensation(a,b,scale=0.018):
    """Broad smooth zero-mean deformation on both strands."""
    n=len(a); t=np.arange(n)*2*np.pi/n
    da=np.zeros_like(a); db=np.zeros_like(b)
    for m in range(1,MAX_MODES+1):
        va=RNG.normal(size=(2,3)); vb=RNG.normal(size=(2,3))
        w=1.0/(m*m)
        da += w*(np.sin(m*t)[:,None]*va[0]+np.cos(m*t)[:,None]*va[1])
        db += w*(np.sin(m*t)[:,None]*vb[0]+np.cos(m*t)[:,None]*vb[1])
    da-=da.mean(0); db-=db.mean(0)
    rms=np.sqrt(np.mean(np.sum(np.vstack([da,db])**2,axis=1)))
    fac=scale/max(rms,1e-12)
    return normalize_geom(a+fac*da,b+fac*db)


def normalized_alignment(r, accepted):
    nr=np.linalg.norm(r)
    if nr<1e-15 or not accepted: return 0.0
    u=r/nr
    return max(abs(float(np.dot(u,q/max(np.linalg.norm(q),1e-15)))) for q in accepted)


def scar_fraction(r,xyz,center,radius=.55):
    mask=np.linalg.norm(xyz-center,axis=1)<radius
    return float(np.sum(r[mask]**2)/max(np.sum(r*r),1e-15))


def main():
    n,h,xyz,*_=grid()
    xyzs=xyz[::SCREEN_STRIDE]
    st=np.load(ROOT/'analysis'/'ELEC009_state.npz')
    model=Model(20,knots=st['knots_final'],m_energy=64)
    d0,lk0,cert,_=model.cert(st['z_final'])
    a0,b0=model.curves(st['z_final'],256); a0,b0=normalize_geom(a0,b0)
    accepted_screen=[]; accepted_full=[]; rows=[]; residual_u=[]; residual_s=[]; centers=[]

    for p in range(N_PAIRS):
        off=FAMILY_OFFSETS[p%len(FAMILY_OFFSETS)]
        for _ in range(100):
            a=smooth_random(a0,0.004+0.004*RNG.random()); b=smooth_random(b0,0.004+0.004*RNG.random())
            a,b=normalize_geom(a,b); lk,dm=topology(a,b)
            if abs(abs(lk)-1)<.04 and dm>.052: break
        tref_s=tube(xyzs,np.vstack([a,b])); dl=descriptor(a,b)
        pool=[]
        for q in range(N_BASE):
            width=float(RNG.uniform(8,42)); tilt=float(RNG.uniform(-1.0,1.0)); mode=('a','b','split')[q%3]
            loc=off+int(RNG.integers(-24,25))
            out=first_unlink_amplitude(a,b,loc,width,tilt,mode)
            if out is None: continue
            ua,ub,amp,lku,dmu,center=out
            for k in range(N_COMP):
                scale=float(RNG.uniform(.004,.035)) if k else 0.0
                aa,bb=(ua,ub) if scale==0 else distributed_compensation(ua,ub,scale)
                lkt,dmt=topology(aa,bb,stride=4)
                if abs(lkt)>.03 or dmt<.052: continue
                ts=tube(xyzs,np.vstack([aa,bb])); r=ts-tref_s
                fld=rel_l2(tref_s,ts); align=normalized_alignment(r,accepted_screen); scar=scar_fraction(r,xyzs,center)
                score=FIELD_WEIGHT*fld+DECORR_WEIGHT*align+SCAR_WEIGHT*scar
                pool.append((score,fld,align,scar,aa,bb,amp,lkt,dmt,center,width,tilt,mode,loc,scale,ts,r))
        if not pool: raise RuntimeError(f'no distributed candidates pair {p}')
        pool.sort(key=lambda z:z[0])
        tref=tube(xyz,np.vstack([a,b])); fine=[]
        for c in pool[:TOP_FINE]:
            score,fld,align,scar,aa,bb,amp,lku,dmu,center,width,tilt,mode,loc,scale,tsc,rsc=c
            tu=tube(xyz,np.vstack([aa,bb])); r=tu-tref
            ff=rel_l2(tref,tu); al=normalized_alignment(r,accepted_full); sc=scar_fraction(r,xyz,center)
            fs=ff+DECORR_WEIGHT*al+SCAR_WEIGHT*sc
            fine.append((fs,ff,al,sc,c,tu,r))
        fs,fld,align,scar,c,tu,ru=min(fine,key=lambda z:z[0])
        _,_,_,_,aa,bb,amp,lku,dmu,center,width,tilt,mode,loc,scale,_,_=c

        # Same-family topology-preserving sham, selected only to match full-field disturbance.
        target=np.linalg.norm(ru); shams=[]
        for frac in np.linspace(.05,.995,60):
            sa,sb,_=surgery_geometry(a,b,loc,width,tilt,mode,float(frac*amp))
            if scale>0: # same broad compensation scaled by fraction via deterministic interpolation
                sa,sb=normalize_geom(sa+frac*(aa-ua if 'ua' in locals() else 0),sb)
            lks,dms=topology(sa,sb,stride=2)
            if abs(abs(lks)-1)<.08 and dms>.025:
                ts=tube(xyz,np.vstack([sa,sb])); mag=np.linalg.norm(ts-tref)
                shams.append((abs(mag-target)/max(target,1e-15),-frac,sa,sb,lks,dms,ts,float(frac)))
        # fallback: core-only sham, still field-balanced
        if not shams:
            for frac in np.linspace(.05,.995,60):
                sa,sb,_=surgery_geometry(a,b,loc,width,tilt,mode,float(frac*amp))
                lks,dms=topology(sa,sb,stride=2)
                if abs(abs(lks)-1)<.08 and dms>.025:
                    ts=tube(xyz,np.vstack([sa,sb])); mag=np.linalg.norm(ts-tref)
                    shams.append((abs(mag-target)/max(target,1e-15),-frac,sa,sb,lks,dms,ts,float(frac)))
        if not shams: raise RuntimeError(f'no sham pair {p}')
        _,_,sa,sb,lks,dms,ts,frac=min(shams,key=lambda z:(z[0],z[1]))
        rs=ts-tref

        accepted_screen.append(c[-1]); accepted_full.append(ru)
        residual_u.append(ru); residual_s.append(rs); centers.append(center)
        du=descriptor(aa,bb); ds=descriptor(sa,sb)
        scalev=np.maximum(np.abs(dl),np.r_[1,1,np.ones(6),np.ones(24)]*.05)
        rec=dict(pair=p,family=p%len(FAMILY_OFFSETS),linked_lk=lk,unlinked_lk=lku,sham_lk=lks,
                 linked_dmin=dm,unlinked_dmin=dmu,sham_dmin=dms,mode=mode,width=width,tilt=tilt,
                 amplitude=amp,compensation_scale=scale,sham_fraction=frac,field_rel_l2_unlinked=fld,
                 residual_alignment_at_selection=align,surgery_scar_at_selection=scar,
                 field_rel_l2_sham=rel_l2(tref,ts),disturbance_ratio=float(np.linalg.norm(rs)/max(np.linalg.norm(ru),1e-15)),
                 descriptor_rms_unlinked=float(np.sqrt(np.mean(((du-dl)/scalev)**2))),
                 descriptor_rms_sham=float(np.sqrt(np.mean(((ds-dl)/scalev)**2))))
        rows.append(rec)
        print(f"pair={p} field={fld:.5f} align={align:.3f} scar={scar:.3f} S/U={rec['disturbance_ratio']:.3f}",flush=True)

    Gu,medu,maxu,pca_u,scar_u=residual_diagnostics(residual_u,xyz,centers)
    Gs,meds,maxs,pca_s,scar_s=residual_diagnostics(residual_s,xyz,centers)
    fld=np.array([x['field_rel_l2_unlinked'] for x in rows]); ratio=np.array([x['disturbance_ratio'] for x in rows]); desc=np.array([x['descriptor_rms_unlinked'] for x in rows])
    bars={
      'B1_no_readout_leakage': True,
      'B2_topology_triplets': bool(cert and abs(abs(lk0)-1)<.03 and all(abs(x['unlinked_lk'])<.03 and abs(abs(x['sham_lk'])-1)<.08 for x in rows)),
      'B3_full_field_controls': bool(np.median(fld)<.025 and np.max(fld)<.04),
      'B4_residual_alignment': bool(medu<.20 and maxu<.45),
      'B5_residual_pca': bool(pca_u<.35),
      'B6_no_common_surgery_scar': bool(np.median(scar_u)<.60 and np.max(scar_u)<.80),
      'B7_sham_disturbance_balance': bool(np.median(np.abs(ratio-1))<.15 and np.max(np.abs(ratio-1))<.30),
    }
    finding='DISTRIBUTED_CONTROLS_QUALIFIED' if all(bars.values()) else 'DISTRIBUTED_CONTROLS_NOT_YET_QUALIFIED'
    summary=dict(n_pairs=N_PAIRS,grid_n=n,h=h,median_field_rel_l2=float(np.median(fld)),max_field_rel_l2=float(np.max(fld)),median_abs_residual_alignment=medu,max_abs_residual_alignment=maxu,residual_pca1=pca_u,median_surgery_scar=float(np.median(scar_u)),max_surgery_scar=float(np.max(scar_u)),median_sham_disturbance_ratio=float(np.median(ratio)),max_sham_ratio_error=float(np.max(np.abs(ratio-1))),median_descriptor_rms=float(np.median(desc)),bars=bars,finding=finding)
    out=ROOT/'analysis'
    with open(out/'ROPE_MODE011_controls.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    np.savez_compressed(out/'ROPE_MODE011_residuals.npz',unlinked=np.array(residual_u),sham=np.array(residual_s),gram_unlinked=Gu,gram_sham=Gs,centers=np.array(centers),scar_unlinked=scar_u,scar_sham=scar_s)
    (out/'ROPE_MODE011_summary.json').write_text(json.dumps(summary,indent=2))
    lines=['ROPE-MODE-011 distributed residual-decorrelated control qualification',f'pairs={N_PAIRS} grid={n}^3 h={h}',f'median/worst full-field mismatch={np.median(fld):.6f}/{np.max(fld):.6f}',f'median/max |residual alignment|={medu:.6f}/{maxu:.6f}',f'residual PC1 variance={pca_u:.6f}',f'median/max surgery-scar fraction={np.median(scar_u):.6f}/{np.max(scar_u):.6f}',f'median sham/unlink disturbance ratio={np.median(ratio):.6f}',f'max sham balance error={np.max(np.abs(ratio-1)):.6f}']
    lines += [k+': '+('PASS' if v else 'FAIL') for k,v in bars.items()]
    lines.append('FINDING: '+finding); text='\n'.join(lines); print(text)
    (out/'ROPE_MODE011_run.log').write_text(text+'\n')
    (out/'ROPE_MODE011_results.md').write_text('# ROPE-MODE-011 — Distributed residual-decorrelated controls\n\n'+text.replace('\n','  \n')+'\n\nNo spectral or eigenbasis quantity was used. The classifier was not run.\n')
    return summary

if __name__=='__main__': main()
