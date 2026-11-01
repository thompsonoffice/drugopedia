from gen import *
BG=["FDA Drug Safety Communication: boxed warning on benzodiazepines (2020) and opioid-benzodiazepine combination (2016)","Ashton CH. Benzodiazepines: How They Work and How to Withdraw (The Ashton Manual, 2002)","DEA Controlled Substances schedules","PsychonautWiki, Benzodiazepines"]
BDIS="> Educational harm-reduction content. Not medical advice, not a guide to use. Nothing here gives amounts, preparation, or sourcing. Never stop a daily benzodiazepine suddenly: withdrawal can cause seizures. Counterfeit pills often contain fentanyl or designer benzodiazepines."
def B(slug,name,cls,brands,history,medical,recreational,legal,flavor,ph,routes,skip,od,sources,times=None,cat="benzo",touch=None,met=None):
    D[slug]=dict(name=name,cls=cls,brands=brands,history=history,medical=medical,recreational=recreational,legal=legal,flavor=flavor,ph=ph,routes=routes,skip=skip,od=od,sources=sources+BG,times=times or {},cat=cat,dis=BDIS)
    if touch: D[slug]["touch"]=touch
    if met:
        import med; med.MET[slug]=met
SHORT=lambda o,p,pl,c,a,n: {"oral":[o,"15-45 min",p,pl,c,a,n]}

B("alprazolam","Alprazolam (Xanax)","Triazolobenzodiazepine; short-acting, high-potency.",
"Xanax, Xanax XR, Niravam (orally disintegrating), Alprazolam Intensol. Street: 'bars', 'zannies', 'footballs', 'xannies', 'planks'.",
"Developed by Upjohn (Jackson Hester) in the late 1960s, alprazolam was approved by the FDA in 1981 for anxiety and became the first drug approved for panic disorder. Its fast action made it one of the most prescribed psychiatric drugs in the US. 'Bars' became part of party culture and hip-hop in the 2000s and 2010s. Many street 'Xanax' bars today are counterfeits containing bromazolam, other designer benzos, or fentanyl.",
"Anxiety and panic disorder.","Widely misused for calm and disinhibition, often combined with alcohol or opioids.","US Schedule IV. UK Class C (not prescribable on the NHS).",
["Xanax is described as a fast, clean wave of calm: the 'volume knob' on anxiety turned down, chest tightness gone, racing thoughts slowed. Recreationally, people describe a warm, carefree, disinhibited state, compared to being pleasantly drunk without nausea. It is less sleepy than many benzos at first but more amnesic.",
"Its hallmark is blackout: people act fairly normal to others but later remember nothing, sometimes doing risky or out-of-character things. Because it is short-acting, the comedown brings rebound anxiety and irritability, which drives repeated use."],
["Alprazolam usually begins within 15 to 30 minutes of swallowing: a softening of tension, shoulders dropping, and breathing that feels easier.","Within the next 15 to 30 minutes, calm deepens and worries lose their grip. People feel loose, talkative, and unconcerned. Coordination slips.","The peak, around 1 to 2 hours, brings strong relaxation, mild euphoria, and disinhibition. Speech can slur, balance worsens, and memory begins to drop out.","The plateau is a few hours of calm, sleepy, and sometimes foggy state.","Effects last about 6 to 8 hours in total for immediate-release (PsychonautWiki). Rebound anxiety, irritability, and low mood can arrive sharply.","After-effects include grogginess, memory gaps, and sometimes a 'benzo hangover'.","After regular use, interdose withdrawal is common: anxiety between doses. Stopping suddenly after daily use can cause seizures."],
{"oral":"Immediate-release and extended-release tablets, orally disintegrating tablets, oral concentrate.","sublingual-buccal":"Sometimes used under the tongue; orally disintegrating tablets dissolve in the mouth.","intranasal":"Misused by snorting."},
"No injected, rectal, transdermal, or smoked medical forms.",
"Alone, alprazolam overdose causes deep sedation and confusion. With opioids or alcohol, it is a leading contributor to overdose deaths. Withdrawal seizures are a particular risk because it is short-acting and potent. Counterfeit 'bars' may contain fentanyl.",
["FDA label, Xanax (DailyMed)","Ait-Daoud N, et al. A review of alprazolam use, misuse, and withdrawal (J Addict Med, 2018)"],
times={"oral":["15-30 min","50-90 min","1-2 h","2-4 h","6-8 h total","8-24 h","next day"]},
touch="Per the DailyMed Xanax label, the lower strengths are small oval, scored tablets imprinted 'XANAX'; Xanax and generic alprazolam come as small oval tablets in lower strengths and as long, rectangular 'bars' scored into four sections in the highest immediate-release strength; bars feel like a thin stick with three grooves. Extended-release tablets are triangular or pentagonal. Orally disintegrating tablets crumble on the tongue.",
met="Alprazolam is metabolized by CYP3A4; half-life about 11 hours, and drugs that block CYP3A4 (such as some antifungals and HIV medicines) raise its levels.")

B("diazepam","Diazepam (Valium)","Long-acting benzodiazepine with an active metabolite (desmethyldiazepam) that lasts for days.",
"Valium, Diastat (rectal gel), Valtoco (nasal spray), Libervant (buccal film), Stesolid (Europe).",
"Leo Sternbach at Hoffmann-La Roche created diazepam in 1959, after chlordiazepoxide; it was approved in 1963. From 1968 to 1982 it was the most prescribed drug in the US. The Rolling Stones song 'Mother's Little Helper' (1966) and the 1970s backlash over over-prescription to women made it a cultural symbol.",
"Anxiety, muscle spasm, alcohol withdrawal, seizures (rectal and nasal forms for clusters), and sedation before procedures. Also used to taper people off other benzodiazepines because it lasts so long.",
"Misused for relaxation and to ease comedowns from stimulants.","US Schedule IV. UK Class C.",
["Valium is described as a heavy, warm, body-relaxing calm, more physical than Xanax: muscles melt, the body feels heavy and comfortable, and anxiety fades gradually. It is less sharp and less euphoric, with a gentler, longer arc.","Because it lasts so long, people describe a smooth landing with little rebound, but grogginess can continue into the next day."],
["Swallowed, diazepam starts within 15 to 45 minutes: muscle tension loosens first.","Calm and heaviness build together.","The peak, around 1 to 1.5 hours, is a deep physical relaxation and mental calm.","A long plateau of several hours, with drowsiness.","Fades slowly over many hours.","Next-day sleepiness and slowed reactions are common.","Its active metabolite remains for days. Stopping after regular use causes slower-onset but long withdrawal."],
{"oral":"Tablets and solution.","rectal":"Diastat rectal gel for seizure clusters.","intranasal":"Valtoco nasal spray for seizure clusters.","sublingual-buccal":"Libervant buccal film for seizure clusters.","injected":"IV/IM in hospitals for seizures and alcohol withdrawal."},
"No transdermal or smoked forms.",
"Builds up over days, especially in older adults, causing falls and confusion. Dangerous with opioids and alcohol.",
["FDA label, Valium (DailyMed)","Sternbach LH. The benzodiazepine story (J Med Chem, 1979)"],
times={"oral":["20-40 min","30-60 min","1-1.5 h","2-6 h","6-12 h","12-48 h","still active"],"rectal":["5-15 min","10-20 min","30-60 min","1-4 h","4-12 h","12-48 h","still active"],"intranasal":["5-15 min","10-20 min","30-90 min","1-4 h","4-12 h","12-48 h","still active"],"injected":["IV 1-5 min","under 5 min","IV 5-15 min","30 min-2 h","2-6 h","12-48 h","still active"],"sublingual-buccal":["10-20 min","20-40 min","1 h","1-4 h","4-12 h","12-48 h","still active"]},
touch="Per the DailyMed Valium label, Valium tablets are round, flat-faced, with beveled edges and a V-shaped perforation (a cut-out you can feel), scored vertically on the back. Generics are small, round, scored tablets.",
met="Diazepam is metabolized by CYP3A4 and CYP2C19 into desmethyldiazepam (half-life up to 100 hours); diazepam's own half-life is 20 to 50 hours.")

B("clonazepam","Clonazepam (Klonopin)","Long-acting, high-potency benzodiazepine.",
"Klonopin, Rivotril, Klonopin wafers (discontinued). Street: 'K-pins', 'pins'.",
"Patented by Roche in 1960s, approved for seizures in 1975, and later for panic disorder in 1997.",
"Seizure disorders, panic disorder, and off-label for REM sleep behavior disorder and restless legs.",
"Misused for calm and to soften stimulant or opioid withdrawal.","US Schedule IV. UK Class C.",
["Klonopin is described as a long, steady, flat calm, less euphoric than Xanax, with a slow onset and a gradual fade. People say it 'takes the edge off' all day.","Memory loss and dulled emotions can occur; some describe feeling 'flattened'."],
["Begins 20 to 60 minutes after swallowing, slowly.","A quiet, gradual calm.","Peak at 1 to 4 hours: relaxed, sleepy, steady.","Long plateau of 6 to 12 hours.","Slow fade over the day.","Next-day drowsiness possible.","Daily use leads to dependence; withdrawal is slow-onset and can include seizures."],
{"oral":"Tablets and orally disintegrating tablets.","sublingual-buccal":"Orally disintegrating tablets dissolve in the mouth."},"No other medical routes in the US.",
"Long half-life means accumulation; dangerous with opioids and alcohol. Withdrawal seizures if stopped suddenly.",
["FDA label, Klonopin (DailyMed)"],
times={"oral":["20-60 min","1-2 h","1-4 h","6-12 h","12-24 h","1-2 days","still active"]},
touch="Klonopin tablets are small and round with a 'K'-shaped cut-out through the center on the brand; generics are small, round, and scored. Orally disintegrating tablets are round and dissolve quickly.",
met="Clonazepam is metabolized by CYP3A4; half-life 30 to 40 hours.")

B("lorazepam","Lorazepam (Ativan)","Intermediate-acting benzodiazepine processed without CYP enzymes.",
"Ativan, Loreev XR, Temesta (Europe).","Introduced by Wyeth in 1977.",
"Anxiety, status epilepticus (IV), alcohol withdrawal, sedation before procedures, and nausea from chemotherapy.",
"Misused for calm and sleep.","US Schedule IV. UK Class C.",
["Ativan is described as a heavy, sleepy, very calming effect, more sedating than Xanax and strongly amnesic. People in hospitals often remember little of procedures done under it.","Its euphoria is mild; the main feeling is safety and sleepiness."],
["Begins 20 to 40 minutes after swallowing, faster under the tongue.","Sleepiness and calm build.","Peak at about 2 hours: heavy sedation and relaxation.","Plateau of several hours.","Effects last about 8 to 12 hours in total.","Grogginess and memory gaps.","Daily use leads to dependence and potentially dangerous withdrawal."],
{"oral":"Tablets, liquid, extended-release capsules.","sublingual-buccal":"Tablets are given under the tongue in some countries and hospitals.","injected":"IV/IM for seizures and sedation."},"No other routes.",
"Strong amnesia and sedation; dangerous with opioids and alcohol. IV use requires breathing monitoring.",
["FDA label, Ativan (DailyMed)"],
times={"oral":["20-40 min","30-60 min","1.5-2.5 h","2-8 h","8-12 h total","12-24 h","next day"],"injected":["IV 1-5 min","5-10 min","10-20 min","1-6 h","6-8 h","8-24 h","next day"],"sublingual-buccal":["10-20 min","20-40 min","1 h","2-6 h","6-8 h","8-24 h","next day"]},
touch="Ativan tablets are small, five-sided (pentagonal) tablets; generics are small and round or five-sided, often scored.",
met="Lorazepam is glucuronidated in the liver without CYP enzymes, so it is less affected by liver disease and drug interactions; half-life 10 to 20 hours.")

B("chlordiazepoxide","Chlordiazepoxide (Librium)","The first benzodiazepine; long-acting with active metabolites.",
"Librium, Librax (with clidinium), Limbitrol (with amitriptyline).",
"Leo Sternbach at Roche synthesized it in 1955 and it was discovered to be calming in 1957 when a forgotten compound was tested. Approved in 1960, it launched the benzodiazepine era and quickly replaced barbiturates and meprobamate.",
"Alcohol withdrawal (its main use today) and anxiety.","Little recreational use today.","US Schedule IV.",
["Librium is described as a slow, mild, heavy calm, less euphoric than newer benzos. People often call it 'old-fashioned' and sleepy.","Its long-lasting metabolites give a smooth, extended effect."],
["Begins 30 to 60 minutes after swallowing.","Slow build of relaxation.","Mild peak at 1 to 4 hours.","Long plateau.","Very slow fade.","Next-day sleepiness.","Long-lasting metabolites make withdrawal slow-onset."],
{"oral":"Capsules.","injected":"IM/IV (discontinued in the US)."},"Other routes not used.",
"Accumulation in older adults and those with liver disease. Dangerous with alcohol, which is especially relevant given its use in alcohol withdrawal.",
["FDA label, Librium","Sternbach LH. The benzodiazepine story (1979)"],
times={"oral":["30-60 min","1-2 h","1-4 h","4-12 h","12-48 h","1-3 days","still active"]},
touch="Librium capsules are two-piece capsules, smooth and slightly slippery.")

for slug,name,brand,hist,med,tim,touchs in [
("temazepam","Temazepam (Restoril)","Restoril, Normison, Euhypnos. Street: 'jellies', 'eggs', 'temazzies'.","Introduced in the 1960s and 1970s. In the UK in the 1980s and 1990s, gel-filled capsules were melted and injected, causing gangrene and amputations, and the gel capsules were withdrawn in 1996.","Insomnia.",["20-60 min","30-60 min","1-2 h","2-6 h","6-8 h","8-24 h","next day"],"Restoril is a two-piece capsule."),
("triazolam","Triazolam (Halcion)","Halcion.","Approved in the US in 1982. It became controversial in the early 1990s over reports of amnesia, confusion, and bizarre behavior, and was banned in the UK in 1993.","Short-term insomnia and dental sedation.",["15-30 min","30 min","1-2 h","1-3 h","2-4 h","4-12 h","next day"],"Halcion tablets are small, oval, and scored."),
("oxazepam","Oxazepam (Serax)","Serax (discontinued US brand), Serepax.","Introduced in 1965 as a metabolite of diazepam.","Anxiety and alcohol withdrawal, especially in liver disease.",["45-90 min","1-2 h","2-3 h","3-6 h","6-12 h","12-24 h","next day"],"Capsules and tablets."),
("clorazepate","Clorazepate (Tranxene)","Tranxene T-Tab.","Approved in 1972; a prodrug turned into desmethyldiazepam in the stomach.","Anxiety, seizures, alcohol withdrawal.",["30-60 min","1 h","1-2 h","2-8 h","8-24 h","1-3 days","still active"],"Tablets, often with a 'T' shape on the brand."),
("flurazepam","Flurazepam (Dalmane)","Dalmane.","Approved in 1970, one of the first benzodiazepine sleeping pills.","Insomnia.",["15-45 min","30-60 min","1-2 h","2-8 h","8-12 h","1-3 days","still active"],"Capsules."),
("estazolam","Estazolam (ProSom)","ProSom (discontinued brand).","Approved in the US in 1990.","Insomnia.",["30-60 min","1 h","2 h","2-6 h","6-10 h","10-24 h","next day"],"Small tablets, scored."),
("quazepam","Quazepam (Doral)","Doral.","Approved in 1985.","Insomnia.",["30-60 min","1-2 h","2 h","2-8 h","8-12 h","1-3 days","still active"],"Tablets."),
("midazolam","Midazolam (Versed)","Versed, Seizalam, Nayzilam (nasal spray), Buccolam (Europe).","Synthesized by Roche in 1975 and introduced in 1982; now the most widely used sedative for procedures.","Sedation for procedures and surgery, status epilepticus, and seizure clusters (nasal).",["IV 1-5 min","under 5 min","IV 3-5 min","15-60 min","1-2 h","2-6 h","next day"],"Mostly an injection or nasal spray; the oral syrup is used for children."),
("remimazolam","Remimazolam (Byfavo)","Byfavo.","Approved by the FDA in 2020; designed to be broken down quickly by blood enzymes.","Sedation for short procedures.",["IV 1-3 min","1-2 min","2-5 min","10-20 min","under 30 min","1-2 h","next day"],"Powder for injection only."),
("flunitrazepam","Flunitrazepam (Rohypnol)","Rohypnol. Street: 'roofies', 'rophies', 'forget-me pill'.","Introduced by Roche in 1975. Became notorious as a 'date-rape drug' in the 1990s; Roche reformulated it to turn drinks blue. Never approved in the US; the US banned import in 1996.","Insomnia and pre-anesthesia in some countries.",["15-30 min","30-60 min","1-2 h","2-8 h","8-12 h","12-24 h","next day"],"Tablets; reformulated tablets release a blue dye in liquids."),
("nitrazepam","Nitrazepam (Mogadon)","Mogadon.","Introduced in 1965.","Insomnia and some childhood epilepsies, mainly in the UK, Europe, and Australia.",["30-60 min","1 h","2 h","2-8 h","8-12 h","1-2 days","still active"],"Small round tablets."),
("bromazepam","Bromazepam (Lexotan)","Lexotan, Lexomil.","Patented by Roche in 1963 and introduced in 1974.","Anxiety, in Europe and Latin America.",["30-60 min","1-2 h","1-4 h","4-8 h","8-20 h","1-2 days","next day"],"Tablets, some cross-scored."),
("clobazam","Clobazam (Onfi)","Onfi, Sympazan (film), Frisium.","Introduced in 1975; approved in the US in 2011 for Lennox-Gastaut syndrome.","Lennox-Gastaut syndrome and other epilepsies; anxiety in some countries.",["30-60 min","1 h","1-4 h","4-12 h","12-36 h","1-3 days","still active"],"Tablets and an oral film."),
("lormetazepam","Lormetazepam (Noctamid)","Noctamid, Loramet.","Introduced in the 1980s in Europe.","Insomnia.",["30-60 min","1 h","1-2 h","2-6 h","6-10 h","10-24 h","next day"],"Tablets."),
("prazepam","Prazepam (Centrax)","Centrax (discontinued in US), Demetrin.","Introduced in the 1970s; a prodrug of desmethyldiazepam.","Anxiety (Europe).",["1-2 h","2-4 h","2-6 h","6-24 h","1-3 days","2-4 days","still active"],"Tablets and capsules."),
("etizolam","Etizolam","Etilaam, Depas, Etizola. Street: sold as 'etiz', in counterfeit pills.","A thienodiazepine (benzo-like, not technically a benzodiazepine) introduced in Japan in 1984. Never approved in the US; sold online as a research chemical and found in counterfeit pills in Scotland and the US.","Anxiety and insomnia in Japan, India, and Italy.",["20-60 min","30-60 min","1-2 h","2-6 h","6-8 h","8-24 h","next day"],"Prescription tablets in India and Japan; street pills vary."),
]:
    B(slug,name,"Benzodiazepine (or benzodiazepine-like drug, for etizolam).",brand,hist,med,
      "Misused for sedation, sleep, calm, or disinhibition, and sometimes to come down from stimulants." + (" Also used in drug-facilitated sexual assault." if slug=="flunitrazepam" else ""),
      "US Schedule IV" + (" (flunitrazepam is not approved; treated as Schedule IV with Schedule I penalties)." if slug=="flunitrazepam" else (" (etizolam is Schedule I since 2022)." if slug=="etizolam" else ".")),
      [f"{name.split(' (')[0]} is described as producing classic benzodiazepine effects: calm, relaxed muscles, lowered inhibition, and sleepiness. People rarely describe strong euphoria; the core experience is relief and heaviness.",
       "Memory loss is a central effect: people often don't remember the later part of the experience. Compared with other benzos, its character depends mainly on how fast it acts and how long it lasts (see the timeline)."],
      ["Onset begins with loosening tension and a gentle heaviness.","Relaxation and drowsiness build.","Peak: strong calm, sedation, and reduced coordination; memory gaps begin.","Plateau of sedation and calm.","Effects fade; short-acting ones can bring rebound anxiety or insomnia.","Grogginess, memory gaps, impaired driving.","After daily use, stopping can cause dangerous withdrawal including seizures."],
      {"oral":"Tablets or capsules."} | ({"injected":"IV/IM in hospitals.","intranasal":"Nasal spray for seizures.","sublingual-buccal":"Buccal solution (Europe)."} if slug=="midazolam" else {}) | ({"injected":"IV in hospitals only."} if slug=="remimazolam" else {}),
      "Other routes are not used medically.",
      "Dangerous with opioids and alcohol; can cause blackouts, falls, and stopped breathing in combination." + (" Flunitrazepam is strongly sedating and amnesic." if slug=="flunitrazepam" else "") + (" Withdrawal seizures if stopped suddenly after daily use." ),
      [f"FDA or national label, {name}"],times={"oral" if slug not in("midazolam","remimazolam") else "injected":tim},touch=touchs)
D["remimazolam"]["routes"]={"injected":"IV in hospitals only."}
