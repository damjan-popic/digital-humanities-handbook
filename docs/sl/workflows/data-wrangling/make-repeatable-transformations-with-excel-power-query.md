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

1. **Zabeležite mejo vira.** Surove datoteke prekopirajte v stabilno mapo za vajo in jih med delom s poizvedbo ne urejajte. Zapišite imena, kodiranje, ločilo, locale in pravice. Premaknjen ali preimenovan vir lahko pokvari prvi korak.

2. **Povežite se, ne odpirajte.** Uporabite *Data → Get Data → From File → From Text/CSV* oziroma *From Workbook*. V predogledu preverite izvor in ločilo ter izberite *Transform Data*. Poizvedbo poimenujte `Postcards_Clean`.

3. **Preglejte Applied Steps.** Poiščite *Source*, morebitni *Navigation* in samodejna *Promoted Headers* ali *Changed Type*. Samodejni korak izbrišite ali popravite, če je identifikator ali datum napačno interpretiral. Vsak poznejši korak je odvisen od prejšnjega stanja.

4. **Preimenujte stolpce in določite tipe.** Uporabite stabilna kratka imena. `record_id` nastavite na Text pred številčno pretvorbo; normalizirani datum na Date šele po razjasnitvi locale in dvoumnosti; meritvam določite primeren številski tip. Preimenovanje v Power Queryju ne preimenuje izvornega stolpca.

5. **Besedilo očistite vidno.** Na ustreznih stolpcih uporabite *Format → Trim* za začetne/končne presledke in *Clean* za netiskane znake. Ukaza ne rešita zapisnih različic ali pojmovnih kategorij; zanje zapišite ločena pravila zamenjave.

6. **Razdeljujte po zapisanem pravilu.** Sestavljeni stolpec razdelite po ločilu ali položaju samo, če je meja zanesljiva. Izvorni stolpec ohranite, dokler ročni pregled ne uspe. Pred razdelitvijo in po njej preštejte vrstice, da odkrijete izgubo ali širitev.

7. **Filtrirajte in zamenjajte z razlogom.** Vrstice filtrirajte samo po vključitvenem pravilu, na primer izločitvi označene testne vrstice. Vrednosti zamenjujte po majhnem zemljevidu, ne po spominu. Odločitev `foto → photograph` zabeležite skupaj s številom vrstic in občutljivostjo na velikost črk.

8. **Združite šifrant.** `place-lookup.csv` uvozite kot ločeno poizvedbo. Z *Merge Queries* povežite natančni izvorni ključ, preglejte delež ujemanj in razširite le potrebna normalizirana polja. Neujemanja pustite vidna; mehko ali mnogo-proti-mnogo povezovanje ne sme potiho pomnožiti vrstic.

9. **Odstranite samo utemeljene dvojnike.** Pred *Remove Duplicates* določite ključ in razlog. Razvrstitev lahko vpliva na ohranjeno vrstico, zato najprej določite, kateri zapis preživi in ali sta podobni vrstici res dvojnik ali ločeni opažanji, izdaji oziroma različici. Primerjajte število vrstic in identifikatorje.

10. **Rezultat naložite ločeno.** Uporabite *Close & Load To* in rezultat naložite kot tabelo na list `Query Result` ali po potrebi samo kot povezavo. Surovega vira ne prepišite. V README ali posebnem listu vsak Applied Step prevedite v raziskovalni razlog.

11. **Po nadzorovani spremembi osvežite.** V kopijo vira dodajte priloženo vrstico in uporabite *Data → Refresh All*. Preverite, ali gre skozi vsako pravilo, ali združevanje deluje in ali se števila posodobijo. Osvežitev ponovi poizvedbo, ne preveri interpretacije.

12. **Diagnosticirajte pokvarjeni korak.** V zavržljivi kopiji preimenujte izvorni stolpec in osvežite. V urejevalniku klikajte Applied Steps od vrha navzdol ter poiščite prvo napako. Korak popravite šele po presoji, ali se je shema upravičeno spremenila. Preverite vse poznejše korake, saj se sklici verižno pokvarijo.

## Nadomestna vaja za drugo platformo

Razpoložljivost Power Queryja, povezovalnikov, ustvarjanja in osveževanja se razlikuje med Windows, macOS, spletnim Excelom, licencami in izdajami. Če na dodeljeni platformi poizvedbe ne morete ustvariti, iste raziskovalne odločitve izvedite na kopiranem listu `Cleaned` in vodite oštevilčen dnevnik: vhodno število, operacija, stolpec, pravilo, izhodno število in ročno preverjanje. Nato datoteko izmenjajte z osebo, ki lahko požene živo poizvedbo. Nadomestna vaja doseže nizkopražni učni izid, če je postopek res ponovljiv; ročnih popravkov ne predstavlja kot Power Query.

## Rezultat

Pripravite nespremenjeni vir, šifrant, delovni zvezek z listom `Query Result`, izvoženi očiščeni CSV, popis Applied Steps, preizkus osvežitve, uskladitev števila vrstic in diagnozo enega pokvarjenega koraka.

Postopek je uspešen, če osvežitev po dodani vrstici ponovi vse pretvorbe, identifikatorji ostanejo besedilo, združevanje ne pomnoži opažanj, odstranitev dvojnikov ustreza pravilu in lahko določite prvi pokvarjeni korak.

## Preverite se

- Ali lahko ločeno pokažete vir, poizvedbo in naloženi rezultat?
- Ali ima vsak Applied Step raziskovalni razlog in ne samo imena gumba?
- Ali se števila vrstic po filtrih, povezavah in odstranitvi dvojnikov ujemajo?
- Ali osvežitev vključi novo vrstico brez ročnega urejanja rezultata?
- Ali lahko neujemanje v šifrantu ostane vidno in ne prisiljeno?

## Pogoste pasti

- Sprejmete samodejni *Changed Type*, ki odstrani začetne ničle.
- Urejate naloženi rezultat in pričakujete, da bo sprememba preživela osvežitev.
- Kategorije zamenjate brez zemljevida ali pravila velikih črk.
- Povežete neenolične ključe in pomnožite vrstice.
- Dvojnike odstranite brez odločitve o ohranjenem zapisu.
- Popravljate zadnjo napako namesto prve prekinjene odvisnosti.

## Viri in stanje vmesnika

Vire smo preverili **2. septembra 2026**: Microsoft Support o [Power Queryju v Excelu](https://support.microsoft.com/en-us/excel/about-power-query-in-excel), [ustvarjanju, nalaganju in urejanju poizvedbe](https://support.microsoft.com/en-us/excel/create-load-or-edit-a-query-in-excel-power-query), [uvozu virov](https://support.microsoft.com/en-us/excel/import-data-from-data-sources-power-query), [preimenovanju stolpcev in poznejših korakih](https://support.microsoft.com/en-us/excel/rename-a-column-power-query), [združevanju poizvedb](https://support.microsoft.com/en-us/office/merge-queries-power-query) in [virih Power Query po različicah Excela](https://support.microsoft.com/en-us/office/power-query-data-sources-in-excel-versions). Pred ocenjevanjem preverite trenutni nabor funkcij svoje platforme.

## Naloga

Izdelajte vzorčno poizvedbo, jo osvežite po dodani vrstici in nato v zavržljivi kopiji preimenujte izvorni stolpec. Zabeležite prvi neuspešni korak, ga popravite ter uskladite vhodne, neujemajoče, podvojene, izločene in izhodne vrstice.
