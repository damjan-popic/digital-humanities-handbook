---
title: "Kako v lupini Bash uporabim cevovode, preusmerjanje in grep?"
description: "Zgradite in preglejte majhen dokumentiran cevovod za obdelavo besedila."
category_id: "foundations"
category: "Osnove"
difficulty: "začetno"
time: "30–45 min"
tags: [Bash, cevovodi, preusmerjanje, grep, besedilo]
---

# Kako v lupini Bash uporabim cevovode, preusmerjanje in grep?

<div class="answer-meta" markdown>
<span>Osnove</span>
<span>začetno</span>
<span>30–45 min</span>
</div>

## Kaj želite doseči

Prešteti in filtrirati želite majhen seznam krajevnih omemb ter ohraniti korake, ki so ustvarili rezultat. Cevovod je dokumentirana pretvorba od vhoda do izhoda, ne čarobno ločilo in ne interpretacija virov.

Postopek izvedite v lupini Bash v zavržljivi mapi `~/technical-practice/`.

## Trije tokovi

Večina programov v ukazni vrstici uporablja:

- **standardni vhod** (`stdin`): podatke, ki jih ukaz bere;
- **standardni izhod** (`stdout`): običajne rezultate;
- **standardni izhod za napake** (`stderr`): diagnostična sporočila in napake.

Izhod in napake se privzeto izpišejo v terminalu. Bash jih lahko poveže ali preusmeri, vendar morate napake pregledati in jih ne smete zgolj skriti.

## Postopek

### 1. Ustvarite majhen humanistični vhod

```bash
cd ~/technical-practice
mkdir -p pipeline-practice/texts
cd pipeline-practice
printf 'Ljubljana\nMaribor\nLjubljana\nCelje\nMaribor\nLjubljana\n' > "place mentions.txt"
cat "place mentions.txt"
```

Vhod je učni vzorec, ne dokaz o resničnem korpusu.

### 2. Izhod preusmerite v novo datoteko

```bash
grep 'Ljubljana' "place mentions.txt" > "Ljubljana mentions.txt"
cat "Ljubljana mentions.txt"
```

`>` pošlje standardni izhod v datoteko in **nadomesti datoteko, če že obstaja**. Pred uporabo na pomembnem gradivu preverite cilj.

Zabeležko o provenienci pripnite, ne da bi nadomestili obstoječi rezultat:

```bash
printf '# filtered from place mentions.txt\n' >> "pipeline notes.txt"
```

`>>` pripenja. Zato operacija še ni pravilna; preverite, ali ste po pomoti večkrat pripeli isto vsebino.

### 3. Ukaza povežite s cevjo

```bash
grep 'Ljubljana' "place mentions.txt" | wc -l
```

`grep` zapiše ujemajoče se vrstice na standardni izhod. `|` ta izhod poveže s standardnim vhodom `wc -l`, ki prešteje vrstice. Pričakovani rezultat:

```text
3
```

To je opis treh ujemajočih se vrstic, ne razlaga, zakaj je omenjena Ljubljana.

### 4. Pred štetjem enoličnih vrednosti razvrstite vrstice

```bash
sort "place mentions.txt" | uniq -c
```

Pričakovani izpis:

```text
      1 Celje
      3 Ljubljana
      2 Maribor
```

`uniq` združi samo sosednje enake vrstice, zato je `sort` nujni dokumentirani korak. Sprememba velikosti črk, zapisa ali diakritičnih znamenj spremeni štetje; razreševanje krajevnih imen ostaja raziskovalna odločitev.

Rezultat shranite:

```bash
sort "place mentions.txt" | uniq -c > "place counts.txt"
cat "place counts.txt"
```

### 5. Vzorce in imena datotek pravilno navedite

```bash
grep -i 'ljubljana' "place mentions.txt"
grep 'Mari.*' "place mentions.txt"
```

Vzorec za `grep` zapišite v narekovajih, da njegovega ločila najprej ne razloži Bash. Ime datoteke s presledki navedite v narekovajih, da ostane en argument.

**Datotečni vzorec** oziroma *glob* je drugačen: Bash ga pred zagonom ukaza razširi v ujemajoče se poti.

```bash
cp "place mentions.txt" texts/places-1.txt
cp "place mentions.txt" texts/places-2.txt
head -n 1 texts/*.txt
```

Celotnega vzorca `texts/*.txt` ne zapišite v narekovajih, kadar želite razširitev. Pred uporabo vzorca z ukazom, ki spreminja datoteke, ujemanja preglejte s `printf '%s\n' texts/*.txt`.

### 6. Pri diagnosticiranju ločite napake

Naslednji ukaz se v zavržljivi mapi namenoma sklicuje na manjkajočo datoteko:

```bash
cat "missing source.txt" > output.txt 2> errors.log
cat errors.log
```

`2>` preusmeri standardni izhod za napake. Neuspešni ukaz lahko kljub temu ustvari prazen `output.txt`, ker Bash najprej odpre preusmeritev. Preden datoteko obravnavate kot rezultat, preverite sporočilo ukaza in vsebino izhoda.

## Rezultat

- `Ljubljana mentions.txt`;
- `place counts.txt`;
- kratka zabeležka o provenienci;
- `errors.log`, ki pokaže razliko med napako in običajnim izhodom.

## Preverite se

```bash
wc -l "place mentions.txt"
wc -l "Ljubljana mentions.txt"
cat "place counts.txt"
cat errors.log
```

Pričakovano število vhodnih vrstic je 6, filtriranih pa 3.

## Pogoste pasti

- uporabite `>`, ko ste nameravali uporabiti `>>`, in nadomestite datoteko;
- domnevate, da `uniq -c` brez `sort` združi nesosednje vrednosti;
- vzorca ne zapišete v narekovajih in ga razširi Bash;
- datotečni vzorec, ki bi ga moral Bash razširiti, zapišete v narekovajih;
- pogostost obravnavate kot razlago;
- standardnega izhoda za napake ne pregledate, ker izhodna datoteka obstaja.

## Naloga

Kopiji vhoda dodajte dve krajevni omembi. Zapišite štiri ukaze, ki:

1. filtrirajo en kraj;
2. preštejejo ujemajoče se vrstice;
3. izdelajo razvrščeno frekvenčno tabelo;
4. rezultate shranijo pod novimi, opisnimi imeni.

Zabeležite ime vhodne datoteke, natančne ukaze in stavek o tem, česa štetje **ne** dokazuje.

## Preverjeni viri

Dostopano **23. julija 2026**:

- [GNU Bash Reference Manual: cevovodi in preusmeritve](https://www.gnu.org/software/bash/manual/bash.html)
- [priročnik GNU Grep](https://www.gnu.org/software/grep/manual/grep.html)
- [priročnik GNU Coreutils](https://www.gnu.org/software/coreutils/manual/coreutils.html)

Celotno zaporedje smo preizkusili v novoustvarjeni zavržljivi mapi z GNU Bash 5.2.21, GNU grep in GNU coreutils v Ubuntuju 24.04 pod WSL 2.
