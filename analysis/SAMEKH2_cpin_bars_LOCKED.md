# COMMISSION SAMEKH-2 -- EXTRACTING C_pin (BARS, LOCKED)

*Locked 2026-08-11, before computing. The reviewer's protocol, with the
form fixed by ELEC-096 in advance:*

    E_pin(n) = C_pin * s^(-3/2) * [ sum_i n_i^4 - 3/5 ] * E_core

*C_pin is the only unknown. The 3/2 exponent is FIXED INPUT and is NOT
re-derived here -- the reviewer's point, adopted: re-deriving an exponent
alongside a prefactor lets the two compensate.*

## The estimator, fixed before computing

MEM-2 used max-minus-min across three axes. That is a crude estimator
and mixes all harmonics. **This commission PROJECTS instead:** relax at
many orientations, then regress the relaxed energy on the normalized
order-4 cubic harmonic K(n) = sum_i n_i^4 - 3/5. The regression
coefficient IS the anisotropy amplitude at that s, and the residual
measures how much of the signal is NOT order-4 -- which must be reported,
because a large residual means the fixed form is wrong.

## The obstacle, named in advance

MEM-2 found dE/E RISING over s = 1.5-3.0, where the asymptotic law
falls. That range is pre-asymptotic. **Extracting C_pin for an
asymptotic law from pre-asymptotic data would be invalid.** Therefore:

- **S1** Push the engine to the largest s the box allows and look for the
  TURNOVER where the rising behaviour becomes falling.
- **S2** If a turnover is found, extract C_pin from the falling side ONLY,
  and report how many points support it.
- **S3** If NO turnover is reached, the commission may NOT fit C_pin. It
  must report the accessible range as pre-asymptotic and register a
  BOUND or an UNDERSPECIFIED verdict. Fitting an asymptotic coefficient
  to rising data is forbidden by name.

## Numerical requirements

- Noise floor re-measured at the new box size before any signal is read.
- Box adequacy demonstrated: the anchor span and offset grid must be
  large enough that enlarging them does not move the answer at the
  largest s used. Report the check.

## Verdict grammar (pre-committed)

- **C_PIN-MEASURED**: turnover reached, coefficient extracted from the
  asymptotic side. Propagate to s = 82.6/108.0 and confront 1e-6 eV.
  Then classify per the reviewer's three outcomes: C_pin = 0 (needs an
  identity), C_pin small with a derived reason, or C_pin ordinary --
  the last being a real electron-sector failure.
- **PRE-ASYMPTOTIC**: no turnover in reach. Report the range, report any
  bound, do not fit.
- **FORM-WRONG**: the order-4 projection leaves a large residual, i.e.
  the anisotropy is not dominated by the harmonic ELEC-096 derived. That
  would be a finding against ELEC-096 and must be reported as one.

## Standing rule

No adjustable normalization anywhere. If a normalization is needed to
make numbers comparable, it must be a registered quantity or the
relaxation's own measured energy, never a chosen constant.
