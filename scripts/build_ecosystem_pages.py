#!/usr/bin/env python3
"""Generate bilingual ecosystem overview pages from intertextuality.yml."""
from __future__ import annotations

import hashlib
from pathlib import Path

from handbook_structure import CHAPTERS
from intertextuality import MAP_PATH, ROOT, load_map, page_title


def link(locale: str, path: str) -> str:
    title, fallback = page_title(locale, path)
    suffix = ""
    if fallback:
        suffix = " *(angleška nadomestna stran)*" if locale == "sl" else " *(English fallback)*"
    return f"[{title}]({path}){suffix}"


def build(locale: str) -> str:
    data = load_map()
    digest = hashlib.sha256(MAP_PATH.read_bytes()).hexdigest()
    sl = locale == "sl"
    title = "Ekosistem priročnika" if sl else "Handbook ecosystem"
    description = (
        "Povezave med poglavji, praktičnimi postopki, študijami primerov in učnimi potmi."
        if sl
        else "Connections among chapters, practical workflows, case studies, and learning paths."
    )

    out = [
        "---",
        f'title: "{title}"',
        f'description: "{description}"',
        "tags: [ecosystem, navigation, workflows, case-studies]",
        "---",
        "",
        f"# {title}",
        "",
    ]

    if sl:
        out.extend(
            [
                "Priročnik ni sestavljen iz štirih ločenih polic. Poglavja podajajo pojme in argumente, praktični postopki jih pretvorijo v preverljive naloge, študije primerov pokažejo večje raziskovalne sestave, učni poti pa iz vseh treh plasti oblikujeta predmeta. Povezave na posameznih straneh nastajajo iz istega verzioniranega zemljevida, zato jih je mogoče pregledati in preveriti.",
                "",
                "## Kako se premikate po ekosistemu",
                "",
                "1. Začnite z omejenim humanističnim vprašanjem v [jedru priročnika](chapters/index.md).",
                "2. Izberite praktični postopek, ki izdela pregleden rezultat.",
                "3. Primerjajte ga s študijo primera, v kateri je metoda del večjega projekta.",
                "4. Vrnite se k poglavju ter preverite, kaj rezultat lahko pomeni in česa ne more dokazati.",
                "5. Za poučevanje uporabite [Pismenost za informacijsko družbo](learning-paths/pismenost-za-informacijsko-druzbo.md) ali [Digitalno slovenistiko](learning-paths/digitalna-slovenistika.md).",
                "",
                "## Od poglavij k praksi",
                "",
                "| Poglavje | Izbrani praktični postopki | Študije primerov |",
                "| --- | --- | --- |",
            ]
        )
    else:
        out.extend(
            [
                "The handbook is not four separate shelves. Chapters provide concepts and arguments, workflows turn them into inspectable tasks, case studies show larger research assemblies, and learning paths organize all three layers into courses. Page-level connections are generated from one versioned relation map, so the ecosystem remains auditable.",
                "",
                "## How to move through the ecosystem",
                "",
                "1. Begin with a bounded humanities question in the [handbook core](chapters/index.md).",
                "2. Choose a workflow that produces an inspectable output.",
                "3. Compare it with a case study where the method participates in a larger project.",
                "4. Return to the chapter to ask what the output can mean and what it cannot establish.",
                "5. For teaching, use [Information Society Literacy](learning-paths/pismenost-za-informacijsko-druzbo.md) or [Digital Slovenian Studies](learning-paths/digitalna-slovenistika.md).",
                "",
                "## From chapters to practice",
                "",
                "| Chapter | Selected workflows | Case studies |",
                "| --- | --- | --- |",
            ]
        )

    for filename in CHAPTERS:
        chapter_path = f"chapters/{filename}"
        entry = data["chapters"][chapter_path]
        workflows = "<br>".join(link(locale, p) for p in entry["workflows"])
        cases = "<br>".join(link(locale, p) for p in entry["case_studies"])
        out.append(f"| {link(locale, chapter_path)} | {workflows} | {cases} |")

    if sl:
        out.extend(
            [
                "",
                "## Povezave delujejo v obe smeri",
                "",
                "Vsak praktični postopek se poveže s poglavji, ki pojasnijo njegove predpostavke, in s študijami primerov, kjer je povezava dejansko smiselna. Vsaka študija primera se poveže nazaj s pojmovnimi poglavji in izvedljivimi postopki. Tako praktična stran ni golo navodilo, študija primera pa ni slepa ulica.",
                "",
                "## Jeziki in nadomestne strani",
                "",
                "Stabilno jedro in učni poti so v celoti dvojezični. Kadar slovenski prevod praktičnega postopka ali študije primera še ne obstaja, povezava vodi na angleško nadomestno stran in je kot taka označena. To omogoča uporabo celotnega ekosistema, ne da bi neprevedeno stran prikazali kot dokončan slovenski prevod.",
            ]
        )
    else:
        out.extend(
            [
                "",
                "## Connections work in both directions",
                "",
                "Every workflow points back to chapters that explain its assumptions and, where genuinely relevant, to case studies that use related operations. Every case study points to conceptual chapters and executable workflows. A practical page is therefore more than an instruction sheet, and a case study is not a dead end.",
                "",
                "## Languages and fallback pages",
                "",
                "The stable core and learning paths are fully bilingual. When a Slovene workflow or case-study translation does not yet exist, the Slovene edition links to a clearly marked English fallback page. This keeps the whole ecosystem usable without presenting untranslated material as a completed Slovene translation.",
            ]
        )

    out.extend(["", f"<!-- intertextuality-map-sha256:{digest} -->", ""])
    return "\n".join(out)


def main() -> None:
    for locale in ("en", "sl"):
        target = ROOT / "docs" / locale / "ecosystem.md"
        target.write_text(build(locale), encoding="utf-8")
        print(f"Wrote {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
