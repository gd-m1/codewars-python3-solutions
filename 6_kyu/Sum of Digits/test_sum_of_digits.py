import unittest

from sum_of_digits import digital_root


class TestDR(unittest.TestCase):
    def test_sum_of_digits(self):
        self.assertEqual(digital_root(16), 7)
        self.assertEqual(digital_root(942), 6)
        self.assertEqual(digital_root(132189), 6)
        self.assertEqual(digital_root(493193), 2)


if __name__ == '__main__':
    unittest.main()
