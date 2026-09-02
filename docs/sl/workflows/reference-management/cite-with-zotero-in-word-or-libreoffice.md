---
title: "Kako z Zoterom vstavljam navedbe v Word ali LibreOffice?"
description: "Vstavite navedbe z lokatorji in osvežljivo bibliografijo ter ohranite metapodatke v Zoteru in polja urejevalnika besedil."
category: "Upravljanje virov"
category_id: "reference-management"
difficulty: "začetno"
time: "45–75 min"
tags: [zotero, word, libreoffice, navedbe, bibliografija]
---

# Kako z Zoterom vstavljam navedbe v Word ali LibreOffice?

<div class="answer-meta" markdown>
<span>Upravljanje virov</span><span>začetno</span><span>45–75 min</span>
</div>

## Kaj želite doseči

Kako lahko navedba med spreminjanjem besedila ostane povezana s popravljenimi metapodatki vira? Dodatek Zotero v urejevalnik besedil vstavi aktivna polja. Vidna navedba oziroma citat je oblikovan izpis, bibliografske podatke pa popravljate v bibliografskem zapisu v Zoteru.

Pred tem postopkom določite zahtevani sistem citiranja, izberite ustrezni citatni slog in preglejte veljavna navodila za citiranje. Istega dokumenta ne upravljajte hkrati z Zoterom in Wordovim vgrajenim upravljalnikom virov, saj je dokument z dvema vrstama citatnih polj pri skupinskem delu težko popravljati in diagnosticirati.

## Potrebujete

- varnostno kopiran delovni dokument `.docx` ali `.odt`;
- pet metapodatkovno preverjenih enot Zotero;
- sistem citiranja, citatni slog in navodila za citiranje, ki jih zahteva fakulteta, revija, založnik ali izvajalec predmeta;
- najmanj en odlomek s preverjeno stranjo, razdelkom, odstavkom, folijem ali časovno oznako.

Za manjši strukturirani dokument, testne zapise, bibliografijo in pregled citiranja uporabite [vzorčni paket ZIP](../../../assets/downloads/scholarly-work-foundations-v1.zip).

## Postopek

1. **Preverite integracijo.** Zotero odprite pred urejevalnikom besedil. V Wordu poiščite zavihek *Zotero*, v LibreOffice Writerju pa orodno vrstico ali meni Zotero. Če ju ni, zaprite urejevalnik in v Zoteru uporabite *Settings/Preferences → Cite → Word Processors*, da namestite ali znova namestite ustrezni dodatek. Oznake in položaji se razlikujejo po platformah in izdajah.

2. **Nastavite dokument.** Na zavihku oziroma v orodni vrstici Zotero odprite *Document Preferences*. Izberite zahtevani citatni slog in, kjer je možnost na voljo, jezik oziroma območno nastavitev (angl. *locale*), ki vpliva na lokalizirane okrajšave, veznike in druge izraze v navedbah. Ugotovite, ali izbrani sistem uporablja navedbe v besedilu, sprotne opombe ali končne opombe. To so različne konvencije, ne kakovostne stopnje. Word ali Writer ureja postavitev opomb, Zotero pa v njih oblikuje navedbe.

3. **Vstavite vir ob trditev.** Kazalko postavite takoj za trditev ali navedek in izberite *Add/Edit Citation*. Poiščite preverjeno enoto. Odprite možnosti izbrane navedbe in dodajte preverjeni lokator ter njegovo vrsto, denimo stran `27`, razdelek `3` ali čas `00:04:12`. Lokator pokaže citirani odlomek; celotni obseg strani članka sodi v bibliografski zapis.

4. **V eno navedbo vstavite več virov.** V istem pogovornem oknu dodajte drugo enoto in vrstni red spremenite samo, če to zahteva slog ali argument. Lokatorje dodajte posameznim virom in ne kot nestrukturirano besedilo za poljem.

5. **Ustvarite bibliografijo.** Kazalko postavite na mesto seznama literature in izberite *Add/Edit Bibliography*. Ne tipkajte vzporednega ročnega seznama. Bibliografija nastane iz navedb z aktivnimi polji po izbranem slogu; navodila stroke lahko posebej zahtevajo tudi nenavedene primarne vire ali arhivske skupine.

6. **Metapodatke popravite v Zoteru.** Če navedba vsebuje napačnega avtorja, naslov, datum ali DOI, odprite bibliografski zapis v Zoteru in tam popravite metapodatke. Nato se vrnite v dokument in izberite *Refresh*. Iste napake ne popravljajte ročno v vsaki oblikovani navedbi.

7. **Z aktivnimi polji ravnajte previdno.** Ne tipkajte v osenčeno navedbo ali ustvarjeno bibliografijo. Z *Add/Edit Citation* lahko dodate lokator, predpono ali pripono ter, kjer slog dovoljuje, izpustite avtorja. Ročni popravek se lahko ob osvežitvi izbriše ali prepreči zanesljivo posodabljanje.

8. **Osvežite in preglejte.** Po premiku odstavkov ali popravku zapisov izberite *Refresh*. Po avtoritativnih navodilih za citiranje preverite pet primerov: preprost vir, lokator, več virov, ponovljeno navedbo in neobičajnega ustvarjalca oziroma vrsto vira. Osvežitev ni nadomestilo za uredniški pregled.

9. **Sodelujte v združljivi kopiji.** Delovni dokument ohranjajte v enem formatu in pretvorbo preizkusite pred rokom. Zotero glede na sodelovanje uporablja Wordova polja ali zaznamke; trenutna navodila praviloma dajejo prednost poljem, razen kadar je zaradi LibreOffice potrebna združljivost z zaznamki. Ne domnevajte, da večkratna pretvorba med `.docx` in `.odt` ohrani vsa aktivna polja.

10. **Povezave odstranite samo v varnostno kopirani končni oddajni kopiji.** *Unlink Citations* odstrani kode polj Zotero in prepreči prihodnje samodejne posodobitve. Zotero postopek označuje kot nepovraten. Dokument z aktivnimi polji vedno ohranite kot glavni delovni izvod in upoštevajte oddajne zahteve revije, fakultete ali založnika. Ko pripravljate statično končno oddajo, povezave odstranite samo v posebej poimenovani in varnostno kopirani oddajni kopiji. Tega nikoli ne storite v delovnem dokumentu zgolj zato, da bi popravili oblikovanje.

## Oznake v Wordu in LibreOffice

| Operacija | Word | LibreOffice Writer | Trajni pomen |
| --- | --- | --- | --- |
| Vstavljanje/urejanje navedbe | *Zotero → Add/Edit Citation* | Orodna vrstica/meni Zotero → *Add/Edit Citation* | Vstavi ali spremeni aktivno citatno polje. |
| Slog dokumenta | *Zotero → Document Preferences* | Orodna vrstica/meni Zotero → *Document Preferences* | Določi slog in razpoložljive jezikovne možnosti. |
| Bibliografija | *Zotero → Add/Edit Bibliography* | Orodna vrstica/meni Zotero → *Add/Edit Bibliography* | Ustvari ali uredi aktivno bibliografsko polje. |
| Preračun | *Zotero → Refresh* | Orodna vrstica/meni Zotero → *Refresh* | Navedbe znova oblikuje iz metapodatkov knjižnice. |
| Končna odstranitev povezav | *Zotero → Unlink Citations* | Orodna vrstica/meni Zotero → *Unlink Citations* | Nepovratno spremeni navedbe z aktivnimi polji v navadno besedilo. |

## Rezultat

Pripravite glavni delovni dokument z aktivnimi polji, eno navedbo z lokatorjem, eno navedbo z več viri in ustvarjeno bibliografijo ter dnevnik primerjave petih primerov. Kadar oddajna navodila zahtevajo statično besedilo, pripravite še posebej poimenovano in varnostno kopirano končno oddajno kopijo z odstranjenimi povezavami.

Postopek je uspešen, če se enkratni metapodatkovni popravek v Zoteru po *Refresh* prikaže v dokumentu, se vseh pet primerov ujema z izbranimi avtoritativnimi navodili ali ima dokumentirano odstopanje ter povezani delovni izvod ostane na voljo.

## Preverite se

- Ali znate pojasniti, ali je izbrani slog avtor–letnica, opombno-bibliografski ali številčni?
- Ali ima vsak navedek ali natančna trditev ustrezno vrsto lokatorja?
- Ali navedba z več viri ohrani lokator posameznega vira?
- Ali se bibliografija po nadzorovanem popravku metapodatkov in osvežitvi spremeni?
- Ali je morebitna kopija z odstranjenimi povezavami jasno označena kot končna oddajna kopija in ne kot glavni dokument?

## Pogoste pasti

- V enem dokumentu mešate Zotero in Wordov vgrajeni upravljalnik virov.
- Stran pripišete za navedbo z aktivnim poljem, namesto da bi uporabili lokator.
- Bibliografijo ročno popravite, napačni zapis Zotero pa pustite nespremenjen.
- Domnevate, da je vsaka sprotna opomba že opombno-bibliografska navedba.
- *Unlink Citations* uporabite za reševanje običajne oblikovne težave.

## Viri in stanje vmesnika

Vire smo preverili **2. septembra 2026**: uradna dokumentacija Zotero [Word Processor Plugins](https://www.zotero.org/support/word_processor_integration), [Using the Zotero Word Plugin](https://www.zotero.org/support/word_processor_plugin_usage), [odstranjevanje povezav v končni kopiji](https://www.zotero.org/support/kb/unlinking_citations), [Cite settings](https://www.zotero.org/support/preferences/cite) in [Troubleshooting](https://www.zotero.org/support/word_processor_plugin_troubleshooting). Pojmi dodatka so skupni Wordu in Writerju, natančne oznake, način shranjevanja polj in združljivost pa so odvisni od platforme in različice.

## Naloga

Vstavite dve navedbi z enim virom, eno z lokatorjem strani in eno z več viri. Ustvarite bibliografijo, v Zoteru popravite en zapis in dokument osvežite. Shranite glavni dokument z aktivnimi polji in z eno povedjo pojasnite, zakaj ga končna kopija z odstranjenimi povezavami ne more nadomestiti.
