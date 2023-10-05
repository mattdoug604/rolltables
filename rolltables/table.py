from __future__ import annotations

from pathlib import Path
from random import randint
from typing import Dict, List

from .utils import normalize_name

MISSING = "<missing>"


class TableMap:
    @classmethod
    def find_tables(cls, directory: Path | str) -> List[Path]:
        if isinstance(directory, Path):
            dirobj = directory
        else:
            dirobj = Path(directory)

        tables = sorted(dirobj.rglob("*.tsv"))

        return tables

    @classmethod
    def load(cls, directory: Path | str) -> TableMap:
        tables = {}

        for path in cls.find_tables(directory):
            table = Table.load(path)
            table_name = normalize_name(table.name)
            assert table_name not in tables
            tables[table_name] = table

        return TableMap(tables)

    def __init__(self, tables: Dict[str, Table]):
        self.tables = tables

    def __getitem__(self, table_name: str) -> str:
        return self.roll(table_name)

    def roll(self, table_name: str) -> str:
        table_name = normalize_name(table_name)
        table = self.tables[table_name]
        choice = table.roll()

        return choice


class Table:
    @classmethod
    def load(cls, filepath: Path | str) -> Table:
        first_comment_line = True
        first_data_line = True
        name = None
        die = None
        choices = {}

        if isinstance(filepath, Path):
            fileobj = filepath
        else:
            fileobj = Path(filepath)

        with open(fileobj, "r") as fh:
            for line in fh:
                if line := line.strip():
                    # Treat lines starting with '#' as comments
                    if line.startswith("#"):
                        line = line[1:]
                        # Assume the first comment line is the table title
                        if first_comment_line:
                            name = line

                        first_comment_line = False
                    else:
                        # Tables are expected to have two columns
                        col1, col2 = line.split("\t", 1)
                        col1 = col1.strip()
                        col2 = col2.strip()
                        # Optional first row can list the die in the first column
                        if first_data_line and line.startswith("d"):
                            die = int(col1[1:])
                        else:
                            # Normalize the unicode char U+2013 to the more common '-'
                            col1 = col1.replace("–", "-")
                            # Results can be a single number (1) or a range (2-12)
                            temp = col1.split("-", 1)
                            if len(temp) == 1:
                                min_roll = int(temp[0])
                                max_roll = min_roll
                            else:
                                min_roll = int(temp[0])
                                if temp[1] == "00":
                                    max_roll = 100
                                else:
                                    max_roll = int(temp[1])

                            for n in range(min_roll, max_roll + 1):
                                assert n not in choices
                                choices[n] = col2

                        first_data_line = False

        if die is None:
            die = max(choices)

        if name is None:
            name = normalize_name(fileobj.name)

        return Table(name, die, choices)

    def __init__(self, name: str, die: int, choices: Dict[int, str]) -> None:
        self.name = name
        self.die = die
        self.choices = choices

    def roll(self) -> str:
        roll = randint(1, self.die)
        choice = self.choices[roll]

        return choice
