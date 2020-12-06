import pytest

from rolltables.database import Choice, Table, Database


class TestTable:
    def setup_method(self):
        self.choice1 = Choice("choice1", 1.0)
        self.choice2 = Choice("choice2 {table3}", 2.0)
        self.choice3 = Choice("choice3 {table1}", 1.0)
        self.table1 = Table("table1", [self.choice1])
        self.table2 = Table("table2", [self.choice2])
        self.table3 = Table("table3", [self.choice3])
        self.db = Database([self.table1, self.table2, self.table3])

    def test_get_table(self):
        assert self.db._get_table("table1") == self.table1
        assert self.db._get_table("table2") == self.table2

    def test_query(self):
        assert self.db.query("{table1}") == "choice1"

    def test_query_with_recursion(self):
        assert self.db.query("{table2}") == "choice2 choice3 choice1"

    def test_query_multiple_with_recursion(self):
        assert self.db.query("{table1} and {table3}") == "choice1 and choice3 choice1"
