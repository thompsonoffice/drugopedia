# Drugopedia

Drugopedia is an educational, harm-reduction encyclopedia of drugs, written as content for a future iPhone app. It starts with opioids.

## Why it exists

The creator wants people to be able to learn what drugs are, where they came from, how they are used in medicine, and what they honestly feel like, **without having to try them**. Curiosity is normal; overdose is permanent. Every page puts the experience next to the real risks, overdose signs, and where to get help.

The project is written to be fully accessible with screen readers such as VoiceOver, NVDA, and JAWS: plain headings, short paragraphs, and lists instead of tables.

## How it is organized

- `INDEX.md`: the full list of pages.
- `safety/opioid-overdose.md`: what an overdose feels and looks like, what naloxone (Narcan) does, and step-by-step what bystanders should do.
- `drugs/<drug>.md`: one general page per drug: history and origins, medical use then and now, how it entered recreational use, legal status, brand names, role in addiction treatment where relevant, an in-depth description of what it feels like phase by phase, an overdose note, and sources.
- `routes/<route>/<drug>.md`: one page per drug per route of administration (oral, sublingual-buccal, intranasal, rectal, transdermal, injected, inhaled-smoked), with timing for that route, how it feels different, and route-specific risks. Routes a drug is not used by are listed on its general page.
- `tools/`: the Python scripts that generate the pages from structured data.

## Disclaimer

Drugopedia is for education and harm reduction only. It is not medical advice and is not a guide to using drugs. It deliberately contains **no doses or amounts, no preparation, extraction, or tamper-defeating information, no instructions for any route, no sourcing, and no tips for intensifying or mixing**. Timings are typical ranges from medical and harm-reduction references and vary widely from person to person. Street drugs are frequently contaminated with fentanyl.

If you or someone you know needs help: SAMHSA National Helpline **1-800-662-4357** (free, 24/7). In an emergency call **911** and give naloxone.
