---
title: "UI, etika in ponovljivost"
description: "Kako analizo s pomočjo UI spremenite v preverljiv argument s kritiko virov, vrednotenjem, presojo pravic in ohranjenimi raziskovalnimi zapisi."
tags: [UI, etika, ponovljivost, provenienca, pravice]
status: draft
translation_status: machine-assisted draft; requires human language review
---

# UI, etika in ponovljivost

Kadar časopis trdi, da govori v imenu celotnega naroda, s čim bi dokazali, da
gre za več kot politično retoriko? Tekoče napisan povzetek lahko časopisno
trditev neopazno spremeni v raziskovalno ugotovitev. Težava se začne še pred
izmišljenim navedkom: nastane, ko izgine razmerje med virom in argumentom.
Odgovorna uporaba umetne inteligence (UI) omogoča presojo tega razmerja,
vključno z odločitvami, da rezultat popravimo, omejimo ali ga ne uporabimo.

!!! note "Uredniško stanje"
    Poglavje in učne simulacije so strojno podprti osnutki. Čakajo
    na strokovni pregled in kompetenten človeški pregled slovenščine. Spodnji
    primeri so avtorsko pripravljene učne simulacije, ne poročila o izvedenih
    zagonih generativnega modela ali dokaz opravljenega človeškega preverjanja.

## Učni cilji

Po tem poglavju boste znali:

- povezati računalniške rezultate s trditvami, ki jih lahko podprejo;
- razlikovati med tehnično ponovljivostjo, računalniško reproducibilnostjo,
  robustnostjo, preverljivostjo dokazov in interpretativno odgovornostjo;
- ohraniti sled od vira do trditve tudi brez možnosti enakega ponovnega zagona;
- zasnovati stratificirano preverjanje, primerjavo z izhodiščno metodo in
  pravilo za opustitev napovedi;
- presojo zasebnosti, pravic, vključevanja in porabe virov prenesti v postopek;
- dokumentirati pomoč, popravke, nestrinjanje pregledovalcev in odprta vprašanja.

## Pred začetkom

Preberite arhivski odstavek ter določite govorca, občinstvo in najmočnejšo
trditev. Ločite med tem, kar odstavek zatrjuje, in tem, kar bi lahko neodvisno
potrdili. Bi prevod to razliko ohranil? Potrebujete osnove kritike virov,
identifikatorje dokumentov in razlikovanje, razvito v poglavju
[Modeli, dokazno gradivo in interpretacija](models-evidence-interpretation.md).
Računa za storitev UI ne potrebujete. Vajo lahko opravite z ohranjenim paketom
in avtorsko pripravljenimi izhodi. Uporaba zunanje storitve je izbirna in
zahteva ustrezno institucionalno ureditev obdelave podatkov.

## Najprej določite rezultat, nato presodite trditev

UI označuje raznovrstne sisteme, ne ene metode. **Napovedni oziroma
klasifikacijski model** na podlagi naučenih povezav pripiše oznako ali oceno:
odstavek lahko denimo označi glede na politično stališče. To omogoča trditev o
uspešnosti glede na določen kodirni priročnik na preverjenem gradivu, ne
neposrednega vpogleda v avtorjevo prepričanje. **Generativni jezikovni modeli**
tvorijo besedilo na podlagi navodil in konteksta. Uporaben osnutek ostaja
predlog predstavitve; slovnična pravilnost in verjetni navedki ne dokazujejo
zgodovinske resničnosti.

**Vektorske vložitve** predstavijo enote z vektorji. **Priklic informacij**
izbere možne odlomke s poizvedbo in postopkom razvrščanja. Pomenska bližina
lahko pomaga najti drugače ubesedeno gradivo, vendar niti bližina niti mesto
med zadetki ne dokazujeta soglasja, pravilnega pripisa ali popolne pokritosti.
Pri generiranju s priklicanimi viri zato preverjate dvoje: ali je iskanje
priskrbelo pomembne dokaze in ali jih je model ustrezno uporabil. Samozavesten
odgovor ne odpravi izpusta pri iskanju. Pridobivanje virov za raziskovalno
zbirko je širša odločitev o gradivu in dostopu, ne zgolj ta računski korak.

**OCR, prepoznavanje rokopisov (HTR) in verjetnostno obogatitev** uporabljamo za
predloge prepisov, entitet ali jezikovnih struktur. Rezultat ločite od
dokumenta, ki ga opisuje. **Sistem na osnovi pravil** pa lahko uporablja slovar
ali regularni izraz brez kakršnega koli učenja; tržna oznaka UI njegovega
delovanja ne spremeni. Pregledno pravilo je lahko dobra izhodiščna metoda,
čeprav spregleda ironijo, zgodovinski zapis ali kontekst. Preverjanje posameznih
ravni obravnavata poglavji [Jezikoslovna anotacija in CLASSLA](linguistic-annotation-classla.md)
in [Teme, sentiment in čustva](topics-emotions-classification.md).

Ločiti morate tudi načine uporabe. **Lokalna** namestitev omogoča nadzor nad
izvedljivimi različicami, če ohranite odvisnosti in uteži modela. **Gostovani**
vmesnik del nadzora prepusti ponudniku. **API** je programski vmesnik, ne
jamstvo za zasebnost ali stabilnost; dostopa lahko do lokalne ali oddaljene
storitve. Opišite dejansko ureditev. Ime storitve ne določa nujno modela,
skritih navodil, usmerjanja zahtev, politike hrambe ali možnosti izvoza
raziskovalnih zapisov.

## Pet različnih zagotovil

V tem priročniku **tehnična ponovljivost** pomeni ponovno izvedbo istega
postopka v določenih pogojih. Bajtno enakost zahtevamo le, kadar jo izrecno
določimo. **Računalniška reproducibilnost** pomeni, da lahko drug raziskovalec
iz ohranjenih podatkov, kode in okolja rekonstruira izračun ter dobi vnaprej
opredeljen enakovreden rezultat. Poročilo ameriških nacionalnih akademij iz
leta 2019 razlikuje reproducibilnost z istimi raziskovalnimi vhodi od
replikacije z novimi podatki. Ker se izrazje med disciplinami razlikuje,
pojasnite namen preizkusa in ne predpostavljajte skupnega pomena izraza.[^ai-nas]

**Robustnost** preverja, ali sklep vzdrži utemeljene spremembe pozivov, modelov,
nastavitev ali vzorcev. **Preverljivost dokazov**, ki jo podpira **sledljivost**,
bralcu omogoča pot od pomembnega izhoda do podanih virov in pretvorb.
**Interpretativna odgovornost** zahteva razlago, zakaj dokazi podpirajo neko
branje, ohranjanje nasprotnih dokazov in možnost utemeljenega nestrinjanja.
Interpretativna reproducibilnost zato ne zahteva nujno enake razlage: drug
raziskovalec mora imeti možnost rekonstruirati in presoditi pot do sklepa.
Ponovljivosti in angleškega izraza *reproducibility* torej ne enačimo samodejno.

| Predlagano zagotovilo | Kaj ohranite ali preizkusite | Česa s tem ne dokažete |
| --- | --- | --- |
| Natančna ponovitev | Enaki vhodi in konfiguracija; določena bajtna primerjava | Da je ponovljeni odgovor pravilen |
| Računalniška reproducibilnost | Podatki, izvedljiva koda, odvisnosti, datoteke modela ali dostopen posnetek, pričakovani rezultat in toleranca | Veljavnosti zunaj teh vhodov |
| Robustnost | Omejene spremembe, vsi poskusi, razlike in merilo sprejemljivosti | Neodvisnosti modelov ali splošne zanesljivosti |
| Sledljivost in preverljivost | Izhod, identifikatorji odlomkov, različice virov, pretvorbe in popravki | Prepričljivosti vsake interpretacije |
| Interpretativna odgovornost | Argument, druge razlage, nestrinjanje pregledovalcev in končna odgovornost | Obveznega soglasja ali mehanske interpretacije |

Ohranjen odgovor gostovanega sistema je lahko preverljiv tudi po umiku modela.
Zgolj ohranjen poziv pa ne upravičuje trditve o računalniški reproducibilnosti.
Nasprotno lahko povsem ponovljiv izpis vztrajno ohranja napako OCR. Navedite,
katero zagotovilo ste preizkusili in katero ni dosegljivo. Naključno seme je
zapis enega vhoda, ne dokaz nadzora nad vsemi viri nedeterminističnosti,
lastniškimi sestavinami ali operacijami, odvisnimi od strojne opreme.

## Ohranite zapis raziskovalnega dogodka

Zabeležite ponudnika, identifikator modela, različico ali datirani posnetek,
če obstaja, dejanski datum in čas UTC ter vmesnik oziroma API. Ohranite
sistemska in uporabniška navodila, kadar je razkritje dovoljeno, primere,
zgodovino pogovora, parametre generiranja in konfiguracijo priklica informacij.
Pri priklicu potrebujete poizvedbo, različico indeksa, model vektorskih
vložitev, delitev na odseke, filtre, razvrščanje in izbrane odlomke v podanem
vrstnem redu. Vire opremite s stalnimi identifikatorji odlomkov, kontrolnimi
vsotami in pogoji dostopa. Opišite predobdelavo, normalizacijo, prevajanje in
krajšanje. Če vmesnik kontekst skrajša brez razvidnega zapisa, obseg označite
kot neznan.

Prvotni izhod hranite ločeno od dnevnika popravkov in popravljenega predloga.
Dodajte protokol in dejanski vzorec preverjanja, odločitve pregledovalcev,
kodo, okolje paketov, pomembne podatke o strojni opremi, čas izvajanja in
denarni strošek. Neznano lastniško podrobnost označite z `unknown`, zakriti
podatek z `redacted` ter razlogom in potjo do dovoljenega dostopa, neizvedeno
dejanje pa z `not_run`. Nobena od teh oznak ne pomeni številčne ničle. V
javni zapis ne vključujte poverilnic. Ohranite dovoljeni izvoz konfiguracije:
sami zaslonski posnetki lahko izpustijo nastavitve in otežijo dostopno ponovno
uporabo.

Predlogo najdete v [postopku dokumentiranja in preverjanja analize](../workflows/ai/document-and-audit-a-source-grounded-ai-analysis.md).
Zmožnosti storitve, pogoje uporabe in cene preverite ter datirajte za dejansko
izbranega ponudnika. Poglavje ne daje trenutnih jamstev za posamezne storitve;
datum preverjanja virov je 7. september 2026. Raziskovalni paket povežite z
označeno različico objave, kot pojasnjuje [Živi odprti priročnik](open-living-handbook.md),
omejeno dostopne dokaze pa ohranite v okviru dovoljenega dostopa.

## Razdelan primer: od narodnega soglasja do pripisane trditve

Raziskovalno vprašanje se glasi: kako *Ilustrirani Slovenec* oblikuje predstavo
politične enotnosti? Uporabite [paket arhivskega trenja](../../assets/downloads/archival-friction-v1.zip)
in [paket besedilnega in jezikoslovnega preverjanja](../../assets/downloads/text-nlp-validation-v1.zip).
Zgodovinski predmet je *Ilustrirani Slovenec*, 7. februar 1925, letnik 1,
številka 7, z identifikatorjem dLib `URN:NBN:SI:doc-YPI8OFSU`.[^ai-archive]
Natančno mesto je prva stran PDF, uvodni odstavek pod naslovom,
`AF-OCR-P1-INTRO`, poved z začetkom `Tudi danes`. V jezikoslovnem paketu
`raw/annotation-samples.csv` ta izbor ohranja kot `TNLP-AF-REF` in
`TNLP-AF-OCR`, s kontrolnimi vsotami in izvorom izluščenega besedila.
Referenčni prepis, ponudnikov OCR in jezikoslovne oznake, pripravljene s
pomočjo UI, so različne ravni.

Začnite s čistim kontrolnim primerom: `source/contemporary-sample.csv`, zapis
`TNLP-C02`, prva poved. Raziskovalci v tem avtorskem sintetičnem besedilu
preverjajo prepise in pojasnjujejo negotovost. Sprejemljiv opis navede ti dve
dejanji, ne da bi izumil projekt ali rezultat. Primer pokaže želeno nalogo
na izrecni ubeseditvi, ne uspešnosti na zgodovinskih arhivih. Kontrolnega in
zgodovinskega odlomka nikoli ne združujte kot neodvisni zgodovinski opazovanji.

Nato preverite **avtorsko simulacijo napačnega angleškega povzetka UI**:
“The article documents unanimous Slovenian support for the Slovene People's
Party. A national survey confirms that differences of worldview no longer
matter.” Povzetek zatrjuje soglasno podporo Slovenski ljudski stranki in se
sklicuje na anketo med prebivalstvom. Zapis ne izhaja iz dokumentiranega
preizkusa modela, temveč je učna simulacija, pripravljena s pomočjo UI.
Njegov tekoči slog omogoča vajo o napačnem pripisu, izmišljeni dokazni podlagi
in izbrisani negotovosti brez pošiljanja virov v zunanjo storitev. Dodatni
**simulirani zapis navedka** iz OCR prepiše `stavovske` in `narodain` ter ju
označi kot »navedek, preverjen ob posnetku«. Oznaka je namerno napačna;
A03 preverja ta dodatni avtorski zapis, ne besed v angleškem povzetku.

| Zapis | Simulirana napaka | Preverjanje vira | Popravek in posledica |
| --- | --- | --- | --- |
| A01 | Narodno soglasje je predstavljeno kot ugotovljeno dejstvo | `TNLP-AF-REF`; odstavek zatrjuje enotnost, ne ponuja pa neodvisnih podatkov o prebivalstvu | Trditev pripišite časopisu; opustite sklep o izmerjeni javni podpori |
| A02 | Anketa med prebivalstvom je izmišljena | `AF-OCR-P1-INTRO`, celotni odstavek; anketa ni navedena | Trditev odstranite in označite z `unsupported_claim`; ne ugibajte manjkajočega bibliografskega vira |
| A03 | Besedilo OCR nastopa kot zanesljiv navedek | Primerjajte `TNLP-AF-OCR`, `TNLP-AF-REF` in prvo stran PDF; OCR vsebuje `stavovske` in `narodain` | Navedite preverjeni prepis; napako OCR in popravek ohranite ločeno |
| A04 | Angleški povzetek izbriše pripis političnega glasu | Ponovno preberite slovenski odlomek in omembo stranke; prevod primerjajte z izvirnikom | Angleško besedilo označite kot parafrazo in ohranite mesto v slovenskem viru |

Popravljena učna interpretacija je ožja: uvodni odstavek podporo stranki
predstavlja kot služenje skupni narodni svobodi in tej trditvi podredi razlike
v nazorih. Je dokaz retorike publikacije, ne anketa med Slovenci. Za presojo
sprejema bi potrebovali druge dokaze. Predlagani navedek preverite ob posnetku;
angleškega prevoda ne morete znakovno primerjati s slovenskim izvirnikom in
pričakovati enakosti. Neodvisni bralec naj pregleda celotni odstavek in presodi
to razlago. Tak človeški pregled je predlagan, ne predstavljen kot opravljen.

## Preverjajte odločitve, ne videza usposobljenosti

Izhod razdelite na preverljive trditve in poleg izrečenega preglejte izpuste.
Znakovna primerjava potrdi pojavitev navedka v viru, ne pa pravilnega govorca,
datuma, obsega ali konteksta. Navedeno mesto poiščite v ohranjenem dokumentu,
nato preučite okoliško besedilo in moč sklepa. Uporabljajte natančne kategorije:
izmišljena trditev, napačen pripis, spremenjen navedek, napačno mesto v viru,
izpuščena omejitev, izpust pri priklicu in nepodprt prevod. »Halucinacija« tu
pomeni generirano vsebino, ki je v ustreznem dokaznem kontekstu izmišljena ali
nepodprta; natančnejša kategorija je navadno uporabnejša. NIST-ov profil
tveganj generativne UI takšno konfabulacijo obravnava poleg drugih tveganj
sistema.[^ai-nist]

Vzorec določite pred prilagajanjem pozivov. Naključni vzorec običajnega gradiva
dopolnite z namenskimi skupinami za zgodovinski pravopis, poškodovan OCR,
navajanje, ironijo, jezik in žanr. Zapišite identifikatorje ter imenovalec
vsakega deleža: nič pregledanih primerov pomeni nedoločen delež, ne popolne
točnosti. Večji delež težavnih odlomkov pomaga odkrivati slabosti, brez
ustreznega uteževanja pa ne ocenjuje napak celotne zbirke. Poročajte o majhnih
številih in negotovosti ter o pomembnih primerih, ki jih vzorec ne zajema.

Kadar je izvedljivo, naj dva bralca izbrane trditve neodvisno presodita po
kratkem kodirnem priročniku. Pred pogovorom ohranite začetne odločitve,
utemeljitve in mesta v virih. Usklajevanje naj zabeleži sprejeto rešitev in
preostalo nestrinjanje; večinsko soglasje dvoumnosti ne spremeni v gotovost.
Referenčne oznake so raziskovalne presoje z določenim stanjem pregleda, ne
nevtralna resnica. Pri učni vaji lahko pregledate vsak izhod, večji projekt
pa potrebuje izrecen načrt vzorčenja in predaje težavnih primerov v presojo.

Pri klasifikatorjih **umerjenost** primerja napovedano gotovost z dejansko
pravilnostjo na ustreznem gradivu, ki ni bilo uporabljeno za učenje. Ocena 0,9
sama po sebi ne pomeni 90-odstotne verjetnosti pravilnosti. Guo in sodelavci pokažejo, da je gotovost
nevronskih modelov lahko slabo umerjena.[^ai-calibration] Postopek umerjanja in
prag za opustitev napovedi določite na validacijskih podatkih ter ju preverite
na nedotaknjeni testni množici. Poročajte o napaki in pokritosti: če sistem
polovico primerov zavrne, se spremeni obseg tega, kar opisuje. Zavrnitve
preglejte po skupinah, da opuščanje napovedi ne bi sistematično izločalo
manjšinskega jezika. Samozavestna ubeseditev generativnega odgovora ni takšna
izmerjena verjetnost.

Rezultat primerjajte z izhodiščno metodo: ročnim izpisom iz vira, iskanjem
ključnih besed ali majhnim naborom pravil na isti nalogi in enotah. Upoštevajte
čas pregleda in spregledane dokaze. Testnih dokumentov ne vključujte v učenje
ali primere v pozivu; skoraj enake časopisne strani lahko povzročijo uhajanje
med navidezno ločenimi množicami. Neznani lastniški učni podatki omejujejo
trditev o preizkusu brez kontaminacije. Uspeh na sodobni angleščini ne dokazuje
uspešnosti na zgodovinski slovenščini. Presodite izboljšanje konkretnega
raziskovalnega opravila v navedenih pogojih.

## Robustnost preverjajte z utemeljenim obsegom dela

Naenkrat spreminjajte le en dejavnik: ubeseditev poziva, primere, vrstni red
odlomkov, globino priklica, dolžino konteksta ali model. Ponovite enake pogoje,
da opazujete razlike med zagoni, ter ohranite tudi neuspehe in zavrnitve.
Liu in sodelavci so pri preučevanih nalogah z dolgim kontekstom ugotovili vpliv
položaja informacij. To utemeljuje preizkus vrstnega reda, ne splošne trditve
o vsakem današnjem modelu.[^ai-context]
[Postopek preverjanja robustnosti](../workflows/ai/compare-ai-output-across-prompts-models-and-runs.md)
ločuje slogovne razlike od sprememb pripisa, dokazov, negotovosti in izpustov,
ki vplivajo na sklep.

Omejeno adversarialno preverjanje oziroma *red-teaming* namerno preizkuša
verjetne okoliščine odpovedi: zavajajoč naslov, nasprotujoča si odlomka ali
navodilo, vstavljeno v dokument. Izvorno besedilo obravnavajte kot dokaz,
nikoli kot pooblastilo za spremembo raziskovalnega postopka. Uporabite
dovoljene neobčutljive primere in pravilo ustavitve. Vaja preverja določeno
ranljivost, ne tekmovanja v premagovanju klepetalnika. Tudi soglasje modelov
ni neodvisna potrditev: modeli si lahko delijo podatke in vzorce napak.

## Etične odločitve naj spremenijo postopek

Zasebno pismo lahko razkrije žive sorodnike; po odstranitvi imena lahko osebo
še vedno določa kombinacija dogodkov. Pred pošiljanjem drugam določite,
kateri osebni ali občutljivi podatki prečkajo mejo, kdo dostopa do njih,
kako potekata hramba in izbris, ali se uporabljajo za učenje in kakšne so
pogodbene omejitve. Zmanjšajte poslani odlomek ali uporabite nadzorovano
lokalno obdelavo. Nejasno pravno podlago ali ureditev obdelave naj pred
prenosom razrešijo pristojni za naročanje in varstvo podatkov v ustanovi.
Smernice EDPB pojasnjujejo omejitev namena, najmanjši obseg podatkov in
varovanje občutljivih podatkov; javna dostopnost teh obveznosti ne razreši.[^ai-privacy]

Pravice presojajte ločeno za vire, oznake, modele, programsko opremo in izhode.
Dovoljenje za branje vira še ne dovoljuje razširjanja ali pošiljanja tretji
osebi. Preverite licence, pogoje storitve, institucionalne pogodbe in zahteve
za navedbo ter zapišite različico in datum dostopa. Generirani izhod lahko
ponovi varovano izrazno obliko, zato ponudnikovo dovoljenje za uporabo izhoda
ne razreši vseh pravic v njem. Ob negotovosti objavite identifikatorje in
postopek rekonstrukcije namesto nedovoljeno razširjenih kopij ter vprašanje
zabeležite za strokovno pravno presojo.

Kulturna avtoriteta presega soglasje posameznika. Imetnik zbirke morda ne
zastopa skupnosti, katere znanje zbirka vsebuje. Načela CARE za upravljanje
podatkov staroselskih ljudstev poudarjajo skupno korist, pristojnost za
odločanje, odgovornost in etiko.[^ai-care] Njihovega specifičnega staroselskega
okvira ne posplošujte v splošen kontrolni seznam. Določite, kdo odloča
o dovoljenih rabah, pregleduje opise in lahko zahteva omejitev, ter zagotovite
sredstva za sodelovanje. Kolonialne ali strankarske kategorije ne prenesite
v nevtralno oznako klasifikatorja brez razlage izvora in posledic.

Jezikovna in področna neenakost se pokažeta v napakah po skupinah, izpustih
priklica ter obsegu popravljanja. Ne prevajajte vsega v angleščino zgolj zato,
ker neki sistem tam deluje bolje: ohranite izvirnik in preverite pomenske
spremembe. Pristranskost v prid avtomatiziranemu odgovoru zmanjšujte tako,
da pregledovalci najprej preberejo vire. Ohranjajte vaje iz kritike virov,
da pomoč ne nadomesti veščine, potrebne za prepoznavanje napake. Priznajte
delo označevanja, prepisovanja, prevajanja in moderiranja; opišite znane
delovne okoliščine, ne da bi izmišljali trditve o nevidnih delavcih.

Podporne rabe lahko širijo dostop z bralno pomočjo, prepisovanjem ali osnutki
opisov. Rezultate preverite s predvidenimi uporabniki: skrajšano besedilo lahko
izpusti negotovost, tekoč opis slike pa si izmisli podrobnost. Zagotovite
dostopno možnost, povezano z virom, in pot za popravke. Sodelovanje naj ne
zahteva plačljivega računa ali razkritja oviranosti ponudniku.

Finančna in okoljska sorazmernost sodita v izbiro metode. Luccioni, Jernite
in Strubell merijo energijo za sklepanje pri različnih nalogah in modelih
ter pokažejo pomen izbire načina uporabe.[^ai-energy] Določite obseg zagonov,
shranite rezultate, kadar je to dovoljeno, in primerjajte preprostejše metode.
Zapišite število žetonov ali čas izračuna ter dostopne meritve energije z
mejami merjenja. Neznana poraba ponudnika ni ničelna, ocena ogljičnega odtisa
ene poizvedbe pa ni univerzalna. Pri presoji koristnosti upoštevajte tudi
strošek strokovnega preverjanja.

## Vaja

Za odlomka iz paketov pripravite register virov in preverite štiri simulirane
napake. Dodajte en izpust, ki bi spremenil zgodovinski argument. Napišite
popravljeno interpretacijo v 80 besedah ter ohranite obe različici. Druga
oseba naj pred primerjavo odločitev uporabi vaš kodirni priročnik; če ni na
voljo, človeški pregled označite kot čakajoč. Izpolnite zapis preverjanja in
zasnujte omejeno vajo robustnosti brez poročanja o neizvedenih zagonih.
Oddajte tabelo trditev, identifikatorje vzorca, zapis nestrinjanja, zgornjo
mejo stroška in razlog za opustitev napovedi. Merilo ocenjevanja so dokazi
in odločitve, ne dostop do dragega modela.

## Refleksija

Katere dele bi drug raziskovalec lahko ponovno izvedel, katere samo pregledal
in katerim utemeljeno ugovarjal? Kdo nosi posledice izpuščene omejitve? Bi
objava celotnega dnevnika razkrila informacije, ki jih mora raziskava varovati?
Pojasnite primer, pri katerem metodološka omejitev zahteva ožjo trditev,
ne boljšega poziva.

## Povzetek

Pomoč UI postane del znanstvenega dela z ohranjenimi dokazi, izrecnimi
preizkusi in odgovorno interpretacijo. Razkrijte, kaj je pomoč obsegala, kaj
so ljudje preverili in kaj ostaja odprto; samo razkritje uporabe UI postopka
ne upraviči. ALLEA odgovornost za raziskovalno integriteto pripisuje
raziskovalcem in ustanovam.[^ai-integrity] Uporabna izjava navede nalogo, zapis
modela, obravnavano gradivo, preverjanje in odgovorne sodelujoče. Ohranite
jo z določeno različico objave, da popravki argument spremenijo vidno in
ne s tihim nadomeščanjem njegove dokazne zgodovine.

## Nadaljnje branje

- National Academies of Sciences, Engineering, and Medicine. 2019.
  *Reproducibility and Replicability in Science*.
  [Poročilo in DOI](https://doi.org/10.17226/25303). Za izrecne opredelitve.
- Autio, Chloe, idr. 2024. *Artificial Intelligence Risk Management Framework:
  Generative Artificial Intelligence Profile*. NIST AI 600-1.
  [Poročilo](https://doi.org/10.6028/NIST.AI.600-1). Za omejene preizkuse tveganj.
- Guo, Chuan, Geoff Pleiss, Yu Sun in Kilian Q. Weinberger. 2017.
  »On Calibration of Modern Neural Networks.« *PMLR* 70: 1321–1330.
  [Članek](https://proceedings.mlr.press/v70/guo17a.html).
- Liu, Nelson F., idr. 2024. »Lost in the Middle: How Language Models Use
  Long Contexts.« *Transactions of the Association for Computational Linguistics*
  12: 157–173. [Članek](https://aclanthology.org/2024.tacl-1.9/).
- Carroll, Stephanie Russo, idr. 2020. »The CARE Principles for Indigenous
  Data Governance.« *Data Science Journal* 19: 43.
  [Članek](https://datascience.codata.org/en/articles/dsj-2020-043).
- Luccioni, Sasha, Yacine Jernite in Emma Strubell. 2024. »Power Hungry
  Processing: Watts Driving the Cost of AI Deployment?« *FAccT '24*: 85–99.
  [DOI](https://doi.org/10.1145/3630106.3658542).
- ALLEA. 2023. *The European Code of Conduct for Research Integrity*,
  prenovljena izdaja. [Kodeks in prevodi](https://allea.org/code-of-conduct/).

[^ai-nas]: [Poročilo nacionalnih akademij](https://doi.org/10.17226/25303), 2019. Petdelna razmejitev je učni dogovor, ne splošno veljavna terminologija.
[^ai-archive]: [Bibliografski zapis dLib](https://www.dlib.si/details/URN:NBN:SI:doc-YPI8OFSU), preverjen 7. septembra 2026. Pred ponovno uporabo preberite politiki pravic in prepisovanja v paketu.
[^ai-nist]: [NIST AI 600-1](https://doi.org/10.6028/NIST.AI.600-1), 2024. Kategorije napak to vprašanje prilagodijo humanističnemu delu z viri.
[^ai-calibration]: [Guo idr.](https://proceedings.mlr.press/v70/guo17a.html), 2017.
[^ai-context]: [Liu idr.](https://aclanthology.org/2024.tacl-1.9/), 2024.
[^ai-privacy]: European Data Protection Board, [Data protection basics](https://www.edpb.europa.eu/sme/learn-the-basics/data-protection-basics_en), dostop 7. septembra 2026. Uporabljivost pravil in institucionalna ureditev zahtevata presojo konkretnega primera.
[^ai-care]: [Carroll idr.](https://datascience.codata.org/en/articles/dsj-2020-043), 2020; [Global Indigenous Data Alliance](https://www.gida-global.org/careprinciples), dostop 7. septembra 2026.
[^ai-energy]: [Luccioni, Jernite in Strubell](https://doi.org/10.1145/3630106.3658542), 2024; [avtorski rokopis](https://arxiv.org/abs/2311.16863).
[^ai-integrity]: [Kodeks ALLEA](https://allea.org/code-of-conduct/), prenovljena izdaja 2023. Vsi povezani viri so bili preverjeni 7. septembra 2026; to je datum dostopa, ne datum človeškega pregleda.
