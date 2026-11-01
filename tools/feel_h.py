from gen import D
import feel_g
G=feel_g.F
G["oxymorphone"]["plateau"]=["Oxymorphone's plateau, especially with extended-release forms, is long and heavily sedated. The body feels sunk and slack, skin is warm and flushed, and nodding is frequent. Itch is usually mild.",
"Mentally the plateau is drowsy and dreamlike; people drift in and out of awareness, and conversation fades. The euphoria settles into deep, sleepy contentment, and time passes without notice.",
"Breathing remains suppressed for many hours, and the long duration means overdose can develop during sleep. Constipation and dry mouth build."]
G["oxymorphone"]["comedown"]=["The comedown is slow for extended-release tablets and quicker for immediate-release: heaviness lifts into tiredness and aching.",
"Emotionally people describe a flat, gray mood and restlessness as the strong calm drains away.",
"Regular use leads to dependence; withdrawal brings sweating, yawning, goosebumps, cramps and craving. Taking more during the comedown stacks on drug still in the body."]
G["tramadol"]["plateau"]=["Tramadol's plateau is steady and mild: a light warmth, eased pain, sweating and sometimes a faint itch. Some feel a buzzing restlessness in the legs rather than heaviness.",
"Mentally people feel calm, chatty or mildly upbeat, an antidepressant-like brightness rather than dreamy sedation. Concentration is mostly preserved.",
"Nausea and dizziness may continue, and the seizure and serotonin syndrome risks persist throughout, especially with antidepressants, other opioids or alcohol."]
G["tramadol"]["comedown"]=["As tramadol fades, the body feels tired and slightly achy, and sweating can continue.",
"Emotionally some feel irritable, anxious or low, a dip linked to its serotonin and noradrenaline effects.",
"Regular use causes dependence. Withdrawal combines opioid symptoms (aches, runny nose, diarrhea) with antidepressant-like ones: anxiety, 'brain zaps', confusion and sometimes hallucinations. Stopping should be tapered."]
G["kratom"]["plateau"]=["At lower amounts the plateau feels like a long, mild stimulant: alert, slightly tingly, talkative. At higher amounts it becomes warm and heavy, with relaxed muscles, sweating and narrowed pupils.",
"Mentally people feel calm and content or focused and sociable depending on amount; the mood is milder and less dreamy than prescription opioids.",
"Constipation, dry mouth and nausea build, and combining with other sedatives raises breathing risk."]
G["kratom"]["comedown"]=["The comedown is gradual: tiredness, mild aches and sometimes a headache.",
"Mood may dip into irritability or low energy, especially in daily users.",
"Daily use causes dependence; withdrawal includes aches, irritability, runny nose, jerky limbs and insomnia, similar to but usually milder than opioid withdrawal."]
for k in("oxymorphone","tramadol","kratom"): D[k]["feel"]=G[k]
