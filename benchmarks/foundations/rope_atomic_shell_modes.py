"""ROPE-MODE-001: standing-wave spectrum on the certified linked rope geometry.

Core question: do natural longitudinal/transverse standing modes of the present
rope geometry generate a discrete hierarchy that resembles atomic shell
spacing, rather than merely the ordinary harmonics of a closed string?

This is a geometry-and-kinematics gate.  It does not add electron dynamics or
claim an atom model.  Constant tension and linear mass density are set to one,
so only dimensionless frequency ratios are interpreted.
"""
from pathlib import Path
import csv, sys
import numpy as np
from scipy.linalg import eigh

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from benchmarks.foundations.electron_variational_remesh import Model

LEVELS = (128, 256, 512)
N_MODES = 10                 # positive frequency modes per component
CONV_TOL = 0.01              # 256->512 relative frequency agreement
HARMONIC_R2_BAR = 0.995
SHELL_ADVANTAGE_BAR = 0.10   # shell template must improve RMS error by >=10%


def periodic_fem_spectrum(curve, nmodes=N_MODES):
    """Linear string FEM on a closed nonuniform polygon.

    Stiffness corresponds to integral |du/ds|^2 ds and the consistent mass
    matrix to integral u^2 ds.  Tension and linear density are unity.
    """
    x = np.asarray(curve, float)
    n = len(x)
    ell = np.linalg.norm(np.roll(x, -1, axis=0) - x, axis=1)
    if np.min(ell) <= 1e-12:
        raise ValueError("degenerate curve segment")
    K = np.zeros((n, n)); M = np.zeros((n, n))
    for i, h in enumerate(ell):
        j = (i + 1) % n
        ke = np.array([[1., -1.], [-1., 1.]]) / h
        me = h * np.array([[2., 1.], [1., 2.]]) / 6.
        idx = np.ix_([i, j], [i, j])
        K[idx] += ke; M[idx] += me
    vals, vecs = eigh(K, M, subset_by_index=[0, min(n-1, 2*nmodes+4)])
    vals = np.maximum(vals, 0.)
    omega = np.sqrt(vals)
    # The first periodic eigenvalue is the constant displacement mode.  Drop it
    # by index rather than an absolute threshold because roundoff scales with M.
    omega = omega[1:1+nmodes]
    return omega, ell.sum()


def grouped_pair_frequencies(omega):
    """Average the nearly degenerate sine/cosine pairs of a closed string."""
    m = (len(omega)//2)*2
    return omega[:m].reshape(-1,2).mean(axis=1)


def fit_template(y, template):
    a = float(np.dot(y, template) / np.dot(template, template))
    pred = a * template
    rmse = float(np.sqrt(np.mean((y-pred)**2)))
    ss = float(np.sum((y-y.mean())**2))
    r2 = 1.0 - float(np.sum((y-pred)**2))/ss if ss > 0 else float('nan')
    return a, pred, rmse, r2


def run():
    state = np.load(ROOT/'analysis'/'ELEC009_state.npz')
    z = state['z_final']; knots = state['knots_final']
    model = Model(20, knots=knots, m_energy=64)
    d, lk, cert, certvals = model.cert(z)

    rows=[]; spectra={}
    for M in LEVELS:
        curves = model.curves(z, M)
        spectra[M]=[]
        for strand,c in enumerate(curves):
            omega,L = periodic_fem_spectrum(c)
            pairs = grouped_pair_frequencies(omega)
            spectra[M].append(pairs)
            for k,w in enumerate(pairs, start=1):
                rows.append((M,strand,k,L,w,w/pairs[0]))

    # Resolution convergence on pair-averaged ratios.
    conv=[]
    for s in range(2):
        a=spectra[256][s]; b=spectra[512][s]
        conv.extend(np.abs(b-a)/np.maximum(np.abs(b),1e-14))
    max_conv=float(np.max(conv))

    # Pool both strands after normalization by each fundamental.
    y=np.concatenate([q/q[0] for q in spectra[512]])
    n=np.tile(np.arange(1,len(spectra[512][0])+1,dtype=float),2)
    # Ordinary closed-string template: omega_n proportional to n.
    ah,ph,err_h,r2_h=fit_template(y,n)
    # Atomic-shell-inspired templates.  Hydrogen binding magnitude scales 1/n^2;
    # excitation from the ground approaches 1-1/n^2.  Neither has a nonzero n=1
    # frequency, so compare n>=2 after allowing a scale only.
    mask=n>=2
    shell_bind=1.0/(n[mask]**2)
    shell_exc=1.0-1.0/(n[mask]**2)
    _,_,err_b,r2_b=fit_template(y[mask],shell_bind)
    _,_,err_e,r2_e=fit_template(y[mask],shell_exc)
    err_shell=min(err_b,err_e); best_shell='1/n^2' if err_b<=err_e else '1-1/n^2'
    shell_adv=(err_h-err_shell)/err_h

    # Degeneracy diagnostic: each spatial harmonic is a sine/cosine pair on
    # each strand (four scalar modes total), unlike atomic shell capacities 2n^2.
    observed_deg=4
    expected_shell=np.array([2*n0*n0 for n0 in range(1,len(spectra[512][0])+1)])
    degeneracy_match=bool(np.all(expected_shell==observed_deg))

    B1=bool(cert and d>=0.060 and abs(abs(lk)-1)<=0.03)
    B2=max_conv<CONV_TOL
    B3=r2_h>HARMONIC_R2_BAR
    B4=shell_adv>=SHELL_ADVANTAGE_BAR
    B5=degeneracy_match
    finding = ('SHELL_LIKE_NORMAL_MODE_SPECTRUM' if all((B1,B2,B4,B5)) else
               'DISCRETE_MODES_BUT_ORDINARY_STRING_HARMONICS')

    with open(ROOT/'analysis'/'ROPE_MODE001_spectrum.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['samples','strand','harmonic_index','curve_length','omega_pair_mean','omega_over_fundamental']); w.writerows(rows)
    np.savez(ROOT/'analysis'/'ROPE_MODE001_spectrum.npz',levels=np.array(LEVELS),
             strand0=spectra[512][0],strand1=spectra[512][1],
             harmonic_fit=ph,normalized_data=y)
    out=[]
    out.append('ROPE-MODE-001 standing-wave spectrum')
    out.append(f'certified={cert} dmin={d:.8f} Lk512={lk:.8f}')
    out.append(f'max 256->512 frequency change={max_conv:.6g}')
    out.append('strand 0 normalized pairs: '+', '.join(f'{v/spectra[512][0][0]:.6f}' for v in spectra[512][0]))
    out.append('strand 1 normalized pairs: '+', '.join(f'{v/spectra[512][1][0]:.6f}' for v in spectra[512][1]))
    out.append(f'harmonic fit R2={r2_h:.8f}, RMSE={err_h:.6g}')
    out.append(f'best atomic-shell template={best_shell}, R2={max(r2_b,r2_e):.8f}, RMSE={err_shell:.6g}, shell advantage={shell_adv:.6g}')
    out.append(f'observed scalar degeneracy per harmonic={observed_deg}; atomic shell capacities={expected_shell.tolist()}')
    for name,b in [('B1 certified linked reference',B1),('B2 mesh-converged frequencies',B2),('B3 ordinary harmonic law',B3),('B4 atomic shell template beats harmonic law',B4),('B5 atomic shell degeneracy reproduced',B5)]:
        out.append(name+': '+('PASS' if b else 'FAIL'))
    out.append('FINDING: '+finding)
    text='\n'.join(out); print(text)
    (ROOT/'analysis'/'ROPE_MODE001_run.log').write_text(text+'\n')
    return locals()

if __name__=='__main__': run()
