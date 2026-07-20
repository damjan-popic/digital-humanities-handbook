---
title: "Kako zgradim omrežje sopojavljanja, povezano z viri?"
description: "Povezave ustvarite iz skupnih enot ter ohranite prizore, dokumente ali dogodke, ki utemeljujejo vsako povezavo."
category: "Omrežja"
difficulty: "srednje"
time: "90–150 min"
tags: [omrežje, sopojavljanje, dvodelno, NetworkX]
---

# Kako zgradim omrežje sopojavljanja, povezano z viri?

<div class="answer-meta" markdown>
<span>Omrežja</span><span>srednje</span><span>90–150 min</span>
</div>

## Kaj želite doseči

Entitete so povezane s skupnimi enotami – literarni liki s prizori, osebe s pismi, kraji z dokumenti – in želite zgraditi omrežje. Najprej ohranite tabelo entitet in enot; projicirani seznam povezav je izpeljani pogled.

## Potrebujete

- CSV s poljema `unit_id` in `entity_id`, en par na vrstico;
- jasno opredelitev skupne enote;
- Python s paketoma `pandas` in `networkx`;
- sklice na vire za vsako enoto.

## Postopek

```python
from itertools import combinations
from collections import Counter
import pandas as pd

memberships = pd.read_csv("data/entity_unit.csv")
edges = Counter()
evidence = {}

for unit_id, group in memberships.groupby("unit_id"):
    entities = sorted(set(group["entity_id"]))
    for left, right in combinations(entities, 2):
        edges[(left, right)] += 1
        evidence.setdefault((left, right), []).append(unit_id)

rows = [
    {"source": a, "target": b, "weight": weight,
     "evidence_units": "|".join(evidence[(a, b)])}
    for (a, b), weight in edges.items()
]
pd.DataFrame(rows).to_csv("output/edges.csv", index=False)
```

Seznam povezav nato naložite v NetworkX, Gephi ali Cytoscape. Stopnjo izračunajte šele po pregledu velikosti enot; en velik prizor ustvari veliko projiciranih povezav.

## Rezultat

Izvirna dvodelna tabela entitet in enot, izpeljani seznam povezav z identifikatorji dokazov ter vizualizacija z dokumentiranim pragom.

## Preverite se

- Skupna enota res pomeni razmerje, ki ga trdite?
- So različice imen in dvojniki razrešeni?
- Velike enote prevladujejo v projekciji?
- Lahko vsako povezavo odprete nazaj do izvornega dokaza?
- Kaj se zgodi, ko odstranite negotova članstva?

## Pogoste pasti

- po projekciji zavržemo dvodelno tabelo;
- utež brez razlage obravnavamo kot moč odnosa;
- osamljene entitete izločimo iz objavljenih podatkov;
- prag izberemo le zato, da je graf privlačen;
- silno usmerjeno postavitev beremo kot geografijo ali kronologijo.

## Naloga

Omrežje zgradite dvakrat: z vsemi skupnimi enotami ter brez enot nad 90. percentilom velikosti. Pojasnite, katere centralnosti se spremenijo in kaj to pove o pravilu povezave.
