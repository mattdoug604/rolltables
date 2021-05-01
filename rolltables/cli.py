import sys

from .loader import load


def main():
    try:
        file_to_format = sys.argv[1]
        database_file = sys.argv[2]
    except IndexError:
        raise ValueError(f"Usage: {__name__} <file_to_format> <database_file>")

    database = load(database_file)
    with open(file_to_format, "r") as fh:
        format_string = fh.read().rstrip()
        print(database.query(format_string))
