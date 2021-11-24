import unittest

from max_sequence import max_sequence


class Test(unittest.TestCase):
    def test_max_sequence(self):
        self.assertEqual(max_sequence([]), 0)
        self.assertEqual(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)


if __name__ == '__main__':
    unittest.main()
