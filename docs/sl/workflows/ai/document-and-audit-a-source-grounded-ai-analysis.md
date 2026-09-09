---
title: "Kako dokumentiram in preverim analizo UI, utemeljeno v virih?"
description: "Ohranite vire, konfiguracijo, izhode in človeške odločitve ter razlikujte med reproducibilnostjo in sledljivo trditvijo."
category: "UI"
category_id: AI
difficulty: "srednje zahtevno"
time: "90–120 min"
tags: [UI, provenienca, kritika-virov, preverjanje, reproducibilnost]
status: draft
translation_status: machine-assisted draft; requires human language review
---

# Kako dokumentiram in preverim analizo UI, utemeljeno v virih?

<div class="answer-meta" markdown="span">
<span>UI</span>
<span>srednje zahtevno</span>
<span>90–120 min</span>
</div>

## Kaj želite doseči

Pojasniti želite, kako časopis oblikuje predstavo politične enotnosti, ne da
bi njegovo retoriko spremenili v ugotovitev o javnem mnenju. Ohranite dovolj
dokazov za pregled vsake pomembne trditve tudi po morebitnem umiku modela.
Postopek dopolnjuje poglavje
[UI, etika in ponovljivost](../../chapters/ai-ethics-reproducibility.md).

To je strojno podprt dokumentacijski osnutek, ki čaka na strokovni in jezikovni
pregled. Napačni izhodi v poglavju so avtorske učne simulacije. Spodnja predloga
ne beleži opravljenega zagona UI ali človeškega preverjanja.

## Kaj potrebujete

- [Paket besedilnega in jezikoslovnega preverjanja](../../../assets/downloads/text-nlp-validation-v1.zip)
  in [paket arhivskega trenja](../../../assets/downloads/archival-friction-v1.zip)
  z zapisi pravic, politike prepisovanja in izvora.
- Urejevalnik besedila ali dostopno orodje za tabele, bralnik PDF in mesto za
  ločeno hrambo prvotnih ter popravljenih izhodov.
- Raziskovalno vprašanje, kratek priročnik za presojo trditev in dogovor o
  razkritju ter dostopu. Plačljivega računa ali zunanjega modela ne potrebujete.

`TNLP-CLEAN-02` uporabite kot sintetični čisti kontrolni primer,
`TNLP-AF-REF` in `TNLP-AF-OCR` pa kot predstavitvi iste zgodovinske povedi,
ne neodvisna zgodovinska vira. Natančni izbori in kontrolne vsote so v
`raw/annotation-samples.csv`. Zgodovinsko mesto je `AF-OCR-P1-INTRO`, prva
stran PDF pod naslovom, poved z začetkom `Tudi danes`.

## Postopek

1. **Določite mejo.** Zapišite vprašanje in prepovejte nepodprto sklepanje o
   mnenju prebivalstva. Preberite zapise pravic in pred izbiro storitve
   prepoznajte omejeno dostopno gradivo. Če naročanje, zasebnost ali pogoji
   ponovne uporabe ostajajo nejasni, opravite vajo brez povezave z avtorsko
   simulacijo.
2. **Ohranite vhod.** Shranite izvorne datoteke in kontrolne vsote. Zapišite
   identifikatorje odlomkov, okoliško besedilo, normalizacijo, prevode in
   izpuste. Pri priklicu informacij ohranite različico indeksa in modela
   vektorskih vložitev, poizvedbo, delitev na odseke, filtre, razvrščanje,
   število izbranih odlomkov in njihov podani vrstni red.
3. **Zabeležite dogodek.** Ustrezna polja izpolnite pred izbirnim zagonom in
   med njim. Zapišite dejanski čas UTC in vrnjeni identifikator modela; imena
   izdelka ne uporabite namesto manjkajoče različice. Kadar je dovoljeno,
   ohranite navodila in zgodovino. Skrite ali nedostopne nastavitve izrecno
   označite.
4. **Ohranite predlog.** Shranite celoten neurejeni odgovor ali jasno označeno
   učno simulacijo. Dodelite stalni identifikator izhoda. Ohranite napake,
   zavrnitve in skrajšane izhode. Prvotnega besedila ne prepišite s popravljenim.
5. **Preverite trditve in izpuste.** Navedke znakovno primerjajte z ustrezno
   besedilno ravnijo, nato še s posnetkom. Ločeno preverite govorca, mesto,
   datum, obseg in nasprotne dokaze. Tudi resničen navedek je lahko napačno
   pripisan. Prevod preglejte ob slovenskem izvirniku.
6. **Preglejte odločitve.** Pri tej majhni vaji preverite vsako trditev. Če je
   druga oseba na voljo, naj jih presodi neodvisno; pred usklajevanjem
   ohranite obe odločitvi in razloga. Pri večji raziskavi določite naključni
   vzorec in skupine po jeziku, stanju OCR ter žanru, z identifikatorji in
   imenovalci. Če drugega bralca ni, pregled pošteno označite kot čakajoč.
7. **Popravite in poročajte.** Ohranite dnevnik popravkov, ožjo znanstveno
   trditev in izjavo o pomoči UI. Navedite, kaj je mogoče ponovno izvesti
   in kaj le pregledati. Poziv in ohranjeni izhod ne rekonstruirata umaknjenega
   gostovanega modela. Paket povežite z natančno različico objave, ki ga uporablja.

## Dokumentacijski zapis

Kopirajte in izpolnite zapis YAML. Strojni ključi so v obeh jezikih enaki.
`not_run` nadomestite šele po izvedbi. Za nedostopno informacijo uporabite
`unknown`, za zakrito pa `redacted` z razlogom in potjo do dovoljenega
dostopa. Prazni metapodatki nikoli samodejno ne pomenijo ničle. Dokler človeški
pregled še čaka, v poljih `reviewer`, `review_date` in `review_scope` ohranite
vrednost YAML `null`. Pred navedbo opravljenega pregleda vpišite ime osebe,
datum ISO (`YYYY-MM-DD`) in vsebinski opis pregledanega gradiva ter izvedenih
preverjanj. Poverilnic nikoli ne objavite.

```yaml
record_type: ai-analysis-audit
record_status: template
research_question: Kako uvodni odstavek oblikuje predstavo politične enotnosti?
provider: not_run
model_identifier: not_run
model_version_or_snapshot: not_run
run_time_utc: not_run
interface: not_run
system_instructions: not_run
user_instructions: not_run
parameters: not_run
retrieval_configuration: not_run
source_documents:
  - teaching-data/text-nlp-validation/raw/annotation-samples.csv
  - teaching-data/archival-friction/source/ilustrirani-slovenec-1925-02-07.pdf
passage_ids: [TNLP-CLEAN-02, TNLP-AF-REF, TNLP-AF-OCR]
preprocessing: Pred zagonom prepišite dokumentirani postopek izluščenja in zapise kontrolnih vsot.
truncation: not_run
output_path: not_run
correction_log: not_run
validation_sample: [TNLP-CLEAN-02, TNLP-AF-REF, TNLP-AF-OCR]
validation_protocol: Preglejte vse trditve; ohranite neodvisne presoje in zapis njihovega usklajevanja.
environment: not_run
cost: not_run
nondeterminism: unknown
unavailable_details: unknown
disclosure: Predloga ne beleži preizkusa modela; po izvedbi razkrijte nalogo, zapis zagona, obravnavano gradivo, preverjanja in odgovorne osebe.
review_status: pending_human_review
reviewer: null
review_date: null
review_scope: null
```

Polje `source_documents` določa izbrane vhode, ne podeljuje licence. V
spremljajoči register virov dodajte kontrolne vsote, različice in pogoje
dostopa. Pri dejanskem zagonu naj `cost` vsebuje valuto in znesek, `environment`
pa pomembne različice programske opreme in paketov, strojno opremo ter čas
izvajanja. Nedostopno okolje oddaljenega ponudnika ostaja neznano. Zakrivanje
omejuje javno preverljivost; omejitev opišite namesto obljube neomejene
reprodukcije.

Za vsako trditev ali pomemben izpust uporabite svojo vrstico:

| claim_id | original_output_id | claim_or_omission | source_id_and_locator | verdict | correction | consequence_for_argument | reviewer_and_date |
| --- | --- | --- | --- | --- | --- | --- | --- |
| izpolnite | izpolnite | izpolnite | izpolnite | pending | pending | pending | pending |

Predlagane razsodbe so `supported`, `partly_supported`, `unsupported_claim`,
`misattribution`, `quotation_error`, `locator_error`, `omission`, `unverifiable`.
Opredelite jih v priročniku in dovolite več oznak napak. Začetna nestrinjanja
pregledovalcev ohranite poleg končne razsodbe.

## Rezultat

Register virov, zapis zagona ali izrecno neizvedenega zagona, ohranjen predlog,
pregled trditev, dnevnik popravkov, vzorec preverjanja in izjava o pomoči UI.
Popravljena interpretacija naj trditev o enotnosti pripiše časopisu in odstrani
izmišljeno anketo. To so pričakovane učne odločitve, ne izmerjena uspešnost modela.

## Preverite se

- Ali lahko drug bralec najde vsak odlomek in loči OCR, referenčni prepis ter
  sintetični kontrolni primer?
- Ali lahko rekonstruirate podani kontekst oziroma ste označili neznano?
- Ali ste poleg dobesednosti navedkov preverili pripis in izpuste?
- Ali so dejanski človeški pregled, načrtovani pregled in pomoč UI razločljivi?
- Ali deleži navajajo imenovalec in pri ničelnem imenovalcu ostajajo nedoločeni?

## Pogoste pasti

- Model preverja samega sebe, pregledovalec pa nima vira.
- Mesto v viru ali tekoč prevod obravnavate kot dokaz utemeljenosti trditve.
- Prepišete prvotni izhod, zgodovino pozivov ali začetne odločitve pregledovalcev.
- Navedete reproducibilnost, čeprav ste ohranili le sledljivost.
- Zaradi prikaza preglednosti v dnevniku objavite zasebno izvorno gradivo.

## Naloga

Preverite simulacijo A01–A04 iz poglavja in napišite popravljeno interpretacijo
v 80 besedah. Zabeležite eno nestrinjanje z drugo osebo ali pojasnite, zakaj
pregled še čaka. Določite polje, ki bi pri gostovani storitvi ostalo neznano,
in omejitev trditve o reproducibilnosti. Naslednji preizkus zasnujte s
[postopkom omejene primerjave](compare-ai-output-across-prompts-models-and-runs.md).
