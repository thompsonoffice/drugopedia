from gen import D
MET={"morphine":"Morphine is processed mainly by glucuronidation in the liver into morphine-3-glucuronide and the active morphine-6-glucuronide, both cleared by the kidneys; its half-life is about 2 to 4 hours.",
"codeine":"Codeine is converted by the liver enzyme CYP2D6 into morphine, which produces most of its effect; genetics determine how fast this happens. Half-life about 3 hours.",
"hydrocodone":"Hydrocodone is metabolized by CYP3A4 and CYP2D6 (into hydromorphone); half-life about 4 hours.",
"oxycodone":"Oxycodone is metabolized mainly by CYP3A4, with a small part turned into oxymorphone by CYP2D6; half-life about 3 to 4.5 hours for immediate-release.",
"oxymorphone":"Oxymorphone is glucuronidated in the liver; its oral bioavailability is only about 10 percent and food raises it. Half-life about 7 to 9 hours.",
"hydromorphone":"Hydromorphone is glucuronidated in the liver; half-life about 2 to 3 hours.",
"methadone":"Methadone is metabolized by CYP3A4, CYP2B6, and CYP2D6, and its half-life varies enormously, from about 8 to 59 hours, so it accumulates over several days.",
"buprenorphine":"Buprenorphine is metabolized by CYP3A4 to norbuprenorphine; it binds receptors very tightly and has a half-life of about 24 to 42 hours.",
"fentanyl":"Fentanyl is very fat-soluble, reaching the brain quickly, and is metabolized by CYP3A4; it redistributes into fat, so its effect after one IV dose is short but repeated exposure builds up.",
"fentanyl-illicit":"Fentanyl is very fat-soluble, reaching the brain quickly, and is metabolized by CYP3A4; illicit mixtures contain unknown amounts and other drugs.",
"heroin":"Heroin crosses into the brain faster than morphine and is turned within minutes into 6-monoacetylmorphine and then morphine, which carry the effect; heroin itself lasts only minutes in the blood.",
"tramadol":"Tramadol is turned by CYP2D6 into O-desmethyltramadol, which carries most of the opioid effect; the parent drug provides serotonin and norepinephrine effects. Half-life about 6 hours.",
"tapentadol":"Tapentadol is active itself (not a prodrug) and is glucuronidated; half-life about 4 hours.",
"meperidine":"Meperidine is turned into normeperidine, which has a half-life of 15 to 30 hours and builds up with repeated doses or kidney disease.",
"tianeptine":"Tianeptine has a short half-life of about 2.5 hours and is broken down mostly by beta-oxidation, not CYP enzymes.",
"kratom":"Mitragynine is metabolized by CYP3A4, partly into 7-hydroxymitragynine; effects vary with leaf alkaloid content.",
"lean":"Codeine is converted by CYP2D6 into morphine; promethazine is a phenothiazine antihistamine metabolized by CYP2D6 with a half-life of 10 to 19 hours."}
GENERIC={"opioid":"Like other opioids, it acts mainly on mu-opioid receptors in the brain, spinal cord, and gut, and is cleared mostly by the liver.",
"benzo":"Like other benzodiazepines, it enhances the effect of the calming neurotransmitter GABA at GABA-A receptors and is cleared mostly by the liver."}
EXTRA={
"opioid":{
"onset":["From a medical point of view, the onset reflects how quickly the drug reaches the brain. {met} As blood levels rise, mu-opioid receptors in the brainstem, limbic system, and spinal cord begin to activate, which is why pain signals soften and mood changes before the body feels fully affected.",
"Clinicians watch for early signs at this stage: the pupils begin to narrow, breathing rate drops slightly, the face may flush from histamine release, and the gut slows. Patients often report relief of tension or pain before any pleasure, and some feel lightheaded when standing because blood vessels relax."],
"peak":["Medically, the peak corresponds to the highest drug levels at the receptors. The same receptors that produce euphoria and pain relief also tell the brainstem to breathe less, so respiratory depression is greatest during the peak. Oxygen levels can fall without the person noticing, because opioids blunt the brain's alarm response to rising carbon dioxide.",
"Hospital staff monitor sedation and breathing most closely at this point. Signs that the effect is turning dangerous include deepening sleepiness, snoring or gurgling, breathing slower than about one breath every five seconds, and difficulty waking. Mixing with alcohol, benzodiazepines, gabapentinoids, or other sedatives makes this phase far more dangerous."],
"comedown":["The comedown reflects falling blood levels as the liver and kidneys clear the drug. Receptor activity decreases, and the brain's normal pain and stress signals return. In people who have used opioids regularly, the nervous system has adapted, so falling levels trigger the beginnings of withdrawal: increased noradrenaline activity causes anxiety, sweating, yawning, and goosebumps.",
"For long-acting or extended-release forms, the comedown can be very drawn out, and drug can remain active well after the person feels 'normal'. That is one reason taking more during the comedown is a common cause of overdose: the new amount stacks on drug that is still present."]},
"benzo":{
"onset":["From a medical point of view, the onset reflects how quickly the drug is absorbed and enters the brain. {met} As it binds to GABA-A receptors, brain activity slows: anxiety eases, muscles relax, and reaction time lengthens.",
"Clinicians notice early signs such as slower speech, drooping eyelids, and reduced coordination. People often underestimate how impaired they already are at this stage, which is why driving is dangerous."],
"peak":["Medically, the peak is when sedation, muscle relaxation, and memory impairment are strongest. Benzodiazepines can block the formation of new memories (anterograde amnesia), so people may act normally yet remember nothing later.",
"On their own, benzodiazepines rarely stop breathing in healthy adults, but combined with opioids or alcohol they greatly deepen respiratory depression. The FDA added its strongest boxed warning about this combination in 2016."],
"comedown":["As levels fall, the calming effect wears off. With short-acting benzodiazepines, rebound anxiety and insomnia can be sharp. Long-acting ones and their active metabolites can linger for days, causing next-day drowsiness and impaired driving.",
"In people who take them daily, falling levels can trigger withdrawal, which in severe cases includes seizures and delirium. This is why stopping should be a slow medical taper, not a sudden stop."]}}
VARY={"opioid":"Why the same amount affects people differently: tolerance is the biggest factor, since daily users may need many times more to feel the same effect, and tolerance drops quickly after a break. Liver enzymes (especially CYP2D6 and CYP3A4) vary by genetics and are changed by other medicines and even grapefruit. Body size, age, kidney and liver health, sleep apnea, and lung disease all matter. Mixing with alcohol, benzodiazepines, or other sedatives multiplies the effect on breathing. Stronger effects do not stop at a higher level of pleasure: the line between deep sedation and overdose is thin and invisible from the inside.",
"benzo":"Why the same amount affects people differently: tolerance builds quickly, liver function and age change how fast benzodiazepines are cleared (older adults clear many much more slowly), and many medicines block the CYP3A4 enzyme that breaks down alprazolam, midazolam, and triazolam. Alcohol and opioids multiply the sedation and breathing risk. Stronger effects shade into blackouts, falls, and, in combinations, stopped breathing."}
def expand(slug,d,b):
    met=MET.get(slug,GENERIC[b])
    E={k:[x.format(met=met) for x in v] for k,v in EXTRA[b].items()}
    return E
