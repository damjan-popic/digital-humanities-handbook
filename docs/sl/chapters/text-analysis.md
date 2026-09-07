---
title: "Analiza besedil"
description: "Kako frekvenca, porazdelitev, konkordanca, ključnost in kolokacije postanejo humanistično dokazno gradivo, ki upošteva vir."
tags: [frekvenca, dokumentna-frekvenca, razpršenost, konkordanca, ključnost, kolokacija, stilometrija]
status: draft
translation_status: machine-assisted draft; requires human language review
---

# Analiza besedil

!!! warning "Stanje prevoda"
    Slovensko besedilo je strojno podprti uredniški osnutek. Pred formalno
    objavo potrebuje vsebinski in jezikovni pregled strokovnjaka za slovenščino.

Časopis besedo *svoboda* večkrat uporabi v enem dolgem uvodniku, v desetih
drugih člankih pa je ni. Je svoboda značilna za zbirko ali za en dokument?
Odgovor se spremeni, če štejete pojavitve, dokumente ali razpršenost, ter znova,
ko v primerjavo vključite OCR, žanr in dolžino dokumentov.

## Učni cilji

Po tem poglavju boste znali:

- razlikovati frekvenco pojavnic, normalizirano frekvenco, dokumentno frekvenco
  in razpršenost;
- določiti enoto, imenovalec, poizvedbo in razdelitev korpusa za posamezno štetje;
- s konkordancami preveriti pomen, navedek, zanikanje in ponavljajoče se predloge;
- pojasniti, zakaj ključne besede zahtevajo primerljiv referenčni korpus;
- kolokacijo razlagati kot od parametrov odvisno povezanost in ne kot pomen;
- v količinskem rezultatu prepoznati učinke vira, OCR, anotacije in vzorčenja;
- ločiti raziskovalno iskanje vzorcev od njihove podkrepitve; in
- ohraniti dovolj dokazov za ponovitev in kritiko analize.

## Pred začetkom

Beseda se v korpusu A pojavi 300-krat, v korpusu B pa 180-krat. Zapišite, kaj
potrebujete, preden jo razglasite za značilnejšo za A. Potrebujete vsaj velikost
in število dokumentov, porazdelitev, žanre, datume, pravilo za dvojnike,
besedilne plasti in opredelitev štete oblike. Sami števili sta rezultata, ne
dokazno gradivo.

Če morate ločiti izmerjeni vzorec od interpretacije, se vrnite k poglavju
[Modeli, dokazno gradivo in interpretacija](models-evidence-interpretation.md).
Če štetje uporablja leme ali slovnične kategorije, preberite tudi
[Jezikoslovna anotacija in CLASSLA](linguistic-annotation-classla.md).

## Osrednji argument: vsako štetje vsebuje model korpusa

Analiza besedil ponavljajoče se značilnosti spremeni v strukturirane primerjave.
Štetje se zdi preprosto, vendar že vsebuje odločitve o viru, meji dokumenta,
prepisu, normalizaciji, tokenizaciji, poizvedbi in imenovalcu. Te odločitve
določijo, kaj lahko najdete.

Utemeljen rezultat zato poveže štiri dele:

1. **opis:** kaj vsebujejo korpus, poizvedba in izračun;
2. **dokazno gradivo:** števila, kontekste, porazdelitve in negotovost, pomembne
   za navedeno vprašanje;
3. **interpretacijo:** zgodovinsko in jezikoslovno utemeljeno razlago možnega
   pomena vzorca; in
4. **priporočilo ali odločitev:** naslednji korak vzorčenja, branja ali preverjanja.

Ne dovolite, da programska oprema dele združi v razvrščeni seznam, ki je videti,
kot da se razlaga sam.

## Poimenujte opazovano in analizno enoto

**Pojavnica** je ena pojavitev po tokenizaciji; **različnica** je različna
površinska oblika ali lema po prijavljenem pravilu enakovrednosti. **Poved** in
**odlomek** sta kontekstualni enoti, katerih meje so lahko uredniške ali modelske.
**Dokument** je bibliografska ali analizna enota in ni samodejno ena datoteka.
**Govorec** lahko prispeva več odlomkov, **korpus** pa je dokumentirana zbirka, iz
katere ste jih izbrali.

Opazovana enota je zapisani pojav, na primer pojavnica. Analizna enota je tisto,
o čemer govori trditev, denimo govor, govorec ali časopisna številka. Zamenjava
ustvari lažno natančnost: tisoči pojavnic enega govorca ne postanejo tisoči
neodvisnih govorcev. Pred izbiro statistične metode navedite obe enoti.

## Frekvenca odgovori »kolikokrat?«

**Frekvenca pojavnic** je število pojavitev določenega pojava. Lahko štejete
natančno obliko, obliko brez razlikovanja velikosti črk, lemo, besedno zvezo ali
anotirani vzorec. Povejte, kaj ste izbrali. Skupno štetje oblik `arhiv`, `Arhiv`
in pregibnih različic je operacionalizacija in ne nevtralna priročnost.

Absolutna števila so uporabna znotraj ene zbirke in za preverjanje podatkov, niso
pa neposredno primerljiva pri različnih velikostih korpusa. **Normalizirana
frekvenca** uporabi prijavljeni imenovalec, pogosto:

```text
normalizirana frekvenca = pojavitve izraza / vse upravičene pojavnice × 10.000
```

»Upravičene« je pomembna beseda. Ali štejete ločila, metapodatke, ponovljene
glave in neberljive odlomke OCR? Mera na 10.000 pojavnic primerja relativni
besedilni prostor, ne verjetnosti, da izraz uporabi dokument ali avtor. Če se
dolžine zelo razlikujejo, en dolg dokument prevlada v števcu in imenovalcu.

## Dokumentna frekvenca odgovori »kako široko?«

**Dokumentna frekvenca (DF)** šteje dokumente z vsaj eno pojavitvijo. Imenovalec
je število upravičenih dokumentov. Objavite število in delež:

```text
dokumentni delež = dokumenti z izrazom / upravičeni dokumenti
```

Frekvenca in DF razkrijeta različni obliki korpusa. Deset rab v enem uvodniku
daje frekvenco 10 in DF 1. Po ena raba v desetih člankih daje isto frekvenco in
DF 10. Prva lahko kaže močan krajevni argument, druga širše kroženje. Meje
dokumentov morajo biti pomenljive: delitev knjige na poglavja spremeni DF, ne pa
besedila.

Kadar so resnične vzorčne enote avtorji, številke ali dogodki in ne datoteke,
izračunajte tudi te enote. Obravnava vseh člankov istega plodovitega avtorja kot
neodvisnih lahko napihne doseg osebne navade.

**Razpon** je družina sorodnih mer za število delov korpusa, ki vsebujejo izraz.
DF je dokumentni razpon, kadar so deli dokumenti; trditvi morda bolje ustreza
razpon po avtorjih, številkah, žanrih ali obdobjih. Navedite delitev in imenovalec,
namesto da bi objavili neopredeljeni odstotek razpona.

## Razpršenost odgovori »kako enakomerno?«

DF loči navzočnost od odsotnosti, vendar ne opiše koncentracije med dokumenti,
kjer je izraz navzoč. **Razpršenost** opiše porazdelitev pojavitev po dokumentih
ali pomenljivih delih korpusa. Vedno navedite mero in razdelitev.

Učni paket uporablja Griesov DP, ker imajo štiri avtorske tematske skupine
neenaka števila upravičenih pojavnic: 83, 68, 66 in 113. Za skupno frekvenco
izraza \(F>0\), število izraza \(f_i\) v delu \(i\), velikost dela \(N_i\) in
velikost korpusa \(N\) primerjajte opažene in pričakovane deleže:

```text
opaženi_i = f_i / F
pričakovani_i = N_i / N
DP = 0.5 * sum_i(abs(opaženi_i - pričakovani_i))
```

DP je 0, kadar delež pojavitev izraza sledi deležem pojavnic v delih; višje
vrednosti pomenijo večji odklon in koncentracijo. Pri ničelni skupni frekvenci
ni določen. Pričakovani deleži upoštevajo neenako količino besedila, rezultat pa
je še vedno odvisen od izbrane razdelitve in ni prirojena splošnost besede.

Ob vrednosti DP objavite velikosti delov in števila izraza po delih. En indeks
prikrije vodilno skupino in vprašanje, ali razdelitev sploh ustreza
zgodovinskemu problemu.

## Konkordance povežejo vzorec z odlomkom

Konkordanca KWIC vsako pojavitev postavi v omejeni levi in desni kontekst. Med
oddaljenim in natančnim branjem zgradi most, ne da bi kratko okno predstavljala
kot celotno besedilo.

S konkordanco lahko:

- ločite homografe, imena in nepomembne pomene;
- pregledate zanikanje, poročani govor, navedke in ironijo;
- najdete ponovljene glave, oglase ali agencijska besedila;
- primerjate slovnične konstrukcije in bližnje vrednotenjsko izrazje;
- poiščete odlomke za poglobljeno branje; in
- pojasnite spremembo števila po popravi OCR ali lematizaciji.

Ohranite identifikator dokumenta in pojavitve, poizvedovano obliko, odmike ali
položaje pojavnic, velikost okna, pravilo razvrščanja in izvorno plast. Posnetek
zaslona ni ponovljiva konkordanca. Ko je razlaga odvisna od govorca, žanra ali
argumenta zunaj izseka, okno povečajte oziroma odprite dokument.

## Ključne besede potrebujejo referenčni korpus

**Ključna beseda** je v ciljnem korpusu nenavadno pogosta glede na referenčni
korpus. Ni zgolj pogosta ali zanimivo zveneča beseda. Rezultat določata oba
korpusa.

Referenca naj nadzoruje nameravano razliko. Pri primerjavi dveh strank v istih
volitvah uskladite obdobje, žanr, medij in pravila izbora. Primerjava govorov ene
stranke s splošnim spletnim korpusom pomeša učinke stranke, politike, govora,
obdobja in medija. »Nevtralne« reference ni; obstajajo primerne ali neprimerne
reference za določeno vprašanje.

Logaritemsko razmerje verjetij in sorodne statistike merijo moč dokaza proti
enaki relativni frekvenci pod določenimi predpostavkami. Mere učinka, na primer
logaritemsko razmerje frekvenc, opišejo velikost in smer. V zelo velikem korpusu
je lahko drobna razlika statistično močna. Objavite ciljno in referenčno število,
velikosti korpusov, pravilo glajenja ničel, statistiko, mero učinka, pravilo
večkratnega primerjanja in konkordance. Razvrščeni seznam je začetek razlage.

## Kolokacija meri povezanost, ne pomena

**Kolokat** se z iskano besedo pojavlja znotraj določenega okna ali slovničnega
razmerja pogosteje od pričakovanja po navedeni osnovi. Rezultat je odvisen od:

- obravnave iskane besede kot oblike, leme ali vzorca;
- širine in smeri okna ter meja povedi;
- tokenizacije in pravil za seznam nepolnopomenskih besed;
- najmanjše frekvence iskane besede, kolokata in para;
- mere povezanosti; in
- delitve korpusa ter metapodatkovnih filtrov.

Vzajemna informacija daje prednost razmeroma izključnim in včasih redkim parom.
Frekvenčne ali verjetnostne mere navadno poudarijo trdne pogoste vzorce. LogDice
daje omejeno mero, priročno za primerjavo parov, vendar še vedno podeduje
predobdelavo in vzorčenje. Nobena mera ne dokaže pomenskega razmerja,
vrednotenjskega stališča ali vzroka. Preberite konkordance in dokumente, kjer se
pari kopičijo.

## Primerljivost je pred izračunom

Pred primerjavo skupin preverite število in dolžino dokumentov, avtorje, žanre,
datume, mesta objave, dvojnike in agencijska besedila, manjkajoče gradivo,
kakovost OCR, jezikovno različico, kakovost anotacije in pravila izbora. Razlika
v založniški praksi se lahko pokaže kot navidezna leksikalna sprememba.

Združeni podatki lahko ustvarijo Simpsonov paradoks: splošni trend se znotraj
žanra, medija ali obdobja obrne. Pripravite dokumentne povzetke in razslojene
rezultate. Pojavnica ni neodvisni vzorec, kadar jih na tisoče prihaja iz enega
dokumenta. Uravnoteženost ni vedno zgodovinsko zaželena, mora pa biti neenakost
vidna in interpretirana, ne prikrito normalizirana.

Posebej preglejte OCR. Napake razpoznavanja lahko zmanjšajo navidezno frekvenco,
ustvarijo lažne redke besede, poškodujejo funkcijske besede in spremenijo velikost
korpusa. Če ima ena skupina slabši OCR, je lahko pristranska tudi normalizirana
mera. Poročajte o kakovosti po skupinah, preizkusite popravljeni vzorec ter
pomembne kandidate povežite s posnetki strani ali pregledanimi prepisi.

## Ohranite imenovalce in negotovost

Ne shranite le končnega grafa. Ponovno uporabna dokumentna tabela naj vsebuje
stabilni identifikator, navedbo vira, datum, avtorja oziroma stanje neznanega
avtorstva, žanr, jezik, identifikator besedilne plasti, pravice, število
upravičenih pojavnic, razpoložljivo mero kakovosti OCR ter odločitev o vključitvi
z razlogom. Tabela poizvedb naj vsebuje niz ali vzorec, pravilo za črke in leme,
različico skripte, čas ter kontrolno vsoto SHA-256 vhoda. Izpeljane vrstice naj ohranijo
identifikator dokumenta, da lahko vsako skupno mero razgrnete.

Negotovost se pojavi pred statističnim modeliranjem. Manjkajoča številka spremeni
imenovalec korpusa; negotovi datumi spremenijo časovne skupine; zaupanje OCR
morda ni umerjeno; dvoumna konkordanca spremeni števec. Te podatke zapišite kot
polja, razpone ali alternativne analize, namesto da bi vsako negotovost pretvorili
v gotovo vrednost. Pri majhnem korpusu so vsa dokumentna števila lahko
povednejša od zapletenega intervala z neverjetno predpostavko neodvisnosti.

Kadar vzorčenje dopušča sklepanje, naj metoda negotovosti spoštuje vzorčno enoto.
Vnovično vzorčenje pojavnic enega članka pretirano poveča količino informacij;
ustreznejši so morda dokumenti, avtorji ali številke. Navedite število neodvisnih
enot in predpostavke. Statistična značilnost ne popravi pristranskega izbora,
neenake ohranjenosti ali neprimernega referenčnega korpusa.

Pred razlago določite pravila za zaustavitev. Rezultat raziščite, če en dokument
prispeva več od določenega deleža, če se kakovost OCR med skupinama pomembno
razlikuje, če glavni kandidati izginejo ob verjetni predobdelavi ali če pregled
konkordanc zavrne veliko ujemanj. Rešitev je lahko popravljeni vzorec, analiza na
ravni dokumentov ali ožja trditev, ne dodatna okrasna statistika.

## Predobdelava je del argumenta

Neupoštevanje velikosti črk, normalizacija Unicode, odstranjevanje ločil,
filtriranje nepolnopomenskih besed, krnjenje in lematizacija spremenijo predmet
analize. Ohranite izvorno plast in zabeležite vrstni red pretvorb. V primerjavi
uporabite isto prijavljeno pravilo, razen če drugače zahteva raziskovalna zasnova.

Nepolnopomenske besede niso nujno nepomembne. Funkcijske besede lahko izražajo
slog, register in slovnično strukturo. Odstranjevanje lahko pomaga tematskemu
modelu, vendar uniči stilometrično vprašanje. Leme zmanjšajo redkost zaradi
pregibanja, a vnesejo anotacijsko napako in lahko zabrišejo zgodovinsko pomembne
oblike. Preizkusite občutljivost na verjetne alternative.

Besedni in znakovni **n-grami** predstavljajo krajevna zaporedja. Besedni bigrami
ohranijo obrazce, ki jih unigrami razdelijo; znakovni n-grami prenesejo del
pregibanja in podprejo primerjavo sloga, vendar lahko modelirajo tudi sistem OCR,
pravopis ali glave strani. Dokumentirajte dolžino, obravnavo mej, frekvenčni prag
in število značilk. Značilke vrnite v odlomke; napovedni delček sam ni pomenljiv
motiv.

Graf frekvenc ali zemljevid zmanjšanja razsežnosti je raziskovalen, dokler
vzorčenje in negotovost ne upravičita sklepanja. Osi, glajenje, širina razredov,
barva in izpuščeni dokumenti lahko spremenijo vizualno trditev. Objavite tabelo
za prikazom, pokažite dokumentno variabilnost in vzorec imenujte kandidat, dokler
ne prestane prijavljenega preverjanja.

## Slog in stilometrija

Stilometrija primerja dokumente z merljivimi značilkami, kot so frekvence
funkcijskih besed, znakovni n-grami, dolžina povedi ali slovnični vzorci. Podpre
vprašanja o avtorstvu, žanru, obdobju in prevodnem slogu, gruča pa sama ne
poimenuje vzroka.

Ločite zasnovo značilk, razdaljo ali model, vrednotenje in zgodovinsko
interpretacijo. Delov istega dela ne razporedite v učno in testno množico.
Analizo ponovite pri verjetnih velikostih odsekov, naborih značilk, pragih OCR in
metapodatkovnih nadzorih. Datum, urednik, žanr in kakovost razpoznavanja lahko
ustvarijo navidezni avtorski podpis.

## Od raziskovanja do podkrepitve

Raziskovanje je dragoceno za odkrivanje možnih vzorcev. Krožno postane, ko isti
podatki izberejo vzorec in parametre ter ga nato navidezno potrdijo. Kadar je
mogoče, raziskujte na enem delu, zapišite trditev in pravilo, nato pa preizkusite
zadržane dokumente ali drugo zbirko. Arhivirajte neuspešne poizvedbe in izbire
parametrov skupaj s privlačnim rezultatom.

Humanističnemu dokazovanju se ni treba pretvarjati, da je klinični preizkus. Mora
pa iskreno povedati, kdaj ste vzorec opazili, katere možnosti ste preizkusili in
katero neodvisno gradivo bi ga lahko ovrglo.

## Razdelan primer: frekvenca ni doseg

[Učni paket za preverjanje besedilnih analiz in NLP](../../assets/downloads/text-nlp-validation-v1.zip)
vsebuje dvanajst kratkih sintetičnih slovenskih dokumentov v štirih avtorskih
tematskih skupinah s po tremi dokumenti, vendar z neenakim številom pojavnic.
Korpus je namenjen učenju in ne govori o
resničnih arhivih, muzejih, jezikovni praksi ali časopisju.

Izraz *arhiv* se ponovi večkrat, vendar je zgoščen v majhnem številu dokumentov
arhivske skupine. *Korpus* se ponavlja v enem jezikovnem dokumentu. *Svoboda* je
izrazita v enem časopisnem dokumentu, drugje pa je ni. Primerjava frekvence, DF,
dokumentnega deleža, velikosti delov, števil po temah in Griesovega DP pokaže
različne oblike.
Konkordanca nato razkrije, ali pojavitve izražajo isto trditev ali si delijo le
obliko.

Rezultat podpira trditve o izdelanem učnem naboru: neki izraz se ponavlja
krajevno, drugi doseže več dokumentov, oba sta morda omejena na eno tematsko
skupino. Ne podpira trditve o slovenskem javnem diskurzu. Sintetična zasnova
razlike med merami prikaže pred uporabo na posledičnem zgodovinskem gradivu.

## Načini odpovedi in etične omejitve

Pogoste napake so primerjava absolutnih števil v neenakih korpusih, uporaba imen
datotek kot pomenljivih dokumentov, prezrtje prevladujočega besedila, zamenjava
ključnih besed s temami, razlaga kolokacije kot sentimenta, izločitev
nasprotujočih konkordanc in poročanje le o ugodnih parametrih.

Števila lahko škodljive kategorije predstavijo kot objektivne. Iskalne oznake
lahko ponovijo zgodovinske žaljivke; entitetno in demografsko sklepanje lahko
razkrije ljudi; korpus lahko nadzastopa ohranjene ustanove in vplivne govorce.
Navajajte le, kar zahteva argument, spoštujte pravice in zasebnost, ohranite
provenienco ter odsotnost opišite kot lastnost zbirke, ne kot molk preteklosti.

## Vaja

Izvedite postopek [Kako primerjam frekvenco, dokumentno frekvenco in razpršenost?](../workflows/text-analysis/compare-frequency-document-frequency-and-dispersion.md).
Izberite tri izraze z različnimi porazdelitvami. Za vsakega napišite opis mere,
eno z virom utemeljeno razlago in trditev, ki je paket ne dovoljuje. Pred
odločitvijo preberite vse konkordančne vrstice.

## Refleksija

- Je vaša enota pojavnica, poved, dokument, delo, avtor, številka ali dogodek?
- Bi vzorec lahko ustvaril en dokument ali podvojeni odlomek?
- Ali referenčni korpus osami nameravano razliko?
- Katera odločitev predobdelave najbolj spremeni seznam kandidatov?
- Kateri odlomek nasprotuje skupnemu vzorcu in zakaj je pomemben?

## Povzetek

Frekvenca meri količino, dokumentna frekvenca doseg, razpršenost pa porazdelitev
po prijavljenih delih. Normalizacija razkrije izbrani imenovalec, vendar ne
popravi neprimerljivega korpusa. Konkordance vrnejo števila v odlomke; ključne
besede so odvisne od primerne reference; kolokacije od oken in mer povezanosti.
Kritika vira, metapodatkovno razslojevanje, analiza občutljivosti in natančno
branje spremenijo izračune v utemeljeno dokazno gradivo.

## Nadaljnje branje

- Gries, Stefan Th. 2008. “Dispersions and Adjusted Frequencies in Corpora.”
  *International Journal of Corpus Linguistics* 13 (4): 403–437.
  [https://doi.org/10.1075/ijcl.13.4.02gri](https://doi.org/10.1075/ijcl.13.4.02gri).
- Gries, Stefan Th. 2022. “Toward More Careful Corpus Statistics: Uncertainty
  Estimates for Frequencies, Dispersion, Association, and Keyness.” *Research
  Methods in Applied Linguistics* 1 (1).
  [https://doi.org/10.1016/j.rmal.2021.100002](https://doi.org/10.1016/j.rmal.2021.100002).
- Dunning, Ted. 1993. “Accurate Methods for the Statistics of Surprise and
  Coincidence.” *Computational Linguistics* 19 (1): 61–74.
  [Bibliografski zapis ACL Anthology](https://aclanthology.org/J93-1003/).
