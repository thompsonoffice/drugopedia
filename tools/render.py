import os,sys,importlib
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__))+"/..")
from gen import *
from med import expand,VARY
from touch import touch
from lohi import lohi
from er import er
for m in ["data","ph_core","data_rx","data_atyp","data_nso","data_benzo","data_rcbenzo","spec"]:
    try: importlib.import_module(m)
    except ModuleNotFoundError as e:
        if e.name!=m: raise
CATS={"opioid":"Opioids (prescription, heroin, and fentanyl)","atypical":"Atypical opioids","nso":"Novel synthetic opioids","benzo":"Benzodiazepines (prescription)","rcbenzo":"Designer and research-chemical benzodiazepines"}
SAFE={"opioid":("opioid-overdose.md","What an opioid overdose feels and looks like, and what to do"),
"benzo":("benzodiazepine-safety.md","Benzodiazepine safety: overdose, mixing, blackouts, and withdrawal")}
TOL={"opioid":"Tolerance changes everything here. Someone who has never used opioids feels far stronger effects, more nausea, and much higher overdose risk than someone who uses daily, and people who use every day often say they mainly feel 'normal' rather than high.",
"benzo":"Tolerance to the calming and sleep effects of benzodiazepines builds within weeks, while memory loss and the danger of mixing with alcohol or opioids remain. People taking them daily often feel little except relief from anxiety, and stopping suddenly can cause seizures."}
BOD="""## Signs of a benzodiazepine overdose or dangerous sedation

- Extreme drowsiness, cannot be woken, or slurred, confused speech.
- Stumbling, poor coordination, or collapse.
- Slow or shallow breathing, especially if opioids or alcohol are involved.
- Blue or gray lips and fingertips.

## What to do

- Call 911. Good Samaritan laws in most US states protect people who call for help.
- If opioids may be involved (including counterfeit pills), give naloxone; it will not reverse the benzo but can reverse the opioid part.
- Put them on their side in the recovery position and stay with them.
"""
def w(p,s):
    os.makedirs(os.path.dirname(p) or ".",exist_ok=True); open(p,"w").write(s)
def srcs(d): return "## Sources\n\n"+"\n".join(f"- {s}" for s in d["sources"])+"\n"
def base(d): return "benzo" if d.get("cat","opioid") in("benzo","rcbenzo") else "opioid"
counts=0
for slug,d in D.items():
    b=base(d); sf,st=SAFE[b]
    main=list(d["routes"])[0]
    ph=d.get("ph") or std_phases(d["name"].split(" (")[0],"calm, contented",d.get("itch","mild"),d.get("nod","moderate"),d.get("extra_peak",""),d.get("after",""),d.get("nextday",""))
    t=times(slug,main)
    s=f"# {d['name']}\n\n{d.get('dis',DIS)}\n\n## At a glance\n\n{d['cls']}\n\n**Brand and street names:** {d['brands']}\n\n"
    s+=f"## History and origins\n\n{d['history']}\n\n## Medical use, then and now\n\n{d['medical']}\n\n"
    if d.get("treatment"): s+=f"## Role in addiction treatment\n\n{d['treatment']}\n\n"
    s+=f"## How it entered recreational use\n\n{d['recreational']}\n\n## Legal status\n\n{d['legal']}\n\n"
    s+=er(slug)
    s+=touch(slug)
    s+=f"## What it feels like\n\n### The character of its effects\n\n"+"\n\n".join(d["flavor"])+f"\n\n{d.get('tol',TOL[b])}\n\n"
    s+=f"### Timeline\n\nTimes below are typical for the {ROUTES[main][0].lower()} route and vary a lot between people. Other routes change the timing; see the route pages.\n\n"
    E=expand(slug,d,b); ph2=list(ph)
    if d.get("noext"): E={"onset":[],"peak":[],"comedown":[]}
    ph2[0]=ph2[0]+"\n\n"+"\n\n".join(E["onset"]); ph2[2]=ph2[2]+"\n\n"+"\n\n".join(E["peak"]); ph2[4]=ph2[4]+"\n\n"+"\n\n".join(E["comedown"])
    s+=phases("",list(zip(t,ph2)))
    s+=lohi(slug,b,d)
    s+=f"### Why the same amount affects people differently\n\n{VARY[b]}\n\n"
    s+="## How the route changes the experience\n\n"
    for r,note in d["routes"].items():
        s+=f"- [{ROUTES[r][0]}](../routes/{r}/{slug}.md): {note}\n"
    extra="".join(f" Also see [{SAFE[x][1] if x in SAFE else 'Xylazine (tranq)'}](../safety/{SAFE[x][0] if x in SAFE else 'xylazine.md'})." for x in d.get("also",[]))
    s+=f"\nNot covered: {d['skip']}\n\n## Overdose note for {d['name']}\n\n{d['od']}\n\nRead the shared page: [{st}](../safety/{sf}).{extra}"+(" Also see [naloxone (Narcan)](../narcan/naloxone.md)." if b=='opioid' else '')+f"\n\n## Getting help\n\n{SAMHSA}\n\n"+srcs(d)
    w(f"drugs/{slug}.md",s)
    for r,note in d["routes"].items():
        counts+=1
        t=times(slug,r)
        short=[". ".join(x.split(". ")[:2]).rstrip(".")+"." for x in ph]
        rf=d.get("rfeel",{}).get(r,"")
        rs=f"# {d['name']}: {ROUTES[r][0]}\n\n{d.get('dis',DIS)}\n\n## About this route\n\n{ROUTES[r][1]} For {d['name']}: {note}\n\n## How this route feels different\n\n{rf+' ' if rf else ''}{ROUTE_FEEL[r] if b=='opioid' else BROUTE.get(r,'')}\n\n## Timeline for this route\n\n"
        rs+=phases("",list(zip(t,short)))
        rs+=f"For the full, detailed description of each phase, see the [general {d['name']} page](../../drugs/{slug}.md).\n\n"
        rs+=f"## Risks of this route\n\n{RISK[r] if b=='opioid' else BRISK[r]}\n\n## Overdose note\n\n{d['od']}\n\n{OD if b=='opioid' else BOD}\nRead more: [{st}](../../safety/{sf})."+(" See also [naloxone (Narcan)](../../narcan/naloxone.md)." if b=='opioid' else '')+f"\n\n## Getting help\n\n{SAMHSA}\n\n"+srcs(d)
        w(f"routes/{r}/{slug}.md",rs)
print(len(D),"drugs",counts,"route entries")
ix="# Drugopedia index\n\n## Safety\n\n- [Opioid overdose: what it feels like, looks like, and what to do](safety/opioid-overdose.md)\n- [Xylazine (tranq) safety](safety/xylazine.md)\n\n## Overdose reversal medicines\n\n- [Naloxone (Narcan)](narcan/naloxone.md)\n- [Nalmefene (Opvee)](narcan/nalmefene.md)\n"
if os.path.exists("safety/benzodiazepine-safety.md"): ix+="- [Benzodiazepine safety](safety/benzodiazepine-safety.md)\n"
for c,cn in CATS.items():
    L=[k for k,d in D.items() if d.get("cat","opioid")==c]
    if not L: continue
    ix+=f"\n## {cn}: general pages\n\n"+"".join(f"- [{D[k]['name']}](drugs/{k}.md)\n" for k in L)
for r,(n,_) in ROUTES.items():
    ix+=f"\n## Route: {n}\n\n"
    L=[k for k,d in D.items() if r in d["routes"]]
    ix+="".join(f"- [{D[k]['name']}](routes/{r}/{k}.md)\n" for k in L) or "- None yet\n"
w("INDEX.md",ix)
