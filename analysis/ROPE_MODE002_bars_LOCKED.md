# ROPE-MODE-002 locked bars — central-field orbital-multiplet gate

## Scope

Test the smallest central-field extension of ROPE-MODE-001 without changing the certified linked geometry: a scalar standing-wave field on each closed component is coupled to a softened attractive center.

This is not a full nonlinear atom or equilibrium calculation. It isolates whether a central interaction alone reorganizes the one-dimensional rope spectrum into robust spatial `s/p/d` multiplets.

## Locked implementation

- Reference geometry: final certified ELEC-009 state.
- Operator: periodic finite-element rope Laplacian plus nodal softened central potential
  `V(r) = -alpha / sqrt(r^2 + eps^2)`.
- Coupling sweep: `alpha = 0, 0.1, 0.3, 1, 3, 10`.
- Softening: `eps = 0.15 × median rope radius`, fixed before the sweep.
- Resolution levels: 128, 256, and 512 samples per component.
- Orbital diagnostic: mass-matrix projection onto sampled real spherical-harmonic subspaces with `l = 0,1,2`.
- No post-hoc fit to hydrogen energies.

## Bars

1. Certified reference: `d_min >= 0.060` and `||Lk|-1| <= 0.03`.
2. Mesh convergence: maximum 256→512 relative eigenvalue change below 1%.
3. Multiplicity: the first nine levels form `1,3,5` clusters on both components for at least one nonzero coupling.
4. Classification: those clusters are respectively dominated by `l=0,1,2`, with at least 80% of the first nine modes having projection purity >= 0.5.
5. Robustness: bars 3–4 hold for three adjacent nonzero couplings.

A positive atomic-multiplet claim requires all five bars.
