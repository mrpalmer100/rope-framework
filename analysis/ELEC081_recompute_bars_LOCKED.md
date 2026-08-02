# ELEC-081 — Independent recomputation of the flux-tube radius: locked bars

## Commission
QGATE-018 established that no vacuum experiment in reach can decide Sigma, and
that the two candidates differ because one is an internal consistency argument
and the other a COMPUTATION on published lattice data (ELEC-052). The route to
Sigma is therefore a better calculation. This is the independent redo.

## What makes it independent, fixed before computing
ELEC-052 integrated the DISCRETE DATA POINTS by trapezoid, with an SNR-based
truncation. This session instead FITS the paper's own functional form to the
data and integrates the FIT ANALYTICALLY. That is a different estimator with
different failure modes: a fit is insensitive to point-to-point noise and to
truncation choice, but is exposed to profile-model error, which trapezoid is not.
Agreement between the two would be meaningful; disagreement would be too.

## Locked bars
B1 Fit the two-component sech^2 form (the paper's own) to each lattice setup at
   the verdict-bearing distance d = 0.7 fm, integrate analytically for the
   E^2-weighted radius, and report the median.
B2 THE COMPARISON with ELEC-052's 0.407 fm. Report the deviation. Under 5%
   counts as confirmation; 5-15% as tension; over 15% as a failure to reproduce.
B3 PROFILE-MODEL DEPENDENCE, which is this estimator's own weakness and must
   therefore be tested rather than assumed small: repeat with a SINGLE sech^2
   and with a PURE EXPONENTIAL, and report the spread across models.
B4 A BOOTSTRAP over the quoted point errors, for a statistical error that
   ELEC-052 did not have.
B5 THE VERDICT for Sigma: restate the propagated value and say whether the
   28% tension with the framework's 5.1e35 survives independent computation.
