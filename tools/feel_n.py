# Deep felt-experience: remaining opioids, batch 5.
from gen import D
F={}
F["tilidine"]={
"onset":["Tilidine is a synthetic opioid prodrug used in Germany, Switzerland and Belgium, usually combined with naloxone (Valoron N). Swallowed, the liver converts it into its active form, nortilidine, and the onset comes fairly quickly: a light warmth in the chest, a loosening of the neck and shoulders and pain sliding into the background.",
"Mentally tilidine is often described as brighter and more stimulating than morphine-type opioids. People report a lift in confidence, sociability and a buzzing sense of well-being, which has made it popular among young people in Germany.",
"The added naloxone is meant to block effects if the drug is misused by non-oral routes; swallowed, naloxone is mostly destroyed by the liver. Dizziness, nausea and sweating are common early."],
"peak":["At its peak the body feels warm and light rather than heavily sedated, with a mild itch, dry mouth and narrowed pupils. Some people feel a restless energy in the limbs.",
"Mentally the peak is a confident, talkative euphoria with reduced anxiety and a sense of invulnerability; with more, drowsiness and confusion take over.",
"Breathing suppression rises with higher amounts and especially with alcohol or benzodiazepines, a common and dangerous combination among recreational users."],
"plateau":["The plateau lasts a few hours. The bright lift settles into a steadier, mellow warmth, with sweating, nausea and constipation possible.",
"Mentally people feel calm and somewhat detached, with weaker judgment and slower reactions, so driving is unsafe.",
"Repeated doses can build up, deepening sedation beyond what the user expects."],
"comedown":["The comedown brings tiredness, a heavy head and sometimes aches.",
"Emotionally people often feel irritable, anxious or low, a dip that contrasts with the confident peak.",
"Regular use causes dependence, and withdrawal resembles other opioids: aches, sweats, insomnia, diarrhea and craving."]}
F["oliceridine"]={
"onset":["Oliceridine (Olinvyk) is a newer intravenous opioid approved in the US in 2020 for severe hospital pain. It was designed to activate the pain-relieving signal of the mu receptor more than the pathways linked to some side effects. Given by injection, its onset is within minutes: warmth, relaxation and pain dropping away.",
"Mentally patients describe drowsy calm and relief, with mild euphoria for some.",
"Despite its design, it still slows breathing and causes nausea, especially at higher amounts."],
"peak":["At its peak the body feels heavy and comfortable; pupils narrow and breathing slows.",
"Mentally the peak is sleepy contentment and detachment from pain, similar to morphine but often reported with somewhat less nausea.",
"It is used only with monitoring because breathing suppression and sedation are still real. Naloxone reverses it."],
"plateau":["The plateau is a few hours of steady relief while doses continue.",
"Mentally patients feel quiet, drowsy and slightly foggy.",
"It can affect heart rhythm (QT interval) at higher cumulative amounts, which limits how much is used."],
"comedown":["As it fades, tiredness lingers and pain returns.",
"Emotionally the comedown is usually mild.",
"It is a controlled drug with misuse potential similar to other opioids, though experience outside hospitals is minimal."]}
F["pholcodine"]={
"onset":["Pholcodine is an opioid cough suppressant that was sold for decades in the UK, Australia and Europe. It mainly quiets the cough reflex in the brain, and swallowed, its onset is gradual: the tickle in the throat eases and coughing fits space out.",
"Mentally most people feel little or nothing. It has very weak pain-relieving and euphoric effects compared with codeine.",
"In 2022 and 2023 many countries withdrew it after evidence linked it to a higher risk of severe allergic reactions (anaphylaxis) to muscle relaxants used in surgery."],
"peak":["At its peak there may be mild drowsiness and a faint relaxed feeling, with dry mouth.",
"Mentally the state is calm and quiet but rarely high; this is why misuse has been uncommon.",
"In large excess it can still cause drowsiness, confusion and slowed breathing, especially with other sedatives."],
"plateau":["Pholcodine lasts a long time, so the plateau stretches for many hours of quieted cough and mild drowsiness.",
"Mentally people feel normal or slightly sleepy.",
"Children and older adults are more sensitive to its sedating effects."],
"comedown":["As it fades the cough gradually returns.",
"There is usually no notable mood change.",
"Dependence is rare. Anyone who has taken it and is due for surgery should tell their anesthetist."]}
F["nicocodeine"]={
"onset":["Nicocodeine is a codeine ester used in some European countries as a cough suppressant and pain reliever. It is converted in the body into codeine and morphine-like compounds, and its onset is somewhat quicker and stronger than plain codeine: a warmth rising through the chest, the cough quieting and the body loosening.",
"Mentally the onset brings a soft, comfortable calm and a mild lift in mood.",
"Itching, nausea and light-headedness are common early, much like codeine."],
"peak":["At its peak the body feels heavy and warm with small pupils, itch and slowed breathing.",
"Mentally there is a dreamy contentment and drowsiness, stronger than codeine's but milder than morphine's.",
"Alcohol and other sedatives raise breathing risk."],
"plateau":["The plateau lasts a few hours of light sedation and eased cough.",
"Mentally people feel calm and slow.",
"Constipation and dry mouth build."],
"comedown":["The comedown brings tiredness and the return of cough or aches.",
"Emotionally a mild low or restlessness.",
"Regular use causes codeine-like dependence and withdrawal."]}
for k,v in F.items():
    if k in D: D[k]["feel"]=v
