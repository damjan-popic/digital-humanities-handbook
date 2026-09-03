---
title: "Kako modeliram spreminjajoča se krajevna imena in meje?"
description: "Preverljiv postopek z izrecnimi viri, modelnimi odločitvami in negotovostjo."
category: "Kartiranje"
category_id: "Mapping"
difficulty: "srednje"
time: "60–90 min"
tags: [modeliranje, provenienca, negotovost]
status: draft
translation_status: machine-assisted draft; requires human language review
---

# Kako modeliram spreminjajoča se krajevna imena in meje?

Strojno podprt prevodni osnutek; potreben je strokovni jezikovni pregled.

## Kaj želite doseči

Ugotovite, ali drugačna ozemeljska oznaka pomeni gibanje, upravno spremembo ali negotovo identifikacijo. Ohranite večjezična izvorna imena in nerazrešene kandidate, namesto da jih nadomestite z eno sodobno koordinato. Preberite poglavji [GIS in prostorska humanistika](../../chapters/gis-spatial-humanities.md) ter [Podatkovne zbirke in SQL](../../chapters/databases-sql.md).

## Potrebujete

Razpakirajte [spremljevalni ZIP](../../../assets/downloads/contested-models-v1.zip). Uporabite Python 3.10+ in pregledovalnik CSV ali urejevalnik besedila. Geometrija meje in kandidata za »St. Peter« so izrecno sintetični; niso prerisani z avtentičnega načrta. Za tabelarično pot GIS ni potreben.

## Postopek

### 1. Ločite predmete opisa

V mapi `input/` preberite `dossier.sl.md`, `candidates.csv`, `places.csv`, `boundaries.csv` in `assertions.csv`. Omemba kraja je del opisa delovišča, ne spremembe bivališča. Ohranite zapis »St. Peter«, oba identifikatorja kandidatov, vir, datum in odprto odločitev.

Pri novem zgodovinskem viru dodajte vrstico za vsako večjezično imensko trditev z jezikom, kontekstom, intervalom in virom. Iz današnjega prednostnega imena ne sklepajte o njegovi zgodovinski veljavnosti. Kandidata v vaji imata enako ime; nobeden ni samodejno sprejet.

### 2. Določite časovna in geometrijska pravila

Lokalni inženirski kvadrat sega od 0 do 1.000 m po obeh oseh. Ločnica je pred letom 1920 pri x=500, pozneje pri x=600. Zahod pomeni x pod ločnico; vzhod vključuje ločnico. Intervali so polodprti. Koordinate niso EPSG:3794 in ne sodijo na zemljepisno podlago.

Čas objave vira ločite od predstavljenega obdobja. Stalno bivališče A je predpostavljena trditev za leta 1910–1925; spreminjajoča se meja je druga trditev. Resnična raziskava bi za obe potrebovala neodvisne vire.

### 3. Ponovite pripis po središču in ob negotovosti

```bash
python run.py --output output-first
python query.py --database output-first/dossier.sqlite --subject SYN-L1 --as-of 1920-01-01
```

Odprite `output-first/membership.csv`.

| Kraj | Središčni x | Pred 1920 | Od 1920 | Ob ±75 m |
|---|---:|---|---|---|
| SYN-L1 | 550 | vzhod | zahod | obe pripadnosti možni v obeh obdobjih |
| SYN-L2 | 800 | vzhod | vzhod | samo vzhod |

Razpon ±75 m je predpostavka občutljivosti, ne verjetnostna porazdelitev. Možna geometrijska pripadnost ne prepiše pripadnosti, ki jo zatrjuje vir. Pojasnite razliko.

### 4. Ohranite dvoumnost v rezultatu

Za vsakega kandidata in obdobje pripravite vrstico z izvirnim imenom, identifikatorjem, podlago geometrije, središčno pripadnostjo, možnimi pripadnostmi in stanjem odločitve. Nerazrešeno omembo štejte enkrat, ne kot dve delovišči ali dve osebi. Navedite dokaz, ki bi kandidata ločil: datirani opis ulice, okoliška imena ali itinerar konkretnega vira.

Če narišete shemo, jo označite kot sintetično in priložite tabelo. Pri resnični prilagoditvi v GeoPackage ohranite ločene datirane mejne objekte z identifikatorji, povezanimi s tabelo trditev. Starega poligona ne prepišite z novim.

### 5. Preverite drugo predpostavko

V kopiji paketa negotovost L1 spremenite na nič in ponovite izračun v novi mapi. Pripadnost postane enolična v vsakem obdobju, sprememba po središčni točki pa ostane. Vrnite izvirnik in pojasnite, zakaj poskus ne dokazuje natančnega resničnega položaja. Ločeno preverite 1919-12-31 in 1920-01-01 za kontrolo krajišč intervala.

## Rezultat

Oddajte časovno opredeljeno tabelo, dnevnik odločitev o kandidatih, opombo o datumu vira in predstavljenem času ter primerjavo občutljivosti. Tabelarični prikaz je popoln rezultat; zemljepisno delujoč zemljevid teh inženirskih koordinat bi zavajal.

## Preverite se

Sta oba kandidata še vidna? Je delovišče brez dokaza postalo bivališče? So stare meje obnovljive? Je negotovost označena kot predpostavka? Lahko bralec razbere natančno pravilo pripisa?

## Pogoste pasti

Neopazno sprejetje prvega zadetka imenika, razglasitev mejne spremembe za selitev, štetje kandidatnih vrstic kot oseb in enačenje datuma izdaje načrta z datumom vsakega prikazanega pojava.

## Naloga

V 150 besedah odgovorite na vprašanje »Ali se je A preselila?«. Ločite predpostavljeno bivališče, spreminjajočo se središčno pripadnost, položajno negotovost in nerazrešeno omembo delovišča. Navedite poizvedljivo razliko in razliko, ohranjeno v prozi.
