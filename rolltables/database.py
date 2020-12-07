import random
from typing import Dict, List

from .formatter import Formatter


class Choice:
    def __init__(self, value: str, weight: float = 1.0, exclude: Dict[str, str] = {}):
        self.value = value
        self.weight = weight
        self.exclude = exclude

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

    def roll(self, exclude: List[str] = []) -> Choice:
        choices = self._get_choices(exclude)
        return random.choices(population=choices, weights=self.weights)[0]

    def _get_choices(self, exclude: List[str] = []) -> List[Choice]:
        return [i for i in self.choices if i.value not in exclude]


class Database:
    def __init__(self, tables: List[Table]):
        self.tables = tables
        self._excluded: Dict[str, List[str]] = {}

    def query(self, format_string: str, _checked: List[str] = []) -> str:
        substring = {}
        for table_name in Formatter.get_field_names(format_string):
            table = self._get_table(table_name)
            exclude = self._excluded.get("table_name", [])
            choice = table.roll(exclude)
            for key, val in choice.exclude.items():
                self._excluded.setdefault(key, []).append(val)
            substring[table_name] = self.query(choice.value, _checked)
        return format_string.format(**substring)

    def _get_table(self, table_name: str) -> Table:
        tables = [table for table in self.tables if table.name == table_name]
        assert len(tables) <= 1, f"More than one table named '{table_name}' found"
        assert len(tables) > 0, f"No table named '{table_name}' found"
        return tables[0]
