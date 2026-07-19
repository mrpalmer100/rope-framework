"""GRV-008/009/010: the gravity tensor-structure campaign, session 1.

THREE THEOREMS (sympy-verified), in the three-response model where light,
rulers, and clocks all derive from the network's {T, mu, lambda}:
  dc/c = (tau - m)/2;  dL/L = (l - tau)/2  [rulers ~ xi = sqrt(lambda/T),
  FND-MATTER-001];  dw/w = tau - (m + l)/2  [clocks ~ c/xi]
  where tau = dT/T, m = dmu/mu, l = dlambda/lambda.

  T1 (LOCAL c-INVARIANCE): dc/c - dL/L - dw/w = 0 IDENTICALLY for arbitrary
     conditioning -- an equivalence-principle-like theorem: co-materiality of
     clocks, rulers, and light makes the conditioning locally undetectable.
  T2 (PPN CONSISTENCY): gamma(bending) = gamma(rulers) identically -- the medium
     picture defines ONE effective gamma; it cannot produce inconsistent
     weak-field observables.
  T3 (THE FACTOR-2 REDUCED): gamma_eff = 1  <=>  m = 3*tau - 2*l.
     The 'why 2?' question is now one linear constraint on response coefficients.

CANDIDATE 1 FAILED (GRV-009): per-strand STRAIN conditioning is fully specified
by session results (tau = (k/T0)eps from EM-RECON-009; m = -eps from P-VOL;
l = -2*eps from torsional rigidity ~ r^4 under volume-conserving thinning):
  gamma_eff = -(k/T0 + 2)/(2 k/T0 + 3)  ->  -4/7 at k/T0 = 2; gamma = 1 needs
  k/T0 = -5/3 (impossible). Wrong SIGN of spatial curvature; Cassini-excluded.
  Consistent with GRV-005 (mass couples absurdly weakly to strain): strain is
  the wrong channel by two independent arguments. Pure COVERAGE conditioning is
  metric-invisible (per-strand properties unchanged): tau = m = l = 0.

CANDIDATE 2 SHARPLY POSED (GRV-010, Open): MODE-BATH conditioning (background
wave energy <g^2> on strands): tau = (k/2T0)<g^2> (from <eps> = <g^2>/2) and
m = +<g^2> (wave energy adds inertia) are COMPUTED; the constraint then
PREDICTS the required l = (3k/(4T0) - 1/2)<g^2>. Non-degeneracy: dw/w =
(<g^2>/8)(k/T0 - 2) -- the candidate is DEGENERATE (no redshift) at exactly
k/T0 = 2, and gives the correct redshift SIGN (clocks slow) only for
k/T0 < 2, which requires K_c > k in EM-RECON-013's core condition. Falsifiable
structure, no knobs; the l-mechanism is the open derivation.
"""
import sympy as sp


def theorems():
    tau, m, l = sp.symbols('tau m l', real=True)
    dc, dL, dw = (tau - m)/2, (l - tau)/2, tau - (m + l)/2
    t1 = sp.simplify(dc - dL - dw) == 0
    t2 = sp.simplify((dc/dw - 1) - (dL/dw)) == 0
    m_req = sp.solve(sp.Eq(sp.simplify(dL/dw), 1), m)[0]
    t3 = sp.simplify(m_req - (3*tau - 2*l)) == 0
    return t1, t2, t3


def candidate1_fails():
    eps = sp.symbols('epsilon', positive=True)
    kT = sp.symbols('kT', real=True)   # real, so the (unphysical) negative root is exposed
    tau, m, l = kT*eps, -eps, -2*eps
    gamma = sp.simplify(((l - tau)/2) / (tau - (m + l)/2))
    at2 = sp.nsimplify(gamma.subs(kT, 2))
    req = sp.solve(sp.Eq(gamma, 1), kT)[0]
    return at2 == sp.Rational(-4, 7) and req == sp.Rational(-5, 3)


def candidate2_structure():
    g2, kT = sp.symbols('g2 kT', positive=True)
    tau, m = (kT/2)*g2, g2
    l_req = sp.simplify((3*tau - m)/2)
    dw = sp.simplify(tau - (m + l_req)/2)
    degenerate_at_2 = sp.simplify(dw.subs(kT, 2)) == 0
    correct_sign_below_2 = sp.simplify(dw.subs(kT, sp.Rational(3, 2))) < 0
    return degenerate_at_2 and bool(correct_sign_below_2)


def test():
    t1, t2, t3 = theorems()
    assert t1, "T1: local c-invariance identity"
    assert t2, "T2: single consistent gamma"
    assert t3, "T3: gamma=1 <=> m = 3tau - 2l"
    assert candidate1_fails(), "strain conditioning: gamma=-4/7 at k/T0=2; gamma=1 needs k/T0=-5/3"
    assert candidate2_structure(), "mode-bath: degenerate at k/T0=2; correct redshift sign below 2"
    print("T1 local c-invariance: PASS (identity)   T2 single gamma: PASS (identity)")
    print("T3 factor-2 reduced: gamma=1 <=> dmu/mu = 3 dT/T - 2 dlam/lam: PASS")
    print("candidate 1 (strain): gamma=-4/7, needs k/T0=-5/3 -> FAILED, Cassini-excluded")
    print("candidate 2 (mode-bath): tau,m computed; l predicted; degenerate at k/T0=2;")
    print("      correct redshift sign requires k/T0<2 (hence K_c>k): sharply posed, OPEN")
    print("PASS: the factor-2 is now one linear constraint; first candidate dead; second live.")


if __name__ == "__main__":
    test()
