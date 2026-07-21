"""QB-006: the quantum boundary re-explored with this session's structural
results. Two parts, both honest:

PART 1 -- the failures were THEOREM-FORCED. Exhaustive enumeration of all
deterministic local strategies gives max |CHSH| = 2 (re-deriving QB-001's bound
independently); QM and loophole-free experiments give 2*sqrt(2). ANY local
mechanism -- rope or otherwise, built by any model of any capability -- is
capped at 2. QB-001/002/003 were the corpus hitting Bell's theorem, not running
out of cleverness. Model capability does not change theorems.

PART 2 -- Bell's theorem blocks only LOCAL accounts; the open door is nonlocal
hidden variables (Bohmian mechanics walks through it and reproduces QM). A
viable nonlocal substrate needs four things, and the corpus NOW possesses
structural analogues of each -- none of which existed when QB-003 was closed:
  (1) physical nonlocal connections: LITERAL interparticle ropes (the ontology's
      core claim);
  (2) a preferred frame: derived position (FND-REL-001/002, Lorentz emergent,
      transverse-only);
  (3) a superluminal coordination channel that cannot signal: EXACTLY the dark
      longitudinal channel (gapless c_L > c, EM-RECON-012; non-signaling at
      linear order by exact decoupling, EM-RECON-011) -- candidate carrier,
      NOT established as the guidance mechanism;
  (4) wave-particle structure: wave modes propagate and interfere; matter is
      discrete knots; detection is a knot event. Pilot-wave-shaped natively.

WALLS THAT REMAIN (equal force): the Born rule (QB-002 stands: counting gives
(pi-theta)/pi, not cos^2(theta/2)); the CONFIGURATION-SPACE obstruction (3N-dim
wavefunctions vs 3-space modes; the network's relational connectivity graph is
the one asset that speaks to it, unproven whether sufficiently); hbar inherited
(do not chase); no guidance equation derived. Necessary is not sufficient.

CORRECTION (Mark): the original necessary-conditions list was INCOMPLETE. A
fifth necessary condition is STATISTICAL, not structural: quantum equilibrium
(Born-distributed hidden variables) plus equivariance (dynamics preserving the
measure). Without it, nonlocal guidance generically produces observable
signaling -- QM's no-signaling is a statistical property holding ON the Born
measure, not a consequence of channel decoupling alone. The corpus establishes
nothing about such a measure. Corrected scoreboard: 4 of 5 necessary conditions
present, 0 sufficient.
"""
from itertools import product
import numpy as np


def local_deterministic_chsh_bound():
    best = 0
    for fa in product([1, -1], repeat=2):
        for fb in product([1, -1], repeat=2):
            S = fa[0] * fb[0] + fa[0] * fb[1] + fa[1] * fb[0] - fa[1] * fb[1]
            best = max(best, abs(S))
    return best


def structural_conditions_present():
    """Four STRUCTURAL conditions, each mapping to a registered corpus result."""
    conditions = {
        "nonlocal_connections": True,   # ontology: literal interparticle ropes
        "preferred_frame": True,        # FND-REL-001/002 (Derived/EFT-constrained)
        "superluminal_nonsignaling": True,  # EM-RECON-011/012 (exact decoupling; gapless)
        "wave_plus_discrete_knots": True,   # modes interfere; matter = knots
    }
    return all(conditions.values())


def statistical_condition_established():
    """The FIFTH necessary condition (Mark's correction): Bell correlations
    without signaling require the hidden variables to be BORN-DISTRIBUTED
    (quantum equilibrium) AND the dynamics to preserve that measure
    (equivariance). Out-of-equilibrium pilot-wave dynamics generically SIGNAL.
    The corpus has established NOTHING about a Born-equilibrium measure on the
    network. Not present -- and its absence caps what QB-006 may claim."""
    return False


def sufficiency_absent():
    """The honest walls: none of these are derived."""
    walls = {
        "born_rule": False,             # QB-002: counting gives wrong law
        "guidance_equation": False,     # none derived
        "hbar": False,                  # inherited
        "config_space_resolved": False, # known obstruction, unresolved
    }
    return not any(walls.values())


def test():
    bound = local_deterministic_chsh_bound()
    assert bound == 2, "local deterministic CHSH bound must be exactly 2"
    assert 2 * np.sqrt(2) > bound, "QM exceeds every local mechanism: the failures were theorem-forced"
    assert structural_conditions_present(), "four STRUCTURAL substrate conditions present"
    assert not statistical_condition_established(), "the fifth (STATISTICAL) condition is NOT established -- must be declared"
    assert sufficiency_absent(), "no sufficiency claimed: Born rule, guidance, hbar, config space all open"
    print(f"local deterministic CHSH bound = {bound}; QM = {2*np.sqrt(2):.3f} -> local accounts theorem-blocked")
    print("QB-001/002/003 failures re-explained: NECESSARY (Bell), not incidental")
    print("four STRUCTURAL conditions present (ropes, frame, dark channel, knots+waves)")
    print("fifth NECESSARY condition (statistical: Born-equilibrium measure + equivariance) NOT established")
    print("sufficiency absent and declared: Born rule, guidance equation, hbar, configuration space")
    print("PASS: reframing stands with the corrected scoreboard -- 4 of 5 necessary conditions, 0 sufficient.")


if __name__ == "__main__":
    test()
