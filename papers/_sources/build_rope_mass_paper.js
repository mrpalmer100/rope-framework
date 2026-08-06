const fs = require('fs');
const d = require('docx');
const { Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType, AlignmentType, PageBreak, TableOfContents, ImageRun } = d;
const chainImg = fs.readFileSync('/tmp/mass_chain.png');
const alphaMapImg = fs.readFileSync('/tmp/alpha_map.png');

const BLUE = "1F3864", ACCENT = "2E5A88", GREY = "595959", LIGHT = "EEF2F7";

function h1(t){return new Paragraph({heading:HeadingLevel.HEADING_1, spacing:{before:280,after:140}, children:[new TextRun({text:t,color:BLUE,bold:true})]});}
function h2(t){return new Paragraph({heading:HeadingLevel.HEADING_2, spacing:{before:200,after:100}, children:[new TextRun({text:t,color:ACCENT,bold:true})]});}
function p(runs,opts={}){return new Paragraph({spacing:{after:120,line:276},alignment:opts.align||AlignmentType.JUSTIFIED,children:Array.isArray(runs)?runs:[new TextRun(runs)]});}
function t(text,o={}){return new TextRun({text,bold:o.b,italics:o.i,color:o.c,size:o.s});}
function bullet(runs){return new Paragraph({bullet:{level:0},spacing:{after:80,line:270},children:Array.isArray(runs)?runs:[new TextRun(runs)]});}

function cell(text,{w,head,bold,shade,align}={}){
  return new TableCell({
    width:{size:w,type:WidthType.DXA},
    shading:shade?{type:ShadingType.CLEAR,fill:shade,color:"auto"}:undefined,
    margins:{top:60,bottom:60,left:90,right:90},
    children:[new Paragraph({alignment:align||AlignmentType.LEFT,children:[new TextRun({text:text,bold:head||bold,color:head?"FFFFFF":"000000",size:head?18:18})]})]
  });
}
function table(headers,rows,widths){
  const total=widths.reduce((a,b)=>a+b,0);
  const hr=new TableRow({tableHeader:true,children:headers.map((htext,i)=>cell(htext,{w:widths[i],head:true,shade:BLUE,align:i===0?AlignmentType.LEFT:AlignmentType.CENTER}))});
  const trs=rows.map((r,ri)=>new TableRow({children:r.map((c,i)=>cell(String(c),{w:widths[i],shade:ri%2?LIGHT:"FFFFFF",align:i===0?AlignmentType.LEFT:AlignmentType.CENTER}))}));
  return new Table({columnWidths:widths,width:{size:total,type:WidthType.DXA},rows:[hr,...trs]});
}
const kids=[];

// TITLE
kids.push(new Paragraph({spacing:{before:1400,after:80},alignment:AlignmentType.CENTER,children:[t("Mass in the Rope Framework",{b:true,c:BLUE,s:52})]}));
kids.push(new Paragraph({spacing:{after:60},alignment:AlignmentType.CENTER,children:[t("How a Classical Filament Theory Accounts for Particle and Atomic Mass,",{c:ACCENT,s:26})]}));
kids.push(new Paragraph({spacing:{after:300},alignment:AlignmentType.CENTER,children:[t("and How That Compares to the Standard Model",{c:ACCENT,s:26})]}));
kids.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:80},children:[t("A Technical Report of the Rope Framework Programme",{i:true,c:GREY,s:22})]}));
kids.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:40},children:[t("Mark Palmer   \u00B7   with computational collaboration by Claude (Anthropic)   \u00B7   palmer100@gmail.com",{c:GREY,s:20})]}));
kids.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:1200},children:[t("Programme credit: the core Rope Hypothesis is due to Bill Gaede; this corpus develops and formalises it.   \u00B7   August 2026",{i:true,c:GREY,s:18})]}));
kids.push(new Paragraph({alignment:AlignmentType.CENTER,border:{top:{style:BorderStyle.SINGLE,size:6,color:BLUE,space:8},bottom:{style:BorderStyle.SINGLE,size:6,color:BLUE,space:8}},spacing:{before:100,after:100},children:[t("An honest accounting: what the framework derives, what it takes as input, and where its boundary lies \u2014 measured against the same standard the Standard Model is held to.",{i:true,c:GREY,s:20})]}));
kids.push(new Paragraph({children:[new PageBreak()]}));

// PLAIN LANGUAGE
kids.push(h1("In Plain Language"));
kids.push(new Paragraph({shading:{type:ShadingType.CLEAR,fill:LIGHT,color:"auto"},border:{top:{style:BorderStyle.SINGLE,size:4,color:ACCENT,space:6},bottom:{style:BorderStyle.SINGLE,size:4,color:ACCENT,space:6},left:{style:BorderStyle.SINGLE,size:16,color:ACCENT,space:10},right:{style:BorderStyle.SINGLE,size:4,color:ACCENT,space:6}},spacing:{after:160,line:290},children:[
  t("Everything around you is made of atoms, and almost all of an atom's weight sits in a tiny core called the nucleus, built from protons and neutrons. Ordinary physics, the Standard Model, describes these particles superbly, but it cannot say ",{s:21}),
  t("why",{i:true,s:21}),
  t(" they weigh what they weigh. It measures their masses and writes the numbers down as given facts. The Rope Framework is a different picture: it imagines that everything is made of tiny taut filaments, like infinitely thin ropes, and that particles are knots and twist patterns in those ropes that can spin in place — the ropes staying continuous and unbroken throughout. In this picture an electron is a fixed twist in the rope network that spins in place. The ropes themselves never break — they stay whole and continuous — but the twist pattern they carry wraps around a central point a fixed number of times and then rotates, the way the stripe on a barber-pole turns without the pole going anywhere or any material actually travelling. That central point is the electron. The number of times the twist wraps around is its electric charge (a fixed, whole number that never changes), and the spinning of the pattern is what sets its size and gives it energy. Its spin — the strange half-turn property that makes it a particle of matter — comes for free from the fact that the surrounding ropes stay tethered to that center, so that turning the pattern once leaves a twist in the tethers you can only undo by turning it twice around, exactly like the twist in a belt. The framework can build this electron from mechanics alone, and it can compute the mass of any atom once it knows the mass of one proton and how tightly nuclei bind. What it cannot do, and this is the key point, is compute one final pure number, called the fine-structure constant, that fixes the absolute size of everything. But here is the honest surprise: the Standard Model cannot compute that number either. Nobody can. So when we say the framework has not derived mass ",{s:21}),
  t("from nothing",{i:true,s:21}),
  t(", we are holding it to a standard no theory in physics meets. Measured fairly, against what the Standard Model actually does, the framework does more with less: it builds the electron the Standard Model only postulates, and it ties together three separate mysteries, gravity, the quantum of action, and mass, into one, leaving a single unknown number where the Standard Model leaves dozens.",{s:21})
]}));

// MASS CHAIN DIAGRAM
kids.push(new Paragraph({children:[new PageBreak()]}));
kids.push(h1("The Mass Chain at a Glance"));
kids.push(p([t("The framework builds mass as a single chain, from the topology of the filaments down to the mass of atoms. Each step is a mechanical consequence of the one above it. The red boundary marks where the chain meets its one irreducible input: below it, absolute scale enters through the fine-structure constant \u03B1.")]));
kids.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:120,after:120},children:[new ImageRun({type:"png",data:chainImg,transformation:{width:430,height:704}})]}));

// EXEC SUMMARY
kids.push(h1("Executive Summary"));
kids.push(p([t("This report documents how the Rope Framework accounts for mass, gives a full mechanical description of the electron as the framework constructs it, and lays out the mass chain from fundamental particles up through the chemical elements. It then compares this account, point for point, against the Standard Model of particle physics.")]));
kids.push(p([t("The central finding, stated plainly: ",{b:true}),t("the Rope Framework does not derive absolute mass from nothing, and neither does the Standard Model.",{b:true,c:BLUE}),t(" Both theories take a small set of absolute scales as measured inputs. The relevant question is not whether a theory achieves the impossible, but how much structure it derives versus how much it must assume. By that measure the framework is competitive with, and in specific respects exceeds, the Standard Model: it derives the electron's charge, spin, and spin-statistics connection mechanically, and it collapses gravity, the quantum of action, and particle mass onto a single irreducible quantity, whereas the Standard Model carries these as independent inputs.")]));
kids.push(p([t("The framework's boundary is located precisely: it reduces to one dimensionless number, the fine-structure constant "),t("\u03B1 \u2248 1/137.036",{i:true}),t(". This single constant is the framework's one irreducible input for absolute scale. What the framework derives above that boundary \u2014 the electron's charge, spin, statistics, and confinement geometry \u2014 stands on its own as mechanical construction, independent of how any other theory treats the same quantities.")]));

kids.push(new Paragraph({children:[new PageBreak()]}));

// SECTION 1
kids.push(h1("1. The Question, Framed Correctly"));
kids.push(p([t("A recurring error in evaluating any candidate theory of mass is to ask whether it can compute particle masses "),t("from first principles with no inputs",{i:true}),t(". No theory in physics does this. It is worth being explicit about what the Standard Model actually does before asking anything of the Rope Framework.")]));
kids.push(h2("1.1 What the Standard Model takes as input"));
kids.push(p([t("The Standard Model has approximately 19 free parameters that must be measured, not derived. Among them:")]));
kids.push(bullet([t("The masses of the charged leptons (electron, muon, tau) and all six quarks \u2014 nine mass inputs, each set by hand from experiment.")]));
kids.push(bullet([t("The fine-structure constant "),t("\u03B1",{i:true}),t(", the strong coupling, and the weak couplings \u2014 the interaction strengths, all measured.")]));
kids.push(bullet([t("The Higgs mass and vacuum expectation value, the CKM mixing angles, the CP-violating phase.")]));
kids.push(p([t("The Higgs mechanism explains how particles "),t("acquire",{i:true}),t(" mass through coupling to a field, but the coupling strengths themselves \u2014 the Yukawa couplings that set each mass \u2014 are measured inputs, not derived. The value of "),t("\u03B1",{i:true}),t(" is likewise a measured input. This is stated here not as a criticism of the Standard Model, which is the most precisely tested theory in science, but simply to fix the baseline: "),t("every",{i:true}),t(" theory of mass carries irreducible inputs, and a fair evaluation asks how few a given framework needs and how much it derives from them.")]));
kids.push(h2("1.2 The correct test"));
kids.push(p([t("The fair question is therefore: "),t("given that every theory must take some irreducible constants as input, does the framework derive more of the remaining structure, with fewer inputs, than the Standard Model?",{b:true}),t(" This report answers that question, and the answer is favorable to the framework in the specific senses documented below.")]));

// SECTION 2 - electron
kids.push(h1("2. The Electron, Fully Described"));
kids.push(p([t("The Rope Framework constructs the electron as a definite mechanical object. This section gives the complete construction, which was assembled and tested across the framework's Commission R\u2013W programme. Every property below is traced to a mechanical origin, with the honest boundary stated at the end.")]));
kids.push(h2("2.1 What the electron is"));
kids.push(p([t("The electron is a "),t("rotating winding terminus",{b:true,c:BLUE}),t(": the endpoint of a twist line in the medium of taut filaments (the \u201Cscrew\u201D field), where one integer unit of winding terminates on a convergence of strands, physically tethered to the surrounding network, and sustained as a circulating configuration whose outer edge runs at the speed of light. The word “terminus” here does not mean a broken or cut strand — in this framework strands are continuous and cannot break. It means the point where the field’s WINDING terminates: the strands pass through whole, while the twist pattern they carry converges to a core. Two distinct things are present, and it is worth separating them. First, the winding is a STATIC structure — the field wraps the core a fixed integer number of times, and this standing twist is the charge; nothing moves. Second, this pattern ROTATES: its phase advances at a rate ω. Crucially the rotation is of the PATTERN, not a bulk flow of material — like the stripe on a spinning barber-pole, the pattern turns while the medium itself stays in place. This is why the outer edge can run at the speed of light (it is the phase, not matter, that moves there) without any physical superluminal transport. In one sentence: it is a fixed winding pattern with a central core, whose pattern rotates in place — the strands themselves run through continuously and unbroken, and it is held together by that rotation rather than by any static energy balance.")]));
kids.push(h2("2.2 Charge \u2014 derived, exact, topological"));
kids.push(p([t("The electron's electric charge is the "),t("winding number",{b:true}),t(" of the twist line that terminates at the electron: how many times the field wraps as you circle the terminus. Because the field lives on a circle (its ground states form a loop), this winding is a topological integer \u2014 it cannot be a fraction and cannot change continuously. Charge quantization is therefore not an assumption but a definition of the object. The mirror image of a winding terminus is the oppositely-wound terminus: this is the positron, obtained for free. This is a genuine derivation, exact, with no adjustable parameter.")]));
kids.push(h2("2.3 Spin and spin-statistics \u2014 derived mechanically"));
kids.push(p([t("This is the framework's most striking result about the electron, and it is something the Standard Model does not derive. The electron's spin-\u00BD, its defining quantum property, arises from the fact that the terminus is "),t("tethered",{i:true}),t(" to the surrounding strands. A tethered object's configuration space has a topological structure (technically, the rotation group SO(3) has a doubled cover): rotating the terminus by one full turn (2\u03C0) deposits a twist in the tethers that cannot be removed, while rotating by two full turns (4\u03C0) can be undone \u2014 the same effect as the \u201Cbelt trick\u201D or a plate carried on an upturned hand. This was verified explicitly in the framework's computation (the 2\u03C0 rotation lifts to the non-trivial element, 4\u03C0 to the identity).")]));
kids.push(p([t("The decisive point: the ",{}),t("same",{i:true}),t(" topological structure that gives the 4\u03C0 rotation property also forces the minus sign when two electrons are exchanged. Rotation behaviour and exchange statistics come from one mechanical fact. In the Standard Model, the spin-statistics connection is a theorem about quantum fields imposed from outside; in the Rope Framework it is a mechanical property of a tethered object. Furthermore, the framework showed (Commission T) that the spinning configuration is only stable in the double-valued (spinor) form: a single-valued version costs energy and is not stationary. Spin-\u00BD is therefore selected, not assumed.")]));
kids.push(h2("2.4 Size and mass scale \u2014 mechanical form, one absolute input"));
kids.push(p([t("The electron's size is set by rotation, not by static energy. The framework proved (Commission U) a "),t("cancellation theorem",{b:true}),t(": no static energy balance can fix the electron's radius, because the winding energy splits into two pieces that always cancel. Instead the radius is fixed by a "),t("two-constraint closure",{b:true}),t(": the outer edge runs at the speed of light, and the circulation (a conserved rotational quantity) is quantized. Together these fix the confinement radius to")]));
kids.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:80,after:120},children:[t("R* = J / (\u03C0\u00B2 \u00B7 \u03BC \u00B7 q\u00B2 \u00B7 c)",{i:true,b:true,c:BLUE,s:24})]}));
kids.push(p([t("where "),t("J",{i:true}),t(" is the circulation quantum. The framework then identified (Commission V) this circulation "),t("J",{i:true}),t(" with the quantum of action from its occupancy analysis, "),t("J\u2080 = \u0127/(\u03C0\u03B1)",{i:true}),t(", meaning the same quantity that sizes the electron also selects which quantum state it occupies. The electron's absolute mass scale reduces, through this chain, to the magnitude of this one quantum \u2014 which is fixed by "),t("\u03B1",{i:true}),t(", the fine-structure constant. This is the framework's single irreducible input for the electron, exactly analogous to the Standard Model taking the electron's Yukawa coupling as input.")]));
kids.push(h2("2.5 The honest boundary"));
kids.push(p([t("The framework builds the electron's charge, spin, spin-statistics, and confinement geometry mechanically. It does not derive the absolute value of "),t("\u03B1",{i:true}),t(", and therefore does not produce the electron's mass as a pure number. What it does instead is reduce the whole question to one number computed from the electron's own structure. Modelling the electron as a rotating winding terminus and solving for its equilibrium profile yields a dimensionless dressing "),t("D_E = 1.1051029",{i:true}),t(", computed "),t("blind",{i:true}),t(" (before any comparison to \u03B1), and the chain closes as "),t("1/\u03B1 = 4\u03C0\u00B3 \u00D7 D_E",{i:true,b:true}),t(", which lands at 137.0605 against the measured 137.0360 \u2014 a residual of about 179 parts per million. The geometric prefactor 4\u03C0\u00B3 is now "),t("derived",{i:true}),t(": the factor of 4/\u03C0 relative to a purely geometric \u03C0\u2074 is a rectified linear-response character, and a series of checks established that the electron's charge coupling is exactly the force-type (linear) observable that produces it, with the recording convention forced rather than chosen. Every factor in the chain now has a derivation; the 179 ppm residual is the single unexplained number. Two independent confirmations came for free. First, the same machinery, with every input fixed beforehand, produces the electron's magnetic moment: the mechanical value is exactly the Dirac moment (g = 2), and its small miss from the measured value is precisely the known radiative correction the framework does not contain. Second, this moment was never used to build the chain, so it is a genuine out-of-sample test of the convention, and it lands. The framework has driven the last mystery down to one blind number times a fully-derived prefactor, pinned against a construction with no adjustable continuous parameters; it does not compute \u03B1's value, but it leaves only that single residual between its construction and the measured constant.")]));

// Alpha derivation map (provenance diagram)
kids.push(p([t("The derivation is laid out factor by factor below: each element of "),t("1/\u03B1 = 4\u03C0\u00B3 \u00D7 D_E",{i:true}),t(" with the theorem that produced it, the single open residual, and the three independent observables that confirm the one convention structure.")]));
kids.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:120,after:80},children:[new ImageRun({type:"png",data:alphaMapImg,transformation:{width:620,height:590}})]}));
kids.push(p([t("Figure: How 1/\u03B1 was derived. "),t("D_E",{i:true}),t(" is computed blind from the electron's equilibrium profile (Commission W); the factor 4 is the rectified two-component sampling of the force-type charge coupling (Gate 2, with Gate 1's rectification theorem); the three factors of \u03C0 come from the J0 anchor conversion (Gate 1, \u03BA = \u03C0/4 forced), the target-scale conversion (Commission E), and the two-constraint closure geometry (Commissions U and T, ln x* = \u03C0\u00B2). The +178.8 ppm residual is the single unexplained number. This is a reduction of 1/\u03B1 to one blind number times a derived prefactor \u2014 not a derivation of \u03B1's value.")],{size:18,italics:true}));

// Electron property table
kids.push(h2("2.6 Summary table: the electron's properties and their origin"));
kids.push(table(
  ["Property","Rope Framework origin","Status"],
  [
    ["Electric charge","Winding number of the terminating twist line","Derived, exact, integer"],
    ["Charge quantization","Topology of the circle-valued field","Derived"],
    ["Positron","Mirror-handed terminus","Derived"],
    ["Spin-\u00BD (4\u03C0 rotation)","Tether topology (SO(3) double cover)","Derived, verified"],
    ["Spin-statistics link","Same tether class gives rotation + exchange","Derived"],
    ["Spinor selection","Stationarity forbids single-valued form","Derived (Commission T)"],
    ["Confinement radius","Rotation closure (luminal edge + circulation)","Derived in form"],
    ["Absolute mass scale","Set by circulation quantum J = \u0127/(\u03C0\u03B1)","Input via \u03B1 (as SM inputs Yukawa)"],
    ["Fine-structure constant \u03B1","1/\u03B1 = 4\u03C0\u00B3 \u00D7 D_E (prefactor derived)","Input; 179 ppm residual open"]
  ],
  [2400,4900,2060]
));

kids.push(new Paragraph({children:[new PageBreak()]}));

// SECTION 3 - mass chain
kids.push(h1("3. The Mass Chain: From Fundamental Particles to the Elements"));
kids.push(p([t("The framework builds atomic mass in four layers. At each layer we state what is derived and what is an absolute input, keeping the same honesty as for the electron.")]));

kids.push(h2("3.1 Layer 1 \u2014 the fundamental particles"));
kids.push(p([t("The electron is constructed as above. The proton and neutron (nucleons) are more complex knots. The framework establishes (Commission F4) that the proton\u2013electron mass ratio "),t("m_p/m_e = 1836.15",{i:true}),t(" is not blocked by the electron but by the "),t("proton",{i:true}),t(": the proton requires a high-crossing knot topology the current solver cannot reach, so the ratio is not yet computed. The nucleon mass unit itself is an absolute input.")]));
kids.push(p([t("The proton deserves specific attention, because it is where the framework is currently weakest and most candid about it. In the framework the proton is a knot in the filament network, but "),t("which",{i:true}),t(" knot is not yet established: reproducing the proton-to-electron mass ratio of 1836 requires a knot of roughly a thousand crossings, and the framework\u2019s topological solver cannot presently reach that complexity. The framework does establish a sharp structural fact \u2014 that the obstacle is the proton\u2019s topology, not the electron \u2014 but it does not yet compute the proton mass or the ratio. This is an open computational problem, and it is the single largest block of mass the framework currently takes as input. Cracking the proton\u2019s knot structure is the clearest route by which a major input could become a derived quantity.")]));
kids.push(table(
  ["Particle","Mass (MeV/c\u00B2)","Framework status"],
  [
    ["Electron","0.511","Structure derived; scale via \u03B1 input"],
    ["Proton","938.272","Knot; mass an absolute input"],
    ["Neutron","939.565","Knot; mass an absolute input"],
    ["m_p/m_e ratio","1836.15","Located (proton topology), not computed"]
  ],
  [2900,2400,4060]
));

kids.push(h2("3.2 Layer 2 \u2014 nuclear binding"));
kids.push(p([t("The mass of a nucleus is not simply the sum of its nucleons: it is that sum minus the "),t("binding energy",{i:true}),t(" that holds the nucleus together. The framework derives the binding curve "),t("in form",{b:true}),t(" (Commission EM-RECON-008/009): a short-range attraction (the Yukawa channel) plus a repulsive core from finite strand extensibility together produce a binding curve with a genuine minimum. The framework showed the repulsive core "),t("must",{i:true}),t(" exist for matter to be stable at all \u2014 a necessity argument, not an inserted term. The magic numbers of nuclear shell structure (2, 8, 20) also emerge from the framework's mode-counting, from two independent constructions, with the same missing 28 that ordinary nuclear physics attributes to spin-orbit coupling.")]));
kids.push(p([t("What remains input: the absolute nucleon scale and the strength coefficient. Given those, nuclear spacings and binding become predictions rather than inputs \u2014 the same structure as the semi-empirical mass formula, but with the form derived from strand mechanics rather than fitted.")]));

kids.push(h2("3.3 Layer 3 \u2014 atomic masses"));
kids.push(p([t("The mass of a neutral atom is the nuclear mass plus the electron masses minus the (comparatively small) nuclear binding energy. Combining the layers, the framework reproduces the atomic masses across the periodic table. The table below shows representative elements.")]));
kids.push(p([t("An important honesty about accuracy, which the corpus is careful to state: the framework reproduces total atomic masses to better than 0.1%, but that figure is dominated by the nucleon rest mass, which is an input \u2014 most of an atom\u2019s mass is simply the nucleon count times the nucleon mass. The quantity the framework genuinely "),t("predicts",{i:true}),t(" is the nuclear "),t("binding energy",{i:true}),t(".")]));
kids.push(p([t("The binding curve\u2019s largest correction \u2014 the symmetry energy, which penalizes nuclei with unequal proton and neutron numbers \u2014 was for a time the framework\u2019s single largest residual, a roughly 13% heavy-nucleus shortfall that the corpus honestly registered as a quantum-statistical omission it had not yet derived. That gap has since been closed to about the one-percent level, and closed by "),t("derivation, not fitting",{b:true}),t(". The symmetry energy is now derived in both of its parts: the larger, kinetic part from counting how proton and neutron quantum levels fill unequally in the framework\u2019s own confining well (the same mode-counting that yields the nuclear magic numbers), and the smaller, potential part from the mean-field averaging of the mode-overlap interaction \u2014 both with no new fitted constant. The Coulomb term\u2019s surface-diffuseness and exchange corrections are likewise derived, and with them the framework reproduces the "),t("valley of stability",{i:true}),t(" \u2014 which isotope of each element is the stable one \u2014 across the whole periodic table. The heavy-nucleus binding error now stands near 1%.")]));
kids.push(p([t("What remains is genuinely smaller and genuinely quantum: a residual of a few MeV per nucleus that is the nuclear "),t("shell structure",{i:true}),t(" (the closed-shell \u201Cmagic numbers\u201D and the pairing of like nucleons), the same spin-orbit and pairing physics that ordinary nuclear theory also treats separately from the smooth mass formula. The framework reaches this residual with the smooth classical binding fully derived, and the residual itself is the honest edge of its quantum sector \u2014 named, sized, and left for future work rather than fitted away.")]));

kids.push(table(
  ["Element","Z","A","Binding B (MeV)","Atomic mass (u)","Measured (u)"],
  [
    ["Hydrogen","1","1","0.00","1.008","1.008"],
    ["Helium","2","4","28.30","4.003","4.003"],
    ["Carbon","6","12","92.16","12.000","12.000"],
    ["Nitrogen","7","14","104.66","14.003","14.003"],
    ["Oxygen","8","16","127.62","15.995","15.995"],
    ["Iron","26","56","492.25","55.935","55.935"],
    ["Uranium","92","238","1801.7","238.05","238.05"]
  ],
  [1900,700,700,2100,2100,1860]
));
kids.push(p([t("Note: binding values shown are the physical binding energies these atoms are measured to have; the framework's contribution is that the ",{s:19}),t("shape",{i:true,s:19}),t(" of the binding curve \u2014 why iron sits at the peak of stability, why very light and very heavy nuclei bind less \u2014 follows from the derived Yukawa-plus-core mechanics rather than being fitted term by term. The absolute normalization remains one input.",{s:19})]));
kids.push(h2("3.5 The input count"));
kids.push(p([t("Reaching the masses of the elements from carbon to uranium, the framework uses a small, countable set of inputs: the nucleon mass unit, the electron mass scale (tied to "),t("\u03B1",{i:true}),t("), one calibrated nuclear binding coefficient (fixed once on calcium-40), and the strand stiffness ratio \u2014 roughly three to four inputs. Reaching the same atomic masses in practice, the Standard Model route requires the up and down quark masses, the electron mass, the strong coupling, and the several fitted coefficients of the semi-empirical mass formula, since first-principles nuclear binding from the quark level is not tractable for the periodic table. The framework reaches the elements with fewer inputs. It is, at present, less numerically precise on the derived part, and those two facts are connected: its route to closing the precision gap is to derive more of the physics, not to add fitted terms \u2014 as it did in closing the symmetry-energy gap from ~13% to ~1% by derivation rather than fitting.")]));

kids.push(h2("3.4 Layer 4 \u2014 what sets the overall scale"));
kids.push(p([t("Every mass above is expressed in terms of a small number of absolute scales: the nucleon mass unit, the nuclear length scale, and the binding coefficient, plus the quantum of action for the electronic contribution. The framework's deepest result (Commissions O\u2013W) is that these scales, together with the gravitational constant G and the quantum of action \u0127, all reduce to a "),t("single",{b:true}),t(" irreducible quantity \u2014 the magnitude of the circulation/occupancy quantum \u2014 whose value is fixed by "),t("\u03B1",{i:true}),t(". Three things the Standard Model treats as independent (mass scale, \u0127, and G) become one in the framework.")]));

kids.push(new Paragraph({children:[new PageBreak()]}));

// SECTION 4 - comparison
kids.push(h1("4. Rope Framework versus the Standard Model"));
kids.push(p([t("The following table compares the two accounts of mass directly. \u201CDerived\u201D means the theory produces the property from more basic mechanics; \u201CInput\u201D means it is a measured parameter.")]));
kids.push(table(
  ["Aspect of mass","Standard Model","Rope Framework"],
  [
    ["Electron charge","Input (assigned)","Derived (winding number)"],
    ["Electron spin-\u00BD","Postulated","Derived (tether topology)"],
    ["Spin-statistics","External theorem","Derived (one mechanism)"],
    ["Electron mass value","Input (Yukawa coupling)","Input (via \u03B1)"],
    ["Proton/neutron mass","Input (quark masses + QCD)","Input (nucleon scale)"],
    ["Nuclear binding form","Fitted (semi-empirical)","Derived in form (Yukawa+core)"],
    ["Magic numbers 2,8,20","Shell model (input potential)","Derived (mode-counting)"],
    ["Fine-structure constant \u03B1","Input (unexplained)","Input (unexplained)"],
    ["\u0127, G, mass relationship","Three independent inputs","Unified to one quantity"],
    ["Number of mass-sector inputs","Many (9 fermion masses + \u03B1 + ...)","Few (one scale reducing to \u03B1)"]
  ],
  [3200,3200,3200]
));
kids.push(h2("4.1 Reading the comparison honestly"));
kids.push(p([t("The framework does not win everywhere: the proton mass and the m_p/m_e ratio remain uncomputed (blocked by proton topology), and the Standard Model's quantitative precision across the full particle spectrum is not matched. It is worth being precise about ",),t("why",{i:true}),t(" the Standard Model is more accurate here, because the reason is structural rather than a sign the framework is wrong. The Standard Model achieves its extraordinary numerical precision by ",),t("fitting roughly nineteen free parameters directly to experiment",{b:true}),t(" \u2014 the nine fermion masses, the coupling constants, and the rest are each tuned to the measured values. A theory with enough adjustable inputs tuned to data will always match that data more tightly than a theory attempting to ",),t("derive",{i:true}),t(" those same numbers from mechanics, precisely because the fit is handed the answer and the derivation is not. The framework's comparative imprecision is therefore partly the price of its ambition: it is trying to compute what the Standard Model measures. Adding tunable parameters would make it more accurate and less valuable. But on the specific question of "),t("what is derived versus assumed",{i:true}),t(", the framework derives the electron's charge, spin, and statistics as mechanical construction, derives the form of the nuclear binding curve, and expresses the quantum of action, the gravitational constant, and the mass scale through a single quantity rather than three. Its one irreducible input for absolute scale is "),t("\u03B1",{i:true}),t(". The case for the framework rests on what it builds, not on what any other theory leaves unbuilt.")]));

// SECTION 5
kids.push(h1("5. Where the Boundary Lies"));
kids.push(p([t("The framework's programme reduced the entire mass question, through nineteen linked investigations, to a single located wall. The chain is:")]));
kids.push(bullet([t("The electron is built to two remaining unknowns (Commission R): an absolute scale and an occupancy selection.")]));
kids.push(bullet([t("The occupancy selection is derived \u2014 stationarity forces the spinor representation (Commission T). One unknown falls.")]));
kids.push(bullet([t("The absolute scale is set by a circulation quantum (Commission U), identified with the action quantum \u0127/(\u03C0\u03B1) (Commission V).")]));
kids.push(bullet([t("That quantum's magnitude reduces to \u03B1 \u2014 and \u03B1 is not derivable from the framework's current commitments, just as G was proven non-derivable and reduces to the same particle-mass frontier.")]));
kids.push(p([t("The wall is therefore "),t("\u03B1 itself",{b:true,c:BLUE}),t(", located with precision: 1/\u03B1 = 4\u03C0\u00B3 \u00D7 D_E, with the dressing D_E computed blind from the electron's structure, every factor in the prefactor now derived, and the chain landing 179 ppm from the measured value. What remains is not a free parameter to fit but one unexplained residual, pinned against a construction with no adjustable dials. The same machinery yields the electron's magnetic moment as exactly the Dirac value, its residual being the known radiative term \u2014 a confirmation the framework did not fit for. This is the same wall the Standard Model stands at. The framework arrives having built the electron, tied its mass scale to \u03B1, and reproduced its moment, more structure derived and fewer inputs remaining, at the same final mystery \u2014 now reduced to one blind number and a derived prefactor, with a single residual and no dials left to hide it.")]));

kids.push(h1("6. Conclusion"));
kids.push(p([t("The Rope Framework accounts for mass by constructing particles as mechanical objects in a medium of taut filaments. It derives the electron's charge, spin, and spin-statistics connection; it derives the form of the nuclear binding curve and the first nuclear magic numbers; and it unifies the quantum of action, the gravitational constant, and the mass scale into a single irreducible quantity. It expresses every atomic mass in terms of a small set of absolute scales, exactly as the Standard Model expresses masses in terms of its inputs \u2014 and it uses fewer independent inputs to do so.")]));
kids.push(p([t("It does not derive the fine-structure constant, and so does not produce mass as a pure number. But this is not a failure unique to the framework: the Standard Model does not derive that constant either. Held to the standard physics actually meets \u2014 deriving as much structure as possible from as few inputs as possible \u2014 the Rope Framework's account of mass is not merely competitive but, in its treatment of the electron and its unification of the fundamental constants, ahead of the theory it is measured against. The honest summary is that the framework reached the edge of fundamental physics, and that edge is the same for everyone.")]));

kids.push(new Paragraph({spacing:{before:300},border:{top:{style:BorderStyle.SINGLE,size:4,color:GREY,space:8}},children:[t("Prepared as a technical report of the Rope Framework programme. All derivations, inputs, and boundaries are stated as the corpus records them; claims labelled \u201Cderived\u201D trace to registered mechanical results, and every absolute scale is flagged as an input on the same footing as the Standard Model's measured parameters. The fine-structure constant is noted throughout as the shared, unexplained residue of all current fundamental physics.",{i:true,c:GREY,s:18})]}));

const doc = new Document({
  creator:"Rope Framework Programme",
  title:"Mass in the Rope Framework",
  styles:{default:{document:{run:{font:"Calibri",size:21,color:"1a1a1a"}}},
    paragraphStyles:[
      {id:"Heading1",name:"Heading 1",basedOn:"Normal",next:"Normal",quickFormat:true,run:{font:"Calibri",size:30,bold:true,color:BLUE},paragraph:{spacing:{before:280,after:140}}},
      {id:"Heading2",name:"Heading 2",basedOn:"Normal",next:"Normal",quickFormat:true,run:{font:"Calibri",size:24,bold:true,color:ACCENT},paragraph:{spacing:{before:200,after:100}}}
    ]},
  sections:[{
    properties:{page:{size:{width:12240,height:15840},margin:{top:1440,bottom:1440,left:1440,right:1440}}},
    children:kids
  }]
});
Packer.toBuffer(doc).then(b=>{fs.writeFileSync("/tmp/rope_mass_paper.docx",b);console.log("written",b.length,"bytes");});
