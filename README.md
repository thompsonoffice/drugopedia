# Drugopedia

Drugopedia is an educational, harm-reduction encyclopedia of drugs, written as content for a future iPhone app. It currently covers opioids (prescription, historical, heroin, fentanyl, Lean, atypical, and novel synthetic opioids) and benzodiazepines (prescription and designer). Planned next: muscle relaxants, barbiturates, sedative-hypnotics, gabapentinoids, inhalants, cannabis, anesthetics, and more.

## Why it exists

The creator has lived experience with drugs and built this so that people don't have to do what they did. The creator wants people to be able to learn what drugs are, where they came from, how they are used in medicine, and what they honestly feel like, **without having to try them**. Curiosity is normal; overdose is permanent. Every page puts the experience next to the real risks, overdose signs, and where to get help.

The project is written to be fully accessible with screen readers such as VoiceOver, NVDA, and JAWS: plain headings, short paragraphs, and lists instead of tables.

## How it is organized

- `INDEX.md`: the full list of pages.
- `narcan/`: naloxone and nalmefene, the overdose-reversal medicines.
- `safety/benzodiazepine-safety.md` and `safety/xylazine.md`: shared safety pages.
- `safety/depressant-mixing.md`: why combining depressants kills, and what to do.
- `products/<product>.md`: brand and combination products (Percocet, Norco, Tylenol #3, Fioricet, Suboxone vs Zubsolv vs Subutex and more), with how the added ingredients change the feel and the risks.
- `safety/opioid-overdose.md`: what an overdose feels and looks like, what naloxone (Narcan) does, and step-by-step what bystanders should do.
- `drugs/<drug>.md`: one general page per drug: history and origins, medical use then and now, how it entered recreational use, legal status, brand names, role in addiction treatment where relevant, an in-depth description of what it feels like phase by phase, an overdose note, and sources.
- `routes/<route>/<drug>.md`: one page per drug per route of administration (oral, sublingual-buccal, intranasal, rectal, transdermal, injected, inhaled-smoked), with timing for that route, how it feels different, and route-specific risks. Routes a drug is not used by are listed on its general page.
- `tools/`: the Python scripts that generate the pages from structured data.

## Categories covered

Opioids (prescription, heroin, fentanyl, rare and historic), atypical opioids, novel synthetic opioids, prescription and designer benzodiazepines, muscle relaxants, barbiturates, sedative-hypnotics, and gabapentinoids.

## Disclaimer

Drugopedia is for education and harm reduction only. It is not medical advice and is not a guide to using drugs. It deliberately contains **no doses or amounts, no preparation, extraction, or tamper-defeating information, no instructions for any route, no sourcing, and no tips for intensifying or mixing**. Timings are typical ranges from medical and harm-reduction references and vary widely from person to person. Street drugs are frequently contaminated with fentanyl.

If you or someone you know needs help: SAMHSA National Helpline **1-800-662-4357** (free, 24/7). In an emergency call **911** and give naloxone.
