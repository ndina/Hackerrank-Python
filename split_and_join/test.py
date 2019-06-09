import split_and_join.split_and_join

class TestCases:
    def test1(self):
        assert split_and_join.split_and_join.split_and_join('i have my book') == 'i-have-my-book'

    def test2(self):
        assert split_and_join.split_and_join.split_and_join('pride and prejudice') == 'pride-and-prejudice'

    def test1(self):
        assert split_and_join.split_and_join.split_and_join('darcy or musk') == 'darcy-or-musk'