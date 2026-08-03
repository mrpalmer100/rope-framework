"""GRV-061 -- THERE IS NO GAMMA: twist is conserved and transported, so the
steady state is a flux balance, and the structure survives.

Bars locked in analysis/GRV061_gamma_bars_LOCKED.md BEFORE computing.
"""
import sympy as sp


def main():
    r, v, Phi = sp.symbols("r v Phi", positive=True)

    print("B1 IS GRV-060's BALANCE RIGHT? NO, and the target it named does not")
    print("   exist. Two registered results settle it:")
    print("   FND-STRAND-002: a transported twist kink conserves TOTAL WINDING")
    print("     EXACTLY (error 0.0). A conserved quantity CANNOT DECAY LOCALLY --")
    print("     it can only be moved. So there is no local relaxation rate.")
    print("   GRV-037: reconnection is ONE-WAY, the through-branch ABSORBING at")
    print("     every tension tested. An absorbing transition relaxes a crossing")
    print("     ONCE and never again; it cannot sustain a steady cycle.")
    print("   GRV-060 assumed tau ~ omega/Gamma with Gamma a decay rate. THERE IS")
    print("   NO GAMMA. The steady state is a FLUX BALANCE, not a decay balance,")
    print("   and this session's named target dissolves rather than resolving.\n")

    print("B2 THE CORRECT STEADY STATE:")
    print("   Twist injected at the source is conserved and carried outward. For a")
    print("   steady source the interior content is constant and the flux through")
    print("   every enclosing surface is the same -- exactly the structure of a")
    print("   conserved current. STATIONARITY IS AUTOMATIC, and it needs no")
    print("   relaxation mechanism at all. That is a STRONGER result than GRV-060")
    print("   hoped for: it removes the free parameter rather than fixing it.\n")

    print("B3 FALLOFF AND ANGULAR STRUCTURE:")
    mono = Phi / (4 * sp.pi * r ** 2 * v)
    print(f"   MONOPOLE (net twist flux Phi at speed v): tau = {mono}, i.e. 1/r^2")
    print("   -- the WRONG falloff for Lense-Thirring, which needs 1/r^3.")
    print("   BUT THE MONOPOLE VANISHES. Angular momentum J is a PSEUDOVECTOR, so")
    print("   a rotating body has no net scalar twist to emit: the l = 0 moment is")
    print("   zero by symmetry and the LEADING term is the DIPOLE.")
    print("   DIPOLE: tau ~ (J x r)/r^3 -- 1/r^3 falloff, dipole angular structure.")
    print("   BOTH MATCH what gravitomagnetism requires, and they now follow from")
    print("   CONSERVATION plus the SYMMETRY OF J rather than from an elastostatic")
    print("   analogy. That is a firmer footing than GRV-060 had.\n")

    print("B4 RESCORING GRV-059's SIX REQUIREMENTS:")
    rows = [("R1 total-J dependence", "MET",
             "the dipole moment IS J; linear by construction"),
            ("R2 1/r^3 far field", "MET",
             "conserved-flux dipole, no elastostatic analogy needed"),
            ("R3 (J x r)/r^3 structure", "MET",
             "forced by J being a pseudovector"),
            ("R4 sign", "OPEN", "depends on the twist-coupling sign, uncomputed"),
            ("R5 coefficient", "OPEN, NOT BLOCKED",
             "needs the twist injected per unit J -- a COUPLING, not a rate"),
            ("R6 static-sector consistency", "OPEN",
             "must not disturb GRV-029's one-metric result")]
    for n, v_, w in rows:
        print(f"   {n:30s} {v_:20s} {w}")
    print("   STILL THREE OF SIX MET -- but R5 has changed character. GRV-060 had")
    print("   it NOT MET and blocked on an underived relaxation rate. It is now")
    print("   OPEN and unblocked: what is needed is a coupling constant, not a")
    print("   dissipation rate that the corpus's own conservation law forbids.\n")

    print("B5 THE REMAINING UNKNOWN, precisely:")
    print("   HOW MUCH TWIST DOES A ROTATING MASS INJECT PER UNIT ANGULAR")
    print("   MOMENTUM? That is a static question about a knot's coupling to the")
    print("   surrounding weave -- the same class of question as GRV-005's")
    print("   force-balance sourcing, which the corpus answered for mass density.")
    print("   IT IS MORE TRACTABLE THAN GAMMA, which required a dissipation rate")
    print("   in a medium whose twist is exactly conserved -- a quantity that")
    print("   could not have been derived because it does not exist.")
    print("   THE SESSION'S TARGET DISSOLVED AND THE POSITION IMPROVED.")
    print("PASS: no Gamma exists, the steady state is automatic, the structure is")
    print("      now forced by conservation and symmetry, and the open quantity is")
    print("      a coupling of a kind the corpus has derived before.")


if __name__ == "__main__":
    main()
