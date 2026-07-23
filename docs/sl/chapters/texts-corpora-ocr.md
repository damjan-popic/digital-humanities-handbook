---
title: "Besedila, korpusi in OCR"
description: "Kako iz izvorno digitalnih, skeniranih in zgodovinsko spremenljivih virov zgradimo interpretabilne besedilne zbirke."
tags: [besedilo, korpus, OCR, vzorčenje]
status: draft
---

# Besedila, korpusi in OCR

## Učni cilji

Po tem poglavju boste znali:

- razlikovati med sliko dokumenta, besedilom OCR, popravljenim besedilom, jezikoslovno anotacijo in metapodatki;
- korpus zasnovati glede na vprašanje in ne glede na priročnost;
- presoditi reprezentativnost, uravnoteženost in primerljivost;
- izbrati normalizacijsko politiko, primerno zgodovinskemu ali nestandardnemu jeziku;
- izmeriti kakovost OCR in pojasniti njen vpliv na nadaljnjo analizo.

## Pred začetkom

Odprite skenirano zgodovinsko stran in njen prepis OCR. Poiščite pet razlik. Katere napake bi preprečile iskanje? Katere bi spremenile frekvenco besede? Katere bi zavedle razpoznavalnik imenskih entitet? Vse napake nimajo enake raziskovalne cene.

Institucionalne in ročne korake med knjižničnim posnetkom in objavljenim korpusom v slovenskem okolju predstavi poglavje [Digitalna humanistika v Sloveniji](digital-humanities-in-slovenia.md).

## Digitalno besedilo ima več plasti

En dokument ima lahko več povezanih predstavitev:

1. **sliko** — sken ali fotografijo;
2. **opis postavitve** — območja, stolpce, vrstice in marginalije;
3. **diplomatični prepis** — natančen zapis vidnih znakov in strukture;
4. **normalizirano besedilo** — poenoten zapis, ločila ali kodiranje;
5. **jezikoslovno anotacijo** — pojavnice, leme, besedne vrste, entitete ali skladnjo;
6. **metapodatke** — vir, datum, avtorja, žanr, pravice in zgodovino obdelave.

Plasti se ne smejo tiho prepisovati. Slika ostane dokaz, kadar je OCR negotov. Diplomatično besedilo ohrani zgodovinsko obliko. Normalizirana različica lahko olajša iskanje, vendar je interpretacija in mora ostati povezana z izvirnikom.

## Zasnova korpusa se začne s pravili vključevanja

Korpus je namensko oblikovana zbirka besedil, ne zgolj mapa z veliko datotekami. Njegove meje moramo utemeljiti.

Določite:

- ciljno populacijo: katero širše množico besedil naj korpus predstavlja;
- vzorčni okvir: katero gradivo je bilo dejansko na voljo za izbor;
- merila vključevanja in izločanja;
- pokritost časa, žanrov, regij, jezikov in avtorstva;
- enoto vzorčenja in enoto analize;
- znane vrzeli, podvajanje in omejitve pravic.

Milijon spletnih strani je lahko manj uporaben od tisoč dobro dokumentiranih besedil, kadar raziskava primerja obdobja, žanre ali avtorje.

## Reprezentativnost je trditev

Noben korpus ne predstavlja »jezika« ali »kulture« na splošno. Predstavlja določeno populacijo pod določenimi pogoji. Spletni korpusi premočno zastopajo javno, strojno dosegljivo in iskalnikom vidno gradivo. Časopisni arhivi odražajo ohranjenost, licence in prednostne naloge digitalizacije. Literarni korpusi pogosto premočno zastopajo kanonična dela v javni domeni.

Uravnoteženost preglejte z metapodatkovnimi tabelami in porazdelitvami. Preštejte dokumente in besede po letu, žanru, viru, avtorju in drugih pomembnih slojih. Veliko število besed ne nadomesti manjkajoče kategorije.

## OCR kot merjenje

Optično razpoznavanje znakov napoveduje besedilo iz slike. Ni nevtralen prepis. Kakovost je odvisna od tiska, pisave, jezikovnega modela, ločljivosti posnetka, postavitve, deljenja besed, poškodb strani in zgodovinskega zapisa.

Pogosti meri sta:

- **stopnja napak na znakih (CER):** zamenjave, vrivanja in izpusti glede na referenčne znake;
- **stopnja napak na besedah (WER):** enaka logika na ravni besed.

Skupna ocena lahko prikrije neenakomerne težave. Lastna imena, diakritika, drobni tisk, tabele ali manjšinski jezikovni odlomki so lahko veliko slabši od navadnega proznega besedila. Ocenjujte stratificiran vzorec, ki vsebuje zahtevne strani in značilnosti, bistvene za raziskavo.

## Nadaljnja cena napak OCR

Napake OCR različno vplivajo na metode:

- iskanje po polnem besedilu izgubi priklic, ko je ciljna beseda napačno prepoznana;
- frekvenčni seznami eno besedo razcepijo v več napačnih oblik;
- lematizatorji in označevalniki odpovejo pri poškodovanih pojavnicah;
- razpoznavanje imenskih entitet je posebno občutljivo na nenavadna imena;
- tematski modeli lahko okoli ponavljajočih se artefaktov ustvarijo šumne teme;
- navedki in znanstvene izdaje zahtevajo veliko večjo natančnost kot zbirni trendi.

Potrebna količina popravljanja je zato odvisna od trditve. Groba analiza trendov lahko prenese napake, ki jih znanstvena izdaja ne sme.

## Normalizacija in zgodovinska variacija

Normalizacija izboljša primerljivost, vendar lahko izbriše dokaze. Izvirno in normalizirano obliko hranite ločeno. Dokumentirajte pravila za:

- Unicode in kodiranje znakov;
- deljenje besed ob koncu vrstice;
- zgodovinske znake in diakritiko;
- zapisne različice;
- ločila in narekovaje;
- ponavljajoče se glave, noge in številke strani;
- jezikovno mešanje in preklapljanje kodov.

Samodejna normalizacija naj bo povratna ali vsaj pregledna. Seznam popravkov z izvorno obliko, zamenjavo, kontekstom in razlogom je boljši od nedokumentiranega iskanja in zamenjave.

## Odstranjevanje dvojnikov in identiteta dokumenta

Digitalne zbirke pogosto vsebujejo dvojnike: zrcaljene spletne strani, agencijske novice, popravljene izdaje, več izvozov OCR istega skena ali dokumente, navedene znotraj drugih dokumentov. Dvojniki lahko prevladajo nad frekvencami in lažno povečajo gotovost.

Dodelite identifikatorje dokumentov, za popolnoma enake datoteke izračunajte zgoščene vrednosti, za skorajšnje dvojnike pa uporabite mere podobnosti. Ne brišite na slepo: ponavljanje in razširjanje sta lahko zgodovinsko pomembna. Označite razmerja, kot so `dvojnik`, `ponatis` ali `razlicica`, in določite raven, ki jo potrebuje analiza.

## Razdelan primer: zgodovinski časopisni korpus

Utemeljen postopek bi lahko bil:

1. glede na vprašanje izberemo časopisne naslove in leta;
2. zabeležimo metapodatke o številkah in člankih;
3. ločeno ohranimo slike strani in OCR;
4. čez naslove, leta in tipe postavitev vzorčimo strani za oceno OCR;
5. popravimo sistematične napake z velikim vplivom;
6. razdelimo članke in ohranimo povezave do koordinat na strani;
7. dokumentiramo manjkajoče številke in spremembe pogostosti izhajanja;
8. pred analizo primerjamo porazdelitve besed in dokumentov;
9. vodimo register napak in navedemo uporabljeno izdajo korpusa.

## Vaja

Za zbirko, ki bi jo lahko dejansko zgradili, pripravite kartico korpusa. Vključite ciljno populacijo, vzorčni okvir, pravila vključevanja in izločanja, metapodatkovna polja, pričakovane napake OCR ali zajema, pravilo za dvojnike ter najmočnejšo primerjavo, ki jo korpus podpira.

## Refleksija

- Katera manjkajoča besedila so nevidna zato, ker nikoli niso bila digitalizirana?
- Bi normalizacija odstranila značilnost, ki jo bo interpretacija morda potrebovala?
- Katere napake OCR so najpomembnejše za načrtovano metodo?

## Povzetek

Besedilni korpus je dokumentiran raziskovalni instrument. Sestavljajo ga povezane plasti, izrecne meje, metapodatki in izmerjena preoblikovanja. OCR in normalizacija ustvarita uporabno besedilo, pa tudi novo negotovost. Kakovost korpusa ni število pojavnic, temveč ujemanje med izborom, predstavitvijo, profilom napak in raziskovalno trditvijo.
