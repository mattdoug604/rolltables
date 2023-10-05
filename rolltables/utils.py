from string import punctuation

REPLACE = str.maketrans(punctuation + " ", "_" * (len(punctuation) + 1))


def normalize_name(name: str) -> str:
    """Normalize a table name."""
    return name.translate(REPLACE).lower()
