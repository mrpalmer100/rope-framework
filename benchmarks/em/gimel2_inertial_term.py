#!/usr/bin/env python3
"""COMMISSION GIMEL-2 -- EM-016 blocker (ii): is the inertial term forced?

Bars: analysis/GIMEL2_inertial_term_bars_LOCKED.md.
C1 symmetry ledger; C2 uniqueness at leading order; C3 the coefficient.
"""
import sympy as sp

t, x = sp.symbols("t x", real=True)
a = sp.Function("a")(t, x)
c0 = sp.Symbol("c_0")            # constant shift

print("=" * 70)
print("C1 -- THE SYMMETRY LEDGER (computed)")
print("=" * 70)
print("Registered fact: there are NO material points (FND-REL-002, Derived);")
print("the displacement/orientation variable is a GAUGE LABEL, defined only")
print("up to a constant shift a -> a + c_0. EM-RECON-012 uses exactly this")
print("to forbid a mass term. Test each candidate term under the shift:\n")

cands = {
    "m^2 a^2/2        (mass term)": a**2 / 2,
    "mu (da/dt)^2/2   (inertial)": sp.diff(a, t)**2 / 2,
    "K (da/dx)^2/2    (stiffness)": sp.diff(a, x)**2 / 2,
    "lam a (da/dt)    (mixed)": a * sp.diff(a, t),
}
for name, expr in cands.items():
    shifted = expr.subs(a, a + c0).doit()
    shifted = sp.simplify(sp.expand(shifted.replace(
        sp.Derivative(a + c0, t), sp.diff(a, t)).replace(
        sp.Derivative(a + c0, x), sp.diff(a, x))))
    delta = sp.simplify(shifted - expr)
    ok = (delta == 0)
    print(f"   {name:34} shift-invariant: {ok}"
          + ("" if ok else f"   (changes by {delta})"))

print("\n   => the mass term is FORBIDDEN by the shift symmetry (as")
print("      EM-RECON-012 registered), while terms built from DERIVATIVES")
print("      of a survive it. The apparent paradox dissolves: a itself is")
print("      a label, but its RATE OF CHANGE is observable. A term with two")
print("      time derivatives is permitted by exactly the symmetry that")
print("      forbids a term with none.")

print()
print("=" * 70)
print("C2 -- UNIQUENESS AT LEADING ORDER")
print("=" * 70)
print("Among shift-invariant, local, isotropic, quadratic terms, order by")
print("number of derivatives (the standard effective-Lagrangian counting):")
print("   2 derivatives: (da/dt)^2 and (grad a)^2   <- leading order")
print("   4 derivatives: (d^2a/dt^2)^2, (lap a)^2, ...  <- suppressed")
print("The stiffness (grad a)^2 is already REGISTERED as EM-007; the only")
print("other two-derivative scalar is the time one. Time-reversal (t -> -t)")
print("forbids a single-time-derivative scalar; parity/isotropy forbid a")
print("preferred-direction kernel.")
print("\n   Alternatives NAMED, per the bar, and their exclusions:")
print("   - higher time derivatives: suppressed by the derivative expansion")
print("     (they enter at the same order as the lattice corrections the")
print("     corpus already truncates);")
print("   - anisotropic kernel mu_ij: excluded by the registered isotropy")
print("     of the wave sector (FND-REL-002 forces Lorentz-invariant form);")
print("   - nonlocal kernel mu(k): excluded at leading order by locality,")
print("     which is what the derivative expansion assumes -- STATED as an")
print("     assumption, not smuggled.")
print("\n   => (mu/2)(da/dt)^2 is the UNIQUE leading-order term. FORM FORCED.")

print()
print("=" * 70)
print("C3 -- THE COEFFICIENT (form vs value, kept separate)")
print("=" * 70)
K, mu = sp.symbols("K mu", positive=True)
print("   The form fixes the DISPERSION but not the SCALE:")
print(f"      c = sqrt(K/mu) = {sp.sqrt(K/mu)}")
print("   The corpus already registers the transverse branch at")
print("   omega^2 = (T0/mu) q^2 (EM-RECON-025) with mu the rope mass")
print("   density, and c = sqrt(T0/mu) as the light speed. Matching the")
print("   field EOM to that registered branch FIXES mu as the same rope")
print("   mass density -- it is not a new constant.")
print("   HONEST LIMIT: this is a CONSISTENCY IDENTIFICATION with an")
print("   already-registered sector, not an independent derivation of the")
print("   numerical value. The value rides on the same calibration the")
print("   transverse sector rides on. Reported as partial.")

print()
print("VERDICT: FORM-FORCED. Blocker (ii) discharges as to FORM;")
print("the coefficient is fixed by consistency with EM-RECON-025 rather")
print("than derived independently, and that limit is registered.")
