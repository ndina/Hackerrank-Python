import name.whats_your_name


class TestCases:

    def test1(self):
        assert name.whats_your_name.print_full_name('Dina', 'N') == 'Hello Dina  N! You just delved into python.'

    def test2(self):
        assert name.whats_your_name.print_full_name('Aida', 'U') == 'Hello Aida  U! You just delved into python.'

    def test3(self):
        assert name.whats_your_name.print_full_name('Adilkhan', 'K') == 'Hello Adilkhan  K! You just delved into python.'