import unittest

from square_every_digit import square_digits


class Test(unittest.TestCase):
    def test_square_every_digit(self):
        self.assertEqual(square_digits(9119), 811181)


if __name__ == '__main__':
    unittest.main()
