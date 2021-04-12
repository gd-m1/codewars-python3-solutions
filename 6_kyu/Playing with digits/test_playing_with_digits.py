import unittest

from playing_with_digits import dig_pow


class Test(unittest.TestCase):
    def test_playing_with_digits(self):
        self.assertEqual(dig_pow(89, 1), 1)
        self.assertEqual(dig_pow(92, 1), -1)
        self.assertEqual(dig_pow(46288, 3), 51)


if __name__ == '__main__':
    unittest.main()
