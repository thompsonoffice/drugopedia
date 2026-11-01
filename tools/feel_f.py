# Fuller psilocybin and MDMA, then remaining opioids.
from gen import D
import feel_e
F={}
F["psilocybin"]=feel_e.F["psilocybin"]
F["psilocybin"]["plateau"]=["Psilocybin's plateau is a slower, rolling continuation of the peak. The body often feels heavy and warm, sometimes with a sense of melting into the floor or bed, and movement feels effortful. Waves of tingling or energy may move through the limbs, and the stomach may still feel unsettled. Visual effects persist as breathing surfaces, shifting patterns and intensified colors, especially with eyes closed.",
"Mentally people often drift through long chains of thought and memory. Emotions can be close to the surface: laughter, tears, gratitude or grief may arrive suddenly. Many describe feelings of connection with nature, other people or something larger; others feel vulnerable, exposed or stuck in a thought loop. Time can feel suspended.",
"Coordination and judgment are reduced, so walking around unsupervised, near water, traffic or heights, is risky. Anxiety can resurface in waves, usually easing with a calm setting and reassurance."]
F["psilocybin"]["comedown"]=["As psilocybin fades, visuals soften into a slight shimmer, the body feels tired and loose, and appetite may return. Some feel mild headache or lingering stomach discomfort.",
"Emotionally the comedown is often reflective and calm, with a sense of having been through something meaningful. Some feel raw, tearful or anxious, and people may want to talk through what they experienced.",
"Sleep usually comes more easily than after LSD. Rarely, people experience lasting anxiety, low mood or perception changes, and people with a personal or family history of psychosis or bipolar disorder face higher risk."]
F["mdma"]=feel_e.F["mdma"]
F["mdma"]["plateau"]=["The plateau holds warmth, energy and heightened touch sensitivity: hugging, stroking or dancing feels unusually pleasant. The jaw stays tight and people may grind their teeth or chew. Sweating continues, and the body is hot, especially in crowded venues. The eyes may flicker slightly (nystagmus) and pupils remain wide.",
"Mentally people stay open, talkative and affectionate. Conversations can feel deep and honest, and people may share things they normally keep private. The intense rush of the peak smooths into a warm, contented glow, though some feel a slight restlessness or wish for more.",
"Overheating, dehydration and, from drinking very large amounts of water, low blood sodium remain the main dangers. Combining with other stimulants or serotonergic drugs adds risk."]
F["mdma"]["comedown"]=["As MDMA wears off, the body feels tired, achy and heavy; the jaw and teeth may be sore, and some feel chilled or sweaty. Sleep can be difficult despite exhaustion.",
"Emotionally the warmth drains away, often leaving a flat, empty or tearful mood. The next few days can bring the 'Tuesday blues' of low mood, irritability and poor concentration, linked to depleted serotonin.",
"Repeated or heavy use worsens these effects and is linked to lasting mood and memory problems. Severe headache, confusion or vomiting after heavy water drinking is an emergency sign of low blood sodium."]
for k,v in F.items(): D[k]["feel"]=v
