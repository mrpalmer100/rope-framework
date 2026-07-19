# `rope_solver.topology.linking`

Linking number and link constructions

> topology/linking.py  --  Canonical linking-number and curve topology tools.

## `hopf_curves(M, R=1.0, sep=None)`

Two interlocked circles forming a Hopf link (Lk=1), as node arrays.

## `linking_number(A, B)`

Discrete Gauss linking integral between two closed curves A, B.

A, B : (M,3) and (K,3) arrays of node positions (closed: last connects
to first).  Returns a float that should be close to an integer for a
well-resolved link.

## `torus_link(M, n, R=2.5, r=0.9)`

Construct a (2,2n) torus link: two components with linking number n.

Returns (C1, C2), each an (M,3) array.  The constructed linking number
should verify as approximately n via linking_number(C1, C2).

## `writhe(C)`

Self-writhe of a single closed curve C (M,3) via the Gauss double sum.

Diagonal (i==j) and adjacent terms are skipped to avoid the self-singularity.
