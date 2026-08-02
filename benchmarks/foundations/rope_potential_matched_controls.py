"""ROPE-MODE-009: optimize linked/unlinked controls against the sampled tube field.

This benchmark does not expand the classifier. It asks whether local unlinking
controls can be made substantially better matched by optimizing the entire
sampled tubular potential, rather than only low-order geometric summaries.
"""
from pathlib import Path
import csv, json, sys
import numpy as np
from scipy.spatial import cKDTree

ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from benchmarks.foundations.rope_matched_ensemble_classifier import (
    grid, descriptor, normalize_geom, smooth_random, surgery, tube,
    FAMILY_OFFSETS, RNG, N_FAMILIES, PER_FAMILY, SIGMA
)
from benchmarks.foundations.electron_variational_remesh import Model
from benchmarks.foundations.strand_substrate import gauss_link

# Control-only benchmark: more candidate diversity than MODE-008.
N_PAIRS=5
SCREEN_STRIDE=3
N_CANDIDATES=140
TOP_FINE=8


def field_metrics(t_ref,t_ctl,U):
    d=t_ctl-t_ref
    rel_l2=float(np.linalg.norm(d)/max(np.linalg.norm(t_ref),1e-15))
    rel_l1=float(np.mean(np.abs(d))/max(np.mean(np.abs(t_ref)),1e-15))
    corr=float(np.corrcoef(t_ref,t_ctl)[0,1])
    # The Hamiltonian only sees U^T diag(t) U in the reduced low-energy sector.
    Mr=U.T@(t_ref[:,None]*U); Mc=U.T@(t_ctl[:,None]*U)
    op_rel=float(np.linalg.norm(Mc-Mr)/max(np.linalg.norm(Mr),1e-15))
    return rel_l2,rel_l1,corr,op_rel


def main():
    n,h,xyz,r,Hc,ec,U=grid()
    xyz_screen=xyz[::SCREEN_STRIDE]
    st=np.load(ROOT/'analysis'/'ELEC009_state.npz')
    model=Model(20,knots=st['knots_final'],m_energy=64)
    d0,lk0,cert,_=model.cert(st['z_final'])
    a0,b0=model.curves(st['z_final'],256); a0,b0=normalize_geom(a0,b0)
    rows=[]; pair_results=[]
    offsets=list(FAMILY_OFFSETS)
    for p in range(N_PAIRS):
        fi=p%len(offsets); off=offsets[fi]
        # independent linked perturbation
        for _ in range(60):
            a=smooth_random(a0,0.004+0.004*RNG.random()); b=smooth_random(b0,0.004+0.004*RNG.random()); a,b=normalize_geom(a,b)
            lk=float(gauss_link(a[::2],b[::2])); dm=float(np.min(cKDTree(a).query(b,k=1)[0]))
            if abs(abs(lk)-1)<.04 and dm>.052: break
        dl=descriptor(a,b)
        tref_s=tube(xyz_screen,np.vstack([a,b]))
        candidates=[]
        for q in range(N_CANDIDATES):
            width=float(RNG.uniform(8,42)); tilt=float(RNG.uniform(-0.9,0.9)); mode=('a','b','split')[q%3]
            jitter=int(RNG.integers(-18,19))
            out=surgery(a,b,off+jitter,width,tilt,mode)
            if out is None: continue
            aa,bb,amp,lku,dmu=out
            tu_s=tube(xyz_screen,np.vstack([aa,bb]))
            rel_s=float(np.linalg.norm(tu_s-tref_s)/max(np.linalg.norm(tref_s),1e-15))
            du=descriptor(aa,bb)
            # Light descriptor penalty prevents field matching by gross geometry drift.
            scale=np.maximum(np.abs(dl),np.r_[1,1,np.ones(6),np.ones(24)]*0.05)
            dscore=float(np.sqrt(np.mean(((du-dl)/scale)**2)))
            score=rel_s+0.08*dscore
            candidates.append((score,rel_s,dscore,aa,bb,amp,lku,dmu,width,tilt,mode,du))
        if not candidates: raise RuntimeError(f'no candidates pair {p}')
        candidates.sort(key=lambda z:z[0])
        tref=tube(xyz,np.vstack([a,b]))
        fine=[]
        for c in candidates[:TOP_FINE]:
            score,rel_s,dscore,aa,bb,amp,lku,dmu,width,tilt,mode,du=c
            tu=tube(xyz,np.vstack([aa,bb]))
            fm=field_metrics(tref,tu,U)
            # Primary fine criterion is full-field L2, then low-energy operator mismatch.
            fine_score=fm[0]+0.35*fm[3]+0.05*dscore
            fine.append((fine_score,fm,c,tu))
        best=min(fine,key=lambda z:z[0])
        fine_score,fm,c,tu=best
        score,rel_s,dscore,aa,bb,amp,lku,dmu,width,tilt,mode,du=c
        # summarize descriptor differences as paired standardized-like relative RMS
        scale=np.maximum(np.abs(dl),np.r_[1,1,np.ones(6),np.ones(24)]*0.05)
        desc_rel=np.abs((du-dl)/scale)
        rec=dict(pair=p,family=fi,linked_lk=lk,unlinked_lk=lku,linked_dmin=dm,unlinked_dmin=dmu,
                 mode=mode,width=width,tilt=tilt,amplitude=amp,screen_rel_l2=rel_s,
                 field_rel_l2=fm[0],field_rel_l1=fm[1],field_corr=fm[2],operator_rel=fm[3],
                 descriptor_rms=dscore,descriptor_max=float(np.max(desc_rel)),fine_score=fine_score)
        pair_results.append(rec)
        rows.append(rec)
        print(f"pair={p} fieldL2={fm[0]:.5f} op={fm[3]:.5f} corr={fm[2]:.6f} desc={dscore:.4f} Lk={lku:.2g}",flush=True)

    fld=np.array([r['field_rel_l2'] for r in rows]); op=np.array([r['operator_rel'] for r in rows]); corr=np.array([r['field_corr'] for r in rows]); desc=np.array([r['descriptor_rms'] for r in rows])
    bars={
      'B1_topology_controls': bool(cert and abs(abs(lk0)-1)<.03 and all(abs(r['unlinked_lk'])<.02 for r in rows)),
      'B2_full_field_match_median': bool(np.median(fld)<0.10),
      'B3_full_field_match_worst': bool(np.max(fld)<0.15),
      'B4_low_energy_operator_match': bool(np.max(op)<0.08),
      'B5_field_correlation': bool(np.min(corr)>0.985),
      'B6_descriptor_pair_match': bool(np.median(desc)<0.10),
    }
    finding='FULL_POTENTIAL_MATCHED_CONTROLS_READY' if all(bars.values()) else ('CONTROLS_IMPROVED_BUT_NOT_FULLY_MATCHED' if np.median(fld)<0.15 else 'FULL_POTENTIAL_MATCHING_FAILED')
    summary={
      'n_pairs':N_PAIRS,'grid_n':n,'h':h,'sigma':SIGMA,
      'median_field_rel_l2':float(np.median(fld)),'max_field_rel_l2':float(np.max(fld)),
      'median_operator_rel':float(np.median(op)),'max_operator_rel':float(np.max(op)),
      'min_field_corr':float(np.min(corr)),'median_descriptor_rms':float(np.median(desc)),
      'bars':bars,'finding':finding
    }
    out=ROOT/'analysis'
    with open(out/'ROPE_MODE009_controls.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    (out/'ROPE_MODE009_summary.json').write_text(json.dumps(summary,indent=2))
    lines=['ROPE-MODE-009 full-potential matched controls',f'pairs={N_PAIRS} grid={n}^3 h={h}',
           f'median full-field relative L2={summary["median_field_rel_l2"]:.6f}',f'worst full-field relative L2={summary["max_field_rel_l2"]:.6f}',
           f'median low-energy operator mismatch={summary["median_operator_rel"]:.6f}',f'worst low-energy operator mismatch={summary["max_operator_rel"]:.6f}',
           f'minimum field correlation={summary["min_field_corr"]:.6f}',f'median descriptor RMS={summary["median_descriptor_rms"]:.6f}']
    lines += [k+': '+('PASS' if v else 'FAIL') for k,v in bars.items()]
    lines.append('FINDING: '+finding)
    text='\n'.join(lines); print(text); (out/'ROPE_MODE009_run.log').write_text(text+'\n')
    (out/'ROPE_MODE009_results.md').write_text('# ROPE-MODE-009 — Full-potential matched controls\n\n'+text.replace('\n','  \n')+'\n\nThis benchmark improves controls only; it does not rerun or expand the blinded classifier.\n')
    return summary

if __name__=='__main__': main()
