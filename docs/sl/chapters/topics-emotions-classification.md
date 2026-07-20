---
title: "Teme, sentiment in čustva"
description: "Kako uporabiti klasifikacijo in raziskovalne modele, ne da bi oznake, teme ali ocene zamenjali za človeški pomen."
tags: [klasifikacija, tematsko-modeliranje, sentiment, čustva, preverjanje]
status: draft
---

# Teme, sentiment in čustva

## Učni cilji

Po tem poglavju boste znali:

- razlikovati med nadzorovano klasifikacijo, nenadzorovanim gručenjem in tematskim modeliranjem;
- pojasniti razliko med sentimentom, stališčem, afektom in čustvom;
- pripraviti anotacijsko shemo in ovrednotiti ujemanje označevalcev;
- rezultate tematskega modela razlagati kot raziskovalno predstavitev in ne odkrito resnico;
- rezultate modela preveriti ob izvornih besedilih, metapodatkih in človeški presoji.

## Pred začetkom

Poved *Sijajno – spet čudovita zamuda* vsebuje pozitivne besede, vendar verjetno izraža negativno vrednotenje. Model, ki besedišče ocenjuje brez konteksta, lahko odpove. Pred izbiro orodja določite, kaj kategorija pomeni in kateri besedilni dokaz upraviči oznako.

## Klasifikacija se začne z operacionalizacijo

Klasifikator besedila ali odlomke razporedi v vnaprej določene kategorije. To so lahko žanr, obdobje, avtor, stališče, sentiment, čustvo ali relevantnost. Osrednje raziskovalno dejanje ni izbira algoritma, temveč prevod pojma v opazljiva anotacijska pravila.

Dober kodirni priročnik določi:

- enoto označevanja: poved, odstavek, dokument ali dogodek;
- definicije in meje kategorij;
- pozitivne in izključitvene primere;
- obravnavo negotovosti, mešanih primerov in odsotnosti;
- predvideno uporabo oznak;
- znane kulturne, zgodovinske in žanrske omejitve.

Če usposobljeni označevalci kategorije ne morejo dosledno uporabiti, model pojmovne dvoumnosti ne more popraviti.

## Sentiment ni čustvo

**Analiza sentimenta** navadno napoveduje vrednotenjsko polarnost – pozitivno, negativno ali nevtralno – do določene tarče. **Stališče** opisuje podporo, nasprotovanje ali umeščanje do trditve ali akterja. **Analiza čustev** poskuša določiti kategorije ali razsežnosti, kot so veselje, strah, jeza, žalost, vzburjenost ali valenca. **Afekt** se lahko širše nanaša na izraženo ali vzbujeno intenzivnost.

Pojmi niso zamenljivi. Zgodovinsko pismo lahko opisuje strah, ne da bi bil avtor prestrašen; tragedija lahko vzbuja žalost, čeprav vsebuje malo negativnega vrednotenja; satira lahko s hvalo kritizira. Določite, ali označujete besedilo, pripovedovalca, literarni lik, govorca, tarčo ali odziv bralca.

## Trije pogosti pristopi

### Leksikonske metode

Leksikon besede poveže z ocenami ali kategorijami. Je pregleden in ga lahko pregledamo, vendar ga spodkopljejo kontekst, zanikanje, stopnjevanje, metafora, sprememba področja in oblikoslovje. Pri slovenščini so pomembne pregibne oblike in lematizacija, prevedene leksikone pa je treba kulturno preveriti.

### Nadzorovani modeli

Nadzorovani model se uči iz označenih primerov. Njegovo zgornjo mejo določata kakovost in reprezentativnost oznak. Kadar lahko pride do uhajanja, podatke delite po dokumentih, avtorjih ali virih. Naključna delitev povedi lahko ustvari navidezno odličen rezultat, ker se skoraj enaki odlomki pojavijo v učni in testni množici.

### Jezikovni modeli z navodili

Jezikovni model lahko klasificira po navodilih in primerih, vendar se njegovo vedenje spreminja z formulacijo, različico modela in dolžino konteksta. Pozive obravnavajte kot del metode, shranite natančne vhode in izhode, preverite stabilnost in tekoče razlage ne zamenjujte za vrednotenje.

## Vrednotenje onkraj točnosti

Pri neuravnoteženih kategorijah je točnost lahko zavajajoča. Poročajte o matriki zamenjav ter po potrebi o preciznosti, priklicu in meri F1 za posamezne razrede. Primerjajte s preprostimi izhodišči: večinskim razredom, leksikonskim pravilom ali modelom samo z metapodatki.

Vprašajte tudi:

- Ali so napake skoncentrirane v enem žanru, obdobju ali družbeni skupini?
- Ali se model nauči vira dokumenta namesto želenega pojma?
- Ali negotove človeške primere štejemo kot napake modela, ne da bi priznali dvoumnost?
- Bi preostala napaka spremenila zgodovinski ali literarni sklep?

## Tematski modeli so leče

Tematski modeli in sorodne metode gručenja prostor dokumentov in besed ali vektorskih vložitev skrčijo v ponavljajoče se vzorce. V verjetnostnem tematskem modelu je »tema« porazdelitev po besedah in dokumentih, ne vnaprej poimenovan predmet z naravno mejo.

Rezultat je odvisen od:

- predobdelave in besedišča;
- enote analize in dolžine dokumentov;
- števila tem ali gruč;
- naključne inicializacije in hiperparametrov;
- vrste modela, denimo LDA, NMF ali gručenja vložitev;
- sestave korpusa in podvojenega besedila.

Raziskovalci teme poimenujejo po pregledu besed in dokumentov. Oznako zato spremljajte z reprezentativnimi dokumenti, nasprotnimi primeri in negotovostjo, ne zgolj z besednim oblakom.

## Stabilnost in interpretabilnost

Navidezno koherentna tema je lahko nestabilna med naključnimi semeni ali ob majhni spremembi korpusa. Izvedite več nastavitev in preverite, ali se vzorec ohrani. Statistične mere koherentnosti lahko pomagajo izbrati kandidate, ne morejo pa nadomestiti področne interpretacije.

Utemeljeno poročilo o tematski analizi vsebuje:

1. korpus in odločitve o predobdelavi;
2. model in parametre;
3. postopek izbire prikazane rešitve;
4. reprezentativne in nasprotujoče si dokumente;
5. razširjenost tem po relevantnih metapodatkih z negotovostjo;
6. občutljivost na drugo seme, model ali število tem;
7. pojasnilo, kaj model izpusti ali združi.

## Razdelan primer: čustveno okvirjanje v parlamentarni razpravi

Predpostavimo, da raziskujemo čustveno okvirjanje podnebne politike.

1. Določimo tarčo: čustvene besede govorcev, pripisana čustva ali čustveno okvirjanje politike.
2. Vzorčimo razprave in ohranimo podatke o govorcu, stranki, datumu in dnevnem redu.
3. Na poskusnem vzorcu oblikujemo kodirni priročnik in popravimo dvoumne kategorije.
4. Vsaj dva označevalca označita del gradiva in razpravljata o nesoglasjih.
5. Če je smiselno, primerjamo leksikonsko izhodišče, nadzorovani model in jezikovni model z navodili.
6. Rezultat preverimo po strankah, obdobjih in vrstah govorov, ne le skupno.
7. Preberemo lažno pozitivne, lažno negativne in zelo samozavestne primere.
8. Tematsko ali gručilno analizo uporabimo le kot dopolnilni raziskovalni pogled.
9. Rezultat predstavimo kot dokaz o jeziku korpusa, ne kot neposreden dostop do notranjih stanj govorcev.

## Vaja

Napišite enostranski kodirni priročnik za eno kategorijo: relevantnost, sentiment, stališče ali čustvo. Dodajte pet pozitivnih primerov, pet izključitev, dva negotova primera, enoto analize ter posledice lažno pozitivne in lažno negativne napovedi.

## Refleksija

- Merite jezik, pripisano stanje ali psihološko stanje?
- Bi model lahko oznako napovedal iz vira ali obdobja, ne da bi prebral pomembni odlomek?
- Katera človeška nesoglasja razkrivajo resnično pojmovno kompleksnost in ne slabe anotacije?

## Povzetek

Klasifikacija in tematska analiza lahko uredita velike zbirke besedil, vendar oznake in teme nastanejo skozi operacionalizacijo, podatke in modeliranje. Sentiment ni čustvo, tema ni samostojno obstoječ predmet, tekoč rezultat modela pa ni preverjanje. Kodirni priročniki, izhodišča, vrednotenje na zadržanih podatkih, analiza napak po skupinah, preverjanje občutljivosti in natančno branje te metode spremenijo v utemeljene humanistične dokaze.
