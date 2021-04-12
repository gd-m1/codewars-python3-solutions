import unittest

from rgb_to_hex_conversion import rgb


class Test(unittest.TestCase):
    def test_rgb_to_hex_conversion(self):
        self.assertEqual(rgb(0, 0, 0), "000000", "testing zero values")
        self.assertEqual(rgb(1, 2, 3), "010203", "testing near zero values")
        self.assertEqual(rgb(255, 255, 255), "FFFFFF", "testing max values")
        self.assertEqual(rgb(254, 253, 252), "FEFDFC", "testing near max values")
        self.assertEqual(rgb(-20, 275, 125), "00FF7D", "testing out of range values")


if __name__ == '__main__':
    unittest.main()
