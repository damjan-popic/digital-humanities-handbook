---
title: "Kako namestim in preizkusim CLASSLA s Pythonom 3.12?"
description: "Ustvarite čisto virtualno okolje, namestite CLASSLA, prenesite slovenski model in izvedite najmanjši preizkus."
category: "NLP"
difficulty: "začetno"
time: "30–60 min"
tags: [CLASSLA, Python, slovenščina, namestitev]
status: draft
translation_status: machine-assisted draft; requires human language review
---

# Kako namestim in preizkusim CLASSLA s Pythonom 3.12?

!!! warning "Stanje prevoda"
    Slovensko besedilo je strojno podprti uredniški osnutek. Pred formalno
    objavo potrebuje vsebinski in jezikovni pregled strokovnjaka za slovenščino.

<div class="answer-meta" markdown>
<span>NLP</span><span>začetno</span><span>30–60 min</span>
</div>

## Kaj želite doseči

Želite preverjeno okolje CLASSLA, preden začnete anotirati raziskovalno gradivo. Namestitev, prenos modela in najmanjši test naj bodo ločeni od glavnega projekta.

!!! quote "V eni povedi"
    Ustvarite virtualno okolje Python 3.12, namestite CLASSLA, prenesite slovenske vire in shranite uspešen najmanjši test.

## Potrebujete

- nameščen Python 3.12;
- ukazno vrstico;
- internetno povezavo za namestitev in prvi prenos modela;
- novo projektno mapo.

## Postopek

### 1. Ustvarite okolje

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

V Windows:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\activate
```

### 2. Namestite paket

```bash
python -m pip install --upgrade pip
python -m pip install classla
python -m pip freeze > requirements-lock.txt
```

### 3. Prenesite in preizkusite model

Ustvarite `test_classla.py`:

```python
import classla

classla.download("sl")
nlp = classla.Pipeline("sl", processors="tokenize,pos,lemma")
doc = nlp("Digitalna humanistika povezuje podatke in interpretacijo.")

for sentence in doc.sentences:
    for word in sentence.words:
        print(word.text, word.lemma, word.upos, sep="\t")
```

Zaženite:

```bash
python test_classla.py
```

### 4. Zabeležite okolje

Shranite različico Pythona, seznam paketov, datum prenosa modela in operacijski sistem. Velikih modelskih datotek ne dodajajte v Git, temveč dokumentirajte postopek pridobitve.

## Zabeležite in preverite nameščeno izvedbo

Zaklenjeni paket še ne določa prenesenih modelskih virov. Zabeležite različici
paketa in Pythona, seznam procesorjev, datum in mapo prenosa modela, nastavitev
CPU/GPU, zgoščene vrednosti vhodov in rezultatov ter razpoložljive zgoščene
vrednosti datotek virov. Prvi samodejni rezultat ohranite in ga ne prepišite s
popravki. Uspešna namestitev ni raziskovalno preverjanje; nadaljujte s postopkom
[vrednotenja CLASSLA na domensko specifičnem vzorcu](evaluate-classla-on-a-domain-specific-sample.md).

## Rezultat

Delujoče virtualno okolje, datoteka zaklenjenih različic in izpis slovenskih pojavnic, lem ter besednih vrst.

## Preverite se

- Ukaz `python --version` kaže 3.12?
- Izpis ohranja šumnike?
- Leme so smiselne?
- Lahko okolje izbrišete in obnovite iz navodil?

## Pogoste pasti

- pakete namestimo globalno;
- ukaza `pip` in `python` kažeta na različni okolji;
- model prenesemo v začasno mesto brez dokumentacije;
- prvi uspešen izpis zamenjamo za preverjanje kakovosti na raziskovalnem korpusu.

## Naloga

Okolje ustvarite znova v drugi mapi samo iz navodil in datoteke odvisnosti. Zabeležite vsako navodilo, ki je manjkalo.
