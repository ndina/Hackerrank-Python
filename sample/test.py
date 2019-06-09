import sample.main


class TestCases:
    def test1(self):
        assert sample.main.f('asd') == 'dsa'

    def test2(self):
        assert sample.main.f('asdfg') == 'gfdsa'

    def test3(self):
        assert sample.main.f('123') == '321'