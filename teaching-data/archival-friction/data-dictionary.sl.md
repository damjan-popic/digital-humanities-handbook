# Podatkovni slovar

Vse datoteke CSV uporabljajo UTF-8, vejico kot ločilo, eno naslovno vrstico
in zaključke vrstic `\n`. Oznake opazovanj se začnejo z `AF-`, pristnih
uredniških odločitev z `AF-ED-`, sintetičnih posegov z `AF-SYN-`, nerešenih
primerov z `AF-U-`, vrstic pregleda OCR pa z `AF-OCR-A`.

## Plasti in vaje

`source/` vsebuje samo nespremenjeno gradivo ponudnikov: zgodovinski PDF,
zajeta zapisa dLib in Commons ter OCR ponudnika. `reference/` vsebuje
priročniška, na viru utemeljena opazovanja, uredniške odločitve, referenčni
prepis in pravila. `teaching/` prijavlja sintetične motnje. `raw/` ohranja
njihov namenoma neurejeni rezultat; `interim/` vsebuje kandidate za pregled;
`cleaned/` preverjeni rezultat; `output/` izpeljane mere in povzetke;
`validation/` pričakovane vrednosti in zgoščene vrednosti; `known-problems/`
pa omejitve.

Pri metapodatkovni vaji primerjajte `raw/messy-records.csv` z
`reference/observations.csv` in odločitve zapišite, preden pogledate
`cleaned/records.csv`. Pri vaji OCR primerjajte ponudnikovo in referenčno
besedilo, nato preverite natančne številčne rezultate v `output/`.

## Polja opazovanj

Ta stalna polja so v `reference/observations.csv`, obeh metapodatkovnih
tabelah na vrhnji ravni ter tabelah v plasteh `raw/` in `cleaned/`.

| Polje | Pomen in dovoljene vrednosti |
| --- | --- |
| `record_id` | Stalna oznaka opazovanja o številki ali prispevku. |
| `record_kind` | Vrsta zapisa: `issue` (številka), `captioned_feature` (prispevek z napisom), `portrait` (portret) ali `group_portrait` (skupinski portret). |
| `page` | Stran ali razpon strani PDF-ja kot besedilo. |
| `label_transcribed` | Priročniški prepis natisnjenega napisa po objavljenih pravilih. |
| `label_provider_ocr` | Ustrezno besedilo OCR-ja ponudnika. |
| `date_scope` | Kaj datum opisuje: `issue_publication` (objava številke), `depicted_event` (upodobljeni dogodek), `referenced_event` (omenjeni dogodek), `photograph_creation` (nastanek fotografije) ali `not_modelled` (datum ni modeliran). |
| `printed_date` | Datumski izraz, viden v viru; prazno, če ni natisnjen. |
| `date_normalized` | Normalizirani datum, ki ga podpirajo dokazi; prazno, če je neznan ali ni modeliran. |
| `date_status` | `exact` (neposredno naveden), `derived_from_relative_date` (izpeljan iz relativnega datuma), `unknown` (neznan) ali `not_applicable` (se ne uporablja). |
| `issue_context_date` | Datum objave kot kontekst prispevka, ločen od datuma prispevka. |
| `printed_person_or_group` | Oznaka osebe ali skupine natančno tako, kot je natisnjena v viru. |
| `entity_structure` | `zero_people` (brez oseb), `one_person` (ena oseba) ali `multiple_people` (več oseb); to ni rezultat povezovanja z normativnim zapisom. |
| `authority_candidate` | Zunanji kandidat za normativni zapis, preverjen pri usklajevanju. |
| `authority_link_status` | `not_attempted` (ni bilo poskusa), `not_reconciled` (ni usklajeno), `candidate_rejected` (kandidat zavrnjen), `accepted` (sprejet), `unresolved` (nerešeno) ali `not_applicable` (se ne uporablja). |
| `authority_evidence` | Dokazi za stanje povezave ali razlog, da se povezovanje ne uporablja. |
| `source_locator` | Stran in območje v shranjenem PDF-ju. |
| `evidence_note` | Pojasnilo prepisa, datuma, modela ali omejitve. |
| `synthetic` | `true` samo, če na neurejeno vrstico vpliva prijavljena učna motnja, sicer `false`. |

Natisnjena oznaka, struktura enote in povezava z normativnim zapisom so
ločene. Jasno natisnjeno ime brez zunanjega URI-ja je lahko `one_person` in
`not_attempted`; zato še ni nerešena identiteta. Skupinski portret je
`multiple_people`, ne ena nerešena oseba. AF-P1-002 ima
`date_scope=photograph_creation`, prazno `date_normalized`,
`date_status=unknown` in ločeni `issue_context_date=1925-02-07`.

## Polja učnega in preglednega dela

`teaching/synthetic-perturbations.csv` vsebuje `perturbation_id`, `operation`
(`set` za spremembo ali `duplicate` za podvojitev), `target_record_id`,
neobvezni `new_record_id`, spremenjeno `field`, umetno `synthetic_value` in
`teaching_reason`. To so prijavljeni pripomočki pri vaji, nikoli
zgodovinska dejstva.

`interim/reconciliation-candidates.csv` vsebuje `candidate_id`, `record_id`,
`field`, `candidate_value`, `reference_value`, `review_status` in
`synthetic`. Vrstice zahtevajo pregled in ne dovoljujejo tihih sprememb.

`correction-log.csv` in `cleaned/decisions.csv` vsebujeta `decision_id`,
`record_id`, `field`, `input_value`, `result_value`, določeno dejanje
`action`, `source_locator`, `evidence`, `responsible_process`,
`decision_date`, `rule_version`, `confidence`, `reversible` in `synthetic`.
Osem vrstic z `synthetic=false` dokumentira delo ob viru, štiri z
`synthetic=true` pa razveljavijo prijavljene motnje.

`unresolved-cases.csv` vsebuje `case_id`, `record_id`, polje `field`, stanje
`status`, `current_value`, `current_evidence`, `reason` in
`evidence_needed`. Neznani ali zavrnjeni rezultat je preverljiv izid, ne
prazno mesto za samodejno dopolnitev.

## Polja rezultatov OCR

`output/ocr-evaluation.csv` ločeno poroča o zamenjavah, izpustih in vstavkih
znakov in besed, referenčnih imenovalcih, skupnem številu sprememb ter CER in
WER. Poravnava znakov uporablja kodne točke Unicode z notranjimi presledki,
poravnava besed pa deli po presledkih Unicode. Ob izenačenju ima prednost
ujemanje, nato zamenjava, izpust in vstavek. Stopnji sta
`spremembe / referenčni imenovalec` in sta zaokroženi na šest decimalk po
pravilu zaokroževanja polovice k sodemu številu.

`output/ocr-error-audit.csv` vsebuje `audit_id`, `sample_id`,
`source_locator`, `reference_form`, `provider_form`, `operation`,
`error_category`, `policy_or_recognition`, `probable_downstream_consequence`,
`review_status` in `aggregate_relation`. Devet vrstic predstavlja vse
neujemajoče se besedne operacije in seštevek se ujema z besednimi S/D/I.
Znakovne S/D/I nastanejo z ločeno poravnavo celotnega niza, zato niso umetno
razdeljene med besedne vrstice.

`output/record-summary.csv` uporablja `dimension`, `category`, `count` in
`notes` za popis, vrste zapisov, stanja datumov, strukture enot in stanja
povezav. `validation/expected-results.json` hrani iste ključne rezultate in
mere OCR v strojno berljivi obliki.
