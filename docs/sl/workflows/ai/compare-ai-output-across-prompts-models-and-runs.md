---
title: "Kako primerjam izhode UI med pozivi, modeli in zagoni?"
description: "Preverite, ali sklep iz virov vzdrži nadzorovane spremembe, ter razvrstite razlike, ki vplivajo na argument."
category: "UI"
category_id: AI
difficulty: "srednje zahtevno"
time: "90–150 min"
tags: [UI, robustnost, vrednotenje, kritika-virov, negotovost]
status: draft
translation_status: machine-assisted draft; requires human language review
---

# Kako primerjam izhode UI med pozivi, modeli in zagoni?

## Kaj želite doseči

Ugotoviti želite, ali povzetek ob spremembi poziva, vrstnega reda virov ali
modela ohrani podatek, kdo izreka zgodovinsko trditev. To je omejena vaja
robustnosti, ne lestvica splošno najboljših modelov. Preberite poglavje
[UI, etika in ponovljivost](../../chapters/ai-ethics-reproducibility.md)
in najprej opravite
[pregled virov in zapisa zagona](document-and-audit-a-source-grounded-ai-analysis.md).

Postopek je strojno podprti osnutek, ki čaka na človeški pregled. Predlaga osem
klicev modela, poroča pa o **nič dejanskih zagonih**. Različica vaje brez
povezave uporablja avtorske simulacije in ne dokazuje uspešnosti modela.

## Kaj potrebujete

- [Paket besedilnega in jezikoslovnega preverjanja](../../../assets/downloads/text-nlp-validation-v1.zip)
  in [paket arhivskega trenja](../../../assets/downloads/archival-friction-v1.zip)
  z zapisi pravic in izvora.
- Tri identifikatorje odlomkov: `TNLP-CLEAN-02` (sintetični kontrolni primer),
  `TNLP-AF-REF` in `TNLP-AF-OCR` (predstavitvi iste zgodovinske povedi).
- Tabelo preverjanja, register virov in čas za branje. Če se odločite za
  zagone, uporabite le odobrene storitve; brez povezave računa ne potrebujete.

Vprašanje je, kako uvodni odstavek oblikuje predstavo politične enotnosti.
Zgodovinsko mesto je `AF-OCR-P1-INTRO`, prva stran PDF pod naslovom, poved
z začetkom `Tudi danes`. Ročna izhodiščna obravnava naj izpiše govorca,
trditev o enotnosti, ponujene dokaze in potrebno omejitev. Pripravite jo
pred branjem povzetkov UI, da zmanjšate vpliv prvega prikazanega odgovora.
Izhodiščna obravnava je predlagana naloga, ne opravljena človeško pregledana
referenca.

## Postopek

1. **Določite primerjavo.** Ohranite iste različice virov, identifikatorje
   odlomkov, nalogo in obliko izhoda. P0 zahteva: »Za vsak odlomek določite
   govorca, povzemite trditev, navedite identifikator odlomka in pojasnite,
   česa vir ne dokazuje. Ne dodajajte dokazov.« P1 spremeni le prvo navodilo
   v »Za vsak odlomek ločite trditev publikacije od ugotovitve o njenem
   občinstvu«, preostale zahteve pa ohrani.
2. **Opredelite pogoje.** C0 uporablja P0, M1 in prvotni vrstni red; C1
   spremeni le poziv v P1; C2 spremeni le vrstni red v obratnega; C3 spremeni
   le model v M2. M1 in M2 sta mesti za dejanska identifikatorja modelov,
   ne imeni izdelkov. Parametre določite, kjer je to mogoče, nedostopne
   nastavitve pa zapišite. Uporabite svež kontekst brez prejšnjih odgovorov.
3. **Načrtujte dve ponovitvi na pogoj.** Vsak klic prejme vse tri jasno
   označene odlomke in vrne ločene zapise zanje. Štirje pogoji z dvema
   ponovitvama pomenijo osem načrtovanih klicev. Pri vsakem dejanskem klicu
   shranite čas, identifikator modela, konfiguracijo in izhod, tudi ob
   zavrnitvi ali napaki. Drugi model lahko zahteva drugega ponudnika;
   pred pošiljanjem preverite njegovo ureditev podatkov. Če ni na voljo,
   C3 označite z `not_run` in omejite trditev, ne dokumentacije.
4. **Preglejte brez imen modelov.** Izhodom dodelite identifikatorje in med
   prvim branjem po možnosti skrijte pogoje. Vsako pomembno trditev primerjajte
   z virom in ročno izhodiščno obravnavo. Sintetični kontrolni primer ločite
   od zgodovinskega besedila; zgodovinski predstavitvi sta povezani, ne
   neodvisni opazovanji za statistično sklepanje. Ker sta referenčni prepis
   in OCR vidna skupaj, preverjate uporabo povezanih dokazov, ne uspešnosti
   na samem OCR. Za preizkus z ločenimi vhodi določite nov načrt in obseg stroškov.
5. **Razvrstite razlike.** Uporabite spodnjo tipologijo. Spremenjen pridevnik
   ni samodejno raziskovalna razlika, lahko pa postane, če spremeni gotovost.
   Slovenski izvirnik primerjajte z angleško parafrazo; tekoča angleščina
   ni referenca pravilnosti. Preglejte tudi izpuste in zavrnitve.
6. **Uskladite presoje in odločite.** Kadar je mogoče, ohranite neodvisne
   odločitve pregledovalcev, razloge, končno rešitev in odprte primere.
   V vsaki skupini ločeno štejte napake in pregledane trditve. Poročajte
   o številih, pokritosti in manjkajočih pogojih. Dve ponovitvi ne zadoščata
   za oceno stabilne porazdelitve uspešnosti ali trditev o statistični značilnosti.
7. **Pojasnite mejo.** Navedite, katere spremembe vplivajo na zgodovinski
   argument in ali metoda izpolnjuje merilo sprejemljivosti. Poziva, izbranega
   po ogledu rezultatov, ne predstavite kot neodvisno preverjenega. Trditve
   o uspešnosti popravljenega poziva zahtevajo nov izločen vzorec preverjanja.

## Načrt primerjave

Kopirajte zapis in v obeh jezikih ohranite strojne ključe. Predlagani proračun
je učna zgornja meja, ne dovoljenje za nastanek stroškov. Pred izbirnimi
plačljivimi klici zagotovite ustrezno dovoljeno ureditev, sicer uporabite vajo
brez povezave. Vsak dejanski zagon potrebuje celoten zapis izvora iz povezanega
postopka. Ločite `unknown`, `redacted` z razlago in `not_run`. Pred oznako
opravljenega človeškega pregleda navedite resnična imena, datume ISO in obseg.

```yaml
record_type: ai-robustness-plan
record_status: template
research_question: Does the summary preserve attribution and uncertainty?
source_documents:
  - teaching-data/text-nlp-validation/raw/annotation-samples.csv
  - teaching-data/archival-friction/source/ilustrirani-slovenec-1925-02-07.pdf
passage_ids: [TNLP-CLEAN-02, TNLP-AF-REF, TNLP-AF-OCR]
baseline: Manual extraction of speaker, claim, evidence and qualification; pending.
conditions:
  - {condition_id: C0, prompt: P0, model: M1, source_order: original}
  - {condition_id: C1, prompt: P1, model: M1, source_order: original}
  - {condition_id: C2, prompt: P0, model: M1, source_order: reversed}
  - {condition_id: C3, prompt: P0, model: M2, source_order: original}
planned_runs: 8
actual_runs: 0
run_records: []
consequential_difference_taxonomy:
  - attribution
  - evidence
  - uncertainty
  - omission
  - translation
  - abstention
  - style_only
validation_strata:
  - {stratum: synthetic_clean, passage_ids: [TNLP-CLEAN-02]}
  - {stratum: historical_reference, passage_ids: [TNLP-AF-REF]}
  - {stratum: historical_ocr, passage_ids: [TNLP-AF-OCR]}
validation_sample: [TNLP-CLEAN-02, TNLP-AF-REF, TNLP-AF-OCR]
adjudication: Preserve initial decisions, source reasons, final decisions and disagreement.
acceptance_rule: No invented evidence or population claim in any publishable candidate.
stop_rule: Stop at the budget limit or an unresolved privacy or rights problem.
budget:
  maximum_model_calls: 8
  maximum_paid_cost_eur: 5
  maximum_review_minutes: 120
  actual_cost: not_run
  energy_measurement: unknown
results_status: not_run
review_status: pending_human_review
reviewer: pending
review_date: pending
review_scope: pending
```

## Razlike, ki vplivajo na sklep

| Kategorija | Kaj primerjate | Zakaj je pomembno |
| --- | --- | --- |
| `attribution` | Kdo kaj zatrjuje ali doživlja? | Strankarska trditev lahko postane napačna ugotovitev o prebivalstvu |
| `evidence` | Dodana, spremenjena ali odsotna podpora; navedek in mesto | Izmišljena anketa spremeni podlago argumenta |
| `uncertainty` | Omejitve, gotovost in obseg | Možna razlaga lahko postane neupravičeno dejstvo |
| `omission` | Manjkajoči nasprotni dokazi ali kontekst | Navidezno pravilna poved lahko skriva zavajajoč izbor |
| `translation` | Pomen in politični glas med jeziki | Gladko napisana parafraza lahko izbriše stališče izvirnika |
| `abstention` | Zavrnitev, delni odgovor ali izrecno neznano | Pokritost se spremeni, morda neenakomerno po skupinah |
| `style_only` | Ubeseditev ob enakih dokazih, pripisu in obsegu | Raziskovalna trditev lahko ostane enaka |

Za vsak odlomek in par identifikatorjev izhodov uporabite svojo vrstico:

| passage_id | output_ids | difference_tags | source_locator | consequence | reviewer_decisions | final_treatment |
| --- | --- | --- | --- | --- | --- | --- |
| izpolnite | izpolnite | izpolnite | izpolnite | izpolnite | pending | pending |

## Rezultat

Opredeljen načrt, vsi zapisi dejanskih zagonov, izhodiščna obravnava s stanjem
pregleda, tabela parnih razlik in omejen sklep. Vključite dejanske in
načrtovane klice ter manjkajoče pogoje. Predlog za objavo z izmišljenimi dokazi
zavrnite ali popravite; sama ta odločitev še ne dokazuje robustnosti modela.
Če ste pregledali le simulacije, poročajte o vaji preverjanja brez rezultatov
modela.

## Preverite se

- Ali vsaka primerjava spremeni samo napovedani dejavnik?
- Ali so vključeni neuspešni klici in zavrnitve ter ločeni števili napak in pokritosti?
- Ali ste v vsaki skupini pregledali vire, tudi težaven OCR in slovenščino?
- Ali so pomembne razlike povezane z zgodovinskim argumentom?
- Ali ste se izognili obravnavi povezanih predstavitev kot neodvisnih virov?
- Ali ste dejanske stroške in nedostopne podrobnosti okolja zapisali pošteno?

## Pogoste pasti

- Hkrati primerjate različne naloge, dolžine konteksta in modele.
- Soglasje modelov imenujete neodvisna potrditev zgodovinske trditve.
- Poročate samo o najboljšem odgovoru ali skrivate neizvedene pogoje.
- Dve uspešni ponovitvi zamenjate za zanesljivo populacijsko oceno.
- Sintetične primere ali nedokončan človeški pregled predstavljate kot merilo uspešnosti.

## Naloga

Brez povezave napišite tri jasno označene različice simulacije iz poglavja:
prva spremeni le slog, druga odstrani pripis, tretja pa ponovno uvede
negotovost. Razvrstite jih in pojasnite spremembe znanstvenih trditev.
Ohranite `actual_runs: 0` in vajo opišite ločeno; avtorskega besedila ne
vpisujte med zagone modela. Če imate odobren dostop, namesto tega izvedite
načrtovane klice in ohranite vsak rezultat. Na koncu podajte utemeljen sklep
in vprašanje, na katero primerjava ne more odgovoriti.
