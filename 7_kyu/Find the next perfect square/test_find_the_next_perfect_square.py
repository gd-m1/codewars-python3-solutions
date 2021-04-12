import unittest

from find_the_next_perfect_square import find_next_square


class Test(unittest.TestCase):
    def test_find_the_next_square(self):
        self.assertEqual(find_next_square(121), 144)
        self.assertEqual(find_next_square(625), 676)
        self.assertEqual(find_next_square(319225), 320356)
        self.assertEqual(find_next_square(15241383936), 15241630849)
        self.assertEqual(find_next_square(155), -1)
        self.assertEqual(find_next_square(342786627), -1)


if __name__ == '__main__':
    unittest.main()
