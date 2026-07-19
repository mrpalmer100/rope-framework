# `rope_solver.geometry.curve`

Discrete-curve forces (rope tension)

> geometry/curve.py  --  Canonical discrete-curve forces.

## `curve_field_energy(curves, q2=1.0, a=0.14)`

Total softened-Coulomb field energy of a list of curves (proxy field).

Sums over all node pairs across all curves with a single 1/r kernel.

## `pair_repulsion_force(C, other, q2=1.0, a=0.14, core=None, core_k=60.0)`

Field repulsion on nodes of C from another curve `other`.

If `core` is given, adds a HARD short-range repulsion for separations
below `core`, enforcing non-crossing so the linking number is preserved.
A purely soft potential is finite at r=0 and lets ropes pass through one
another (silently changing Lk) -- the hard core prevents that.

## `planarity(C)`

0 for a perfectly planar curve; grows as it leaves a plane.

Ratio of smallest to largest singular value of the centred node cloud.

## `rms_radius(C)`

RMS distance of nodes from their centroid.

## `self_repulsion_force(C, q2=1.0, a=0.14)`

Softened Coulomb self-repulsion within a single curve.

For the linear psi equation the pairwise 1/r kernel IS the field force
(the Green's function), so this is the genuine field force, not only a
proxy, for inter-node interactions.

## `tension_energy(C, T0=1.0)`

E_tension = T0 * total length of closed curve C.

## `tension_force(C, T0=1.0)`

Rope tension force on each node of closed curve C (M,3).

Gradient of E = T0 * sum |segment length|.
