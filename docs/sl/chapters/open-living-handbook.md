---
title: "Živi odprti priročnik"
description: "Kako lahko recenzirana znanstvena izdaja in sproti vzdrževani učni vir sobivata brez zmede glede avtoritete, avtorstva ali navajanja."
tags: [odprto-izobraževanje, verzioniranje, recenziranje, prispevki, založništvo]
status: draft
---

# Živi odprti priročnik

## Učni cilji

Po tem poglavju boste znali:

- razlikovati med živo izdajo in stabilno recenzirano različico;
- pravilno navesti verzionirano digitalno publikacijo;
- zasnovati postopke prispevanja, pregledovanja in prevajanja;
- pojasniti, kako Git, GitHub Pages in arhiv opravljajo različne založniške naloge;
- presoditi, ali sprememba zahteva popravek, manjšo ali večjo izdajo.

## Pred začetkom

Natisnjeno navodilo za programsko opremo je lahko zastarelo, še preden ga študenti odprejo. Spletno mesto, ki se nenehno spreminja, pa je težko navesti ali recenzirati. Rešitev ni izbira med trajnostjo in spremembo. Vsaki je treba dodeliti jasno plast.

## Dve izdaji, ena publikacija

Priročnik loči:

1. **živo izdajo** na privzeti veji, kjer nastajajo popravki, novi postopki in prevodi; ter
2. **stabilno izdajo**, opredeljeno z različico, datumom in arhiviranim posnetkom.

Živa izdaja podpira poučevanje in vzdrževanje. Stabilna izdaja je predmet formalne recenzije, navajanja in ohranjanja. Bralci lahko vedno vidijo, katero izdajo uporabljajo.

Model je običajen pri programski opremi in podatkovnih objavah, ustreza pa tudi področjem, kjer se metode in vmesniki hitro spreminjajo. Pojmovna poglavja naj se spreminjajo počasi, praktične postopke pa lahko posodabljamo pogosteje.

## Vloge založniške infrastrukture

Različne sestavine imajo različne naloge:

- **repozitorij Git:** izvorne datoteke, zgodovina, prijave težav, pregled in prispevki;
- **GitHub Pages:** berljiva javna spletna izdaja;
- **označena izdaja:** zamrznjen niz datotek, ki predstavlja izdajo;
- **arhivski repozitorij:** dolgoročni zapis in trajni identifikator;
- **založniški zapis:** recenzija, metapodatki, katalogizacija in institucionalno priznanje;
- **neobvezni posnetek PDF:** oblika za delo brez povezave, oddajo in pregled, ne uredniški izvirnik.

Nobena platforma ne sme nositi vseh nalog. Spletni naslov veje ni arhiv, PDF pa ni vzdrževani izvor.

## Številke različic sporočajo pomen

Uporabna semantična shema je:

- izdaja **popravka**, denimo 1.0.1: popravki, ki bistveno ne spreminjajo metode ali učnih ciljev;
- **manjša** izdaja, denimo 1.1.0: novi postopki, prevodi ali združljivi dodatki;
- **večja** izdaja, denimo 2.0.0: obsežna reorganizacija, spremenjena metodološka priporočila ali na novo recenzirana izdaja.

Vsaka izdaja naj vsebuje dnevnik sprememb, podatke za navajanje in izjavo o recenzijskem statusu. Arhivirane izdaje ne prepisujte potiho.

## Navajanje in status recenzije

Spletno mesto naj pokaže:

- trenutno različico ali razvojni status;
- datum objave in zadnje posodobitve;
- priporočeni navedek;
- DOI ali arhivski identifikator, ko je dodeljen;
- uredniško in recenzijsko izjavo;
- licence za besedilo, kodo in podatke;
- povezavo do natančne različice izvornih datotek.

Bralec, ki navaja raziskovalno trditev, naj navede uporabljeno stabilno izdajo. Pri predmetu lahko uporabljamo živo izdajo in zabeležimo commit ali semestrsko različico.

## Prispevanje ni neurejeno urejanje

Odprtost pomeni, da ljudje lahko predlagajo in pregledajo spremembe, ne da se vsaka sprememba samodejno objavi. Postopek prispevanja naj zahteva:

1. določeno težavo in ciljno občinstvo;
2. preverjanje virov in pravic;
3. ponovljiv najmanjši primer;
4. pričakovani izhod in načine odpovedi;
5. uredniški in tehnični pregled;
6. jezikovni pregled, kadar je potreben;
7. razkritje vloge avtorja in soglasje z licenco;
8. samodejne preizkuse pred združitvijo.

Študenti so lahko resnični sodelavci. Njihovo delo mora biti priznano, pregledano in objavljeno pod licenco, s katero so zavestno soglašali. Ocenjevanje in odločitev o objavi morata biti ločena, da študenti niso prisiljeni v javno avtorstvo.

## Dvojezična objava je uredniško delo

Jezikovni preklopnik je tehnična funkcija; dvojezični priročnik zahteva uredniško enakovrednost.

Vsaka jezikovna različica potrebuje:

- idiomatično terminologijo in ne mehanske zamenjave besed;
- usklajene učne cilje in primere;
- način označevanja manjkajočih ali zastarelih prevodov;
- recenzente, usposobljene za ustrezni jezik in področje;
- provenienco in datum prevoda;
- politiko za spremembe, ki prizadenejo samo en jezik.

Različici ne potrebujeta stavčne istovetnosti. Podpirati morata enakovredno učenje in jasno pokazati razlike. Privzeti jezik lahko začasno ponudi nadomestne strani, manjkajoči prevodi pa se ne smejo predstavljati kot popolna pokritost.

## Upravljanje prepreči odvisnost od ene osebe

Živi vir ne sme biti odvisen od spomina enega človeka. Zapišite:

- vloge urednika in vzdrževalca;
- kdo potrdi vsebinske, prevodne in tehnične spremembe;
- intervale pregleda strani, odvisnih od programske opreme;
- oznake za preverjene, zastarele ali arhivirane postopke;
- postopke popravkov in umikov;
- načrt nasledstva in lastništva repozitorija;
- obravnavo navzkrižij interesov.

Upravljanje odprtost naredi trajno. Založniku tudi omogoči priznanje spreminjajočega se projekta, ne da bi domneval, da je bil vsak commit formalno recenziran.

## Postopek izdaje

Formalna izdaja lahko sledi tem korakom:

1. razglasimo vsebinski zamrznitveni rok in kandidata za izdajo;
2. izvedemo samodejne preizkuse povezav, strukture in kode;
3. zaključimo strokovno in didaktično recenzijo stabilnega jedra;
4. vnesemo zahtevane spremembe in zabeležimo potrditev recenzentov;
5. opravimo jezikovni in dostopnostni pregled;
6. označimo izvor ter zgradimo spletni in PDF-izdelek;
7. izdajo arhiviramo in pridobimo ali registriramo trajni identifikator;
8. objavimo podatke za navajanje in opombe ob izdaji;
9. živo izdajo ponovno odpremo za razvoj.

Tako ohranimo odgovornost in zagon.

## Razdelan primer: študentski prispevek

Študentka predlaga postopek za kartiranje krajev v prepisih ustne zgodovine.

- Odda majhen anonimiziran vzorec, metodo, izhod in omejitve.
- Kolega postopek ponovi.
- Urednik pregleda zasebnost, geokodirno negotovost in terminologijo.
- Prispevek je popravljen in avtorica navedena.
- V živo izdajo vstopi kot pregledan postopek.
- Ob naslednji manjši izdaji postane del stabilne arhivirane različice.

Študentsko delo postane resnično znanstveno komuniciranje in ne zavržena domača naloga, uredniški postopek pa ščiti bralce in udeležence.

## Vaja

Za en digitalni učni vir pripravite založniško arhitekturo. Določite živi izvor, stabilno izdajo, arhiv, navedek, uredniške vloge, pot prispevanja, prevodno politiko in merila za novo večjo izdajo.

## Refleksija

- Kaj natančno je bilo recenzirano: vsaka stran, jedrna poglavja ali ena izdaja?
- Kako bo bralec vedel, da je postopek, odvisen od programske opreme, še aktualen?
- Kdo je lastnik in vzdrževalec projekta, če prvotni urednik odide?

## Povzetek

Živi priročnik je lahko odprt in akademsko navedljiv, kadar jasno ločimo razvoj in objavo. Git podpira zgodovino in prispevke, spletno mesto branje, označene izdaje recenzijo, arhiv pa ohranjanje. Verzioniranje, upravljanje, dvojezična uredniška politika in izrecni status recenzije neprestano spreminjanje iz slabosti spremenijo v dokumentirano znanstveno metodo.
