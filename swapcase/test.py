import swapcase.swap_case


class TestCases:
    def test1(self):
        assert swapcase.swap_case.swap_case('asdA') == 'ASDa'

    def test2(self):
        assert swapcase.swap_case.swap_case('DINaa') == 'dinAA'

    def test3(self):
        assert swapcase.swap_case.swap_case('ELLoonN') == 'ellOONn'