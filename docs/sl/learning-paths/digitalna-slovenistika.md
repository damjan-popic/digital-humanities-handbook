---
title: "Digitalna slovenistika"
description: "Nadaljevalna učna pot skozi slovenske in južnoslovanske korpuse, anotacijo, analizo besedil, podatkovne zbirke, GIS, omrežja in ponovljivo raziskovanje."
tags: [predmet, slovenistika, CLASSLA, korpus, ponovljivost]
status: draft
---

# Digitalna slovenistika

## Namen

Učna pot študente usposobi za načrtovanje, izvedbo in kritično interpretacijo računalniških raziskav slovenskega jezika, književnosti in kulturnega gradiva. Tehnično je zahtevnejša od Pismenosti za informacijsko družbo: študenti delajo s strukturiranimi podatki, okolji Python, CLASSLA, relacijskimi podatkovnimi zbirkami in ponovljivimi projektnimi repozitoriji.

Tehnična spretnost ni končni cilj. Vsaka operacija mora ostati povezana s slovenističnim vprašanjem, kritiko virov ter jezikoslovnimi, literarnimi ali zgodovinskimi posledicami modelskih odločitev.

## Predznanje

Študenti naj obvladajo datoteke, tabele CSV, osnovne korpusne pojme, reference in kritično vrednotenje virov. Napredno programiranje ni predvideno, predmet pa uporablja Python 3.12, ukazno vrstico, virtualna okolja in krajše skripte. Študentom brez tega predznanja naj bo na voljo pripravljalna delavnica.

## Učni izidi

Po končani poti bodo študenti znali:

- oblikovati digitalnoslovenistično vprašanje in pregledno raziskovalno zasnovo;
- zgraditi in dokumentirati manjši slovenski ali južnoslovanski korpus;
- uporabiti CLASSLA ter razložiti anotacijske plasti in napake;
- izračunati in preveriti korpusne, slogovne, tematske in čustvene značilke;
- humanistične entitete in razmerja modelirati v SQLite in SQL;
- razrešiti in kartirati prostorske dokaze z negotovostjo;
- zgraditi in kritično presoditi z viri povezano omrežje;
- podatke, kodo in interpretacijo objaviti kot navedljiv in ponovljiv projekt.

## Predlagano zaporedje 14 modulov

### 1. Digitalna slovenistika kot področje

Preberite [Kaj je digitalna humanistika?](../chapters/what-is-digital-humanities.md) in [Od vprašanja do metode](../chapters/research-design.md). Eno tradicionalno slovenistično vprašanje preoblikujte tako, da bodo podatki, enota analize, primerjava in omejitve izrecni.

### 2. Ponovljivo delovno okolje Python

Ustvarite virtualno okolje Python 3.12, namestite pakete, zaženite skripto in inicializirajte repozitorij. Izvedite ustrezne [postopke za Python in NLP](../workflows/nlp/index.md). Oddajte README in specifikacijo okolja.

### 3. Besedilni formati, kodiranje in zasnova korpusa

Preberite [Besedila, korpusi in OCR](../chapters/texts-corpora-ocr.md). Preglejte primere navadnega besedila, CSV, JSON ter TEI/XML. Pripravite kartico korpusa s pravili vzorčenja, identifikatorji dokumentov, metapodatki in pravicami.

### 4. Zajem, OCR, čiščenje in dvojniki

Pridobite ali pripravite manjši dovoljeni korpus. Ohranite surovo in obdelano plast, izmerite vzorec OCR ali zajema, odstranite ponavljajoče se dele ter označite popolne in skorajšnje dvojnike, ne da bi izgubili provenienco.

### 5. Anotacija s CLASSLA

Preberite [Jezikoslovna anotacija in CLASSLA](../chapters/linguistic-annotation-classla.md). Namestite in preizkusite CLASSLA, anotirajte besedilo ter izvozite rezultate na ravni pojavnic. Zabeležite različice modela in programske opreme ter preglejte napake pri slovenskih imenih, nestandardnih oblikah ali zgodovinskem jeziku.

### 6. Konkordance, frekvence, ključne besede in kolokacije

Preberite [Analiza besedil](../chapters/text-analysis.md). Primerjajte dva utemeljena podkorpusa, normalizirajte števila, izračunajte dokumentno frekvenco in preglejte konkordance. Poročajte o vsaj eni meri učinka in eni omejitvi sestave korpusa.

### 7. Slog in signali avtorstva

Iz funkcijskih besed, znakovnih n-gramov ali drugih utemeljenih značilk ustvarite matriko dokumentov in značilk. Prikažite podobnost, preverite občutljivost na dolžino in žanr ter gručenje ločite od dokaza o avtorstvu.

### 8. Teme, sentiment in čustva

Preberite [Teme, sentiment in čustva](../chapters/topics-emotions-classification.md). Pripravite kodirni priročnik in ročno označen vzorec. Primerjajte eno preprosto izhodišče z enim modelom ali tematskim pristopom ter izvedite kvalitativno analizo napak.

### 9. Entitete in relacijski podatki

Preberite [Podatkovne zbirke in SQL](../chapters/databases-sql.md). Samodejno ali ročno določite osebe, kraje, ustanove ali dela, razrešite različice imen ter zasnujte normalizirano shemo SQLite s provenienco in negotovostjo.

### 10. Analiza SQL

Podatke uvozite, uveljavite ključe in napišite shranjene poizvedbe SQL, ki povezujejo entitete, združujejo zapise in razkrivajo manjkajočo pokritost. Rezultat ene poizvedbe izvozite za nadaljnjo analizo, poizvedbo pa ohranite.

### 11. GIS ter literarni in kulturni prostor

Preberite [GIS in prostorska humanistika](../chapters/gis-spatial-humanities.md). Krajevne omembe povežite z ustreznimi imeniki, ohranite alternative in čas ter zgradite zemljevid, katerega legenda pokaže negotovost.

### 12. Omrežja

Preberite [Omrežja in vizualizacija](../chapters/networks-visualization.md). Povezavo določite iz izvornih dokazov, zgradite seznam povezav, primerjajte dvodelni in projicirani pogled ter centralnost razložite samo glede na konstrukcijsko pravilo.

### 13. UI, etika in raziskovalni paket

Preberite [UI, etika in ponovljivost](../chapters/ai-ethics-reproducibility.md). Preglejte licence, zasebnost in reprezentacijsko pristranskost. Dodajte preizkuse, podatke za navajanje, podatkovni slovar, omejitve in izjavo o uporabi UI.

### 14. Izdaja in zagovor

Preberite [Živi odprti priročnik](../chapters/open-living-handbook.md). Označite kandidata za izdajo, projekte izmenjajte za pregled ponovljivosti, odpravite blokirajoče napake ter predstavite vsebinski rezultat in najmočnejši razlog za previdnost.

## Model ocenjevanja

Predlagana razdelitev je:

- **tehnični laboratoriji (25 %)** — ponovljive vaje iz Pythona, CLASSLA, SQL, GIS in omrežij;
- **kritika metode (15 %)** — natančna analiza enega objavljenega ali javnega digitalnega projekta;
- **dosje zasnove korpusa/podatkov (15 %)** — vzorčenje, metapodatki, pravice in načrt preverjanja;
- **končni ponovljivi projekt (35 %)** — podatki, koda, rezultati in interpretacija;
- **medvrstniški pregled in ustni zagovor (10 %)** — ponovitev drugega projekta in zagovor metodoloških odločitev.

Lepota kode ne sme prevladati nad raziskovalno veljavnostjo. Ocenjevanje naj loči tehnično neuspel, vendar dobro diagnosticiran poskus od nepreglednega uspešnega zagona.

## Specifikacija končnega projekta

Projektna izdaja naj vsebuje:

1. eno natančno slovenistično raziskovalno vprašanje;
2. izjavo o virih in pravicah;
3. zasnovo korpusa ali podatkovni model s pravili vključevanja;
4. lokacijo surovih podatkov ali navodila za rekonstrukcijo;
5. dokumentirano predobdelavo in anotacijo;
6. eno glavno metodo in eno strategijo preverjanja;
7. z viri povezane primere, ki podpirajo interpretacijo;
8. vsaj eno tabelo, graf, zemljevid ali omrežje s popolnim napisom;
9. razpravo o napakah, pristranskosti, negotovosti in drugih razlagah;
10. README, okoljsko datoteko, licenco in `CITATION.cff`;
11. označeno izdajo in dnevnik sprememb;
12. krajši prispevek v priročnik, kadar je postopek ponovno uporaben.

## Predlagane teme projektov

Primerne teme so leksikalne ali slovnične spremembe, literarni slog, časopisni diskurz, čustveno okvirjanje, zgodovina prevajanja, imenske entitete v zgodovinskih zbirkah, prostorska pripoved, omrežja korespondence, terminologija, digitalizirana dediščina ali vrednotenje jezikovne tehnologije za slovenščino.

Vprašanje naj bo dovolj ozko za ročno preverjanje. Skromen korpus s preglednimi dokazi je boljši od ogromnega nabora, ki ga študent ne razume.

## Verzioniranje pri predmetu

Za semester določite eno stabilno izdajo priročnika in eno preizkušeno okoljsko datoteko. Ko orodje preneha delovati, spremembo dokumentirajte v živi izdaji in objavite predmetni popravek, namesto da ocenjevana navodila tiho spremenite. Študentski repozitoriji naj zabeležijo točni commit ali izdajo uporabljenih postopkov.
