import unittest

from find_outlier import find_outlier


class Test(unittest.TestCase):
    def test_find_outlier(self):
        self.assertEqual(find_outlier([2, 4, 6, 8, 10, 3]), 3)
        self.assertEqual(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
        self.assertEqual(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)


if __name__ == '__main__':
    unittest.main()
