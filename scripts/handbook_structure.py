"""Canonical order and localized section labels for the stable handbook core."""
from __future__ import annotations

ORIENTATION = "index.md"
COURSE_PATHS = (
    "pismenost-za-informacijsko-druzbo.md",
    "digitalna-slovenistika.md",
)
PARTS = (
    (
        "what-is-digital-humanities.md",
        "history-of-digital-humanities.md",
        "models-evidence-interpretation.md",
        "critical-infrastructures.md",
        "digital-humanities-in-slovenia.md",
    ),
    (
        "research-design.md",
        "data-metadata-models.md",
        "texts-corpora-ocr.md",
    ),
    (
        "linguistic-annotation-classla.md",
        "text-analysis.md",
        "topics-emotions-classification.md",
        "databases-sql.md",
        "gis-spatial-humanities.md",
        "networks-visualization.md",
    ),
    (
        "ai-ethics-reproducibility.md",
        "open-living-handbook.md",
    ),
)
CHAPTERS = tuple(filename for part in PARTS for filename in part)

SECTION_LABELS = {
    "en": {
        "handbook": "Handbook",
        "orientation": "Orientation",
        "parts": (
            "Part I — Histories, theories and contexts",
            "Part II — Research design and sources",
            "Part III — Analytical methods",
            "Part IV — Responsible research and publication",
        ),
        "course_pathways": "Course pathways",
    },
    "sl": {
        "handbook": "Priročnik",
        "orientation": "Uvod",
        "parts": (
            "I. del — Zgodovine, teorije in konteksti",
            "II. del — Raziskovalna zasnova in viri",
            "III. del — Analitične metode",
            "IV. del — Odgovorno raziskovanje in objavljanje",
        ),
        "course_pathways": "Učne poti",
    },
}
