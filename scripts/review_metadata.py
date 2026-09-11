"""Shared structural checks for claimed human reviews, not review authentication."""
from __future__ import annotations

import re
import unicodedata
from datetime import date

REVIEW_PLACEHOLDERS = {
    "pending", "unknown", "not run", "redacted", "tbd", "todo", "null", "none",
    "nil", "n a", "na", "nan", "not applicable", "unavailable", "withheld",
    "undetermined", "unassigned", "not reviewed", "not selected", "placeholder",
    "to be determined", "to be reviewed", "to be assigned", "fill in",
    "v čakanju", "na čakanju", "čaka", "čakajo", "čakajoč", "čakajoča", "čakajoče",
    "v teku", "neznano", "neznan", "neznana", "ni znano", "ni podatka",
    "ni podatkov", "ni določeno", "ni navedeno", "ni izvedeno", "ni pregledano",
    "neizvedeno", "neizveden", "neizvedena", "zakrito", "zakrit", "zakrita",
    "zaupno", "anonimno", "brez pregleda", "za pregled", "nedoločeno",
    "neopredeljeno", "manjkajoče", "izpolnite", "dopolnite", "ni relevantno", "se ne uporablja",
    "ni na voljo", "ne velja", "čakanje", "v pripravi", "zadržano",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def is_review_placeholder(value: object) -> bool:
    if not isinstance(value, str) or not value.strip():
        return True
    normalized = unicodedata.normalize("NFKC", value).casefold()
    normalized = " ".join(re.sub(r"[^\w]+|_", " ", normalized).split())
    if not normalized:
        return True
    # Reject padded/composed sentinels, not only a truthy exact 'pending'.
    # 'na' is also a common Slovene preposition (and can occur in a name).
    # Null-like NA/N/A is a sentinel only when it is the whole field.
    exact_only = {"na", "n a"}
    return normalized in exact_only or any(
        f" {sentinel} " in f" {normalized} " for sentinel in REVIEW_PLACEHOLDERS - exact_only
    )


def validate_review_metadata(reviewer: object, review_date: object,
                            review_scope: object, context: str) -> None:
    require(not is_review_placeholder(reviewer), f"{context}: reviewer must not be a placeholder")
    name_words = re.findall(r"[^\W\d_]+", reviewer)
    role_words = {
        "name", "named", "first", "last", "reviewer", "human", "subject", "matter",
        "language", "scholarly", "competent", "assigned", "confirmed", "review",
        "ime", "priimek", "in", "pregledovalec", "strokovni", "jezikovni", "človeški",
        "usposobljeni", "recenzent", "imenovani", "potrjen", "dr", "prof", "mr", "ms",
    }
    require(len(name_words) >= 2 and not all(word.casefold() in role_words for word in name_words),
            f"{context}: require a named reviewer, not an unnamed role")
    date_text = str(review_date)
    require(re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_text) is not None,
            f"{context}: review_date must be a valid ISO date (YYYY-MM-DD)")
    try:
        date.fromisoformat(date_text)
    except ValueError as error:
        raise ValueError(f"{context}: review_date must be a valid ISO date") from error
    require(not is_review_placeholder(review_scope), f"{context}: review_scope must not be a placeholder")
    require(len(review_scope.strip()) >= 20 and len(re.findall(r"[^\W_]+", review_scope)) >= 4,
            f"{context}: review_scope must describe a substantive review scope")
    # These structural checks do not authenticate an identity or prove review.
