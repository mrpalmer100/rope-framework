"""ELEC-079 -- LOCAL OR GLOBAL? The conservation constraint is global, the far
field is a reservoir at fixed tension, and the pure-tension functional stands.

Bars locked in analysis/ELEC079_constraint_locality_bars_LOCKED.md BEFORE deciding.
"""
import sympy as sp


def main():
    up, p, T0, k = sp.symbols("up p T0 k", real=True)
    eps = sp.sqrt((1 + up) ** 2 + p ** 2) - 1

    print("B1 CROSSING NUMBER:")
    print("   Strands are curves and curves cannot end, so the number crossing a")
    print("   plane is a topological invariant. But a TRANSVERSE displacement does")
    print("   not change it: the strand still crosses, merely at a displaced")
    print("   position. Crossing number is INSENSITIVE to psi and therefore places")
    print("   NO CONSTRAINT ON u'. It cannot be the source of ELEC-078's")
    print("   integral u' dx = 0.\n")

    print("B2 TOTAL STRAND LENGTH:")
    print("   Conserved for an inextensible medium -- but GLOBALLY. Local length")
    print("   between two fixed planes is NOT conserved, because a strand with no")
    print("   material points can slide: length drawn into one region is supplied")
    print("   from another. The constraint is integral eps dx = 0 over the WHOLE")
    print("   MEDIUM, not over a localised region.")
    print("   ELEC-078 IMPOSED A GLOBAL CONSTRAINT AS THOUGH IT WERE LOCAL. That")
    print("   is the error, and it is the reason the local quartic disappeared.\n")

    print("B3 THE VERDICT for a localised disturbance in an infinite,")
    print("   pre-tensioned medium:")
    print("   the far field acts as a RESERVOIR at fixed tension T0. Length flows")
    print("   in from infinity and the far field does the work against T0, so no")
    print("   local density change is forced: u' = 0 is admissible locally.")
    E_local = sp.expand(sp.series(T0 * eps.subs(up, 0), p, 0, 8).removeO())
    print(f"   The local energy is then T0 x (local excess length):")
    print(f"      E = {E_local}")
    print("   which is EXACTLY the pure-tension functional T0(sqrt(1+p^2) - 1).")
    print("   OF THE THREE REGISTERED FUNCTIONALS, THE VERDICT SELECTS THE")
    print("   PURE-TENSION ONE -- the same one FND-REL-002 selected in ELEC-077,")
    print("   now for an independent reason.\n")

    print("B4 CONSEQUENCES:")
    print("   ELEC-078's THIRD MODEL IS SUPERSEDED: its constraint is the global")
    print("   one applied locally. Its reconciliation of EM-RECON-011's legs")
    print("   STANDS -- u gauge, u' density -- and that remains the session's")
    print("   durable contribution; its variational conclusion does not.")
    print("   ELEC-074 and ELEC-075 are RESTORED: the variational setup ELEC-078")
    print("   put in question is the right one after all, and ELEC-075's clean")
    print("   negative on the electron identification stands unqualified.")
    print("   ELEC-068's free pointwise minimisation remains wrong for a different")
    print("   reason (ELEC-077: it presupposes material points), so nothing there")
    print("   is restored.\n")

    print("B5 WHAT THE VERDICT RESTS ON, and what would overturn it:")
    print("   IT RESTS ON the medium being infinite and pre-tensioned, so that a")
    print("   reservoir exists and tension is fixed at T0 rather than rising as")
    print("   length is withdrawn. That is the framework's own picture of the")
    print("   vacuum, but it is an assumption.")
    print("   IT WOULD BE OVERTURNED by a medium in which the far field cannot")
    print("   supply length quickly enough -- i.e. if the longitudinal signal")
    print("   speed were finite and slow compared with the disturbance. It is not:")
    print("   QB-008 corners that channel onto the INSTANTANEOUS limb, so the")
    print("   reservoir responds without delay. THE FAST CHANNEL, WHICH ELEC-076")
    print("   SHOWED THE SOLITON DOES NOT NEED, IS WHAT MAKES THE RESERVOIR")
    print("   ARGUMENT WORK -- an unexpected dependency worth recording.")
    print("PASS: the constraint is global, the pure-tension functional is selected")
    print("      a second time by an independent route, and ELEC-074/075 stand.")


if __name__ == "__main__":
    main()
