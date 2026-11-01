# Brand and combination product pages. No amounts.
import os
from gen import SAMHSA
DIS="> Educational harm-reduction content. Not medical advice, not a guide to use. Nothing here gives amounts, preparation, or sourcing. Counterfeit pills made to look like these brands often contain fentanyl or other drugs."
ING={
"apap":"**Acetaminophen (paracetamol):** adds pain and fever relief without extra sedation, but it is the most common cause of acute liver failure in the US. Liver damage can happen silently over a day or two, with few symptoms until it is severe, and is more likely with alcohol, fasting, liver disease, or taking more than one acetaminophen product at once (many cold medicines contain it). In 2011 the FDA limited the acetaminophen in prescription combinations and added a boxed warning about liver injury. Overdose needs hospital treatment even if the person feels fine.",
"asa":"**Aspirin:** adds anti-inflammatory pain relief but thins the blood and irritates the stomach, raising the risk of stomach bleeding and ulcers, especially with alcohol. Large amounts cause aspirin poisoning: ringing in the ears, fast breathing, confusion, and acid-base problems. Not for children or teens with viral illness (Reye's syndrome).",
"ibu":"**Ibuprofen:** adds anti-inflammatory relief; it can cause stomach bleeding, kidney injury (worse with dehydration), and raises heart and blood-pressure risks.",
"promethazine":"**Promethazine:** an antihistamine that adds heavy drowsiness, anti-nausea effects, and dry mouth. It deepens opioid sedation and breathing depression, can cause confusion, restlessness, and seizures, and is especially dangerous in young children.",
"chlorphen":"**Chlorpheniramine:** a sedating antihistamine that adds drowsiness, dry mouth, and urinary retention, and deepens breathing depression.",
"caffeine":"**Caffeine:** adds a mild lift and helps headache relief; it can cause jitteriness, fast heartbeat, and trouble sleeping, and can mask how sedated someone is.",
"butalbital":"**Butalbital:** a barbiturate that adds sedation and muscle relaxation. Barbiturates have a narrow safety margin, cause dependence, and withdrawal can cause seizures. Frequent use causes rebound (medication-overuse) headaches.",
"naloxone":"**Naloxone (in the tablet or film):** poorly absorbed when the product dissolves under the tongue as directed, so it does little. It is included to discourage injection, which can trigger sudden withdrawal.",
"none":"",
}
P=[
("vicodin","Vicodin","hydrocodone",["apap"],"Introduced by Knoll in 1978; one of the most prescribed drugs in the US through the 2000s. Hydrocodone combinations were moved from Schedule III to Schedule II in 2014. The brand name was discontinued but the name is still used for generics.","The acetaminophen adds pain relief that works differently from the opioid, so many people feel more relief with a milder high than from hydrocodone alone. Some describe a clean, warm, chatty lift with mild itch.","Large, white oblong or capsule-shaped tablets, often scored."),
("norco","Norco","hydrocodone",["apap"],"Launched in the 1990s by Watson with less acetaminophen per tablet than older Vicodin. Became a common hydrocodone brand after the 2011 FDA acetaminophen limits.","Feels like other hydrocodone-acetaminophen products; the opioid part sets the mood effects.","Per one DailyMed generic label: capsule-shaped scored tablets, or unscored ovals, depending on strength."),
("lortab","Lortab","hydrocodone",["apap"],"Brand by UCB, also sold as an elixir (liquid) with a fruity flavor, which raised risks of measuring errors.","Similar to Vicodin and Norco; the liquid works a bit faster.","Tablets are oblong and scored; also a liquid."),
("vicoprofen","Vicoprofen","hydrocodone",["ibu"],"Approved in 1997, combining hydrocodone with ibuprofen instead of acetaminophen.","Stronger relief for inflammatory pain (dental, injuries); the opioid feel is similar. Stomach upset is more common.","Film-coated tablets."),
("percocet","Percocet","oxycodone",["apap"],"Introduced by Endo in 1976. Its name and its blue imprinted tablets ('perc 30s' in street slang refers to counterfeit oxycodone) are among the most counterfeited in the US.","A brighter, more energetic euphoria than hydrocodone combinations for many people, with the acetaminophen adding pain relief.","Tablets vary by strength in color and shape; many are round or oblong and scored. Counterfeit 'Percocet' and 'M30' pills commonly contain fentanyl."),
("endocet","Endocet","oxycodone",["apap"],"Endo's generic-branded version of Percocet.","Same as Percocet.","Round or oblong, scored tablets."),
("roxicet","Roxicet","oxycodone",["apap"],"Roxane's oxycodone-acetaminophen brand, also as an oral solution.","Same as Percocet; the solution works slightly faster.","Tablets and a liquid."),
("percodan","Percodan","oxycodone",["asa"],"Introduced in 1950 by Endo; it was one of the most misused drugs of the 1960s.","The aspirin adds anti-inflammatory relief; stomach upset and bleeding risk are higher than with Percocet.","Yellow, round, scored tablets historically."),
("combunox","Combunox","oxycodone",["ibu"],"Approved in 2004 and later discontinued.","Ibuprofen added anti-inflammatory relief.","Tablets."),
("roxybond","RoxyBond and Oxaydo","oxycodone",["none"],"Abuse-deterrent immediate-release oxycodone tablets (Oxaydo 2011, RoxyBond 2017).","Same as plain immediate-release oxycodone when swallowed as directed.","Tablets designed to resist misuse."),
("tylenol-3-4","Tylenol with Codeine #3 and #4","codeine",["apap"],"Tylenol with codeine has been sold in the US since the 1950s; the numbers refer to how much codeine each tablet contains (#4 has more than #3). In Canada, low-codeine versions were sold without prescription for decades.","A mild, warm, sleepy calm; how strong it feels depends on CYP2D6 genetics, so some people feel nothing and ultra-rapid metabolizers feel much more, with higher danger.","White round tablets."),
("fioricet-codeine","Fioricet with Codeine","codeine",["apap","butalbital","caffeine"],"Fioricet (butalbital, acetaminophen, caffeine) is a long-used tension-headache medicine; the codeine version adds an opioid.","A layered effect: barbiturate sedation and muscle looseness, a caffeine lift, and codeine warmth. People describe it as more 'drunk-feeling' than plain codeine.","Capsules."),
("fiorinal-codeine","Fiorinal with Codeine","codeine",["asa","butalbital","caffeine"],"The aspirin version of Fioricet with codeine.","Similar to Fioricet with codeine; aspirin adds stomach and bleeding risk.","Capsules."),
("tussionex","Tussionex","hydrocodone",["chlorphen"],"An extended-release cough suspension (hydrocodone and chlorpheniramine on a slow-release resin), given every 12 hours.","Heavy, long sleepiness and quieted cough; the antihistamine adds dry mouth and grogginess.","A liquid suspension. Misuse in place of cough syrups has caused fatal breathing depression, including in children."),
("tuxarin","Tuzistra XR and other codeine cough products","codeine",["chlorphen"],"Extended-release codeine-chlorpheniramine cough suspension; other codeine-promethazine syrups are the basis of 'lean'.","Sleepy, heavy, long-lasting calm.","Liquids. See the Lean page for promethazine-codeine."),
("ultracet","Ultracet","tramadol",["apap"],"Tramadol-acetaminophen, approved in 2001 for short-term acute pain.","Mild opioid warmth with tramadol's antidepressant-like effects; nausea is common.","Film-coated tablets. Tramadol's seizure and serotonin risks remain."),
("talacen","Talacen","pentazocine",["apap"],"Pentazocine with acetaminophen; discontinued.","Kappa effects (drowsiness, sometimes odd thoughts) with added pain relief.","Tablets."),
("talwin-nx","Talwin NX","pentazocine",["naloxone"],"Created in 1983 after 'T's and Blues' injection epidemics; naloxone was added to block effects if injected.","When swallowed, like pentazocine; injected, naloxone can cause withdrawal.","Tablets; discontinued in the US."),
("darvocet","Darvocet and Darvon","propoxyphene",["apap"],"Propoxyphene was sold from 1957; Darvocet added acetaminophen. All propoxyphene was withdrawn from the US in 2010 after heart-rhythm deaths.","Weak opioid calm with notable heart risk.","Historical."),
("suboxone","Suboxone","buprenorphine",["naloxone"],"Approved in 2002 for opioid addiction treatment; the film version replaced most tablets in the US around 2010.","For people in treatment, a steady, flat feeling of 'normal' without cravings or withdrawal; little high in tolerant people.","Orange rectangular film (DailyMed). Taking it too soon after full opioids can trigger precipitated withdrawal."),
("zubsolv","Zubsolv","buprenorphine",["naloxone"],"A buprenorphine-naloxone sublingual tablet approved in 2013 that dissolves faster and absorbs more efficiently, so its strengths are not interchangeable with Suboxone.","Similar to Suboxone; some prefer the taste and faster dissolving.","Small tablets with a menthol flavor."),
("subutex","Subutex (buprenorphine alone)","buprenorphine",["none"],"Buprenorphine-only tablets approved in 2002; the brand was discontinued in the US but generics remain, used especially in pregnancy and for starting treatment.","The same buprenorphine effect without naloxone.","Small sublingual tablets."),
("zohydro-hysingla","Zohydro ER and Hysingla ER","hydrocodone",["none"],"Single-ingredient extended-release hydrocodone (2013, 2014).","Slow, flat, long effect with no acetaminophen.","Capsules (Zohydro) and tablets (Hysingla). See the extended-release section on the hydrocodone page."),
("oxycontin","OxyContin","oxycodone",["none"],"Purdue Pharma, 1996. Its aggressive marketing is widely tied to the start of the US opioid crisis. Reformulated in 2010; Purdue pleaded guilty to federal charges in 2007 and 2020.","Slow, steady 12-hour effect when used as directed.","Round, film-coated, bi-convex tablets debossed 'OP' (DailyMed)."),
("ms-contin","MS Contin","morphine",["none"],"Extended-release morphine introduced in 1987.","Steady background relief.","Round, film-coated tablets (DailyMed)."),
("fioricet","Fioricet and Fiorinal (without codeine)","butalbital",["apap","butalbital","caffeine"],"Tension headache medicines containing a barbiturate.","Sedation, muscle looseness and a caffeine lift.","Capsules and tablets. Covered here because they are often confused with the codeine versions."),
]
def render(D):
    os.makedirs("products",exist_ok=True); idx=[]
    for slug,name,drug,ings,hist,feel,touch in P:
        dn=D[drug]["name"] if drug in D else drug.title()
        link=f"[{dn}](../drugs/{drug}.md)" if drug in D else dn
        op=D.get(drug,{}).get("cat","opioid") in("opioid","atypical","nso")
        s=f"# {name}\n\n{DIS}\n\n## What it contains\n\nThe opioid or main ingredient is {link}"+("" if ings==["none"] else ", combined with: "+", ".join(i for i in [{'apap':'acetaminophen','asa':'aspirin','ibu':'ibuprofen','promethazine':'promethazine','chlorphen':'chlorpheniramine','caffeine':'caffeine','butalbital':'butalbital (a barbiturate)','naloxone':'naloxone'}[x] for x in ings]))+".\n\n"
        s+=f"## History\n\n{hist}\n\n## How the combination changes the feel\n\n{feel}\n\n"
        from feel_prod import PF
        if slug in PF:
            s+="## What it feels like over time\n\nTimes vary between people; this describes swallowed tablets.\n\n"
            for k,n in (("onset","Onset"),("peak","Peak"),("plateau","Plateau"),("comedown","Comedown")): s+=f"### {n}\n\n"+"\n\n".join(PF[slug][k])+"\n\n"
            touch=PF[slug]["touch"]
        r=[ING[i] for i in ings if ING[i]]
        if r: s+="## What the added ingredients bring, and their risks\n\n"+"\n\n".join(r)+"\n\n"
        s+=f"## What it feels like to the touch\n\n{touch}"+("" if slug in PF else " Touch and shape cannot confirm what a pill is: ask a pharmacist, use a pill-imprint app or a fentanyl test strip.")+"\n\n"
        s+="## Overdose and safety\n\n"
        if op: s+="Opioid overdose signs: cannot be woken, slow or stopped breathing, blue lips, pinpoint pupils. Call 911 and give [naloxone](../narcan/naloxone.md). Read [opioid overdose](../safety/opioid-overdose.md). "
        if "apap" in ings: s+="If too much was taken, the acetaminophen can destroy the liver even when the person seems fine; go to an emergency department or call Poison Control (1-800-222-1222) right away, since an antidote (acetylcysteine) works best early. "
        if "butalbital" in ings: s+="Butalbital adds barbiturate sedation; see [depressant mixing](../safety/depressant-mixing.md). "
        s+=f"\n\nFor the full drug page, see {link}.\n\n## Getting help\n\n{SAMHSA}\n\n## Sources\n\n- DailyMed prescribing information for {name}\n- FDA Drug Safety Communication on prescription acetaminophen combination products (2011)\n- DEA Drug Scheduling\n"
        open(f"products/{slug}.md","w").write(s); idx.append((slug,name))
    return idx
