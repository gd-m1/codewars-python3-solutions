import unittest

from mirror_on_the_wall import mirror


class Test(unittest.TestCase):
    def test_mirror(self):
        self.assertEqual(mirror([]), [])
        self.assertEqual(mirror([1]), [1]),
        self.assertEqual(mirror([2, 1]), [1, 2, 1]),
        self.assertEqual(mirror([1, 3, 2]), [1, 2, 3, 2, 1]),
        self.assertEqual(mirror([-8, 42, 18, 0, -16]), [-16, -8, 0, 18, 42, 18, 0, -8, -16])


if __name__ == '__main__':
    unittest.main()
