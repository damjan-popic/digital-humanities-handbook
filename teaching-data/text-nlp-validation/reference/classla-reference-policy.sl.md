---
translation_status: machine-assisted draft; requires human language review
---

# Pravila referenčnega anotiranja CLASSLA

Štiri datoteke CoNLL-U so ročno pregledana učna referenca različice
`TNLP-REF-1`. Omogočajo pregleden preizkus ene zamrznjene izvedbe CLASSLA, ne
določajo pa univerzalne jezikoslovne resnice ali splošne kakovosti modela.

## Odločitve

1. Ohranite izbrano poved, velike in male črke ter ločila. Ponudnikovega OCR ne
   zamenjajte prikrito z referenčnim prepisom.
2. Pri sodobnih vzorcih in referenčnem prepisu anotirajte branje dane plasti.
   Pri ponudnikovem OCR ohranite opaženo obliko, vendar anotirajte na podlagi
   posnetka preverjeno raziskovalno mejo besede ali lemo, kadar arhivski paket
   dokumentira očitno napako prepoznavanja.
3. Zlepljeni OCR `narodain` zapišite kot večbesedno pojavnico CoNLL-U `naroda`
   + `in`. Ohranite opažene oblike `stavovske`, `kultrunega` in `i`, pripišite
   pa izvorno utemeljene leme `stanovski`, `kulturen` in `ki`.
4. Posamostaljeni `vse` v `zato gre vse` obravnavajte kot `PRON`, lemo `ves`
   in osebek glagola `gre`. Gre za izrecno pregledovalčevo odločitev.
5. Sporne analize CLASSLA ohranite, kadar vzorec sam ne utemeljuje odločnejše
   trditve. Nestrinjanje o odvisnostih in zgodovinskih lemah je možno tudi po
   pregledu.

Pregled je 7. septembra 2026 opravil en vzdrževalec. Neodvisnega dvojnega
anotiranja ali razsojanja ni bilo. Pri ponovni rabi navedite omejitev, ta pravila
in imenovalce posameznih plasti.
