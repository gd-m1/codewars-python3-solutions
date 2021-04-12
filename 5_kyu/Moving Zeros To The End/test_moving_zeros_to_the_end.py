import unittest

from moving_zeros_to_the_end import multiplication_table


class Test(unittest.TestCase):
    def test_moving_zeros(self):
        self.assertEqual(multiplication_table(3), [[1, 2, 3], [2, 4, 6], [3, 6, 9]])


if __name__ == '__main__':
    unittest.main()
