import unittest

from money import calculate_years


class Test(unittest.TestCase):
    def test_calculate_years(self):
        self.assertEqual(calculate_years(1000, 0.05, 0.18, 1100), 3)
        self.assertEqual(calculate_years(1000, 0.01625, 0.18, 1200), 14)
        self.assertEqual(calculate_years(1000, 0.05, 0.18, 1000), 0)


if __name__ == '__main__':
    unittest.main()
