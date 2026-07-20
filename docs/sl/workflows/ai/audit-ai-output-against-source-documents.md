---
title: "Kako rezultat UI preverim ob izvornih dokumentih?"
description: "Vsako dejansko trditev, navedek in izpust generiranega povzetka povežite s preverljivim dokazom."
category: "UI"
difficulty: "začetno"
time: "45–90 min"
tags: [UI, preverjanje, viri, halucinacije]
---

# Kako rezultat UI preverim ob izvornih dokumentih?

<div class="answer-meta" markdown>
<span>UI</span><span>začetno</span><span>45–90 min</span>
</div>

## Kaj želite doseči

Model je povzel enega ali več dokumentov. Želite ločiti podprte trditve, napačne povezave, izmišljene navedke in pomembne izpuste.

## Postopek

1. Ohranite točni model, datum, poziv, parametre in vhodni kontekst.
2. Generirani tekst razdelite na najmanjše preverljive trditve.
3. Za vsako trditev poiščite odlomek, identifikator in stran ali označite »brez podpore«.
4. Navedke primerjajte znak za znakom; parafraze ne predstavljajte kot navedek.
5. Zabeležite protislovne in manjkajoče dokaze.
6. Druga oseba naj pregleda vsaj naključni vzorec odločitev.
7. Popravljeni izhod objavite skupaj z omejitvami ali ga zavrnite, če napake niso obvladljive.

## Revizijska tabela

| claim_id | generated_claim | source_id | passage | verdict | correction | reviewer |
|---|---|---|---|---|---|---|

Možne razsodbe naj bodo vnaprej določene, denimo `podprto`, `delno`, `napačno`, `brez vira`, `nepreverljivo`.

## Rezultat

Revizijska tabela, popravljeni povzetek in ponovljiv zapis uporabe modela.

## Preverite se

- Ima vsaka dejanska trditev vir?
- So vsi navedki dobesedni in pravilno pripisani?
- Je model združil dve osebi ali dogodka?
- So pomembni nasprotni dokazi izpuščeni?
- Bi drug pregledovalec z istimi pravili prišel do podobne razsodbe?

## Pogoste pasti

- model prosimo, naj preveri lastni rezultat, brez dostopa do virov;
- tekoč slog zamenjamo za zanesljivost;
- spletne naslove ali bibliografijo sprejmemo brez preverjanja;
- popravljeni rezultat objavimo brez razkritja postopka;
- preverimo le najbolj očitne trditve.

## Naloga

Preverite povzetek z najmanj desetimi trditvami. Izračunajte delež podprtih trditev, opišite tri vrste napak in napišite pravilo, kdaj bi uporabo modela pri tej nalogi ustavili.
