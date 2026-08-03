"""FND-022 -- THE SUPERLUMINAL CHANNEL IS REQUIRED, AND IT IS TWO DIFFERENT
OBJECTS: a finite-speed elastic wave and an instantaneous constraint.

Bars locked in analysis/FND022_two_channels_bars_LOCKED.md BEFORE computing.
"""
import numpy as np

C = 2.99792458e8
K_OVER_T0_BELL = 1.9e8


def main():
    print("B1 WHAT REQUIRES A FASTER-THAN-LIGHT INFLUENCE:")
    rows = [
        ("QB-007", "Modeled",
         "winner-take-all localization -- the detector CLICK. Without spacelike "
         "depletion g2 is pinned >= 1 (machine-checked) against a measured ~0.18. "
         "The fast channel is called 'the ONLY NATIVE CANDIDATE'."),
        ("QB-012", "Derived",
         "a rope-native supplier of the nonlocal conditional must be "
         "NON-PROPAGATING: co-material carriers need 4.3 us to cross "
         "loophole-free geometry with 200 ns windows. A DERIVED no-go against "
         "every sub-luminal carrier."),
        ("QB-023", "Modeled",
         "entanglement -- 'the reel IS the nonlocal element', named as such."),
        ("ELEC-079/080", "Modeled",
         "the reservoir that lets the medium carry light AT ALL needs the far "
         "field to supply length without delay."),
    ]
    for cid, st, why in rows:
        print(f"   {cid:14s} [{st:9s}] {why}")
    print("   SO THE ANSWER IS YES, AND EMPHATICALLY: measurement, Bell")
    print("   correlations, entanglement, and arguably the optics sector all")
    print("   depend on it. Removing it does not cost the framework a prediction;")
    print("   it costs the framework quantum mechanics.\n")

    print("B2 THE LONGITUDINAL WAVE SPEED (FND-021's relation):")
    cL = C * np.sqrt(K_OVER_T0_BELL)
    print(f"   c_L = c sqrt(k/T0) = c x {np.sqrt(K_OVER_T0_BELL):.3e} "
          f"= {cL:.3e} m/s")
    print("   FAST -- fourteen thousand times light -- BUT FINITE.\n")

    print("B3 CAN THAT WAVE DO THE JOB? NO.")
    print("   QB-008 records that BANCAL'S SIGNALLING THEOREM EXCLUDES ALL FINITE")
    print("   SPEEDS -- any finite-speed hidden influence, however fast, permits")
    print("   superluminal signalling between suitably arranged parties. That is")
    print("   exactly why QB-008 forced the conjecture onto the")
    print("   INSTANTANEOUS-CONSTRAINT limb rather than a fast-wave limb.")
    print("   THE FINITE-SPEED LONGITUDINAL WAVE IS EXCLUDED FROM SUPPLYING BELL")
    print("   CORRELATIONS, no matter how large k/T0 is.\n")

    print("B4 THE DISTINCTION, stated because the corpus has been blurring it:")
    print("   (a) THE LONGITUDINAL ELASTIC WAVE. Speed c sqrt(k/T0), finite,")
    print("       gapless, dark at linear order. It EXISTS BECAUSE k IS FINITE")
    print("       (FND-021). Claims: EM-RECON-011, EM-RECON-012, ELEC-067.")
    print("   (b) THE INSTANTANEOUS CONSTRAINT. Not a wave. No speed. The")
    print("       RIGIDITY of the inextensible limit -- the k -> infinity idealisation.")
    print("       Claims: QB-007, QB-008, QB-012, QB-023, and the reservoir")
    print("       argument in ELEC-079.")
    print("   THESE ARE DIFFERENT OBJECTS AND THEY WANT OPPOSITE LIMITS OF k.")
    print("   (a) needs k FINITE or there is no wave at all.")
    print("   (b) needs k -> INFINITY or the constraint propagates and Bancal")
    print("       excludes it.")
    print("   THE FRAMEWORK CURRENTLY WANTS BOTH, from the same modulus.\n")

    print("B5 THE CONSEQUENCE:")
    print("   FND-021 resolved 'inextensible vs extensible' in favour of finite k,")
    print("   which is right for the elastic wave and WRONG FOR THE CONSTRAINT")
    print("   that quantum mechanics needs. The honest position is that the medium")
    print("   must behave as k -> infinity for the nonlocal conditional and as")
    print("   k finite for the longitudinal wave, and NOTHING IN THE CORPUS")
    print("   EXPLAINS HOW ONE MEDIUM DOES BOTH.")
    print("   THIS IS NOT OBVIOUSLY FATAL. A constraint force and a propagating")
    print("   mode are different sectors of one elastic system, and rigid")
    print("   constraints in mechanics routinely coexist with finite-speed waves --")
    print("   a rigid rod's constraint is instantaneous in the idealisation while")
    print("   its sound speed is finite. Whether that carries over to a")
    print("   relativistic medium with a preferred frame is EXACTLY the open")
    print("   question, and it has not been asked.")
    print("   THE PARAMETER CARD MUST DISTINGUISH THE TWO CHANNELS.")
    print("PASS: the answer is yes and load-bearing, and the question exposed a")
    print("      conflation between a finite wave and an infinite-stiffness limit.")


if __name__ == "__main__":
    main()
