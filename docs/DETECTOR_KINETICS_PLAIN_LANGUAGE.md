# What Small Isolated Detectors Do, and Why: A Plain-Language Account

*Companion to the strand-kinetics campaign, FND-STRAND-009 through 021
(releases v3.7.0 and the following cut). Written for a reader outside the
project. Every claim referenced here has a registered entry in
`claims.yaml`, an executable benchmark, and pre-committed pass criteria in
`analysis/`.*

---

## Three questions this framework can now answer

Before the detail, here are the three results in their simplest form.
Everything below unpacks them; every sentence traces to a registered,
benchmarked claim.

**1. How does a single-photon detector actually work?**
A click is a real mechanical event: a tiny knot forming on a strand when
enough energy gathers at one spot. The detector is a threshold device,
like a mousetrap. The surrounding medium (the weave) is a warm bath that
constantly jiggles the strand, and the rate of clicks follows the classic
escape-over-a-barrier law. The remarkable part: the "attempt rate" in
that law is not a fitted number. It is the bath's own minimum vibration
frequency, the strand mass scale. The medium itself is the detector's
metronome, and this held up under two independent statistical methods
with opposite failure modes.

**2. Why does a small detector seem to have memory, when nothing in it
remembers anything?**
Freshly reset small detectors click fast at first and then settle down,
which looks like aging or memory. We hunted for the memory with
purpose-built instruments and found nothing changing: temperature flat,
forces flat, no starting condition predicting anything. The answer came
from changing one line: start the detector in true equilibrium with its
bath instead of switched on cold, and the effect vanishes completely.
The "memory" was a switch-on transient, the brief extra jostling any
system feels while it and its bath get acquainted. Nothing inside ever
remembers; the appearance of memory is the echo of the power-up. And
detector size hides the effect by pure arithmetic: a large detector is
many independent click sites racing each other, the first click always
comes early, and early clicks only ever sample the settled behavior. We
proved the exact law: the large detector's statistics are the small
one's raised to the size ratio, with zero adjustable constants.

**3. How can single photons, fired one at a time over hours, build up an
interference pattern, as if each one interferes with itself?**
Because nothing pointlike ever travels. Each emission is a wave that
goes through both slits every single time and lays the full striped
energy pattern on the screen. The dot is not the photon arriving; the
dot is the detector firing, a threshold event that is pointlike because
that is what tripping a threshold is, like one ping of rain on a tin
roof. The odds of the dot landing at any spot are proportional to the
wave energy delivered there, so each photon's single dot is a sample
drawn from the same standing striped pattern. Fire ten thousand photons
over ten hours and the dots trace the stripes, because every dot was
drawn from the same map. Nothing needs to remember anything between
shots, and no photon ever "chooses a slit," because no photon ever
travels as a particle. The wave delivers the odds; the bath delivers
the dot.

One honest sentence to complete the picture: this account is
established for the plain double-slit, and the framework states exactly
where it ends. Splitting one photon's energy between two separated
detectors is beyond the classical machinery (the funneling step,
described near the end of this document), and that boundary is measured
and registered, not glossed.

---

## The question in one sentence

When a detector clicks in the dark, with no signal present, what sets the
timing of those false clicks, and does the pattern carry any fingerprint
of the physics underneath?

In this framework a detector click is a physical event: a small knot
nucleates on a strand when enough energy gathers in one place. The
"darkness" around the detector is not empty. It is the weave, a background
of strand vibrations that acts as a heat bath. So the dark-count question
becomes a concrete mechanical one: how does a warm weave kick a strand
over its threshold, and how often?

## The short answer

A detector's dark-count behavior has exactly two regimes, and we can now
state both from first principles, with every constant accounted for.

**Steady state.** Leave any detector running, large or small, and its
clicks are textbook random: a steady Poisson stream, the same odds at
every moment. The rate follows the classic escape-over-a-barrier law, and
the "attempt frequency" in that law is not a fitted number. It is the
weave's own minimum vibration frequency, the band gap, which is the strand
mass scale. The metronome of the detector is the medium itself. This
identification survived two independent statistical methods with opposite
failure modes, which is about as hard a test as a simulation result can be
given.

**Just after switch-on.** Power up, reset, or suddenly isolate a small
detector, and for a limited time its clicks are NOT steady. The click rate
starts elevated and relaxes downward to the steady value over one
characteristic epoch, the time it takes the detector and its bath to
become properly acquainted. During this window the waiting times between
clicks are measurably non-exponential. After the window closes, the
detector is ordinary forever.

**And size matters in a precise way.** The switch-on fingerprint is
strongest in the smallest detectors and vanishes in large ones. Not
because large detectors settle faster. They do not; the settling time is a
property of the medium and is the same at every size. Large detectors hide
the fingerprint by arithmetic: a big detector is many independent
nucleation sites racing each other, the first click always arrives early,
and early clicks sample only the flat beginning of each site's curve. We
proved the exact law for this. Take the measured survival curve of the
small reference detector and raise it to a power equal to the size ratio.
That is the whole formula. Nothing in it is fitted; the one quantity you
would expect to tune, the number of independent sites, cancels out of the
algebra. The formula predicted three independently measured sizes inside
their error bars with zero adjustable constants, and it now carries the
corpus's Derived status, the highest tier.

## How we got it wrong before we got it right

The honest history matters, because the wrong turns are load-bearing.

For seven sessions the falling click rate looked like a mystery. It
behaved like memory, so we hunted for the memory with purpose-built
instruments, each with its pass and fail conditions locked before the data
existed. A thermometer on the bath: temperature flat to five parts in ten
thousand. A meter on the force the bath delivers: flat to six parts in ten
thousand. A census of 256 starting configurations: no measurable property
of the start predicted a detector's fate. A complete deterministic theory
of the effect: dead at its own first checkpoint, kept on display in the
registry as required. At that point the phenomenon had been replicated
three times on independent data and was invisible to every natural
variable.

The resolution came in two steps. First, the size study and the
power-law derivation showed the per-site memory is real, permanent, and
intensive, and that large systems simply never look at it. Second, and
decisively, one final experiment changed a single line: instead of
starting each simulation with the strand perfectly cold and uncorrelated
with its bath (the "product state," which is what the code had always
done), we prepared the true joint equilibrium of strand and bath together.
The falling rate vanished completely. Flat clicks, exponential waiting
times, at exactly the rate the old ensembles had always been decaying
toward.

The mystery had been hiding in the first line of every script. The strand
started at zero. Physics calls the consequence "initial slip": a system
switched on uncorrelated with its bath feels a brief excess of effective
noise while correlations build, even though every stationary quantity
(temperature, force intensity) reads constant the whole time. Our
instruments were not wrong. They were measuring exactly the things that
do not change. The transient lives in the correlations those instruments
integrate out.

So the earlier confusion was necessary. Each flat instrument was an
exclusion that pinned the effect into the one corner where it actually
lives, and the dead theory exposed the internal mixing of the bath that is
precisely the mechanism by which the slip relaxes.

## What an experimentalist could do with this

Prediction 11 of the framework now reads as a two-part statement that a
lab could in principle test on small single-photon detectors or similar
threshold devices:

1. **The quench fingerprint.** After a reset or power-up, a sufficiently
   small, well-isolated detector should show dark counts whose waiting
   times are non-exponential for one bath-correlation epoch, with the
   apparent rate drifting down while the device's measured temperature
   holds constant. A rate drift at constant temperature is the
   distinctive part; ordinary thermal-drift explanations cannot produce
   it.
2. **The size law.** Compare detectors of different sizes prepared the
   same way. The deviation from Poisson should shrink with size following
   the exact power law: the large detector's survival curve is the small
   one's raised to the size ratio. No fitting allowed; the curve for the
   small device fully determines the prediction for the large one.

And the boring regime is a prediction too: in steady operation, every
size should be clean Poisson, with an attempt-rate prefactor set by one
structural scale of the medium, the same scale that sets the decoherence
floor in Prediction 10. Two independent instrument-facing predictions
pinned to a single number is the kind of rigidity that makes a framework
falsifiable rather than flexible.

## The scale caveat, stated plainly

All of this is a statement about the model's own units. The framework does
not yet fix the absolute physical scale of the strand mass, so these are
predictions about the SHAPE and the RELATIONSHIPS of detector statistics
(two regimes, a size power law, drift at constant temperature, one shared
prefactor scale), not yet about a frequency in hertz. The shape claims are
falsifiable now; the absolute calibration is registered as open.

## The sequel: one click, and the edge of the story

After the two-regime picture was settled, we chased the last loose thread:
why does one photon's worth of energy produce exactly one click, never
two? Three sessions later the answer arrived, and it came in two parts.

**Part one: the click is a cliff.** When we finally modeled the photon
correctly, as a concentrated packet rather than a faint glow spread over
the whole screen (two earlier designs failed for exactly that reason, and
the failures are kept on the books), the detector's response turned out
to be a sharp threshold: a full packet clicks about half the time, and a
packet with HALF the energy clicks never. Not rarely. Never, in every
trial. That settles the one-click question almost embarrassingly simply:
split one photon's energy between two places and neither place can click,
so a double click was never possible. No hidden bookkeeping needed. The
staircase is so steep that half a step is the same as no step.

**Part two: the honest edge.** But that simplicity exposes something the
framework must own. In real laboratories, a single photon sent through a
beamsplitter DOES click, on exactly one side, about half the time each.
Our classical machinery, asked the same question, says neither side
clicks. So the framework's detector story, for all its success, cannot
yet do the one thing every beamsplitter experiment shows: gather a split
photon's full energy back into one spot. We call that missing move the
funneling step, and rather than paper over it, it is registered as a
measured boundary, with the experiments that live beyond it (which-path
tests, delayed choice, the quantum eraser) explicitly marked as not yet
in reach. The leading idea for crossing the boundary is a single minimal
assumption, that a quantum's energy is always delivered whole or not at
all, which together with the framework's existing probability rule would
reproduce the laboratory statistics. Whether to adopt that assumption is
a decision recorded as pending, not smuggled in.

A theory that can say "here is exactly where my story ends, and here is
the measurement that proves it" is doing something most theories never
manage. The edge is not a defeat. It is a surveyed border, and surveyed
borders are where the next expedition starts.

## Where to look in the corpus

- The campaign: claims FND-STRAND-009 through FND-STRAND-021 in
  `claims.yaml`, each with its benchmark under
  `benchmarks/foundations/`.
- The cornerstone law (Derived): FND-STRAND-020,
  `benchmarks/foundations/strand_poissonization.py`.
- The switch-on resolution: FND-STRAND-021,
  `benchmarks/foundations/strand_switch_on.py`.
- Pre-committed pass criteria for every session:
  `analysis/STRAND0xx_*_bars_LOCKED.md`.
- The kills and the buried theory, kept on display: FND-STRAND-015, 016,
  and 017.
- The exclusivity arc and the surveyed edge: FND-STRAND-022, 023, and
  024, with the limit statement now in `papers/falsifiable_predictions.pdf`
  ("A Registered Limit — The Funneling Step").

Every number quoted above can be recomputed from the archived datasets by
running the corresponding benchmark.
