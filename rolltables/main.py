from pathlib import Path

from .table import TableMap

DEFAULT_TABLE_DIR = Path(__file__).parent / "table"
DEFAULT_INPUT = Path(__file__).parent / "template" / "dungeon.txt"
MAX_ITER = 100


def load_text(filepath: str) -> str:
    with open(filepath, "r") as fh:
        text = fh.read().strip()

    return text


def format_text(text: str, table_map: TableMap) -> str:
    for _ in range(MAX_ITER):
        _text = text.format_map(table_map)
        if _text == text:
            break
        else:
            text = _text

    return text


def main():
    text = load_text(DEFAULT_INPUT)
    table_map = TableMap.load(DEFAULT_TABLE_DIR)
    text = format_text(text, table_map)

    print(text)
