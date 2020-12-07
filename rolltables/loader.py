from typing import Dict, Tuple

from .database import Choice, Database, Table


def load(filepath: str, sep="|") -> Database:
    choice = None
    choices = []
    table_name = None
    table = None
    tables = []
    database = None

    for line in _iter(filepath):
        if line and table_name is None:
            table_name = line
        elif line and table_name:
            value, weight, exclude = _split(line, sep)
            choice = Choice(value, weight=weight, exclude=exclude)
            choices.append(choice)
        elif not line and table_name:
            table = Table(table_name, choices)
            tables.append(table)
            table_name = None
            choices = []
        else:
            pass

    if table_name:
        table = Table(table_name, choices)
        tables.append(table)
        table_name = None
        choices = []

    database = Database(tables)
    return database


def _iter(filepath: str):
    with open(filepath, "r") as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield line
            else:
                yield None


def _split(string: str, sep="|") -> Tuple[str, float, Dict]:
    temp = [i.strip() for i in string.split(sep)][:3]
    value = str(temp[0])
    try:
        if temp[1]:
            weight = float(temp[1])
        else:
            weight = 1.0
    except IndexError:
        weight = 1.0

    try:
        key, val = temp[2].split(":", 1)
        exclude = {key: val}
    except IndexError:
        exclude = {}

    return value, weight, exclude
