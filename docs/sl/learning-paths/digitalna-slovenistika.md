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

## Preverjanje tehnične pripravljenosti

To neoštevilčeno preverjanje opravite **pred prvim modulom**. Z njim vzpostavite skupno tehnično izhodišče; ne šteje kot petnajsti modul. Začnite na vozlišču [Tehnično delovno okolje](../foundations/technical-workspace.md), kjer so razločeni terminal, lupina, WSL, Bash, Git, Python in virtualno okolje.

| Stopnja | Dejavnost in dokaz |
| --- | --- |
| Samo Windows | [Namestite in preverite WSL 2 z Ubuntujem](../workflows/foundations/install-wsl-and-ubuntu-on-windows.md) ter zabeležite `wsl --list --verbose`. Če uporabljate macOS ali Linux, zapišite, zakaj ste WSL preskočili. |
| Vsi | Določite terminal in lupino, nato pa se [z lupino Bash premikajte po zavržljivi mapi](../workflows/foundations/navigate-files-and-directories-with-bash.md). |
| Vsi | [Namestite in nastavite Git](../workflows/foundations/install-and-configure-git.md), vključno z odločitvijo o zasebnosti e-poštnega naslova v potrditvah. |
| Vsi | [Klonirajte manjši začetni repozitorij, ki ga zagotovi izvajalec](../workflows/foundations/clone-run-change-and-commit-a-handbook-project.md). Javni repozitorij GitHub ni potreben. |
| Vsi | [Ustvarite in aktivirajte virtualno okolje Python 3.12](../workflows/nlp/create-a-python-312-virtual-environment.md). |
| Vsi | Z `python -m pip install -r requirements.txt` [namestite pregledane zahteve](../workflows/nlp/install-python-packages-with-pip.md). |
| Vsi | [Zaženite kratko skripto](../workflows/nlp/run-a-python-script-from-terminal.md), preglejte rezultat, v veji spremenite eno neškodljivo oznako, preglejte razliko in ustvarite eno krajevno potrditev. |

Oddajte ali pokažite naslednji izdelek pripravljenosti:

```text
technical-readiness/
├── README.md
├── environment-check.md
├── hello.py
├── requirements.txt
└── output/
```

Repozitorij lahko vsebuje tudi `.gitignore`, licenco in skrite metapodatke Gita. `.venv/` mora ostati nesledena.

V `environment-check.md` zabeležite:

- operacijski sistem, pri sistemu Windows pa tudi različico Ubuntuja in WSL;
- lupino;
- različico Gita;
- različico Pythona;
- natančni ukaz za aktiviranje;
- natančni uspešni ukaz za skripto;
- potrditev, da ste pregledali rezultat in eno potrditev.

Ne vključite gesel, žetonov, zasebnih e-poštnih naslovov ali občutljivih absolutnih poti. Izvajalka ali izvajalec lahko pregleda krajevni repozitorij oziroma sprejme izdelek po odobrenem sistemu ustanove; za oceno pripravljenosti ne potrebujete javnega oddaljenega repozitorija ali zahtevka za vključitev. Če korak ne uspe, oddajte celotno neobčutljivo napako in diagnozo, namesto da bi obšli dovoljenja ali varnostne nadzore.

## Predlagano zaporedje 14 modulov

### 1. Zgodovine področja in slovenski ekosistem

Preberite [Kaj je digitalna humanistika?](../chapters/what-is-digital-humanities.md), [Zgodovine in genealogije digitalne humanistike](../chapters/history-of-digital-humanities.md) ter [Digitalna humanistika v Sloveniji](../chapters/digital-humanities-in-slovenia.md). Raziščite, kako je izbrana slovenistična praksa odvisna od spreminjajočih se poimenovanj, ustanov, jezikovnih virov in sodelovalnega dela, nato pa ločite dokumentirano zgodovino od genealogije, ki jo iz nje izpeljete.

### 2. Modeli, dokazno gradivo, infrastrukture in raziskovalna zasnova

Preberite [Modeli, dokazno gradivo in interpretacija](../chapters/models-evidence-interpretation.md), [Infrastrukture digitalne humanistike](../chapters/critical-infrastructures.md) ter [Od vprašanja do metode](../chapters/research-design.md). Eno slovenistično vprašanje preoblikujte tako, da bodo vir, model, enota analize, primerjava, odvisnost od infrastrukture, dokazno gradivo in omejitve izrecni.

### 3. Ponovljivo delovno okolje Python

Nadaljujte iz uspešnega repozitorija pripravljenosti in namestitve ne ponavljajte. Z [navodili za manjši projekt Python za NLP](../workflows/nlp/structure-a-small-python-nlp-project.md) ga preuredite za omejeno korpusno nalogo; popravite README, neposredne zahteve in `.gitignore`; nato pa z [diagnostičnim postopkom](../workflows/nlp/troubleshoot-python-venv-and-pip.md) preverite, ali lahko kolegica ali kolega okolje znova ustvari. Potrdite specifikacijo okolja, ne `.venv/`, tako da bo podpirala raziskovalno zasnovo iz drugega modula.

### 4. Besedilni formati, zasnova korpusa, zajem, OCR, čiščenje in dvojniki

Preberite [Besedila, korpusi in OCR](../chapters/texts-corpora-ocr.md) ter preglejte primere navadnega besedila, CSV, JSON in TEI/XML. Pripravite kartico korpusa s pravili vzorčenja, identifikatorji dokumentov, metapodatki in pravicami; pridobite ali pripravite manjši dovoljeni korpus; ohranite surovo in obdelano plast; izmerite vzorec OCR ali zajema; ter označite ponavljajoče se dele in dvojnike, ne da bi izgubili provenienco.

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
