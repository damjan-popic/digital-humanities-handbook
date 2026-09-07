---
title: "GIS in prostorska humanistika"
description: "Zgodovinski kraji, več možnih identifikacij in časovno opredeljene geometrije kot preverljivi humanistični argumenti."
tags: [GIS, kartiranje, geokodiranje, kraj, negotovost]
status: draft
translation_status: machine-assisted draft; requires human language review
---

# GIS in prostorska humanistika

## Učni cilji

Po tem poglavju boste znali:

- razlikovati med krajem, njegovimi imeni, geometrijami in upravno pripadnostjo;
- ločiti datum vira, predstavljeni čas in datum prostorske identifikacije;
- pojasniti koordinatni referenčni sistem, georeferenciranje, merilo in položajno točnost;
- ohraniti nerazrešene kandidate ter preveriti identifikacijo z neodvisnimi dokazi;
- preveriti, kako meje, imenovalci, manjkajoči zapisi in prometne predpostavke vplivajo na sklep;
- objaviti dostopen zemljevid s tabelaričnim prikazom dokazov in omejitev.

## Pred začetkom

Je človek prestopil mejo ali je meja prešla prek njegovega bivališča? Zapis o drugačni upravni pripadnosti prebivalca sam po sebi ne dokazuje selitve. Tudi pismo z navedbo »St. Peter« ne določa ene same nedvoumne točke. Preden odprete zemljevid, zapišite, kateri dokazi bi omogočili razlikovanje med gibanjem, upravno spremembo in napačno uredniško identifikacijo. Katere možnosti lahko ohranjeni viri sploh pomagajo preveriti?

Spremljevalni dosje iz poglavja [Podatkovne zbirke in SQL](databases-sql.md) obravnava imena, status, jezikovno rabo in ozemeljsko pripadnost. Osebe in poskus s spreminjajočo se mejo so izrecno sintetični. Ne gre za rekonstruirane življenjepise oseb iz avtentičnega časopisnega gradiva. [Prenosljivi paket](../../assets/downloads/contested-models-v1.zip) vsebuje tudi pravi načrt Ljubljane in današnje koordinate orientacijskih točk. Te ravni dokazov ločujte: zgodovinski načrt ne potrjuje izmišljene upravne meje.

Besedilo je strojno podprt prevodni osnutek; pred potrditvijo je potreben strokovni pregled slovenskega jezika in terminologije.

## Osrednji argument: koordinate so opredeljene trditve

Prostorska humanistika raziskuje, kako lokacija, razdalja, ozemlje in doživljanje kraja prispevajo k interpretaciji. Točkovni zemljevid lahko pokaže razporeditev, ne more pa sam ugotoviti, kaj je kraj pomenil prebivalcu ali zakaj ga je vir imenoval. Zbornik [The Spatial Humanities](https://iupress.org/9780253222176/the-spatial-humanities/) obravnava GIS kot raziskovalno orodje, katerega predstavitve morajo odgovarjati zgodovinskim in interpretativnim vprašanjem, ne pa jih nadomeščati.

Praktično načelo je zato naslednje: odlomek, odločitev o identifikaciji, geometrijo in časovno opredelitev ohranite kot ločljive zapise. Upravna oznaka priča o razvrščanju; koordinata je uredniška prostorska predstavitev. Nobena nujno ne izraža samoopredelitve prebivalca. Tudi zgodovinski zemljevid zahteva kritiko vira. Harley v razpravi [»Deconstructing the Map«](https://doi.org/10.3138/E635-7827-1757-9T53) v analizo vključuje družbene in politične okoliščine kartografije. Vprašajte se, kdo je načrt naročil, kaj je naredil vidno in kaj so njegove konvencije izključile.

## Kraj, toponim, geometrija in ozemlje

**Toponim** je zemljepisno ime. **Entiteta kraja** je referent, ki ga projekt obravnava kot istega skozi zapise; tudi njegovo kontinuiteto je včasih treba utemeljiti. **Geometrija** je prostorska predstavitev za določen namen. **Upravna enota** je institucionalno opredeljeno ozemlje; njeno ime, pristojnosti in meja se ne spreminjajo nujno hkrati. **Pot** predstavlja zaporedje ali možen potek gibanja. **Regija** je lahko upravna, okoljska ali opredeljena z vsakdanjo rabo. Zamišljene domovine ali spominske soseske morda ni mogoče upravičeno zapreti v poligon.

Za dosje vodite tabelo krajev, tabelo trditev o imenih in časovno omejeno ozemeljsko pripadnost. Ko sodobni normativni vir določi prednostno ime, ne preimenujte vseh zgodovinskih pojavitev. Izvirni zapis »St. Peter« ohranite poleg kandidatov `SYN-L1` in `SYN-L2`. Oba sta izmišljena za vajo; ne dokazujeta, da sta konkretna resnična kraja nosila to ime.

Točka lahko zadošča za približen prikaz soseske. Tloris stavbe podpira drugačno vprašanje. Težišče regije ne pokaže, kje so živeli njeni prebivalci. Pri vsaki geometriji utemeljite ustreznost in navedite, katerih sklepov ne dovoljuje.

## Imeniki zemljepisnih imen brez samodejne gotovosti

Zgodovinski imeniki zemljepisnih imen povezujejo imena, identifikatorje in opise v različnih časovnih ter jezikovnih okoliščinah. [Southall, Mostern in Berman](https://doi.org/10.3366/ijhac.2011.0028) pojasnjujejo, zakaj zgodovinski imenik potrebuje več kot seznam koordinat. Normativni identifikator pomaga razlikovati zapise, vendar ne razreši vsakega zgodovinskega vprašanja istovetnosti.

Pri poizvedbi shranite izvirno iskalno obliko, jezik, datum vira, uporabljeni imenik, različico ali datum dostopa, vrnjeni identifikator, alternative in pregledovalčevo odločitev. Preizkusite več imenskih oblik. Preverite sosednje kraje, institucionalno okolje in sočasni opis. Ocena storitve lahko meri podobnost nizov ali vrstni red zadetkov; brez umerjene validacijske raziskave je ne preimenujte v »90-odstotno zgodovinsko pravilnost«.

Ohranite zavrnjene in nerazrešene kandidate. Zabeležite razlog zavrnitve, namesto da kandidata neopazno izbrišete. Ime, ki ga sodobni imenik ne pozna, lahko označuje izginulo naselje, neuradno četrt, preimenovano ulico ali napako v prepisu. Uspešen zadetek pa lahko kaže na oddaljen današnji kraj z enakim imenom. Preglejte tudi vzorec navidezno zanesljivih ujemanj, ne samo neuspešnih poizvedb.

## Časovno opredeljen model kraja

Vir, identifikacija kraja in prostorski pripis ozemlju odgovarjajo na različna vprašanja:

| Zapis | Bližnjica s sodobno točko | Opredeljena alternativa |
|---|---|---|
| »St. Peter« v `SYN-D2` | prvi zadetek v iskalniku | ohranite `SYN-L1` in `SYN-L2`; odločitev ostaja odprta |
| Bivališče A v `SYN-L1` | ena koordinata in današnja država | datirana trditev o bivališču, geometrija in pripadnost |
| Poznejša upravna oznaka | sklep o selitvi | primerjava stalnosti bivališča z različicami meje |
| Načrt, izdan leta 1910 | vse pojave datirajte v leto 1910 | ločite izdajo od predstavljenega časa in izmere |

Zgodovinski vir lahko opisuje starejše potovanje, ponatisne starejši načrt ali predlaga prihodnjo cesto. Datum objave hranite ločeno od predstavljenega časa ter podatkov o izmeri in popravkih, kadar so znani. Neznani datumi naj ostanejo neznani. Ne ustvarjajte navidezno natančnega intervala samo zato, ker časovno filtriranje v programu zahteva dve datumski polji.

Pri nerazrešeni identifikaciji sta dve vrstici s pojasnilom lahko ustreznejši rezultat kot dve prepričljivo izrisani bivališči. Število kandidatov ni število dejansko naseljenih krajev. Paket hrani časovno okno omembe ločeno od veljavnosti meje in imena. Primerjalno obdobje je dejanski polodprti presek ene različice meje in ene različice imena ter je izrecno označeno kot zgodovina možnega kraja, ne trajanje omembe. Zato sprememba imena leta 1917 znotraj iste različice meje ne izgine. To razliko pojasnite tudi bralcu, ki vidi samo izvoženo tabelo.

## Koordinatni referenčni sistemi in transformacije

Koordinate razlagamo znotraj **koordinatnega referenčnega sistema**, ki opredeli tudi enote in referenčni okvir položaja. Zemljepisna dolžina in širina sta kotni koordinati. Projicirane koordinate omogočajo ravninske izračune na določenem območju uporabe. Površina, izračunana v kvadratnih stopinjah, ni površina v kvadratnih metrih.

Dodelitev sistema pove, kaj obstoječa števila pomenijo; transformacija izračuna druga števila za drug sistem. Če ti operaciji zamenjate, se lahko sloj premakne, njegova oblika pa ostane prepričljiva. Pred razlago prekrivanja preverite razpone koordinat, vrstni red osi in enote. Paket predpomnjene koordinate iz zemljepisne dolžine in širine pretvori v EPSG:3794, pri čemer izrecno določi dolžino kot prvo os. Geodetska uprava opisuje državni referenčni okvir in poimenovanje [D96-17/TM](https://www.e-prostor.gov.si/podrocja/drzavni-koordinatni-sistem/horizontalna-sestavina/); programska oprema lahko uporablja tudi oznako D96/TM.

Zabeležite izvorni in ciljni sistem, izvedbo transformacije ter potrebne transformacijske mreže. Sprotna projekcija za prikaz ne spremeni shranjenih izvornih koordinat. Za programske korake uporabite dokumentacijo [QGIS 3.40 o projekcijah](https://docs.qgis.org/3.40/en/docs/user_manual/working_with_projections/working_with_projections.html). Dokumentirana različica ni trditev o najnovejši izdaji.

## Merilo, ločljivost in položajna točnost

Merilo povezuje razdaljo na zemljevidu z razdaljo na terenu. Ločljivost opisuje najmanjšo predstavljeno ali vzorčeno enoto. Položajna točnost se nanaša na ujemanje z utemeljeno referenčno lokacijo. Natančnost zapisa opisuje drobnost številskega izraza. Lastnosti so povezane, vendar niso zamenljive.

Avtentični načrt v paketu je Kochova *Ljubljana* iz leta 1910 v merilu 1 : 8.200, kakor ga opisuje [dLib.si](https://dlib.si/details/URN:NBN:SI:IMG-132KCU7C). Pri tem nominalnem merilu milimeter na tisku pomeni 8,2 metra na terenu. Znak za stavbo je lahko kljub temu posplošen ali premaknjen. Višja ločljivost skena ne povrne podrobnosti, ki jih kartograf ni zapisal.

Prav tako šest decimalnih mest pri današnji orientacijski točki ne pomeni geodetske točnosti. Paket ločeno beleži natančnost, navedeno v Wikidata, in ročno izbrane slikovne točke. Nekatere koordinate označujejo objekt na splošno, ne določljivega vogala. Če takšno neskladje prezrete, primerjate različne prostorske referente, ne pa napake pri istem položaju.

## Georeferenciranje kot preverljiv postopek

Georeferenciranje oceni transformacijo med slikovnimi in referenčnimi koordinatami. Izberite kontrolne točke, ki v obeh virih označujejo isti fizični element, ter jih razporedite po celotnem območju. Izračuna transformacije ne naslonite na eno samo ulico ali tesno skupino objektov. Vogal je lahko bolj ponovljiv kot približno središče, če se stavba medtem ni spremenila.

Afina transformacija omogoča premik, zasuk, spremembo merila in strig. Ne odpravi vsake lokalne deformacije. Prožnejša transformacija lahko zmanjša odstopanja pri kontrolnih točkah, hkrati pa povzroči neutemeljeno ukrivljanje med njimi. Izberite jo glede na predpostavke in neodvisno preverjanje, ne samo glede na privlačen rezultat.

Nekaj točk izločite iz izračuna in jih namenite neodvisnemu preverjanju. Odstopanje je razlika med napovedanim in referenčnim položajem. Koren povprečne kvadratne napake (RMSE) povzema razdalje, vendar je njegova razlaga odvisna od enot, kakovosti in razporeditve točk. [Dokumentacija georeferencerja QGIS](https://docs.qgis.org/3.40/en/docs/user_manual/managing_data_source/georeferencer.html) pojasni transformacije in obravnavo kontrolnih točk; program ne potrjuje njihove zgodovinske ustreznosti.

## Izdelani primer: neuspešno preverjanje poravnave

Paket vsebuje sken dLib z oznako javne domene, šest prvih ročnih izbir orientacijskih točk, predpomnjene današnje koordinate in ponovljiv afini izračun. Štiri točke določajo transformacijo, železniška postaja in stolnica pa sta izločeni za preverjanje. Gre za namenoma ohranjen pilot, ne za potrjene geodetske kontrolne točke. Središča objektov in slikovne izbire zahtevajo ročni pregled.

| Preverjanje | Rezultat v metrih | Razlaga |
|---|---:|---|
| RMSE štirih uporabljenih kontrolnih točk | 15,231 | opisuje le prileganje pri izbranih kontrolah |
| RMSE dveh neodvisnih točk | 220,063 | ne podpira trditve o približno 15-metrski točnosti |
| Izločitev zahodne kontrolne točke in naknadno preverjanje | 1.090,241 | razkrije šibko prostorsko oporo in ekstrapolacijo |
| Samostojno preverjanje stolnice | 142,481 | ponovno preverite slikovni element in referent koordinate |

Rezultate lahko ponovite brez QGIS. Povezani [postopek georeferenciranja](../workflows/mapping/georeference-and-check-a-historical-map-in-qgis.md) dodaja navodila za grafični vmesnik, shranjevanje transformacije in primerjavo s sodobnim slojem. Postopek v vmesniku še potrebuje dokumentiran pregled v QGIS. Številski pilot ne pomeni, da je bil dobljeni raster tudi vizualno potrjen.

Slabe kontrolne točke ne izbrišite samo zato, da izboljšate oceno. Ponovno odprite sliko in referenčni opis ter zabeležite, ali je bila točka napačno prepoznana, premaknjena, posplošena ali premalo natančno določena. Popravljeni poskus shranite ločeno. Majhno odstopanje pri prileganju in veliko pri neodvisnem preverjanju skupaj koristno opišeta meje modela.

## Izdelani primer: premakne se meja

Poskus z mejo uporablja izrecno izmišljen kvadrat s stranico 1.000 metrov v lokalnem inženirskem koordinatnem sistemu. To ni EPSG:3794 in ne gre za zgodovinske ljubljanske meje. Navpična ločnica se leta 1920 premakne z x=500 na x=600. Bivališče A ostane pri x=550; dosje predpostavi kontinuiteto do konca leta 1925. Vzhodno ozemlje vključuje samo ločnico, zato je pravilo pripisa jasno.

| Kandidat | Središčni x | Pripadnost leta 1910 | Pripadnost leta 1925 | Ob položajni negotovosti ±75 m |
|---|---:|---|---|---|
| `SYN-L1` | 550 m | `SYN-EAST` | `SYN-W` | obe ozemlji v obeh obdobjih |
| `SYN-L2` | 800 m | `SYN-EAST` | `SYN-EAST` | vzhodno ozemlje v obeh obdobjih |

Pri razvrščanju po središčni točki se ozemeljska pripadnost A spremeni brez selitve. Če upoštevate območje negotovosti, same geometrije ne zadoščajo za enolično pripadnost. Razpon ±75 metrov je predpostavka analize občutljivosti, ne izmerjen interval zaupanja. Nerazrešena omemba delovnega kraja ne sme nadomestiti trditve o bivališču.

[Povezani postopek](../workflows/mapping/model-changing-place-names-and-boundaries.md) ponovi to tabelo. Resnična zgodovinska raziskava bi potrebovala še dokaze o datumu in geometriji meje, stalnosti bivališča ter upravnem pomenu spremembe. Sintetični izračun pokaže logične posledice predpostavk, ne zgodovinskih dejstev.

## Prostorsko združevanje in manjkajoči podatki

Prostorsko združevanje pripiše atribute glede na vsebovanost, presečišče ali bližino. Prostorski pogoj združite s časovnim: točka in poligon, ki se na zaslonu prekrivata, se lahko nanašata na različni stoletji. Navedite, kako obravnavate točke na meji, prekrivajoče se pristojnosti in negotove intervale. Možno pripadnost ločite od pripadnosti pri vseh dovoljenih položajih.

Nelocirane omembe vključite v imenovalec poročila o pokritosti. Če lahko umestite deset od dvajsetih pisem, zemljevid teh desetih ne opiše nujno geografije celotne korespondence. Manjkajoči podatki so lahko povezani z jezikom, katalogizacijo, razpoložljivostjo mestnih naslovov ali selektivnim ohranjanjem. Prazna regija lahko kaže pomanjkanje virov, digitalizacije ali uspešnih identifikacij, ne odsotnosti zgodovinskega dogajanja.

Pred razlago gostote primerjajte ujemajoče se in neujemajoče se zapise po obdobju, vrsti vira in jeziku. Objavite tabelo nerazrešenih zapisov z razlogi in dovoljenimi kratkimi odlomki. Koordinate ne določite na silo samo zato, da bi bila pokritost videti popolna.

## Kartogrami, imenovalci in problem prostorskih enot

Kartogram obarva območja glede na vrednost. Število dogodkov odgovarja na drugačno vprašanje kot stopnja glede na prebivalstvo. Dva izmišljena okraja imata denimo 20 in 10 ohranjenih pisem, vendar 2.000 in 500 relevantnih prebivalcev. Po številu pisem vodi prvi; stopnji pa sta 10 in 20 pisem na tisoč prebivalcev. Nobena vrednost sama ne meri pismenosti brez predpostavk o avtorstvu, ohranjenosti in ustrezni populaciji.

Rezultati se spreminjajo tudi z mejami in velikostjo združenih območij. To je **problem spremenljive prostorske enote** oziroma MAUP. [Fotheringham in Wong](https://doi.org/10.1068/a231025) obravnavata njegove posledice za večspremenljivostno analizo. Pri preprostejši vaji primerjajte števila in stopnje ob drugačnem združevanju ter pojasnite, kateri prebivalci in zapisi sestavljajo imenovalec.

Števca iz leta 1850 brez utemeljitve ne delite z današnjim prebivalstvom. Manjkajoče vrednosti ločite od ničel. Objavite števec, imenovalec, obdobje in meje razredov, da bo mogoče obarvanost rekonstruirati tudi brez zemljevida.

## Poti, razdalja in dostopnost

Ravna črta med omenjenima krajema ni dokaz potovanja. Vir lahko opisuje spomin, posredno poročanje ali zamišljeni cilj. Tudi pri dokumentirani poti je najkrajša današnja cestna povezava lahko zgodovinsko nemogoča. Na dostopnost vplivajo mostovi, mejni nadzor, naklon, letni čas in razpoložljivi načini prevoza.

Določite, ali ocenjujete geometrijsko razdaljo, razdaljo po omrežju, potovalni čas ali dokumentirani itinerar. Omrežje poti potrebuje datirane odseke in izrecne predpostavke o stroških prehoda. Preverite vsaj eno verjetno alternativo: odstranite nepotrjeni most ali spremenite hitrost hoje, namesto da objavite en sam navidezno točen čas.

Pri dvoumnem »St. Peter« primerjajte posledice obeh kandidatov, vendar ne izmišljajte poti, da bi z njo krožno dokazali identifikacijo. Argument o verjetnosti poti je uporaben le, če so njegove zgodovinske prometne predpostavke neodvisno utemeljene. Besedilno zaporedje ohranite tudi takrat, ko ni mogoče narisati upravičene povezave.

## Oblikovanje, dostopnost in občutljive lokacije

Izrez, oznake, razredi in izpusti vplivajo na kartografski argument. Za urejene količine uporabite zaporedno barvno lestvico; manjkajoče podatke prikažite nevtralno in jasno. Ne zanašajte se samo na barvo. Simbole kandidatov povežite z identifikatorji, kategorijami negotovosti in razlago. Sintetični model meje mora biti vidno označen.

Priložite tabelo vseh prikazanih identifikatorjev, obdobij, pripadnosti, negotovosti in povezav do virov. Besedilni opis naj pove vzorec in izjeme, ne samo tega, da zemljevid obstaja. Oznake naj ostanejo berljive pri predvideni velikosti izpisa; preverite svetlo in temno ozadje. Interaktivni zemljevid potrebuje tudi tipkovnični dostop in prenosljivo alternativo.

Natančne lokacije lahko ogrozijo ranljive žive skupnosti, sveta mesta ali arheološka najdišča. Javna dostopnost podatkov ne odpravi odgovornosti. Pred objavo presodite soglasje, omejitve in predvidljive zlorabe; razmislite o posplošitvi ali omejenem dostopu. Kjer je dovoljeno, varno ohranite izvorni zapis ter pojasnite javno posplošitev, ne da bi razkrili varovane koordinate.

## Hibridno modeliranje

Vseh razlik ni treba prenesti v eno predstavitev. Relacijske tabele ohranijo poizvedljive trditve o krajih; TEI/XML besedilne različice in uredniško strukturo; GeoPackage datirane geometrije; graf pa omogoča raziskovanje povezav ali poti. Faksimili in diplomatski prepis ohranijo dokazno gradivo. Prozne opombe hranijo razlike, ki jih ne smemo prisiliti v kategorije.

Vprašajte se, katere razlike morajo biti poizvedljive, katere morajo ostati obnovljive in katere naj se upirajo formalizaciji. Stabilni identifikatorji povezujejo predstavitve, ne da bi jim vsilili enako notranjo strukturo. Pri izvozu preverite, ali lahko bralec iz točke še vedno pride do konkretnega odlomka in uredniške odločitve.

## Vaja

Razpakirajte spremljevalni arhiv in izvedite:

```bash
python run.py --output output-first
```

Za vsak poskus uporabite novo izhodno mapo. Pred kartiranjem preglejte `membership.csv`, `gcp-residuals.csv` in `gcp-leave-one-out.csv`. Primerjajte pripadnost po središčni točki s pripadnostjo ob negotovosti ter pojasnite, zakaj dveh kandidatov za isto ime ne smete šteti kot dve bivališči. Nato ob sliki in predpomnjenem referenčnem zapisu preverite eno uporabljeno in eno izločeno orientacijsko točko.

Oddajte tabele, opombo o virih in pravicah, zapis koordinatnega sistema in transformacije, dnevnik odločitev o kandidatih ter interpretacijo v približno 200 besedah. Navedite sklep, ki analizo občutljivosti prestane, in sklep, ki je ne. Če GIS ne morete uporabiti, tabele z izrecnimi pravili pripisa pomenijo celovito ne-grafično oddajo.

## Refleksija

- Katera navidezna selitev bi bila lahko sprememba meje ali razvrščanja?
- Kaj dejansko meri ocena zanesljivosti uporabljenega geokodirnika?
- Bi drug imenovalec, referenčna točka ali verjeten kandidat obrnil sklep?
- Katere lokacije naj ostanejo približne ali neobjavljene in kdo naj o tem odloča?

## Povzetek

Prostorski dokaz postane verodostojen z opredeljeno identifikacijo, ne z dovršenim izrisom. Imena, kraji, geometrije, pristojnosti in poti potrebujejo ločene zapise ter izrecne datume. Neodvisno preverjanje lahko razkrije zavajajoče dobro prileganje. Ohranjanje kandidatov, prostorsko združevanje z negotovostjo, utemeljeni imenovalci in zgodovinske prometne predpostavke omogočajo preverjanje argumenta. Tabela, ki pošteno ohrani dvoumnost, je lahko močnejši rezultat kot brezhiben zemljevid.

## Nadaljnje branje

- Bodenhamer, David J., John Corrigan in Trevor M. Harris, ur. 2010. [*The Spatial Humanities: GIS and the Future of Humanities Scholarship*](https://iupress.org/9780253222176/the-spatial-humanities/). Indiana University Press.
- Harley, J. B. 1989. [»Deconstructing the Map.«](https://doi.org/10.3138/E635-7827-1757-9T53) *Cartographica* 26(2): 1–20.
- Southall, Humphrey, Ruth Mostern in Merrick Lex Berman. 2011. [»On historical gazetteers.«](https://doi.org/10.3366/ijhac.2011.0028) *International Journal of Humanities and Arts Computing* 5(2): 127–145.
- Fotheringham, A. S., in D. W. S. Wong. 1991. [»The Modifiable Areal Unit Problem in Multivariate Statistical Analysis.«](https://doi.org/10.1068/a231025) *Environment and Planning A* 23(7): 1025–1044.
- QGIS Documentation. [Georeferencer, različica 3.40](https://docs.qgis.org/3.40/en/docs/user_manual/managing_data_source/georeferencer.html). Različici prilagojen operativni vir, ne trditev o najnovejši izdaji.
