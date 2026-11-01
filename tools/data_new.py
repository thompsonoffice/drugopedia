# Cannabis, dissociatives, inhalants, stimulants, cathinones. No amounts, no preparation, no sourcing, no mixing tips.
from gen import D
import med
DN="> Educational harm-reduction content. Not medical advice, not a guide to use. Nothing here gives amounts, preparation, or sourcing. Street products are often mislabeled or contaminated, including with fentanyl."
SG={"cann":["NIDA: Cannabis (Marijuana) DrugFacts","CDC: Cannabis and Public Health","DEA Drugs of Abuse (2024 edition)","PsychonautWiki"],
"diss":["NIDA DrugFacts and Research Reports","DEA Drugs of Abuse (2024 edition)","StatPearls (NCBI Bookshelf)","PsychonautWiki"],
"inh":["NIDA: Inhalants DrugFacts","StatPearls: Inhalant Abuse and Toxicity","DEA Drugs of Abuse (2024 edition)"],
"stim":["NIDA DrugFacts","DEA Drugs of Abuse (2024 edition)","DailyMed prescribing information","StatPearls (NCBI Bookshelf)"],
"cath":["NIDA: Synthetic Cathinones (Bath Salts) DrugFacts","DEA Drugs of Abuse (2024 edition)","EMCDDA/EUDA drug profiles: synthetic cathinones","PsychonautWiki"]}
TH={"cann":"What the products look and feel like","diss":"What the products look and feel like","inh":"What the products look and feel like","cath":"What the products look and feel like"}
def X(slug,name,cat,cls,brands,hist,medu,rec,legal,flav,ph,times,routes,od,touch,met,lohi=None,er=None,skip="Other routes are not covered.",src=()):
    D[slug]=dict(name=name,cat=cat,cls=cls,brands=brands,history=hist,medical=medu,recreational=rec,legal=legal,flavor=flav,ph=ph,times=times,routes=routes,od=od,touch=touch,lohi=lohi,er=er,skip=skip,sources=list(src)+SG[cat],dis=DN,touchh=TH.get(cat,"What the pills feel like"))
    med.MET[slug]=met
t=lambda *a:list(a)
CW=" Street and online products are frequently mislabeled; lab testing services have found products with different drugs or none of the advertised one."
SR="Stimulant drugs sold on the street, including counterfeit Adderall, are often contaminated with methamphetamine or fentanyl."
import data_new_cann, data_new_diss, data_new_stim
