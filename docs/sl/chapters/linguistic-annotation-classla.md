---
title: "Jezikoslovna anotacija in CLASSLA"
description: "Kako samodejna jezikoslovna anotacija besedilo razdeli na analizne plasti – in zakaj moramo vsako plast še vedno preveriti."
tags: [anotacija, CLASSLA, lema, besedna-vrsta, NER]
status: draft
---

# Jezikoslovna anotacija in CLASSLA

## Učni cilji

Po tem poglavju boste znali:

- razlikovati med tokenizacijo, lematizacijo, označevanjem besednih vrst, morfološko analizo, odvisnostnim razčlenjevanjem in razpoznavanjem imenskih entitet;
- pojasniti, zakaj je jezikoslovna anotacija modelska interpretacija in ne nevtralno dejstvo;
- izbrati anotacijske plasti, ki ustrezajo humanističnemu raziskovalnemu vprašanju;
- izvesti in dokumentirati osnovni postopek s CLASSLA za slovenščino ali drug podprt južnoslovanski jezik;
- samodejni rezultat preveriti na namenskem vzorcu in z analizo napak.

## Pred začetkom

Vzemite poved *Zala je v Novi Gorici predstavila novo Zalo.* Je *Zala* oseba, izdelek, kraj ali kaj drugega? Katere dokaze bi uporabil človek? Označevalnik mora sorodne odločitve sprejeti iz oblike, konteksta in vzorcev, naučenih iz podatkov.

## Anotacija ustvari analizne plasti

Neobdelano besedilo sestavljajo znaki in presledki. Večina računalniških metod najprej ustvari izrecnejše enote:

- **pojavnice** razdelijo tekoče besedilo na besede, ločila ali druge enote;
- **povedi** določijo meje lokalnega konteksta;
- **leme** združijo pregibne oblike pod slovarsko osnovno obliko;
- **oznake besednih vrst in morfološke oznake** opišejo slovnično kategorijo in lastnosti;
- **odvisnostna razmerja** predstavijo skladenjske povezave med besedami;
- **imenske entitete** označijo odseke, kot so osebe, organizacije, kraji ali datumi.

Te plasti omogočajo vprašanja, na katera zgolj površinske oblike ne odgovorijo. Leme podpirajo primerjave kljub pregibanju. Morfološke oznake omogočijo raziskovanje sklona, števila ali časa. Entitete lahko besedila povežejo s podatkovnimi zbirkami in zemljevidi. Odvisnostna razmerja lahko približno pokažejo, kdo deluje na koga.

## Vsaka anotacija je trditev

Samodejno anotacijo ustvarijo pravila ali statistični modeli, naučeni na že označenih primerih. Rezultat zato odraža:

- anotacijsko shemo v učnih podatkih;
- žanre, obdobja in jezikovne različice, zastopane v njih;
- odločitve o tokenizaciji in normalizaciji;
- arhitekturo modela in različico programske opreme;
- dvoumnosti, ki jih razpoložljivi kontekst ne razreši.

Oznaka ni odkrita lastnost v istem smislu kot številka strani. Je napoved znotraj določene predstavitve. Razlika je posebej pomembna, ko raziskovalna trditev temelji na majhni kategoriji, nenavadnem jeziku, zgodovinskem zapisu, narečju, poeziji ali imenih, ki jih v učnih podatkih ni.

## CLASSLA v južnoslovanskem prostoru

CLASSLA ponuja jezikoslovne procesne verige in vire za slovenščino ter več drugih južnoslovanskih jezikov. Običajna veriga lahko besedilo tokenizira, razdeli na povedi, pripiše leme in oblikoskladenjske oznake, razčleni odvisnosti ter razpozna imenske entitete, odvisno od jezika in razpoložljivih modelov.

Prednost ni samo priročnost. Dokumentirana regionalna infrastruktura olajša navajanje modelov, primerjanje jezikov in razumevanje označevalnih shem. Metodološka obveznost ostane: zabeležimo jezik, različico modela ali paketa, uporabljene procesorje, pripravo vhodnih podatkov in datum obdelave.

CLASSLA je tudi središče znanja za dokumentacijo, svetovanje, izobraževanje in objavo virov. Njeno institucionalno vlogo in razmerje s CLARIN.SI pojasnjuje poglavje [Digitalna humanistika v Sloveniji](digital-humanities-in-slovenia.md).

## Izberite samo plasti, ki jih potrebujete

Več anotacije ni samodejno bolje. Vsaka plast prinaša računanje, shranjevanje in možne napake.

Za raziskavo leksikalnih sprememb so morda dovolj pojavnice, leme in metapodatki. Raziskava slovničnih konstrukcij lahko potrebuje morfologijo in odvisnosti. Zemljevid ustanov zahteva imenske entitete in razreševanje identitet. Zagon vseh procesorjev zgolj zato, ker obstajajo, upočasni postopek in oteži presojo, ne da bi nujno izboljšal argument.

Začnite pri raziskovalni spremenljivki. Vprašajte se, katero opazljivo značilnost potrebujete, katera anotacija jo približa in kako bi napake v tej plasti spremenile rezultat.

## Od rezultata do urejene tabele

Uporabna anotacijska tabela ima navadno eno vrstico na pojavnico in polja, kot so:

| document_id | sentence_id | token_id | form | lemma | upos | feats | head | deprel |
|---|---:|---:|---|---|---|---|---:|---|
| d001 | 1 | 1 | Raziskovalke | raziskovalka | NOUN | Case=Nom\|Gender=Fem\|Number=Plur | 2 | nsubj |

Metapodatke dokumentov hranite v ločeni tabeli, povezani z `document_id`. Ohranite izvirno besedilo in, kadar je mogoče, odmike znakov, ki anotacijo povežejo z njim. Izvoz zgolj v sploščeno preglednico lahko uniči strukturo povedi, večbesedne pojavnice ali negotovost.

## Preverjanje mora ustrezati raziskovalni nalogi

Skupna točnost, ki jo navede avtor modela, ni preverjanje vašega korpusa. Iz lastnega gradiva izberite vzorec in preglejte plast, ki jo analiza dejansko uporablja.

Utemeljen postopek je:

1. vzorec stratificiramo po žanru, obdobju ali drugem verjetnem viru razlik;
2. ročno anotiramo ali preverimo pomembne značilnosti;
3. primerjamo samodejne in referenčne oznake;
4. po potrebi poročamo o preciznosti, priklicu ali ujemanju;
5. pregledamo ponavljajoče se tipe napak, ne le ene skupne ocene;
6. ocenimo, ali so napake naključne ali sistematično povezane s primerjanimi skupinami.

Če razpoznavalnik zaradi drugačnih okrajšav pogosteje spregleda zgodovinske ženske, je primerjava skupin lahko pristranska tudi ob navidezno dobri skupni točnosti.

## Razpoznavanje entitet ni razreševanje identitet

Ko niz *Ljubljana* prepoznamo kot kraj, še ne vemo, na kateri zapis v podatkovni zbirki se nanaša. Podobno lahko *J. Novak*, *Janez Novak* in *Novak* označujejo eno osebo ali več oseb. **Razreševanje entitet** omembe poveže s stabilnimi identitetami in zabeleži negotovost.

Uporabite identifikatorje, različice imen, časovne podatke in provenienco. Povezave ne vsiljujte, če ni dovolj dokazov. Nerazrešena omemba je boljša od samozavestne napačne povezave.

## Razdelan primer: glagoli govorjenja v časopisju

Predpostavimo, da želimo primerjati poročevalske glagole v dveh časopisnih obdobjih.

1. Določimo in vzorčimo primerljivo časopisno gradivo.
2. Ohranimo metapodatke o članku in datumu.
3. Izvedemo tokenizacijo, lematizacijo, morfološko in odvisnostno analizo.
4. Po lemi in konstrukciji poiščemo možne glagole govorjenja.
5. Ročno preverimo stratificiran vzorec, tudi naslove in navedke.
6. Resnične poročevalske rabe ločimo od homonimije in napak razčlenjevanja.
7. Števila normaliziramo glede na velikost korpusa in porazdelitev člankov.
8. Razlike razlagamo skupaj z uredniškim in zgodovinskim kontekstom.

Anotacija zoži iskalni prostor. Ne nadomesti interpretativnega razlikovanja med navedkom, poročanim govorom, metaforo in obrazcem.

## Vaja

Izberite raziskovalno vprašanje in pripravite načrt anotacije. Navedite potrebne plasti, programsko opremo in jezikovni model, vhodni format, izhodna polja, vzorec za preverjanje, pričakovane napake in točko, na kateri je potrebna človeška odločitev.

## Refleksija

- Katere kategorije v vašem gradivu so slabo zastopane v običajnih učnih podatkih?
- Bi napaka enako prizadela vse dokumente ali bi lahko izkrivila primerjavo?
- Katere anotacijske plasti lahko izpustite, ne da bi oslabili argument?

## Povzetek

Jezikoslovna anotacija besedilne vzorce naredi računalniško obdelovalne z napovedanimi plastmi, kot so leme, slovnične oznake, skladnja in entitete. CLASSLA ponuja močno infrastrukturo za slovenščino in južnoslovansko gradivo, vendar je rezultat še vedno odvisen od modela. Uporabite le plasti, ki jih zahteva vprašanje, ohranite povezavo z izvirnim besedilom, zabeležite različice in preverite ravno tisto značilnost, na kateri temelji interpretacija.
