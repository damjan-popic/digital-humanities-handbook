---
title: "Kako preverim omrežno trditev ob izvornih zapisih?"
description: "Preverljiv postopek z izrecnimi viri, modelnimi odločitvami in negotovostjo."
category: "Omrežja"
category_id: "Networks"
difficulty: "srednje"
time: "45–60 min"
tags: [modeliranje, provenienca, negotovost]
status: draft
translation_status: machine-assisted draft; requires human language review
---

# Kako preverim omrežno trditev ob izvornih zapisih?

Strojno podprt prevodni osnutek; potreben je strokovni jezikovni pregled.

## Kaj želite doseči

Preverite, ali trditev »C je vodil skupino« ali »E je posredovala komunikacijo« izhaja iz izbranih zapisov. Od mere ali slike se vrnite k identiteti, pomenu povezave in izvornemu odlomku. Najprej preberite poglavje [Omrežja in vizualizacija](../../chapters/networks-visualization.md).

## Potrebujete

Razpakirajte [spremljevalni ZIP](../../../assets/downloads/contested-models-v1.zip), preberite `input/dossier.sl.md` in zaženite skripto standardne knjižnice Python. Zadostujeta urejevalnik besedila in pregledovalnik CSV. Sintetični dosje omogoča nadzorovani poskus; avtentična časopisna opazovanja ostajajo ločen nasprotni primer na ravni vira.

## Postopek

### 1. Zapišite preverljivo trditev

Navedite graf, populacijo, časovni izbor, pravilo povezave in mero. Pred preskusom »najpomembnejši« zamenjajte z merljivo izjavo. Na primer: »C ima največjo stopnjo med šestimi ohranjenimi osebami v projekciji skupnih dokumentov pri pragu 2.« Te omejene ugotovitve ne zamenjajte za zgodovinsko vodstvo.

### 2. Ponovite rezultat in izberite vzorec pregleda

```bash
python run.py --output output-first
```

Preglejte `projection_t2-metrics.csv` in `correspondence-metrics.csv`. Izberite vidno vozlišče, nepričakovano izolirano vozlišče in različno podprte povezave. Uporabite ta najmanjši pregled:

| Predmet | Podporni zapis | Kaj podpira |
|---|---|---|
| AB | SYN-D1, SYN-D2, SYN-D5 | skupne dokumente; D2 tudi zatrjuje A → B |
| CE | SYN-D3, SYN-D5 | skupne sezname, ne korespondence |
| E → F | SYN-D6 | zatrjevano pismo z verjetnim prejemnikom in februarskim oknom |
| Pari avtentične številke | lokatorji opazovanj AF | sopojavljanje v številki, ne pisem |

Pri odločitvah ohranite polne identifikatorje. Odprite razdelek dosjeja, ki ga določa dokument, ne samo izpeljane tabele povezav.

### 3. Preverite identiteto in čas

Dosje predpostavi identiteto A prek imenskih različic. Pojasnite, katere dodatne dokaze bi potreboval resnični projekt. Preverite, ali bi združitev negotovih identitet združila tudi njihove sosede v lažen most.

Pri D6 ohranite polodprti februarski interval in verjetnega prejemnika. Interval naj ne postane enomesečno razmerje. Agregirani graf zajema leti 1910 in 1925; ne dokazuje sočasne razpoložljivosti vseh poti.

### 4. Preverite konkurenčna pravila

Primerjajte `projection-evidence.csv` in `correspondence-edges.csv`: CE pri pravilu korespondence izgine. Primerjajte vse prejemnike s samo zanesljivo določenimi: izgine E→F. Pri pragu 2 brez D6 postane surova vmesnost E nič namesto štiri. Spremembe zabeležite, namesto da izberete najprepričljivejšo sliko.

Odprite `authentic-issue-cooccurrence.csv` in izvleček izvirnih opazovanj. Štiri posamično poimenovane osebe ustvarijo šest parov samo zato, ker celotna številka velja za eno enoto. Opazovanja podpirajo nič korespondenčnih povezav, ne pa odsotnosti vse resnične korespondence.

### 5. Preverite sklepanje iz slike

Če imate risbo, naštejte trditve, izpeljane iz položaja, bližine, barve ali velikosti. Skupek v razporeditvi na podlagi sil ne dokazuje skupne ideologije. Preverite, ali bi zasuk ali drugačna razporeditev nespremenjenega grafa spremenila besedni argument. Nepodprte interpretacije označite kot nepodprte, ne kot napake zgodovinskega vira.

## Rezultat

Oddajte dnevnik s trditvijo, modelom, mero, lokatorjem vira, obsegom dokaza, alternativnim pravilom in presojo: podprto znotraj modela, potrebuje zunanje dokaze ali nepodprto. Dodajte tabele vozlišč in povezav ter besedilni povzetek. Za dokončanje pregleda virov ogled grafa ni potreben.

## Preverite se

Ali vir zatrjuje narisano razmerje? Je zanesljivost vezana na pravo trditev? Lahko bralec obnovi zavrnjeno interpretacijo? Je občutljive identitete in domnevne vezi primerno objaviti?

## Pogoste pasti

Razporeditev berete kot geografijo; sopojavljanje spremenite v prijateljstvo; neznane datume obravnavate kot sočasne; izolirano vozlišče označite za družbeno osamljeno; matematično skupnost opišete kot dokumentirano politično skupino.

## Naloga

V 150 besedah preoblikujte trditev »E je bila nepogrešljiva posrednica v omrežju«. Poročajte, kateri graf ji pripiše vmesnost, kaj se zgodi brez D6 in katere dodatne dokaze bi potrebovali za dejansko posredovanje. Neuspešno trditev ohranite v dnevniku.
