from gen import *
G=["Goodman & Gilman's The Pharmacological Basis of Therapeutics (opioid chapter)","National Institute on Drug Abuse (nida.nih.gov)","DEA Controlled Substances schedules (dea.gov)"]
def R(slug,name,cls,brands,history,medical,recreational,legal,flavor,ph,routes,skip,od,sources,times=None,**k):
    D[slug]=dict(name=name,cls=cls,brands=brands,history=history,medical=medical,recreational=recreational,legal=legal,flavor=flavor,ph=ph,routes=routes,skip=skip,od=od,sources=sources+G,times=times or {},cat="opioid",**k)

R("meperidine","Meperidine (pethidine, Demerol)","Synthetic phenylpiperidine opioid; full mu agonist with anticholinergic and serotonergic effects.",
"Demerol, Pethidine, Meperitab, Dolantin (Germany).",
"Synthesized in 1938 by Otto Eisleb at IG Farben, originally as an anticholinergic; Otto Schaumann noticed its painkilling effect. It was the most-used hospital opioid in the US for decades, especially in childbirth, because it was wrongly believed to cause less spasm and less addiction than morphine.",
"Once routine for labor, post-surgical pain, and shivering after anesthesia. Today largely abandoned, because its metabolite normeperidine builds up and causes tremor, agitation, and seizures. Still used occasionally for post-anesthesia shivering.",
"Demerol addiction was common among doctors and nurses with access to it. A 1984 case, the death of Libby Zion after meperidine was given with the antidepressant phenelzine, led to reforms in resident doctors' work hours. In 1982, a botched attempt to make an illicit meperidine analog (MPPP) produced MPTP, which gave several young people permanent Parkinson's disease.",
"US Schedule II.",
["Meperidine is described as a short, buzzy, slightly heady opioid high, with a spinning, light-headed, almost dizzy quality and less of the heavy, dreamy warmth of morphine. Some describe a mild stimulant edge, dry mouth, and racing heart from its anticholinergic effect.",
"People who have had it in hospital often recall a rush of pleasant floatiness that faded fast. Unlike most opioids, it often does not shrink the pupils much, and with repeated use it can cause shakiness, twitching, and anxiety instead of calm."],
["Injected meperidine works within a minute or two; swallowed, within 15 to 45 minutes. The first sensation is often a light-headed, spinning warmth.",
"The come-up feels quick and heady: a wave of floaty well-being with dry mouth and a flushed face. Some feel a little dizzy or nauseous.",
"The peak is brief and pleasant, a buzzy euphoria with reduced pain and anxiety, but less body heaviness than morphine.",
"The plateau is short, roughly 1 to 2 hours. Sedation is moderate; some people feel restless rather than nodding.",
"It wears off within 2 to 4 hours, often leaving people wanting more, which drove frequent redosing in hospital patients.",
"After repeated doses, normeperidine accumulates: tremor, twitching, agitation, anxiety, and in some, seizures. This toxic phase can come after the pleasant effect is long gone.",
"After regular use, withdrawal comes on quickly and is described as harsh, with anxiety and agitation."],
{"injected":"IV, IM, SC in hospitals; its main historic use.","oral":"Tablets and syrup."},
"No intranasal, rectal (rare historic), transdermal, sublingual, or smoked medical forms.",
"Seizures from the normeperidine metabolite, especially with kidney problems or repeated doses; naloxone does not reverse these. Deadly reactions with MAOI antidepressants (serotonin syndrome).",
["FDA label, Demerol (DailyMed)","Latta KS, et al. Meperidine: a critical review (Am J Ther, 2002)","Langston JW, et al. MPTP and parkinsonism (Science, 1983)"])

R("levorphanol","Levorphanol","Synthetic morphinan opioid; mu, kappa, and delta agonist, NMDA antagonist, and serotonin-norepinephrine reuptake inhibitor.",
"Levo-Dromoran (original brand), generic levorphanol tartrate.",
"First described in Germany in 1946 and introduced in the US in 1953 by Roche. It fell out of favor for decades and was rediscovered for difficult nerve pain.",
"Moderate to severe pain, including nerve pain, often when other opioids have failed. Long-acting and can accumulate.",
"Rarely misused, mostly because it is rarely prescribed.",
"US Schedule II.",
["Levorphanol is described as a long, smooth, clear-headed opioid effect with less euphoria than oxycodone and a slightly 'different', sometimes dreamy or dysphoric edge from its kappa activity. Some report odd perceptual effects at higher levels.",
"Its long half-life gives a steady, drawn-out feeling, more like methadone than oxycodone."],
["Swallowed, it begins in about 30 to 60 minutes with a gradual warmth.","The come-up is slow and even, with relaxation and easing of pain.","The peak, around 1 to 2 hours, is a calm, moderate euphoria with some sedation; some people feel slightly detached.","The plateau lasts many hours, often 6 to 15.","The comedown is slow.","Accumulation with repeated doses can cause more sedation over days.","After regular use, withdrawal is slow-onset and long."],
{"oral":"Tablets; the only current US form.","injected":"Injectable form existed historically (discontinued in the US)."},
"No other forms.","Long half-life means accumulation and delayed overdose, similar to methadone.",
["FDA label, levorphanol tartrate (DailyMed)","Gudin J, et al. Levorphanol revisited (J Pain Res, 2016)"],
times={"oral":["30-60 min","1-2 h","1-2 h","6-15 h","15-24 h","1-2 days","still active"]})

for slug,name,brand,hist,med in [
("sufentanil","Sufentanil","Sufenta, Dsuvia (sublingual tablet, discontinued 2024), Zalviso (Europe).","Synthesized by Janssen in 1974; about 5 to 10 times stronger than fentanyl.","Anesthesia, intensive care; Dsuvia was a sublingual tablet for military and supervised settings, approved in 2018 amid controversy over its strength."),
("alfentanil","Alfentanil","Alfenta, Rapifen.","Synthesized by Janssen in 1976.","Short procedures and anesthesia; acts within about a minute and wears off in minutes."),
("remifentanil","Remifentanil","Ultiva.","Developed by Glaxo and approved in 1996; broken down by blood enzymes so it wears off within minutes of stopping.","Anesthesia and intensive care by continuous infusion; also used in labor in some countries.")]:
    R(slug,name,"Synthetic fentanyl-family opioid; very potent full mu agonist used only in medicine.",brand,hist,med,
    "Misuse is mostly limited to healthcare workers with access, and is often fatal.","US Schedule II.",
    [f"{name} is a hospital drug. Patients describe a fast, heavy wave of warmth and sleepiness, sometimes a pleasant floaty detachment before anesthesia, rather than a long euphoria. Its effects are extremely short and very strong.",
     "People who received it rarely remember much; its main 'feeling' is sudden sedation and dulled pain, sometimes with nausea or itch on waking."],
    ["Given IV, it acts within about a minute.","There is little or no come-up.","The peak comes within minutes: heavy sedation and strong pain relief; breathing can stop and chest muscles can stiffen, which is why it is used only with airway support.","The effect lasts only as long as the drug is being given (remifentanil) or for minutes to an hour.","It wears off quickly.","Patients may feel groggy, nauseous, or have more pain as it ends.","Little next-day effect after single medical use."],
    {"injected":"IV in hospitals, with monitoring."} | ({"sublingual-buccal":"Dsuvia tablet (discontinued)."} if slug=="sufentanil" else {}),
    "No oral, intranasal (outside research), rectal, transdermal, or smoked medical forms.",
    "Extremely potent; breathing can stop and chest-wall rigidity occur within a minute. Used only where airway support is ready.",
    [f"FDA label, {name} (DailyMed)","Stanley TH. The fentanyl story (J Pain, 2014)"],
    times={"injected":["under 1 min","seconds","1-5 min","5-30 min (remifentanil ends within minutes of stopping)","under 1 h","1-4 h","next day"],"sublingual-buccal":["10-30 min","15-30 min","30-60 min","1-3 h","3-4 h","4-8 h","next day"]})

for slug,name,brand,hist,routes,extra in [
("butorphanol","Butorphanol","Stadol, Stadol NS (nasal spray), Torbugesic (veterinary).","Developed by Bristol-Myers in 1972; the nasal spray (1991) was widely misused before it was moved to Schedule IV in 1997.",{"intranasal":"Nasal spray, mainly for migraine.","injected":"IV/IM in hospitals and labor."},"The nasal spray was linked to dependence in migraine patients."),
("nalbuphine","Nalbuphine","Nubain.","Developed in the 1960s and approved in 1979.",{"injected":"IV, IM, SC in hospitals."},"Not controlled in the US; sometimes misused by bodybuilders."),
("pentazocine","Pentazocine (Talwin)","Talwin, Talwin NX (with naloxone), Talacen, Fortral (UK).","Developed by Sterling Winthrop in 1958 and marketed in 1967. In the 1970s, 'Ts and Blues' (Talwin with the antihistamine tripelennamine) became a street injection drug in the US Midwest, prompting Talwin NX with naloxone in 1983.",{"oral":"Tablets.","injected":"IM/IV injection (largely discontinued in the US)."},"Injected tablets caused severe skin and muscle damage.")]:
    R(slug,name,"Mixed agonist-antagonist opioid: activates kappa receptors and partly blocks or weakly activates mu receptors, with a ceiling effect.",brand,hist,
    "Moderate to severe pain, labor, and migraine (butorphanol). Rarely used today.",
    f"Less sought after than full agonists because of unpleasant kappa effects. {extra}",
    "Butorphanol and pentazocine US Schedule IV; nalbuphine not controlled.",
    [f"{name} is described as an odd, mixed experience: mild opioid warmth and sedation combined with spacey, dreamlike, or uneasy feelings from kappa receptors, sometimes dysphoria, racing thoughts, or hallucinations. People rarely describe it as purely pleasant.",
     "In people dependent on full opioids, it can trigger withdrawal because it partly blocks the mu receptor."],
    ["Injected, it starts within minutes; nasal spray within about 15 minutes; swallowed within 15 to 30 minutes. Often a light-headed, floaty start.","The come-up brings sleepiness, a 'drunk' or detached feeling, and sometimes dizziness or sweating.","The peak combines pain relief and sedation with dreaminess; some feel anxiety, strange thoughts, or vivid imagery.","The plateau is sedated and spacey, lasting a few hours.","It fades over 3 to 6 hours.","Some feel hungover, dizzy, or low.","Next day is usually normal after single use."],
    routes,"Other routes are not used medically.",
    "Has a ceiling on breathing suppression alone, but is dangerous with other sedatives. Can cause hallucinations and precipitate withdrawal in people dependent on other opioids.",
    [f"FDA label, {name} (DailyMed)","Senay EC. 'Ts and Blues' (Drug Alcohol Depend, 1985)"])

R("propoxyphene","Propoxyphene (Darvon, Darvocet)","Synthetic opioid related to methadone; weak mu agonist whose metabolite norpropoxyphene is toxic to the heart.",
"Darvon, Darvocet (with acetaminophen), Darvon-N, Distalgesic and Co-proxamol (UK).",
"Introduced by Eli Lilly in 1957 and once one of the most prescribed painkillers in the US. The UK withdrew co-proxamol in 2005 over suicide overdoses, and the FDA had it withdrawn in November 2010 after finding it disrupts heart rhythm even at normal doses.",
"No longer used. Withdrawn worldwide.",
"Commonly misused in the 1960s to 1980s; Darvon was implicated in many overdose deaths.",
"US Schedule IV (no longer marketed).",
["Propoxyphene was described as a weak, mild opioid buzz: light warmth and relaxation, often barely more than acetaminophen alone. Its danger far outweighed its effect.","People recalled it as sleepy and dull rather than euphoric."],
["Effects began 30 to 60 minutes after swallowing.","A gentle warmth and drowsiness.","A mild calm peaking around 2 hours.","Mild sedation for a few hours.","Faded over 4 to 6 hours.","Its metabolite stayed much longer, affecting the heart.","Mild next-day grogginess."],
{"oral":"Capsules and tablets (withdrawn)."},"Oral only.",
"Heart rhythm disturbances and rapid death in overdose, which naloxone could not fully reverse. Combination products added acetaminophen liver toxicity.",
["FDA 2010 announcement on propoxyphene withdrawal","UK MHRA, co-proxamol withdrawal (2005)"])

R("dihydrocodeine","Dihydrocodeine","Semi-synthetic opioid close to codeine, somewhat stronger.",
"DF118, DHC Continus (UK), Synalgos-DC and Trezix (US, with caffeine and acetaminophen), Paracodin.",
"Developed in Germany in 1908 and marketed from 1911. Widely used in the UK and Europe.",
"Moderate pain and cough. In Germany and Austria it was used in the 1990s as an informal substitution treatment for heroin addiction.",
"Misused like codeine, especially in Europe.",
"US Schedule II (Schedule III in combinations). UK Class B.",
["Dihydrocodeine feels much like codeine but a little stronger and more consistent, with gentle warmth, mild euphoria, sleepiness, and notable itch.","Some describe a slightly more 'pins and needles' itchy body feeling than codeine."],
["Effects start 30 to 45 minutes after swallowing.","Warmth and relaxation build gently.","Mild to moderate euphoria peaks around 1 to 2 hours.","Drowsy calm for a few hours.","Fades over 4 to 6 hours.","Constipation and itch.","Mostly normal next day."],
{"oral":"Tablets and syrups.","injected":"Injectable form exists in some countries."},"No other routes.",
"Similar to codeine; combination products add acetaminophen risk.",["UK BNF, dihydrocodeine","PsychonautWiki, Dihydrocodeine"])

R("opium","Opium, laudanum, and paregoric","Dried latex of the opium poppy (Papaver somniferum), containing morphine, codeine, thebaine, papaverine, and noscapine. Laudanum is a tincture of opium in alcohol; paregoric is camphorated tincture of opium.",
"Laudanum (Opium Tincture USP), Paregoric, Dover's Powder (historical). Street: 'O', 'black tar' is a different product (heroin).",
"Opium was used in Mesopotamia by 3400 BCE and in ancient Egypt, Greece, and Rome. Paracelsus popularized laudanum in the 1500s, and Thomas Sydenham standardized it in 1676. In the 1800s, laudanum was sold freely and given to babies in 'soothing syrups'. Britain fought the Opium Wars (1839 to 1842 and 1856 to 1860) to force China to accept opium imports. Writers like Thomas De Quincey ('Confessions of an English Opium-Eater', 1821) and Samuel Taylor Coleridge described its effects.",
"Today, opium tincture and paregoric are still prescribed in the US for severe diarrhea.",
"Opium smoking was common in 19th-century China and in Chinese immigrant communities in the US, leading to the first US anti-drug law (San Francisco, 1875). Opium is still used traditionally and recreationally in Iran, Afghanistan, and India.",
"Opium tincture US Schedule II; paregoric Schedule III. Raw opium is illegal in most countries.",
["Opium's effect is described as gentler, dreamier, and more 'rounded' than pure morphine, because it contains several alkaloids. People describe a pleasant, reverie-like state, vivid daydreams, and a sense of peaceful detachment. De Quincey called it 'the true hero of the tale' for its calm.","Smoked opium is described as light, relaxing, and social; swallowed opium is heavier and longer, with more nausea."],
["Smoked: within seconds to minutes; swallowed: 30 to 60 minutes. A soft warmth and loosening.","Dreamy relaxation builds, with itch and some nausea.","A peaceful, contemplative euphoria, rich daydream imagery.","Long reverie and light nodding.","Gradual fade over several hours.","Constipation, dry mouth, and lethargy.","After regular use, typical opioid withdrawal."],
{"oral":"Laudanum and paregoric tinctures; traditional eating of opium.","inhaled-smoked":"Traditional opium smoking."},"No modern injected or other forms.",
"Strength varies widely between batches. Laudanum contains much more morphine than paregoric, and confusing the two has caused deaths.",
["FDA label, Opium Tincture USP","Booth M. Opium: A History (1996)","De Quincey T. Confessions of an English Opium-Eater (1821)"],
times={"inhaled-smoked":["seconds-5 min","5-15 min","15-45 min","1-3 h","3-5 h","5-12 h","next day"]})

R("diphenoxylate","Diphenoxylate (Lomotil)","Synthetic opioid related to meperidine that acts mostly in the gut; combined with atropine to discourage misuse.",
"Lomotil, Lonox; difenoxin (Motofen) is its active metabolite.","Developed by Janssen in 1956.","Diarrhea.","Rarely misused because atropine causes unpleasant effects and little reaches the brain at medical amounts.","US Schedule V (with atropine).",
["At medical amounts there is little or no high. Misuse mostly produces atropine effects: dry mouth, flushed hot skin, fast heartbeat, blurry vision, and confusion, with only a faint opioid calm.","It is mainly dangerous for children, who can be poisoned by small numbers of tablets."],
["Swallowed, effects begin in 45 to 60 minutes.","Mild drowsiness, dry mouth.","Slight calm; atropine effects dominate.","Several hours of drowsiness.","Fades over 3 to 4 hours.","Dry mouth, constipation.","Normal next day."],
{"oral":"Tablets and liquid."},"Oral only.","Children can have delayed breathing suppression up to 12 hours or more after swallowing; atropine poisoning too.",["FDA label, Lomotil"])

R("levomethadyl","Levomethadyl acetate (LAAM)","Synthetic opioid related to methadone, with even longer action.","ORLAAM.","Approved by the FDA in 1993 for opioid addiction treatment, allowing dosing three times a week. Withdrawn in the US in 2003 and Europe in 2001 after reports of fatal heart rhythm problems.","Formerly for opioid use disorder; no longer available.","Not commonly misused.","US Schedule II (not marketed).",
["Like methadone, LAAM produced little euphoria at stable treatment doses, instead a steady, normal feeling lasting 2 to 3 days.","People who tried it described it as smooth and long, with slow onset."],
["Slow onset over hours.","Gradual relief of withdrawal.","Mild, flat peak.","Plateau of 48 to 72 hours.","Very gradual fade.","Sweating, constipation.","Still active for days."],
{"oral":"Liquid at treatment clinics."},"Oral only.","Fatal heart rhythm disturbances (QT prolongation); very long, delayed effect.",["FDA safety communication on ORLAAM (2001-2003)"],
times={"oral":["1-4 h","4-8 h","8-12 h","1-3 days","2-3 days","3+ days","still active"]})

for slug,name,cls,brand,hist,legal,routes in [
("dextromoramide","Dextromoramide","Synthetic opioid related to methadone, fast and short-acting, about three times stronger than morphine.","Palfium, Jetrium.","Discovered by Janssen in 1956. Used in the UK and Netherlands; withdrawn in the UK in 2004.","US Schedule I; UK Class A.",{"oral":"Tablets.","sublingual-buccal":"Tablets were often used under the tongue.","rectal":"Suppositories."}),
("dipipanone","Dipipanone","Synthetic opioid related to methadone, sold with the antiemetic cyclizine.","Diconal (UK).","Introduced in the UK in the 1950s. In the 1980s, injected Diconal was misused in the UK, causing serious harm from cyclizine.","US Schedule I; UK Class A.",{"oral":"Tablets (Diconal)."}),
("piritramide","Piritramide","Synthetic opioid used in hospitals.","Dipidolor.","Developed by Janssen in 1960; used mainly in Germany, Belgium, the Netherlands, and Austria.","Not used in US (Schedule I); controlled in Europe.",{"injected":"IV/IM in hospitals, often by patient-controlled pumps."}),
("ethylmorphine","Ethylmorphine","Semi-synthetic opioid similar to codeine.","Dionin, Cosylan.","Introduced by Merck in 1884. Used in Scandinavia and elsewhere for cough and pain.","US Schedule II.",{"oral":"Tablets and syrups."}),
("nicomorphine","Nicomorphine","Semi-synthetic opioid, the dinicotinic ester of morphine.","Vilan.","Patented in 1904 and used in parts of Europe for pain.","US Schedule I.",{"injected":"Injection.","rectal":"Suppositories.","oral":"Tablets."}),
("dihydromorphine","Dihydromorphine","Semi-synthetic opioid close to morphine, slightly stronger.","Paramorfan.","Developed in Germany in 1900.","US Schedule I.",{"injected":"Injection (historical).","oral":"Tablets (historical)."}),
("anileridine","Anileridine","Synthetic opioid related to meperidine.","Leritine.","Developed by Merck in the 1950s; discontinued in the US and Canada.","US Schedule II (not marketed).",{"oral":"Tablets (discontinued).","injected":"Injection (discontinued)."}),
("alphaprodine","Alphaprodine","Synthetic opioid related to meperidine, rapid and short-acting.","Nisentil.","Introduced in the 1940s by Roche and used in childbirth and dentistry; withdrawn in the US in 1986.","US Schedule II (not marketed).",{"injected":"Injection (discontinued)."}),
("benzhydrocodone","Benzhydrocodone","Prodrug of hydrocodone, sold with acetaminophen.","Apadaz.","Approved by the FDA in 2018.","US Schedule II.",{"oral":"Tablets."}),
("meptazinol","Meptazinol","Partial mu-opioid agonist.","Meptid.","Developed in the UK in the 1970s.","Not controlled in the UK.",{"oral":"Tablets.","injected":"Injection."}),
("dezocine","Dezocine","Mixed agonist-antagonist opioid.","Dalgan.","Approved in the US in 1986 and discontinued; widely used in China.","Not controlled in US.",{"injected":"Injection."}),
]:
    R(slug,name,cls,brand,hist,"Moderate to severe pain or cough (depending on the drug); many are now rarely used or discontinued.",
    "Rare; mostly limited to people with access in the countries where it is or was sold.",legal,
    [f"Information on what {name} feels like is limited to older clinical descriptions and a small number of reports. It is generally described as producing classic opioid effects: warmth, relaxation, pain relief, and drowsiness, with euphoria similar to other drugs in its family.",
     "Because it is rare, there are few trustworthy descriptions, and anything sold under this name outside a pharmacy is likely to be something else, often fentanyl."],
    ["Onset depends on route: minutes when injected, 15 to 45 minutes swallowed.","A warm, relaxing build.","Typical opioid peak of calm, contentment, and pain relief.","Sedation and possible nodding.","Gradual fade over several hours.","Constipation and drowsiness.","Typical opioid withdrawal after regular use."],
    routes,"Other routes not used.","Standard opioid overdose risk; data is limited.",[f"Drug monographs for {name} (WHO, national formularies)"],
    reduced=True)
