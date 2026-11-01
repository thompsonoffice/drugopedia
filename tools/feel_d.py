# Rich felt-experience phase text: cannabis, ketamine, LSD, psilocybin, MDMA, plus fuller amphetamine and clonazepam.
from gen import D
F={}
F["cannabis-flower"]={
"onset":["When cannabis flower is smoked or vaporized, effects begin within minutes. The first signs are often a tingling or pressure around the eyes and forehead, a warm heaviness in the shoulders, and a noticeably faster heartbeat. The mouth dries ('cottonmouth') and the eyes redden and may feel dry.",
"Mentally the onset brings a shift in perception: sounds and music can feel richer, thoughts begin to jump and connect in unusual ways, and the mood often lightens into giggliness or relaxed amusement. Some people instead feel a flicker of anxiety as the heart rate rises.",
"Short-term memory begins to slip early; people lose the thread of a sentence or forget why they walked into a room. Standing up quickly can bring dizziness or, in some first-time users, fainting."],
"peak":["At the peak the body feels relaxed and heavy, sometimes 'couch-locked', especially with sedating strains. Limbs can tingle, and the skin may feel more sensitive. The heart is still fast, and appetite rises sharply ('the munchies').",
"The emotional tone ranges from euphoric, giggly and sociable to calm and introspective. Time distortion is typical: minutes feel long, and people may lose track of conversations. Colors, tastes and music can feel intensified.",
"With high-THC products or in vulnerable people, the peak can bring anxiety, paranoia, a racing heart and panic. People with a personal or family history of psychosis face higher risk. Driving is impaired."],
"plateau":["During the plateau, the body stays relaxed and slightly heavy; the dry mouth and red eyes persist. Hunger often continues.",
"Mentally there is a mellow, drifting state with slowed time, wandering thoughts and reduced focus. Some feel creative or reflective, others sleepy.",
"Coordination and memory stay impaired, so driving and risky tasks remain dangerous."],
"comedown":["The comedown is gradual: heaviness turns to tiredness, and many people feel sleepy.",
"Emotionally people feel calm or slightly flat; some feel foggy for a while.",
"Regular heavy users may notice irritability, poor sleep and low appetite between uses. Heavy daily use can also cause cannabinoid hyperemesis syndrome, with cycles of severe vomiting."]}
F["ketamine"]={
"onset":["Ketamine's onset depends on route, but people quickly notice a numb, floaty heaviness in the limbs, a slight tingling, and difficulty coordinating movement.",
"Mentally, the world begins to feel distant or unreal; sounds can seem echoey, and thoughts become detached.",
"Nausea, a faster heart rate and raised blood pressure are common, and walking becomes unsteady."],
"peak":["At the peak, the body can feel numb, weightless or separated from the mind; moving is difficult. Vision can blur, and eyes may flick side to side.",
"The emotional tone varies from dreamy and euphoric to confusing or frightening. At higher levels, people may enter the 'K-hole', a deep dissociation with loss of sense of self and surroundings.",
"Risks include accidents, choking on vomit, and dangerous combinations with alcohol or depressants. Long-term use damages the bladder."],
"plateau":["The plateau keeps a heavy, numb, detached body feeling.",
"Mentally people drift in a dreamlike state with slowed time.",
"Movement remains clumsy, and falls are common."],
"comedown":["The comedown is fairly quick, with heaviness and grogginess.",
"Emotionally, some feel calm or reflective, others confused or low.",
"Frequent use brings tolerance, cravings and bladder pain."]}
F["lsd"]={
"onset":["LSD's onset is slow and subtle. People first notice a restless, slightly anxious energy, yawning, goosebumps or chills, and dilated pupils. Some feel mild nausea or a tight jaw.",
"Mentally, there is a growing sense that something is shifting: colors seem brighter, objects look slightly alive, and thoughts become associative.",
"Heart rate and blood pressure rise modestly, and body temperature may increase."],
"peak":["At the peak, visual changes are prominent: surfaces breathe, patterns flow, and colors intensify. The body can feel energized, tingly or heavy.",
"The emotional tone can be awe, joy and insight, or anxiety and confusion. Time can feel stretched or meaningless, and sense of self may dissolve.",
"Risks include panic, frightening experiences and dangerous behavior. Blotters sold as LSD may contain NBOMes."],
"plateau":["The plateau is long: visuals and energy continue for hours.",
"Mentally, people may reflect deeply or feel overwhelmed.",
"Sleep is difficult until the effects fade."],
"comedown":["The comedown brings tiredness while visual effects soften.",
"Emotionally, people feel reflective or drained.",
"Some experience lingering anxiety or, rarely, persistent perception changes (HPPD)."]}
F["psilocybin"]={
"onset":["Psilocybin mushrooms begin with stomach discomfort, yawning and a sense of heaviness or chills.",
"Mentally people feel giddy or anxious as perception shifts.",
"Pupils widen, and colors brighten."],
"peak":["The peak brings strong visual changes and emotional depth; the body may feel heavy or tingling.",
"The emotional tone is often introspective, emotional, sometimes overwhelming.",
"Risks include panic and accidents."],
"plateau":["The plateau continues visual and emotional effects.",
"People drift in thought, often feeling connected or vulnerable.",
"Coordination is reduced."],
"comedown":["The comedown is gentle, with tiredness.",
"People feel reflective and calm.",
"Rarely, lasting anxiety or perception changes occur."]}
F["mdma"]={
"onset":["MDMA starts with a rush: tingling, warm waves through the body, a clenching jaw and sometimes nausea.",
"Mentally people feel a growing euphoria and openness.",
"Pupils widen, and heart rate rises."],
"peak":["The peak brings intense warmth, touch sensitivity and energy; the jaw clenches, and the body heats up.",
"The emotional tone is deep empathy, affection and joy.",
"Risks include overheating, low blood sodium and serotonin syndrome."],
"plateau":["The plateau keeps warmth and openness.",
"People stay sociable and affectionate.",
"Dehydration and overheating risk continue."],
"comedown":["The comedown brings tiredness and jaw soreness.",
"Emotionally, a low mood can follow for days ('Tuesday blues').",
"Repeated use worsens these effects."]}
for k,v in F.items(): D[k]["feel"]=v
