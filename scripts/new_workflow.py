#!/usr/bin/env python3
"""Create a localized workflow page from the handbook template."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    "terminology", "cat-tools", "subtitling", "automation", "nlp", "corpora", "pdf",
    "visualization", "mt-eval", "audio", "publishing", "data-wrangling", "editions",
    "mapping", "ai", "ethics", "text-analysis", "data", "networks",
}


def slugify(text: str) -> str:
    text = text.casefold()
    replacements = {"č": "c", "š": "s", "ž": "z"}
    for a, b in replacements.items():
        text = text.replace(a, b)
    text = re.sub(r"^(how do i|kako)\s+", "", text)
    return re.sub(r"(^-|-$)", "", re.sub(r"[^a-z0-9]+", "-", text)) or "new-workflow"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("title")
    parser.add_argument("--lang", choices=["en", "sl"], default="en")
    parser.add_argument("--category", required=True, choices=sorted(CATEGORIES))
    parser.add_argument("--difficulty", default=None)
    parser.add_argument("--time", default="30–60 min")
    parser.add_argument("--tags", default="")
    args = parser.parse_args()

    title = args.title.strip()
    if args.lang == "en" and not title.lower().startswith("how do i"):
        title = f"How do I {title[0].lower() + title[1:]}"
    if args.lang == "sl" and not title.lower().startswith("kako"):
        title = f"Kako {title[0].lower() + title[1:]}"
    if not title.endswith("?"):
        title += "?"
    difficulty = args.difficulty or ("beginner" if args.lang == "en" else "začetno")
    tags = ", ".join(t.strip() for t in args.tags.split(",") if t.strip()) or args.category
    path = ROOT / "docs" / args.lang / "workflows" / args.category / f"{slugify(title)}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise SystemExit(f"Refusing to overwrite {path.relative_to(ROOT)}")

    if args.lang == "en":
        body = f'''---
title: "{title}"
description: "Replace with a one-sentence summary."
category: "{args.category}"
difficulty: "{difficulty}"
time: "{args.time}"
tags: [{tags}]
---

# {title}

<div class="answer-meta" markdown>
<span>{args.category}</span><span>{difficulty}</span><span>{args.time}</span>
</div>

## What you are trying to do

Explain the practical situation and the research meaning of the output.

## You need

- A small input sample
- A documented tool or script
- A validation rule

## Workflow

1. Preserve the source and identifiers.
2. Run the smallest useful example.
3. Inspect and validate the output.
4. Scale only after the sample works.

## Output

Name the files, fields and interpretation produced.

## Check yourself

- Can every result be traced to evidence?
- What would count as failure?

## Common traps

- Hiding a consequential default.
- Scaling before validation.

## Practice task

Add a small reproducible exercise.
'''
    else:
        body = f'''---
title: "{title}"
description: "Zamenjajte z enopovednim povzetkom."
category: "{args.category}"
difficulty: "{difficulty}"
time: "{args.time}"
tags: [{tags}]
---

# {title}

<div class="answer-meta" markdown>
<span>{args.category}</span><span>{difficulty}</span><span>{args.time}</span>
</div>

## Kaj želite doseči

Pojasnite praktično situacijo in raziskovalni pomen rezultata.

## Potrebujete

- Majhen vhodni vzorec
- Dokumentirano orodje ali skripto
- Pravilo preverjanja

## Postopek

1. Ohranite vir in identifikatorje.
2. Izvedite najmanjši uporabni primer.
3. Preglejte in preverite rezultat.
4. Obseg povečajte šele po uspešnem vzorcu.

## Rezultat

Poimenujte datoteke, polja in interpretacijo.

## Preverite se

- Lahko vsak rezultat povežete z dokazom?
- Kaj bi štelo kot odpoved?

## Pogoste pasti

- Skrijemo pomembno privzeto nastavitev.
- Obseg povečamo pred preverjanjem.

## Naloga

Dodajte majhno ponovljivo vajo.
'''
    path.write_text(body, encoding="utf-8")
    print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
