import os
SAMHSA="SAMHSA National Helpline: **1-800-662-4357** (free, confidential, 24/7, English and Spanish). In an emergency, call **911**."
OD="""## Signs of an opioid overdose

- Breathing that is very slow, shallow, gurgling, or has stopped. Snoring-like sounds can be a warning sign, not sleep.
- Cannot be woken, or does not respond to a loud voice or a firm rub on the breastbone.
- Pinpoint pupils.
- Blue, gray, or ashen lips and fingertips; cold, clammy skin.
- Limp body.

## What to do

- Call 911. Many US states have Good Samaritan laws that protect people who call for help.
- Give naloxone (Narcan or another brand) if it is available. It is sold over the counter in US pharmacies. It can wear off before the opioid does, so overdose can return; stay with the person.
- If they are breathing, put them on their side (recovery position) so they do not choke.
- Never leave the person alone to "sleep it off."
"""
DIS="> Educational harm-reduction content. Not medical advice, not a guide to use. Nothing here gives amounts, preparation, or sourcing. Any opioid can cause fatal overdose, and street drugs are frequently contaminated with fentanyl."

ROUTES={
"oral":("Oral (swallowed)","Swallowed as tablets, capsules, or liquids. The drug passes through the gut and liver first (first-pass metabolism), which lowers and slows what reaches the brain."),
"sublingual-buccal":("Sublingual and buccal (under the tongue or in the cheek)","Absorbed through the lining of the mouth, partly skipping first-pass metabolism."),
"intranasal":("Intranasal (nasal sprays and snorting)","Absorbed through the nasal lining into the bloodstream, faster than swallowing."),
"rectal":("Rectal (suppositories)","Given as suppositories in medicine, mainly when a patient cannot swallow. Absorption is partly protected from first-pass metabolism and varies a lot."),
"transdermal":("Transdermal (skin patches)","Medical skin patches release drug slowly through the skin over days."),
"injected":("Injected (intravenous, intramuscular, subcutaneous)","Delivered into a vein, muscle, or under the skin. Intravenous is the fastest and most dangerous route."),
"inhaled-smoked":("Inhaled and smoked","Vapor or smoke absorbed through the lungs, reaching the brain within seconds."),
}
RISK={
"oral":"Slower onset tempts people to take more before the first amount has peaked (\"stacking\"), a common overdose pattern. Extended-release products hold a large reserve of drug; damaging them releases it all at once and has caused many deaths. Combination products with acetaminophen (paracetamol) can cause liver failure. Constipation and nausea are common.",
"sublingual-buccal":"Effects build slowly and last long, so a second amount may overlap with the first. Dental problems have been linked to sublingual buprenorphine films and tablets.",
"intranasal":"Faster, stronger peak than swallowing, raising overdose risk. Damage to nasal tissue, nosebleeds, and sinus infections. Shared straws can spread hepatitis C. Crushing pills meant to be swallowed releases extended-release reserves and binders that harm tissue.",
"rectal":"Absorption is unpredictable, so the effect can be stronger or weaker than expected. Irritation and tissue injury are possible.",
"transdermal":"Heat (fevers, heating pads, hot tubs, sun) can speed release and cause overdose. Children and pets have died from contact with used or discarded patches. Any tampering with a patch is extremely dangerous. Effects keep going for many hours after removal.",
"injected":"The highest overdose risk of any route: the full effect hits within seconds to minutes, with no time to react. Infections (abscesses, endocarditis, sepsis), HIV and hepatitis C from shared equipment, collapsed veins, and damage from pill fillers, which are not made for veins. Syringe service programs offer sterile supplies, testing, and naloxone.",
"inhaled-smoked":"Very fast onset makes the drug feel compulsive, encouraging repeated use and dependence. Overdose can happen within minutes. Lung irritation, burns, and shared equipment risks. Smoking is lower risk than injecting for infections, but is not safe.",
}
def phases(title, ph):
    names=["Onset","Come-up","Peak","Plateau","Comedown","After-effects","Next day"]
    out=""
    for n,(t,txt) in zip(names,ph):
        out+=(f"### {n}\n\n" if t==n.lower() else f"### {n} ({t})\n\n")+f"{txt}\n\n"
    return out

D={}
def drug(slug,**k): D[slug]=k

# ---------- shared phase text builders ----------
def std_phases(name, flavor_short, itch="mild", nod="moderate", extra_peak="", after="", nextday=""):
    return [
f"""The first sign is often subtle: a faint warmth in the stomach or chest, a slight heaviness behind the eyes, and a loosening of tension in the shoulders. People describe it as the edge coming off whatever they were feeling. With {name}, many say they notice their breathing slow slightly and their thoughts get quieter before they feel anything they would call pleasure.""",
f"""The warmth spreads outward to the arms, legs, and face. Pain, if present, fades into the background rather than disappearing outright; people describe still knowing it is there but no longer caring. A {flavor_short} mood rises. Itching, usually {itch}, often starts on the nose, face, or upper body, caused by histamine release and by opioid effects on the nervous system. Some people feel a wave of nausea at this point, especially if they are new to opioids or moving around.""",
f"""At the peak, people describe a deep, cozy contentment, as if wrapped in a warm blanket, with worries feeling far away and unimportant. Body feels heavy and relaxed; speech can slow. Pupils shrink to pinpoints. {extra_peak} This is also when breathing is most suppressed and overdose is most likely, often without the person noticing anything wrong.""",
f"""The effects level off into a steady, calm state. "Nodding" ({nod} with {name}) can occur: drifting in and out of a light sleep, head dropping, then jerking awake, sometimes mid-sentence or with a cigarette or drink in hand. People report vivid, dreamlike half-sleep. Talkativeness or a quiet, inward contentment are both common. Mouth dryness, flushed skin, and difficulty urinating can appear.""",
f"""The glow fades gradually. People describe the world getting "louder" again: light, noise, and small problems regain their weight. Tiredness and a flat, slightly gray mood are common. Pain, if it was being treated, returns. In people with dependence, this is where restlessness, yawning, and craving start.""",
after or f"""Over the following hours: constipation, dry mouth, mild headache, and sluggishness. Sleep may be heavy but not restful. Some feel a mild low mood or irritability as the drug clears.""",
nextday or f"""After a single medical exposure, most people feel close to normal, perhaps a little foggy or constipated. After repeated use, the next day can bring early withdrawal: anxiety, runny nose, goosebumps, aches, diarrhea, and strong craving. Tolerance builds quickly, which means the same effect needs more drug and overdose risk rises, especially after a break, when tolerance drops but habits do not."""]

def T(route_times):
    return route_times

# route timing defaults: onset, comeup, peak, plateau, comedown, after, nextday
RT={
"oral":["15-45 min","30-60 min","1-2 h","2-4 h","4-6 h","6-24 h","next day"],
"oral-er":["30-90 min","1-3 h","3-6 h","6-12 h","12-24 h","24-36 h","next day"],
"sublingual-buccal":["10-30 min","30-60 min","1-3 h","2-4 h","4-8 h","8-24 h","next day"],
"intranasal":["5-15 min","10-20 min","15-45 min","1-2 h","2-4 h","4-12 h","next day"],
"rectal":["10-30 min","20-40 min","45-90 min","1-3 h","3-6 h","6-24 h","next day"],
"transdermal":["6-12 h","12-24 h","24-72 h","while patch on","12-24+ h after removal","1-3 days","after removal"],
"injected":["IV seconds; IM/SC 5-15 min","IV under 1 min; IM/SC 10-20 min","IV 2-10 min; IM/SC 20-60 min","30 min-2 h","2-4 h","4-12 h","next day"],
"inhaled-smoked":["seconds","under 1 min","1-5 min","10-30 min","30 min-2 h","2-6 h","next day"],
}
ROUTE_FEEL={
"oral":"Swallowing gives the slowest, smoothest, longest experience of the fast routes. There is no \"rush\"; instead the effects creep in over half an hour or more. Nausea is more common because the drug sits in the stomach. Pain relief lasts longer.",
"sublingual-buccal":"Slower and steadier than injecting or snorting, faster than swallowing for some drugs. There is no rush; people describe a gradual settling.",
"intranasal":"A noticeably quicker and sharper onset than swallowing, with a mild rush or 'drop' of warmth, a bitter drip in the throat, and a shorter overall duration.",
"rectal":"Onset sits between swallowing and snorting. It is mostly used medically; experiences vary because absorption is uneven.",
"transdermal":"No rush and no clear peak; a slow, flat, constant effect over days. Medical patients mostly notice steady pain relief, drowsiness, and constipation.",
"injected":"Intravenous use produces the classic 'rush': within seconds a hot, intense wave of pleasure from the stomach up through the chest and head, often compared to orgasm, sometimes with flushing, a heavy body, and a feeling of 'coming home'. It is shorter and the comedown is harder. Intramuscular and subcutaneous injection are slower, without much of a rush.",
"inhaled-smoked":"Almost as fast as injecting, but in shorter, smaller waves with each breath. People describe a quick, warm, dreamy hit that fades fast, leading to frequent redosing.",
}
def times(slug,route):
    o=D[slug].get("times",{}).get(route)
    return o or RT[route]
BROUTE={
"oral":"Swallowing is the standard medical route. Effects build gradually, with no rush; food can slow onset.",
"sublingual-buccal":"Under the tongue, some benzodiazepines start a little faster than when swallowed. Medically used for alprazolam, lorazepam, and others in some countries, and buccal midazolam for seizures.",
"intranasal":"Medical nasal sprays (midazolam, diazepam) are used to stop seizures quickly. Snorting pills is a misuse route that brings faster onset, more blackouts, and nasal damage.",
"rectal":"Rectal diazepam gel (Diastat) is used by families and caregivers to stop prolonged seizures.",
"injected":"Injection is a hospital route for sedation, anesthesia, alcohol withdrawal, and status epilepticus. Effects can begin within a minute, and breathing must be monitored.",
"inhaled-smoked":"Not a medical route.",
"transdermal":"Not a medical route."}
BRISK={"oral":"Slow onset tempts people to take more before the first amount peaks. Long-acting drugs and their metabolites build up over days, especially in older adults, causing falls, confusion, and impaired driving. Counterfeit pills may contain fentanyl or designer benzodiazepines.",
"sublingual-buccal":"Faster onset than swallowing for some drugs, with a sharper drop in alertness and memory.",
"intranasal":"Medical sprays are designed for seizures and are safe when used as directed. Snorting pills causes nasal damage, faster sedation, and more blackouts.",
"rectal":"Used by caregivers for seizures; sedation and slowed breathing must be watched afterward.",
"injected":"A hospital route. IV benzodiazepines can stop breathing, especially with opioids, so they are given with monitoring. Injecting pills or powders causes vein damage, infections, and gangrene (temazepam gel capsules in the UK caused amputations).",
"inhaled-smoked":"Not a typical route.","transdermal":"Not a medical route."}
