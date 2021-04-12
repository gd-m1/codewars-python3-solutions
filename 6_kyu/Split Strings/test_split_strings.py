import unittest

from split_strings import solution


class Test(unittest.TestCase):
    def test_split_strings(self):
        self.assertEqual(solution("asdfadsf"), ['as', 'df', 'ad', 'sf'])
        self.assertEqual(solution("asdfads"), ['as', 'df', 'ad', 's_'])
        self.assertEqual(solution(""), [])
        self.assertEqual(solution("x"), ["x_"])


if __name__ == '__main__':
    unittest.main()
