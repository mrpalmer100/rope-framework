"""GRV-059 -- THE SOURCE-AND-FORM AUDIT: nothing in the action carries a
stationary mass current, so the present gravity sector is falsified by frame
dragging.

Bars locked in analysis/GRV059_source_audit_bars_LOCKED.md BEFORE the audit.
"""
GPB_MEAS, GPB_ERR, GPB_GR = 37.2, 7.2, 39.2
LARES_FRAC = 0.05


def main():
    print("B1 STEP 1 -- WHAT IS IN THE GRAVITATIONAL SOURCE?")
    print("   The registered source is GRV-005: 'static force balance")
    print("   div(stress) = -f IS the conservation law; the Poisson equation and")
    print("   the 1/r conditioning field are FORCED by 3D elastostatics.'")
    print("   f is a FORCE DENSITY. There is no velocity in it, no momentum")
    print("   density, no vorticity, no angular-momentum coupling.")
    print("   GRV-026 asserts covariant matter sourcing, but GRV-057 established")
    print("   that its covariance fingerprint tested the SCALAR channel only.")
    print("   GRV-058's nonlinear mechanism couples to d_t of the FIELD, which is")
    print("   a different object again.")
    print("   GRV-036 does register 'angular momentum as circulation' -- but as a")
    print("   property of MATTER knots that survives reconnection, not as a term")
    print("   in the gravitational action.")
    print("   STEP 1 RETURNS NOTHING. No term linear in velocity, momentum")
    print("   density, vorticity or angular momentum appears in the registered")
    print("   gravitational source.")
    print("   Steps 2-5 are therefore not reached: there is no candidate whose")
    print("   weak-field response could be derived, no stationary vector field to")
    print("   test, and no structure to compare with (J x r)/r^3.\n")

    print("B2 THE CONCLUSION, in the reviewer's terms and not softened:")
    print("   THE PRESENT ROPE GRAVITY SECTOR IS EXPERIMENTALLY FALSIFIED BY FRAME")
    print("   DRAGGING. Recovery would require a momentum-current coupling NOT")
    print("   CURRENTLY CONTAINED IN THE FRAMEWORK.")
    print("   GRV-058 called this 'not yet a refutation' on the grounds that a")
    print("   rescue was conceivable. That was too generous: a conceivable")
    print("   mechanism that does not appear anywhere in the action is not a")
    print("   defence, it is a proposal for a different theory.\n")

    print("B3 THE CORRECTED ARITHMETIC:")
    print(f"   Gravity Probe B: {GPB_MEAS} +/- {GPB_ERR} mas/yr against a GR value")
    print(f"   of -{GPB_GR}; zero differs from the central value by "
          f"{GPB_MEAS/GPB_ERR:.1f} SIGMA. This is the robust number.")
    print(f"   LARES/LAGEOS: mu = 1.00 +/- {LARES_FRAC}, a FEW-PERCENT AGREEMENT")
    print("   with GR whose uncertainty is dominated by a gravity-model")
    print("   systematic, NOT a Gaussian sigma. It should not be converted into a")
    print("   sigma count, and GRV-058's '20 sigma' and the plain-language")
    print("   'twenty times over' are WITHDRAWN as unsupported by that error model.")
    print("   The conclusion does not depend on them.\n")

    print("B4 THE DIAGNOSIS, stated in the right variables:")
    print("   GRAVITOELECTRIC (g_00): sourced by mass density. The framework has")
    print("     this -- Poisson from elastostatics, and the classical tests are")
    print("     unconditional (GRV-029).")
    print("   GRAVITOMAGNETIC (g_0i): sourced by MOMENTUM DENSITY T_0i. The")
    print("     framework does not have this at all.")
    print("   A theory can reproduce Newtonian and static gravity completely and")
    print("   still fail here, because frame dragging tests the OFF-DIAGONAL")
    print("   components, not the scalar potential. That is exactly the corpus's")
    print("   situation, and it explains why the failure went unnoticed through")
    print("   fifty-eight gravity claims.\n")

    print("B5 WHAT A SUCCESSOR MECHANISM MUST REPRODUCE -- all six, so that no")
    print("   future patch is accepted on partial agreement:")
    for i, req in enumerate((
            "dependence on the total angular momentum J",
            "the correct 1/r^3 far-field behaviour",
            "the vector/dipole angular structure, A_g ~ (J x r)/r^3",
            "the sign",
            "the numerical coefficient",
            "consistency with the already-claimed static-gravity sector"), 1):
        print(f"     ({i}) {req}")
    print("   AND IT MUST BE A NEW DERIVATION CAMPAIGN, not an assumption that")
    print("   'the medium responds to angular momentum'. GRV-056 already showed")
    print("   the obvious candidate -- gyroscopic twist coupling -- carries no")
    print("   spatial derivative and therefore has the wrong form.")
    print("PASS: the audit returns nothing, and the falsification is registered")
    print("      in the terms the evidence supports.")


if __name__ == "__main__":
    main()
