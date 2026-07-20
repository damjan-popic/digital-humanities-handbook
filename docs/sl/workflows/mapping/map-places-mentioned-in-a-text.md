---
title: "Kako kartiram kraje, omenjene v besedilu?"
description: "Iz besedila ustvarite pregled krajev, ki ohranja izvorne omembe, identitete, koordinate in negotovost."
category: "Kartiranje"
difficulty: "začetno"
time: "45–90 min"
tags: [kartiranje, geokodiranje, literarna-geografija, kraji]
---

# Kako kartiram kraje, omenjene v besedilu?

<div class="answer-meta" markdown>
<span>Kartiranje</span><span>začetno</span><span>45–90 min</span>
</div>

## Kaj želite doseči

Želite prostorski pregled krajev v besedilu, arhivu ali intervjuju, ne da bi dvoumno ime samodejno spremenili v navidezno natančno koordinato.

## Potrebujete

- besedilo z identifikatorji odlomkov;
- imenik krajev ali drug zanesljiv vir;
- tabelo za omembe, kandidate, izbrane identitete in gotovost;
- QGIS, uMap ali drugo kartografsko orodje.

## Postopek

1. Krajevne omembe izluščite ročno ali z NER ter ohranite odlomek.
2. Ločite resnične, izmišljene, zgodovinske, nejasne in metaforične kraje.
3. Za vsako omembo poiščite možne identitete in zapišite dokaz.
4. Koordinate dodajte samo razrešenim krajem; ohranite uporabljeni CRS.
5. Negotove kandidate prikažite drugače ali jih pustite nekartirane.
6. Zemljevid povežite nazaj z odlomkom in dodajte legendo gotovosti.
7. Napišite interpretacijo izpustov, frekvence omemb in prostorske pokritosti.

## Predlagana tabela

| mention_id | source_text | passage_id | place_id | display_name | latitude | longitude | certainty | evidence |
|---|---|---|---|---|---:|---:|---|---|

## Rezultat

Zemljevid in prenosljiva tabela, v kateri lahko vsako točko povežemo z izvorno omembo in odločitvijo o identiteti.

## Preverite se

- So zgodovinska imena razrešena z obdobju ustreznim virom?
- So dvoumni kraji res razrešeni ali le izbrani po priljubljenosti?
- Je »ni kartirano« dokumentirano?
- Frekvenco omemb pravilno ločite od prisotnosti ali pomembnosti?

## Pogoste pasti

- vsakemu kraju pripišemo eno stabilno točko;
- sodobne meje uporabimo za zgodovinsko trditev brez pojasnila;
- izločimo negotove primere in s tem ustvarimo lažno gotovost;
- zemljevid objavimo brez podatkov, legende in virov.

## Naloga

Kartirajte samo pet krajev. Za vsakega ohranite odlomek, najmanj enega zavrnjenega kandidata ter razlago gotovosti. Omejitev naj nalogo ohrani interpretativno in ne zgolj kartografsko.
