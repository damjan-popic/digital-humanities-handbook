---
title: "Podatki, metapodatki in modeli"
description: "Kako humanistično gradivo postane strukturiran podatek, ne da bi izgubili izvor, negotovost in kontekst."
tags: [podatki, metapodatki, modeliranje, izvor]
status: draft
---

# Podatki, metapodatki in modeli

## Učni cilji

Po tem poglavju boste znali:

- razlikovati med podatki, metapodatki in dokumentacijo;
- oblikovati stabilne identifikatorje in preprost tabelarni podatkovni model;
- izrecno predstaviti izvor, negotovost in manjkajoče vrednosti;
- prepoznati, kdaj mora preglednica postati relacijska podatkovna zbirka;
- presoditi, ali shema odraža raziskovalno vprašanje ali zgolj obliko razpoložljivega vira.

## Pred začetkom

Odprite tabelo, ki ste jo že uporabili pri raziskavi. Ali lahko brez vprašanja avtorju ugotovite, kaj predstavlja ena vrstica, kateri stolpci so obvezni, kaj pomenijo prazne celice, od kod izvirajo vrednosti in katero različico gledate? Če ne, težava ni samo v »neurejenih podatkih«, temveč v manjkajočem pomenu.

To poglavje se posveča praktični zgradbi podatkov in dokumentaciji. Širšo spoznavno razlago prehoda od virov in modelov do dokaznega gradiva razvija poglavje [Modeli, dokazno gradivo in interpretacija](models-evidence-interpretation.md).

## Podatki, metapodatki in dokumentacija

V humanistični raziskavi so **podatki** zabeležena opazovanja ali predstavitve, ki jih uporabljamo kot dokaz. **Metapodatki** opisujejo predmete, zapise ali postopke: naslov, datum, ustvarjalca, vir, jezik, pravice, zbirko, koordinate, stanje prepisa ali različico anotacije. **Dokumentacija** pojasni, kako so podatki in metapodatki nastali ter kako jih moramo razlagati.

Razlika je odvisna od vprašanja. Datum izdaje je lahko pri iskanju po korpusu metapodatek, v raziskavi zgodovine založništva pa postane analizirani podatek.

Trden projekt ohranja vse tri ravni:

- vir ali stabilno sklicevanje nanj;
- strukturirane zapise, uporabljene pri analizi;
- dokumentacijo preoblikovanj in odločitev.

## Kaj pomeni ena vrstica?

Najpomembnejše vprašanje pri oblikovanju tabele je **enota opazovanja**. Ena vrstica naj predstavlja eno jasno določeno stvar: dokument, osebo, kraj, dogodek, poved, anotacijo ali razmerje.

Mešanje ravni povzroča napake. Tabela z eno vrstico na avtorja in več naslovi knjig v isti celici ne more zanesljivo odgovarjati na vprašanja o knjigah. Tabele z eno vrstico na časopisno številko in temami člankov v seznamih, ločenih z vejicami, ni mogoče nedvoumno filtrirati ali šteti.

Koristen preizkus je dopolnitev povedi:

> Vsaka vrstica predstavlja natanko en/eno ________.

Če je možnih več odgovorov, podatke razdelite v povezane tabele.

## Identifikatorji pred imeni

Imena so oznake, ne stabilni identifikatorji. Ljudje spreminjajo imena; kraji imajo zgodovinske in večjezične različice; naslovi se ponavljajo; zapis je nedosleden. Vsaki entiteti dodelite stabilen notranji identifikator, na primer `oseba_0042` ali `kraj_0187`, imena pa shranite kot lastnosti ali različice.

Identifikator naj bo:

- enkraten znotraj projekta;
- obstojen med različicami;
- po možnosti brez občutljivega pomena;
- nikoli tiho ponovno uporabljen;
- povezan z zunanjimi identifikatorji, kot so Wikidata, VIAF ali GeoNames, kadar je to primerno, vendar brez domneve, da je zunanje razreševanje vedno pravilno.

## Manjka, ni znano ali ni relevantno

Prazna celica je nevarno dvoumna. Lahko pomeni:

- vrednost ni znana;
- vrednost ni bila zabeležena;
- polje ni relevantno;
- vir ni čitljiv;
- vrednost je namenoma prikrita;
- delo še ni končano.

Določite izrecno pravilo. V analitični tabeli je lahko primerna strojno berljiva manjkajoča vrednost, vendar ohranite ločen status ali opombo, kadar so različne vrste negotovosti zgodovinsko pomembne.

Neznanih vrednosti ne nadomeščajte z ničlo, razen če je nič dejansko opažena vrednost. »Ni evidentiranih pisem« ni isto kot »napisanih je bilo nič pisem«.

## Nadzorovani slovarji in odprto besedilo

Nadzorovani slovarji omogočajo primerjavo: `roman`, `poezija`, `esej` namesto številnih zapisnih različic. Fiksne kategorije pa lahko izbrišejo dvoumnost in vsilijo sodobne razlike.

Praktična rešitev ohrani:

- nadzorovano polje za analizo;
- izvirno poimenovanje iz vira;
- opombo ali stopnjo zaupanja;
- dokument slovarja z definicijami kategorij in zgodovino sprememb.

Kategorij naj bo dovolj malo za dosledno uporabo in dovolj veliko za raziskovalno vprašanje. Kategorija »drugo« je pogosto potrebna, vendar jo je treba pregledovati, ne pa uporabljati kot koš za nelagodje.

## Izvor in preoblikovanje

Vsako izpeljano vrednost mora biti mogoče izslediti. Zabeležite vsaj:

- identifikator in lokacijo vira;
- datum pridobitve;
- uporabljeno metodo ali skripto;
- različico programske opreme ali modela, kadar je pomembna;
- osebo ali proces, odgovoren za spremembo;
- ročne popravke;
- razmerje med surovimi, očiščenimi in analiziranimi datotekami.

Pogosta struktura map loči `data/raw`, `data/interim`, `data/processed` in `output`. Surovi podatki naj bodo po možnosti samo za branje. Popravki sodijo v dokumentirano preoblikovanje ali tabelo popravkov, ne v tiho prepisovanje.

## Kdaj preglednica ne zadošča več

Preglednica je odlična za pregled in majhne ploščate zbirke. O relacijski podatkovni zbirki razmislite, kadar:

- ima ena oseba več del in eno delo več oseb;
- zapisi potrebujejo stabilna razmerja med tabelami;
- ponavljajoče se besedilne vrednosti povzročajo nedoslednost;
- podatke ureja ali poizveduje več ljudi;
- so pomembna pravila celovitosti;
- projekt potrebuje ponovno uporabne poizvedbe.

Odločitev ni stvar prestiža. Podatkovna zbirka je koristna, kadar so razmerja in omejitve del dokazov.

## Razdelan primer: podatki o korespondenci

Projekt korespondence bi lahko uporabljal štiri tabele:

- `osebe(oseba_id, prednostno_ime, leto_rojstva, ...)`
- `pisma(pismo_id, datum_besedilo, datum_od, datum_do, vir_id, ...)`
- `udelezenci_pisem(pismo_id, oseba_id, vloga)`
- `kraji(kraj_id, prednostno_ime, sirina, dolzina, ...)`

Tabela udeležencev omogoča več pošiljateljev, prejemnikov, oseb v vednost ali negotovih vlog brez stolpcev `prejemnik_2` in `prejemnik_3`. Datum je predstavljen kot izvirni niz in kot računski interval, zato lahko ohranimo negotovost, na primer »pomlad 1898«.

## Vaja

Za majhno humanistično zbirko pripravite:

1. podatkovni slovar z imenom polja, definicijo, tipom, dovoljenimi vrednostmi in pravilom za manjkajoče vrednosti;
2. pet vzorčnih zapisov;
3. opombo o izvoru, ki pojasni eno preoblikovanje;
4. seznam entitet, ki potrebujejo stabilne identifikatorje.

## Refleksija

- Katere kategorije izvirajo iz zgodovinskega vira in katere iz vaše raziskovalne zasnove?
- Bi drug raziskovalec lahko rekonstruiral izpeljano vrednost iz vaših zapisov?
- Kaj prazna celica pomeni v posameznem polju?

## Povzetek

Podatkovna struktura je operacionalizirana interpretacija. Jasne enote opazovanja, stabilni identifikatorji, izrecna manjkajočnost, dokumentirani slovarji in izvor omogočajo analizo, ne da bi se pretvarjali, da so kulturni dokazi čistejši ali zanesljivejši, kot so. Podatkovno zbirko uporabimo, ko so pomembna razmerja in omejitve, ne zgolj zato, ker so podatki »resni«.
