---
title: "Kako podatke povzamem z vrtilnimi tabelami in preglednimi grafikoni?"
description: "Na omejeno vprašanje odgovorite s preverjeno vrtilno tabelo in zadržanim grafikonom z jasnim virom, enoto, imenovalcem in manjkajočimi vrednostmi."
category: "Urejanje podatkov"
category_id: "data-wrangling"
difficulty: "začetno"
time: "60–90 min"
tags: [excel, vrtilna-tabela, grafikon, imenovalec, preverjanje]
---

# Kako podatke povzamem z vrtilnimi tabelami in preglednimi grafikoni?

<div class="answer-meta" markdown>
<span>Urejanje podatkov</span><span>začetno</span><span>60–90 min</span>
</div>

## Kaj želite doseči

Kako so kataloški zapisi razporejeni po dokumentiranih kategorijah in katere sklepe takšna porazdelitev podpira? Vrtilna tabela odgovori na določeno agregacijsko vprašanje, grafikon pa predstavi izbrane vrednosti. Nobeden ne izbere veljavnega imenovalca in ne razloži zgodovinskega pomena namesto vas.

Začnite z urejenimi, preverjenimi podatki: ena vrstica na enoto opazovanja, ena spremenljivka na stolpec, stabilni identifikatorji, izrecne manjkajoče vrednosti in brez spojenih celic v tabeli.

## Potrebujete

- očiščeno Excelovo tabelo in podatkovni slovar;
- zapisano vprašanje s populacijo, skupinsko spremenljivko, mero in izključitvami;
- dnevnik od surovih do očiščenih podatkov in znane manjkajoče kategorije;
- [vzorčni paket ZIP](../../../assets/downloads/scholarly-work-foundations-v1.zip), kjer delovni zvezek, povzetek, podatki za grafikon in ročna preverjanja tvorijo pregledno verigo.

## Postopek

1. **Napišite agregacijsko vprašanje.** Ločite `Koliko vrstic?`, `Kolikšna je vsota številske mere?`, `Kakšno je povprečje med nepraznimi opažanji?` in `Koliko je različnih dokumentov?` Ponovljeni dokument lahko povzroči razliko med številom vrstic in enoličnih dokumentov.

2. **Izberite imenovalec in pravilo manjkajočih vrednosti.** Navedite, ali populacijo tvorijo vse uvožene vrstice, sprejeti očiščeni zapisi, samo zapisi z znanim datumom ali druga podmnožica. Odločite, ali je `unknown` vidna kategorija, izključen iz deleža z opombo ali del imenovalca. Privzeto skrivanje praznin v vrtilni tabeli ne sme odločiti namesto vas.

3. **Vstavite vrtilno tabelo.** Izberite celico v poimenovani očiščeni tabeli in uporabite *Insert → PivotTable*. Preverite tabelo/obseg in rezultat postavite na novi list `Pivot Check`. Izvorna tabela naj ostane nespremenjena.

4. **Polja razporedite namerno.** Skupinsko polje postavite v *Rows*, mero pa v *Values*. Odprite *Value Field Settings* ter po vprašanju izberite Count, Sum ali Average. Za število različnih dokumentov uporabite *Distinct Count*, kjer ga podpirata različica Excela in Data Model; sicer izdelajte pregledno razdvojeno kontrolno tabelo in nadomestilo dokumentirajte.

5. **Razkrijte manjkajoče kategorije.** Preglejte filtre in oznake vrstic. Potrdite, da so prazne, neznane in nerelevantne vrednosti obravnavane po pravilu. Pri majhnem imenovalcu poleg deleža pokažite tudi število.

6. **Po spremembi vira osvežite.** Če je vir Excelova tabela ali rezultat poizvedbe, po novi vrstici oziroma posodobitvi uporabite *Refresh*. Preverite, ali vir vrtilne tabele še vedno obsega prave podatke in ali filter ni ohranil zastarelega stanja kategorij.

7. **Ročno preverite podmnožico.** Izberite manjšo kategorijo z največ petimi vrsticami. Izvorno tabelo filtrirajte, naštejte vključene ID-je ter ročno preštejte ali izračunajte mero. Rezultat primerjajte z vrtilno tabelo, zabeležite uspeh/neuspeh in razliko razrešite pred grafikonom.

8. **Pripravite tabelo za grafikon.** Kopirajte ali povežite samo kategorije in preverjene vrednosti, potrebne za sporočilo. Pomožna tabela naj ostane sledljiva do vrtilne ali izvorne tabele. Nepojasnjenih vrednosti ne prilepite v nepovezani grafikon.

9. **Izberite en zadržan grafikon.** Razvrščeni stolpčni ali palični grafikon je primeren za manjšo primerjavo kategorij, črtni pa za urejeno časovno vrsto. Izognite se 3D-učinkom, prelivom, okrasnim ikonam in barvi brez pomena. Ko so pomembne natančne vrednosti, je lahko tabela jasnejša.

10. **Označite dokazno gradivo.** Dodajte opisni naslov in vidne enote, naslova osi pa samo, kjer sta potrebna. Pod grafikon napišite popoln napis: izvorna datoteka/različica, enota opazovanja, mera, imenovalec, izključitve, pravilo manjkajočih vrednosti, sklic na pretvorbo in rezultat ročnega preverjanja. Dodajte smiselno nadomestno besedilo ter pomena ne kodirajte samo z barvo.

11. **Interpretacijo napišite ločeno.** Najprej opišite, kaj preverjeni grafikon kaže, nato dokazno gradivo in odločitve, ki so ga ustvarile. Šele nato podajte interpretacijo in omejitev. Dodelan grafikon ni interpretacija, povezava med kataloškimi kategorijami pa ne dokazuje zgodovinskega vzroka.

## Rezultat

Pripravite osveženo vrtilno tabelo, ročno preverjeno podmnožico, povezano tabelo za grafikon, en zadržan grafikon, popoln napis in nadomestno besedilo ter odstavek, ki loči opis, dokazno gradivo, interpretacijo in omejitev.

Postopek je uspešen, če izbrana agregacija odgovori na zapisano vprašanje, sta imenovalec in pravilo manjkajočih vrednosti izrecna, se ročni vzorec ujema z vrtilno tabelo ter je vsaka narisana vrednost sledljiva do očiščene tabele.

## Preverite se

- Ali polje Values uporablja Count, Sum, Average ali Distinct Count iz zapisanega razloga?
- Ali lahko poimenujete imenovalec in vse izključitve?
- Ali je osvežitev vključila pričakovano nadzorovano vrstico?
- Ali ročna podmnožica ponovi rezultat vrtilne tabele?
- Ali napis omogoča določitev vira, enote, mere in manjkajočih vrednosti?
- Ali interpretativna trditev ne presega dokaznega gradiva?

## Pogoste pasti

- Število vrstic poročate kot število različnih dokumentov.
- Povprečite polje brez pregleda manjkajočih in neštevilskih vrednosti.
- Praznine ostanejo skrite zaradi privzetih nastavitev vrtilne tabele.
- Urejate rezultat vrtilne tabele namesto vira in osvežitve.
- Naslov grafikona uporabite kot edino opombo o viru ali enoti.
- Vizualno dodelanost, korelacijo ali visok stolpec obravnavate kot zgodovinsko razlago.

## Viri in stanje vmesnika

Vire smo preverili **2. septembra 2026**: Microsoft Support o [ustvarjanju vrtilne tabele](https://support.microsoft.com/en-us/excel/get-started/create-a-pivottable-to-analyze-worksheet-data), [osveževanju podatkov](https://support.microsoft.com/en-us/office/refresh-pivottable-data), [ustvarjanju grafikonov](https://support.microsoft.com/en-us/excel/get-started/create-a-chart-from-start-to-finish), [naslovih grafikona in osi](https://support.microsoft.com/en-us/office/excelexp/add-or-remove-titles-in-a-chart) in [dostopnih Excelovih zvezkih](https://support.microsoft.com/en-us/accessibility/excel/make-your-excel-documents-accessible-to-people-with-disabilities). Vmesnik vrtilnih tabel, Distinct Count in grafični ukazi so odvisni od platforme in izdaje.

## Naloga

Iz očiščene vzorčne tabele pripravite število po kategorijah, prikažite neznano kategorijo, ročno preverite eno kategorijo, rezultat po dodani vrstici osvežite in izdelajte en grafikon z napisom, ki navede imenovalec ter pravilo manjkajočih vrednosti.
