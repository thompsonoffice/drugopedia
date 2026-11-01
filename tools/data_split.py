# Split pages where drugs differ meaningfully.
from gen import D
from data_new import X,t,CW,SR
# --- methylone page now methylone only
m=D["methylone"]; m["name"]="Methylone (bk-MDMA)"; m["brands"]="Methylone, bk-MDMA, M1; often sold as 'molly'."
m["history"]="Methylone was patented by Peyton Jacob and Alexander Shulgin in 1996 as a possible antidepressant and sold in the Netherlands as 'Explosion' around 2004. It was one of the most common substitutes in US 'molly' in the early 2010s."
m["legal"]="US Schedule I (2013); UN 1971 Convention Schedule II (2015)."
m["flavor"]=["Methylone feels like a weaker, shorter MDMA: euphoria, empathy and energy, with more stimulation and less emotional warmth.","Its effects arrive and fade faster than MDMA, which tempts redosing.","People expecting MDMA may take more when it feels different, raising risks of overheating, seizures and low blood sodium."]
m["ph"]=["Swallowed, methylone begins within 15 to 45 minutes.","A quick rise of energy and mild euphoria.","Peak around 1 to 1.5 hours, with sociability and stimulation.","Effects last about 2 to 3 hours.","A fairly quick comedown, sometimes with anxiety.","Insomnia and tiredness.","Low mood the next day."]
m["times"]={"oral":t("15-45 min","30-60 min","1-1.5 h","2-3 h","3-5 h","6-24 h","next day")}
D["other-cathinones"]["name"]="Other synthetic cathinones (N-ethylpentylone, 4-MEC, pentedrone, hexen, alpha-PHP and others)"
D["other-cathinones"]["brands"]="N-ethylpentylone (ephylone), 4-MEC, pentedrone, N-ethylhexedrone (hexen), alpha-PHP."
X("eutylone","Eutylone (bk-EBDB)","cath","Synthetic cathinone with stimulant and MDMA-like effects.","Eutylone, bk-EBDB; sold as 'molly', 'ecstasy' or bath salts.",
"Eutylone appeared on drug markets around 2014 and, after N-ethylpentylone was controlled, became the most common synthetic cathinone identified in US drug seizures and 'molly' samples around 2019 to 2021.","None.","Mostly taken unknowingly by people who believed they bought MDMA.","US Schedule I (temporary 2020, then permanent); UN 1971 Convention Schedule II (2022).",
["Eutylone is more stimulating and less empathetic than MDMA: wired energy, racing thoughts and a short euphoria followed by a strong urge to take more.","Long-lasting insomnia, anxiety, sweating, teeth grinding and a racing heart are common; many describe it as 'MDMA that keeps you up all night without the love'.","Emergency reports describe agitation, overheating, seizures and deaths, often when people redosed because they thought the 'MDMA' was weak."],
["Swallowed, effects begin within 30 to 60 minutes.","Stimulation rises faster than euphoria.","Peak around 1 to 2 hours: energy, restlessness, jaw clenching.","Stimulant effects continue for several hours.","A long, wakeful comedown with anxiety.","Insomnia lasting into the next night.","Fatigue and low mood for a day or two."],
{"oral":t("30-60 min","about 1 h","1-2 h","3-6 h","6-12 h","12-36 h","next 1-2 days")},{"oral":"Capsules, crystals, or pressed pills sold as MDMA."},
"Eutylone toxicity causes agitation, overheating, seizures, heart rhythm problems and death.","Off-white crystals or capsules indistinguishable from 'molly'."+CW,
"Eutylone inhibits dopamine and noradrenaline reuptake more strongly than it releases serotonin, which is why it feels more stimulating than MDMA.",
src=["DEA temporary scheduling order for N-ethylhexedrone, eutylone and others (2019-2020)","Krotulski AJ. et al. Eutylone intoxications. J Anal Toxicol 2021"])
X("3-mmc","3-MMC (3-methylmethcathinone)","cath","Synthetic cathinone, a positional isomer of mephedrone.","3-MMC, metaphedrone; often bought online in Europe.",
"3-MMC appeared in 2011 after mephedrone was banned, and became especially popular in the Netherlands and in European chemsex settings until it was controlled there in 2021.","None.","Popular for sociability and sexual arousal; often redosed through a night.","UN 1971 Convention Schedule II (2022); controlled across the EU; US analog laws apply.",
["3-MMC is milder and more 'social' than mephedrone: talkativeness, a gentle euphoria, energy and arousal, with less intense rush.","Its short duration leads to frequent redosing, which brings a racing heart, sweating, insomnia and anxiety.","Heavy use is linked to compulsive use, kidney injury, paranoia and, rarely, deaths, particularly with other drugs."],
["Swallowed or snorted, effects begin within 15 to 45 minutes.","Sociability and energy rise.","Peak at about 1 hour.","Effects last 2 to 3 hours.","A comedown with craving.","Insomnia and anxiety.","Low mood and fatigue next day."],
{"oral":t("15-45 min","30-60 min","about 1 h","2-3 h","3-5 h","6-12 h","next day"),"intranasal":t("5-15 min","15-30 min","30-60 min","1-2 h","2-4 h","6-12 h","next day")},{"oral":"Swallowed.","intranasal":"Snorted."},
"Toxicity causes overheating, fast heart rate, agitation and seizures.","White crystals or powder."+CW,"3-MMC releases dopamine and noradrenaline more than serotonin.",src=["WHO ECDD critical review: 3-MMC (2021)","EMCDDA risk assessment of 3-MMC (2021)"])
# --- hemp cannabinoids split
d8=D["delta-8-thc"]; d8["name"]="Delta-8-THC"; d8["brands"]="Delta-8, D8; sold as gummies, vapes and 'diet weed' in gas stations and online."
d8["flavor"]=["Delta-8 feels like a milder, clearer version of ordinary THC: relaxed, mildly euphoric and sleepy, with less anxiety for many people.","It occurs naturally only in tiny amounts, so commercial delta-8 is made by chemically converting hemp CBD; leftover acids, solvents and by-products are a concern.","Products are often mislabeled and may contain delta-9-THC or other cannabinoids. Poison centers report many child exposures."]
X("thc-o","THC-O acetate","cann","Acetylated THC, a synthetic cannabinoid made from hemp-derived THC.","THC-O, THCO, 'the psychedelic cannabinoid'.",
"THC acetate was studied by the US military in the 1950s and turned up in a few clandestine labs. It was marketed widely after 2020 as a 'legal' hemp product.","None.","Marketed as stronger and 'more psychedelic' than THC.","The DEA stated in 2023 that THC-O is a Schedule I controlled substance because it does not occur naturally in hemp.",
["THC-O is a prodrug: the body removes the acetate group to release THC, so effects start late and feel heavy, sedating and longer-lasting.","Reports of 'psychedelic' effects are mostly anecdotal and probably reflect strength.","Vaping acetate compounds is a concern: heated vitamin E acetate caused EVALI lung injuries, and THC-O acetate can form ketene, a lung toxin, when heated."],
["Effects begin slowly: 20 to 60 minutes vaped, 1 to 2 hours eaten.","A gradual, heavy relaxation.","Peak: strong body heaviness and time distortion.","A long plateau.","Slow fade.","Grogginess.","Next-day fog."],
{"inhaled-smoked":t("20-60 min","30-60 min","1-2 h","2-3 h","3-5 h","5-8 h","next day"),"oral":t("1-2 h","2-3 h","3-5 h","5-7 h","7-10 h","12-24 h","next day")},{"inhaled-smoked":"Vapes.","oral":"Gummies."},
"Too much causes long-lasting confusion, vomiting and anxiety; vaping may injure the lungs.","Usually vape cartridges or gummies."+CW,"THC-O is converted to THC in the body, delaying effects.",
src=["DEA letter on delta-9-THCO and delta-8-THCO (2023)","Munger KR. et al. Ketene from vaping THC-O acetate. PNAS 2022"])
X("hhc","HHC (hexahydrocannabinol)","cann","Hydrogenated cannabinoid made from hemp CBD.","HHC, HHC-P, HHC-O.",
"HHC was first made by Roger Adams in 1944 by adding hydrogen to THC. It appeared in US and European markets in 2021 as a hemp product.","None.","Marketed as a shelf-stable 'legal' THC alternative; it spread rapidly in Europe in 2022.","Banned in many EU countries from 2023, and controlled under the UN 1971 Convention (Schedule II) in 2025; status varies by US state.",
["HHC feels close to ordinary THC, somewhat milder: relaxation, euphoria, appetite and time distortion.","Products contain a mix of two forms, only one strongly active, so strength varies.","Like delta-8, it is made by chemical reactions in unregulated labs, and newer variants (HHC-P) are much stronger."],
["Inhaled, effects begin within minutes; edibles take 30 minutes to 2 hours.","Relaxation builds.","Peak with typical cannabis effects.","Plateau about an hour (vape) or several hours (edible).","Gradual fade.","Dry mouth and sleepiness.","Possible next-day fog."],
{"inhaled-smoked":t("minutes","5-15 min","15-45 min","about 1 h","2-3 h","3-5 h","next morning"),"oral":t("30 min-2 h","1-3 h","2-4 h","4-6 h","6-10 h","12-24 h","next day")},{"inhaled-smoked":"Vapes.","oral":"Gummies."},
"Too much causes anxiety, vomiting, confusion and fast heart rate.","Vapes and gummies."+CW,"HHC binds CB1 like THC; the 9(R) form is the active one.",src=["EMCDDA: HHC technical report (2023)","UN Commission on Narcotic Drugs decision on HHC (2025)"])
# --- anorectics split
p=D["phentermine"]; p["name"]="Phentermine (Adipex-P, Lomaira) and benzphetamine"
p["brands"]="Phentermine: Adipex-P, Lomaira; with topiramate in Qsymia. Benzphetamine: Didrex, Regimex. Withdrawn relatives: fenfluramine (Pondimin), sibutramine (Meridia)."
for slug,name,br,hist,legal,flav,ext_t,sched in [
("diethylpropion","Diethylpropion (amfepramone)","Tenuate, Tenuate Dospan (extended-release), Tepanil; outside the US: amfepramone.",
"Diethylpropion was approved in the US in 1959. Chemically, it is a cathinone, related to bupropion. It was withdrawn in parts of Europe after safety reviews, and the EU recommended withdrawal of amfepramone in 2022.",
"US Schedule IV; UN 1971 Convention Schedule IV.",
["Diethylpropion is one of the milder anorectics: appetite suppression and mild alertness with less euphoria than phentermine.","Side effects include dry mouth, restlessness, insomnia and raised blood pressure; it can lower the seizure threshold.","Like other anorectics, it is linked rarely to pulmonary hypertension and heart valve problems, especially with long-term use."],
"Tenuate immediate-release tablets act for about 4 hours; Tenuate Dospan is a controlled-release tablet designed to last most of the day and should be swallowed whole.","IV"),
("phendimetrazine","Phendimetrazine (Bontril)","Bontril PDM, Bontril Slow-Release; generic tablets and extended-release capsules.",
"Phendimetrazine was approved in 1959. It is a prodrug converted in the body into phenmetrazine (Preludin), a stimulant widely misused in the 1950s and 1960s, including by the Beatles in Hamburg, and withdrawn from the US market.",
"US Schedule III; its active metabolite phenmetrazine is Schedule II.",
["Phendimetrazine feels more amphetamine-like than diethylpropion because phenmetrazine releases dopamine and noradrenaline: alert, energetic and not hungry, with some euphoria.","Side effects include insomnia, a racing heart, dry mouth and irritability.","Misuse can cause anxiety, high blood pressure and psychosis, and it carries the anorectic risks of pulmonary hypertension and valve disease."],
"Immediate-release tablets are taken several times a day; extended-release capsules last most of the day. Capsules should be swallowed whole.","III")]:
    X(slug,name,"stim","Amphetamine-like appetite suppressant (anorectic), schedule "+sched+".",br,hist,"Short-term treatment of obesity alongside diet and exercise.","Misused for weight loss and energy; less common than phentermine.",legal,flav,
    ["Swallowed, effects begin within about 1 hour.","Appetite falls and alertness rises.","Peak at 1 to 2 hours (immediate-release).","Effects last several hours; extended-release longer.","Comedown with tiredness and hunger.","Insomnia if taken late.","Possible next-day fatigue."],
    {"oral":t("about 1 h","1-2 h","1-2 h","4-12 h","6-14 h","next night","next day")},{"oral":"Tablets and capsules."},
    "Overdose causes agitation, high blood pressure, fast heart rate, hallucinations and seizures.","Generic tablets and capsules vary by manufacturer. "+SR,
    "Diethylpropion is metabolized to active compounds in the liver." if slug=="diethylpropion" else "Phendimetrazine is converted in the liver to phenmetrazine, which carries most of the effect.",er=ext_t,src=["DailyMed prescribing information"])
