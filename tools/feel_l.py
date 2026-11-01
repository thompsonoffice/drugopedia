# Deep felt-experience: remaining opioids, batch 3.
from gen import D
F={}
F["nicomorphine"]={
"onset":["Nicomorphine (Vilan) is a morphine ester used for pain in a few European countries. It is converted to morphine in the body quite quickly, so its onset feels like a slightly faster, smoother morphine: warmth rising through the chest, the limbs loosening and pain fading into the background.",
"Mentally the onset brings a soft, enveloping calm. Tension and worry ease, and many describe a quiet, comforting feeling of being safe and held.",
"Nausea, itching and light-headedness are common early, and breathing begins to slow even before the full effect is felt."],
"peak":["At its peak the body feels heavy and warm, skin flushed and itchy, pupils pinpoint and breathing slow. Like morphine it can cause a histamine release that makes the face and neck itch and redden.",
"Mentally there is a deep, dreamy contentment, with drifting thoughts and drowsiness. Compared with morphine people sometimes describe a slightly cleaner, quicker arrival, but the overall character is very similar.",
"Combined with other sedatives the peak can tip into dangerous breathing suppression; naloxone reverses it."],
"plateau":["The plateau lasts a few hours of warm, heavy sedation with nodding, dry mouth and constipation.",
"Mentally people feel calm, slow and inward, with fragmented dreamy moments.",
"Breathing remains suppressed, especially during sleep."],
"comedown":["The comedown brings tiredness, aching and the return of pain, sometimes with nausea.",
"Emotionally a gray, flat mood and restlessness can follow.",
"Regular use causes morphine-like dependence and withdrawal."]}
F["dihydromorphine"]={
"onset":["Dihydromorphine (Paramorfan) is a close morphine relative that was used for pain in some countries. Its onset is somewhat faster and its effect a bit stronger than morphine: a quick flush of warmth, heaviness in the arms and legs and pain receding.",
"Mentally there is a rapid settling of anxiety and a comfortable, sleepy calm. It tends to be described as morphine-like but with less nausea and a shorter duration.",
"Breathing slows early, and itching is common."],
"peak":["At its peak the body is warm and slack, eyelids heavy, pupils small. Itch and dry mouth are frequent.",
"Mentally the peak is a dreamy, contented drowsiness, with slowed thinking and nodding.",
"Breathing suppression is the main danger, worsened by alcohol or benzodiazepines."],
"plateau":["The plateau is shorter than morphine's, a couple of hours of fading heaviness.",
"Mentally the calm thins out into quiet tiredness.",
"Shorter action can lead to more frequent redosing and faster tolerance."],
"comedown":["The comedown brings aches, restlessness and sometimes nausea.",
"Emotionally people feel flat and irritable.",
"Dependence and withdrawal resemble morphine's."]}
F["anileridine"]={
"onset":["Anileridine (Leritine) was a meperidine-related opioid used for pain in the mid-twentieth century, now discontinued. Its onset was fairly quick: warmth, relaxation and a dulling of pain within a short time.",
"Mentally people described a light, comfortable lift with mild euphoria, similar to meperidine's brighter, less sleepy quality.",
"Dizziness, nausea and sweating were common early effects."],
"peak":["At its peak the body felt loose and warm, with dry mouth and some drowsiness, but less heavy sedation than morphine.",
"Mentally there was a pleasant, airy calm, sometimes talkative.",
"Breathing suppression rose with higher amounts or other sedatives."],
"plateau":["The plateau was relatively short, a couple of hours of mild warmth.",
"Mentally the lift faded into quiet tiredness.",
"Frequent redosing was a misuse risk."],
"comedown":["The comedown brought aches, restlessness and tiredness.",
"Emotionally people felt low and anxious.",
"Dependence developed with regular use. It is no longer marketed."]}
F["alphaprodine"]={
"onset":["Alphaprodine, sold as Nisentil, was a fast, short-acting opioid related to meperidine, used during childbirth and in dentistry until it was discontinued in the US in the 1980s. Given by injection, it came on within minutes: a warm flush spreading through the chest and limbs, the body going loose and heavy, and pain receding sharply.",
"Mentally the onset brought a quick, floaty calm. Patients described a sense of drifting above their pain, as if it belonged to someone else, along with a mild lift in mood.",
"Breathing could slow very quickly, and when it was given during labor it crossed to the baby, sometimes leaving newborns sleepy and slow to breathe."],
"peak":["At its peak the body felt relaxed and sunk, with slowed breathing, small pupils and sometimes dizziness or sweating.",
"Mentally there was a brief, dreamy contentment and detachment. Some people felt drowsy enough to doze; others stayed awake but unconcerned.",
"Because the peak came fast, breathing problems could develop within minutes, so it needed close monitoring and reversal medicine on hand."],
"plateau":["The plateau was short, typically fading within an hour or two, which was why it was chosen for brief procedures.",
"Mentally the calm thinned into quiet drowsiness, with thinking slowly clearing.",
"Breathing still needed watching until the person was fully alert."],
"comedown":["Effects lifted fairly quickly, leaving tiredness, sometimes nausea and a return of pain.",
"Emotionally the comedown was usually mild, though some felt groggy or disoriented.",
"Its short action and misuse risk, along with safer alternatives, led to its withdrawal from the market."]}
F["meptazinol"]={
"onset":["Meptazinol, sold as Meptid in the UK, is a partial opioid that has been used particularly for pain during labor. Its onset brings drowsiness, a woozy light-headedness and moderate relief, with less warmth and heaviness than full opioids.",
"Mentally people describe a mild, sleepy calm with little euphoria. Some feel slightly detached or dizzy rather than pleasantly relaxed.",
"Nausea and vomiting are common and are often the most noticeable early effect."],
"peak":["At its peak the body feels sleepy and slow, with sweating and sometimes a sense of unsteadiness.",
"Mentally the peak is drowsy and inward, with dulled concentration but rarely a strong high, which is part of why it is thought to carry less misuse risk.",
"Its breathing suppression is generally lower than morphine's, but it still adds up dangerously with alcohol, benzodiazepines or other opioids."],
"plateau":["The plateau lasts a few hours of light sedation and partial pain relief.",
"Mentally people feel quiet and slightly foggy.",
"Nausea and dizziness may persist, making standing or walking unsteady."],
"comedown":["As it fades, tiredness lingers and pain returns.",
"Emotionally the comedown is usually unremarkable.",
"Misuse and dependence are uncommon but possible with long use."]}
for k,v in F.items():
    if k in D: D[k]["feel"]=v
D["benzhydrocodone"]["feel"]={
"onset":["Benzhydrocodone, sold with acetaminophen as Apadaz, is a prodrug: it does nothing until enzymes in the gut convert it into hydrocodone. Swallowed as intended, the onset feels much like a hydrocodone combination tablet, building gradually over the first hour: a warmth settling into the stomach and chest, muscles loosening, and pain softening into a dull, distant pressure.",
"Mentally the onset brings hydrocodone's mellow, cozy calm. Worries lose their sharpness, the mind slows a little, and many people feel a gentle, comfortable contentment rather than a bright rush.",
"Because the conversion happens in the gut, it was designed so that other routes do not produce a faster or stronger effect. The acetaminophen in the tablet adds liver risk if too much is taken overall, including from other cold or pain products."],
"peak":["At its peak the body feels warm, heavy and loose. An itch often creeps across the nose, face or chest, pupils narrow, and breathing slows and deepens.",
"Mentally the peak is a dreamy, contented mellowness. Some people become chatty and sociable, others quietly drowsy; music and conversation may feel pleasantly soft, and time slides by.",
"Breathing suppression rises sharply with alcohol, benzodiazepines or other opioids. Acetaminophen overdose can silently damage the liver over the following days even when the person feels fine."],
"plateau":["The plateau lasts a few hours of steady, mild sedation and pain relief. Dry mouth, constipation and sometimes nausea develop.",
"Mentally the state is calm, slowed and somewhat inward, with weaker concentration and slower reactions, so driving is unsafe.",
"Breathing remains suppressed, and people who sleep during the plateau after mixing sedatives are at greatest risk."],
"comedown":["The comedown brings tiredness, a heavy-headed feeling and the return of pain.",
"Emotionally some feel flat, restless or mildly irritable as the comfort fades.",
"Regular use causes hydrocodone-like dependence; withdrawal brings aches, yawning, runny nose, diarrhea and craving."]}
