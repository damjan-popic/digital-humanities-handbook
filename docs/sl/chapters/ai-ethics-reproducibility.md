---
title: "UI, etika in ponovljivost"
description: "Kako uporabljati računalniške in generativne sisteme ter pri tem ohraniti dokaze, pravice, odgovornost in možnost ponovitve raziskave."
tags: [UI, etika, ponovljivost, provenienca, pravice]
status: draft
---

# UI, etika in ponovljivost

## Učni cilji

Po tem poglavju boste znali:

- razlikovati med ponovljivostjo, replikacijo in preglednostjo;
- podatke, kodo, modele, pozive in okolja dokumentirati kot raziskovalno gradivo;
- prepoznati tveganja za zasebnost, avtorske pravice, reprezentacijo in delo v digitalnohumanističnih projektih;
- zasnovati z viri podprto uporabo generativne UI in preveriti rezultate;
- pripraviti izdajo, ki jo lahko druga oseba pregleda in ponovno zažene.

## Pred začetkom

Klepetalnik pripravi tekoč povzetek s tremi prepričljivimi navedki. En je nekoliko spremenjen, en pripada drugemu avtorju, tretji pa ne obstaja. Težava ni samo v tem, da »UI halucinira«. Postopek je generativnemu sistemu dodelil vlogo vira dokazov, ne da bi ohranil preverljivo pot nazaj do dokumentov.

To poglavje obravnava varovala znotraj projekta. Poglavje [Infrastrukture digitalne humanistike: moč, dostop in vzdrževanje](critical-infrastructures.md) pa širše obravnava zbirke, standarde, vmesnike, delo in vzdrževanje, ki projekt pogojujejo pred začetkom dela.

Delovni primer v poglavju [Digitalna humanistika v Sloveniji](digital-humanities-in-slovenia.md) pokaže, kako se avtorske pravice, vrednotenje modela, izbira repozitorija, različice in vzdrževanje povežejo v verjetno lokalno raziskovalno verigo.

## Ponovljivost je oblikovalska odločitev

Rezultat je **računalniško ponovljiv**, kadar druga oseba z istimi podatki, kodo in okoljem dobi isti ali sprejemljivo enakovreden izhod. **Replikacija** pogosto pomeni preverjanje trditve z neodvisno zbranimi podatki ali drugo izvedbo. **Preglednost** pomeni, da so pomembne odločitve, pretvorbe in omejitve dostopne za presojo.

Humanistični projekti lahko vsebujejo interpretativne korake, ki jih ni mogoče mehansko ponoviti. Še vedno jih lahko naredimo pregledne s kodirnimi priročniki, dnevniki odločitev, primeri in provenienco.

## Zabeležite celotno verigo

Najmanjši raziskovalni paket naj določi:

- izvorno gradivo in pogoje dostopa;
- pravila izbora in izločanja podatkov;
- skripte, poizvedbe in ročne pretvorbe;
- različice programske opreme, paketov in modelov;
- nastavitve, naključna semena in korake, občutljive na strojno opremo;
- pozive, sistemska navodila in identifikatorje generativnih modelov;
- vmesne in končne izhode;
- postopke preverjanja in znane napake;
- vloge sodelujočih in licence.

Zvezek, ki deluje samo na avtorjevem računalniku, ni ponovljiv. Prav tako ni ponovljiv repozitorij, ki izpusti zasebne podatke, ne da bi pojasnil, kako lahko pooblaščeni raziskovalec analizo ponovno izvede.

## Okolja in verzioniranje

Odvisnosti se spreminjajo. Združljive različice zapišite v `requirements.txt`, `environment.yml`, zaklenjeno datoteko ali opis vsebnika. Dodajte majhen preizkus delovanja in pričakovani izhod. Javne izdaje označite z značkami različic in navajajte izdajo, ne premikajoče se veje `main`.

Verzionirajte tudi podatke. Popravljen korpus lahko spremeni števila, čeprav je koda enaka. Opombe ob izdaji naj ločijo vsebinske popravke, metodološke spremembe in kozmetične posege.

## Etična presoja se začne pred zbiranjem

Pred pridobivanjem podatkov vprašajte:

- Je bilo gradivo ustvarjeno za javno kroženje ali omejen kontekst?
- Ali pravna dostopnost in etično dovoljenje kažeta v isto smer?
- Bi navajanje, povezovanje ali združevanje izpostavilo osebo, ki je bila v izvornem kontekstu neopažena?
- Ali gradivo vključuje ranljive skupnosti, mladoletne, zdravstvene podatke ali družinske zgodovine?
- Ali vmesnik platforme podatke kaže, medtem ko pogoji ali družbene norme odvračajo od množičnega zajema?
- Kdo opravlja čiščenje, anotacijo in moderiranje ter ali je delo priznano?

»Javno dostopno« ni popolna etična utemeljitev.

## Avtorske pravice, licence in ponovna uporaba

Ločite pravice v izvornem gradivu, anotacijah, kodi, dokumentaciji in rezultatih. Korpus je morda mogoče deliti le kot metapodatke, identifikatorje, izpeljane značilke ali skripte, ki jih pooblaščeni uporabniki zaženejo lokalno. Odprti repozitorij ne pomeni, da je vsak vključeni predmet odprto licenciran.

Za vsako sestavino navedite:

- imetnika pravic ali vir;
- licenco ali pravno podlago;
- dovoljeno razširjanje;
- zahteve za navedbo;
- omejitve dostopa in postopek umika.

Uporabite najmanj omejujočo licenco, ki jo lahko zakonito podelite, ne tiste, ki bi jo zgolj želeli.

## Pristranskost in reprezentacijska škoda

Digitalne zbirke premočno zastopajo gradivo, ki je bilo ohranjeno, digitalizirano, katalogizirano, berljivo za OCR in dostopno pod izvedljivimi pravicami. Modeli dodajo pristranskosti učnih podatkov, anotacijskih kategorij ter različnih rezultatov med jeziki in skupnostmi.

Vrednotenje naj zato vključuje:

- pokritost pomembnih skupin, žanrov, obdobij in jezikov;
- manjkajoče podatke in pristranskost ohranjenosti;
- stopnje napak po skupinah;
- primere škodljivih ali stereotipnih rezultatov;
- posvetovanje, kadar projekt predstavlja ali imenuje skupnosti;
- omejitve trditev in objave občutljivih podrobnosti.

Model je lahko povprečno tehnično natančen, hkrati pa ponavlja škodljivo zgodovinsko kategorijo ali odpove prav pri manjšinskem gradivu.

## Generativna UI, podprta z viri

Generativna UI je najlažje utemeljiva, kadar preoblikuje ali preiskuje podane vire in lahko vsako pomembno trditev preverimo.

Postopek, podprt z viri, lahko:

1. iz dokumentirane zbirke pridobi omejene odlomke;
2. od modela zahteva povzetek ali klasifikacijo samo teh odlomkov;
3. zahteva identifikatorje odlomkov in citirane dokaze;
4. samodejno preveri, ali navedeni nizi obstajajo;
5. človek preveri interpretacijo in izpuste;
6. ohrani poziv, model, parametre, pridobljeni kontekst in rezultat;
7. po možnosti primerja rezultat z negenerativnim izhodiščem.

Bibliografije ne polnite z navedki, ki jih je model ustvaril iz spomina. Samozavestno besedišče modela obravnavajte kot retoriko in ne umerjeno verjetnost.

## Človeška odgovornost in razkritje

Orodje ne more prevzeti avtorske odgovornosti, pridobiti soglasja ali presoditi, ali objava škoduje živi osebi. Navedite, kdo je sprejel končne odločitve. Pomoč UI razkrijte na ravni, pomembni za bralca: snovanje, prevajanje, programiranje, klasifikacija, jezikovni pregled ali generiranje.

Razkritje naj omogoči vrednotenje in ne le ritualne izpovedi. »Uporabili smo UI« je presplošno; »model X, različica/datum, je po kodirnem priročniku Y razvrstil 1.200 odstavkov; dva označevalca sta pregledala vse primere z nizko gotovostjo in 20-odstotni naključni vzorec« je uporabno.

## Razdelan primer: arhivski vodnik s pomočjo UI

Skupina z jezikovnim modelom pripravi osnutke opisov arhivskih map.

1. Vhode omeji na dovoljene kataložne opise in izbrane dokumente.
2. Določi obvezna polja in prepovedane sklepe.
3. Za vsako trditev zahteva identifikator vira.
4. Točnost izluščanja preveri na ročno pripravljenem vzorcu.
5. Imena, občutljive podatke in negotove datume označi za pregled.
6. Rezultat primerja po jezikih in vrstah dokumentov.
7. Generirani opis do potrditve ohrani ločeno od arhivskega zapisa.
8. Zabeleži pregledovalca, datum in spremembe.
9. Objavi izjavo o uporabi modela in pot za popravke.

Sistem pospeši pripravo osnutka; arhivisti ostanejo odgovorni za opis in odločitve o dostopu.

## Vaja

Za en projekt pripravite kontrolni seznam ponovljivosti in etike. Vključite pravice do podatkov, zasebnost, pristranskost izbora, različice modelov, naključne elemente, človeški pregled, preverjanje, datoteke izdaje, navajanje ter načrt odziva na napake ali zahteve za umik.

## Refleksija

- Katerih delov postopka ne morete deliti in kako jih lahko vseeno dokumentirate?
- Kdo je v podatkih predstavljen, vendar ga ni pri projektnih odločitvah?
- Bi rezultat preživel spremembo modela ali nedostopnost spletne storitve?

## Povzetek

Odgovorna digitalna humanistika združuje tehnično ponovljivost in etično odgovornost. Ohranite verigo od vira do izhoda, verzionirajte kodo in podatke, navedite pravice in omejitve, preverite rezultat tam, kjer se lahko zgostita škoda ali pristranskost, ter generativno UI privežite na preverljive dokaze. Ponovljivost ni mapa, dodana na koncu, temveč arhitektura raziskovalnega procesa, ki ga drugi lahko pregledajo, izpodbijajo in izboljšajo.
