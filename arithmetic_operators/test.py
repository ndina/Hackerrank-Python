import arithmetic_operators
# import pytest


class TestCases:
    def test1(self):
        assert arithmetic_operators.main(1, 2) == 3

    def test2(self):
        assert arithmetic_operators.main(1, 4) == 5

    def test3(self):
        assert arithmetic_operators.main(0, 0) == 0



