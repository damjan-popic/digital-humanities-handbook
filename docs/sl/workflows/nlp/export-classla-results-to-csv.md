---
title: "Kako rezultate CLASSLA izvozim v CSV?"
description: "Anotirane dokumente pretvorite v urejeno tabelo z identifikatorji dokumentov, povedi in pojavnic."
category: "NLP"
difficulty: "srednje"
time: "45–90 min"
tags: [CLASSLA, CSV, pandas, metapodatki]
---

# Kako rezultate CLASSLA izvozim v CSV?

<div class="answer-meta" markdown>
<span>NLP</span><span>srednje</span><span>45–90 min</span>
</div>

## Kaj želite doseči

Več besedil želite anotirati in združiti v tabelo, ne da bi izgubili identiteto dokumenta ali strukturo povedi.

## Postopek

1. Za vsako vhodno datoteko določite stabilni `doc_id`.
2. Besedilo preberite kot UTF-8 in ga anotirajte z enako procesno verigo.
3. Za vsako besedo shranite `doc_id`, `sent_id`, `word_id`, `form`, `lemma`, `upos` in po potrebi morfološke ali odvisnostne oznake.
4. Metapodatke dokumentov hranite v ločeni tabeli in jih povežite z `doc_id`.
5. CSV zapišite z izrecnim kodiranjem ter preizkusite ponovni uvoz.

```python
from pathlib import Path
import pandas as pd
import classla

nlp = classla.Pipeline("sl", processors="tokenize,pos,lemma")
rows = []

for path in sorted(Path("data/raw").glob("*.txt")):
    doc_id = path.stem
    doc = nlp(path.read_text(encoding="utf-8"))
    for sent_id, sentence in enumerate(doc.sentences, 1):
        for word in sentence.words:
            rows.append({
                "doc_id": doc_id,
                "sent_id": sent_id,
                "word_id": word.id,
                "form": word.text,
                "lemma": word.lemma,
                "upos": word.upos,
            })

pd.DataFrame(rows).to_csv("output/tokens.csv", index=False, encoding="utf-8")
```

## Rezultat

Tabela pojavnic, ki jo lahko povežete z dokumentnimi metapodatki in ponovno uvozite brez izgube šumnikov.

## Preverite se

- Je kombinacija dokumenta, povedi in besede enolična?
- So vsi vhodni dokumenti zastopani?
- Ohranite prazne ali neuspešne dokumente v dnevniku obdelave?
- Lahko iz tabele rekonstruirate vrstni red besed?

## Pogoste pasti

- uporabimo samo zaporedno številko besede in izgubimo dokument;
- metapodatke ponovimo v vsaki vrstici brez nadzorovanega vira;
- CSV odpremo in shranimo v programu, ki spremeni kodiranje ali identifikatorje;
- sploščimo večbesedne pojavnice in odvisnosti brez dokumentacije.
