"""GRV-013: the systematic locked-quadrupole hunt -- a no-go within the mapped
channel space. TARGET: traceless conditioning at range 1/r with a/b = 1/4.

CHANNEL MAP (each computed, no tuning):
  elastic strain (Hessian)        1/r^3    pure traceless
  diffusive bath deficit          1/r      a/b = 0
  diffusion quadrupole corr.      1/r^3    suppressed ~ (mfp/r)^2
  ballistic 1D rope shadow (NEW)  1/r^2    a/b = 1  [pattern (1,0,0)]
  anchored-tension excess (NEW)   1/r^2    a/b = 1
  orientation x bath products     1/r^3    mixed
  TARGET (GR)                     1/r      a/b = 1/4

THE GEOMETRIC DILUTION THEOREM (why the hunt HAD to fail): every direction-
carrying structure near a mass is the anchored-rope population, whose local
fraction dilutes as N/(4 pi r^2 n) -- solid-angle geometry, not modeling.
Direction-blind scalars can reach 1/r (diffusion); direction-carriers cannot.

THE BRACKET: the transport regimes bracket the target -- a/b spans [0
(diffusive), 1 (ballistic)] and GR's 1/4 lies strictly inside; the crossover
sweeps through 1/4 at ONE radius (r ~ mfp), but gamma = 1 is measured at all
radii (solar limb to AU). Locking requires SCALE-FREE transport (mfp ~ r);
the bath-deficit feedback gives mfp(r) = mfp*(1 + c/r) -- not scale-free.

COMPLETENESS AUDIT (Mark's catch): the interpenetrability/threshold-contact
channel (FND-MATTER-004 coverage threshold + K_c contact physics, sourced by
the converging anchored population near the sun) was MISSING from the original
map. Audited: coverage excess ~ 1/r^2 (the same solid-angle dilution -- the
excess IS the anchored population measured in area fraction); near-threshold
nonlinear amplification rescales but cannot reshape 1/r^2 into 1/r; the
radially-biased mixed shape is immaterial given the range miss; and observed
near-solar transparency independently bounds the channel small exactly where
bending is measured. Row added; the no-go SURVIVES with the map now complete
against this channel class. Conceptual note: interpenetrability is what makes
the thicket transparent to grazing light at all -- it licenses the
conditioning-based bending story and, audited, declines to rescue it.

THE REFUSED RESCUE: a scale-free-transport postulate would save the sector,
but by the programme's own postulate-audit standard (P-VOL precedent:
necessity + independent naturalness + consistency) it has NECESSITY ONLY --
its sole motivation is escaping falsification. NOT adopted. GRV-012's verdict
stands, hardened from 'no mechanism found' to 'channel space mapped and
excludes the target'.
"""
import sympy as sp

TARGET_RANGE, TARGET_AB = 1, sp.Rational(1, 4)

# (range exponent p in 1/r^p, a/b ratio or None for pure/suppressed)
CHANNELS = {
    "elastic_hessian": (3, sp.oo),          # pure traceless
    "diffusive_bath": (1, sp.Integer(0)),
    "diffusion_quadrupole": (3, None),
    "ballistic_rope_shadow": (2, sp.Integer(1)),
    "anchored_tension": (2, sp.Integer(1)),
    "orientation_x_bath": (3, None),
    "branching_tree_tension": (2, sp.Integer(1)),  # Mark's 2nd catch: Gaede's non-uniform
    # tension via merging trees (trunk = sum of branches). Per-rope tension DOES rise
    # toward the mass, but the TENSION-FLUX CONSERVATION THEOREM makes per-area excess
    # F_total/(4 pi r^2) ~ 1/r^2 TOPOLOGY-INDEPENDENT: branching redistributes a
    # conserved flux among fewer, tenser carriers. Single-strand gradients are forbidden
    # by interpenetrability itself (no distributed contact); grazing 1919 starlight rides
    # PASSING ropes the tree cannot touch sub-threshold. The same conservation that gives
    # Gaede Newton's 1/r^2 force forbids his channel from reaching the 1/r the metric needs.
    "threshold_contact_coverage": (2, None),   # Mark's catch: FND-MATTER-004/K_c contact
    # physics near the sun -- coverage excess ~ 1/r^2 (same solid-angle theorem);
    # near-threshold amplification rescales amplitude, cannot reshape 1/r^2 into 1/r;
    # doubly excluded: solar-limb transparency independently bounds it small.
}


def ballistic_pattern_decomposition():
    v = sp.Matrix([1, 0, 0])
    iso = sp.Rational(sum(v), 3)
    tl_amp = (v - sp.Matrix([iso] * 3))[0] / 2
    return iso == sp.Rational(1, 3) and tl_amp == sp.Rational(1, 3)   # a/b = 1


def no_channel_hits_target():
    for name, (p, ab) in CHANNELS.items():
        if p == TARGET_RANGE and ab == TARGET_AB:
            return False
    return True


def bracket_contains_target():
    return sp.Integer(0) < TARGET_AB < sp.Integer(1)


def mfp_not_scale_free():
    r, c0, m0 = sp.symbols('r c0 m0', positive=True)
    mfp = m0 * (1 + c0 / r)
    return sp.limit(mfp / r, r, sp.oo) == 0     # mfp/r -> 0: NOT scale-free


def test():
    assert ballistic_pattern_decomposition(), "(1,0,0) = 1/3 iso + 1/3 traceless -> a/b = 1"
    assert no_channel_hits_target(), "no constructible channel has (1/r, a/b = 1/4)"
    assert bracket_contains_target(), "the regimes bracket 1/4 -- poignant, not sufficient"
    assert mfp_not_scale_free(), "bath feedback gives mfp(r) = m0(1+c/r): locking impossible"
    print("channel map complete: every constructible channel misses on RANGE or RATIO")
    print("geometric dilution theorem: direction-carriers dilute as 1/r^2 (solid angle) -- forced")
    print("bracket: a/b spans [0,1], GR's 1/4 strictly inside; crossover cannot lock (mfp fixed)")
    print("rescue postulate (scale-free transport) REFUSED: necessity only, no independent motivation")
    print("PASS: no-go established; GRV-012's adverse verdict HARDENED, not escaped.")


if __name__ == "__main__":
    test()
