import the_minion_game


class TestCases:
    def test1(self):
        assert the_minion_game.minion_game('HEELOOOO') == 'Kevin 23'

    def test2(self):
        assert the_minion_game.minion_game('ABCD') == 'Stuart 6'

    def test3(self):
        assert the_minion_game.minion_game('STUART') == 'Stuart 14'