from data import *
import os
def w(p,s):
    os.makedirs(os.path.dirname(p) or ".",exist_ok=True); open(p,"w").write(s)
def srcs(d): return "## Sources\n\n"+"\n".join(f"- {s}" for s in d["sources"])+"\n"
NAL="[What an overdose feels and looks like, and what to do](../{}safety/opioid-overdose.md)"
counts=0
for slug,d in D.items():
    main=list(d["routes"])[0]
    ph=std_phases(d["name"].split(" (")[0],"calm, contented",d.get("itch","mild"),d.get("nod","moderate"),d.get("extra_peak",""),d.get("after",""),d.get("nextday",""))
    t=times(slug,main)
    s=f"# {d['name']}\n\n{DIS}\n\n## At a glance\n\n{d['cls']}\n\n**Brand and street names:** {d['brands']}\n\n"
    s+=f"## History and origins\n\n{d['history']}\n\n## Medical use, then and now\n\n{d['medical']}\n\n"
    if d.get("treatment"): s+=f"## Role in addiction treatment\n\n{d['treatment']}\n\n"
    s+=f"## How it entered recreational use\n\n{d['recreational']}\n\n## Legal status\n\n{d['legal']}\n\n"
    s+=f"## What it feels like\n\n### The character of its euphoria\n\n"+"\n\n".join(d["flavor"])+"\n\n"
    s+=f"Tolerance changes everything below. Someone who has never used opioids feels far stronger effects, more nausea, and much higher overdose risk than someone who uses daily, and people who use every day often say they mainly feel 'normal' rather than high.\n\n"
    s+=f"### Timeline\n\nTimes below are typical for the {ROUTES[main][0].lower()} route. Other routes change the timing; see the route pages.\n\n"
    s+=phases("",list(zip(t,ph)))
    s+="## How the route changes the experience\n\n"
    for r,note in d["routes"].items():
        s+=f"- [{ROUTES[r][0]}](../routes/{r}/{slug}.md): {note}\n"
    s+=f"\nNot covered: {d['skip']}\n\n## Overdose note for {d['name']}\n\n{d['od']}\n\nRead the shared page: {NAL.format('')}.\n\n## Getting help\n\n{SAMHSA}\n\n"+srcs(d)
    w(f"drugs/{slug}.md",s)
    for r,note in d["routes"].items():
        counts+=1
        t=times(slug,r)
        short=[". ".join(x.split(". ")[:2]).rstrip(".")+"." for x in ph]
        rs=f"# {d['name']}: {ROUTES[r][0]}\n\n{DIS}\n\n## About this route\n\n{ROUTES[r][1]} For {d['name']}: {note}\n\n## How this route feels different\n\n{ROUTE_FEEL[r]}\n\n## Timeline for this route\n\n"
        rs+=phases("",list(zip(t,short)))
        rs+=f"For the full, detailed description of each phase and the character of the high, see the [general {d['name']} page](../../drugs/{slug}.md).\n\n"
        rs+=f"## Risks of this route\n\n{RISK[r]}\n\n## Overdose note\n\n{d['od']}\n\n{OD}\nRead more: {NAL.format('../')}.\n\n## Getting help\n\n{SAMHSA}\n\n"+srcs(d)
        w(f"routes/{r}/{slug}.md",rs)
print(len(D),counts)
# index
ix="# Drugopedia index\n\n## Safety\n\n- [Opioid overdose: what it feels like, looks like, and what to do](safety/opioid-overdose.md)\n\n## Opioids: general pages\n\n"
ix+="".join(f"- [{d['name']}](drugs/{k}.md)\n" for k,d in D.items())
for r,(n,_) in ROUTES.items():
    ix+=f"\n## Route: {n}\n\n"
    L=[k for k,d in D.items() if r in d["routes"]]
    ix+="".join(f"- [{D[k]['name']}](routes/{r}/{k}.md)\n" for k in L) or "- None yet\n"
w("INDEX.md",ix)
