import unittest

from valid_parentheses import valid_parentheses


class Test(unittest.TestCase):
    def test_valid_parentheses(self):
        self.assertEqual(valid_parentheses("  ("), False)
        self.assertEqual(valid_parentheses(")test"), False)
        self.assertEqual(valid_parentheses(""), True)
        self.assertEqual(valid_parentheses("hi())("), False)
        self.assertEqual(valid_parentheses("hi(hi)()"), True)


if __name__ == '__main__':
    unittest.main()
