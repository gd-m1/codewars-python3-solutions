import unittest

from your_order import order


class Test(unittest.TestCase):
    def test_your_order(self):
        self.assertEqual(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
        self.assertEqual(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
        self.assertEqual(order(""), "")


if __name__ == '__main__':
    unittest.main()
