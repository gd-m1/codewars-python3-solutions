import unittest

from disemvowel_trolls import disemvowel


class Test(unittest.TestCase):
    def test_disemvowel_trolls(self):
        self.assertEqual(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")


if __name__ == '__main__':
    unittest.main()
