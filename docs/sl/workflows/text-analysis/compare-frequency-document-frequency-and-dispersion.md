---
title: "Kako primerjam frekvenco, dokumentno frekvenco in razpršenost?"
description: "Na neenakomernem slovenskem učnem korpusu ločite ponavljanje, dokumentni doseg in porazdelitev po delih korpusa."
category: "Analiza besedil"
difficulty: "začetno"
time: "45–75 min"
tags: [frekvenca, dokumentna-frekvenca, razpršenost, konkordanca, slovenščina]
status: draft
translation_status: machine-assisted draft; requires human language review
---

# Kako primerjam frekvenco, dokumentno frekvenco in razpršenost?

!!! warning "Stanje prevoda"
    Slovensko besedilo je strojno podprti uredniški osnutek. Pred formalno
    objavo potrebuje vsebinski in jezikovni pregled strokovnjaka za slovenščino.

<div class="answer-meta" markdown>
<span>Analiza besedil</span><span>začetno</span><span>45–75 min</span>
</div>

## Kaj želite doseči

Pri več dokumentih želite ločiti tri trditve: kolikokrat se izraz pojavi, koliko
dokumentov ga uporablja in kako enakomerno je razporejen po pomenljivih delih
korpusa. Pred razlago števil boste pregledali konkordance.

!!! quote "V eni povedi"
    Frekvenca meri ponavljanje, dokumentna frekvenca doseg, razpršenost pa
    zgoščenost v navedeni razdelitvi.

## Potrebujete

- kopijo repozitorija ali
  [učni paket za preverjanje besedilnih analiz in NLP](../../../assets/downloads/text-nlp-validation-v1.zip);
- Python 3.12 za ponovno gradnjo pripravljenih tabel;
- pregledovalnik preglednic ali urejevalnik besedila; in
- pojme iz poglavja [Analiza besedil](../../chapters/text-analysis.md).

Dvanajst dokumentov je sintetično učno gradivo. Namenoma so neenakomerni in niso
dokaz o resničnih ustanovah, žanrih ali slovenski rabi.

## Vhodi in rezultati

| Datoteka | Vloga |
| --- | --- |
| `source/contemporary-sample.csv` | dvanajst dokumentov s stabilnimi identifikatorji, avtorsko temo in pravicami |
| `output/document-summary.csv` | imenovalci upravičenih pojavnic po dokumentih |
| `output/frequency-dispersion.csv` | frekvenca, DF, dokumentni delež, Juillandov D in štiri skupinska števila |
| `output/concordance.csv` | vsaka ujemajoča se pojavitev z omejenim kontekstom |
| `validation/expected-values.json` | izbrane nespremenljivke za preverjanje |

Deterministični gradilnik uporabi Unicode NFC, male črke in zaporedja najmanj
dveh črk. Ne lematizira. Štiri avtorske tematske skupine – arhivi, muzeji, jezik
in časopisje – imajo po tri dokumente, zato učni izračun Juillandovega D
uporablja enake dele.

## Postopek

### 1. Ponovno zgradite tabele

V korenu repozitorija zaženite:

```bash
make text-nlp-validation
```

Ukaz pred ustvarjanjem tabel preveri vhode in zamrznjene artefakte. Modela NLP ne
namesti ali prenese.

### 2. Pred skupnimi merami preglejte dokumente

Odprite `source/contemporary-sample.csv` in `output/document-summary.csv`.
Preverite stabilni `doc_id`, temo, `synthetic=true`, izjavo o pravicah in
imenovalec pojavnic. Razvrstite po številu pojavnic ter presodite, ali bi najdaljši
dokument lahko prevladal v absolutnem številu.

Meje dokumentov so tu določene za vajo. V raziskavi so to lahko članki, pisma,
knjige, številke ali govori. Sprememba meje spremeni DF, tudi če znaki ostanejo
isti.

### 3. Primerjajte tri različne izraze

V `output/frequency-dispersion.csv` poiščite `arhiv`, `korpus` in `svoboda`. Za
vsak izraz zapišite:

- skupno frekvenco;
- normalizirano frekvenco na 10.000 upravičenih pojavnic;
- dokumentno frekvenco in dokumentni delež;
- števila v štirih tematskih skupinah; in
- Juillandov D.

Izrazov ne razvrstite le po enem stolpcu. Povejte, na katero vprašanje odgovori
posamezni stolpec. Ponavljana beseda ima lahko visoko frekvenco in nizko DF;
izraz lahko doseže več dokumentov, vendar ostane v eni tematski skupini.

Potrjena tabela občutljivosti pokaže obrat:

| Izbira | `svoboda` | `raziskovalci` | Posledica |
| --- | ---: | ---: | --- |
| frekvenca natančne oblike | 9 / 330 pojavnic, 1. mesto med štirimi izrazi | 2 / 330, 4. mesto | prevlada ponavljanje v dolgem dokumentu |
| dokumentna frekvenca | 1 / 12 dokumentov, 4. mesto | 2 / 12, 2. mesto | manj pogosti izraz ima širši dokumentni doseg |

Razvrstitev uporablja padajoči števec, izenačenja pa razreši po zapisu Unicode.
Ne določa boljšega izraza, ampak odgovarja na različni vprašanji.

### 4. Frekvenco in DF preverite ročno

`output/concordance.csv` filtrirajte na en izraz. Število vrstic mora ponoviti
frekvenco, število različnih vrednosti `doc_id` pa DF. Preverite:

```text
dokumentni_delež = dokumentna_frekvenca / 12
normalizirana_frekvenca = frekvenca / vse_upravičene_pojavnice * 10.000
```

Formuli uporabljata različna imenovalca. Zapis »izraz je v 16,7 % korpusa« je
dvoumen: lahko govori o dokumentih, pojavnicah ali bajtih. Enoto poimenujte.

### 5. Ponovno izračunajte razpršenost

Za en neničelni izraz vzemite štiri tematska števila. Izračunajte povprečje in
populacijski standardni odklon, nato:

```text
D = 1 - (populacijski_standardni_odklon / povprečje) / sqrt(4 - 1)
```

Rezultat primerjajte s šestdecimalno vrednostjo v tabeli. Če so vse pojavitve v
eni temi, je D enak 0; pri enakih skupinskih številih je 1. Vmesna vrednost je
pomenljiva le skupaj s štirimi števili.

Preproste formule ne uporabite, kadar se deli korpusa razlikujejo po velikosti.
Izberite prilagojeno mero ali dokumentne porazdelitve.

### 6. Preberite vse konkordančne vrstice

Za tri izraze preglejte `left_context`, `match` in `right_context`. Celotni
dokument odprite, če govorec, zanikanje ali argument presega okno. Vsako pojavitev
označite kot pomembno, dvoumno ali nepomembno za vprašanje, ki ga določite. S tem
ustvarite novo anotacijsko plast, zato dokumentirajte pravilo.

Preverite, ali ponovitev izhaja iz namernega nasprotja, seznama, naslova ali
obrazca. Frekvenca tega sama ne pove.

### 7. Preizkusite eno alternativo

Premislek ponovite ob spremenjeni izbiri: upoštevanje velikosti črk, lema namesto
oblike, dokumentna namesto tematske razpršenosti ali največ ena pojavitev na
dokument. Celotnega paketa ni treba znova izračunati. Napovejte spremembo in jo
preverite na majhnem vzorcu.

Cilj je odkriti občutljivost, ne izbrati pretvorbo, ki najmočneje podpre želeno
zgodbo.

## Rezultat

Napišite kratko dokazno beležko, ki vsebuje:

- opredelitev korpusa in tokenizacije;
- izraz, obliko poizvedbe in izvorno plast;
- absolutno in normalizirano frekvenco z imenovalcem;
- DF z dokumentnim imenovalcem;
- poimenovano mero razpršenosti, razdelitev in skupinska števila;
- eno razlago, podprto s konkordanco;
- en nasprotujoč ali dvoumen kontekst; in
- omejitev posploševanja.

## Preverite se

- Lahko drug bralec obnovi vsak imenovalec?
- Je frekvenca enaka številu konkordančnih vrstic?
- Je DF enaka številu različnih identifikatorjev dokumentov?
- D spremljajo razdelitev in skupinska števila?
- Ste opisali sintetični nabor in ne slovenskega diskurza?

## Pogoste pasti

- Pogost izraz razglasite za razširjenega brez preverjanja DF.
- Visoko DF razglasite za enakomerno razpršenost brez skupinskih števil.
- Primerjate normalizirane mere z različnimi pravili upravičenih pojavnic.
- Poljubno datotečno mejo obravnavate kot zgodovinsko mejo dokumenta.
- Okno KWIC berete, kot da vsebuje celoten argument.
- Juillandov D za enake dele uporabite na močno neenakih delih korpusa.

## Naloga

Izberite dodatna izraza s podobno frekvenco, vendar različno DF ali
razpršenostjo. Razliko pojasnite s konkordancami. Nato zasnujte primerljiv vzorec
resničnega korpusa ter naštejte metapodatke, preglede OCR in presojo pravic, ki
jih potrebujete pred ponovitvijo izračuna.

Končajte s trditvijo, ki poimenuje enoto in mero, na primer: »V dvanajstih
sintetičnih dokumentih ima natančna mala oblika *svoboda* frekvenco pojavnic 9,
dokumentno frekvenco pa 1/12; ponavlja se krajevno in ni široko razporejena.«
