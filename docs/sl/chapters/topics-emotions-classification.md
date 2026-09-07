---
title: "Teme, sentiment in čustva"
description: "Kako raziskovalne teme, gruče, nadzorovane oznake in kontekstualne trditve o čustvih ohranite metodološko ločene."
tags: [klasifikacija, gručenje, tematsko-modeliranje, sentiment, stališče, čustva, stabilnost, preverjanje]
status: draft
translation_status: machine-assisted draft; requires human language review
---

# Teme, sentiment in čustva

!!! warning "Stanje prevoda"
    Slovensko besedilo je strojno podprti uredniški osnutek. Pred formalno
    objavo potrebuje vsebinski in jezikovni pregled strokovnjaka za slovenščino.

Časopisna poved pravi: »Čudovito – še ena zamuda.« Leksikon najde pozitivno
besedo, klasifikator polarnosti morda napove negativni sentiment, tematski model
jo lahko postavi ob muzejsko upravo, človeški bralec pa čustvo govorca pusti
nerazrešeno. Rezultati odgovarjajo na različna vprašanja. Kateri lahko podpre
zgodovinsko trditev, ki jo želite oblikovati?

## Učni cilji

Po tem poglavju boste znali:

- razlikovati tematsko modeliranje, gručenje in nadzorovano klasifikacijo;
- primerjati vrečo besed s kontekstualnimi predstavitvami;
- pojasniti vpliv segmentacije dokumentov, števila tem, inicializacije in
  naključnega semena na raziskovalno tematsko rešitev;
- povezati teme med izvedbami ter ohraniti nestabilne in nepovezane sestavine;
- zasnovati učno, validacijsko in testno množico brez uhajanja vira;
- neuravnoteženo klasifikacijo primerjati s preprostimi izhodišči in umerjenostjo;
- ločiti leksikalno asociacijo, sentiment, stališče, afekt, izraženo in pripisano
  čustvo ter odziv bralca; in
- prepoznati časovne, domenske, večjezične, OCR- in prevodne omejitve.

## Pred začetkom

Za poved *Sijajno – spet čudovita zamuda* naštejte vse trditve, ki jih besedilo
podpira brez poznavanja avtorja. Besedi imata pozitivno leksikalno asociacijo.
Izjava verjetno z ironijo izvaja negativno vrednotenje. Cilj je zamuda. Nosilec
določenega čustva lahko ostane neznan. Odziv bralca ni zapisan v povedi. Tako
ločevanje je začetek kodirnega priročnika.

Klasifikacija pojem operacionalizira, ne pa odkrije samoumevne kategorije.
Poglavje [Modeli, dokazno gradivo in interpretacija](models-evidence-interpretation.md)
pomaga ločiti kodirni priročnik, vhodno predstavitev, rezultat, dokazno gradivo
preverjanja in trditev.

## Tri družine modelov, tri vrste rezultatov

### Tematsko modeliranje

Tematski modeli predstavijo ponavljajoče se vzorce sopojavljanja. Klasični
verjetnostni modeli dokument opišejo kot mešanico porazdelitev besed;
nenegativna matrična faktorizacija (NMF) nenegativno matriko dokumentov in
izrazov razstavi na dokumentne uteži in izrazne sestavine. Raziskovalci lahko
sestavino po pregledu izrazov ter dokumentov interpretirajo kot temo. Sestavina
ni samostojno obstoječi predmet in nima sama po sebi zanesljivega imena.

### Gručenje

Gručenje opazovanja razporedi po podobnosti v izbrani predstavitvi in razdalji.
Gruča navadno opazovanje umesti v eno skupino, tematski model pa dokumentu lahko
pripiše uteži več sestavin. Meje, oblika gruč in pomen razdalje so odvisni od
metode. Če gručo imenujete tema, s tem še ne dokažete skupnega zgodovinskega
vzroka njenih članov.

### Nadzorovana klasifikacija

Klasifikator se nauči napovedovati kategorije, ki so že opredeljene v označenih
podatkih: žanr, relevantnost, sentiment, stališče, čustvo ali drugo raziskovalno
oznako. Kakovost omejujeta skladnost in pokritost kodirnega priročnika ter
anotacij. Nadzorovane oznake imajo za razliko od raziskovalnih tem prijavljeno
tarčo, a so še vedno izdelane raziskovalne spremenljivke in ne naravne vrste.

## Enote in predstavitve spremenijo vprašanje

Model ne more predstaviti konteksta, ki ga segmentacija odstrani. Celotne knjige
poudarijo široko besedišče, poglavja ali odlomki krajevne premike, povedi pa
olajšajo kontekstualno klasifikacijo, vendar lahko izgubijo govorca in argument.
Drseča okna podvajajo kontekst in niso neodvisna. Skozi vse segmente ohranite
identifikator izvornega dokumenta, da ostaneta vidna uhajanje in združevanje.

**Vreča besed** beleži oblike, leme ali n-grame in večinoma prezre vrstni red. Je
redka in pregledna: najvišje uteži lahko povežete z natančnimi izrazi. Težko
obravnava oddaljeni kontekst, večpomenskost, zanikanje in ironijo.
**Kontekstualna predstavitev** besedo ali odlomek preslika z naučenim modelom,
ki upošteva okolico. Lahko zajame več razlik, vendar podeduje nepregledne učne
podatke, različico modela, tokenizacijo, jezikovno pokritost ter izbiro poziva ali
združevanja. Večja zapletenost ne odpravi potrebe po branju virov.

Pri slovenščini in kodnem preklapljanju preverite natančno jezikovno različico.
Večjezični model lahko zmogljivost med jeziki porazdeli neenako, slovenski model
pa lahko napačno obravnava nemške, italijanske, hrvaške ali narečne odlomke.
Prevajanje ni nevtralna predobdelava. Spremeni besedišče, ritem, entitete,
sentimentne namige in morebitno tematsko strukturo, zato je prevod nova modelska
plast z lastno provenienco.

## Tematske rešitve so pogojne

Rezultati so odvisni od segmentacije dokumentov, besedišča, normalizacije,
seznama nepolnopomenskih besed, spodnje in zgornje dokumentne frekvence,
uteževanja, števila sestavin, družine modela, inicializacije, naključnega semena,
konvergenčnih nastavitev, sestave korpusa ter dvojnikov. Napake OCR lahko postanejo
redki izrazi z visoko utežjo; lematizacija zmanjša razpršenost pregibnih oblik, a
vnese anotacijske napake.

**Število tem** nadzoruje zrnatost. Premalo sestavin združi različne vzorce,
preveč jih lahko en vzorec razcepi, osami dokument ali modelira šum. Navadno ni
ene skrite pravilne vrednosti. Primerjajte več števil, ki ustrezajo verjetnim
ravnem raziskovanja, in poročajte o razcepih, spojih ter izginotjih.

Naključna inicializacija išče po prostoru z več krajevnimi optimumi. Nastavljeno
**naključno seme** ponovi eno izvedbo, ne zagotovi njene stabilnosti. Izvedite več
semen pri istih nastavitvah. Nato spremenite število tem ali segmentacijo, da
preverite drug vir občutljivosti.

## Pred primerjavo teme povežite

Številka teme je med izvedbami poljubna: tema 1 pri semenu 7 ni nujno tema 1 pri
semenu 19. Določite pravilo povezovanja. Pregledno učno pravilo lahko primerja
množice najpomembnejših izrazov z Jaccardovim prekrivanjem:

```text
J(A, B) = |A ∩ B| / |A ∪ B|
```

Teme povežite ena proti ena tako, da maksimizirate skupno prekrivanje, in navedite
način prirejanja ter pravilo za izenačenje. V večji raziskavi sta morda boljša
ujemanje dokumentnih uteži ali distribucijska razdalja. Ne glede na pravilo
ohranite slabo ujemajoče se in nepovezane teme. So dokaz nestabilnosti.

Ne iščete univerzalnega praga. Preverite, ali isti izrazi in dokumenti podpirajo
primerljivo branje. Številsko koherentno temo lahko sestavljajo obrazec, poškodbe
OCR ali en plodovit vir. Zgodovinsko pomenljiv vzorec lahko uporablja raznoliko
besedišče in doseže skromno mero. Številska koherentnost in interpretativna
veljavnost sta različni presoji.

## Človeška interpretacija je del metode

Za vsako objavljeno sestavino preberite več dokumentov z visoko utežjo, enega s
srednjo, enega z nizko ali nasprotujočo utežjo ter dokumente iz pomembnih
metapodatkovnih skupin. Zapišite začasno oznako, dokazne odlomke, izločitve,
negotovost in alternativne oznake. Oznaka naj bo ožja od vzorca. »Besedišče
arhivskega opisovanja v tem sintetičnem naboru« je varnejše kot »tema arhiva v
slovenski kulturi«.

Tematska razširjenost je modelska utež, ne delež resnične pozornosti. Po
metapodatkih jo združujte šele po pregledu dolžine dokumentov, vzorčenja,
negotovosti in odvisnosti virov. Sprememba ohranjenosti ali OCR se lahko kaže
kot tematska sprememba.

## Nadzorovano vrednotenje zahteva ločitev

Začnite s kodirnim priročnikom, ki določi enoto, vključitve, izključitve, mešane
in negotove primere, namen ter posledice lažno pozitivnih in negativnih napovedi.
Kjer je mogoče, ga preizkusite z več označevalci. Ujemanje označevalcev je dokaz
o priročniku in nalogi; nestrinjanje lahko razkrije resnično interpretativno
zapletenost. Ob razsojanju ohranite tudi prvotne odločitve.

Ločite **učno**, **validacijsko** in **testno** vlogo. Učna množica prilagodi
parametre, validacijska izbere značilke, prag ali poziv, zadržani test pa oceni
vedenje po teh odločitvah. Delite po dokumentu, avtorju, številki ali viru, kadar
bi segmenti lahko uhajali. Skoraj enaki odlomki v učni in testni množici
ustvarijo privlačne, a brezvredne ocene.

Primerjajte preprosta izhodišča: večinski razred, razslojeno naključno napoved,
pregledno leksikonsko pravilo ali model samo z metapodatki. Pri neuravnoteženih
razredih objavite matriko zamenjav ter preciznost, priklic in F1 po razredih.
Makro povprečje razrede uteži enako, mikro povprečje pa primere. Povejte, na katero
vprašanje odgovarja izbrano povprečje.

Kadar rezultat uporabljate kot verjetnost ali za prednostni pregled, preverite
**umerjenost**: ali je med primeri z verjetnostjo 0,8 oznaka na ustreznih
zadržanih podatkih pravilna približno v 80 % primerov? Razvrščanje je lahko
uporabno kljub slabi umerjenosti, vrednosti pa brez dokaza ne imenujte zaupanje.

Časovni in domenski premik omejujeta vsako vrednotenje. Klasifikator sodobnih
ocen izdelkov se nauči polarnosti, ki se ne prenese na zgodovinska pisma. Spremenijo
se lahko stranka, žanr, platforma, sistem OCR ali anotacijski dogovor. Poročajte
po skupinah, pomembnih za vprašanje, in po bistvenem premiku znova preverite.

## Sentiment, stališče, afekt in čustvo niso sopomenke

**Sentiment** navadno pomeni pozitivno, negativno ali nevtralno vrednotenje
določenega cilja. **Stališče** zadeva podporo, nasprotovanje ali umeščanje do
trditve ali akterja. **Afekt** se lahko širše nanaša na izraženo ali vzbujeno
valenco in intenzivnost. **Čustvo** lahko uporablja ločene kategorije, kot so
veselje, strah, jeza in žalost, ali razsežnosti, kot sta valenca in vzburjenost.
Pojme opredelite in jih ne uporabljajte izmenično.

Raziskava čustev zahteva dodatne vloge:

- **leksikalna asociacija:** oblika je v leksikonu povezana s kategorijo;
- **izraženo čustvo:** besedilo predstavi čustvo kot trenutno izraženo;
- **pripisano čustvo:** pripovedovalec ali govorec čustvo pripiše drugemu;
- **nosilec ali izkuševalec:** predstavljeni nosilec čustva;
- **cilj ali dražljaj:** oseba, predmet, dogodek ali trditev, h kateri je čustvo
  usmerjeno oziroma ki ga vzbudi;
- **navedeni govor:** vstavljeni glas, ki ga ne smete samodejno pripisati
  poročevalcu ali avtorju;
- **stališče pripovedovalca:** vrednotenjska umestitev pripovedovalca, ki se lahko
  razlikuje od čustev oseb; in
- **odziv bralca:** empirična ali teoretična trditev o bralcih in ne oznaka, ki
  bi bila neposredno zapisana v besedah.

Zanikanje lahko razveljavi žalost: »ni bila žalostna«. Modalnost oslabi zavezo:
»morda se je bala« ni enako kot »bala se je«. Ironija lahko obrne vrednotenje,
ne da bi določila čustvo: »Kako čudovito« po novi napaki. Metajezikovna omemba
prav tako ne zadostuje: »jeza v zapisu ni nujno jeza avtorja«. Leksikonsko
ujemanje dokazuje le leksikalno asociacijo.

## Pregledno leksikonsko izhodišče

Leksikon je uporaben, ker lahko pregledate vsako ujemanje. Zabeležite jezik,
različico, vir, način izdelave, kategorije, enoto, pravilo ujemanja, licenco in
pogoje razširjanja. Tujega leksikona ne kopirajte v učni paket zgolj zato, ker ga
lahko prenesete. Pri slovenščini sta pomembna pregibanje in lematizacija,
prevedene kategorije pa zahtevajo jezikovni in kulturni pregled.

Izhodišče mora ohraniti primere brez ujemanj ter lažno pozitivne in negativne
napovedi. Popravljanje leksikona po branju primerov za vrednotenje je razvoj
modela; spremembo preizkusite drugje. Primerjava natančnih oblik z lemami ali
dodajanje enega dokumentiranega vnosa razkrije pridobitev in izgubo.

## Ponavljajoča se omejena primerjava

[Učni paket za preverjanje besedilnih analiz in NLP](../../assets/downloads/text-nlp-validation-v1.zip)
omogoča namenoma majhno primerjavo. Vzorec čustev ima osem sintetičnih povedi in
izvirni učni mikroleksikon z osmimi vnosi. Tematski vzorec ima dvanajst
sintetičnih dokumentov. Nobeden ne ocenjuje zgodovinske populacije.

| Metoda | Enota in vhod | Rezultat in preverjanje | Podprta trditev | Nepodprta trditev | Pridobitev, izguba in odpoved |
| --- | --- | --- | --- | --- | --- |
| natančni leksikon oblik | poved; površinske oblike | kategorijska ujemanja proti osmim pregledanim primerom | katere prijavljene oblike se ujemajo | kdo resnično čuti čustvo | pregledno; prezre pregibanje in kontekst |
| ročna anotacija čustev | poved, sobesedilo in priročnik | čustvo, nosilec, cilj, glas, zanikanje, ironija, negotovost; en pregledovalec | kako je bil priročnik uporabljen | objektivna psihologija ali razširjenost v korpusu | kontekstualno; sporno in delovno zahtevno |
| nadzorovani klasifikator | zahteval bi označene učne, validacijske in testne enote | namenoma ni prilagojen: osem primerov ne zadostuje | nobena za ta paket | napovedna kakovost | opustitev prepreči okrasni model z uhajanjem |
| raziskovalni NMF | dokument; vreča besed TF-IDF | 2, 3 in 4 sestavine × semena 7, 19 in 31; povezani izrazi in prebrani odlomki | občutljivost sintetične predstavitve | splošna tematska struktura | pokaže razcepe in nestabilnost; majhno in od besedišča odvisno |

Čustveni primeri vključujejo navedek *obiskovalci se bojijo*, zanikano žalost,
metajezikovno *jezo*, pripisani strah, ironično *čudovita* in preteklo obliko
*bali*, ki nima natančnega ujemanja. Tako dobite vidne lažno pozitivne in lažno
negativno napoved. Ročna anotacija določi nosilca in cilj, ironijo pa lahko pusti
nerazrešeno, namesto da bi si izmislila čustvo.

Prikaz NMF ohrani vektorizacijo in spreminja seme ter število sestavin. Nekatere
sestavine ohranijo sorodne izraze in dokumente, druge besedišče arhivov, muzejev,
jezika in časopisja združijo drugače. To je lekcija o občutljivosti, ne dokaz, da
je model »odkril« avtorske teme.

## Načini odpovedi in etične omejitve

Pogoste napake so poimenovanje tem samo iz ključnih izrazov, izbira števila tem
zaradi urejenega grafa, zavrženje nestabilnih izvedb, delitev povedi istega vira
med učno in testno množico, poročanje o točnosti neuravnotežene naloge, razlaga
modelske verjetnosti kot umerjenega zaupanja in prevajanje brez zapisa posega.

Oznake čustev in stališč lahko patologizirajo ljudi, sklepajo o varovanih
lastnostih ali napačno predstavijo navedene govorce. Zgodovinsko besedišče lahko
vsebuje nasilje in stigmo. Zmanjšajte osebne podatke, ohranite glas in kontekst
vira, dokumentirajte negotovost, preverite napake po skupinah ter ne trdite ničesar
o notranjih stanjih, česar besedilo ne podpira. Ločeno preverite pravice korpusa,
leksikona in modela.

## Vaja

Izvedite oba postopka:

1. [Kako preverim stabilnost in interpretabilnost tematskega modela?](../workflows/text-analysis/test-topic-model-stability-and-interpretability.md)
2. [Kako analiziram čustva z leksikonom in ročnim preverjanjem?](../workflows/text-analysis/analyse-emotion-with-a-lexicon-and-manual-check.md)

Za vsakega napišite eno podprto in nepodprto trditev. Določite spremembo vira,
predstavitve ali kodirnega priročnika, ki bi podprto trditev najbolj ogrozila.

## Refleksija

- Urejate leksikalne vzorce, napovedujete oznako priročnika ali sklepate o človeku?
- Kateri dokumenti ali govorci bi lahko uhajali med evalvacijske množice?
- Katero nestabilno temo je bilo najlaže poimenovati in kaj ji je nasprotovalo?
- Komu pripada čustvo v navedku: navedenemu govorcu, pripovedovalcu, avtorju ali
  nikomur brez dodatnih dokazov?
- Kateri časovni, domenski ali jezikovni premik zahteva novo preverjanje?

## Povzetek

Tematsko modeliranje, gručenje in nadzorovana klasifikacija ustvarjajo različne
predstavitve in zahtevajo različna preverjanja. Število tem, seme, inicializacija,
segmentacija in pravilo povezovanja spremenijo stabilnost v empirično vprašanje.
Nadzorovane oznake zahtevajo ločene podatke, izhodišča, razredno občutljive mere
in preizkuse premika. Pri čustvih morate ločiti besedo, vrednotenje, glas,
nosilca, cilj in odziv bralca. Primeri, povezani z virom, ohranjena negotovost in
človeško branje omejijo rezultat na utemeljene trditve.

## Nadaljnje branje

- Su, Jinyu, David Greene, in Derek O’Callaghan. 2016. “Topic Stability over
  Noisy Sources.” [ACL Anthology](https://aclanthology.org/W16-3913/).
- Morstatter, Fred, in Huan Liu. 2018. “In Search of Coherence and Consensus:
  Measuring the Interpretability of Statistical Topics.” *Journal of Machine
  Learning Research* 18 (169): 1–32.
  [Članek JMLR](https://jmlr.org/papers/v18/17-069.html).
- Bostan, Laura Ana Maria, Evgeny Kim, in Roman Klinger. 2020. “GoodNewsEveryone:
  A Corpus of News Headlines Annotated with Emotions, Semantic Roles, and Reader
  Perception.” [ACL Anthology](https://aclanthology.org/2020.peoples-1.12/).
- Reschke, Kevin, in Pranav Anand. 2011. “Extracting Contextual Evaluativity.”
  [ACL Anthology](https://aclanthology.org/W11-1511/).
