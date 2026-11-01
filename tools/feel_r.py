# Deep felt-experience: designer / research-chemical benzodiazepines.
from gen import D
F={}
WARN="Designer benzodiazepines are unapproved, their strength in powders, blotters and counterfeit pills is unknown, and they are increasingly found mixed with fentanyl, which multiplies the risk of fatal breathing suppression."
def R(k,intro,char,dur,peaknote):
    long_=dur=="long"; short=dur=="short"
    F[k]={"onset":[intro+" "+("It comes on fast: a sudden heaviness, muscles going slack and eyelids drooping." if short else "It builds over a while: a loosening in the neck and shoulders, a warm drowsiness and a quieting of the chest."),
    "Mentally the onset is "+char,WARN],
    "peak":["At its peak the body is heavy and uncoordinated, with slurred speech, stumbling and a strong pull toward sleep.","Mentally the peak is disinhibited, careless and forgetful; blackouts, where people act normally but later remember nothing, are very common with these drugs. "+peaknote,"Combined with opioids, alcohol or other sedatives, breathing can slow dangerously. Naloxone reverses only the opioid part, but should still be given in any suspected overdose."],
    "plateau":[("The plateau is very long, often stretching across a day or more, and repeated doses pile up." if long_ else "The plateau is shorter, a few hours, which drives repeated dosing." if short else "The plateau lasts several hours of steady sedation.")+" Balance stays poor and falls and injuries are common.","Mentally people feel foggy and muted, sometimes re-dosing because they forget they already took some.","Driving or caring for others during this time is unsafe."],
    "comedown":["The comedown brings grogginess, headache and a heavy, dull body, sometimes lasting into the next day.","Emotionally rebound anxiety, irritability, low mood and regret over forgotten actions are common.","Dependence develops fast with daily use, and withdrawal can cause seizures and psychosis; medically supervised tapering, often with a prescribed benzodiazepine, is the safe route."]}
R("flualprazolam","Flualprazolam is a fluorinated relative of alprazolam that appeared around 2018 and was widely found in counterfeit Xanax.","a fast, strong, alprazolam-like calm, with anxiety disappearing and a floaty, euphoric ease that is noticeably stronger and longer than Xanax.","medium","Amnesia is pronounced.")
R("flubromazolam","Flubromazolam is an extremely potent triazolo designer benzodiazepine.","a heavy, overwhelming sedation that arrives deceptively slowly, then hits hard.","long","Very long blackouts and next-day impairment are typical.")
R("clonazolam","Clonazolam is a highly potent designer benzodiazepine related to clonazepam and alprazolam.","a powerful sedation and blank calm that can come on stronger than expected.","medium","It is known for extreme amnesia and dangerous behavior during blackouts.")
R("bromazolam","Bromazolam became one of the most common designer benzos in the US drug supply around 2022, often mixed into fentanyl.","an alprazolam-like calm and drowsiness.","medium","Mixed with fentanyl, it causes deep, prolonged unconsciousness that naloxone alone does not wake.")
R("diclazepam","Diclazepam is a long-acting designer benzodiazepine related to diazepam.","a gradual, diazepam-like calm and muscle relaxation.","long","It breaks down into delorazepam and lorazepam, extending its effects.")
R("deschloroetizolam","Deschloroetizolam is a weaker relative of etizolam.","a light, etizolam-like calm.","medium","Sedation can still be substantial.")
R("pyrazolam","Pyrazolam is a designer benzodiazepine reported as less sedating than most.","a clear-headed easing of anxiety with less sleepiness.","medium","Impairment is still present even if the person feels clear.")
R("nifoxipam","Nifoxipam is a designer benzodiazepine related to flunitrazepam.","a strong, sleep-inducing drowsiness.","medium","Amnesia is pronounced.")
R("meclonazepam","Meclonazepam is a clonazepam relative originally studied against parasites.","a clonazepam-like calm with sedation.","long","It lingers into the next day.")
R("phenazepam","Phenazepam (Fenazepam) is prescribed in Russia and sold elsewhere as a research chemical.","a slow-building, very long and heavy sedation; people often take more because they feel little at first.","long","Effects can last days, with confusion and loss of coordination.")
R("flubromazepam","Flubromazepam is a very long-acting designer benzodiazepine.","a gradual, steady calm.","long","Its very long elimination means it builds up dangerously with repeated use.")
R("metizolam","Metizolam is a weaker relative of etizolam.","a mild, etizolam-like calm.","medium","Effects are milder but still impairing.")
R("adinazolam","Adinazolam is a triazolo benzodiazepine developed as an antidepressant but never approved.","a short calm with a mild mood lift.","short","It is converted into a more sedating metabolite.")
R("desalkylgidazepam","Desalkylgidazepam (bromonordiazepam) is the active metabolite of gidazepam, sold as a designer drug.","a slow, long calm.","long","Accumulation is common.")
R("flunitrazolam","Flunitrazolam is an extremely potent triazolo relative of flunitrazepam.","a fast, overwhelming sedation.","medium","Tiny differences in amount change the effect drastically.")
R("norfludiazepam","Norfludiazepam is a very long-acting metabolite of several benzodiazepines, sold as a designer drug.","a slow, steady calm.","long","Effects linger for days.")
R("rilmazafone","Rilmazafone is a Japanese sleep prodrug that becomes a triazolo benzodiazepine in the body.","a gradual drowsiness leading to sleep.","medium","It has appeared as a designer drug linked to deaths.")
R("clobromazolam","Clobromazolam is a newer, very potent designer benzodiazepine.","a strong, heavy sedation.","medium","It has been found mixed with opioids.")
R("fonazepam","Fonazepam (desmethylflunitrazepam) is a flunitrazepam metabolite sold as a designer drug.","a hypnotic heaviness.","medium","Amnesia is strong.")
R("3-hydroxyphenazepam","3-Hydroxyphenazepam is the active metabolite of phenazepam.","a strong, prolonged calm.","long","Effects can last a very long time.")
R("nitemazepam","Nitemazepam is a nitro-substituted relative of temazepam sold as a designer drug.","a sleepy, temazepam-like calm.","medium","Very little is known about it.")
R("thionordazepam","Thionordazepam is a sulfur-containing relative of nordazepam.","a gradual calm.","long","Its safety is essentially unstudied.")
R("cloniprazepam","Cloniprazepam is a clonazepam prodrug sold as a designer drug.","a clonazepam-like sedation.","long","It breaks down into clonazepam and related compounds.")
R("norflurazepam","Norflurazepam is the long-acting metabolite of flurazepam.","a slow, heavy drowsiness.","long","It lingers for days.")
for k,v in F.items():
    if k in D: D[k]["feel"]=v
