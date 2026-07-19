import os
#!/usr/bin/env python3
"""Diagrams for the corrected electricity chapter (guide palette).
1) charge = frozen braid (linking number)
2) current = braid streaming via local rotation (barber-pole / batons)
3) closed loop = why current needs a circuit (wraps in = wraps out)"""
import math
OUT=os.environ.get("PLG_FIGS_OUT", "plg_figs")
NAVY="#1B3A5C"; TEAL="#1F5C5C"; WARM="#B5651D"; RUST="#7B2D26"; GRAY="#666666"
GOLD="#C99A2E"; SKY="#D6E4F0"; SAND="#EDE4D0"; PAPER="#FCFBF8"

def wrap(s):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="600" height="{h}" '
            'viewBox="0 0 600 {h}" font-family="Georgia, serif">{defs}'
            '<rect width="600" height="{h}" fill="'+PAPER+'"/>{b}</svg>')
def txt(x,y,s,size=15,col=NAVY,anc="middle",it=False,wt="normal"):
    st=' font-style="italic"' if it else ''
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{col}" text-anchor="{anc}" font-weight="{wt}"{st}>{s}</text>'
def amark(col):
    return f'<marker id="m{col[1:]}" markerWidth="11" markerHeight="11" refX="8" refY="3.5" orient="auto"><path d="M0,0 L9,3.5 L0,7 Z" fill="{col}"/></marker>'

# ---------- 1. Frozen braid: two strands wound N times = charge N ----------
def fig_braid():
    H=300; b=""
    b+=txt(300,38,"Charge \u2014 a fixed braid of the two strands",20,NAVY,wt="bold")
    b+=txt(300,60,"how many times they wind = the charge (a whole number)",13,GRAY)
    def braid(cx,N,label):
        x0,x1=cx-70,cx+70; yc=150; amp=22; L=x1-x0
        pts1=[];pts2=[]
        for i in range(0,L+1,3):
            ph=2*math.pi*N*i/L
            pts1.append(f"{x0+i},{yc-amp*math.sin(ph)}")
            pts2.append(f"{x0+i},{yc+amp*math.sin(ph)}")
        nonlocal b
        b+=f'<polyline points="{" ".join(pts1)}" fill="none" stroke="{NAVY}" stroke-width="2.5"/>'
        b+=f'<polyline points="{" ".join(pts2)}" fill="none" stroke="{WARM}" stroke-width="2.5"/>'
        b+=f'<circle cx="{x0}" cy="{yc}" r="5" fill="{GRAY}"/><circle cx="{x1}" cy="{yc}" r="5" fill="{GRAY}"/>'
        b+=txt(cx,yc+58,label,14,NAVY,wt="bold")
    braid(150,0,"neutral (0 wraps)")
    braid(320,1,"charge 1 (1 wrap)")
    braid(480,2,"charge 2 (2 wraps)")
    b+=txt(300,250,"You cannot have half a wrap and still have closed strands \u2014 which is why",12,GRAY,it=True)
    b+=txt(300,266,"charge comes only in whole units. More charge = more wraps, never bigger ones.",12,GRAY,it=True)
    return wrap("").format(h=H,defs="",b=b)

# ---------- 2. Current: braid streams via local rotation (barber pole) ----------
def fig_stream():
    H=320; b=""
    defs=f'<defs>{amark(WARM)}{amark(TEAL)}{amark(GRAY)}</defs>'
    b+=txt(300,36,"Current \u2014 the braid streams down the wire",20,NAVY,wt="bold")
    b+=txt(300,58,"each bit of rope rotates in place; the pattern travels, the material stays",13,GRAY)
    # a barber-pole wire: diagonal stripes inside a horizontal tube
    x0,x1=80,520; yt,yb=110,170
    b+=f'<rect x="{x0}" y="{yt}" width="{x1-x0}" height="{yb-yt}" rx="8" fill="{SKY}" stroke="{NAVY}" stroke-width="2"/>'
    # diagonal stripes (the wraps)
    import math as m
    for s in range(-3,int((x1-x0)/22)+1):
        sx=x0+s*22
        b+=f'<line x1="{sx}" y1="{yb}" x2="{sx+30}" y2="{yt}" stroke="{WARM}" stroke-width="4" opacity="0.8"/>'
    # clip mask via overpainting edges
    b+=f'<rect x="{x0-40}" y="{yt-6}" width="42" height="{yb-yt+12}" fill="{PAPER}"/>'
    b+=f'<rect x="{x1-2}" y="{yt-6}" width="46" height="{yb-yt+12}" fill="{PAPER}"/>'
    b+=f'<rect x="{x0}" y="{yt}" width="{x1-x0}" height="{yb-yt}" rx="8" fill="none" stroke="{NAVY}" stroke-width="2"/>'
    # pattern-travel arrow
    b+=f'<line x1="{x0+60}" y1="90" x2="{x0+200}" y2="90" stroke="{TEAL}" stroke-width="2.5" marker-end="url(#m{TEAL[1:]})"/>'
    b+=txt(x0+130,83,"pattern travels this way (fast)",12,TEAL)
    # local rotation arrows (circular) beneath a couple of points - material rotates in place
    for cxr in (x0+140, x0+300):
        b+=f'<path d="M{cxr-16},{yb+28} A16,16 0 1,1 {cxr-15},{yb+30}" fill="none" stroke="{GRAY}" stroke-width="1.8" marker-end="url(#m{GRAY[1:]})"/>'
    b+=txt(300,yb+70,"the rope rotates in place (like a barber pole) \u2014 the stripes climb forever,",12,GRAY,it=True)
    b+=txt(300,yb+86,"yet the pole never winds up, because each wrap leaving is replaced by one arriving.",12,GRAY,it=True)
    b+=txt(x0-6,145,"",12)
    return wrap("").format(h=H,defs=defs,b=b)

# ---------- 3. Closed loop: current needs a circuit (wraps in = wraps out) ----------
def fig_loop():
    H=320; b=""
    defs=f'<defs>{amark(WARM)}</defs>'
    b+=txt(300,36,"Why current needs a closed loop",20,NAVY,wt="bold")
    b+=txt(300,58,"wraps must enter at one end and leave at the other \u2014 or the rope winds up",13,GRAY)
    # a circuit rectangle with a battery and the wire; arrows showing wrap flow around
    lx,rx,ty,by=140,460,110,250
    b+=f'<rect x="{lx}" y="{ty}" width="{rx-lx}" height="{by-ty}" rx="10" fill="none" stroke="{NAVY}" stroke-width="3"/>'
    # battery on left side
    b+=f'<line x1="{lx}" y1="170" x2="{lx}" y2="185" stroke="{PAPER}" stroke-width="6"/>'
    b+=f'<line x1="{lx-9}" y1="168" x2="{lx+9}" y2="168" stroke="{RUST}" stroke-width="3"/>'
    b+=f'<line x1="{lx-5}" y1="187" x2="{lx+5}" y2="187" stroke="{RUST}" stroke-width="5"/>'
    b+=txt(lx-16,180,"battery",11,RUST,"end")
    b+=txt(lx-16,196,"(twist pump)",11,RUST,"end")
    # flow arrows around the loop (clockwise)
    import math as m
    b+=f'<line x1="{lx+70}" y1="{ty}" x2="{rx-70}" y2="{ty}" stroke="{WARM}" stroke-width="2.5" marker-end="url(#m{WARM[1:]})"/>'
    b+=f'<line x1="{rx}" y1="{ty+50}" x2="{rx}" y2="{by-50}" stroke="{WARM}" stroke-width="2.5" marker-end="url(#m{WARM[1:]})"/>'
    b+=f'<line x1="{rx-70}" y1="{by}" x2="{lx+70}" y2="{by}" stroke="{WARM}" stroke-width="2.5" marker-end="url(#m{WARM[1:]})"/>'
    b+=txt(300,ty-8,"wraps stream out (+)",11,WARM)
    b+=txt(300,by+18,"wraps return (\u2212)",11,WARM)
    b+=txt(rx+12,180,"lamp / load",11,NAVY,"start")
    b+=txt(300,290,"The battery supplies wraps at one terminal and takes them back at the other.",12,GRAY,it=True)
    b+=txt(300,306,"No loop = nowhere for wraps to go = no steady current. This is charge conservation.",12,GRAY,it=True)
    return wrap("").format(h=H,defs=defs,b=b)

for name,fn in [("braid",fig_braid),("stream",fig_stream),("loop",fig_loop)]:
    open(f"{OUT}/plg_{name}.svg","w").write(fn())
    print("wrote plg_"+name+".svg")
