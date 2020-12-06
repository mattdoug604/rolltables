import sys
from pathlib import Path

from rolltables.cli import main

TEST_DB = Path(__file__).parent / "data" / "db.txt"
TEST_STRING = Path(__file__).parent / "data" / "string.txt"


def test_cli(mocker):
    mocker.patch.object(sys, "argv", [None, TEST_STRING, TEST_DB])
    main()
