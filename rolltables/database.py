import random
from typing import List

from .formatter import Formatter


class Choice:
    def __init__(self, value: str, weight: float = 1.0):
        self.value = value
        self.weight = weight

    def __repr__(self) -> str:
        return self.value


class Table:
    def __init__(self, name: str, choices: List[Choice]):
        self.name = name
        self.choices = choices

    def __repr__(self) -> str:
        return self.name

    @property
    def weights(self) -> List[float]:
        total = len(self.choices)
        return [choice.weight / total for choice in self.choices]

    def roll(self) -> str:
        return random.choices(population=self.choices, weights=self.weights)[0].value


class Database:
    def __init__(self, tables: List[Table]):
        self.tables = tables

    def query(self, format_string: str, _checked: List[str] = []) -> str:
        replacements = []
        for table_name in Formatter.get_field_names(format_string):
            table = self._get_table(table_name)
            value = table.roll()
            replacements.append(self.query(value, _checked))
        return Formatter.format(format_string, *replacements)

    def _get_table(self, table_name: str) -> Table:
        tables = [table for table in self.tables if table.name == table_name]
        assert len(tables) <= 1, f"More than one table named '{table_name}' found"
        assert len(tables) > 0, f"No table named '{table_name}' found"
        return tables[0]
