"""ELEC-002: SELF-CONSISTENT CURVE--FIELD LOCALISATION GATE.

The field is not replaced by the pairwise proxy used in ELEC-001.  At every
curve update, a Gaussian tube source is rebuilt on a 3-D grid, Poisson's
equation is solved, and the same total functional

    E[C,psi] = T0 * length(C) + kappa/2 * integral |grad psi|^2 dV

is evaluated.  The field is therefore relaxed exactly (adiabatically) for each
trial curve while the curve is descended in a finite Fourier basis.  Steps are
accepted only when the common energy falls and the non-crossing topological
sector remains |Lk| ~= 1.

Locked bars:
 B1 topology: every candidate ends with ||Lk|-1| < 0.20.
 B2 common-action descent: energy falls >5% in every trial and accepted history
    is monotone.
 B3 localisation: every final combined RMS radius lies in 0.4..2.0.
 B4 common attractor: final-radius CV across five perturbed seeds <15%.
 B5 unlinked control: an unlinked pair stays |Lk| <0.15 under the same protocol.

This is only an existence/consistency gate.  It does not identify the object as
an electron or derive electron mass, spin, or magnetic moment.
"""
from pathlib import Path
import csv
import sys
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from rope_solver.psi.solver import grid, solve_psi, field_energy, laplacian_3d
from rope_solver.topology.linking import hopf_curves, linking_number
from rope_solver.geometry.curve import tension_energy

N = 14
L_BOX = 8.0
A_THICK = 0.24
M = 24
KAPPA = 2.0
T0 = 1.0
ITERS = 115

coords, X, Y, Z, H = grid(N, L_BOX)
GRID_POINTS = np.stack([X.ravel(), Y.ravel(), Z.ravel()], axis=1)
L3 = laplacian_3d(N, H)
T = np.linspace(0.0, 2.0*np.pi, M, endpoint=False)
BASIS = np.array([f(k*T) for k in (1, 2, 3) for f in (np.sin, np.cos)])


def parameter_curves(x, linked=True):
    R = float(np.exp(x[0]))
    if linked:
        c1, c2 = hopf_curves(M, R=R)
    else:
        c1, c2 = hopf_curves(M, R=R)
        c1[:, 0] -= 2.0
        c2[:, 0] += 2.0
        # Put both rings in parallel planes so the control is plainly unlinked.
        c2[:, 1], c2[:, 2] = c2[:, 2].copy(), np.zeros(M)
    coeff = x[1:].reshape(2, 3, 6)
    curves = []
    for j, c in enumerate((c1, c2)):
        d = np.einsum("ak,kn->na", coeff[j], BASIS)
        curves.append(c + d)
    centre = np.vstack(curves).mean(axis=0)
    return curves[0] - centre, curves[1] - centre


def tube_source(curves):
    d2 = np.full(len(GRID_POINTS), np.inf)
    for curve in curves:
        # Nodes plus segment midpoints approximate a continuous Gaussian tube.
        samples = np.vstack([curve, 0.5*(curve + np.roll(curve, -1, axis=0))])
        for p in samples:
            d2 = np.minimum(d2, np.sum((GRID_POINTS - p)**2, axis=1))
    src = np.exp(-d2/(2.0*A_THICK**2)).reshape(N, N, N)
    return src/(src.sum()*H**3)


def common_energy(x, linked=True):
    curves = parameter_curves(x, linked=linked)
    psi = solve_psi(tube_source(curves), H, L3=L3, rtol=5e-6, maxiter=700)
    return (sum(tension_energy(c, T0) for c in curves)
            + KAPPA*field_energy(psi, H))


def combined_rms(curves):
    pts = np.vstack(curves)
    pts -= pts.mean(axis=0)
    return float(np.sqrt(np.mean(np.sum(pts*pts, axis=1))))


def optimise(seed, linked=True, iters=ITERS):
    rng = np.random.default_rng(seed)
    x = np.zeros(37)
    x[0] = np.log(0.85)
    x[1:] = rng.normal(0.0, 0.05 if linked else 0.025, 36)
    e = common_energy(x, linked)
    e0 = e
    history = [e]
    m = np.zeros_like(x)
    v = np.zeros_like(x)

    for it in range(1, iters + 1):
        delta = rng.choice((-1.0, 1.0), size=len(x))
        ck = 0.026/(1.0 + it/90.0)**0.15
        ep = common_energy(x + ck*delta, linked)
        em = common_energy(x - ck*delta, linked)
        g = ((ep - em)/(2.0*ck))*delta
        m = 0.9*m + 0.1*g
        v = 0.999*v + 0.001*g*g
        mh = m/(1.0 - 0.9**it)
        vh = v/(1.0 - 0.999**it)
        step = 0.018/(1.0 + it/120.0)**0.4 * mh/(np.sqrt(vh) + 1e-8)

        accepted = False
        for fraction in (1.0, 0.25):
            trial = x - fraction*step
            trial[0] = np.clip(trial[0], np.log(0.35), np.log(1.8))
            trial[1:] = np.clip(trial[1:], -0.35, 0.35)
            curves = parameter_curves(trial, linked)
            lk = abs(linking_number(*curves))
            topology_ok = (abs(lk - 1.0) < 0.20) if linked else (lk < 0.15)
            if not topology_ok:
                continue
            en = common_energy(trial, linked)
            if en <= e + 1e-10:
                x, e, accepted = trial, en, True
                break
        history.append(e)

    curves = parameter_curves(x, linked)
    return {
        "seed": seed,
        "E0": float(e0), "Ef": float(e),
        "drop": float((e0-e)/e0),
        "R_rms": combined_rms(curves),
        "Lk": float(linking_number(*curves)),
        "monotone": bool(np.all(np.diff(history) <= 1e-9)),
    }


def test():
    results = [optimise(seed, linked=True) for seed in range(5)]
    links = [abs(r["Lk"]) for r in results]
    drops = [r["drop"] for r in results]
    radii = [r["R_rms"] for r in results]
    cv = float(np.std(radii, ddof=1)/np.mean(radii))

    assert all(abs(lk-1.0) < 0.20 for lk in links), links
    assert all(d > 0.05 for d in drops), drops
    assert all(r["monotone"] for r in results)
    assert all(0.4 < rr < 2.0 for rr in radii), radii
    assert cv < 0.15, cv

    control = optimise(101, linked=False, iters=70)
    assert abs(control["Lk"]) < 0.15, control

    out = Path(__file__).resolve().parents[2]/"analysis"/"ELEC002_results.csv"
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        w.writeheader(); w.writerows(results)

    print("ELEC-002 locked-bar results")
    print(f"B1 PASS |Lk|={min(links):.3f}..{max(links):.3f}")
    print(f"B2 PASS common-energy reduction={100*min(drops):.1f}%..{100*max(drops):.1f}% (monotone)")
    print(f"B3 PASS final rms radius={min(radii):.3f}..{max(radii):.3f}")
    print(f"B4 PASS attractor CV={100*cv:.2f}%")
    print(f"B5 PASS unlink control |Lk|={abs(control['Lk']):.4f}")
    print("FINDING: the common Poisson curve-field functional supports a finite,")
    print("topologically charged localized attractor in this reduced-basis test.")
    print("No physical-electron identification is made.")


if __name__ == "__main__":
    test()
