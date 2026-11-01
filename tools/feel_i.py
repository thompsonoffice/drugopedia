from gen import D
F={}
F["fentanyl-illicit"]={
"onset":["Illicitly made fentanyl, sold as powder, in counterfeit pills, or mixed into heroin and other drugs, hits within seconds to a minute when smoked and almost instantly when injected. People describe a sudden heavy warmth falling over the body like a weight, with the limbs going limp and the head dropping.",
"Mentally the rush is brief and narrow: a flash of relief and calm, then rapidly deepening sedation. Many people who knew heroin say fentanyl has less euphoria and 'more nod', and that they lose minutes or hours without remembering.",
"Pupils pinpoint and breathing slows almost at once. Because street fentanyl's strength varies wildly from one part of a batch to another, and is often mixed with xylazine or benzodiazepines, the same-looking amount can be harmless or fatal. Rarely, chest-wall rigidity makes breathing physically difficult within minutes."],
"peak":["The peak arrives fast and is deeply sedating. The body feels extremely heavy, almost unmovable, and people may slump, fall asleep mid-action, or stop responding.",
"The emotional tone, when awareness remains, is a blank, warm calm rather than a vivid high. People often describe 'going under' rather than feeling good, and memory of this phase is patchy.",
"This is the most lethal phase of any drug in this encyclopedia. Breathing can stop within minutes. Signs: unresponsive, gurgling or snoring, blue or gray lips, pinpoint pupils. Call 911, give naloxone, and repeat it if there is no response after a few minutes. Xylazine does not respond to naloxone, so rescue breathing matters."],
"plateau":["The plateau is short: heavy nodding, a warm itch, and slow, shallow breathing. People drift in and out, sometimes for long stretches.",
"Mentally there is little sense of time; the pleasant part fades quickly, which pushes people to use again soon.",
"Breathing remains dangerous throughout, and each repeat use stacks on what is still present. Using alone is the biggest risk factor for dying."],
"comedown":["Fentanyl's comedown is fast. Within a few hours the heaviness lifts and the body feels restless, sweaty and uncomfortable.",
"Emotionally people describe sudden anxiety, irritability and craving, far sooner than with heroin.",
"In dependent people, withdrawal can start within hours: sweating, yawning, goosebumps, cramps, diarrhea and severe restlessness. Wounds linked to xylazine adulteration may worsen. Treatment with buprenorphine or methadone greatly lowers the risk of death."]}
F["tapentadol"]={
"onset":["Tapentadol (Nucynta) starts within a short time by mouth, with mild warmth and an easing of pain that many describe as 'cleaner' and less dopey than other opioids.",
"Mentally there is a light lift and a slightly alert calm, because tapentadol also raises noradrenaline.",
"Nausea, dizziness and sleepiness are the most common early effects; itch is less frequent."],
"peak":["At the peak the body feels relaxed and warm with strong pain relief and moderate heaviness.",
"The emotional tone is calm, mild contentment with less euphoria than oxycodone.",
"Seizures and serotonin syndrome are possible with antidepressants; breathing depression is real, especially with other sedatives."],
"plateau":["The plateau holds steady relief, mild drowsiness and dry mouth.",
"Mentally people stay fairly clear, sometimes a little wired.",
"Constipation is generally milder than with other opioids, but dizziness may continue."],
"comedown":["The comedown is gentle for immediate-release and slow for extended-release.",
"Mood may turn flat or anxious.",
"Dependence develops with regular use, and withdrawal resembles both opioid and antidepressant withdrawal."]}
F["meperidine"]={
"onset":["Meperidine (Demerol) comes on quickly, especially when injected in hospitals, with a fast, warm, slightly buzzy rush and a lightness in the head.",
"Mentally the onset is euphoric and a little stimulating, quite different from morphine's dreamy heaviness. Some feel giddy.",
"Dry mouth, dizziness and a racing heart can occur, because meperidine has anticholinergic effects."],
"peak":["The peak is short and intense: warmth, tingling and relaxation, sometimes with tremor or restlessness.",
"The emotional tone is bright euphoria with little nausea.",
"Its metabolite normeperidine builds up with repeated use or kidney problems and causes tremor, twitching, agitation and seizures. With MAO inhibitors it can cause fatal serotonin syndrome."],
"plateau":["The plateau is brief, with mild sedation and occasional jitteriness.",
"Mentally people stay pleasantly calm.",
"Repeated use raises seizure risk."],
"comedown":["The comedown arrives within a few hours.",
"People feel flat and restless.",
"Dependence develops quickly, and its use in hospitals has declined."]}
F["carfentanil"]={
"onset":["Carfentanil, an elephant tranquilizer far stronger than fentanyl, appears occasionally in the street supply mixed into heroin or fentanyl. Its effects arrive within moments of exposure.",
"Mentally there is little time to notice anything; people lose consciousness quickly.",
"Breathing may slow or stop almost immediately."],
"peak":["The peak is profound unconsciousness.",
"There is no meaningful 'high' to describe; people rarely recall the experience.",
"Overdose is common and fatal without rapid help. Multiple doses of naloxone are often needed, and emergency care is essential."],
"plateau":["Effects can last longer than naloxone, so people may stop breathing again after reviving.",
"Mentally people remain heavily sedated.",
"Monitoring for hours is needed."],
"comedown":["Survivors feel exhausted and ill.",
"Withdrawal can be severe after naloxone.",
"Avoiding any exposure is the only safe approach."]}
F["nitazenes"]={
"onset":["Nitazenes (isotonitazene, protonitazene, metonitazene and others) are synthetic opioids appearing in counterfeit pills and street drugs. Effects begin quickly, with heavy warmth and sedation.",
"Mentally people report rapid, deep drowsiness and confusion.",
"Breathing slows quickly, often more than people expect."],
"peak":["The peak is profound sedation with pinpoint pupils and slowed or stopped breathing.",
"Emotional tone is lost to unconsciousness in many cases.",
"Nitazenes cause frequent fatal overdoses; naloxone works but may need repeating."],
"plateau":["Effects can outlast naloxone, so people may stop breathing again.",
"Mentally people remain sedated.",
"Close monitoring is needed."],
"comedown":["Survivors feel exhausted and nauseated.",
"Withdrawal may follow naloxone.",
"Fentanyl test strips do not detect nitazenes; nitazene strips exist."]}
for k,v in F.items(): D[k]["feel"]=v
