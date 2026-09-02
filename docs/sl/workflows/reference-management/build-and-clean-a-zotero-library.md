---
title: "Kako ustvarim in očistim knjižnico Zotero?"
description: "Zberite manjši nabor humanističnih virov, popravite bibliografske metapodatke ter ločeno ohranite priponke, zapiske in odločitve o pravicah."
category: "Upravljanje virov"
category_id: "reference-management"
difficulty: "začetno"
time: "60–90 min"
tags: [zotero, metapodatki, bibliografija, viri, preverjanje-kakovosti]
---

# Kako ustvarim in očistim knjižnico Zotero?

<div class="answer-meta" markdown>
<span>Upravljanje virov</span><span>začetno</span><span>60–90 min</span>
</div>

## Kaj želite doseči

Kako lahko o viru ohranite dovolj podatkov, da ga boste znova našli, pravilno navedli in pojasnili, kaj ste dejansko pregledali? Uvoz v Zotero ustvari predlog bibliografskega zapisa, ne pa dokaza, da so katalog, podatkovna zbirka, register DOI ali spletna stran poslali pravilne metapodatke.

V postopku boste ustvarili manjšo preverjeno knjižnico. Ločili boste vir, njegovo enoto v Zoteru, pripeti PDF ali posnetek spletne strani ter svoj bralni zapisek. Spodnje oznake opisujejo trenutni namizni Zotero in Connector; njihov položaj se lahko spremeni.

## Potrebujete

- pet namerno raznolikih virov, med njimi knjigo, članek, spremenljivo spletno stran, podatkovni nabor ali programsko opremo;
- dostop do naslovne strani, kolofona, kataloga, zapisa DOI, pristajalne strani ali popisa, s katerim boste podatke preverili;
- [Zotero](https://www.zotero.org/download/) in ustrezni [Zotero Connector](https://www.zotero.org/download/connectors) iz uradnega vira;
- zapisano odločitev, ali smete priponke prenesti, sinhronizirati ali deliti.

[Vzorčni paket ZIP](../../../assets/downloads/scholarly-work-foundations-v1.zip) vsebuje vajo z identifikatorji, pet zapisov RIS, znane metapodatkovne težave in podatke o pravicah. Gre za učno gradivo in ne za dokaz o resnični zgodovinski trditvi.

## Postopek

1. **Namestite iz uradnega vira.** Namestite namizni Zotero in nato Connector za podprti brskalnik. Če se integracija ne prikaže, znova zaženite brskalnik ali urejevalnik besedil. Na institucionalnem računalniku boste morda potrebovali skrbniško pomoč.

2. **Ustvarite projektno zbirko.** V *My Library* ustvarite zbirko `Preizkus znanstvenega dela`. Zbirka je bolj podobna seznamu predvajanja kot datotečni mapi: isto enoto povlecite v `Pisanje`, `Podatki` in `Za preverjanje`, ne da bi ustvarili dvojnike v knjižnici. Podzbirke uporabite samo, če podpirajo resnično iskalno potrebo.

3. **Zapise dodajte na štiri načine.** V knjižničnem katalogu ali znanstveni podatkovni zbirki odprite celotni zapis in uporabite *Save to Zotero*. Preverjeni DOI in ISBN dodajte z *Add Item by Identifier*. Vir, ki ga samodejni uvoz ne podpira, ustvarite z *New Item* in ustrezno vrsto enote. Raje shranite pristajalno stran vira kot neposredni PDF: PDF je navadno priponka nadrejene bibliografske enote in ni enota sama.

4. **Najprej preverite vrsto enote.** Napačno uvožena spletna stran, poglavje, poročilo, naloga, podatkovni nabor ali članek prikaže napačna polja in se lahko nepravilno izpiše. Enoto v Zoteru primerjajte z virom, ne le z drugim agregatorjem.

5. **Preglejte polja, ki oblikujejo navedbo.** Preverite vloge in vrstni red ustvarjalcev, naslov in podnaslov, naslov matične oziroma nadrejene publikacije, datum, letnik in številko, obseg strani, izdajo, založnika, DOI ali ISBN, spletni naslov in datum dostopa. Korporativnega avtorja ohranite kot organizacijo. V polje URL ne vnesite povezave do kataloškega zapisa, če dela niste pregledali tam. Za spremenljivi spletni vir zabeležite datum dejanskega dostopa.

6. **Zabeležite popravek.** Dodajte kratek podrejeni zapisek, na primer `Metapodatki preverjeni po naslovni strani in pristajalni strani DOI, 2026-09-02; popravljena številka in obseg strani.` Uvoženi metapodatki so izhodišče. Zelena ikona Connectorja ali DOI ne potrdita samodejno vsakega polja.

7. **Različne funkcije uporabljajte ločeno.** Zbirke uporabite za pripadnost projektu, oznake za teme ali stanja, kot sta `prebrano` in `metapodatki-preverjeni`, zapiske pa za sledljiva opažanja. V zavihku *Related* povežite recenzijo z recenzirano knjigo ali podatkovni nabor z dokumentacijo. Povezava omogoča premikanje med enotami; ne združi zapisov.

8. **Prave dvojnike združite previdno.** Odprite *Duplicate Items*, primerjajte kandidate, izberite najboljše vrednosti glavnega zapisa in uporabite *Merge*. Preverite, ali so ostali zapiski, oznake, zbirke in priponke. Dve izdaji, prevoda, različici ali arhivska izvoda so lahko povezani, vendar različni viri; ne združite jih samo zaradi podobnega naslova.

9. **Preverite vzorec petih enot.** Izberite namerno raznolike zapise, pri katerih se uporabljajo različna polja. Za vsakega označite uspeh ali neuspeh pri vrsti enote, ustvarjalcih, naslovu, nadrejeni publikaciji, datumu, lokatorskih poljih, trajnem identifikatorju, URL-ju in datumu dostopa ter stanju priponke. Metapodatke popravite v bibliografskem zapisu v Zoteru, namesto da bi ročno popravljali vsako prihodnjo navedbo.

10. **Odločite se o sinhronizaciji.** Zotero lahko sinhronizira podatke knjižnice in zapiske; shramba priponk je ločeno vprašanje. Osebni račun je koristen za več naprav, skupinska knjižnica pa za skupne zapise, če članstvo in dovoljenja ustrezajo projektu. Avtorsko varovanih PDF-jev, omejenih posnetkov, osebnih podatkov ali licenčnih izvozov ne pošiljajte v skupino ali oblak brez ustrezne pravne podlage. Bibliografski zapis je lahko deljiv, čeprav priponka ni.

## Rezultat

Pripravite:

```text
preverjanje-knjiznice-zotero/
├── pregled-petih-enot.csv
├── dnevnik-popravkov-metapodatkov.md
├── odlocitev-o-priponkah-in-sinhronizaciji.md
└── izvoz-knjiznice.ris
```

Postopek je uspešen, če se vseh pet zapisov v ustreznih poljih ujema z avtoritativnim virom, nobena priponka ni zamenjana z nadrejeno enoto in ima vsaka sinhronizirana datoteka dokumentirano pravno podlago.

## Preverite se

- Ali je isti vir v več zbirkah kot ena knjižnična enota in ne kot več kopij?
- Ali so avtorji, uredniki, prevajalci in korporativni ustvarjalci v pravilnih vlogah in vrstnem redu?
- Ali lahko ločite uvožene podatke od tistih, ki ste jih preverili?
- Ali ločite izdaje, prevode in različice od pravih dvojnikov?
- Ali lahko bibliografski zapis delite, ne da bi nedovoljeno delili priponko?

## Pogoste pasti

- Shranite samo PDF in navajate ime datoteke ali naslov, izluščen iz PDF-ja.
- Uvoženo rabo velikih začetnic, vrstni red ustvarjalcev, datum ali vrsto enote obravnavate kot avtoritativno.
- Oznake, zbirke, povezane enote in združevanje dvojnikov uporabljate, kot da bi opravljali isto nalogo.
- DOI zamenjate z začasnim naslovom seje v podatkovni zbirki.
- Sinhronizacijo priponk vključite pred preverjanjem avtorskih pravic, zasebnosti in dovoljenj skupine.

## Viri in stanje vmesnika

Vire smo preverili **2. septembra 2026**: uradna navodila Zotero [Basics](https://www.zotero.org/support/quick_start_guide), [Adding Items](https://www.zotero.org/support/adding_items_to_zotero), [Item Types and Fields](https://www.zotero.org/support/kb/item_types_and_fields), [Collections and Tags](https://www.zotero.org/support/collections_and_tags), [Duplicate Detection](https://www.zotero.org/support/duplicate_detection), [Syncing](https://www.zotero.org/support/sync) in [Group Libraries](https://www.zotero.org/support/groups). Pojmovna preverjanja ostanejo veljavna tudi po premiku gumbov; oznake primerjajte s trenutno uradno stranjo.

## Naloga

Pet vzorčnih zapisov uvozite na najmanj tri načine. Namerno popravite eno vlogo ustvarjalca, eno vrsto enote, eno polje nadrejene publikacije in en datum dostopa. Isti vir dodajte v dve zbirki, združite en pravi dvojnik in pojasnite, zakaj mora en podoben zapis ostati ločen.
