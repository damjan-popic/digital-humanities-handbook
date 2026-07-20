---
title: "Kako z NMF raziščem ponavljajoče se teme?"
description: "Zgradite interpretabilen model dokumentov in izrazov, preglejte značilna besedila ter preverite, ali teme preživijo spremembo parametrov."
category: "Analiza besedil"
difficulty: "srednje"
time: "90–150 min"
tags: [NMF, tematska-analiza, TF-IDF, preverjanje]
---

# Kako z NMF raziščem ponavljajoče se teme?

<div class="answer-meta" markdown>
<span>Analiza besedil</span><span>srednje</span><span>90–150 min</span>
</div>

## Kaj želite doseči

Želite raziskovalni pregled ponavljajočih se besednih vzorcev po dokumentih. Nenegativna matrična faktorizacija (NMF) matriko dokumentov in izrazov TF-IDF razstavi na sestavine, ki jih raziskovalci lahko razložijo kot teme.

!!! quote "V eni povedi"
    Prilagodite več manjših modelov NMF, preglejte najpomembnejše besede in celotne dokumente ter poročajte o stabilnih vzorcih, ne o eni izvedbi kot odkriti resnici.

## Potrebujete

- CSV s polji `doc_id`, `text` in uporabnimi metapodatki;
- vsaj nekaj deset dokumentov, po možnosti več;
- Python s paketoma `pandas` in `scikit-learn`;
- dokumentirano pravilo za nepolnopomenske besede in normalizacijo.

## Postopek

### 1. Preglejte uravnoteženost korpusa

Preštejte dokumente in besede po obdobju, viru in žanru. Odstranite popolne dvojnike ter določite, ali boste zelo kratke dokumente združili ali izločili.

### 2. Zgradite izhodiščni model

```python
import pandas as pd
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer

frame = pd.read_csv("data/documents.csv")
vectorizer = TfidfVectorizer(
    lowercase=True, min_df=3, max_df=0.85,
    ngram_range=(1, 2), max_features=8000,
)
X = vectorizer.fit_transform(frame["text"].fillna(""))
model = NMF(n_components=8, init="nndsvda", random_state=42, max_iter=500)
W = model.fit_transform(X)
H = model.components_
terms = vectorizer.get_feature_names_out()

for topic_id, weights in enumerate(H):
    top = weights.argsort()[-12:][::-1]
    print(topic_id, ", ".join(terms[top]))
```

### 3. Preglejte dokumente in ne le besed

Za vsako sestavino izpišite dokumente z največjo utežjo in jih preberite. Začasno oznako zapišite šele, ko ugotovite, kaj dokumente povezuje in kaj ji nasprotuje.

```python
for topic_id in range(W.shape[1]):
    top_docs = W[:, topic_id].argsort()[-5:][::-1]
    print("TEMA", topic_id, frame.loc[top_docs, ["doc_id", "title"]])
```

### 4. Preverite občutljivost

Postopek ponovite z drugim številom sestavin, pravili besedišča in naključnimi semeni. Zapišite, katere teme ostanejo, se razcepijo, združijo ali izginejo. Primerjajte jih s preprosto analizo ključnih besed ali metapodatkov.

### 5. Ustvarite interpretacijsko tabelo

Za vsako prikazano sestavino shranite najpomembnejše izraze, reprezentativne in nasprotujoče si dokumente, razširjenost po metapodatkih, oznako, stopnjo gotovosti in opombe.

## Rezultat

Verzionirana tabela nastavitev in interpretiranih sestavin, povezave do izvornih dokumentov ter opomba o občutljivosti.

## Preverite se

- Sestavine ustvarjajo napake OCR, ponavljajoča se predloga ali en sam vir?
- Ste prebrali celotne dokumente ali poimenovali temo iz desetih besed?
- Vzorec preživi drugo razumno nastavitev?
- Je oznaka ožja od dokazov?

## Pogoste pasti

- število sestavin izberemo samo zato, ker je rezultat urejen;
- koherentnost ali napako rekonstrukcije obravnavamo kot humanistično sodbo;
- odstranimo vse pogoste besede, preden preverimo njihov žanrski ali zgodovinski pomen;
- rišemo razširjenost brez negotovosti na ravni dokumentov;
- sestavine imenujemo »teme, o katerih so ljudje govorili«, čeprav so besedni vzorci v vzorčenem korpusu.

## Naloga

Prilagodite modele s 6, 8 in 10 sestavinami. Izberite en ponavljajoč se vzorec in napišite 300-besedno interpretacijo, podprto s tremi dokumenti in enim nasprotnim primerom.
