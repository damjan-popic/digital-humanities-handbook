---
title: "Omrežja in vizualizacija"
description: "Kako zgraditi, meriti in prikazati razmerja, ne da bi graf zamenjali za družbeni ali kulturni svet sam."
tags: [omrežja, vizualizacija, graf, centralnost, negotovost]
status: draft
---

# Omrežja in vizualizacija

## Učni cilji

Po tem poglavju boste znali:

- opredeliti vozlišča, povezave, smer, utež in dvodelna omrežja;
- razlikovati med opazovanimi razmerji in razmerji, izpeljanimi s konstrukcijskim pravilom;
- previdno razlagati osnovne mere centralnosti in skupnosti;
- zasnovati vizualizacijo, ki razkrije merilo, negotovost in manjkajoče podatke;
- dokumentirati pretvorbe od izvornih zapisov do grafa.

## Pred začetkom

Dve osebi se pojavita v istem časopisnem članku. Sta povezani? Morda sodelujeta, si nasprotujeta, sta zgolj navedeni ali se pojavita v nepovezanih odstavkih. Omrežna povezava ni samodejno najdena v viru. Ustvari jo pravilo, katerega pomen moramo utemeljiti.

## Omrežje je podatkovni model

Graf vsebuje **vozlišča** in **povezave**. Vozlišča lahko predstavljajo osebe, besedila, kraje, ustanove ali pojme. Povezave lahko predstavljajo dopisovanje, citiranje, sorodstvo, soavtorstvo, potovanje, sopojavljanje ali drugo razmerje.

Določite, ali je povezava:

- usmerjena ali neusmerjena;
- utežena ali neutežena;
- datirana ali časovno omejena;
- neposredno opažena ali izpeljana;
- pozitivna, negativna ali tipizirana;
- podprta z enim ali več viri.

Različne definicije povezav ustvarijo različna omrežja. Definicija sodi v opis metode in po možnosti tudi v strojno berljive podatke.

## Enovrstna in dvodelna omrežja

Enovrstno omrežje povezuje isto vrsto vozlišč, denimo osebo z osebo. **Dvodelno** omrežje povezuje dve vrsti, denimo osebe z ustanovami ali literarne like s prizori.

Projekti dvodelno omrežje pogosto projicirajo v enovrstno omrežje sopojavljanja: dva lika sta povezana, če nastopita v istem prizoru. Projekcija izgubi informacije in lahko okoli velikih prizorov ustvari zelo goste povezave. Ohranite izvirne dvodelne podatke ter navedite pravilo projekcije in uteževanja.

## Centralnost je odvisna od vprašanja

Pogoste mere so:

- **stopnja:** število neposrednih povezav;
- **utežena stopnja:** vsota uteži povezav;
- **vmesnost:** kako pogosto vozlišče leži na najkrajših poteh;
- **bližina:** oddaljenost do drugih dosegljivih vozlišč;
- **lastni vektor ali PageRank:** povezanost z že dobro povezanimi vozlišči.

Nobena mera na splošno ne pomeni »pomembnosti«. Stopnja lahko kaže vidnost, priložnost ali le boljšo dokumentiranost. Vmesnost je močno odvisna od predpostavke, da najkrajše poti predstavljajo raziskovani proces. Nepovezana in zelo majhna omrežja zahtevajo posebno previdnost.

## Skupnosti in gruče

Algoritmi za odkrivanje skupnosti omrežje razdelijo v skupine z gostimi notranjimi povezavami. Rezultat je odvisen od algoritma, ločljivosti in naključne inicializacije. Skupnost ni samodejno zgodovinska frakcija ali literarna tema.

Primerjajte več ločljivosti, preglejte mejna vozlišča in skupine povežite z neodvisnimi metapodatki. Poročajte, kadar obstaja več verjetnih razdelitev. Vizualno urejen modularen graf lahko ustvari že postavitev, čeprav so dokazi šibki.

## Čas in sprememba

Združevanje več desetletij odnosov v en graf lahko ustvari povezave, ki nikoli niso sočasno obstajale. Kadar je kronologija pomembna, zgradite časovne rezine, intervalna omrežja ali poglede dogodkov.

Vprašajte se, ali vozlišča vstopajo in izstopajo, ali se uteži povezav seštevajo ter ali manjkajoča leta pomenijo brez dejavnosti ali brez ohranjenih podatkov. Animacija je privlačna, a jo je težko primerjati; majhni večkratniki ali interaktivni filtri spremembo pogosto pokažejo jasneje.

## Manjkajoči podatki in neenaka vidnost

Omrežja so posebej občutljiva na ohranjenost arhivov. Ploden korespondent je lahko videti obroben, ker je ohranjen le en arhiv. Znane osebe imajo morda boljše kataloge in razrešene identitete. Omrežja sopojavljanja privilegirajo dolge dokumente in pogosta imena.

Prikažite pokritost in število virov. Razmislite o analizah občutljivosti: odstranite negotove povezave, uporabite druge pragove ali primerjajte arhive. Odsotnost povezave navadno pomeni »ni opažena s tem postopkom«, ne »razmerje ni obstajalo«.

## Vizualizacija kot analitična zasnova

Omrežni prikaz potrebuje več kot pisana vozlišča. Odločitve vključujejo postavitev, velikost vozlišč, prosojnost povezav, oznake, filtriranje in barvne kategorije. Silno usmerjene postavitve optimizirajo berljivost, ne geografske ali kronološke resnice; ponovni zagoni lahko vozlišča postavijo drugače.

Dobra praksa:

- označujte le, kadar oznake služijo vprašanju;
- pojasnite vsako vizualno kodiranje;
- površine vozlišč ne povečujte zavajajoče;
- prikažite osamljena vozlišča, če bi njihov izbris prikril pokritost;
- za natančne vrednosti ponudite tabelo ali iskalni pogled;
- poskrbite za dostopnost barv in kontrasta;
- dodajte provenienco in prenosljiv seznam povezav.

## Razdelan primer: omrežje literarnih likov

Utemeljen postopek bi bil:

1. Določimo identiteto likov, različice imen in kolektivne like.
2. Izberemo pravilo povezave: skupni prizor, neposredni nagovor ali poročana interakcija.
3. Besedilo razdelimo in ohranimo sklice na odlomke.
4. Zgradimo dvodelno tabelo likov in prizorov.
5. Projekcijo izvedemo le, če vprašanje zahteva graf lik-lik.
6. Preverimo druge definicije prizorov in pragove povezav.
7. Centralnost primerjamo s pripovednim glediščem in količino govora.
8. V besedilu pregledamo navidezno središčne in presenetljivo obrobne like.
9. Objavimo vizualizacijo in podatke o konstrukciji.

Graf povzema en razmernostni vidik romana. Ne modelira globine lika, tematske pomembnosti ali bralske izkušnje, če tega nismo posebej operacionalizirali.

## Vaja

Iz vsaj desetih izvornih zapisov zgradite majhno omrežje. Pravilo povezave napišite v eni povedi, za vsako povezavo ohranite polje z dokazom, izračunajte stopnjo in ustvarite dva prikaza z različnima pragoma. Pojasnite, katera razmerja izginejo in zakaj.

## Refleksija

- Kaj povezava pomeni v jeziku virov?
- Katera vozlišča so vidna zato, ker so se njihovi zapisi ohranili ali jih je lažje prepoznati?
- Bi dvodelna predstavitev ohranila razlike, ki jih projekcija skrije?

## Povzetek

Omrežja so izrecni modeli razmerij, ne prosojne slike družbe ali književnosti. Definicije vozlišč in povezav, projekcija, čas, manjkajoči podatki in algoritmi oblikujejo vsak rezultat. Centralnost ni splošna pomembnost, skupnosti niso samorazlagalne skupine, postavitve pa niso dokaz. Sledljiva konstrukcijska pravila in z viri povezane povezave omrežno analizo naredijo primerno za humanistično interpretacijo.
