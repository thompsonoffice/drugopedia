from gen import *
from data_rx import R
def N(slug,*a,**k):
    R(slug,*a,**k); D[slug]["cat"]="nso"; D[slug]["also"]=["xyl"]
NS="Novel synthetic opioids are sold as powders, counterfeit pills, or mixed into heroin and fentanyl. Their potency is unknown to the person using them."
N("nitazenes","Nitazenes (isotonitazene, protonitazene, metonitazene, and others)","Benzimidazole opioids, a chemical family unrelated to fentanyl. Many are stronger than fentanyl.",
"Isotonitazene ('iso'), protonitazene, metonitazene, etonitazene, etodesnitazene, N-pyrrolidino etonitazene, and others.",
"Developed by the Swiss company CIBA in the late 1950s as possible painkillers; never approved because of their danger. Isotonitazene appeared on the illicit market in 2019, followed by dozens of relatives, especially in the UK, Europe, and the US. They are found in counterfeit oxycodone and benzo pills and in heroin.",
"None.","Usually taken unknowingly in pills or powders sold as other drugs.","Isotonitazene and many relatives US Schedule I; UK Class A since 2024.",
["Little is known from direct reports. People describe a heavy, fast opioid effect, similar to or stronger than fentanyl, with rapid loss of consciousness.","Because they are in counterfeit pills, most people never know they took a nitazene."],
["Onset within seconds to minutes depending on route.","Little come-up.","Heavy sedation, sometimes immediate unconsciousness.","Duration unclear, may be longer than fentanyl.","Comedown unclear.","Unknown.","Strong dependence expected."],
{"oral":"In counterfeit pills.","intranasal":"In powders.","inhaled-smoked":"Smoked like fentanyl.","injected":"Injected in mixtures."},"Other routes not covered.",
"Extremely potent; overdose can happen quickly and may need several doses of naloxone. Standard fentanyl test strips do not detect them; nitazene test strips exist.",
["UNODC Early Warning Advisory on nitazenes","Ujváry I, et al. DARK classics in chemical neuroscience: etonitazene and related benzimidazoles (ACS Chem Neurosci, 2021)","DEA scheduling of isotonitazene (2020)"])
for slug,name,hist,legal in [
("u-47700","U-47700 ('pink')","Developed by Upjohn in the 1970s; appeared on the illicit market around 2015. It was linked to many deaths in 2015 and 2016 and sold as 'pink' or 'U4'.","US Schedule I (2016)."),
("ah-7921","AH-7921","Developed by Allen and Hanburys in the 1970s; sold as a research chemical from 2012, linked to deaths in Europe.","US Schedule I."),
("mt-45","MT-45","Developed in Japan in the 1970s; sold online from about 2013, linked to deaths and hearing loss in Sweden.","US Schedule I."),
("carfentanil","Carfentanil","Synthesized by Janssen in 1974 and used as a large-animal tranquilizer (Wildnil), about 100 times stronger than fentanyl. It appeared in illicit drugs in 2016 and again in 2024.","US Schedule II (veterinary).")]:
    N(slug,name,"Synthetic opioid never approved for human use.","Street names vary; often unlabeled.",hist,"None in humans" + (" (veterinary tranquilizer only)." if slug=="carfentanil" else "."),
    "Sold as a 'research chemical' or found in counterfeit pills and powders.",legal,
    [f"{name} produces opioid effects of warmth, sedation, and euphoria reported to be similar to other strong opioids. Reliable descriptions are scarce, and many people who took it did not know.","Its strength and duration are unpredictable in street products."],
    ["Fast onset, often seconds to minutes.","Rapid build.","Heavy opioid peak.","Short to moderate duration.","Rapid comedown.","Unknown.","Dependence likely."],
    {"oral":"In pills.","intranasal":"Powder.","injected":"Mixtures."},"Other routes not covered.",
    "Very high overdose risk; carfentanil can kill in tiny amounts and may need multiple naloxone doses.",
    ["UNODC Early Warning Advisory","DEA Drug Fact Sheets"])
