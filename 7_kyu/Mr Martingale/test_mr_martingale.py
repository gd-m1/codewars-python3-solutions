import unittest

from mr_martingale import martingale


class Test(unittest.TestCase):
    def test_martingale(self):
        self.assertEqual(martingale(500, []), 500)
        self.assertEqual(martingale(1000, [1, 1, 0, 0, 1]), 1300)
        self.assertEqual(martingale(0, [0, 0, 0, 0, 1, 0, 0]), -200)
        self.assertEqual(martingale(5100, [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0]), 5600)
        self.assertEqual(martingale(-500, [1, 1, 0, 1, 0, 1, 0]), -200)


if __name__ == '__main__':
    unittest.main()
