# The rope ontology — what each phenomenon *is*

> Conceptual mapping, stated as the framework's claims (motivation, not
> established fact). Each claim that is encoded in code has a module and a
> regression test; see the [README](../README.md) reference-implementation table.

The wager of the rope model is that one physical object — a two-strand rope under
tension — generates phenomena currently explained by a zoo of disconnected
abstractions:

- **Light** is a transverse kink traveling along the rope — a real disturbance
  with a definite location, not a wave packet that collapses.
  *(code: `rope_solver.electromagnetism.photon`)*
- **Gravity** is a tension gradient in the rope network — always attractive
  because tension wells are always positive.
  *(code: `rope_solver.gravity`)*
- **Magnetism** — why magnets pull and push — comes from the rope's helical
  winding, the geometry that makes left- and right-wound ropes mirror images.
- **Electricity** is three distinct mechanical quantities, not one. **Charge** is the
  linking number of the rope curves (an integer topological invariant): it is quantized
  because you cannot link two loops a fractional number of times. **Current** is *transported*
  linking — the rate at which that linking moves along the rope, delivered by the screw
  rotation of the two-strand helix — a flux of the invariant, not the invariant itself.
  **Voltage** is the longitudinal *tension* field that drives the transport. Only charge is
  topological; current and potential are separate mechanical quantities the framework derives
  in their own right (EM-001, EM-008, EM-014, EM-016).
  *(code: `rope_solver.topology`, `rope_solver.electromagnetism`)*
- **Entanglement** is the framework's registered *boundary*, not a solved item: a
  configuration-counting rope model provably cannot reproduce Bell/CHSH violation
  (QB-003 Failed, QB-005 negative). A shared physical rope connection is the intuition
  the picture *reaches for*, but it is not claimed to work — the single-particle
  statistics are mapped (QB-007–010) while the two-particle correlation remains beyond
  a classical counting model. Retired as an ambition, preserved as an honest limit.
- **Chemistry** is standing-wave modes of the rope network around nuclei.
  (By the framework's own admission, mathematically identical to standard quantum
  chemistry — hence *no* chemistry module; see `open_problems` and the README
  scope note.)
- **Particle masses, generations, and forces** arise from how the rope is knotted
  and linked with itself. *(partially encoded: `rope_solver.particles`; the
  absolute mass scale is UNSOLVED — see `open_problems`)*

## Axioms

- **A1**: space is 3-dimensional (d = 3).
- **A2**: the rope has two strands (N = 2).

Almost everything else is claimed to follow from these two plus the single
coupling α = 1/137.036. Where a claim is established, it is in code with a test;
where it is not, it is in the `open_problems` registry.
