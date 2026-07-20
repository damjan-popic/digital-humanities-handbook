---
title: "Kako s CLASSLA anotiram majhno besedilo?"
description: "Eno slovensko besedilo UTF-8 tokenizirajte, lematizirajte in označite z besednimi vrstami ter rezultat ročno preglejte."
category: "NLP"
difficulty: "začetno"
time: "30–60 min"
tags: [CLASSLA, slovenščina, tokenizacija, lematizacija, besedne-vrste]
---

# Kako s CLASSLA anotiram majhno besedilo?

<div class="answer-meta" markdown>
<span>NLP</span><span>začetno</span><span>30–60 min</span>
</div>

## Kaj želite doseči

Imate kratko slovensko besedilo in želite ustvariti identifikatorje povedi in pojavnic, besedne oblike, leme ter oznake besednih vrst. Najprej obdelajte eno datoteko in šele nato cel korpus.

!!! quote "V eni povedi"
    Obdelajte eno navadno besedilno datoteko, izvozite anotacijo, jo ročno preglejte in šele nato povečajte obseg.

## Potrebujete

- Python 3.12 in preizkušen CLASSLA;
- preneseni slovenski model;
- eno navadno besedilno datoteko UTF-8;
- mape `data/raw/`, `output/` in `scripts/`.

## Postopek

### 1. Ustvarite vhod

V `data/raw/sample-sl.txt` zapišite:

```text
Digitalna humanistika povezuje jezik, podatke in interpretacijo.
Majhni preizkusi preprečijo velike napake.
```

### 2. Ustvarite skripto

V `scripts/annotate_classla_txt.py`:

```python
from pathlib import Path
import classla

input_path = Path("data/raw/sample-sl.txt")
output_path = Path("output/sample-sl.tsv")
output_path.parent.mkdir(exist_ok=True)
text = input_path.read_text(encoding="utf-8")

nlp = classla.Pipeline("sl", processors="tokenize,pos,lemma")
doc = nlp(text)
rows = ["sent_id\tword_id\ttext\tlemma\tupos"]

for sent_id, sentence in enumerate(doc.sentences, start=1):
    for word in sentence.words:
        rows.append(f"{sent_id}\t{word.id}\t{word.text}\t{word.lemma}\t{word.upos}")

output_path.write_text("\n".join(rows) + "\n", encoding="utf-8")
print(f"Zapisano: {output_path}")
```

### 3. Zaženite in preglejte

```bash
python scripts/annotate_classla_txt.py
```

Odprite `output/sample-sl.tsv` in ročno preverite 10–20 pojavnic: meje povedi, ločila, leme, glagole, lastna imena ter šumnike.

## Rezultat

Datoteka TSV z identifikatorjem povedi, identifikatorjem besede, besedilno obliko, lemo in oznako UPOS.

## Preverite se

- Lahko vsako izhodno vrstico povežete z vhodom?
- So meje povedi in ločila smiselni?
- Kje je model negotov ali očitno napačen?
- Ste ohranili ime izvorne datoteke za poznejši korpus?

## Pogoste pasti

- PDF ali Word neposredno pošljemo v jezikoslovni procesor;
- prvi rezultat razglasimo za pravilen;
- velik korpus obdelamo pred pregledom vzorca;
- pri združevanju datotek izgubimo identifikator dokumenta.

## Naloga

Anotirajte slovensko besedilo s 5–10 povedmi. Naključno izberite 20 pojavnic ter zapišite tri pravilne, eno negotovo in eno napačno anotacijo.
