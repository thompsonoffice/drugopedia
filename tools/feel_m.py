# Deep felt-experience: remaining opioids, batch 4.
from gen import D
F={}
F["dezocine"]={
"onset":["Dezocine (Dalgan) is a mixed opioid that was used by injection in US hospitals and remains common in China. Its onset brings a quick heaviness, drowsiness and noticeable pain relief, often with dizziness.",
"Mentally the onset is calm but muted. People describe sleepy relaxation with little euphoria; it partly blocks the receptors responsible for the strongest highs.",
"Nausea, sweating and light-headedness are common, and in people dependent on full opioids it can bring on withdrawal."],
"peak":["At its peak the body feels slack and sleepy, pain greatly reduced, and breathing somewhat slowed, though less than with morphine.",
"Mentally the peak is drowsy and detached. Some people feel foggy or mildly uneasy; vivid dreams can come with dozing.",
"Its breathing suppression has a ceiling, but combining it with other sedatives still carries real danger."],
"plateau":["The plateau lasts a few hours of light sedation, dry mouth and pain relief.",
"Mentally people feel quiet and slightly slowed, content to rest.",
"Dizziness on standing and nausea may continue."],
"comedown":["As it fades, people feel tired and sometimes headachy, and pain returns.",
"Emotionally the comedown is usually mild, with occasional low mood.",
"Its misuse potential is considered lower than full opioids, but dependence is possible with long use."]}
F["desomorphine"]={
"onset":["Desomorphine is a very fast, short-acting morphine relative. In medicine it was briefly used in Switzerland, but it is best known as the main ingredient of 'krokodil,' a crude, contaminated homemade drug seen mostly in Russia and Ukraine. Pure desomorphine comes on quickly: an abrupt wave of warmth, heaviness and relief from pain or withdrawal.",
"Mentally the onset is sudden and intense: a rush of calm and euphoria that sweeps away anxiety, followed quickly by drowsy contentment.",
"Street krokodil is not pure desomorphine. It contains toxic leftovers that destroy skin, blood vessels and bone, causing gangrene and grayish, scaly dead tissue that gave it its name. Those injuries, not the opioid itself, define most of its harm."],
"peak":["At its peak the body feels heavy and warm, breathing slows, and pupils shrink. The peak is short.",
"Mentally there is a strong but brief dreamy euphoria, then sedation.",
"Overdose from breathing suppression is possible, and contaminants cause infections, blood clots, kidney and liver damage and tissue death."],
"plateau":["The plateau is very short, often only an hour or two, which drives frequent repeated use.",
"Mentally the calm fades quickly into restlessness and craving.",
"Repeated use multiplies exposure to toxic contaminants."],
"comedown":["The comedown is rapid and harsh: aches, sweating, restlessness and intense craving.",
"Emotionally people often describe despair, anxiety and a compulsion to use again.",
"Dependence develops fast, and the tissue damage can be permanent. Medical care for wounds and addiction treatment are urgent."]}
F["dihydroetorphine"]={
"onset":["Dihydroetorphine is an extremely potent opioid, thousands of times stronger than morphine, used in China as tablets dissolved under the tongue for severe pain. Its onset is fast: a strong warmth and heaviness spreading through the body and pain disappearing.",
"Mentally the onset brings a quick, deep calm and sedation; people describe a short euphoric lift and then drowsiness.",
"Its potency means tiny differences in amount can dramatically change the effect and the breathing risk."],
"peak":["At its peak the body is heavy, warm and still; breathing slows markedly and pupils are pinpoint.",
"Mentally the peak is drowsy and dreamlike.",
"Overdose can come quickly; naloxone works but may need repeating."],
"plateau":["The plateau is relatively short, a few hours of fading sedation.",
"Mentally people feel calm and slow.",
"Its short action led to frequent use and rapid dependence in China during the 1990s, when it became a drug of misuse."],
"comedown":["The comedown brings aches and restlessness.",
"Emotionally a low, anxious mood with craving.",
"Dependence and withdrawal like other strong opioids."]}
F["ketobemidone"]={
"onset":["Ketobemidone (Ketogan) is a strong synthetic opioid used for severe pain mainly in Scandinavia. Its onset brings a smooth warmth, loosening muscles and strong pain relief, without as much histamine itch as morphine.",
"Mentally the onset brings a pleasant, clear-headed calm and euphoria. It also has NMDA-blocking activity, and some describe a slightly detached, floating quality.",
"Nausea and dizziness can occur early; breathing begins to slow."],
"peak":["At its peak the body feels heavy and comfortable, with small pupils and slowed breathing.",
"Mentally the peak is a strong contentment and detachment, sometimes described as more euphoric than morphine, which gives it a high misuse reputation in Nordic countries.",
"Breathing suppression is dangerous, especially with alcohol or benzodiazepines."],
"plateau":["The plateau lasts a few hours of steady sedation and relief.",
"Mentally calm and dreamy.",
"Constipation builds."],
"comedown":["The comedown brings tiredness and returning pain.",
"Emotionally a flat, restless mood.",
"Dependence develops with regular use."]}
for k,v in F.items():
    if k in D: D[k]["feel"]=v
