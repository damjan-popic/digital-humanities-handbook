---
title: "Kako primerjam slog s funkcijskimi besedami?"
description: "Zgradite pregledno stilometrično izhodišče in preverite, ali navidezne avtorske ali žanrske razlike preživijo nadzor dokumentov."
category: "Analiza besedil"
difficulty: "srednje"
time: "90–150 min"
tags: [stilometrija, funkcijske-besede, PCA, dokumentne-značilke]
---

# Kako primerjam slog s funkcijskimi besedami?

<div class="answer-meta" markdown>
<span>Analiza besedil</span><span>srednje</span><span>90–150 min</span>
</div>

## Kaj želite doseči

Želite primerjati slog pisanja s pogostimi slovničnimi besedami, ki so manj odvisne od teme kot polnopomensko besedišče. Cilj je izhodišče za raziskovanje avtorstva, žanra, prevajanja ali obdobja, ne samodejna razsodba o avtorstvu.

## Potrebujete

- po možnosti več dokumentov na skupino;
- primerljive dolžine in žanre ali metapodatke za njihov nadzor;
- dokumentiran seznam funkcijskih besed za jezik;
- Python s paketoma `pandas` in `scikit-learn`.

## Postopek

1. Dolga dela razdelite na primerljive dele, vendar delov istega dela ne mešajte med učno in testno množico.
2. Izbrane besede preštejte po dokumentih in normalizirajte v relativne frekvence.
3. Značilke standardizirajte šele po ločitvi morebitne evalvacijske množice.
4. Prikažite jih s PCA in preverite, katere besede oblikujejo razsežnosti.
5. Primerjajte razdalje znotraj avtorja in med avtorji.
6. Postopek ponovite po nadzoru žanra, obdobja, kakovosti OCR in prevodnega statusa.

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

features = pd.read_csv("output/function_word_frequencies.csv", index_col="doc_id")
X = StandardScaler().fit_transform(features)
coords = PCA(n_components=2, random_state=42).fit_transform(X)
pd.DataFrame(coords, index=features.index, columns=["pc1", "pc2"]).to_csv(
    "output/style_pca.csv"
)
```

## Rezultat

Matrika dokumentov in značilk, dokumentiran seznam besed, raziskovalne koordinate ali razdalje ter analiza občutljivosti.

## Preverite se

- Deli istega dela uhajajo med evalvacijske množice?
- Skupine najprej ločuje žanr ali datum in šele nato avtor?
- Poškodbe OCR spreminjajo kratke, zelo pogoste besede?
- Vzorec preživi drugo množico značilk ali velikost odsekov?

## Pogoste pasti

- graf PCA predstavimo kot klasifikator;
- bližino razlagamo kot literarni vpliv;
- vsako besedilo istega avtorja obravnavamo kot neodvisno;
- značilke izberemo po tem, ko smo že videli želene skupine;
- izpustimo dokumente, ki oslabijo vizualno zgodbo.

## Naloga

Primerjajte vsaj tri dokumente iz dveh skupin. Postopek ponovite z dvema velikostma odsekov ter poročajte o enem stabilnem in enem nestabilnem opažanju.
