from data_benzo import B
from gen import D
RC=[("flualprazolam","Flualprazolam","A fluorinated alprazolam analog, patented in 1969 but never marketed; appeared in counterfeit Xanax around 2018 to 2020.","longer and more sedating than alprazolam"),
("flubromazolam","Flubromazolam","Appeared online in 2014; extremely potent and long-lasting, linked to deaths and long comas.","extremely strong, long, heavily amnesic"),
("clonazolam","Clonazolam","Described in the 1970s, sold online from 2014; very potent.","strongly sedating and amnesic, with blackouts"),
("bromazolam","Bromazolam","First described in 1976, never marketed; from about 2021 the most common designer benzo in the US and UK, often mixed with fentanyl.","Xanax-like but longer"),
("diclazepam","Diclazepam","A chlorinated diazepam analog synthesized by Sternbach in 1960, sold online from 2013.","long, heavy, Valium-like"),
("deschloroetizolam","Deschloroetizolam","An etizolam analog sold online from about 2014.","shorter and lighter than etizolam"),
("pyrazolam","Pyrazolam","Sold online from 2012; reported as anxiolytic with less sedation.","calming, less sleepy"),
("nifoxipam","Nifoxipam","A flunitrazepam metabolite-related compound sold from 2014.","very sedating"),
("meclonazepam","Meclonazepam","Developed by Roche in the 1970s as an anti-parasite drug; sold online from 2014.","sedating with long duration"),
("phenazepam","Phenazepam","Developed in the USSR in 1975 and still prescribed in Russia and some former Soviet states; sold elsewhere as a research chemical and linked to deaths.","very long, delayed, heavily amnesic"),
("flubromazepam","Flubromazepam","Sold online from 2012; extremely long half-life.","very long, lingering for days"),
("metizolam","Metizolam","An etizolam analog sold online from 2015.","milder and longer than etizolam"),
("adinazolam","Adinazolam","Developed by Upjohn in the 1980s as an antidepressant (Deracyn), never approved; sold online from 2015.","short and mild"),
("desalkylgidazepam","Desalkylgidazepam (bromonordiazepam)","Metabolite of gidazepam (a Ukrainian prescription drug); sold online from about 2020.","long and calm"),
("flunitrazolam","Flunitrazolam","Sold online from 2016; extremely potent.","very strong and sedating"),
("norfludiazepam","Norfludiazepam","Active metabolite of flurazepam, sold online.","long-lasting")]
for slug,name,hist,char in RC:
    B(slug,name+" (designer benzodiazepine)","Designer ('research chemical') benzodiazepine never approved for medical use in the US or UK; little or no human research.",
    "Sold online as 'research chemicals', and pressed into counterfeit Xanax, Valium, or other pills.",hist,"None (except phenazepam in Russia and some neighboring countries).",
    "Sold as 'legal' or 'research' alternatives, and found unknowingly in counterfeit pills.","Many are US Schedule I (several were scheduled in 2022 to 2023); UK Class C or controlled under the Psychoactive Substances Act.",
    [f"Reports describe {name} as {char}. The general pattern is benzodiazepine calm, muscle relaxation, sleepiness, and disinhibition, often with heavy memory loss.",
     "There is almost no research on these drugs in people. Potency is unknown and products are often mislabeled, so the same named product can be far stronger than expected. Counterfeit 'Xanax' bars containing these drugs, sometimes with fentanyl, have caused many deaths."],
    ["Onset reports vary; many begin within 15 to 60 minutes when swallowed.","Relaxation builds.","Peak: sedation, calm, and memory loss; blackouts are common.","Plateau can be long.","Fades slowly for long-acting ones.","Next-day sedation and memory gaps.","Daily use leads to dependence; withdrawal can cause seizures and may need hospital care."],
    {"oral":"Pills, powders, liquids, or blotters."},"Other routes not covered.",
    "Unknown potency and very long durations make overdose and long blackouts likely, especially with opioids or alcohol. Naloxone does not reverse benzodiazepines but should be given if opioids (including fentanyl in counterfeit pills) may be involved.",
    ["UNODC Early Warning Advisory on new psychoactive substances","EMCDDA, New benzodiazepines in Europe (2021)","DEA scheduling notices on designer benzodiazepines (2022-2023)","Manchester KR, et al. The emergence of new psychoactive substance benzodiazepines (Drug Test Anal, 2018)"],
    cat="rcbenzo")
