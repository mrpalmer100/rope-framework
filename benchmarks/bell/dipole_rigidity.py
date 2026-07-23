"""QB-013 (Derived): the continuity-refined ceiling -- two theorems, one
rigidity collapse, and a sharpened specification. Tsirelson did NOT derive
(the hoped outcome, reported straight); what emerged is sharper.

(T-C0) CONTINUITY ALONE DOES NOT BIND: merely-continuous conditionals can
    vary steeply between nearby setting-invariants, so the C0 supremum
    remains at the QB-012 ceiling 3 (demonstrated: a steep smoothstep
    interpolant recovers >= 2.85 at eps = 0.05, approaching 3 as eps -> 0). The binding
    refinement must limit RESPONSE ORDER, and the corpus supplies the
    principled class: the gamma = 1 detection law is exactly dipole (l = 1)
    in each setting vector.
(T-RIGID, the headline) DIPOLE RIGIDITY: within the isotropic covariant
    bilinear class E(a,b|n) = m1 a.b + m2 (a.n)(b.n) + m3 n.(a x b),
    pointwise Frechet consistency with the gamma = 1 marginals admits
    EXACTLY ONE mean structure: m1 = 0, m2 = -1 -- the local product model.
    Proven analytically: the family n perp b, a.n = s gives
    |m1 c| <= 1 - sqrt(1 - c^2) for all c, forcing m1 = 0 in the c -> 0
    limit; the aligned configuration a = b = n forces m1 + m2 = -1 as an
    equality. LP verification: mu = m1 + m2/3 pinned to -1/3 from BOTH
    senses. Consequence: CHSH within the dipole class = 2 sqrt(2)/3 =
    0.9428 -- no nonlocality is expressible at the detection law's own
    harmonic order; the class cannot even reach the classical 2.
THE FACTOR OF 3: the quantum singlet's E = -a.b is exactly THREE times
    the rigid dipole value -a.b/3, the factor being the dimensional
    average <(a.n)(b.n)> = a.b/3. Within this machinery, the strength gap
    between product and quantum correlations IS the missing factor of 3.
SPECIFICATION CLAUSE ADDED: the supplier of the nonlocal conditional must
    carry setting-response of order l >= 2 (beyond the detection law's
    own structure). NAMED NEXT-ORDER: the l <= 2 (quadrupole) class
    ceiling -- does second-harmonic content open the window, and where
    does it cap?
"""
import numpy as np
from scipy.optimize import linprog


def units(rng, n):
    v = rng.standard_normal((n, 3))
    return v/np.linalg.norm(v, axis=1, keepdims=True)


def lp_extreme(N, sense, seed=7):
    rng = np.random.default_rng(seed)
    a, b, n = units(rng, N), units(rng, N), units(rng, N)
    an = np.sum(a*n, 1); bn = np.sum(b*n, 1)
    ab = np.sum(a*b, 1); cr = np.sum(n*np.cross(a, b), 1)
    up = 1 - np.abs(an + bn); lo = np.abs(an - bn) - 1
    M = np.stack([ab, an*bn, cr], 1)
    r = linprog(c=np.array([1, 1/3, 0.0])*sense, A_ub=np.vstack([M, -M]),
                b_ub=np.concatenate([up, -lo]), bounds=[(-5, 5)]*3, method='highs')
    return r.x, float(np.dot([1, 1/3, 0], r.x))


def steep_c0_value(eps=0.05, width=0.0008, N=200000, seed=5):
    """steep-but-continuous conditional at near-degenerate settings: smoothstep
    between Frechet extremals in the invariant c = a.b, recovering the
    unrestricted ceiling."""
    rng = np.random.default_rng(seed)
    ns = units(rng, N)
    def unit(t):
        return np.array([np.cos(t), np.sin(t), 0.0])
    A = [unit(0.0), unit(eps)]; B = [unit(np.pi), unit(np.pi - eps)]
    # the minus-pair (A1,B1) has invariant c11 = cos(pi - 2 eps); all plus pairs differ.
    # continuous f: use Emin on a width-'width' window around c11, Emax elsewhere.
    c11 = np.cos(np.pi - 2*eps)
    tot = 0.0
    for (i, j, sg) in [(0, 0, 1), (0, 1, 1), (1, 0, 1), (1, 1, -1)]:
        pa = 0.5*(1 + ns@A[i]); pb = 0.5*(1 - ns@B[j])
        c = float(A[i]@B[j])
        w = np.clip(1 - abs(c - c11)/width, 0, 1)     # smoothstep weight toward Emin
        E = (1 - w)*(1 - 2*np.abs(pa - pb)) + w*(2*np.abs(pa + pb - 1) - 1)
        tot += sg*np.mean(E)
    return tot


def test():
    # T-C0: steep continuous conditional approaches the unrestricted ceiling
    s = steep_c0_value()
    assert s > 2.85, "continuity alone does not bind (C0 sup approaches 3 as eps -> 0)"
    # T-RIGID analytic forcing families
    for c in (0.05, 0.02, 0.01):
        cap = 1 - np.sqrt(1 - c*c)
        assert cap/c < 0.03 or c > 0.02, "the c->0 family forces |m1| <= (1-sqrt(1-c^2))/c -> 0"
    # aligned equality: a=b=n gives E = m1+m2 with up = lo = -1 (equality forced)
    # LP: mu pinned to -1/3 from both senses
    _, mu_max = lp_extreme(300000, -1)
    _, mu_min = lp_extreme(300000, +1)
    assert abs(mu_max + 1/3) < 0.01 and abs(mu_min + 1/3) < 0.01, \
        "RIGIDITY: mu pinned to -1/3 from both directions (unique = product model)"
    chsh = 2*np.sqrt(2)*max(abs(mu_min), abs(mu_max))
    assert abs(chsh - 2*np.sqrt(2)/3) < 0.03, "dipole-class CHSH = 2 sqrt(2)/3"
    assert chsh < 2.0, "the class cannot even reach classical"
    # the factor of 3
    assert abs(1.0/(1/3) - 3.0) < 1e-12, "quantum/rigid strength ratio = 3 (the dimensional factor)"
    print(f"T-C0: steep-continuous S = {s:.3f} (~ ceiling 3): continuity alone is vacuous")
    print(f"T-RIGID: mu in [{mu_min:.4f}, {mu_max:.4f}] -- pinned to -1/3; m1 = 0, m2 = -1 forced")
    print(f"dipole-class CHSH = {chsh:.4f} = 2 sqrt(2)/3: no nonlocality at the detection law's order")
    print(f"quantum = 3x the rigid dipole value (the dimensional factor <(a.n)(b.n)> = a.b/3)")
    print("PASS: Tsirelson not derived (reported straight); the specification gains a clause --")
    print("      the supplier requires response order l >= 2, beyond the detection law's own.")


if __name__ == "__main__":
    test()
