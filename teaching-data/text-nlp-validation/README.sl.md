---
translation_status: machine-assisted draft; requires human language review
---

# Učni paket za preverjanje besedilnih analiz in NLP

Raziskovalno vprašanje: kako se jezikoslovni in besedilnoanalitični sklepi
razlikujejo med dvema kratkima sintetičnima sodobnima primeroma, zgodovinskim
referenčnim prepisom in pripadajočo ponudnikovo različico OCR?

Dvojezični paket povezuje 9.–11. poglavje priročnika s preglednim dokaznim
gradivom. Vsebuje dvanajst kratkih sodobnih dokumentov, ki jih je priročnik
napisal za pouk, dokumentirane izvlečke iz obstoječega paketa o arhivskem
trenju, strojno podprti osnutek referenčne anotacije, ki čaka na človeški
pregled, zamrznjeni rezultat CLASSLA,
majhno vajo s frekvenco, dokumentno frekvenco in razpršenostjo ter omejeni vaji
o temah in čustvih. Sodobni dokumenti so sintetično učno gradivo in niso dokazi
o resničnih ustanovah ali dogodkih.

## Plasti

| Plast | Vloga | Pravilo |
| --- | --- | --- |
| `source/` | Avtorski učni korpus in register izvlečkov | Ohranite; register kaže na arhivsko gradivo, namesto da bi ga tukaj podvajal |
| `reference/` | Strojno podprti osnutki anotacije, kodirnih priročnikov in razlag | Obravnavajte jih kot gradivo, ki čaka na človeški pregled, ne kot neposredno resnico |
| `raw/` | Deterministično izvlečeni vhodi | Ponovno ustvarite; ne urejajte ročno |
| `interim/` | Zamrznjeni rezultati modelov CLASSLA in NMF | Ohranite kot dokaz izvedbe; osvežite jih samo z neobveznim ukazom in pregledom |
| `output/` | Mere po plasteh, dnevnik napak, konkordance in analitične tabele | Ponovno ustvarite s standardno knjižnico |
| `validation/` | Pričakovane vrednosti in manifest SHA-256 | Ponovno ustvarite po odobreni spremembi vira ali modela |
| `known-problems/` | Namenoma odprte omejitve | Dopolnite ob novi ugotovljeni omejitvi |

## Študentska pot

1. Preberite `rights-and-provenance.sl.md` in `data-dictionary.sl.md`.
2. Tri sloje v `raw/annotation-samples.csv` primerjajte z osnutkom reference in
   zamrznjenimi tabelami CLASSLA.
3. Ponovno izračunajte en imenovalec posamezne plasti v
   `output/classla-evaluation.csv`, nato dve napaki povežite z
   `output/classla-error-log.csv` in izvornim besedilom.
4. Z `output/frequency-dispersion.csv` in `output/concordance.csv` pojasnite,
   zakaj skupna frekvenca, dokumentna frekvenca in razpršenost odgovarjajo na
   različna vprašanja.
5. Pred previdno interpretacijsko tabelo preglejte ujemanje tem med naključnimi
   semeni in različnim številom sestavin.
6. Pregledno izhodišče čustvenih besed primerjajte s kontekstualnimi oznakami v
   osnutku, ki čaka na človeški pregled. Določite nosilca čustva, cilj, navedek,
   zanikanje in ironijo.

Študentska vaja ne zahteva prenosa modela. Uporabite datoteko
`text-nlp-validation-v1.zip` na strani priročnika ali to izvorno drevo.

## Ukazi za vzdrževanje

Običajno preverjanje uporablja samo standardno knjižnico Python in shranjene
rezultate modelov:

```bash
make text-nlp-validation
make check
```

Ponovni zagon modelov je ločen, ker prenese velike vire:

```bash
python3.12 -m venv .venv-text-nlp
source .venv-text-nlp/bin/activate
python -m pip install -r teaching-data/text-nlp-validation/requirements-text-nlp.txt
make text-nlp-validation-models
```

Ukaz za modele zapiše kandidate v novo mapo `.cache/` in ne prepiše potrjenih
dokazov. Primerjajte bajte in metapodatke, preglejte vsako spremenjeno anotacijo
ali temo ter šele nato v ločeni uredniški potrditvi zamenjajte zamrznjene
datoteke. Predpomnilnika modelov ne vključite v Git.

Zamrznjeni izvedbi kažeta na `interim/model-environment.json` in popolni zapis
`pip freeze --all`. Čas pridobitve virov CLASSLA je dokumentiran ločeno v
`interim/classla/resource-acquisition.json`: manifest datotek je znan, prvotni
čas pridobitve pa ostaja izrecno `unknown`.

## Meja interpretacije

Vzorec anotacije je namenski in majhen: razkrije napake, ne ocenjuje pa splošne
kakovosti CLASSLA ali populacijskega parametra. Tematski modeli uporabljajo
dvanajst kratkih sintetičnih dokumentov in ponazarjajo stabilnost; niso dokaz,
da teme obstajajo v zgodovinskem korpusu. Čustveni leksikon je izvirno majhno
učno izhodišče, ne slovenski čustveni vir. Metodološki in strokovni pregled
slovenščine še nista opravljena.
