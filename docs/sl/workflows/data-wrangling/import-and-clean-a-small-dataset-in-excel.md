---
title: "Kako manjši podatkovni nabor uvozim in očistim v Excelu?"
description: "CSV uvozite z namerno izbranimi tipi, ohranite identifikatorje, očistite kopirano plast in dokumentirajte vsako spremembo."
category: "Urejanje podatkov"
category_id: "data-wrangling"
difficulty: "začetno"
time: "60–90 min"
tags: [excel, csv, podatkovni-tipi, urejeni-podatki, validacija, provenienca]
---

# Kako manjši podatkovni nabor uvozim in očistim v Excelu?

<div class="answer-meta" markdown>
<span>Urejanje podatkov</span><span>začetno</span><span>60–90 min</span>
</div>

## Kaj želite doseči

Kako lahko manjši izvoz ali kataloško tabelo spremenite v raziskovalne podatke, ne da bi potiho spremenili identifikatorje, datume, decimalke ali negotovost? Excel vrednost najprej interpretira in jo nato prikaže. Če CSV dvokliknete, lahko program sprejme sistemske privzete nastavitve, preden pregledate ločilo, kodiranje, podatkovne tipe stolpcev in območne nastavitve (angl. *locale*), ki določajo razlago decimalnih znamenj, datumov in drugih regionalno odvisnih zapisov.

Surovo datoteko ohranite ter izdelajte dokumentirano očiščeno plast. V raziskovalnem naboru vrstice predstavljajo enote opazovanja, stolpci pa spremenljivke. Okrasna tabela za branje lahko uporablja spojene celice, barvo in več dejstev v eni celici, vendar zato še ni ponovno uporaben podatkovni nabor.

## Potrebujete

- manjšo datoteko CSV ali besedilno datoteko z ločili in jasno opredelitev ene vrstice;
- podatek o ločilu, kodiranju, decimalnem znamenju, datumskih pravilih, kodah za manjkajoče vrednosti in pravicah vira;
- namizni Excel z *Data → From Text/CSV* ali enakovrednim uvoznim vmesnikom;
- [vzorčni paket ZIP](../../../assets/downloads/scholarly-work-foundations-v1.zip) s surovimi podatki, šifrantom, očiščenimi podatki, delovnimi in izhodnimi datotekami, preverjanji ter znanimi težavami.

## Postopek

1. **Kopirajte in opišite surovi vir.** Datoteko `postcards-messy.csv` ohranite nespremenjeno. Zabeležite ustvarjalca, vir, datum prejema ali dostopa, licenco oziroma omejitev, kontrolno vsoto, če je na voljo, ločilo, kodiranje in znane težave. Edinega izvoda ne »popravljajte«.

2. **Opredelite enoto opazovanja.** Napišite na primer: `Ena vrstica predstavlja en kataloški zapis ene razglednice.` Vsaki spremenljivki namenite stolpec in vsakemu opažanju vrstico. Enote navedite v glavah ali podatkovnem slovarju, ne med vrednostmi. V podatkovnem območju ne spajajte celic.

3. **Uvozite skozi podatkovni vmesnik.** Uporabite *Data → From Text/CSV* oziroma *Get Data → Text/CSV*. Preglejte predogled ter nastavite pravo ločilo in izvor oziroma kodiranje datoteke, za vzorec UTF-8. Če je razlaga decimalnih števil ali datumov odvisna od okolja, pred nalaganjem določite ali zabeležite nameravane območne nastavitve. Kadar morate popraviti podatkovne tipe, izberite *Transform Data*.

4. **Identifikatorje zaščitite kot besedilo.** Kataloškim oznakam, signaturam, poštnim številkam in dolgim številčnim identifikatorjem pred pretvorbo določite podatkovni tip *Besedilo (Text)*. Preverite, ali `00127` ostane pet znakov ter ali zapisi, podobni datumom ali znanstvenemu zapisu števil, ostanejo dobesedni, kadar so identifikatorji.

5. **Datume in števila preglejte kot vrednosti.** Prikazani datum lahko skriva drugo serijsko vrednost, decimalna vejica pa se lahko v drugem okolju razcepi ali postane besedilo. Preizkusite znano vrstico. Dvoumni izvorni datum ohranite kot besedilo ter dodajte normalizirani datum in polje natančnosti; dneva si ne izmislite.

6. **Naložite delovno plast in jo spremenite v Excelovo tabelo.** List `Raw` oziroma zunanji vir ohranite samo za branje, popravke pa izvajajte na `Cleaned`. Očiščeno območje pretvorite v poimenovano tabelo z eno glavo. Uporabite filtre in zamrznite prvo vrstico. Znotraj tabele ne vstavljajte praznih vrstic, delnih vsot, opomb ali spojenih naslovov.

7. **Opredelite manjkajoče vrednosti.** Določite razliko med prazno, neznano, nerelevantno, nečitljivo in še nepreverjeno vrednostjo. Raje uporabite polje stanja, kot je `date_status`, kakor več nepojasnjenih simbolov. Vseh manjkajočih vrednosti ne zamenjajte z ničlo, saj je nič opažena vrednost.

8. **Izvedite preverjanja čiščenja.** Poiščite podvojene stabilne identifikatorje, začetne/končne in ponovljene presledke, nedosledne kategorije, kot so `Photograph`, `photo` in `foto`, mešane podatkovne tipe, nemogoče datume ter nepričakovane praznine. Kjer normalizacija spremeni pomen, ohranite `source_value`. Zabeležite vsako pravilo in število prizadetih vrstic.

9. **Omejite prihodnji vnos.** Odobrene kategorije postavite v ločeno šifrantno tabelo in na urejevalne celice uporabite *Data Validation → List*. Dodajte jasno sporočilo o napaki. Validacija omeji nove različice, ne popravi obstoječih vrednosti in ne dokazuje smiselnosti kategorije.

10. **Izvozite premišljeno.** Delovni zvezek shranite kot `.xlsx`, da ohranite tabele, tipe, formule, validacijo, komentarje in liste. Očiščeni `.csv` izvozite samo, ko potrebujete navadno interoperabilno tabelo. CSV ne hrani več listov, oblikovanja, formul kot formul, validacije, grafikonov ali zanesljive sheme tipov. Ob izvozu navedite kodiranje, ločilo, konce vrstic in obliko datuma.

## Rezultat

Pripravite nespremenjeno surovo datoteko, očiščeno tabelo, podatkovni slovar, dnevnik pretvorb, poročilo preverjanja in zapis znanih težav. Očiščeni CSV naj vsebuje iste stabilne identifikatorje kot sprejeta surova opažanja, razen če razliko pojasni dokumentirano pravilo za dvojnike.

Postopek je uspešen, če vsi vzorčni identifikatorji ohranijo začetne ničle, so znaki UTF-8 pravilni, ima vsaka sprememba pravilo, v tabeli ni spojenih celic in ročna primerjava petih vrstic ne pokaže tihe pretvorbe tipov.

## Preverite se

- Ali ena vrstica predstavlja eno opredeljeno enoto in en stolpec eno spremenljivko?
- Ali so identifikatorji besedilo tudi takrat, ko vsebujejo samo števke?
- Ali ločite prazno, neznano in nerelevantno vrednost?
- Ali lahko normalizirane vrednosti povežete z izvornimi?
- Ali izvoz CSV dokumentira, česa ne more ohraniti?

## Pogoste pasti

- CSV dvokliknete in ga shranite po tihi pretvorbi datumov ali identifikatorjev.
- Identifikator oblikujete z začetnimi ničlami, ko so izvorne števke že izgubljene.
- Barvo, komentar ali spojeno celico uporabite kot edini nosilec podatka.
- Popravite surovo plast ali sumljivo vrstico izbrišete brez razloga.
- Domnevate, da validacija popravi obstoječe kategorije.
- CSV obravnavate kot popoln arhiv delovnega zvezka.

## Viri in stanje vmesnika

Vire smo preverili **2. septembra 2026**: Microsoft Support o [uvozu in izvozu besedilnih/CSV-datotek](https://support.microsoft.com/en-us/excel/get-started/import-or-export-text-txt-or-csv-files), [Text Import Wizard](https://support.microsoft.com/en-us/excel/text-import-wizard), [uvozu s Power Queryjem](https://support.microsoft.com/en-us/excel/import-data-from-data-sources-power-query), [Excelovih tabelah](https://support.microsoft.com/en-us/office/overview-of-excel-tables), [validaciji podatkov](https://support.microsoft.com/en-us/office/apply-data-validation-to-cells) in [možnostih uvoza ter analize](https://support.microsoft.com/en-us/excel/data-import-and-analysis-options-in-excel). Oznake in samodejne pretvorbe se razlikujejo med Windows, macOS, spletno, naročniško in trajno izdajo.

## Naloga

Surovi vzorec uvozite brez dvoklika. Ohranite identifikatorje, v kopirani plasti normalizirajte dokumentirane kategorije, opredelite manjkajoče vrednosti, uporabite en validacijski seznam, izvozite očiščeni CSV in pet vrstic primerjajte s surovim besedilom v navadnem urejevalniku.
