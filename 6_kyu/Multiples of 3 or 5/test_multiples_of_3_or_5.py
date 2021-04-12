import unittest

from multiples_of_3_or_5 import solution


class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(10), 23)


if __name__ == '__main__':
    unittest.main()
