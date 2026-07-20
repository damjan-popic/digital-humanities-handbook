# Presoja založniške poti

## Projekt

**Priročnik za digitalno humanistiko / Digital Humanities Handbook** je odprta, dvojezična in verzionirana digitalna publikacija. Sestavljata jo:

1. stabilno, recenzabilno jedro dvanajstih poglavij in dveh učnih poti;
2. živa zbirka praktičnih postopkov, študij primerov, kode in učnih gradiv.

Različica `v1.0` bo vsebinsko zamrznjena, recenzirana in arhivirana izdaja. Veja `main` bo po izdaji ostala razvojna različica.

## 1. Razpis za tisk učbenikov FF 2026–2027

### Kdaj je ustrezen

Razpis je vsebinsko močna pot, če so izpolnjeni vsi naslednji pogoji:

- publikacija bo formalno navedena kot obvezna literatura pri obveznem predmetu veljavnega programa FF;
- založba sprejme digitalno rojeno izdajo oziroma izrecno izjemo od tiskarsko zasnovanega postopka;
- končno različico `v1.0` in dve podpisani recenziji je mogoče oddati do 30. septembra 2026;
- pogodba omogoči, da živa različica ostane javna pod odprto licenco in se po izdaji razvija naprej;
- jasno je ločeno, kaj je recenzirana izdaja in kaj poznejša uredniško pregledana dopolnitev.

### Prednosti

- formalni status univerzitetnega učbenika;
- izrecna pedagoško-didaktična merila, ki jih projekt že uresničuje;
- recenzentski, lektorski, uredniški in katalogizacijski postopek;
- močna povezava z učnim načrtom ter institucionalna prepoznavnost.

### Neskladja in tveganja

Razpis je po jeziku in postopkih namenjen **tisku**: določa tipsko stran, format, črno-beli tisk, prelom, naklado, prodajo, izvode in prenos materialnih avtorskih pravic. Odprti dostop je predviden le, če založba zanj pridobi sofinanciranje. To ni samoumevno združljivo z obstoječim odprtim repozitorijem, licenco CC BY 4.0 za besedilo in MIT za kodo.

Izraz »končna različica besedila« je mogoče smiselno izpolniti z označeno izdajo `v1.0`, vendar mora založba to razlago potrditi pisno. Brez tega lahko živa narava projekta deluje kot neizpolnjen pogoj in ne kot prednost.

## 2. Oddelčna strokovna publikacija 2026–2027

Priložen je prijavni obrazec in ne celoten razpis. Obrazec zahteva končno besedilo, kratek opis monografije, obseg v avtorskih polah, lektorja, prevajalca povzetka in priloge. Ne zahteva navedbe obveznega predmeta ali dveh recenzentov in je zato na prvi pogled vsebinsko prožnejši.

### Zakaj je lahko bližja pot

- publikacija lahko nagovarja več predmetov, oddelkov in širšo strokovno javnost;
- izraz »strokovna publikacija« dopušča priročnik, ki ni vezan izključno na en obvezni predmet;
- projekt je mogoče utemeljiti kot oddelčno infrastrukturo za poučevanje, študentsko avtorstvo in odprto strokovno delo;
- dvojezičnost in odprta digitalna oblika sta lažje predstavljivi kot vsebinska odlika, ne odstop od natisnjenega učbenika.

### Kaj še ni znano

Ker polni razpis ni priložen, je treba pred prijavo pisno potrditi:

- ali sprejemajo izvorno digitalno publikacijo brez obvezne tiskane naklade;
- ali je lahko izročena končna različica označena spletna izdaja in arhivski PDF;
- kakšen recenzijski postopek velja;
- kakšne pravice zahteva založniška pogodba;
- ali sta odprta licenca in nadaljnji razvoj na GitHubu dovoljena;
- ali je dvojezični spletni priročnik upravičen strošek oziroma predmet sofinanciranja.

## Priporočilo

### Prednostna strategija

Najprej pošljite **skupno predhodno vprašanje** Znanstveni založbi FF z delujočim prototipom in jasno založniško arhitekturo. Ne prijavljajte projekta kot »spletno stran« ali »repozitorij«, temveč kot:

> odprto digitalno strokovno oziroma univerzitetno publikacijo z recenzirano, označeno in arhivirano izdajo ter živo razvojno različico.

Založbo prosite, naj pisno določi, katera od obeh poti je primerna in pod katerimi pogoji.

### Če založba sprejme digitalni učbenik

Izberite razpis za učbenike, kadar lahko projekt zanesljivo navežete na obvezni predmet in pogodba ostane združljiva z odprto licenco. Prijavite `v1.0`, ne veje `main`. Kot končno besedilo oddajte arhivski PDF ter izvoz iz označene izdaje, recenzentom pa omogočite tudi spletni pregled.

### Če založba vztraja pri tiskani knjigi ali izključnih pravicah

Ne prilagajajte osnovne arhitekture projekta tisku. Uporabite pot oddelčne strokovne publikacije, če dovoljuje odprto digitalno izdajo, ali poiščite drugo institucionalno pot za recenzijo, DOI/ISBN, COBISS in arhiviranje. Tiskani izvod je lahko neobvezni arhivski izvoz, ne uredniški izvirnik.

## Predlagani založniški predmet

- **Primarna publikacija:** dvojezična statična spletna izdaja, zgrajena iz Markdowna.
- **Recenzirana izdaja:** oznaka `v1.0.0` z datumom in zapisom sprememb.
- **Arhivski predmet:** ZIP izvornih datotek, zgrajeno spletno mesto in PDF-posnetek stabilnega jedra.
- **Licenci:** CC BY 4.0 za besedilo in učna gradiva; MIT za izvirno kodo, če pogodba to omogoči.
- **Navajanje:** `CITATION.cff`, priporočeni navedek, različica in trajni identifikator.
- **Živa izdaja:** javna veja `main`, kjer nove vsebine vstopajo po uredniškem in tehničnem pregledu.
- **Nova recenzija:** večje metodološke ali strukturne spremembe vodijo v novo glavno izdajo.
