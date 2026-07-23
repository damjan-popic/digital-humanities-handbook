---
title: "Predloga za študentski prispevek: praktični postopek"
description: "Strukturirana predloga za pretvorbo študijske naloge ali področnega znanja v majhen in ponovljiv postopek za priročnik."
tags: [studenti, prispevek, postopek, predloga, ponovljivost]
---

# Predloga za študentski prispevek: praktični postopek

Predlogo uporabite, kadar želite študijsko nalogo ali svoje področno znanje preoblikovati v praktični prispevek za priročnik.

Prispevek naj odgovori na **eno omejeno vprašanje**, izdela **en pregleden rezultat** in drugemu študentu omogoči, da postopek ponovi. Ni skrajšana seminarska naloga in ni predstavitev posameznega orodja.

!!! important "Ocenjevanje in objava sta ločena postopka"
    Študijska naloga ne postane javna samodejno. Študent lahko opravi ocenjeno obveznost, ne da bi soglašal z objavo. Za javno vključitev so potrebni ločena uredniška odločitev, navedeno avtorstvo, preverjene pravice in soglasje z licencama priročnika.

## Izberite prispevek

Primerno vprašanje se začne s **Kako ...?** in poimenuje konkretno nalogo.

Dobri primeri:

- Kako v QGIS-u primerjam historični zemljevid z današnjim ortofotom?
- Kako terenska opažanja pretvorim v ponovno uporabno zbirko podatkov o dediščini?
- Kako izmerim napake OCR v manjšem zgodovinskem korpusu?
- Kako kartiram negotove omembe krajev, ne da bi zakril dvoumnost?
- Kako povzetek, ki ga je izdelala UI, preverim ob arhivskih virih?

Izogibajte se naslovom, kot so *QGIS*, *Digitalna arheologija*, *Moja diplomska naloga* ali *Umetna inteligenca*. Ti poimenujejo področje ali orodje, ne pa ponovljive naloge.

## Minimalni paket za oddajo

Oddajte manjšo mapo ali repozitorij s to strukturo:

```text
studentski-prispevek/
├── postopek.md
├── README.md
├── vzorec/
│   ├── vhod/
│   └── izhod/
├── koda/                 # neobvezno
├── viri.md
└── izjava-o-prispevku.md
```

Uporabite majhen vzorec z urejenimi pravicami. Ne oddajajte celotne podatkovne zbirke iz diplomske naloge, zaupnega institucionalnega gradiva, natančnih lokacij ranljive dediščine, osebnih podatkov ali slik tretjih oseb, če objava in ponovna uporaba nista izrecno dovoljeni.

## Predloga za kopiranje

Spodnje besedilo Markdown kopirajte v `postopek.md` in zamenjajte navodila v oglatih oklepajih.

```markdown
---
title: "Kako [izvedem eno konkretno nalogo]?"
description: "Enostavčni opis vhoda, metode in pričakovanega izhoda."
category: "mapping"
difficulty: "beginner"
time: "60–120 min"
tags: [dediscina, qgis, preverjanje]
author: "Ime študenta oziroma študentke"
status: "student-draft"
---

# Kako [izvedem eno konkretno nalogo]?

<div class="answer-meta" markdown>
<span>mapping</span>
<span>beginner</span>
<span>60–120 min</span>
</div>

## Kaj želite narediti

Postopek uporabite, kadar imate [vhodno gradivo] in morate za [humanistični namen] pripraviti [vidni izhod].

Nalogo opišite v dveh do petih povedih. Najprej poimenujte področno vprašanje, šele nato programsko opremo.

## Raziskovalni kontekst

Pojasnite, zakaj je naloga pomembna na vašem področju.

- Za kakšen vir ali predmet gre?
- Katero strokovno odločitev postopek podpira?
- Kaj bi bralec napačno razumel, če bi vir obravnaval kot nevtralne podatke?

Razdelek naj bo kratek. Namesto ponavljanja splošne teorije povežite ustrezno poglavje priročnika.

## Kaj potrebujete

- **Izvorno gradivo:** [zemljevidi, besedila, fotografije, terenski zapiski, zapisi podatkovne zbirke ...]
- **Dostop:** [programska oprema, račun, repozitorij, dovoljenje ustanove]
- **Znanje:** [brez predznanja, osnove preglednic, osnove QGIS-a, osnove Pythona ...]
- **Odločitve:** [enota analize, časovni obseg, koordinatni sistem, kategorije, pravila za negotovost]

## Vhodni podatki in izvor

Opišite vzorec in njegov izvor.

| Enota | Vir ali ustvarjalec | Datum | Licenca/dostop | Spremembe |
|---|---|---|---|---|
| `vzorcni-zemljevid.tif` | [vir] | LLLL | [licenca ali omejitev] | obrezano za pouk |
| `opazanja.csv` | [ustvarjalec] | LLLL-MM-DD | CC BY / zasebno / omejeno | imena posplošena |

Če uporabljate tabelo, navedite minimalna obvezna polja.

| Polje | Obvezno? | Primer | Pomen |
|---|---:|---|---|
| `id` | da | `lokacija-001` | Stabilni identifikator zapisa. |
| `vir` | da | `terenski pregled` | Izvor opažanja. |
| `datum` | da | `2026-07-23` | Kjer je mogoče, uporabite zapis ISO. |
| `negotovost` | ne | `srednja` | Dokumentirana stopnja gotovosti ali dvoumnosti. |

## Orodja in različice

- [Ime orodja](https://example.org) — njegova vloga v postopku.
- Uporabljena različica: [različica, samo če je pomembna].
- Druga možnost: [neobvezno orodje in posledice zamenjave].

Kjer je mogoče, povežite uradno dokumentacijo.

## Postopek

1. **Pripravite majhen preizkusni vzorec.**  
   Začnite z dvema ali tremi zapisi, eno sliko ali enim kratkim besedilom. Izvorne datoteke ohranite nespremenjene.

2. **Zabeležite izvor in nastavitve.**  
   Navedite spletni naslov ali arhivsko signaturo, datum dostopa, format datoteke, koordinatni sistem, različico orodja in pomembne nastavitve.

3. **Izvedite prvo pretvorbo.**  
   Natančno napišite, kaj je treba klikniti, zagnati, vnesti ali nastaviti.

4. **Rezultat ročno primerjajte z virom.**  
   Preverite najmanj en izhod ob izvirniku. Zabeležite neskladja, negotovost in informacije, ki so se pri pretvorbi izgubile.

5. **Težave popravite ali označite.**  
   Vira nikoli ne popravljajte brez sledi. Izvorno vrednost ohranite, normalizirano, domnevano ali popravljeno vrednost pa zabeležite ločeno.

6. **Postopek razširite šele po uspešnem preizkusu.**  
   Obdelajte celoten učni vzorec, ne pa samodejno vsega dostopnega gradiva.

7. **Izvozite in dokumentirajte izhod.**  
   Uporabite stabilna imena datotek in dodajte kratek README z opisom nastanka rezultatov.

## Izhod

Poimenujte pričakovani rezultat in prikažite njegovo strukturo.

```text
vzorec/izhod/
├── rezultat.csv
├── zemljevid-rezultata.png
├── vzorec-za-preverjanje.csv
└── znane-omejitve.md
```

Pojasnite vsebino posamezne datoteke in povejte, katero naj bralec odpre najprej.

## Preverjanje

Navedite konkretne preizkuse.

- Ali je vsaka izvorna enota v izhodu zastopana natanko enkrat?
- Ali lahko vsak rezultat povežete z virom?
- Ali so se koordinate, datumi, imena ali kategorije spremenili?
- Ali so negotovi primeri označeni ali so bili na silo razvrščeni?
- Ali druga oseba z navodili dobi enak izhod?

Dodajte najmanj eno merilo uspeh/neuspeh.

> Postopek je uspešen, če [konkretno število ali pogoj], ročni pregled [število] primerov pa ne pokaže [opredeljene kritične napake].

## Interpretacija in omejitve

Napišite, katere trditve izhod podpira in česa ne more dokazati.

Vključite najmanj:

- eno prednost digitalnega postopka;
- eno izgubo ali preoblikovanje;
- en verjetni vir napak;
- eno trditev, ki bi bila premočna.

## Pravice, etika, dostop in občutljivost dediščine

Obravnavajte vprašanja, ki veljajo za vzorec:

- avtorske pravice in ponovna uporaba slik;
- osebni podatki in soglasje;
- arhivske ali institucionalne omejitve;
- natančne lokacije ranljivih najdišč;
- pravice skupnosti oziroma kulturna avtoriteta;
- ali naj bo izhod javen, posplošen, omejen ali izpuščen.

Ne objavite tehnično privlačnega primera, ki povzroči varstveno, zasebnostno ali avtorskopravno težavo.

## Razdelan primer

Opišite en manjši preizkus od vhoda do izhoda. Po potrebi uporabite umetni ali zakonito ponovno uporabljiv vzorec.

Vključite:

- vhod;
- pomembne nastavitve;
- izhod;
- eno napako ali dvoumni primer;
- popravek ali interpretacijo.

## Povezava s priročnikom

Povežite:

- najmanj eno pojmovno poglavje;
- najmanj en sorodni praktični postopek;
- eno študijo primera, kadar obstaja smiselna povezava.

Povezavo pojasnite z eno povedjo; ne dodajte samo gole zbirke povezav.

## Vaja

Drugemu študentu pripravite majhno razširitev ali preizkus.

> Postopek uporabite na [novem majhnem vzorcu], preglejte [število] izhodov ter v kratki refleksiji pojasnite en uspešen rezultat, eno napako in eno metodološko omejitev.

## Nadaljnje branje

Dodajte samo vire, ki so neposredno potrebni za razumevanje ali ponovitev naloge.

## Dnevnik sprememb

| Datum | Sprememba |
|---|---|
| LLLL-MM-DD | Prvi študentski osnutek. |
```

## Izjava o prispevku

V datoteko `izjava-o-prispevku.md` vnesite:

```markdown
# Izjava o prispevku

- Avtor oziroma avtorica:
- Predmet ali izpit:
- Učitelj oziroma urednik:
- Datum oddaje:
- Postopek je preizkusil/a:
- Viri in gradivo tretjih oseb so preverjeni: da / ne / ni relevantno
- Uporaba UI: brez uporabe / natančen opis
- Odločitev glede objave: samo za ocenjevanje / lahko se obravnava za objavo
- Soglasje za licenco sprejetega besedila: CC BY 4.0 / še ni dano
- Soglasje za licenco sprejete izvirne kode: MIT / še ni dano
- Znane omejitve ali gradivo, ki ne sme biti objavljeno:
```

Odločitev **samo za ocenjevanje** je povsem veljavna in ne sme vplivati na oceno.

## Jezikovna pravila za študentske prispevke

Če učitelj ne določi drugače:

- celotni postopek oddajte v jeziku predmeta;
- slovenski različici dodajte angleški naslov in enostavčni opis;
- celotni prevod v drugi jezik je ločen prispevek in potrebuje jezikovni pregled;
- vzporedni angleški in slovenski strani naj imata enako ime datoteke in relativno pot.

## Kontrolni seznam

- [ ] Naslov vsebuje eno praktično vprašanje.
- [ ] Vhod in pričakovani izhod sta poimenovana.
- [ ] Majhen vzorec je priložen ali ga je mogoče rekonstruirati.
- [ ] Izvor in pravice so dokumentirani.
- [ ] Postopek vsebuje oštevilčene in izvedljive korake.
- [ ] Najmanj en izhod je ročno preverjen ob viru.
- [ ] Navedeno je merilo uspeh/neuspeh.
- [ ] Pojasnjeni sta najmanj dve realistični napaki ali omejitvi.
- [ ] Občutljive informacije so izpuščene, posplošene ali omejeno dostopne.
- [ ] Navodila je preizkusila še ena oseba.
- [ ] Morebitna uporaba UI je razkrita.
- [ ] Ocenjevanje in soglasje za objavo sta zabeležena ločeno.
