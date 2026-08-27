# COMMISSION COMPOSITE -- RESULTS (2026-08-18)

Executed under analysis/COMPOSITE_wave_build_bars_LOCKED.md.
Benchmark: benchmarks/foundations/composite_wave_build.py.
Geometry imported from the BLOCH-L build (reading A, load-bearing by
that file's Leg 0 isotropy control). Clean room held: the registered
bracket and the window ceiling appear in Leg 6 only.

**VERDICT: BRACKET-TIGHTENED.** Both customers paid. The exact
phase-averaged two-level kinetic energy is in closed form, verified
against a direct two-torus average to 1e-13; the exact energy total is
**Sigma_wave = [3.222, 4.313] T0 per coarse strand per unit axial
length** (areal [9.67, 12.94] T0/a^2), inside the registered bracket at
every corner. The bill remains payable: dynamical share [0.690, 0.768]
against the registered ceiling 0.889, margin 1.157x.

## 1. THE CATCH: THE BRACKET'S TWO LEGS SAT IN DIFFERENT CONVENTIONS

The path factor (arc length per unit axial length) is
1/(c_ax,1 c_ax,2) and is NOT convention-blind: swapping the reading
swaps sin <-> cos.

    reading A (axial cos = sin psi, LOAD-BEARING):  2.01135
    reading B (axial cos = cos psi):                2.40914

The registered bill carried the level-1 path as sqrt(3) = 1.73205,
which is reading A -- and carried the two-level path as 2.409, which is
reading B, imported from the fine-weave session's coverage leg. **One
bracket, two conventions, one in each leg.**

THE LESSON IS THE THIRTEENTH CATCH'S, RECURRING. The fine-weave file was
swept for the convention correction and cleared, on the ground that its
compensation identity uses sin^2 psi_1 sin^2 psi_2 and is invariant
under the swap. That is true of the IDENTITY. The same file's PATH
FACTOR is convention-sensitive and was not examined, because the check
that passed was blind to it. When a check keeps passing, ask what it is
blind to.

DIRECTION, disclosed: the path factor multiplies the whole per-arc
energy, so the correction brings the wave total DOWN. The fine-weave
coverage number inherits the same factor 0.8349 (coverage falls, packing
headroom rises, that session's assertions still pass) -- a TIGHTENING,
not a break, and it is flagged here for a follow-up rather than acted on
(registered text is history and is not edited).

A second, independent sanity signal for reading A: under it R_1 > R_2
(0.2251 > 0.0940) -- the backbone is wider than the sub-winding it
carries. The inverted reading nests a wider sub-winding inside a
narrower backbone.

## 2. THE EXACT KINETIC ENERGY (first customer)

Material velocity of the nested rotating state, both rigid rotations
superposed, v = Omega_1 (zhat x r) + Omega_2 (t_1 x d), r = C + d.
Exact phase average over the two-torus, in closed form:

    <|v|^2> = Omega_1^2 R_1^2                       [level-1 orbit]
            + Omega_1^2 (R_2^2/2)(1 + c_ax,1^2)     [offset widening]
            + Omega_2^2 R_2^2                       [level-2 orbit]
            + 2 Omega_1 Omega_2 c_ax,1 R_2^2 x s    [CROSS, s = +/-1]

using <d> = 0 (kills the linear cross), t_1 . d = 0, and
(zhat x d).(t_1 x d) = (zhat . t_1) R_2^2. Numeric control on the full
two-torus: agreement to 1e-13 at three corners.

At the standing kb bound, aligned (T0_f units): 1.000000 + 0.116172 +
0.754087 + 0.418578. **The bracket's construction summed the first and
third only** -- it omitted both the offset widening and the cross term.
Omega_1 is fixed by the level-1 centripetal balance (v_1 = c exactly,
FND-132's identity recomputed as a control), Omega_2 by the level-2
balance in the co-moving frame with the bending term RETAINED (the
neutrality theorem is a level-1 statement; s_2 is not 1/3).

## 3. THE HANDEDNESS FORK (a finding, not a defect)

The cross term is nonzero and its sign is the relative handedness of the
level-2 winding against the level-1 rotation, which the registry does
not fix (population-handedness, standing board). **The exact total is
therefore two-valued on the registry.** Both signs are carried; neither
is adopted. This is the honest form: the number is exact given a
handedness, and the handedness is a named open item with an
already-registered route to a reading (ensemble construction).

## 4. THE BOX

    kb = 0,      anti-aligned:  Sigma_wave = 3.2219   <- lower edge
    kb = 0,      aligned:                    3.8256
    kb = bound,  anti-aligned:               3.4713
    kb = bound,  aligned:                    4.3132   <- upper edge

The residual width is NO LONGER an approximation gap. It decomposes
into exactly two named causes: the discrete handedness fork and the
standing kb range. Level-1-only limit control (R_2 -> 0) reproduces the
registered level-1 exact value 2.5981 T0.

## 5. WHAT MOVES

Sigma_wave's registered value narrows from the bracket to the computed
box. The level-1-only edge (2.598) is RETIRED AS AN EDGE OF THE
COMPOSITE -- it was never the composite object, only the level-1 one,
and the two must not share a bracket. The lower edge rises to 3.222.
The upper edge falls to 4.313 (two effects in opposite directions: the
path correction pulls down, the omitted offset and cross terms push up;
down wins). No other registered number moves; both tripwires untouched.

## REFUSALS

No handedness adopted. The fine-weave coverage correction is flagged,
not applied (a separate session owns it). The inherited tension
bookkeeping (1.0 T0_f per unit arc) is declared inherited, not
re-derived -- if it is ever corrected, the bill and this build move
together. T_fibre untouched (tripwire). The pre-stress/contact gap
untouched.
