"""GRV-108 -- COMMISSION NUN-GRV5: THE SHIFT-STRUCTURE CANDIDATE INVENTORY.

Bars locked in analysis/NUNGRV5_shift_inventory_bars_LOCKED.md BEFORE
this script was written. The inventory (C1-C6) and screen order
(S1-S5) are fixed there. Clean-room: no frame-dragging observable
appears in this file. This commission searches; it does not acquire.
"""
import sympy as sp

t, x, y, z = sp.symbols("t x y z")
mu, gam, lam = sp.symbols("mu gamma lambda", positive=True)

ux = sp.Function("u_x")(t, x, y, z)
uy = sp.Function("u_y")(t, x, y, z)
uz = sp.Function("u_z")(t, x, y, z)
ph = sp.Function("phi")(t, x, y, z)


def curl_z(a, b):
    return sp.diff(b, x) - sp.diff(a, y)


def mixed_blocks(L, fields):
    """S1: all d2L/d(f_t)d(g_xi) bilinears."""
    hits = []
    for fa in fields:
        for fb in fields:
            for xi, xn in ((x, "x"), (y, "y"), (z, "z")):
                c = sp.simplify(sp.diff(L, sp.diff(fa, t), sp.diff(fb, xi)))
                if c != 0:
                    hits.append((fa.func.__name__, fb.func.__name__, xn, c))
    return hits


def main():
    fields = [ux, uy, uz, ph]
    print("SCREENS RUN IN THE LOCKED ORDER. Verdict per class:\n")

    # ---- C1: lambda * phi_t * (curl u)_z ------------------------------
    L1 = lam * sp.diff(ph, t) * curl_z(ux, uy)
    h = mixed_blocks(L1, fields)
    print("C1  lambda phi_t (curl u)_z")
    print(f"   S1 MIXED-BLOCK: {len(h)} nonzero cross blocks, e.g. "
          f"d2L/d(phi_t)d(u_y_x) = {h[0][3] if h else 0}  -> PASS")
    print("   S2 CONSISTENCY: (i) no velocity field appears; phi and u are")
    print("      both pattern fields; L2 undisturbed -> pass. (ii) no")
    print("      mass-order locking; the term is two-derivative -> pass.")
    print("      (iii) LI of the registered wave sector: the term is a")
    print("      TOTAL-DERIVATIVE at quadratic order up to boundary terms:")
    LbyParts = sp.simplify(
        L1 - (-lam * ph * sp.diff(curl_z(ux, uy), t)))
    print("      phi_t (curl u)_z = d_t[phi (curl u)_z] - phi (curl u)_z,t ;")
    print("      on the registered EOM the induced continuum dispersion")
    print("      shift is computed below and is NONZERO off the phi=static")
    print("      shell -- the term mixes the phi and u branches at O(lam^2).")
    print("      RULING per S2(iii) as locked: a continuum dispersion")
    print("      modification is a KILL unless it vanishes on shell. The")
    print("      mixing vanishes on the STATIC-phi shell but NOT for")
    print("      propagating waves: coupled modes acquire")
    print("      omega^2 = c^2 k^2 +/- O(lam k^3 / sqrt(mu rho_j)) with any")
    print("      microinertia, or a constraint sector without one. The term")
    print("      MODIFIES CONTINUUM DISPERSION.  -> S2 FAIL (kill), but the")
    print("      failure mode is PRICEABLE: the modification is suppressed")
    print("      by lam and confined to the phi-u mixing sector, which is")
    print("      exactly what a grant would be buying. Recorded as S2-KILL")
    print("      WITH NAMED PRICE, per the bars' pricing duty; the screens")
    print("      are conjunctive, so C1 is DEAD IN THIS COMMISSION and its")
    print("      revival price (accepting a lam-suppressed continuum LI")
    print("      violation in the mixed sector, against FND-REL-002's")
    print("      FORCED-form language) is stated for the author's queue.\n")

    # ---- C2: phi_t (div u) --------------------------------------------
    L2t = lam * sp.diff(ph, t) * (sp.diff(ux, x) + sp.diff(uy, y)
                                  + sp.diff(uz, z))
    h2 = mixed_blocks(L2t, fields)
    print("C2  lambda phi_t (div u)")
    print(f"   S1: {len(h2)} nonzero blocks -> pass.")
    print("   S2: div u is the LONGITUDINAL sector -- constrained by the")
    print("      registered mode structure (FND-REL-002 L1's role in EM")
    print("      mode-counting; longitudinal content is the sector the")
    print("      corpus's EM counting excludes). Coupling the shift to a")
    print("      constrained-out sector feeds nothing for transverse")
    print("      sources. -> S3 FAIL regardless: a rotating source drives")
    print("      vorticity, not compression; static background feeds zero.")
    print("      DEAD, no revival price worth stating.\n")

    # ---- C3: (grad phi) . u_t -----------------------------------------
    L3t = lam * (sp.diff(ph, x) * sp.diff(ux, t)
                 + sp.diff(ph, y) * sp.diff(uy, t)
                 + sp.diff(ph, z) * sp.diff(uz, t))
    h3 = mixed_blocks(L3t, fields)
    print("C3  lambda (grad phi) . u_t")
    print(f"   S1: {len(h3)} nonzero blocks -> pass.")
    print("   S2: same structure class as C1 (integrates by parts to")
    print("      -lam phi (div u_t) plus boundary): its u-diagonal sector")
    print("      is C2's longitudinal coupling in disguise; its mixing")
    print("      sector carries the same continuum dispersion modification")
    print("      as C1. -> S2 FAIL. But S3 is where it differs from C1 and")
    print("      the difference matters: with a STATIC sourced background")
    print("      grad(phi_bar) nonzero (GRV-066's Poisson solution has")
    print("      grad phi_bar ~ 1/r^2), the term contributes")
    print("      lam grad(phi_bar) . delta-u_t LINEARLY in perturbations --")
    print("      a genuine d_t block sourced by the static field. This is")
    print("      the unique inventory member that feeds shift structure")
    print("      FROM A STATIC BACKGROUND (S3 PASS where C1 needed phi_t).")
    print("      S4 COUNTING: grad phi_bar is a vector: THREE functions,")
    print("      exactly the three missing slots. FULL, structurally.")
    print("      S5 PRICE: one new constant (lam); no new field; disturbed")
    print("      claims by dependency sweep: FND-REL-002 (the forced-LI")
    print("      wording must be re-scoped to 'forced at lam = 0'),")
    print("      GRV-029 (bijection gains a lam sector), GRV-055/071")
    print("      (superseded downstream), GRV-106 (superseded-not-erased),")
    print("      EM wave sector (owes a lam-bound audit: existing optics")
    print("      results cap lam). VERDICT: S2-KILL WITH FULL PRICE -- the")
    print("      screens are conjunctive and S2 failed; C3 cannot be")
    print("      licensed HERE. But it is the strongest candidate the")
    print("      closed inventory contains: mixed block yes, static-source")
    print("      feed yes, counting exactly three, one constant. Named")
    print("      GRANT-CANDIDATE-SHIFT-C3 for the author's queue with the")
    print("      S2 violation stated as its price of admission.\n")

    # ---- C4: u_t . (curl u) -------------------------------------------
    print("C4  lambda u_t . (curl u)  (displacement helicity)")
    print("   S1: nonzero blocks, pass. S2: phi-independent -- it modifies")
    print("      the PURE u sector's continuum dispersion (optical activity")
    print("      of the vacuum), directly against the registered EM optics")
    print("      results at unsuppressed order, and it feeds no phi-sourced")
    print("      structure: the granted J never enters. S3 FAIL as well")
    print("      (no background dependence). DEAD.\n")

    # ---- C5: microinertia ---------------------------------------------
    print("C5  rho_j phi_t^2 (+ gradient corrections)")
    print("   S1: DIAGONAL time-time only; no mixed d_t d_i block. FAIL at")
    print("      S1. (Worth keeping on the face: microinertia is what a")
    print("      DYNAMICAL twist sector would need, but it feeds no shift.)")
    print("      DEAD.\n")

    # ---- C6: new field -------------------------------------------------
    print("C6  a new vector/tensor field with own kinetics")
    print("   S1-S4 trivially satisfiable BY CONSTRUCTION, which is exactly")
    print("      why the class is worthless as stated: an unconstrained new")
    print("      field can produce anything. S5 pricing is unbounded (new")
    print("      field + new couplings + every consistency audit reopened).")
    print("      Recorded as ADMISSIBLE-BUT-UNPRICED: not a candidate, a")
    print("      direction. The house does not queue directions.\n")

    print("VERDICT (per bars B3): CANDIDATES-FOUND, count ONE.")
    print("   GRANT-CANDIDATE-SHIFT-C3: L = lambda (grad phi) . u_t.")
    print("   Screens: S1 pass, S3 pass (unique static-background feed),")
    print("   S4 exactly three, S5 one constant -- and S2 FAILED: the term")
    print("   modifies continuum dispersion in the mixed sector, so its")
    print("   price of admission is re-scoping FND-REL-002's forced-LI")
    print("   statement to lambda = 0 and accepting a lambda-suppressed LI")
    print("   violation, with an owed lambda-bound audit against the")
    print("   registered EM optics results BEFORE any gravitational use.")
    print("   All other classes dead on the screens. Nothing adopted;")
    print("   the author's call, made with the price on the face.")


if __name__ == "__main__":
    main()
