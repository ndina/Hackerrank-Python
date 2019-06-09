import merge_tools.merge_the_tools


class TestCases:
    def test1(self):
        assert merge_tools.merge_the_tools.merge_the_tools('AACAAADA', 3) == 'AB''CA''AD'

    def test2(self):
        assert merge_tools.merge_the_tools.merge_the_tools('AACA', 2) == 'A''CAA'

    def test3(self):
        assert merge_tools.merge_the_tools.merge_the_tools('AA', 1) == 'A''A'

