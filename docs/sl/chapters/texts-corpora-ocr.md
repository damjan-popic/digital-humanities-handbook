---
title: "Besedila, korpusi in OCR"
description: "Kako iz izvorno digitalnih, skeniranih in rokopisnih virov zgradite interpretabilne besedilne zbirke, ne da bi prikrili izbor ali napake prepoznavanja."
tags: [besedilo, korpus, OCR, HTR, vzorčenje, prepisovanje]
status: draft
---

# Besedila, korpusi in OCR

Zaradi iskalnega prepisa se lahko zdi, da je arhiv popoln. Toda prepis ni arhiv. Je ena od predstavitev, ki nastane iz izbranih predmetov, posnetkov strani, odločitev o postavitvi, sistema za prepoznavanje in uredniških pravil. Kaj lahko utemeljeno sklepate, če lahko vsaka od teh stopenj izpusti ali spremeni dokaz?

V tem poglavju boste korpus obravnavali kot raziskovalni instrument, ne kot mapo z besedilnimi datotekami. Poglavje se navezuje na [načrtovanje raziskave](research-design.md), [podatke, metapodatke in modele](data-metadata-models.md) ter [kritične infrastrukture](critical-infrastructures.md). Razdelani primer uporablja [ZIP učnega gradiva Arhivsko trenje](../../assets/downloads/archival-friction-v1.zip), [izvorno drevo paketa](https://github.com/damjan-popic/digital-humanities-handbook/tree/main/teaching-data/archival-friction) pa ostaja na voljo za pregled. Tako lahko skupaj pregledate posnetek, ponudnikov prepis, referenčni prepis, metapodatkovne odločitve in rezultate preverjanja.

## Učni cilji

Po tem poglavju boste znali:

- razlikovati med OCR in HTR ter med sliko strani, postavitvijo, prepisom, normaliziranim besedilom, anotacijo in metapodatki;
- napisati pravila za prepis zgodovinskega tiska ali rokopisa;
- opredeliti ciljno populacijo, vzorčni okvir in utemeljen korpusni vzorec;
- izračunati in razložiti stopnjo napak na znakih (CER) in besedah (WER) glede na referenčni prepis;
- preveriti, ali napake prepoznavanja ogrožajo določeno iskanje, štetje ali interpretacijo;
- ohraniti podatke o viru, pravicah, obdelavi in popravkih skozi ves besedilni postopek; ter
- opisati razmerja med dvojniki, ponatisi in različicami, ne da bi izbrisali zgodovinsko pomembno širjenje besedil.

## Pred začetkom

Ne potrebujete ukazne vrstice ali programiranja. Potrebujete pa raziskovalno vprašanje, dovoljenje za uporabo gradiva, manjši nabor posnetkov dokumentov in preglednico ali urejevalnik besedila. Za vrednotenje potrebujete tudi skrbno preverjen referenčni prepis vzorca.

Pripravili boste kartico korpusa, zapis o pravicah, pravila prepisovanja, povezane plasti, dnevnik vzorčenja, poročilo o kakovosti, dnevnik popravkov ter seznam znanih težav. Druga oseba mora ugotoviti, od kod izvira odlomek, skozi katere spremembe je šel in katere trditve dopuščajo preostale napake.

## Začnite pri raziskovalni trditvi

Recimo, da želite raziskati, kako je ilustrirani časopis iz leta 1925 predstavljal javne ustanove. Navodilo »prenesite ves razpoložljivi OCR« še ni raziskovalna metoda. Vprašajte se:

- Kaj je ciljna populacija: en časopis v letu 1925, ilustrirani časopisi v regiji ali vse ohranjene periodične publikacije na enem portalu?
- Kaj je enota vzorčenja: številka, stran, članek, napis pod sliko ali oglas?
- Kaj je enota analize: beseda, imenovana oseba, par slike in napisa, članek ali številka?
- Katere primerjave so pomembne: meseci, žanri, založniki, jeziki ali položaji na strani?
- Kateri dokaz bi vašo interpretacijo ovrgel?

Tako boste prepoznali tudi vprašanje, na katero razpoložljiva zbirka ne more odgovoriti. Douglas Biber pri zasnovi korpusa pokaže, da se reprezentativnost začne z opredeljeno populacijo in teoretično pomembnimi sloji, ne z velikim številom besed.

## Pred prepoznavanjem preverite vir in pravice

Za vsak izvorni predmet najprej ustvarite zapis. Vključite vsaj:

- repozitorij in zbirko;
- stalni spletni naslov ali kataložni identifikator;
- naslov, ustvarjalca ali izdajatelja, datum in obseg, kot jih navaja ponudnik;
- izjavo o pravicah ali licenco in osebo oziroma ustanovo, ki jo je določila;
- datum dostopa in datum prenosa;
- ime, format, velikost in kriptografsko zgoščeno vrednost datoteke;
- podatek, ali gre za izvirno datoteko repozitorija, izpeljanko ali vaš zajem; ter
- znane manjkajoče strani, omejitve dostopa ali občutljivo vsebino.

Ustavite se, če ne morete ugotoviti izvora, pridobiti ali dokumentirati dovoljenja oziroma pojasniti možnosti ponovne objave. Načrt prilagodite, če je raziskovalna uporaba dovoljena, objava posnetkov pa ne. Nadaljujte šele, ko so pridobitev, obdelava in načrtovana objava skladne z zapisom o pravicah. Beseda »spletno« ne pomeni »v javni domeni«.

Učno gradivo pregled ponazori z `rights-and-provenance.sl.md`, `SOURCE_CITATION.sl.md`, `source/dlib-source.json`, `source/commons-source.json` in manifestom zgoščenih vrednosti. dLib zagotavlja trajni URN in bibliografski zapis prek NUK; prikazano polje o pravicah je bilo ob pregledu prazno. Wikimedia Commons navaja dLib kot vir in za nespremenjeno kopijo PDF objavlja presojo javne domene, hkrati pa opozarja, da je treba dodati oznako statusa javne domene v ZDA. Zato mora uporabo v različnih jurisdikcijah dokončno preveriti založnik pri pregledu pravic za različico v1.0. Majhen vzorec je primeren za preskus postopka, ne za predstavljanje celotnega časopisa.

## OCR in HTR rešujeta sorodna, vendar različna problema

**Optično prepoznavanje znakov (OCR)** navadno pomeni samodejno prepoznavanje tiskanih znakov na posnetku strani. **Prepoznavanje rokopisnega besedila (HTR)** napoveduje zaporedja iz rokopisa, pogosto z modeli, ki so naučeni ali prilagojeni na slikah vrstic in prepisih. Meja ni vedno ostra: zgodovinski tisk, mešanica tiska in rokopisa, robni pripisi ter okrasni naslovi jo zabrišejo. Zato zapišite uporabljeni model in postopek, ne le oznake OCR ali HTR.

Če gradivo vsebuje več pisav oziroma rokopisnih rok, boste morda potrebovali ločene modele ali sloje vrednotenja. Ocena zaupanja je rezultat modela po njegovih predpostavkah, ne izmerjena stopnja napak; pred uporabo za filtriranje jo umerite s preverjenim besedilom.

Prepoznavanje je samo ena stopnja. Segmentacija določi območja, stolpce, vrstni red branja in vrstice; prepisovanje napove znake ali besede; popravljanje spremeni napoved; izvoz pa lahko izgubi podatke o postavitvi. Navidez smiselno golo besedilo ima zato lahko pravilne besede v napačnem vrstnem redu ali pa izpusti napis pod sliko.

Uporabniški vmesniki, katalogi modelov in izvozni meniji se spreminjajo. Zabeležite storitev, različico ali datum dostopa, identifikator modela, nastavitve in izvozni format. Ohranite vhod ter preneseni rezultat. Če gostovana storitev nima stabilne različice, to izrecno navedite.

## Ohranite povezave med plastmi dokumenta

Dobro zasnovan besedilni predmet ima več nezamenljivih plasti:

1. **izvorni predmet** — fizični ali izvorno digitalni predmet, ki ga opisuje repozitorij;
2. **sliko strani** — posnetek ali fotografijo s stalnim identifikatorjem strani;
3. **postavitev** — območja, stolpce, vrstice, vrstni red branja in koordinate;
4. **ponudnikov prepis** — besedilo arhiva ali storitve za prepoznavanje;
5. **referenčni ali popravljeni prepis** — človeško preverjeno besedilo po določenih pravilih;
6. **normalizirano besedilo** — za določen namen poenotene zapise, presledke ali znake;
7. **anotacijo** — pojavnice, entitete, teme, uredniške opombe ali jezikoslovne oznake; in
8. **metapodatke ter provenienco** — identiteto, pravice, razmerja in zgodovino obdelave.

Ene plasti nikoli ne prepišite z drugo. Popravek naj kaže na prejšnjo vrednost, mesto v viru, odgovorno osebo ali postopek, datum in pravilo. Element `<choice>` v smernicah TEI lahko na primer poveže izvorno in popravljeno obliko. ALTO XML lahko ohrani prepoznane nize in postavitev strani. Manifest IIIF Presentation lahko poveže urejene poglede strani, slike, pravice in anotacije. Teh standardov vam v razredni preglednici ni treba uporabiti, vendar je njihovo ločevanje predmeta, površine, besedila in opisa uporaben preskus zasnove.

## Pravila prepisovanja napišite pred referenčnim prepisom

**Referenčni prepis**, ki ga pri vrednotenju prepoznavanja pogosto imenujejo *ground truth*, ni neposredna resnica brez posredovanja. Je človeško pripravljen referenčni zapis po izrecnih dogovorih. Dve osebi se lahko ne strinjata, ker ena beleži vidne znake in prelome vrstic, druga pa besede za branje. Pravila napišite vnaprej, preizkusite jih na zahtevnih primerih in jih popravite pred prepisom celotnega vzorca.

Določite vsaj:

- **obseg:** samo tekoče besedilo ali tudi glave, napise pod slikami, oglase, številke strani in marginalije;
- **vrstni red branja:** zaporedje stolpcev, okvirjev, opomb in prekinjenih člankov;
- **prelome vrstic in deljenje besed:** ali ohranite prelome; ali beseda, deljena na koncu vrstice, ostane deljena, se združi ali se zapišeta obe obliki;
- **znake in ligature:** ali vidne ligature in zgodovinske znake zapišete dobesedno, razvežete ali povežete izvorno in normalizirano obliko;
- **pravopis in ločila:** ali ohranite zgodovinski zapis, velike začetnice, okrajšave in ločila;
- **Unicode:** katere sestavljene znake, narekovaje, pomišljaje, presledke in nadomestne znake dovolite;
- **nečitljivo ali manjkajoče besedilo:** kako označite neberljive, poškodovane ali odrezane odlomke;
- **popravke:** kako zapišete tiskarske napake, ročne popravke in uredniške posege; ter
- **postavitev:** ali odstavke, naslove, tabele in napise predstavite v golem besedilu, označevalnem jeziku ali ločeni datoteki.

Te odločitve vplivajo na CER in WER. Če referenčni prepis združi besedo, deljeno na koncu vrstice, OCR pa ohrani vezaj in prelom, rezultat meri tudi razliko med praviloma. Normalizirajte samo značilnosti, ki za preskus niso pomembne, enako pravilo uporabite na obeh besedilih in ga objavite.

## Korpus je zasnovan vzorec

**Ciljna populacija** je širša množica, o kateri želite nekaj trditi. **Vzorčni okvir** je seznam ali mehanizem, iz katerega lahko dejansko izbirate. Med njima so ohranjenost, katalogizacija, digitalizacija, licence, razvrščanje rezultatov in omejitve prenosa. Vsako vrzel opišite.

Razlikujte tri povezane lastnosti:

- **pokritost** pove, ali so pomembne kategorije in obdobja prisotni;
- **uravnoteženost** opisuje njihova razmerja v korpusu;
- **primerljivost** pove, ali so skupine nastale in bile obdelane dovolj podobno za načrtovano primerjavo.

Uravnotežen korpus ni samodejno reprezentativen: enako število enot po desetletjih se lahko razlikuje od zgodovinske populacije. Primerljivost odpove, če ima eno desetletje ponudnikov OCR, drugo pa na novo popravljeni HTR.

Pripravite vzorčno tabelo z eno vrstico na kandidatni predmet ter polji za sloj, ustreznost, izbor, pravice, kakovost posnetka, način prepoznavanja in razlog za izločitev. Dokumente in besede preštejte po pomembnih slojih. Naključni izbor znotraj vnaprej določenih slojev lahko omeji pristranskost priročnosti. Za redke formate ali analizo napak boste morda potrebovali namenski izbor; tako ga tudi poimenujte.

## Vzorec za vrednotenje mora razkriti napake

Ne vrednotite samo najčistejše strani. V vzorec vključite lastnosti, ki lahko vplivajo na trditev: leto, naslov, tisk ali roko, kakovost posnetka, število stolpcev, jezik, žanr, napise, tabele, poškodbe in osebna imena. Del vzorca izberite naključno ali sistematično, da celotne ocene ne določijo samo nepozabne napake. Namenski nabor posebej zahtevnih primerov poročajte ločeno.

En preverjeni odlomek zadošča za učenje postopka. Pri raziskavi zabeležite velikost vzorca, izbor, sloje, prepisovalce, način preverjanja, reševanje nesoglasij in različico pravil. Ocena, ki izključi oglase ali rokopis, o teh delih ne pove ničesar.

## Razdelani primer: arhivsko trenje

### Kje prvi postopek odpove

Učno gradivo se začne z dvostranskim ilustriranim časopisom in ponudnikovim OCR. Če izvoz obravnavate kot članek, potiho sprejmete nestabilni vrstni red stolpcev, izpuščene napise in poškodovana imena. Če vsak napis obravnavate kot članek, zamešate dokumentarno in analitično enoto. Vzorec je premajhen za sklep o celotnem časopisu.

### Ročni poseg

Referenčni prepis sledi določenemu vrstnemu redu, ohrani zgodovinski zapis in ločila ter združi prelome, ki so samo posledica postavitve. Natančni izvoz TXT iz dLib ostane nespremenjen v `source/`; gradilnik ga dekodira, izbere določene vrstice in iz njihove presledkovno normalizirane vsebine ustvari izpeljanko v `raw/`. Odločitev o delu ob viru je zabeležena, ročno preverjeni odlomek pa ostane ločena, dokumentirana datoteka v `reference/`. Človek primerja sliko in besedilo, razvrsti napake, preveri sporna imena ter po dokumentirani normalizaciji pri pripravi odlomka izračuna CER in WER po enotnih pravilih poravnave.

### Kaj ostane negotovo

Natisnjena oblika »Mr. Meker« ostaja ločena od zavrnjenega normativnega kandidata Ezra Meeker, datum nastanka fotografije struge je neznan in ni prevzet iz datuma številke, neprepisana območja pa niso ovrednotena. Vaja ne ocenjuje razlik med številkami, postavitvami ali modeli.

### Vpliv na nadaljnjo trditev

Po dokumentirani normalizaciji pri pripravi odlomka ima preverjeno besedilo CER 0,020305 in WER 0,096774, vendar poškodovano osebno ime še vedno spremeni natančno iskanje. Utemeljeno lahko trdite, da je pri tem odlomku treba preverjati imena. Ne smete pa sklepati o stopnji napak celotne publikacije ali odsotnosti v zgodovini zgolj na podlagi neuspešnega iskanja.

## Izračunajte CER in WER

Rezultat prepoznavanja poravnajte z referenčnim prepisom ter preštejte najmanjše število zamenjav \(S\), izpustov \(D\) in vstavkov \(I\). Če ima referenca \(N\) enot, velja:

\[
\mathrm{stopnja\ napak}=\frac{S+D+I}{N}
\]

Za **stopnjo napak na znakih (CER)** so enote znaki, za **stopnjo napak na besedah (WER)** pa vnaprej določene besedne pojavnice. Navedite, ali med znake štejete presledke, ločila in razliko med velikimi ter malimi črkami, kako poenotite Unicode in kako razdelite besedilo na besede. Zaradi vstavkov je lahko stopnja napak večja od 1. Rezultata ne preimenujte v »odstotek natančnosti«, ne da bi to razmerje natančno opredelili.

Po dokumentirani normalizaciji pri pripravi odlomka učno gradivo vsebuje 591 referenčnih znakov s 7 zamenjavami, 5 izpusti in 0 vstavki (skupaj 12), zato je CER \(12/591=0{,}020305\). Pri 93 besedah je 7 zamenjav, 2 izpusta in 0 vstavkov (skupaj 9), zato je WER \(9/93=0{,}096774\). Pri izenačenih najmanjših poravnavah imajo prednost ujemanje, zamenjava, izpust in vstavek v tem vrstnem redu; stopnji sta zaokroženi na šest decimalk po pravilu polovice k sodemu številu. Ponovljivi vrednosti ne merita izpuščenih presledkov postavitve in opisujeta en odlomek, ne številke, časopisa, portala ali modela.

## Eno število razčlenite v profil napak

CER in WER združita različne težave. Dodajte tabelo s položajem v viru, referenčno in prepoznano obliko, vrsto posega, kategorijo ter verjetno posledico. Koristne kategorije so:

- zamenjava znakov, zlasti diakritike in podobnih zgodovinskih črk;
- napačno združene ali razdeljene besede;
- deljenje ob koncu vrstice;
- izpuščena vrstica, območje, stolpec ali napis;
- ponovljeno besedilo ali napačen vrstni red branja;
- razlika v ločilu ali veliki začetnici;
- napaka v osebnem imenu, datumu ali številu; ter
- razlika v uredniškem pravilu, ne napaka prepoznavanja.

Kadar vzorec to dopušča, poročajte rezultate po pomembnih slojih. Nizek skupni CER se lahko pojavi hkrati s popolnim izpustom napisov ali s slabim priklicem imen. Zgodovinski zapis pa ni napaka OCR, če je tako zapisano na sliki.

## Preverite raziskovalno nalogo, ne splošnega praga

Splošni prag za »dovolj dober« CER ne obstaja. Sprejemljiva napaka je odvisna od naloge in porazdelitve napak. Iskanje po celotnem besedilu izgubi priklic, če so ciljni nizi poškodovani. Frekvenčni seznam eno besedo razdrobi v različice. Razpoznavanje imen je občutljivo na redka imena. Tematske in razvrščevalne metode lahko uredijo ponavljajoči se šum. Točno navajanje, kolacioniranje in znanstveno izdajanje zahtevajo neposredno preverjanje slike.

Preverite samo načrtovano nalogo:

1. Zapišite trditev in besedilne lastnosti, od katerih je odvisna.
2. Manjšo analizo izvedite na ponudnikovem in preverjenem besedilu.
3. Primerjajte najdene enote, števila, vrstni red ali razvrstitve.
4. Po slojih preglejte lažno negativne in lažno pozitivne rezultate.
5. Odločite se, ali boste besedilo popravili, zamenjali metodo, zožili trditev ali se ustavili.

Raziskavi Traub, van Ossenbruggen in Hardman ter Hill in Hengchen pokažeta, da je vpliv napak OCR odvisen od raziskovalne naloge. Zato poročilo združite z osnovnimi metrikami, kategorijami napak in preskusom nadaljnje analize.

## Dvojnike, ponatise in različice ohranite kot razmerja

Ista intelektualna vsebina se lahko pojavi kot popolnoma enaka datoteka, drugi posnetek, agencijsko besedilo, spremenjeni ponatis, nova izdaja ali nov izvoz OCR iste strani. To niso enake vrste dvojnikov.

Uporabljajte stabilne identifikatorje. Zgoščene vrednosti odkrijejo bitno enake datoteke, ne pa intelektualne istovetnosti. Preglejte metapodatke in besedilo ter zabeležite razmerja, kot so `duplicate_of`, `reprint_of` in `version_of`. Določite, ali analiza šteje primerke, članke ali dela. Ponavljanja ne odstranjujte, če raziskujete širjenje.

Če mora več pojavitev zastopati en zapis, ohranite tabelo razmerij in izrecno pravilo izbire, nato preverite identifikatorje in število skupin. Podobnost je podatek za presojo, ne zgodovinska razlaga.

## Postopek zasnujte kot sled dokazov

Uporabite naslednje mape ali enakovredne plasti shranjevanja:

```text
source/          nespremenjeni predmet, zapisa ponudnikov in bajtno ohranjeni izvoz
reference/       priročniška opazovanja, referenčni prepis in pravila
teaching/        izrecno označene sintetične motnje
raw/             normalizirani odlomek OCR-ja in neurejene delovne vrstice
interim/         kandidati, ki čakajo na pregled ob viru ali referenci
cleaned/         preverjeni zapisi, kopija prepisa in odločitve
output/          metrike, pregled napak in povzetki zapisov
validation/      pričakovane vrednosti, zgoščene vrednosti in poročila
known-problems/  nerešene napake in omejitve obsega
```

Za vsako spremembo zapišite vhod, izhod, postopek, različico ali datum dostopa, parametre, izvajalca, datum in rezultat. Manifest naj poveže identifikatorje, poti, zgoščene vrednosti, medijske tipe in vloge plasti. Po popravkih preverite obstoj datotek, enoličnost identifikatorjev, povezave do strani, pričakovana števila, nespremenjenost surove plasti, kodiranje in ponovni izračun metrik.

Preverjanje lahko avtomatizirate, vendar je to izbirna razširitev. Enako sled lahko vzpostavite s preglednico in orodjem operacijskega sistema za zgoščene vrednosti. Za uspešno opravljeno poglavje morate prikazati sled dokazov, ne uporabiti določene platforme.

## Vaja: oblikujte eno utemeljeno trditev

Prenesite [ZIP učnega gradiva Arhivsko trenje](../../assets/downloads/archival-friction-v1.zip). Zgradbo lahko pregledate v [izvornem drevesu paketa](https://github.com/damjan-popic/digital-humanities-handbook/tree/main/teaching-data/archival-friction).

1. Preberite zapis o pravicah in navedbo vira. Pojasnite, katera presoja podpira ponovno uporabo PDF-ja in katero preverjanje mora še opraviti založnik.
2. Pred branjem prepisov preglejte obe strani. Poiščite dve postavitveni lastnosti, ki lahko vplivata na vrstni red branja.
3. Primerjajte `raw/provider-ocr.txt` in `reference/reference-transcription.txt`. Razvrstite vsaj pet razlik.
4. Preberite `reference/transcription-policy.sl.md`. Presodite, ali je vsaka razlika napaka prepoznavanja, razlika v pravilu ali nerešeno branje.
5. Potrdite vsako znakovno in besedno vrednost S/D/I, po objavljenem pravilu znova izračunajte stopnji ter svojo razvrstitev primerjajte z `output/ocr-error-audit.csv`.
6. Izberite eno nalogo — iskanje imena, štetje oblike ali navajanje povedi — in jo preizkusite na obeh prepisih.
7. Napišite trditev, ki velja samo za ta vzorec, nato pa dodajte poved o tem, česa ne morete posplošiti.

Vajo uspešno opravite, če lahko druga oseba vsako število in navedek poveže z datoteko in stranjo, po vaših pravilih ponovi razvrščanje ter razume, zakaj sklep ni širši od vzorca. Izračun CER in WER se začne po dokumentiranem izboru odlomka in normalizaciji presledkov, zato ne meri izpuščenih presledkov postavitve drugod v ponudnikovem izvozu.

## Napake, ustavitev in popravki

Ustavite se, kadar pravice niso skladne z načrtovanim rezultatom, izvor ni ugotovljen, manjkajoče strani onemogočijo primerjavo ali referenčnega prepisa ni mogoče preveriti. Načrt popravite, če manjkajo pomembni sloji, identifikatorji niso stabilni, so se pravila med delom spremenila, je postopek napačno določil območja ali vrstni red branja oziroma se rezultat po popravku bistveno spremeni. Z dokumentirano omejitvijo nadaljujte le, kadar ste napako izmerili, omejili njen možni vpliv in ohranili utemeljenost trditve.

Surove datoteke ne prepišite. Neuspeli rezultat ohranite, popravke zabeležite in ustvarite novo izpeljanko. Ponovitev po spremembi modela ali vmesnika zapišite kot novo različico.

## Etične in licenčne omejitve

Razpoznavanje lahko razkrije imena ali občutljiva dejstva, ki jih je bilo na slikah težko iskati. Javna domena ne odpravi zasebnosti, avtoritete skupnosti ali škode zaradi novega konteksta. Upoštevajte omejitve repozitorija in veljavno pravo, zmanjšajte količino nepotrebnih osebnih podatkov ter dokumentirajte odločitve o dostopu.

Skeniranje, katalogizacijo, prepisovanje, popravljanje in znanje skupnosti priznajte kot delo. Ponudnikovega OCR ne predstavljajte kot svoj prepis. Pri študentskem ali prostovoljskem delu določite usposabljanje, pregled, priznanje prispevka in reševanje nesoglasij.

## Refleksija

- Katera besedila manjkajo, še preden se prepoznavanje začne?
- Katero pravilo prepisovanja najbolj spremeni vašo načrtovano meritev?
- Ali vzorec kakovosti predstavlja običajno gradivo, zahtevno gradivo ali oboje?
- Bi isti profil napak dopuščal iskanje, ne pa tudi točnega navajanja?
- Kdaj je ponatis šum in kdaj dokaz o širjenju besedila?

## Povzetek

Korpus je utemeljeno razmerje med vprašanjem, populacijo, razpoložljivim vzorčnim okvirom in povezanimi predstavitvami. OCR in HTR ustvarjata uporabne napovedi, ne prosojnega besedila. Ohranite sliko, postavitev, ponudnikov, popravljeni, normalizirani in anotirani prepis; pravila določite pred vrednotenjem; CER in WER poročajte skupaj s pravili ter sloji; nato preverite načrtovano raziskovalno nalogo. Pravice, provenienca in znane napake so sestavni del postopka. Več besedila ne popravi nepremišljenega vzorca.

## Nadaljnje branje in veljavni tehnični viri

- Biber, Douglas. 1993. [»Representativeness in Corpus Design.«](https://doi.org/10.1093/llc/8.4.243) *Literary and Linguistic Computing* 8 (4): 243–257.
- Hill, Mark J., in Simon Hengchen. 2019. [»Quantifying the Impact of Dirty OCR on Historical Text Analysis.«](https://doi.org/10.1093/llc/fqz024) *Digital Scholarship in the Humanities* 34 (4): 825–843.
- Traub, Myriam C., Jacco van Ossenbruggen in Lynda Hardman. 2015. [»Impact Analysis of OCR Quality on Research Tasks in Digital Archives.«](https://doi.org/10.1007/978-3-319-24592-8_19) V *Research and Advanced Technology for Digital Libraries*, 252–263.
- OCR-D. [Smernice za pripravo referenčnega prepisa](https://ocr-d.de/en/gt-guidelines/trans/) in [opredelitev CER pri zagotavljanju kakovosti](https://ocr-d.de/en/spec/ocrd_eval.html) (sprotno posodobljena tehnična dokumentacija; dostop 2. septembra 2026).
- Text Encoding Initiative. [Smernice TEI P5, `<choice>`](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-choice.html), različica 4.11.0 z dne 18. februarja 2026 (dostop 2. septembra 2026).
- Library of Congress. [ALTO: Technical Metadata for Layout and Text Objects](https://www.loc.gov/standards/alto/) (trenutna uradna shema 4.4; dostop 2. septembra 2026).
- Konzorcij IIIF. [Presentation API 3.0](https://iiif.io/api/presentation/3.0/) (ob dostopu stabilna različica 3.0.0; dostop 2. septembra 2026). Hkrati je bil objavljen kandidat za izdajo 4.0, zato pri izvedbi zabeležite uporabljeno različico.

Tehnične strani in vmesniki se spreminjajo. Zabeležite različice in datume dostopa.
