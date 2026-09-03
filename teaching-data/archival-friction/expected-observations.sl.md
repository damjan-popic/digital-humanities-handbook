# Pričakovana opazovanja

To so kontrolne točke, ne razlage, ki bi jih prepisali v seminarsko nalogo.

- Paket vsebuje en pristen zgodovinski predmet: en nespremenjen dvostranski
  PDF. Priročnik je ustvaril osem na viru utemeljenih opazovanj: eno o
  številki in sedem o prispevkih. Štiri učne motnje so izrecno sintetične.
- Neurejena tabela ima devet vrstic, ker AF-SYN-004 doda dvojnika;
  očiščena oziroma referenčna tabela ima osem stalnih oznak opazovanj.
- AF-P1-002 nima dokazljivega datuma nastanka fotografije. Polje
  `date_normalized` je prazno, `date_status` je `unknown`, datum 1925-02-07
  pa je shranjen samo kot `issue_context_date`.
- Relativna natisnjena datuma ob dokumentiranih in povratnih uredniških
  odločitvah podpirata 1925-02-01 za AF-P1-001 in 1925-01-27 za AF-P1-004.
- Jasno natisnjena imena ostanejo oznake iz vira tudi brez poskusa
  povezovanja z zunanjim normativnim zapisom. AF-P2-001 je
  `multiple_people`, ne ena nerešena identiteta. Oblika »Meker« je ohranjena,
  Ezra Meeker pa ima stanje `candidate_rejected`.
- `correction-log.csv` vsebuje devet na viru utemeljenih uredniških odločitev
  in štiri razveljavitve izrecno označenih sintetičnih motenj. Deveta
  dokumentira izbor, dekodiranje in normalizacijo presledkov od natančnega
  izvoza TXT iz dLib do primerjalnega odlomka. Vse imajo lokator, dokaz,
  odgovorni postopek, datum, različico pravil, stopnjo zaupanja in podatek o
  povratnosti.
- Pregled OCR zajema celotni izbrani primerjalni odlomek. Izračun CER in WER
  se začne po normalizaciji ob pripravi odlomka in ne meri izpuščenih
  presledkov postavitve. Vrstice pregleda besednih
  napak se seštejejo v zamenjave, izpuste in vstavke besed; znakovne operacije
  izvirajo iz ločene poravnave celotnega niza. CER in WER uporabljata
  referenčna imenovalca ter zaokroževanje na šest decimalk po pravilu polovice
  k sodemu številu.
- `output/record-summary.csv` poroča o popisu, vrstah zapisov, stanjih datumov,
  strukturah enot in stanjih povezav. Štetje opisuje model in samo po sebi ne
  razlaga političnega jezika številke.
