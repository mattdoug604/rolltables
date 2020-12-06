from pathlib import Path

from rolltables.database import Database
from rolltables.loader import load


TEST_DB = Path(__file__).parent / "data" / "db.txt"


def test_load():
    db = load(TEST_DB)
    assert isinstance(db, Database)
    assert [i.name for i in db.tables] == ["environment", "creator", "treasure"]
