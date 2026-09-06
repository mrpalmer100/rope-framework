# COMMISSION METALLIC (ITEM 6c) -- RESULTS (2026-09-05)
Charter analysis/ITEM6_charters_LOCKED.md section 6c (locked before any
channel was computed). Logs analysis/metallic/. Targets loaded once in the
consequence leg.

## VERDICT: ** MET-DISCRIM-FAIL ** (channel M-a refused; kept as a caution)
with the decomposition vector reported whole.

## v1 -- registered reproduction
Na E_model 0.364 / Li 0.564 eV per atom (registered 0.36 / 0.56); halogen
D_band 1.32 -> D_net 0.84 < 1 (discrimination held); non-saturation held
(sqrt(z) band law). v2: the R4 star form reproduces NUC-029's -1/2
(samekh_coh_realization.py re-run: n-vol -1/2 EXACTLY). v3: the cohesive
energies appear in no channel file (channels.log carries only model
energies).

## The decomposition (per channel, per element; F = E_measured / E_model)
                     Li      Na      Cl2 (D_net; < 1 = insulator)
  registered        2.89    3.05      0.84
  M-a  R4 star      1.44    1.53      2.15   <- DISCRIMINATION BROKEN
  M-b  p-lobes      2.89    3.05      0.28   (alkali s band untouched)
  M-a + M-b         1.44    1.53      1.04   (still marginal/metallic)
  M-c  spacing      (baseline; already in E_model)
  M-d  dimer anchor DISPLAY: the residual after M-a, x1.44-1.53, is the
                    size of the t = De/2 understatement (electronic gain
                    = De + core repulsion at d_dim); the sector's
                    Consistency-tier ceiling, not a channel.

## Reading
M-a is the one channel with a dependency path from another sector (the
R4 star coupling, NUC-029's -1/2 realization). Transplanted at the
registered per-state coupling t x persist and the bcc z = 8 (D3), it
DOUBLES the alkali cohesion -- because the star's extremal gain sqrt(z)
t is twice the half-filled band's MEAN gain (sqrt(z)/2) t that the
registered model uses. That halves the shortfall on both elements
consistently (F 1.44 / 1.53, still outside 25 pct) -- but the same
transplant applied to the halogen, as D1 requires, lifts Cl2's D_net
from 0.84 to 2.15: Cl2 becomes a metal. M-b (the p-lobe directional
factor, cos^2 = 1/3 on the bcc shell) pushes the halogen the other way
(0.28) but does not touch the alkali s band, and the two together leave
Cl2 at D_net 1.04, marginal. Under the charter's D1 the channel that
partially closes the number by making the wrong thing a metal is
REFUSED. The 2.8x is therefore NOT explained by coherent sharing alone,
and the discrimination bar is the reason: any channel that scales the
alkali gain scales the halogen's too unless it is s-selective, and the
registered inventory holds no s-selective channel.

## What is named
- The shortfall's likely seat, from the residual's shape: the dimer
  anchor t = De/2 (M-d), element-consistent (x1.44 vs x1.53) as an
  understatement would be. A registered core-repulsion object at d_dim
  would make it a channel; none exists (zero new constants).
- Next-order: an s-selective coherent channel (why the alkali's single
  diffuse s kink would take the star gain while the halogen's five p
  kinks take the band mean) -- a statement about MODE MULTIPLICITY, not
  a coefficient; if derivable it re-opens M-a without breaking
  discrimination.
- CHEM-MET-001 stands as registered ("declared shortfall, causes
  declared"); this decomposition is added to its face.
