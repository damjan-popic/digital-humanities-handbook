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

## Minimalni standard

Pred zahtevkom za vključitev zaženite:

```bash
python scripts/check_handbook.py
python scripts/check_translation_coverage.py
mkdocs build --strict
```

V zahtevku pojasnite, kaj se je spremenilo, kako je bilo preverjeno, na kateri jezik in izdajo se nanaša ter katere podatkovne, avtorske, zasebnostne ali etične omejitve veljajo.

## Študenti kot avtorji

Študijska naloga ne postane javna samodejno. Študent se sam odloči za oddajo, razume odprti licenci, prejme avtorsko priznanje in opravi uredniški pregled. Ocena pri predmetu in odločitev za objavo sta ločeni. Ta ločitev varuje študenta in priročnik.

Pred večjim prispevkom preberite datoteke `CONTRIBUTING.md`, `EDITORIAL_POLICY.md`, `REVIEW_POLICY.md` in `TRANSLATION_POLICY.md` v korenu repozitorija.
