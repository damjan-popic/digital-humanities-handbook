---
title: "Kako z Gitom sledim manjšemu projektu?"
description: "V zavržljivem humanističnem projektu vadite cikel pregleda, priprave in potrditve."
category_id: "foundations"
category: "Osnove"
difficulty: "začetno"
time: "40–60 min"
tags: [Git, repozitorij, potrditev, veja, ponovljivost]
---

# Kako z Gitom sledim manjšemu projektu?

<div class="answer-meta" markdown>
<span>Osnove</span>
<span>začetno</span>
<span>40–60 min</span>
</div>

## Kaj želite doseči

Ohraniti želite razloge za spremembe v manjšem projektu opisovanja virov. Z Gitom boste spremembo pregledali, jo izbrali za naslednji posnetek in potrdili s pojasnilom.

To je krajevna vaja. Ne potrebujete GitHuba ali oddaljenega repozitorija.

## Dve različni izhodišči

- `git init` začne beležiti zgodovino v obstoječi krajevni projektni mapi.
- `git clone <url>` ustvari krajevno kopijo obstoječega repozitorija in zabeleži njegov oddaljeni naslov.

Ukazov ne uporabljajte kot zamenljivih nastavitev. V tej vaji uporabite `git init`, v povezanem sklepnem postopku pa `git clone`.

## Besedišče

| Izraz | Pomen |
| --- | --- |
| **Delovno drevo** | Datoteke, ki jih trenutno vidite v projektni mapi. |
| **Pripravljalno območje** | Predlagana vsebina naslednje potrditve. Posodobite ga z `git add`. |
| **Potrditev** | Shranjen posnetek z metapodatki in sporočilom. |
| **Veja** | Premično ime za zaporedje potrditev. |
| **Oddaljeni repozitorij** | Poimenovani naslov drugega repozitorija, pogosto `origin`. |
| **Pošiljanje (*push*)** | Pošiljanje krajevnih potrditev v oddaljeni repozitorij; s tem spremenite zunanje stanje. |
| **Pridobivanje in združevanje (*pull*)** | Pridobitev oddaljenega dela in njegova vključitev v trenutno vejo. |

## Postopek

### 1. Ustvarite zavržljiv projekt

```bash
mkdir -p ~/technical-practice/git-practice
cd ~/technical-practice/git-practice
printf '# Place-name notes\n\nA teaching project; no research claims yet.\n' > README.md
printf '.venv/\n__pycache__/\n*.pyc\n' > .gitignore
```

V `.gitignore` navedete vzorce nesledenih datotek, ki jih Git praviloma izpusti. Datoteka jih ne izbriše in že potrjenih datotek ne preneha slediti.

### 2. Inicializirajte in preglejte

```bash
git init
git status
```

Če ste nastavili `init.defaultBranch main`, je začetna veja `main`. Če ni, se ustavite in preglejte nastavitve, namesto da bi skozi predmetna navodila neopazno uporabljali drugo ime veje.

### 3. Preglejte prvo spremembo

```bash
git diff
git status --short
```

Nove nesledene datoteke se v običajnem `git diff` ne prikažejo; navede jih `git status`. Pred pripravo datoteki preberite:

```bash
cat README.md
cat .gitignore
```

### 4. Pripravite samo nameravani datoteki

```bash
git add README.md .gitignore
git diff --staged
git status
```

`git add` ne pomeni »naloži na splet«. Trenutno vsebino datoteke prekopira v pripravljalno območje. Če isto datoteko pozneje še uredite, sprememba ni pripravljena, dokler je znova ne dodate.

Če ste pred potrditvijo pripravili napačno sledeno datoteko, jo `git restore --staged <pot>` odstrani iz predlagane potrditve, ne da bi izbrisal delovno datoteko. Po vsakem ukazu za popravek preberite `git status`.

### 5. Potrdite z razlogom

```bash
git commit -m "Document the place-name practice project"
git status
git log --oneline --decorate
```

Uporabno sporočilo pojasni omejeni namen posnetka. Ni mu treba opisati vsakega pritiska tipke.

### 6. Ponovite kratki cikel

```bash
printf '\n## Source note\n\nThe sample list is synthetic and UTF-8 encoded.\n' >> README.md
git diff
git add README.md
git diff --staged
git commit -m "Record the source and encoding limits"
git log --oneline --decorate --max-count=3
```

Cikel je:

```text
sprememba → pregled → priprava → pregled pripravljene vsebine → potrditev → preverjanje
```

### 7. Varno ustvarite vejo

```bash
git switch -c notes/source-description
printf '\nNo personal data is included.\n' >> README.md
git diff
git add README.md
git diff --staged
git commit -m "Add a privacy note"
git switch main
git merge notes/source-description
git status
```

Veja je spremembi med pripravo dala ločeno ime. Združitev jo vključi v `main`. V tej začetni vaji veje ne izbrišete, ne prepisujete zgodovine in ne vsiljujete nobene posodobitve.

## Kaj spremenijo oddaljeni repozitoriji

Pregled oddaljenih naslovov je samo za branje:

```bash
git remote -v
```

Ta krajevni repozitorij nima oddaljenega naslova, če ga ne dodate. `git push` spremeni oddaljeni repozitorij, `git pull` pa oddaljeno delo vključi v krajevno vejo. Nobenega ukaza ne kopirajte, dokler ne poznate repozitorija, veje, dovoljenj in pravil sodelovanja. Vsiljeno pošiljanje, prepisovanje zgodovine in brisanje oddaljenih vej namenoma niso del tega postopka.

## Rezultat

Krajevni repozitorij z:

- dokumentiranim `.gitignore`;
- vsaj tremi majhnimi potrditvami;
- varno vajo z vejo, vključeno v `main`;
- čistim izpisom `git status`.

## Preverite se

```bash
git status
git log --oneline --decorate --all
git diff
git diff --staged
```

Zadnja ukaza ne smeta izpisati ničesar, ko se delovno drevo in pripravljalno območje ujemata z zadnjo potrditvijo.

## Česa Git ne nadomesti

- **Varnostnih kopij:** en repozitorij na enem disku lahko še vedno izgubite.
- **Licenc:** zgodovina ne podeljuje pravic do ponovne uporabe ali objave.
- **Dokumentacije:** sporočila potrditev ne nadomestijo README, podatkovnega slovarja ali opisa metode.
- **Etične presoje:** sledljiva škodljiva zbirka ostaja škodljiva.
- **Interpretacije:** Git beleži spremembe, ne pomena dokazov.

Pretvorbe koncev vrstic ali kodiranja lahko ustvarijo videz, da se je spremenila celotna besedilna datoteka. Pred potrditvijo preglejte razliko in preverite, ali sta vsebina UTF-8 ter nameravani konci vrstic ohranjeni.

## Pogoste pasti

- uporabite `git add .`, ne da bi preverili izbrane datoteke;
- domnevate, da se nesledene datoteke prikažejo v `git diff`;
- potrdite `.venv/`, poverilnice, zasebne podatke ali velike izpeljane datoteke;
- potrditev zamenjate z varnostno kopijo ali pošiljanjem;
- delate na napačni veji, ker ste izpustili `git status`;
- čisto zgodovino Gita obravnavate kot dokaz zakonite ali etične raziskave.

## Naloga

Dodajte `sources.md` z enim sintetičnim opisom vira in opombo o pravicah. Uporabite celoten cikel sprememba → pregled → priprava → pregled → potrditev. Oddajte `git log --oneline --decorate --all` in pojasnite, kateri dokazi ostajajo zunaj Gita.

## Preverjeni viri

Dostopano **23. julija 2026**:

- [Pro Git: pridobitev repozitorija Git](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)
- [Pro Git: beleženje sprememb](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
- [Pro Git: delo z oddaljenimi repozitoriji](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
- [referenčna dokumentacija Git](https://git-scm.com/docs)

Celotno zaporedje za repozitorij in vejo smo preizkusili z Gitom 2.43 v novoustvarjeni zavržljivi mapi. Oddaljenega repozitorija nismo spreminjali, zgodovine nismo prepisovali in ničesar nismo vsiljeno poslali ali oddaljeno izbrisali.
