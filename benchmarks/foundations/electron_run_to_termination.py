"""ELEC-013 (Modeled): THE RUN TO TERMINATION -- THE CERTIFIED DYNAMICS
TERMINATE AT A CONTACT-SATURATED, FIELD-BALANCED, SCALE-STATIONARY
STATE. Partial tightness, not the ideal link; the first-order
generalized residual plateaus at ~0.38 and is kept open.

THE ENGINE STORY: resuming ELEC-012's trajectory, the softmin tangent
exhausted after ONE step -- and the generalized-KKT test (ELEC-012's
named next-order, implemented here) showed why: residual 0.73 with a
first-order-feasible descent direction the single aggregated normal
could not see. The ACTIVE-SET NNLS engine (decompose grad over all
active pair-constraint gradients with nonnegative multipliers; step
along the residual; certify) took over and ran 103 certified
iterations to the pre-locked termination criterion (25-iteration
decrease < 1e-4).

THE TERMINAL STATE, characterized:
  E = 14.9072 (campaign total from ELEC-006: -1.246)
  d_min = 0.0610 (a hair off the 0.0600 core), |Lk| = 1.0004,
  FULL 128/256/512 certification green
  contact set: grew 408 -> 525 pairs and SATURATED (flat from it ~30)
  length: L = 4.5114, FLAT at termination -- and the ropelength ratio
  L/r = 150 vs the ideal Hopf link's 8 pi ~ 25: THE TIGHT-LINK
  EXTRAPOLATION IS CORRECTED. The object did not globally tighten; it
  cinched an EXTENDED CONTACT PATCH and stopped at an INTERIOR
  BALANCE where marginal length savings no longer beat field cost.
  scale bowl: E(0.95, 1.00, 1.05) = 14.932, 14.907, 14.988 -- the
  sampled minimum AT the terminal state: scale-stationary.
  generalized residual: fell 0.73 -> ~0.38 and PLATEAUED (bar 0.05
  not met, kept): first-order equilibrium approached within this
  discretization; the plateau's suspected cause is the first-order
  linearization of a curved contact manifold (steps that look
  feasible violate at second order, shrinking achievable decreases).

WHAT THE CAMPAIGN NOW HOLDS: a fully certified, linked, localized,
scale-stationary, contact-saturated, dynamically terminated object --
the cinched, field-held Hopf link -- with one open number (the
first-order residual plateau) and one named tool to attack it
(second-order steps on the contact manifold).
"""
import sys
from pathlib import Path
import numpy as np
from scipy.optimize import nnls

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.elec_grad import Grad, al
from rope_solver.topology.linking import hopf_curves
from rope_solver.geometry.curve import tension_energy


def seg_geo(A, B):
    P = A[:, None, :]; Q = np.roll(A, -1, axis=0)[:, None, :]
    R = B[None, :, :]; S = np.roll(B, -1, axis=0)[None, :, :]
    u = Q - P; v = S - R; w = P - R
    a = np.sum(u*u, axis=2); b = np.sum(u*v, axis=2); c = np.sum(v*v, axis=2)
    d = np.sum(u*w, axis=2); e = np.sum(v*w, axis=2); den = a*c - b*b
    sc = np.where(den > 1e-14, (b*e - c*d)/den, 0.0)
    tc = np.where(den > 1e-14, (a*e - b*d)/den, np.where(c > 1e-14, e/c, 0.0))
    sc = np.clip(sc, 0, 1); tc = np.clip(tc, 0, 1)
    tc = np.where(c > 1e-14, np.clip((b*sc + e)/c, 0, 1), 0.0)
    sc = np.where(a > 1e-14, np.clip((b*tc - d)/a, 0, 1), 0.0)
    D = w + sc[:, :, None]*u - tc[:, :, None]*v
    return np.sqrt(np.maximum(np.sum(D*D, axis=2), 1e-18)), D, sc, tc


def test():
    g = Grad()
    st = np.load(ROOT/'analysis'/'ELEC013_state.npz')
    z = st['z_final'].astype(float)
    assert bool(st['terminated']), "the run reached its pre-locked termination criterion"
    E, psi, cs = g.energy(z)
    assert E < 14.92, "terminal energy (campaign descent -1.24 from ELEC-006)"
    d, lk, okfull, _ = g.m.cert(z, full=True)
    assert okfull and al.D_HARD <= d <= al.D_HARD + 1.5e-3, "riding a hair off the core, certified"
    assert abs(abs(lk) - 1) < 0.01, "linking pristine"
    # contact saturation + the corrected tight-link picture
    c1, c2 = g.m.curves(z, 128)
    A, B = np.asarray(c1), np.asarray(c2)
    Dm, Dv, sc, tc = seg_geo(A, B)
    ncon = int(np.sum(Dm <= 1.15*al.D_HARD))
    assert ncon >= 450, "extended contact patch (saturated set)"
    L = sum(float(np.sum(np.linalg.norm(np.roll(c, -1, axis=0) - c, axis=1))) for c in (A, B))
    assert L/(al.D_HARD/2) > 100, "FAR from the ideal Hopf ropelength (8 pi ~ 25): partial tightness"
    # scale-stationarity at the terminal shape
    Es = []
    for lam in (0.95, 1.0, 1.05):
        zz = z.copy(); zz[0] += np.log(lam); zz[1:] *= lam
        e_, _, _ = g.energy(zz); Es.append(e_)
    assert Es[1] < Es[0] and Es[1] < Es[2], "scale bowl minimum AT the terminal state"
    # the open number: first-order generalized residual plateau
    grad = g.gradient(z, psi, cs)
    M128 = 128; t128 = np.linspace(0, 2*np.pi, M128, endpoint=False)
    K = al.K
    basis = np.array([f(k*t128) for k in range(1, K+1) for f in (np.sin, np.cos)])
    R = float(np.exp(z[0])); h1, h2 = hopf_curves(M128, R=R)
    J = np.zeros((2*M128, 3, len(z)))
    J[:M128, :, 0] = h1; J[M128:, :, 0] = h2
    for j in range(2):
        for a_ in range(3):
            for k2 in range(2*K):
                J[j*M128:(j+1)*M128, a_, 1 + j*3*2*K + a_*2*K + k2] = basis[k2]
    J -= J.mean(axis=0, keepdims=True)
    ii, jj = np.where(Dm <= 1.10*al.D_HARD)
    rows = []
    for i, j in zip(ii, jj):
        nhat = Dv[i, j]/Dm[i, j]
        Gp = np.zeros((2*M128, 3))
        Gp[i] += (1 - sc[i, j])*nhat; Gp[(i+1) % M128] += sc[i, j]*nhat
        Gp[M128 + j] += -(1 - tc[i, j])*nhat; Gp[M128 + (j+1) % M128] += -tc[i, j]*nhat
        rows.append(np.einsum('na,nap->p', Gp, J))
    Am = np.array(rows)
    mu, _ = nnls(Am.T, grad, maxiter=20*max(Am.shape))
    ratio = float(np.linalg.norm(grad - Am.T@mu)/np.linalg.norm(grad))
    assert 0.2 < ratio < 0.6, "the first-order residual plateau (~0.38): OPEN, kept"
    print(f"terminal: E={E:.4f}, d={d:.4f}, |Lk|={abs(lk):.4f}, contacts={ncon}, "
          f"L/r={L/(al.D_HARD/2):.0f} (ideal 25), gres={ratio:.3f}")
    print(f"scale bowl: {Es[0]:.4f} > {Es[1]:.4f} < {Es[2]:.4f}")
    print("PASS: the certified dynamics TERMINATE at the cinched, field-held Hopf link --")
    print("      contact-saturated, scale-stationary, topologically pristine, residual open.")


if __name__ == "__main__":
    test()
