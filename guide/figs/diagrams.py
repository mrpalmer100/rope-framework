#!/usr/bin/env python3
"""All plain-language-guide diagrams, callable by name: make(name) -> writes <name>.svg.
Keeps the guide's warm palette. The build script renders these to PNG via soffice."""
import math

NAVY="#1B3A5C"; TEAL="#1F5C5C"; WARM="#B5651D"; RUST="#7B2D26"; GRAY="#666666"
SKY="#D6E4F0"; SAND="#EDE4D0"; PAPER="#FCFBF8"; STEEL="#8A97A8"; SHEET="#E7DFCD"

def _wrap(h, body, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="600" height="{h}" '
            f'viewBox="0 0 600 {h}" font-family="Georgia, serif">{defs}'
            f'<rect width="600" height="{h}" fill="{PAPER}"/>{body}</svg>')
def _t(x,y,s,size=15,col=NAVY,anc="middle",it=False,wt="normal"):
    st=' font-style="italic"' if it else ''
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{col}" text-anchor="{anc}" font-weight="{wt}"{st}>{s}</text>'
def _arrow(col,idn):
    return f'<marker id="{idn}" markerWidth="11" markerHeight="11" refX="8" refY="3.5" orient="auto"><path d="M0,0 L9,3.5 L0,7 Z" fill="{col}"/></marker>'

def braid():
    H=330
    b=_t(300,34,"Charge is handedness — like a left and a right glove",19,NAVY,wt="bold")
    b+=_t(300,55,"same strands, mirror-image orientation; no separate 'charge'",12,GRAY)
    def hand(cx,sign,label):
        # draw two strands emerging with a handedness (chirality shown by which way they cross)
        yc=150; import math
        x0,x1=cx-58,cx+58; amp=20; L=x1-x0; p1=[];p2=[]
        for i in range(0,L+1,3):
            ph=2*math.pi*1.5*i/L
            p1.append(f"{x0+i},{yc-amp*math.sin(ph)}")
            p2.append(f"{x0+i},{yc-amp*math.sin(ph+sign*math.pi)}")
        col1,col2=(NAVY,WARM) if sign>0 else (WARM,NAVY)
        s=f'<polyline points="{" ".join(p1)}" fill="none" stroke="{col1}" stroke-width="2.6"/>'
        s+=f'<polyline points="{" ".join(p2)}" fill="none" stroke="{col2}" stroke-width="2.6"/>'
        # a little curl arrow indicating handedness
        aid="ar" if sign>0 else "al"
        s+=f'<path d="M{cx},{yc-40} A20,20 0 1,{1 if sign>0 else 0} {cx+(1 if sign>0 else -1)},{yc-40}" fill="none" stroke="{TEAL}" stroke-width="2" marker-end="url(#{aid})"/>'
        s+=_t(cx,yc+56,label,14,NAVY,wt="bold")
        return s
    defs=f'<defs>{_arrow(TEAL,"ar")}{_arrow(TEAL,"al")}</defs>'
    b+=hand(175,+1,"electron")+_t(175,232,"one handedness",11,GRAY,it=True)
    b+=_t(300,168,"vs",16,GRAY)
    b+=hand(425,-1,"positron")+_t(425,232,"mirror image",11,GRAY,it=True)
    b+=_t(300,270,"Opposite handedness can mesh (attract), like a left and right hand clasping;",11,GRAY,it=True)
    b+=_t(300,286,"same handedness cannot (repel). Charge = which handedness the strands present.",11,GRAY,it=True)
    return _wrap(H,b,defs)


def stream():
    H=330; import math
    defs=f'<defs>{_arrow(TEAL,"at")}{_arrow(GRAY,"ag")}</defs>'
    b=_t(300,34,"Current — turning the helix like a screw",20,NAVY,wt="bold")
    b+=_t(300,55,"rotate the two-strand helix at one end; the screw drives the load at the other",12,GRAY)
    # draw a helix (two strands) as a horizontal screw from battery to load
    x0,x1=110,470; yc=160; amp=22; L=x1-x0; p1=[];p2=[]
    for i in range(0,L+1,3):
        ph=2*math.pi*4*i/L
        p1.append(f"{x0+i},{yc-amp*math.sin(ph)}")
        p2.append(f"{x0+i},{yc-amp*math.sin(ph+math.pi)}")
    b+=f'<polyline points="{" ".join(p1)}" fill="none" stroke="{NAVY}" stroke-width="2.4"/>'
    b+=f'<polyline points="{" ".join(p2)}" fill="none" stroke="{WARM}" stroke-width="2.4"/>'
    # battery (source) at left, turning arrow
    b+=f'<rect x="{x0-46}" y="{yc-26}" width="30" height="52" rx="4" fill="{SAND}" stroke="{RUST}" stroke-width="2"/>'
    b+=_t(x0-31,yc+44,"battery",11,RUST)
    b+=f'<path d="M{x0-31},{yc-40} A16,16 0 1,1 {x0-30},{yc-40}" fill="none" stroke="{TEAL}" stroke-width="2.2" marker-end="url(#at)"/>'
    b+=_t(x0-31,yc-52,"turn",11,TEAL)
    # load (lamp) at right, turning arrow
    b+=f'<circle cx="{x1+22}" cy="{yc}" r="17" fill="{SAND}" stroke="{WARM}" stroke-width="2"/>'
    b+=_t(x1+22,yc+40,"load",11,WARM)
    b+=f'<path d="M{x1+22},{yc-34} A14,14 0 1,1 {x1+23},{yc-34}" fill="none" stroke="{TEAL}" stroke-width="2" marker-end="url(#at)"/>'
    b+=_t(x1+22,yc-46,"turns",11,TEAL)
    b+=_t(300,250,"Turning a plain rod just spins it; turning a HELIX drives motion along it,",11,GRAY,it=True)
    b+=_t(300,266,"like a corkscrew or an Archimedes screw. Rotation and transport are one motion.",11,GRAY,it=True)
    b+=_t(300,290,"(The turning runs down the rope as a very fast torsional wave — not rigid lockstep —",10,STEEL,it=True)
    b+=_t(300,304,"which is why work actually reaches the load.)",10,STEEL,it=True)
    return _wrap(H,b,defs)


def loop():
    H=320; defs=f'<defs>{_arrow(WARM,"aw")}</defs>'
    b=_t(300,36,"Why current needs a closed loop",20,NAVY,wt="bold")
    b+=_t(300,58,"wraps must enter at one end and leave at the other — or the rope winds up",13,GRAY)
    lx,rx,ty,by=140,460,110,250
    b+=f'<rect x="{lx}" y="{ty}" width="{rx-lx}" height="{by-ty}" rx="10" fill="none" stroke="{NAVY}" stroke-width="3"/>'
    b+=f'<line x1="{lx}" y1="170" x2="{lx}" y2="185" stroke="{PAPER}" stroke-width="6"/>'
    b+=f'<line x1="{lx-9}" y1="168" x2="{lx+9}" y2="168" stroke="{RUST}" stroke-width="3"/>'
    b+=f'<line x1="{lx-5}" y1="187" x2="{lx+5}" y2="187" stroke="{RUST}" stroke-width="5"/>'
    b+=_t(lx-16,180,"battery",11,RUST,"end")+_t(lx-16,196,"(twist pump)",11,RUST,"end")
    b+=f'<line x1="{lx+70}" y1="{ty}" x2="{rx-70}" y2="{ty}" stroke="{WARM}" stroke-width="2.5" marker-end="url(#aw)"/>'
    b+=f'<line x1="{rx}" y1="{ty+50}" x2="{rx}" y2="{by-50}" stroke="{WARM}" stroke-width="2.5" marker-end="url(#aw)"/>'
    b+=f'<line x1="{rx-70}" y1="{by}" x2="{lx+70}" y2="{by}" stroke="{WARM}" stroke-width="2.5" marker-end="url(#aw)"/>'
    b+=_t(300,ty-8,"wraps stream out (+)",11,WARM)+_t(300,by+18,"wraps return (−)",11,WARM)
    b+=_t(rx+12,180,"lamp / load",11,NAVY,"start")
    b+=_t(300,290,"The battery supplies wraps at one terminal and takes them back at the other.",12,GRAY,it=True)
    b+=_t(300,306,"No loop = nowhere for wraps to go = no steady current. This is charge conservation.",12,GRAY,it=True)
    return _wrap(H,b,defs)

REGISTRY={"braid":braid,"stream":stream,"loop":loop}

def screw():
    H=320; import math
    b=_t(300,36,"Why a moving winding makes a field that CURLS",20,NAVY,wt="bold")
    b+=_t(300,58,"the two-strand helix has a screw-sense; a scalar imbalance has none",13,GRAY)
    # left: scalar (no handedness) -> no circulation
    cx=160; cy=175
    b+=f'<line x1="{cx-55}" y1="{cy}" x2="{cx+55}" y2="{cy}" stroke="{GRAY}" stroke-width="6"/>'
    b+=_t(cx,cy+70,"scalar imbalance:",13,GRAY)+_t(cx,cy+88,"no screw-sense, no curl",12,GRAY,it=True)
    b+=_t(cx,cy-40,"?",26,GRAY)
    # right: helix with handedness -> circulation
    hx=440; L=110; amp=20
    p1=[];p2=[]
    for i in range(0,L+1,3):
        ph=2*math.pi*2*i/L
        p1.append(f"{hx-55+i},{cy-amp*math.sin(ph)}"); p2.append(f"{hx-55+i},{cy+amp*math.sin(ph)}")
    b+=f'<polyline points="{" ".join(p1)}" fill="none" stroke="{NAVY}" stroke-width="2.5"/>'
    b+=f'<polyline points="{" ".join(p2)}" fill="none" stroke="{WARM}" stroke-width="2.5"/>'
    # circulation arrow around it
    b+=f'<path d="M{hx},{cy-46} A46,46 0 1,1 {hx-1},{cy-46}" fill="none" stroke="{TEAL}" stroke-width="2.2" marker-end="url(#at)"/>'
    b+=_t(hx,cy+70,"two-strand helix:",13,NAVY)+_t(hx,cy+88,"handedness sets a curl direction",12,TEAL,it=True)
    defs=f'<defs>{_arrow(TEAL,"at")}</defs>'
    return _wrap(H,b,defs)

REGISTRY["screw"]=screw


def gravity():
    H=340
    b=_t(300,34,"Gravity — masses conditioning the shared ropes",19,NAVY,wt="bold")
    b+=_t(300,55,"a mass is a source that tightens the surrounding network; another mass feels the pull",12,GRAY)
    yc=200
    # two masses
    mA=(180,yc); mB=(430,yc)
    # bundle of ropes converging on each mass (a 'star' of tension lines)
    for (cx,cy) in (mA,mB):
        for k in range(12):
            ang=math.radians(k*30)
            x2=cx+90*math.cos(ang); y2=cy+70*math.sin(ang)
            b+=f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{STEEL}" stroke-width="1.4"/>'
    # ropes running BETWEEN the two masses, drawn as a two-strand helix under tension
    x0,x1=mA[0]+26,mB[0]-26; L=x1-x0; amp=9; p1=[];p2=[]
    for i in range(0,L+1,3):
        ph=2*math.pi*4*i/L
        p1.append(f"{x0+i},{yc-amp*math.sin(ph):.1f}")
        p2.append(f"{x0+i},{yc-amp*math.sin(ph+math.pi):.1f}")
    b+=f'<polyline points="{" ".join(p1)}" fill="none" stroke="{NAVY}" stroke-width="2.4"/>'
    b+=f'<polyline points="{" ".join(p2)}" fill="none" stroke="{WARM}" stroke-width="2.4"/>'
    for (cx,cy),lab in ((mA,"mass"),(mB,"mass")):
        b+=f'<circle cx="{cx}" cy="{cy}" r="22" fill="{SAND}" stroke="{RUST}" stroke-width="2.5"/>'
        b+=_t(cx,cy+5,lab,12,NAVY,wt="bold")
    # tension arrows pulling the masses toward each other
    defs=f'<defs>{_arrow(TEAL,"ag")}</defs>'
    b+=f'<line x1="{mA[0]+30}" y1="{yc+40}" x2="{mA[0]+80}" y2="{yc+40}" stroke="{TEAL}" stroke-width="2.4" marker-end="url(#ag)"/>'
    b+=f'<line x1="{mB[0]-30}" y1="{yc+40}" x2="{mB[0]-80}" y2="{yc+40}" stroke="{TEAL}" stroke-width="2.4" marker-end="url(#ag)"/>'
    b+=_t(300,yc-40,"ropes under tension",11,GRAY,it=True)
    b+=_t(300,300,"The many ropes converging on each mass are drawn taut; the shared ropes between them",11,GRAY,it=True)
    b+=_t(300,316,"pull the masses together. Weak-field only — this reproduces Newton, not full general relativity.",11,GRAY,it=True)
    return _wrap(H,b,defs)
REGISTRY["gravity"]=gravity

def chemistry():
    H=340
    b=_t(300,34,"Chemistry — standing-wave shells around a nucleus",19,NAVY,wt="bold")
    b+=_t(300,55,"electrons are standing vibration patterns of the ropes, like notes on a string",12,GRAY)
    cx,cy=300,195
    # nucleus: dense knot
    b+=f'<circle cx="{cx}" cy="{cy}" r="16" fill="{RUST}" stroke="{NAVY}" stroke-width="2"/>'
    b+=_t(cx,cy+5,"nucleus",9,PAPER,wt="bold")
    # concentric standing-wave shells, drawn as wavy (node-bearing) rings
    for ri,(r,nlobes) in enumerate([(52,8),(84,12),(116,16)]):
        pts=[]
        for deg in range(0,361,4):
            a=math.radians(deg)
            rr=r+6*math.sin(nlobes*a)
            pts.append(f"{cx+rr*math.cos(a):.1f},{cy+rr*math.sin(a):.1f}")
        col=[NAVY,WARM,TEAL][ri]
        b+=f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="2"/>'
        b+=_t(cx+r+12,cy-r-2,f"2n²={2*(ri+1)**2}",10,col,anc="start")
    b+=_t(300,300,"Each ring is a standing wave that fits a whole number of humps around the nucleus — only",11,GRAY,it=True)
    b+=_t(300,316,"certain patterns fit. Their capacities 2, 8, 18 (=2n²) come from the rope's two strands × n² shapes.",11,GRAY,it=True)
    return _wrap(H,b)
REGISTRY["chemistry"]=chemistry

def nuclear():
    H=340
    b=_t(300,34,"The strong force — bundles in contact",19,NAVY,wt="bold")
    b+=_t(300,55,"the same 'can't share space' that makes matter solid, at nuclear scale",12,GRAY)
    yc=185
    # two nucleons drawn as dense bundles of short ropes, touching
    def bundle(cx):
        s=f'<circle cx="{cx}" cy="{yc}" r="40" fill="{SAND}" stroke="{RUST}" stroke-width="2"/>'
        for k in range(16):
            a=math.radians(k*22.5)
            s+=f'<line x1="{cx+8*math.cos(a):.1f}" y1="{yc+8*math.sin(a):.1f}" x2="{cx+34*math.cos(a):.1f}" y2="{yc+34*math.sin(a):.1f}" stroke="{NAVY}" stroke-width="1.5"/>'
        return s
    b+=bundle(232)+bundle(368)
    b+=_t(232,yc+62,"nucleon",12,NAVY,wt="bold")+_t(368,yc+62,"nucleon",12,NAVY,wt="bold")
    # contact zone highlighted
    b+=f'<ellipse cx="300" cy="{yc}" rx="14" ry="40" fill="none" stroke="{WARM}" stroke-width="2.5" stroke-dasharray="4 3"/>'
    b+=_t(300,yc-52,"bundles touch → strong force",11,WARM)
    b+=_t(300,292,"Where the dense rope bundles overlap they push and grip hugely — short range (they either",11,GRAY,it=True)
    b+=_t(300,308,"touch or don't), charge-blind, with a hard core. Mechanism shown; the exact strength isn't yet derived.",11,GRAY,it=True)
    return _wrap(H,b)
REGISTRY["nuclear"]=nuclear

def heat():
    H=330
    b=_t(300,34,"Heat — the jiggling of the ropes",19,NAVY,wt="bold")
    b+=_t(300,55,"temperature is how vigorously the rope network vibrates; heat flows as that jiggle spreads",12,GRAY)
    import random; random.seed(7)
    # cold side: calm ropes; hot side: agitated ropes
    def side(x0,x1,agit,label,col):
        yc=185; L=x1-x0; s=""
        for row in range(3):
            y=yc-30+row*30; p=[]
            for i in range(0,L+1,4):
                ph=2*math.pi*3*i/L
                jitter=agit*math.sin(ph*2.7+row)+ (random.uniform(-agit,agit))
                p.append(f"{x0+i},{y-6*math.sin(ph)-jitter:.1f}")
            s+=f'<polyline points="{" ".join(p)}" fill="none" stroke="{col}" stroke-width="2"/>'
        s+=_t((x0+x1)/2,yc+70,label,13,NAVY,wt="bold")
        return s
    b+=side(60,285,2,"cool — small jiggle",TEAL)
    b+=side(315,540,13,"hot — big jiggle",WARM)
    # heat-flow arrow from hot to cool
    defs=f'<defs>{_arrow(RUST,"ah")}</defs>'
    b+=f'<line x1="360" y1="95" x2="240" y2="95" stroke="{RUST}" stroke-width="2.6" marker-end="url(#ah)"/>'
    b+=_t(300,88,"heat flows hot → cool",11,RUST)
    b+=_t(300,290,"Nothing new is added for heat: it is the ordinary vibration of the ropes, and temperature",11,GRAY,it=True)
    b+=_t(300,306,"is simply how hard they shake. The same statistical laws come out as in standard thermodynamics.",11,GRAY,it=True)
    return _wrap(H,b,defs)
REGISTRY["heat"]=heat

def light():
    H=330
    b=_t(300,34,"Light — a transverse ripple racing down the rope",19,NAVY,wt="bold")
    b+=_t(300,55,"a sideways flick that travels, the way a wave runs down a snapped jump rope",12,GRAY)
    yc=175
    # two atom hubs the rope runs between
    hx0,hx1=70,530
    b+=f'<circle cx="{hx0}" cy="{yc}" r="16" fill="{RUST}" stroke="{NAVY}" stroke-width="2"/>'
    b+=f'<circle cx="{hx1}" cy="{yc}" r="16" fill="{RUST}" stroke="{NAVY}" stroke-width="2"/>'
    b+=_t(hx0,yc+34,"atom",11,NAVY,wt="bold")+_t(hx1,yc+34,"atom",11,NAVY,wt="bold")
    # the rope as a transverse wave: a single travelling hump toward the right
    x0,x1=hx0+18,hx1-18; L=x1-x0; pts=[]
    for i in range(0,L+1,3):
        frac=i/L
        # localized hump (gaussian envelope) riding a gentle sine, biased left-of-centre to imply motion
        env=math.exp(-((frac-0.42)**2)/(2*0.06**2))
        y=yc-34*env*math.sin(2*math.pi*3*frac)
        pts.append(f"{x0+i},{y:.1f}")
    b+=f'<polyline points="{" ".join(pts)}" fill="none" stroke="{NAVY}" stroke-width="2.8"/>'
    # motion arrow (the ripple travels toward the far atom)
    defs=f'<defs>{_arrow(TEAL,"al")}</defs>'
    b+=f'<line x1="255" y1="{yc-52}" x2="330" y2="{yc-52}" stroke="{TEAL}" stroke-width="2.4" marker-end="url(#al)"/>'
    b+=_t(292,yc-58,"travels at speed c",11,TEAL)
    # a small double-headed marker showing the displacement is SIDEWAYS (transverse)
    b+=f'<line x1="200" y1="{yc}" x2="200" y2="{yc-32}" stroke="{WARM}" stroke-width="1.6" stroke-dasharray="3 2"/>'
    b+=_t(214,yc-16,"sideways",10,WARM,anc="start",it=True)
    b+=_t(300,262,"The rope itself only moves side-to-side; the ripple — the light — is what travels along it,",11,GRAY,it=True)
    b+=_t(300,278,"from one atom to another. Its two sideways directions are the two polarisations of light.",11,GRAY,it=True)
    return _wrap(H,b,defs)
REGISTRY["light"]=light

def permanentmagnet():
    H=340
    b=_t(300,32,"Permanent magnet — aligned rope-swirls, no current",19,NAVY,wt="bold")
    b+=_t(300,53,"each atom is a tiny swirl; lined up, billions of them make one big circulation",12,GRAY)
    # the bar
    bx0,bx1,by0,by1=180,420,150,210
    b+=f'<rect x="{bx0}" y="{by0}" width="{bx1-bx0}" height="{by1-by0}" rx="4" fill="{SAND}" stroke="{RUST}" stroke-width="2"/>'
    # aligned little swirls inside the bar (all same sense)
    defs=f'<defs>{_arrow(TEAL,"am")}</defs>'
    for i in range(5):
        cx=bx0+28+i*46; cy=(by0+by1)/2
        b+=f'<path d="M{cx+9},{cy-9} A11,11 0 1,1 {cx-9},{cy-9}" fill="none" stroke="{NAVY}" stroke-width="1.8" marker-end="url(#am)"/>'
    b+=_t(300,by1+18,"aligned atomic swirls (same sense)",10,GRAY,it=True)
    # the big field loop sweeping around the whole bar (pole to pole)
    b+=f'<path d="M{bx1-10},{by0+8} C {bx1+90},{by0-30} {bx1+90},{by1+40} {(bx0+bx1)/2},{by1+70}" fill="none" stroke="{WARM}" stroke-width="2.4" marker-end="url(#am)"/>'
    b+=f'<path d="M{(bx0+bx1)/2},{by1+70} C {bx0-90},{by1+40} {bx0-90},{by0-30} {bx0+10},{by0+8}" fill="none" stroke="{WARM}" stroke-width="2.4"/>'
    b+=f'<path d="M{bx0+10},{by0-2} C {(bx0+bx1)/2-30},{by0-34} {(bx0+bx1)/2+30},{by0-34} {bx1-10},{by0-2}" fill="none" stroke="{WARM}" stroke-width="2.4" marker-end="url(#am)"/>'
    # pole labels as sweep-direction, not separate charges
    b+=_t(bx0-8,(by0+by1)/2+4,"S",15,NAVY,anc="end",wt="bold")
    b+=_t(bx1+8,(by0+by1)/2+4,"N",15,NAVY,anc="start",wt="bold")
    b+=_t(300,300,"No charge flows. A 'pole' is just which way the threads sweep at an end — the threads",11,GRAY,it=True)
    b+=_t(300,316,"enter one end and leave the other, so cutting the bar only makes two smaller whole magnets.",11,GRAY,it=True)
    return _wrap(H,b,defs)
REGISTRY["permanentmagnet"]=permanentmagnet

def make(name, outdir="."):
    import os
    if name not in REGISTRY: raise KeyError(f"no diagram '{name}' (have {list(REGISTRY)})")
    svg=REGISTRY[name]()
    path=os.path.join(outdir,f"{name}.svg")
    open(path,"w").write(svg); return path

if __name__=="__main__":
    import sys
    for n in (sys.argv[1:] or REGISTRY): print("wrote", make(n))
