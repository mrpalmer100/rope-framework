# The alpha derivation map: every factor of 1/alpha = 4 pi^3 D_E with an arrow
# to the theorem/commission that derived it. Clean SVG, rasterized for the docx.
svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1240" height="1180" viewBox="0 0 1240 1180">
<defs>
<marker id="ar" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto" markerUnits="strokeWidth">
<path d="M0,0 L6,3 L0,6 Z" fill="#2E5A88"/></marker>
<marker id="arg" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto" markerUnits="strokeWidth">
<path d="M0,0 L6,3 L0,6 Z" fill="#4a7c3f"/></marker>
<linearGradient id="der" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#EAF1F8"/><stop offset="100%" stop-color="#D6E4F2"/></linearGradient>
<linearGradient id="blind" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#EAF3E8"/><stop offset="100%" stop-color="#D4E7CF"/></linearGradient>
<linearGradient id="res" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#FBEEE6"/><stop offset="100%" stop-color="#F6E0D0"/></linearGradient>
</defs>
<rect width="1240" height="1180" fill="white"/>
<text x="620" y="46" font-family="Calibri,Arial" font-size="27" font-weight="bold" fill="#1F3864" text-anchor="middle">How 1/\u03b1 Was Derived</text>
<text x="620" y="74" font-family="Calibri,Arial" font-size="15" fill="#595959" text-anchor="middle">Every factor of the fine-structure constant, and the theorem that produced it</text>
'''

# The master formula box
svg += '<rect x="420" y="100" width="400" height="70" rx="12" fill="#1F3864"/>'
svg += '<text x="620" y="132" font-family="Calibri,Arial" font-size="26" font-weight="bold" fill="white" text-anchor="middle">1/\u03b1 = 4 \u03c0\u00b3 \u00d7 D_E</text>'
svg += '<text x="620" y="156" font-family="Calibri,Arial" font-size="14" fill="#c9d6e8" text-anchor="middle">= 137.060504   (measured: 137.035999,  +178.8 ppm)</text>'

# The five factor boxes with provenance. (label, factor, provenance-title, provenance-detail, y, kind)
rows = [
 ("D_E = 1.1051029", "the electron dressing",
  "Commission W \u2014 computed BLIND",
  "EL-BVP solver on the rotating winding terminus; 5 configs, 7-digit agreement, gate PASS. Computed before any comparison to \u03b1.",
  200, "blind"),
 ("\u00d7 4", "rectified two-component sampling",
  "Gate 2 (LINEAR) + Gate 1 rectification theorem",
  "The charge coupling is force-type (degree-1 tether load, EM-013/EM-015). A first-power rotating sampling has zero smooth mean, so its recording is rectified: &lt;|cos|+|sin|&gt; gives 4/\u03c0. Discharged out-of-sample by g=2.",
  300, "der"),
 ("\u00d7 \u03c0", "the J0 anchor conversion",
  "Gate 1 (CLOSED) \u2014 \u03ba = \u03c0/4 forced",
  "The occupancy freeze I = E/\u03c9 = m\u00b7J0 (Commission O) forces the rectified recording; \u03ba = &lt;cos&#178;&gt;/&lt;|cos|&gt; = \u03c0/4. Confirmed by two J0 targets from one formula.",
  400, "der"),
 ("\u00d7 \u03c0", "the target scale \u03c0\u03bb\u0304_C",
  "Commission E \u2014 audited clean",
  "The confinement scale conversion through the tension T0; a single conversion, no free factor.",
  500, "der"),
 ("\u00d7 \u03c0", "the U-closure geometry",
  "Commissions U + T \u2014 two-constraint closure",
  "R* = J/(\u03c0\u00b2\u00b7\u03bc\u00b7q\u00b2\u00b7c), with ln x* = \u03c0\u00b2 exact (T's confinement anchor). The \u03c0\u00b2 is clean rotation-closure geometry.",
  600, "der"),
]
W=520; X=140
for lab, sub, ptitle, pdetail, y, kind in rows:
    fill = {"blind":"url(#blind)","der":"url(#der)","res":"url(#res)"}[kind]
    stroke = {"blind":"#4a7c3f","der":"#2E5A88","res":"#B5652E"}[kind]
    svg += f'<rect x="{X}" y="{y}" width="{W}" height="82" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="1.8"/>'
    svg += f'<text x="{X+22}" y="{y+30}" font-family="Calibri,Arial" font-size="20" font-weight="bold" fill="#1a1a1a">{lab}</text>'
    svg += f'<text x="{X+22}" y="{y+50}" font-family="Calibri,Arial" font-size="13" font-style="italic" fill="#555">{sub}</text>'
    # arrow + provenance to the right
    ax = X+W
    svg += f'<line x1="{ax}" y1="{y+41}" x2="{ax+18}" y2="{y+41}" stroke="{stroke}" stroke-width="2" marker-end="url(#{"arg" if kind=="blind" else "ar"})"/>'
    # provenance text block (wrap detail)
    px = ax+26
    svg += f'<text x="{px}" y="{y+22}" font-family="Calibri,Arial" font-size="12.5" font-weight="bold" fill="{stroke}">{ptitle}</text>'
    # wrap pdetail to ~34 chars
    import textwrap
    lines = textwrap.wrap(pdetail, 44)
    for i,ln in enumerate(lines[:3]):
        svg += f'<text x="{px}" y="{y+40+i*15}" font-family="Calibri,Arial" font-size="11" fill="#444">{ln}</text>'
    # connect factor box down to the formula (visual multiply chain) - subtle
    if y>200:
        svg += f'<line x1="{X-14}" y1="{y}" x2="{X-14}" y2="{y-18}" stroke="#bbb" stroke-width="1.4"/>'

# left spine connecting factors up to the formula
svg += f'<line x1="{X-14}" y1="182" x2="{X-14}" y2="642" stroke="#bbb" stroke-width="1.4"/>'
svg += f'<line x1="{X-14}" y1="170" x2="{X-14}" y2="182" stroke="#2E5A88" stroke-width="2" marker-end="url(#ar)"/>'
svg += f'<text x="{X-24}" y="410" font-family="Calibri,Arial" font-size="12" fill="#888" text-anchor="middle" transform="rotate(-90 {X-24} 410)">multiplied together</text>'

# residual box
ry=706
svg += f'<rect x="380" y="{ry}" width="480" height="66" rx="10" fill="url(#res)" stroke="#B5652E" stroke-width="1.8"/>'
svg += f'<text x="620" y="{ry+27}" font-family="Calibri,Arial" font-size="16" font-weight="bold" fill="#7a3b12" text-anchor="middle">+178.8 ppm \u2014 the single open residual</text>'
svg += f'<text x="620" y="{ry+48}" font-family="Calibri,Arial" font-size="12" fill="#7a3b12" text-anchor="middle">not derived; pinned against a construction with no continuous dials (scale-invariance theorem)</text>'

# confirmations strip
cy=800
svg += f'<text x="620" y="{cy}" font-family="Calibri,Arial" font-size="15" font-weight="bold" fill="#1F3864" text-anchor="middle">Three independent observables, one convention structure</text>'
confs=[
 ("Anchor J0", "Gate 1: one formula hits two registered J0 targets (\u03c0\u03b1 and \u0127)"),
 ("Magnetic moment g=2", "Gate 2b: \u03c0 (mechanical) \u00d7 1/\u03c0 (recording) = Dirac g=2, out of sample; residual = Schwinger term \u03b1/2\u03c0"),
 ("Atomic binding 13.6 eV", "Gate 3: Rydberg at residual\u00b2; convention-count confirms the single 4/\u03c0 lives in e\u00b2"),
]
for i,(t,d) in enumerate(confs):
    yy=cy+24+i*46
    svg += f'<rect x="330" y="{yy}" width="580" height="38" rx="8" fill="#f4f7fa" stroke="#c9d6e8" stroke-width="1.2"/>'
    svg += f'<text x="348" y="{yy+24}" font-family="Calibri,Arial" font-size="13" font-weight="bold" fill="#2E5A88">{t}</text>'
    svg += f'<text x="510" y="{yy+24}" font-family="Calibri,Arial" font-size="11.5" fill="#444">{d}</text>'

# footer honesty line
svg += f'<text x="620" y="1010" font-family="Calibri,Arial" font-size="13" font-style="italic" fill="#595959" text-anchor="middle">Every factor is derived. The +178.8 ppm residual is the single unexplained number.</text>'
svg += f'<text x="620" y="1030" font-family="Calibri,Arial" font-size="13" font-style="italic" fill="#595959" text-anchor="middle">This reduces 1/\u03b1 to one blind number times a derived prefactor \u2014 it is not a derivation of \u03b1\u2019s value.</text>'

# legend
svg += '<rect x="330" y="1070" width="16" height="16" rx="3" fill="url(#blind)" stroke="#4a7c3f" stroke-width="1.3"/><text x="352" y="1083" font-family="Calibri,Arial" font-size="12" fill="#333">Computed blind</text>'
svg += '<rect x="490" y="1070" width="16" height="16" rx="3" fill="url(#der)" stroke="#2E5A88" stroke-width="1.3"/><text x="512" y="1083" font-family="Calibri,Arial" font-size="12" fill="#333">Derived from mechanics</text>'
svg += '<rect x="720" y="1070" width="16" height="16" rx="3" fill="url(#res)" stroke="#B5652E" stroke-width="1.3"/><text x="742" y="1083" font-family="Calibri,Arial" font-size="12" fill="#333">Open residual</text>'
svg += "</svg>"
open("alpha_map.svg","w").write(svg)
print("alpha_map.svg written")
