# Prispevajte

Priročnik je zasnovan tako, da raste z majhnimi, avtorsko priznanimi in pregledanimi prispevki. Dober prispevek naslednjemu bralcu pusti jasnejše vprašanje, bolj ponovljivo metodo ali natančnejši prevod.

## Možni prispevki

- prijava nedelujočega navodila, povezave ali napačne trditve;
- prevod ali jezikovni pregled ustrezne strani;
- izboljšan primer, korak preverjanja ali opis pričakovanega izhoda;
- dokumentiran omejen praktični postopek;
- majhna učna podatkovna zbirka z urejenimi pravicami;
- kritična študija javnega projekta;
- predlog spremembe temeljnega poglavja za naslednjo recenzirano izdajo.

## Predloge

- [Predloga za kritično študijo primera](project-template.md) — petnajst razdelkov o virih, pregledanih dokazih, modeliranju, napakah, pravicah, ponovni uporabi in omejeni učni nalogi; zagon kode ni obvezen;
- [Predloga za študentski prispevek: praktični postopek](student-workflow-template.md) — dvojezična in dostopnejša struktura za študijske naloge, diferencialne izpite in prve prispevke.

Študentska predloga vsebuje obliko strani, strukturo oddajnega paketa, merila preverjanja, izjavo o uporabi UI, pravila glede občutljivih podatkov ter ločeno odločitev o morebitni javni objavi.

Pri študiji primera skupaj pripravite par jezikovnih strani, avtorske
metapodatke in datirani revizijski zapis. Podedovani primeri s stanjem
`legacy-audited` ostajajo vidno ločeni od polne strukture `showcase-v1`.
Predloga pojasni, katere zapise urejate in kateri katalogi nastanejo z
generiranjem; konceptualne povezave sodijo v `intertextuality.yml`.

## Minimalni standard

Pred zahtevkom za vključitev zaženite:

```bash
make check
```

V zahtevku pojasnite, kaj se je spremenilo, kako je bilo preverjeno, na kateri jezik in izdajo se nanaša ter katere podatkovne, avtorske, zasebnostne ali etične omejitve veljajo.

## Študenti kot avtorji

Študijska naloga ne postane javna samodejno. Študent se sam odloči za oddajo, razume odprti licenci, prejme avtorsko priznanje in opravi uredniški pregled. Ocena pri predmetu in odločitev za objavo sta ločeni. Ta ločitev varuje študenta in priročnik.

Pred večjim prispevkom preberite datoteke `CONTRIBUTING.md`, `EDITORIAL_POLICY.md`, `REVIEW_POLICY.md` in `TRANSLATION_POLICY.md` v korenu repozitorija.
