---
title: "Kako v Excelovem Power Queryju izdelam ponovljive pretvorbe?"
description: "V Power Queryju zabeležite manjši postopek od surovih do očiščenih podatkov, ga po spremembi vira osvežite in diagnosticirajte pokvarjeni korak."
category: "Urejanje podatkov"
category_id: "data-wrangling"
difficulty: "začetno"
time: "60–90 min"
tags: [excel, power-query, pretvorba, osvežitev, provenienca]
---

# Kako v Excelovem Power Queryju izdelam ponovljive pretvorbe?

<div class="answer-meta" markdown>
<span>Urejanje podatkov</span><span>začetno</span><span>60–90 min</span>
</div>

## Kaj želite doseči

Kako lahko po spremembi izvorne datoteke ponovite iste odločitve čiščenja? Ponavljajoče ročno urejanje celic pokaže končno stanje, ne postopka. Power Query shrani urejeno zaporedje pretvorb in ga ob osvežitvi znova izvede, surovi vir pa pusti nespremenjen.

Ločite tri plasti: **izvorno datoteko**, **poizvedbo** z operacijami in **naloženi rezultat** v Excelu. Rezultat ni drugi surovi vir, tipkanje vanj pa ni zanesljiv način spreminjanja poizvedbe.

## Potrebujete

- eno manjšo datoteko CSV ali delovni zvezek ter ločeno šifrantno tabelo krajev;
- podatkovni slovar in napisano pravilo za dvojnike;
- različico Excela, ki za potrebne povezovalnike ponuja Power Query oziroma *Get & Transform*;
- [vzorčni paket ZIP](../../../assets/downloads/scholarly-work-foundations-v1.zip). Njegov delovni zvezek pokaže načrtovane plasti in dnevnik korakov, vi pa na svoji platformi izdelate živo poizvedbo.

## Postopek

1. **Zabeležite mejo vira.** Surove datoteke prekopirajte v stabilno mapo za vajo in jih med delom s poizvedbo ne urejajte. Zapišite imena, kodiranje, ločilo, pravice in območne nastavitve (angl. *locale*), ki določajo razlago decimalnih znamenj, datumov in drugih regionalno odvisnih zapisov. Premaknjen ali preimenovan vir lahko pokvari prvi korak.

2. **Povežite se, ne odpirajte.** Uporabite *Data → Get Data → From File → From Text/CSV* oziroma *From Workbook*. V predogledu preverite izvor in ločilo ter izberite *Transform Data*. Poizvedbo poimenujte `Postcards_Clean`.

3. **Preglejte Applied Steps.** Poiščite *Source*, morebitni *Navigation* in samodejna *Promoted Headers* ali *Changed Type*. Samodejni korak izbrišite ali popravite, če je identifikator ali datum napačno interpretiral. Vsak poznejši korak je odvisen od prejšnjega stanja.

4. **Preimenujte stolpce in določite podatkovne tipe.** Uporabite stabilna kratka imena. Stolpcu `record_id` določite podatkovni tip *Besedilo (Text)* pred kakršno koli številsko pretvorbo; normaliziranemu datumu določite tip *Datum (Date)* šele po razjasnitvi območnih nastavitev in dvoumnosti; meritvam pa določite ustrezen številski tip. Preimenovanje v Power Queryju ne preimenuje izvornega stolpca.

5. **Korake čiščenja besedila zabeležite posebej.** Na ustreznih stolpcih uporabite *Format → Trim* za začetne in končne presledke ter *Clean* za netiskane znake. Ukaza ne odpravita zapisnih različic ali pojmovnih razlik med kategorijami; zanje določite ločena, dokumentirana pravila zamenjave.

6. **Razdeljujte po zapisanem pravilu.** Sestavljeni stolpec razdelite po ločilu ali položaju samo, če je meja zanesljiva. Izvorni stolpec ohranite, dokler ročni pregled ne uspe. Pred razdelitvijo in po njej preštejte vrstice, da odkrijete izgubo ali širitev.

7. **Filtrirajte in zamenjajte z razlogom.** Vrstice filtrirajte samo po vključitvenem pravilu, na primer izločitvi označene testne vrstice. Vrednosti zamenjujte po preglednici preslikav oziroma šifrantu, ne po spominu. Odločitev `foto → photograph` zabeležite skupaj s številom vrstic in podatkom, ali pravilo razlikuje med velikimi in malimi črkami.

8. **Združite šifrant.** `place-lookup.csv` uvozite kot ločeno poizvedbo. Z *Merge Queries* povežite natančni izvorni ključ, preglejte delež ujemanj in razširite le potrebna normalizirana polja. Neujemanja pustite vidna. Približno povezovanje (angl. *fuzzy matching*), ki sprejme podobne in ne le enakih nizov, ter povezovanje mnogo-proti-mnogo uporabite samo z izrecnim pravilom in preverjanjem; sicer lahko potiho pomnožita vrstice.

9. **Dvojnike odstranite po izrecnem pravilu.** Če so vrstice popolnoma enake v vseh pomembnih poljih, izberite ta polja in odstranite ponovljeno enako vrstico. Če imajo kandidati isti ključ, v drugih poljih pa se razlikujejo, se ne zanašajte na vidni vrstni red: Power Query pri `Table.Distinct` zaradi optimizacije in izvajanja dela poizvedbe pri viru na splošno ne zagotavlja, kateri kandidat bo ostal. Najprej določite nedvoumno prednostno pravilo, skupino z indeksom ali dokumentirano pravilo za ohranitev in izločitev, ki izbere enega kandidata; nato filtrirajte po tem pravilu. Na koncu zabeležite ohranjene in izločene identifikatorje ter uskladite število vrstic.

10. **Rezultat naložite ločeno.** Uporabite *Close & Load To* in rezultat naložite kot tabelo na list `Query Result` ali po potrebi samo kot povezavo. Surovega vira ne prepišite. V README ali posebnem listu vsak Applied Step prevedite v raziskovalni razlog.

11. **Po nadzorovani spremembi osvežite.** V kopijo vira dodajte priloženo vrstico in uporabite *Data → Refresh All*. Preverite, ali gre skozi vsako pravilo, ali združevanje deluje in ali se števila posodobijo. Osvežitev ponovi poizvedbo, ne preveri interpretacije.

12. **Diagnosticirajte pokvarjeni korak.** V zavržljivi kopiji preimenujte izvorni stolpec in osvežite. V urejevalniku klikajte Applied Steps od vrha navzdol ter poiščite prvo napako. Korak popravite šele po presoji, ali se je shema upravičeno spremenila. Preverite vse poznejše korake, saj se sklici verižno pokvarijo.

## Nadomestna vaja za drugo platformo

Razpoložljivost Power Queryja, povezovalnikov, ustvarjanja in osveževanja se razlikuje med Windows, macOS, spletnim Excelom, licencami in izdajami. Če na dodeljeni platformi poizvedbe ne morete ustvariti, iste raziskovalne odločitve izvedite na kopiranem listu `Cleaned` in vodite oštevilčen dnevnik: vhodno število, operacija, stolpec, pravilo, izhodno število in ročno preverjanje. Nato datoteko izmenjajte z osebo, ki lahko požene dejansko poizvedbo. Nadomestna vaja doseže učni izid z nizkim tehničnim pragom, če je postopek res ponovljiv; ročnih popravkov ne predstavlja kot Power Query.

## Rezultat

Pripravite nespremenjeni vir, šifrant, delovni zvezek z listom `Query Result`, izvoženi očiščeni CSV, popis Applied Steps, preizkus osvežitve, uskladitev števila vrstic in diagnozo enega pokvarjenega koraka.

Postopek je uspešen, če osvežitev po dodani vrstici ponovi vse pretvorbe, identifikatorji ostanejo besedilo, združevanje ne pomnoži opažanj, enake dvojnike odstranite varno, med različnimi kandidati pa izberete z izrecnim ponovljivim pravilom, nato uskladite ohranjene identifikatorje in število vrstic ter določite prvi pokvarjeni korak.

## Preverite se

- Ali lahko ločeno pokažete vir, poizvedbo in naloženi rezultat?
- Ali ima vsak Applied Step raziskovalni razlog in ne samo imena gumba?
- Ali se števila vrstic po filtrih, povezavah in odstranitvi dvojnikov ujemajo?
- Ali osvežitev vključi novo vrstico brez ročnega urejanja rezultata?
- Ali lahko neujemanje v šifrantu ohranite vidno, ne da bi ga na silo povezali z napačnim zapisom?

## Pogoste pasti

- Sprejmete samodejni *Changed Type*, ki odstrani začetne ničle.
- Urejate naloženi rezultat in pričakujete, da bo sprememba preživela osvežitev.
- Kategorije zamenjate brez zemljevida ali pravila velikih črk.
- Povežete neenolične ključe in pomnožite vrstice.
- Domnevate, da vidni vrstni red določa, kateri od različnih podvojenih kandidatov bo ostal.
- Popravljate zadnjo napako namesto prve prekinjene odvisnosti.

## Viri in stanje vmesnika

Vire smo preverili **2. septembra 2026**: Microsoft Support o [Power Queryju v Excelu](https://support.microsoft.com/en-us/excel/about-power-query-in-excel), [ustvarjanju, nalaganju in urejanju poizvedbe](https://support.microsoft.com/en-us/excel/create-load-or-edit-a-query-in-excel-power-query), [uvozu virov](https://support.microsoft.com/en-us/excel/import-data-from-data-sources-power-query), [preimenovanju stolpcev in poznejših korakih](https://support.microsoft.com/en-us/excel/rename-a-column-power-query), [združevanju poizvedb](https://support.microsoft.com/en-us/office/merge-queries-power-query) in [virih Power Query po različicah Excela](https://support.microsoft.com/en-us/office/power-query-data-sources-in-excel-versions); Microsoft Learn pa o funkciji [`Table.Distinct`](https://learn.microsoft.com/en-us/powerquery-m/table-distinct) in nezagotovljeni izbiri ohranjene vrstice. Pred ocenjevanjem preverite trenutni nabor funkcij svoje platforme.

## Naloga

Izdelajte vzorčno poizvedbo, jo osvežite po dodani vrstici in nato v zavržljivi kopiji preimenujte izvorni stolpec. Zabeležite prvi neuspešni korak, ga popravite ter uskladite vhodne, neujemajoče, podvojene, izločene in izhodne vrstice.
