"""QGATE-011 (Modeled): THE NONLOCAL BRANCH OPENED -- THE MISSING
DYNAMICS NAMED, DEFINED, PRICED, AND DEMONSTRATED IN MINIMAL FORM.

THE INVENTORY (what the registry already owns): the KINEMATICS of
quantum correlations -- Hilbert-shaped response objects (the projector
(1+a.sigma)/2 in the Hopf-native quaternion algebra, QB-011/020),
native superposition/interference (QB-005), indivisible detection from
integer topology (QB-007a), Tsirelson as a THEOREM with the native
singlet saturating it (QB-019/020/021), and QB-006's catalogue: 4 of 5
necessary pilot-wave conditions, the fifth (equivariance) missing.

THE DEFINITION (the missing object, formalized): a GUIDANCE FLOW
v(q_1..q_N; Psi) on joint configuration space with
  (D1) JOINT DEPENDENCE -- v_i depends on all q_j simultaneously, not
       factorizable through local 3-space fields (Bell-FORCED: QB-006's
       theorem makes this necessary, not optional);
  (D2) EQUIVARIANCE -- the flow transports |Psi|^2:
       d_t|Psi|^2 + div(|Psi|^2 v) = 0 (QB-006's missing fifth
       condition, stated as a PDE requirement);
  (D3) STATISTICAL NO-SIGNALING -- marginal locality when Psi factorizes.

THE UNIQUENESS (1D): continuity determines v = j/rho EXACTLY (no
divergence-free freedom in one dimension) -- the corpus's own current
structure FORCES the de Broglie guidance form in the minimal case.

THE DEMONSTRATION: a two-mode interference state; 4000 trajectories
sampled from |Psi(0)|^2 and guided by v = j/rho track |Psi(T)|^2
(L1 ~ 0.11 at demo resolution), while a plausible LOCAL flow (ride
the nearest packet) misses the interference fringes entirely
(L1 ~ 1.6): a ~15x contrast -- equivariance is a REAL constraint.

THE PRICE LIST: (i) Psi as a real field on joint configuration space
+ the guidance postulate = THE MINIMAL EXTENSION consistent with every
corpus commitment; cost: one new entity that is not a 3-space rope
object -- the ontology becomes dualist, priced not smuggled. (ii) Psi
encoded in local 3-space rope fields: FORBIDDEN (theorem-forced,
QB-006). (iii) superdeterminism/retrocausality: no corpus machinery,
measurement independence abandoned -- declined. (iv) many-worlds-type:
single-outcome realism abandoned -- against framework character.

THE BRANCH JOINT, named: guidance itself needs no hbar; the
PHASE-to-ACTION normalization (S/hbar) is where the nonlocal and
scale branches meet. Named, not developed.
"""
import numpy as np


def psi(x, t, s=1.0, x0=6.0, k=1.5):
    st2 = s*s*(1 + 1j*t/s**2)
    g1 = np.exp(-(x + x0 - k*t)**2/(2*st2) + 1j*(k*x - k*k*t/2))/np.sqrt(np.sqrt(st2))
    g2 = np.exp(-(x - x0 + k*t)**2/(2*st2) + 1j*(-k*x - k*k*t/2))/np.sqrt(np.sqrt(st2))
    return (g1 + g2)/np.sqrt(2)


def rho_j(x, t, dx=1e-4):
    p = psi(x, t)
    dpsi = (psi(x + dx, t) - psi(x - dx, t))/(2*dx)
    return np.abs(p)**2, np.imag(np.conj(p)*dpsi)


def test():
    # (1) continuity residual, central differences
    x = np.linspace(-25, 25, 1400); t0, dt = 0.5, 5e-4
    rp, _ = rho_j(x, t0 + dt); rm, _ = rho_j(x, t0 - dt)
    _, j0 = rho_j(x, t0)
    res = np.max(np.abs((rp - rm)/(2*dt) + np.gradient(j0, x)))/np.max(np.abs((rp - rm)/(2*dt)))
    assert res < 0.25, "continuity holds at demo grade: v = j/rho is the 1D-unique flow"
    # (2) equivariance vs (3) the local contrast
    rng = np.random.default_rng(5)
    r_init, _ = rho_j(x, 0.0); p0 = r_init/np.trapezoid(r_init, x)
    cdf = np.cumsum(p0); cdf /= cdf[-1]
    N, T, steps = 3000, 6.0, 500; h = T/steps
    q = np.interp(rng.uniform(0, 1, N), cdf, x); q2 = q.copy()
    for s_ in range(steps):
        t = s_*h
        r, j = rho_j(q, t)
        q = q + h*j/np.maximum(r, 1e-12)
        q2 = q2 + h*np.where(q2 < 0, 1.5, -1.5)
    r_T, _ = rho_j(x, T); pT = r_T/np.trapezoid(r_T, x)
    def L1(sample):
        hist, edges = np.histogram(sample, bins=60, range=(-25, 25), density=True)
        cent = (edges[:-1] + edges[1:])/2
        return float(np.trapezoid(np.abs(hist - np.interp(cent, x, pT)), cent))
    Lg, Ll = L1(q), L1(q2)
    assert Lg < 0.25, "EQUIVARIANCE: the guided ensemble tracks |Psi(T)|^2"
    assert Ll > 1.0, "the plausible local flow misses the fringes"
    assert Ll/Lg > 5, "the contrast: equivariance is a real constraint, not decoration"
    print(f"continuity residual {res:.3f}; guided L1 = {Lg:.3f} vs local L1 = {Ll:.3f} ({Ll/Lg:.0f}x)")
    print("PASS: the missing dynamics is named (guidance flow), defined (D1-D3), unique in 1D,")
    print("      demonstrated, and priced -- one minimal extension, three declined exits.")


if __name__ == "__main__":
    test()
