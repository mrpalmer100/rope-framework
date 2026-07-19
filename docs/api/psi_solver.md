# `rope_solver.psi.solver`

Poisson solver for the field psi

> psi/solver.py  --  Canonical 3D Poisson solver for the rope psi-field.

## `field_energy(psi, h)`

Field gradient energy  E = (1/2) integral (grad psi)^2 d^3x.

## `grid(N, L_box)`

Return (coords, X, Y, Z, h) for an N^3 cube spanning [-L/2, L/2]^3.

## `hopf_source(N, L_box, R, a_thick)`

Two interlocked rings (Hopf link, Lk=1), radius R each.

Ring 1 in the xy-plane at origin; ring 2 in the xz-plane centred at
(R,0,0) so it threads ring 1.  Normalised to unit total charge.

## `laplacian_3d(N, h)`

Sparse 3D finite-difference Laplacian on an N^3 grid, spacing h.

Returns a (N^3, N^3) CSR matrix.  Dirichlet (psi->0) boundaries are
implicit in the stencil truncation at the grid edge.

## `ring_source(N, L_box, R, a_thick)`

Gaussian-tube source for a circular ring of radius R in the z=0 plane.

Normalised to unit total charge.

## `solve_psi(source, h, L3=None, rtol=1e-08, maxiter=3000)`

Solve nabla^2 (psi-1) = -4 pi source on the grid.

Parameters
----------
source : (N,N,N) array, normalised so sum(source)*h^3 = total charge
h      : grid spacing
L3     : optional pre-built Laplacian (saves rebuild in scans)

Returns
-------
psi : (N,N,N) array  =  1 + perturbation
