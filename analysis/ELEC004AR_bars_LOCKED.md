# ELEC-004A-R — Deterministic stationarity repair (locked)

## Question
Can the saved ELEC-003A K=8 linked/localized state be repaired to a true stationary point of the same sourced Poisson curve-field energy using deterministic finite-difference L-BFGS-B optimization, without leaving its topological basin?

## Protocol
- Start state: `analysis/ELEC003A_states.npz`, key `x_K8`.
- Grid/basis: N=14, K=8, M=24, tube width 0.24, identical to ELEC-004A.
- Optimizer: bounded L-BFGS-B with an explicit central finite-difference gradient.
- Gradient stencil: h=1e-4, independently checked at 5e-5 and 2e-4.
- A short-range strand-separation barrier is permitted only to prevent curve crossing; the reported energy and gradient are those of the physical curve-field functional.

## Locked bars
1. **B1 — Basin retention:** final geometry remains localized (`0.4 < R_rms < 2.0`) and linked (`||Lk|-1| < 0.22`).
2. **B2 — Energy descent:** final physical energy does not exceed the starting energy.
3. **B3 — Stationarity:** `||grad E||/E < 0.02` at h=1e-4.
4. **B4 — Step robustness:** the independently recomputed relative gradient is below 0.03 at all three finite-difference steps.

A failure of B1 is retained as evidence that the current linked candidate is not protected under unconstrained deterministic descent in this coordinate chart.
