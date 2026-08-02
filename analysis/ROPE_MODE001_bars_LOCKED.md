# ROPE-MODE-001 locked bars — standing-wave atomic-shell gate

## Question
Does the present certified linked rope geometry produce a mesh-converged normal-mode hierarchy that resembles atomic shell spacing, rather than the ordinary harmonics of a closed string?

## Scope
This is the simplest linear constant-tension, constant-linear-density wave operator on each closed rope component. Tension and density are set to unity, so only dimensionless frequency ratios are interpreted. The unchanged ELEC-009 geometry and hard topology certificate are used. This benchmark does not introduce spin, charge, Coulomb dynamics, a nucleus, or electron statistics.

## Locked bars

1. **Certified reference:** the ELEC-009 geometry remains unit linked, with `d_min >= 0.060` and `||Lk|-1| <= 0.03`.
2. **Mesh convergence:** the maximum relative change in paired frequencies from 256 to 512 samples is below 1%.
3. **Ordinary harmonic law:** normalized paired frequencies fit `omega_n/omega_1 = n` with `R^2 > 0.995`.
4. **Atomic-shell advantage:** either the hydrogenic `1/n^2` or `1-1/n^2` template must improve RMS error over the ordinary harmonic law by at least 10%.
5. **Shell degeneracy:** the mode multiplicities must reproduce the atomic shell capacities `2n^2` for the tested levels.

The shell interpretation requires bars 1, 2, 4, and 5. Passing bar 3 while failing bars 4 and 5 supports ordinary closed-string harmonics rather than atomic shells.
