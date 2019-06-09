import sets


class TestCases:
    def test1(self):
        assert sets.average([1,2,2,3]) == 2.0

    def test2(self):
        assert sets.average([1, 2, 1, 2, 3]) == 2.0

    def test3(self):
        assert sets.average([1, 2, 2, 5, 6, 3]) == 3.4
