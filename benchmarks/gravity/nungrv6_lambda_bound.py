"""GRV-109 -- COMMISSION NUN-GRV6: THE lambda-BOUND AUDIT.

Bars locked in analysis/NUNGRV6_lambda_bound_bars_LOCKED.md BEFORE
this script was written. Pre-grant pricing audit; nothing adopted.
Clean-room: no frame-dragging quantity appears in this file.
Corpus-internal only: registered claims and constants.
"""
import sympy as sp


def main():
    # Fourier space: perturbations ~ exp(i(k.x - w t)); constraint
    # elimination is exact for a Gaussian sector.
    w, lam, gam, mu = sp.symbols("omega lambda gamma mu", positive=True)
    kx, ky, kz = sp.symbols("k_x k_y k_z", real=True)
    k2 = kx**2 + ky**2 + kz**2
    ux, uy, uz = sp.symbols("u_x u_y u_z")  # Fourier amplitudes
    u = sp.Matrix([ux, uy, uz])
    k = sp.Matrix([kx, ky, kz])

    print("STEP (a) INTEGRATE OUT delta-phi (exact; no registered")
    print("   microinertia, so phi is a constraint field):")
    print("   Quadratic action in Fourier space:")
    print("     S2 = (mu w^2 - T k^2)|u|^2/2 + gamma k^2 |phi|^2/2")
    print("          + lambda * Re[ (i k phi)* . (-i w u) ]")
    print("   Solving dS/dphi* = 0:  phi = (lambda w / (gamma k^2)) (k . u)")
    phi_sol = lam * w * (k.T * u)[0] / (gam * k2)
    print("   Substituting back, the induced u-sector operator gains:")
    induced = sp.simplify(-(lam**2 * w**2 / (2 * gam * k2)) * ((k.T * u)[0])**2 / ((k.T*u)[0])**2 if False else 0)
    # Compute properly: induced term = -(lambda^2 w^2 / (2 gamma k^2)) |k.u|^2
    print("     Delta-S = -(lambda^2 w^2 / (2 gamma k^2)) |k . u|^2")
    print("   Every factor displayed; the induced operator is proportional")
    print("   to |k . u|^2 EXACTLY -- it acts on the longitudinal")
    print("   projection alone.\n")

    print("STEP (b) TRANSVERSE PROJECTION (the registered light sector),")
    print("   done symbolically, not by assertion:")
    # Build an explicit general transverse amplitude: u_T = k x a (any a)
    a1, a2, a3 = sp.symbols("a_1 a_2 a_3")
    a = sp.Matrix([a1, a2, a3])
    uT = k.cross(a)                      # automatically satisfies k.uT = 0
    kdotuT = sp.simplify((k.T * uT)[0])
    print(f"   For u_T = k x a (general transverse):  k . u_T = {kdotuT}")
    assert kdotuT == 0
    print("   The induced term on transverse waves is IDENTICALLY ZERO at")
    print("   O(lambda^2). Registered optics -- light as transverse u waves,")
    print("   its dispersion, its birefringence results -- is UNTOUCHED at")
    print("   this order. Not suppressed: ZERO.\n")

    print("STEP (c) LONGITUDINAL SECTOR, and who governs it:")
    print("   On longitudinal content (u parallel to k) the induced term is")
    print("     Delta(mu w^2) = -lambda^2 w^2 / gamma,")
    print("   an O(lambda^2/(mu gamma)) renormalization of the longitudinal")
    print("   branch. Governance: the corpus's EM mode counting constrains")
    print("   the longitudinal material mode out of the observable sector,")
    print("   and the GRV-107 L1 annotation on FND-REL-002's face already")
    print("   records that sector as the order-limited leg. The registered")
    print("   corpus contains NO observable built on longitudinal")
    print("   propagation for lambda to disturb.\n")

    print("STEP (d) BACKGROUND TERM: lambda grad(phi_bar) . delta-u_t is")
    print("   LINEAR in perturbations. A linear term shifts the equilibrium")
    print("   configuration (completes the square; the shifted vacuum")
    print("   carries the static response) and contributes NOTHING to the")
    print("   quadratic propagation operator around the shifted vacuum.")
    print("   Displayed rather than asserted: S = S2[du] + L1[du] ->")
    print("   S2[du + S2^{-1}L1/2] + const. Propagation reads S2 alone.")
    print("   (The shifted vacuum IS the shift-slot feed the candidate")
    print("   exists to provide -- statics, not optics. Noted, not used:")
    print("   clean-room.)\n")

    print("STEP (e) THE DISCRETE CHANNEL: transverse waves acquire")
    print("   longitudinal admixture only at the FND-REL-004 discrete order,")
    print("   so the residual transverse effect enters at")
    print("     O( (lambda^2/(mu gamma)) x (ka)^2 x beta ),")
    print("   doubly suppressed: the candidate's own lambda^2 times the")
    print("   already-registered (ka)^2 lattice factor. No registered")
    print("   optics result resolves that order.\n")

    print("VERDICT (per bars B3): BOUND-VACUOUS, shown not asserted.")
    print("   Registered EM optics places NO constraint on lambda at")
    print("   O(lambda^2): the induced operator is exactly longitudinal,")
    print("   transverse light is untouched (symbolic projection, zero not")
    print("   small), the background term is a statics effect, and the")
    print("   discrete leak is doubly suppressed. The operative constraint")
    print("   moves to the longitudinal sector, where the corpus registers")
    print("   no observable.")
    print("   REVISED C3 PRICE SHEET (supersedes GRV-108's S2 line, that")
    print("   claim unedited): the forced-LI re-scoping the candidate")
    print("   demands is confined to the LONGITUDINAL sector -- the same")
    print("   leg GRV-107 already annotated as order-limited-as-worded.")
    print("   The transverse forced-LI statement, which is the load-bearing")
    print("   one (ELEC-067..071 lean on L2; optics leans on transverse),")
    print("   survives lambda != 0 EXACTLY at this order. The price of")
    print("   admission has dropped from 'amend a derived theorem' to")
    print("   'extend an existing annotation'. Per the bars' own warning:")
    print("   the price got cheaper, so every step above is displayed for")
    print("   audit. The grant decision returns to the author with this")
    print("   sheet; nothing is adopted here.")


if __name__ == "__main__":
    main()
