import os.path
import sys
from os import PathLike
from pathlib import Path
from typing import Dict, Sequence

from jinja2 import Environment, FileSystemLoader, Template

from .table import Table, load_tables

DEFAULT_TABLE_DIR = Path(__file__).parent / "table" / "dungeon"
DEFAULT_TEMPLATE_DIR = Path(__file__).parent / "template"
DEFAULT_TEMPLATE = "dungeon.txt"


def init_environment(searchpath: str | PathLike | Sequence[str | PathLike]) -> Environment:
    loader = FileSystemLoader(searchpath=searchpath)
    environment = Environment(loader=loader)
    templates = environment.list_templates()
    print(f"Loaded templates: {' '.join(templates)}", file=sys.stderr)

    return environment


def get_template(environment: Environment, name_or_path: str) -> Template:
    if os.path.exists(name_or_path):
        print(f"Loading template from file '{name_or_path}'", file=sys.stderr)
        with open(name_or_path, "r") as fh:
            string = fh.read()

        template = environment.from_string(string)
    else:
        print(f"Loading template by name '{name_or_path}'", file=sys.stderr)
        template = environment.get_template(name_or_path)

    return template


def recursive_render(
    environment: Environment, template: Template, tables: Dict[str, Table], max_iter: int = 10
):
    text = ""
    for _ in range(max_iter):
        _text = template.render(**tables).strip()
        if _text == text:
            break
        else:
            text = _text
            template = environment.from_string(text)
    else:
        print(f"ERROR Max iterations reached ({max_iter})", file=sys.stderr)

    return text


def main():
    template_dir = DEFAULT_TEMPLATE_DIR
    table_dir = DEFAULT_TABLE_DIR
    name = DEFAULT_TEMPLATE

    environment = init_environment([template_dir, table_dir])
    template = get_template(environment, name)
    tables = load_tables(table_dir)
    text = recursive_render(environment, template, tables)
    print(text)
