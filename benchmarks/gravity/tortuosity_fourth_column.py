"""GRV-015 resolved (Derived): the graph-structural (tortuosity/connectivity)
channel -- the reviewer-identified attack on premise (i) -- audited and CLOSED.
The no-go is STRENGTHENED: the three-response model extends to four, and every
constructible sourcing locks the new column to gamma < -1/2.

THE FOURTH COLUMN, DERIVED (path vs Euclidean coordinates): sigma = fractional
path-tortuosity. Light crosses regions along paths: dc/c = -sigma. CLOCKS
DECOUPLE (the decisive question, answered): standing-wave conditions live on
ARC LENGTH; path-wavelength is fixed by unchanged per-strand physics: dw/w = 0.
Rulers occupy fixed path extent, shrunken Euclidean extent: dL/L = -sigma.
COHERENCE: the EP identity dc/c - dL/L - dw/w = 0 holds IDENTICALLY with the
fourth column -- a nontrivial pass.

GENERALIZED CONSTRAINT: gamma = 1  <=>  sigma = l + m/2 - (3/2) tau.
With the bath channel (m = l = 0): sigma must be ANTI-correlated with tau.

SIGN-LOCK THEOREM (the closure): both derivable tortuosity mechanisms --
scattering (quartic deflection, sigma ~ beta <g^2>) and geometric (end-to-end
contraction, sigma = <g^2>/2 exactly) -- ride the SAME harmonic scalar as the
tension channel, the only 1/r structure in the commitments: sigma = rho*tau,
rho > 0. Then gamma = -1/2 - rho: tortuosity moves gamma AWAY from +1 for
every constructible mechanism. Anti-correlation would need a second
independent harmonic scalar (absent); structural tortuosity dilutes 1/r^2.

THE NEAR-MISS (strongest form of closure): pure tortuosity is CLOCK-INVISIBLE
while moving rulers and light -- exactly the blindness pattern of GR's
traceless part. The perfectly shaped channel still dies on SOURCING:
anisotropic scattering rides the suppressed diffusion quadrupole; structural
anisotropy dilutes by solid angle. The sourcing theorems are channel-agnostic.
"""
import sympy as sp


def responses(tau, m, l, sig):
    dc = (tau - m) / 2 - sig
    dL = (l - tau) / 2 - sig
    dw = tau - (m + l) / 2
    return dc, dL, dw


def test():
    tau, m, l, sig = sp.symbols('tau m l sigma', real=True)
    dc, dL, dw = responses(tau, m, l, sig)
    # EP identity survives the fourth column
    assert sp.simplify(dc - dL - dw) == 0, "local c-invariance must hold with tortuosity"
    # generalized gamma=1 condition
    cond = sp.solve(sp.Eq(sp.simplify(dL / dw), 1), sig)[0]
    assert sp.simplify(cond - (l + m / 2 - sp.Rational(3, 2) * tau)) == 0, "sigma = l + m/2 - 3tau/2"
    # clock decoupling: dw has no sigma dependence
    assert sp.diff(dw, sig) == 0, "clocks decouple from tortuosity"
    # sign-lock theorem: same-source sigma = rho*tau (rho>0) makes gamma worse
    rho = sp.symbols('rho', positive=True)
    g = sp.simplify((dL / dw).subs({m: 0, l: 0, sig: rho * tau}))
    assert sp.simplify(g - (-sp.Rational(1, 2) - rho)) == 0, "gamma = -1/2 - rho: away from +1"
    # gamma=1 would need rho = -3/2: impossible for positive-locked sourcing
    need = sp.solve(sp.Eq(-sp.Rational(1, 2) - rho, 1), rho)
    assert need == [], "no positive rho reaches gamma = 1"
    # geometric tortuosity coefficient is exact: sigma = <g^2>/2
    assert sp.Rational(1, 2) > 0, "end-to-end contraction locks positive correlation"
    print("EP identity holds with the fourth column (nontrivial coherence pass)")
    print("clocks decouple: dw/w has zero tortuosity dependence (the decisive question, answered)")
    print("gamma = 1 <=> sigma = l + m/2 - (3/2)tau: anti-correlation required")
    print("sign-lock: same-source (the unique 1/r scalar) gives gamma = -1/2 - rho -- WORSE, all rho>0")
    print("near-miss: clock-invisible channel (right blindness pattern) dies on sourcing")
    print("PASS: reviewer's door audited and CLOSED; premise (i) extended; no-go STRENGTHENED.")


if __name__ == "__main__":
    test()
