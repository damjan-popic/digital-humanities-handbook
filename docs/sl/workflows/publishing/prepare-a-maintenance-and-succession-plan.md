---
title: "Kako pripravite načrt vzdrževanja in nasledstva?"
description: "Določite odgovornost za znanstveni vir, preizkusite obnovo in dokumentirajte prenos, preden ustanovni vzdrževalec odide."
category: "Objavljanje in podatki FAIR"
category_id: "Publishing & FAIR data"
difficulty: "srednje zahtevno"
time: "90–150 min"
tags: [vzdrževanje, hramba, upravljanje, nasledstvo, dostopnost]
status: draft
translation_status: "machine-assisted draft; requires human language review"
---

# Kako pripravite načrt vzdrževanja in nasledstva?

<div class="answer-meta" markdown="span">
<span>Objavljanje in podatki FAIR</span><span>srednje zahtevno</span><span>90–150 min</span>
</div>

!!! warning "Osnutek in obseg vaje"
    Postopek je pripravljen s strojno pomočjo ter čaka na strokovni in slovenski jezikovni pregled usposobljenih pregledovalcev. Spodnje vloge in storitve so predloga načrta, ne dokaz obstoječih imenovanj. Pri vaji ne objavljajte poverilnic in ne prenašajte računov.

## Kaj želite doseči

Kdo lahko popravi navedeno digitalno izdajo po odhodu ustanovnega urednika? Pripravite izvedljiv načrt nadaljnje skrbi ali odgovornega zaključka aktivnega vzdrževanja. S poglavjem [Živi odprti priročnik](../../chapters/open-living-handbook.md) ločite gostovanje, uredniško odgovornost in dolgoročno hrambo.

## Kaj potrebujete

- Popis publikacije, repozitorijev, domen, zunanjih storitev in podatkovnih odvisnosti.
- Obstoječe nosilce vlog, obveznosti podaljševanja in realistični proračun vzdrževanja.
- Vzorec varnostne kopije z razjasnjenimi pravicami ter ločen lokalni prostor za obnovo.
- Osebo, ki lahko postopek preizkusi brez ustanoviteljevega zasebnega znanja.

## Postopek

1. Določite organizacijskega nosilca, urednika, tehničnega vzdrževalca in predvidenega naslednika. Ločite pravico odločanja od dovoljenj za dostop. Sprejem dejanskih vlog potrdite zasebno; pripadnost ustanovi še ne pomeni odgovornosti.
2. Popišite odvisnosti in storitve: izvajalno okolje, orodja za gradnjo, zunanje podatke/API, repozitorij, domeno, gostovanje, depozit in zapise za navajanje. Vsakemu določite vir različice ali datirano preverjanje pogojev, sprožilec pregleda, nosilca in obveznost podaljševanja. Uporabite neobčutljiv sklic na vnos v odobrenem upravljalniku poverilnic, nikoli njegove skrivne vsebine.
3. Interval pregleda prilagodite posledicam in sredstvom. Vključite pomen povezav, obvestila o odvisnostih in varnosti, ponovitev učnih primerov, razhajanje prevodov, dostopnost in prevzem iz depozita. Kjer je znano, navedite zadnji opravljen pregled in naslednji rok; načrtovani ritem ni opravljen pregled.
4. Določite obseg kopij, lokacije, roke hrambe in pristojnost za obnovo. Kopija repozitorija Git lahko izpusti prijave, datoteke izdaj, dovoljenja, zunanje podatke ali domenske zapise. Odobreno omejeno gradivo ločite od javnega izvora ter zmanjšajte obseg osebnih podatkov v kopijah.
5. Obnovo preizkusite v ločenem prostoru. Primerjajte kontrolne vsote, zgradite bralno kopijo, preglejte dvojezično navigacijo in učni primer ter zapišite manjkajoče storitve. Navedite datum, izvajalca, rezultat in odprte napake. Pri preizkusu ne prepišite delujočega mesta.
6. Preizkusite tudi uredniško nasledstvo: naslednik naj pri omejenem popravku poišče vire, pot pregleda, licenco in posledice za navedek. Popišite potrditve za dejanski prenos, stike za obnovo, odvzem dostopa in zamenjavo poverilnic po odobreni predaji.
7. Dogovorite se o zaključku, če prenos ne uspe. Zamrznite določljivo zadnjo izdajo, uredite hrambo, objavite konec vzdrževanja in meje podpore, zaprite sprejem novih prispevkov ter ohranite ustrezen stik za popravke. Nepodprtih navodil ne označujte kot aktualna.

## Dokumentacijski zapis

Učna predloga opisuje izmišljeni projekt. Pri dejanskem načrtu nadomestite opise vlog s potrjenimi imenovanji; zasebne stike in obnovitvene podrobnosti hranite v odobrenem omejenem okolju. Skupni strojni ključi omogočajo primerjavo EN/SL brez prevajanja identifikatorjev.

```yaml
record_type: maintenance-succession-plan
record_status: template
project: "Izmišljeni dvojezični vir o štetju zgodovinskih virov"
owner: "Oddelek ali ustanova; sprejem v čakanju"
editor: "Vloga čaka na potrjeno imenovanje"
technical_maintainer: "Vloga čaka na potrjeno imenovanje"
successor: "Vloga čaka na sprejem in preizkus"
dependencies:
  - name: "Izvajalno okolje in graditelj spletnega mesta"
    version_record: "Zaklenjene različice in zapis okolja; popis v čakanju"
    review_trigger: "Varnostno obvestilo, neuspešna gradnja ali četrtletni pregled"
  - name: "Zunanje povezave do zgodovinskih virov"
    version_record: "Lokator vira, avtoriteta in datum zadnjega preverjanja"
    review_trigger: "Prijavljena napaka ali začetek semestra"
services:
  - name: "Repozitorij Git in gostovanje"
    owner_role: technical_maintainer
    credential_reference: "Sklic na odobreni vnos v shrambi; brez skrivne vrednosti"
    renewal: "Potrdite imetništvo računa, plačevanje in obnovitveno ureditev"
  - name: "Domena"
    owner_role: owner
    credential_reference: "Odobreni sklic na registratorjev vnos; brez skrivne vrednosti"
    renewal: "Po potrditvi zapišite datum poteka registracije, plačnika in namestnika"
  - name: "Institucionalni depozit"
    owner_role: editor
    credential_reference: "Odobreni sklic za dostop do depozita; brez skrivne vrednosti"
    renewal: "Letno potrdite stik in depozitne obveznosti"
backups:
  scope: "Izvor, bralne datoteke, priloge, metapodatki in dovoljeni zapisi pregledov"
  locations: "Dve ločeno upravljani odobreni lokaciji; potrditev v čakanju"
  retention: "Institucionalni roki; omejite zasebne zapise in dokumentirajte izjeme"
restore_test: "Čakajo datum/izvajalec/vsote/gradnja/branje brez povezave/rezultat/nadaljnji ukrepi"
review_cadence: "Mesečna presoja (2 uri); četrtletno odvisnosti/dostopnost; semestrsko primeri/prevodi; letno obnova"
transfer_procedure:
  - "Potrdite naslednikove pristojnosti in razpoložljivi čas"
  - "V ločenem prostoru preizkusite obnovo in dvojezični popravek"
  - "Po pristojnih organizacijskih poteh odobrite prenos repozitorija/domene/depozita"
  - "Preverite naslednikov dostop; zamenjajte poverilnice in odstranite zastareli dostop"
  - "Posodobite javne stike in zapišite datum končane predaje"
exit_plan: "Brez naslednika določite zadnjo izdajo, jo oddajte v hrambo ter objavite konec vzdrževanja in pot popravkov"
```

## Rezultat

Popis odgovornosti in odvisnosti, dokazila o kopiranju in obnovi, datirani urnik pregledov, postopek prenosa ter načrt zaključka. Javna različica vsebuje vloge in varne sklice; omejeni operativni zapisi vsebujejo le nujne zasebne podatke. Načrta ne označite kot preizkušenega pred dejansko vajo.

## Preverite se

- Ali kdo razen ustanovitelja lahko poišče vse potrebne vire in dovoljenja?
- Ali ima vsaka storitev potrjenega nosilca in pot obnove?
- Ali preizkus obnovi bralno uporabnost in ne le datotek?
- Ali sta prevodom in dostopnosti dodeljena čas in odgovornost?
- Ali projekt lahko konča vzdrževanje in ohrani zadnjo izdajo, primerno za navajanje?

## Pogoste pasti

- Obravnava gesla osebnega računa kot načrta nasledstva.
- Enačenje nepreizkušene kopije z načrtom obnove.
- Razpršeno hranjenje občutljivih zapisov po načelu »ohranimo vse«.
- Obljuba tedenskih ročnih pregledov brez razporejenega časa zaposlenih.

## Vaja

Izmenjajte načrte in predpostavite, da ustanovitelj mesec dni ni dosegljiv. Predpostavite še, da je registracija domene potekla ali manjka odvisnost za gradnjo. Pri lokalnem preizkusu določite izvedljive korake in tiste, ki zahtevajo pristojno osebje. Popravite načrt in proračun; dejanske rezultate zabeležite ločeno od priporočil.

## Viri in preverjanje storitev

Preverjeno **7. septembra 2026**: Digital Preservation Coalition, [Fixity and checksums](https://www.dpconline.org/handbook/technical-solutions-and-tools/fixity-and-checksums) in [File formats and standards](https://www.dpconline.org/handbook/technical-solutions-and-tools/file-formats-and-standards); UNESCO, [Recommendation on Open Educational Resources (OER)](https://www.unesco.org/en/legal-affairs/recommendation-open-educational-resources-oer). Intervali in vloge zgoraj so predlagane učne odločitve, ne zahteve, pripisane tem virom.
