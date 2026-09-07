---
title: "Jezikoslovna anotacija in CLASSLA"
description: "Kako napovedane jezikoslovne plasti postanejo uporabno dokazno gradivo z namenskim preverjanjem, ki upošteva vir."
tags: [anotacija, CLASSLA, lema, oblikoslovje, odvisnostno-razčlenjevanje, NER, preverjanje]
status: draft
translation_status: machine-assisted draft; requires human language review
---

# Jezikoslovna anotacija in CLASSLA

!!! warning "Stanje prevoda"
    Slovensko besedilo je strojno podprti uredniški osnutek. Pred formalno
    objavo potrebuje vsebinski in jezikovni pregled strokovnjaka za slovenščino.

Zgodovinarko zanima, kdo je v časopisju dveh obdobij predstavljen kot govorec.
Iskanje glagolov je šele prva težava. OCR lahko zlepi besedi, zgodovinske oblike
so sodobnemu modelu morda neznane, lema je lahko napačna, odvisnostna analiza pa
govorca poveže z napačnim povedkom. Katera plast je dovolj zanesljiva za
raziskovalno trditev in kako bi to ugotovili?

## Učni cilji

Po tem poglavju boste znali:

- razlikovati segmentacijo povedi, tokenizacijo, lematizacijo, oznake UPOS,
  oblikoslovje, odvisnostno razčlenjevanje in razpoznavanje imenskih entitet;
- pojasniti, zakaj je vsaka anotacijska plast modelska trditev;
- izbrati le plasti, ki jih zahteva humanistično raziskovalno vprašanje;
- dokumentirati izvedbo CLASSLA z različico paketa, procesorji, viri, okoljem
  ter zgoščenimi vrednostmi vhodov in rezultatov;
- sestaviti ročno pregledan referenčni vzorec, ki ostaja odprt za kritiko;
- izračunati mere posameznih plasti z izrecnimi imenovalci; in
- povezati anotacijske napake z lastnostmi vira in interpretativnim tveganjem.

## Pred začetkom

Premislite o povedi *Zala je v Novi Gorici predstavila novo Zalo.* Je posamezna
pojavitev imena *Zala* oseba, izdelek, kraj ali kaj drugega? Bi uporabili veliko
začetnico, pregibanje, sobesedilo, katalog ali poznavanje dogodka? Nato si
zamislite, da OCR vrne *Novl Gorici*. Napaka imenske entitete se je začela že
pred zagonom razpoznavalnika entitet.

Zapišite trditev, ki jo želite oblikovati iz anotiranega besedila. Podčrtajte
natančna anotacijska polja, od katerih je odvisna. Če jih ne morete imenovati,
pred zagonom procesne verige znova preberite poglavje
[Modeli, dokazno gradivo in interpretacija](models-evidence-interpretation.md).

## Osrednji argument: anotacija je dokazna veriga

Jezikoslovna anotacija besedilne vzorce pripravi za poizvedovanje tako, da
besedilu doda izrecne analizne plasti. Ne odkriva lastnosti, ki bi v datoteki
čakale že povsem določene. Procesna veriga uporabi pravilo segmentacije,
anotacijsko shemo in naučene zakonitosti na določeni besedilni predstavitvi:

> izvorni predmet → prepis ali OCR → normalizirano besedilo → povedi in pojavnice
> → leksikalne in slovnične oznake → poizvedba → združevanje → interpretacija

Napaka ali uredniška odločitev na eni stopnji omeji vse poznejše. Zlepljena
oblika OCR lahko hkrati spremeni število pojavnic, lemo, besedno vrsto in
skladnjo. Normalizirano ime lahko izboljša razpoznavanje, vendar prikrije
zgodovinsko pomemben zapis. Visoka skupna mera lahko zakrije sistematično
odpoved prav v žanru ali družbeni skupini, ki jo primerjate. Preverjanje mora
zato slediti raziskovalni trditvi po celotni verigi in ne le potrditi, da je
program končal delo.

## Kaj trdijo posamezne plasti

### Povedi in pojavnice

Segmentacija povedi predlaga, kje se en krajevni kontekst konča in drugi začne.
Tokenizacija predlaga, kateri nizi štejejo kot besede, ločila ali večbesedne
enote. Odločitve določijo imenovalec večine poznejših mer. Zgodovinske krajšave,
začetnice, vezaji, opuščaji in zaradi OCR poškodovani presledki so pogosta mesta
napak. Če *naroda in* postane *narodain*, označevalnik vidi eno neznano besedo
namesto samostalnika in veznika.

Ohranite izvirno besedilo in stabilni identifikator dokumenta. Kadar je mogoče,
ohranite odmike znakov. CoNLL-U lahko ločeno predstavi površinsko večbesedno
pojavnico in njene sestavne besede, sploščena preglednica pa to povezavo pogosto
izgubi.

### Leme

Lema pregibne oblike združi pod slovarsko osnovno obliko. Omogoča sledenje
pojmom prek sklona, števila, osebe ali časa, vendar lahko zabriše razlike in
podeduje slovarske dogovore. Posebej občutljive so zgodovinske, narečne in
imenske oblike. Napačna lema pomembno pojavitev odstrani iz poizvedbe ali doda
enakozvočnico, ki tja ne spada.

Po lematizaciji ne zavrzite površinskih oblik. Poročajte, ali štejete oblike,
oblike z malimi črkami ali leme, ter preberite kontekste, na katerih temelji
argument.

### UPOS in oblikoslovje

Univerzalne oznake besednih vrst (UPOS) dajejo široke kategorije, kot so
`NOUN`, `VERB`, `ADJ` in `PRON`. Oblikoslovne lastnosti dodajo vrednosti za
sklon, spol, število, osebo, čas ali polarnost. Polje XPOS lahko ohrani oznako,
specifično za jezik. Gre za analize znotraj sheme, ne za univerzalne oznake, ki
bi jih vsi jezikoslovci pripisali enako.

Humanistična poizvedba mora navesti operacionalizacijo. »Akterjev« ne morete
preprosto izenačiti s samostalniki v imenovalniku: trpnik, elipsa in neživi
osebki bližnjico zapletejo. Tudi pri meri oblikoslovja povejte, ali je pojavnica
pravilna šele ob ujemanju celotnega svežnja lastnosti ali ocenjujete posamezne
lastnosti ločeno.

### Odvisnosti

Odvisnostna analiza vsaki skladenjski besedi pripiše glavo in razmerje, denimo
`nsubj`, `obj` ali `obl`. Tako lahko iščete konstrukcije namesto osamljenih
besed, na primer osebo, ki je kot osebek povezana s poročevalskim glagolom. Ena
napačna meja pojavnice premakne identifikatorje, napačen povedek pa spremeni več
lokov. Neoznačena pravilnost povezave vpraša, ali je pravilna glava; označena
pravilnost povezave zahteva pravilno glavo in razmerje.

Odvisnosti približajo skladenjsko branje. Same ne določijo zgodovinskega
delovanja, odgovornosti, izvora navedka ali vzročne moči. Te zahtevajo
kontekstualno interpretacijo.

### Imenske entitete

Razpoznavanje imenskih entitet (NER) predlaga razpone in kategorije, kot so
oseba, organizacija ali kraj. Ocenjujte natančne razpone kot razpone. Točnost
oznak na ravni pojavnic je lahko visoka že zato, ker večina pojavnic ni entitet.
Preciznost je število pravilno napovedanih razponov, deljeno z vsemi napovedanimi
razponi; priklic uporablja referenčne razpone; F1 je njuna harmonična sredina.

Razpoznavanje ni razreševanje entitet. Oznaka, da je *Ljubljana* kraj, je še ne
poveže s stabilnim normativnim zapisom. *J. Novak*, *Janez Novak* in *Novak*
lahko označujejo eno osebo ali več oseb. Ohranite različice imen, datume,
provenienco vira in stanje nerazrešenosti. Manjkajoča povezava je varnejša od
samozavestne napačne identitete.

## CLASSLA kot regionalna infrastruktura

CLASSLA ponuja procesne verige in vire za slovenščino ter druge južnoslovanske
jezike. Glede na jezik in razpoložljivost modelov lahko izvede tokenizacijo,
segmentacijo povedi, označevanje besednih vrst in oblikoslovja, lematizacijo,
odvisnostno razčlenjevanje ter NER. Regionalna dokumentacija in povezava s
CLARIN.SI olajšata iskanje in navajanje modelov ter označevalnih shem.
Institucionalni okvir obravnava poglavje
[Digitalna humanistika v Sloveniji](digital-humanities-in-slovenia.md).

Za ponovljivo navedbo ime CLASSLA ne zadostuje. Zamrznjena učna izvedba je 7.
septembra 2026 uporabila CLASSLA `2.2.1`, Python `3.12.3`, izvajanje na CPE ter procesorje
`tokenize,pos,lemma,depparse,ner`. Metapodatki navajajo operacijsko okolje,
različico Torch, ukaz, zgoščene vrednosti normaliziranih vhodov in rezultatov
ter SHA-256 in velikost vsake prenesene datoteke virov. Modelskih datotek ne
razširjamo. Pred razširjanjem ali produkcijsko rabo preverite licenco paketa in
vsakega vira posebej.

Tak opis ne pomeni, da je posamezno zamrznjeno izvedbo mogoče povsod natančno
ponoviti. Strojna oprema, paketi in viri se spreminjajo. Omogoča pa prepoznavo
izvedbe in razlikovanje namerne posodobitve od prikritega odklona.

## Izberite le plasti, ki jih zahteva vprašanje

Več procesorjev ne daje samodejno močnejšega dokaznega gradiva. Vsak doda čas,
prostor in novo možnost za napako.

| Raziskovalno opravilo | Verjetne najmanjše plasti | Dodatno preverjanje |
| --- | --- | --- |
| Štetje različic besede | pojavnice ali leme | konkordanca in porazdelitev po dokumentih |
| Primerjava sklonov | pojavnice, UPOS, oblikoslovje | pregled celotnega svežnja lastnosti |
| Iskanje govorcev poročevalskih glagolov | leme, UPOS, odvisnosti | pregled navedkov in glasu |
| Kartiranje imenovanih ustanov | pojavnice, NER | razreševanje entitet ter krajevna in časovna razločitev |

Začnite pri opazljivi lastnosti, ki jo zahteva trditev. Poimenujte anotacijo, ki
jo približa, in si zamislite najbolj škodljivo verjetno napako. Če jo
interpretacija prenese, plast morda zadostuje. Če je ne, okrepite vzorec,
popravljalni postopek ali omejite trditev.

## Ročna referenca ni razsodnik

Uporabni referenčni vzorec je ročno anotiran ali pregledan po izrecnih pravilih.
Še vedno je raziskovalni poseg. Zabeležite pregledovalca, datum, videno izvorno
plast, ravnanje z napakami OCR, uporabljeno shemo in mesta razumnega nestrinjanja.
Neodvisno dvojno anotiranje in razsojanje izboljšata zanesljivost; če ju ni,
to povejte.

Vzorčite pričakovano raznolikost in ne le lahkega sodobnega besedila. Vključite
obdobje, žanr, stanje dokumenta, imenske entitete ter pojave, pomembne za
vprašanje. Poškodbo vira ločite od napake modela. Če je ponudnikov OCR že izgubil
mejo med besedama, je ni povzročil jezikoslovni označevalnik, čeprav je njegov
odziv na poškodbo še vedno pomemben.

## Za vsako plast navedite imenovalec

Trditev »model je dosegel 92-odstotno točnost« je nepopolna. Enota in upravičeni
nabor se po plasteh spreminjata. Objavite števce za vsako mero:

| Plast | Primer mere | Imenovalec |
| --- | --- | --- |
| segmentacija povedi | natančno ujemanje povedi | referenčni vzorci ali povedi |
| tokenizacija | pravilno poravnane besedne pojavnice | referenčne besede, z ločeno navedenimi vstavki in izpusti |
| lema / UPOS | točnost natančne oznake | besede z enakovredno poravnavo |
| oblikoslovje | točnost celotnega svežnja | poravnane pojavnice, primerne za oblikoslovje |
| odvisnosti | UAS in LAS | poravnane skladenjske besede s poravnljivo glavo |
| NER | preciznost / priklic / F1 razpona | napovedani razponi / referenčni razponi |

Mer ne povprečite v eno prestižno številko. Popolna mera NER pri dveh entitetah
je skromen dokaz. Imenovalec odvisnosti, ki prikrito izloči neporavnane pojavnice
OCR, lahko rezultat olepša. Objavite števec, imenovalec, izločitve in dnevnik
napak.

## Ohranite rezultat, ki ga je mogoče pregledati

Pythonov predmet v pomnilniku še ni raziskovalni rezultat. Izvozite strukturirano
obliko, ki ohrani identifikatorje dokumenta, povedi in besede; površinsko obliko
in lemo; UPOS, jezikovno oznako in lastnosti; glavo in odvisnostno razmerje;
razpon entitete ter povezavo z izvorno plastjo. CoNLL-U dobro ohrani jezikoslovno
strukturo. Tabela pojavnic je priročna za analizo, vendar naj metapodatki
dokumentov ostanejo v povezani tabeli in naj se ne prepisujejo nedosledno v
vsako vrstico.

Normalizacijo dokumentirajte ločeno od vira. Če besedilo pretvorite v male črke,
poenotite zgodovinski zapis ali pred anotiranjem popravite OCR, ohranite
nespremenjeno plast in ponovljivo pretvorbo ali dnevnik odločitev. Rezultat ne
sme namigovati, da uredniško spremenjeni znaki izvirajo s strani. Enako velja za
izločene odlomke in neuspele dokumente: odsotnost iz končne tabele je izborna
odločitev.

Najmanjši zapis izvedbe vsebuje datum in čas, različice paketa in izvajalnega
okolja, vrstni red procesorjev z nastavitvami, identifikatorje ali zgoščene
vrednosti modelov in virov, uporabljeno napravo, identifikatorje in zgoščene
vrednosti vhodov, zgoščene vrednosti rezultatov ter ukaz ali različico skripte.
Kontrolna vsota dokazuje enakost bajtov, ne pravilnosti. Skupaj z referenčnimi
pravili in dnevnikom napak pa omogoči obnovo videnega gradiva in posegov.

Merilo za odločitev določite pred ogledom rezultata. Lahko zahtevate ročni
pregled vseh imenovanih entitet, zavrnete primerjavo obdobij ob pomembno
različnem priklicu ali anotacije uporabite samo za iskanje kandidatov za bližnje
branje. Če je imenovalec premajhen ali se nestrinjanje zgosti v ciljni kategoriji,
ustavite postopek, razširite preverjanje in omejite trditev. »Ni mogoče preveriti«
je uporaben metodološki izid in ne neuspešna programska predstavitev.

## Razdelan primer: sodobno, zgodovinsko in OCR

[Učni paket za preverjanje besedilnih analiz in NLP](../../assets/downloads/text-nlp-validation-v1.zip)
primerja štiri namensko izbrane slovenske povedi. Dve sta sodobna primera, ki ju
je napisal priročnik. Drugi dve sta usklajeni besedilni predstavitvi istega
časopisnega odlomka iz leta 1925 v paketu o arhivskem trenju: ročno preverjeni
referenčni prepis in dokumentirani ponudnikov OCR. Nista neodvisni zgodovinski
opazovanji.

Sodobna poved, ki se začne *Kustosinja Maja Kovač*, dobi verjetne leme, skladnjo
in natančne razpone za osebo, muzej ter Ljubljano. Uspeh je dokaz le za izbrane
primere. V zgodovinskem referenčnem prepisu posamostaljeni *vse* omogoči zapisano
nestrinjanje med modelsko prislovno analizo in pregledovalčevo analizo zaimka ter
osebka. V ponudnikovem OCR sta *naroda in* zlepljena v *narodain*, *stanovske*
postane *stavovske*, *kulturnega* postane *kultrunega*, oziralni *ki* pa *i*.
Zadnjo obliko model analizira kot samostalnik, zato preusmeri tudi odvisnostno
strukturo.

Primerjava loči tri opise:

1. **stanje vira:** kaj vsebuje stran, prepis ali ponudnikov OCR;
2. **vedenje anotacije:** kaj zamrznjena procesna veriga napove za vhod;
3. **interpretativna posledica:** katera poizvedba, število ali pripis se spremeni.

Tak opis je uporabnejši od splošne trditve, da je OCR »slab«. Zlepljeni veznik
ogrozi štetje in skladnjo; poškodovani oziralnik ogrozi pripis stavka ali govorca;
pravilno ohranjena entiteta je morda robustna le v tej povedi. Taksonomija napak
rezultata ne opravičuje, ampak pokaže točko potrebnega posega.

## Načini odpovedi in odgovorne omejitve

Pogoste napake so obdelava PDF namesto dokumentirane besedilne plasti,
normaliziranje pomenljivega zgodovinskega zapisa, izguba identifikatorjev pri
izvozu, sploščitev večbesednih pojavnic, preverjanje samo na lahkem sodobnem
besedilu, objava skupne mere brez imenovalca in prikaz negotovega razreševanja
entitet kot gotovega.

Anotacija lahko okrepi reprezentacijsko neenakost. Imena, jezikovne različice in
žanri, ki so v učnih virih slabo zastopani, lahko odpovedujejo sistematično.
Poizvedba o ženskah, manjšinskojezičnih avtorjih ali regionalnih ustanovah je
zato lahko pristranska tudi ob visoki skupni meri. Napake preglejte po skupinah,
ki jih raziskava primerja, zaščitite občutljive osebne podatke ter iz slovničnih
ali entitetnih oznak ne sklepajte o identiteti ali duševnem stanju.

## Vaja

Izvedite postopek [Kako CLASSLA ovrednotim na domensko specifičnem vzorcu?](../workflows/nlp/evaluate-classla-on-a-domain-specific-sample.md).
Ponovno izračunajte eno mero iz števca in imenovalca, dve zapisani napaki
povežite z izvornima plastema in zapišite trditev, ki jo dokazno gradivo podpira.
Nato oblikujte močnejšo trditev, ki je ne podpira, ter navedite manjkajoče
preverjanje.

## Refleksija

- Katera plast ima v vašem projektu največje interpretativno tveganje?
- Ali vzorec vključuje obdobja, žanre in družbene skupine iz vaše primerjave?
- Katere napake so nastale v OCR ali prepisu in ne v anotaciji?
- Kaj bi drug usposobljen pregledovalec lahko utemeljeno anotiral drugače?
- Katere procesorje lahko izpustite, ne da bi oslabili argument?

## Povzetek

Jezikoslovna anotacija je dokazna veriga napovedanih in od sheme odvisnih plasti.
CLASSLA je pomembna regionalna infrastruktura, toda ime paketa ali splošna mera
ne more preveriti humanistične trditve. Ohranite plasti vira, zaženite le potrebne
procesorje, natančno identificirajte programsko opremo in vire, pripravite
dokumentirano ročno referenco, poročajte o imenovalcih posameznih plasti ter
vsako pomembno napako povežite z interpretacijo, ki jo lahko spremeni.

## Nadaljnje branje

- Ljubešić, Nikola, in Taja Kuzman. 2024. *CLASSLA-Stanza: The Next Step for
  Linguistic Processing of South Slavic Languages*. [Arhivirana izdaja in
  bibliografski zapis](https://doi.org/10.5281/zenodo.13936406).
- [Izvorni repozitorij CLASSLA z navodili za uporabo](https://github.com/clarinsi/classla).
- Universal Dependencies. [Oblika CoNLL-U](https://universaldependencies.org/format.html)
  in [univerzalna odvisnostna razmerja](https://universaldependencies.org/u/dep/).
- Za razlikovanje izvorne slike, rezultata razpoznavanja, popravljenega besedila
  in nadaljnje uporabe znova preberite [OCR, HTR in šumno besedilo](ocr-htr-noisy-text.md).
