import os
#!/usr/bin/env python3
"""Screw-through-rubber-sheet diagram for the magnetism chapter: the 'no tearing'
requirement forces the sheet to wrap the threaded screw."""
import math
OUT=os.environ.get("PLG_FIGS_OUT", "plg_figs")
NAVY="#1B3A5C"; TEAL="#1F5C5C"; WARM="#B5651D"; RUST="#7B2D26"; GRAY="#666666"
STEEL="#8A97A8"; SHEET="#E7DFCD"; PAPER="#FCFBF8"

W,H=600,340
b=""
b+=f'<text x="{W/2}" y="38" font-size="20" fill="{NAVY}" text-anchor="middle" font-weight="bold" font-family="Georgia,serif">Why the network must wrap the charge</text>'
b+=f'<text x="{W/2}" y="61" font-size="14" fill="{GRAY}" text-anchor="middle" font-family="Georgia,serif">the sheet grips the grooves with no tear \u2014 so it is forced to spiral around</text>'

cx,cy=300,205
# --- the rubber sheet as a shaded disc (seen at an angle: ellipse) with a hole ---
b+=f'<ellipse cx="{cx}" cy="{cy}" rx="230" ry="95" fill="{SHEET}" stroke="{GRAY}" stroke-width="1.5" opacity="0.85"/>'
# hole where the screw passes through
b+=f'<ellipse cx="{cx}" cy="{cy}" rx="30" ry="13" fill="{PAPER}" stroke="{GRAY}" stroke-width="1.2"/>'

# --- the sheet's wrapping pattern: concentric wound rings that spiral into the hole ---
for rr in (60,100,150,200):
    ry=rr*95/230
    b+=f'<ellipse cx="{cx}" cy="{cy}" rx="{rr}" ry="{ry:.0f}" fill="none" stroke="{TEAL}" stroke-width="1.4" stroke-dasharray="5,5" opacity="0.75"/>'
# little arrows on one ring to show circulation sense
import math as m
for ang in (20,110,200,290):
    rr=150; ry=rr*95/230
    x=cx+rr*m.cos(m.radians(ang)); y=cy+ry*m.sin(m.radians(ang))
    # tangent direction
    tx=-rr*m.sin(m.radians(ang)); ty=ry*m.cos(m.radians(ang))
    tl=m.hypot(tx,ty); tx,ty=tx/tl*12,ty/tl*12
    b+=f'<line x1="{x-tx:.0f}" y1="{y-ty:.0f}" x2="{x+tx:.0f}" y2="{y+ty:.0f}" stroke="{RUST}" stroke-width="2" marker-end="url(#mr)"/>'

# --- the screw: vertical shaft through the hole, with helical thread ---
sx=cx
b+=f'<rect x="{sx-11}" y="70" width="22" height="200" rx="4" fill="{STEEL}" stroke="{NAVY}" stroke-width="1.2"/>'
# helical thread lines across the shaft
for yy in range(84,262,17):
    b+=f'<path d="M{sx-11},{yy} Q{sx},{yy+8} {sx+11},{yy-2}" fill="none" stroke="{NAVY}" stroke-width="1.6"/>'
b+=f'<text x="{sx+22}" y="95" font-size="13" fill="{NAVY}" text-anchor="start" font-family="Georgia,serif" font-style="italic">the charge:</text>'
b+=f'<text x="{sx+22}" y="112" font-size="13" fill="{NAVY}" text-anchor="start" font-family="Georgia,serif" font-style="italic">a two-strand winding</text>'

# labels
b+=f'<text x="{cx-215}" y="{cy+70}" font-size="13" fill="{TEAL}" text-anchor="start" font-family="Georgia,serif" font-style="italic">the surrounding network (the sheet)</text>'
b+=f'<text x="{cx+120}" y="{cy+52}" font-size="13" fill="{RUST}" text-anchor="middle" font-family="Georgia,serif" font-style="italic">forced to wrap = the field</text>'

defs=f'<defs><marker id="mr" markerWidth="10" markerHeight="10" refX="8" refY="3.5" orient="auto"><path d="M0,0 L9,3.5 L0,7 Z" fill="{RUST}"/></marker></defs>'
svg=(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
     f'{defs}<rect width="{W}" height="{H}" fill="{PAPER}"/>{b}</svg>')
open(f"{OUT}/plg_screw.svg","w").write(svg)
print("wrote plg_screw.svg")
