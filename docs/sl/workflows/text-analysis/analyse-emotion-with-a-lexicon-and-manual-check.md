---
title: "Kako analiziram čustva z leksikonom in ročnim preverjanjem?"
description: "Pripravite pregledno izhodišče za čustveni jezik in izmerite, kje se besede, kontekst in človeške oznake ne ujemajo."
category: "Analiza besedil"
difficulty: "srednje"
time: "90–150 min"
tags: [čustva, leksikon, preverjanje, anotacija]
---

# Kako analiziram čustva z leksikonom in ročnim preverjanjem?

<div class="answer-meta" markdown>
<span>Analiza besedil</span><span>srednje</span><span>90–150 min</span>
</div>

## Kaj želite doseči

Želite oceniti, kje korpus uporablja jezik, povezan s kategorijami, kot so veselje, strah, jeza ali žalost. Leksikon je pregledno izhodišče, vendar ne razkriva notranjega stanja pisca in odpove pri zanikanju, ironiji, navedkih, večpomenskosti ter žanru.

!!! quote "V eni povedi"
    Preštejte dokumentirane čustvene povezave, označite vzorec v kontekstu in poročajte o razliki med leksikalnim signalom ter interpretativno kategorijo.

## Potrebujete

- tabelo dokumentov ali povedi s stabilnimi identifikatorji;
- licenciran čustveni leksikon, primeren jeziku, ali dokumentirano prilagoditev;
- leme, kadar bi pregibanje razpršilo ujemanja;
- kodirni priročnik za človeško kategorijo;
- Python ali preglednico za povezovanje in štetje.

## Postopek

### 1. Določite tarčo

Navedite, ali merite čustvene besede, čustvo, pripisano osebi, pripovedovalčevo stališče, čustveno okvirjanje ali odziv bralca. Izberite eno enoto – poved, odstavek ali dokument – ter opredelite mešane in negotove primere.

### 2. Preglejte leksikon

Zabeležite jezik, vir, kategorije, način anotacije, licenco in izvorno področje. Pri prevedenem leksikonu ročno preglejte kulturno ali oblikoslovno zahtevne vnose. Dvoumne besede odstranite ali označite, ne da bi vsakemu ujemanju tiho zaupali.

### 3. Ustvarite leksikalno izhodišče

```python
import pandas as pd

texts = pd.read_csv("data/sentences.csv")
lexicon = pd.read_csv("data/emotion_lexicon.csv")

rows = []
for row in texts.itertuples():
    lemmas = str(row.lemmas).split()
    matches = lexicon[lexicon["lemma"].isin(lemmas)]
    counts = matches["emotion"].value_counts().to_dict()
    rows.append({"sentence_id": row.sentence_id, **counts})

pd.DataFrame(rows).fillna(0).to_csv("output/lexicon_counts.csv", index=False)
```

### 4. Označite stratificiran vzorec

Vzorčite primere z visokimi ocenami, brez ujemanj, iz različnih žanrov in s pričakovano težavnimi pojavi. Vsaj del vzorca naj po kodirnem priročniku označita dve osebi. Ohranite nesoglasja in razloge.

### 5. Primerjajte signal in presojo

Za odločitveno pravilo ustvarite matriko zamenjav ali, kjer kategorije to dopuščajo, povežite število ujemanj s človeškimi oznakami. Preberite lažno pozitivne in negativne primere. Prilagoditev uvedite le z izrecnim pravilom in jo preverite na drugem vzorcu.

### 6. Odgovorno združujte

Normalizirajte glede na besede ali smiselne enote, prikažite porazdelitve dokumentov in negotovost. Kadar trditev to zahteva, navedeni govor ločite od jezika pripovedovalca ali avtorja.

## Rezultat

Zapis provenience leksikona, kodirni priročnik, tabela štetja po povedih, ročno označen preverjevalni vzorec in analiza napak.

## Preverite se

- Kaj natančno trdi eno ujemanje?
- Ocene povzroča ena pogosta dvoumna beseda?
- Zanikanje ali navedek obrne interpretacijo?
- Prevedene kategorije ustrezajo zgodovinskemu in kulturnemu okolju?
- Lahko vsak zbirni rezultat povežete z odlomki?

## Pogoste pasti

- polarnost imenujemo »čustvo«, ne da bi opredelili enega ali drugega;
- besede literarnega lika razlagamo kot avtorjeva čustva;
- leksikon ocen izdelkov brez preverjanja uporabimo na poeziji;
- skrijemo dokumente brez ujemanj;
- leksikon popravljamo na istih primerih, na katerih poročamo o kakovosti.

## Naloga

Ročno označite 50 povedi, jih primerjajte z leksikalnim pravilom in deset najbolj informativnih napak razvrstite po tipu. Napišite odstavek o tem, kaj leksikon meri dobro, in odstavek o tem, česa ne more meriti.
