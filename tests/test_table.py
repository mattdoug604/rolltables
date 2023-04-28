from rolltables.database import Choice, Table


class TestTable:
    def setup_method(self):
        choice1 = Choice("choice1", 1.0)
        choice2 = Choice("choice2", 2.0)
        choice3 = Choice("choice3", 1.0)
        self.table = Table("table", [choice1, choice2, choice3])

    def test_weights(self):
        assert self.table.weights == [1.0 / 3, 2.0 / 3, 1.0 / 3]

    def test_roll(self):
        assert self.table.roll() in ["choice1", "choice2", "choice3"]
