import unittest

from anagrams import anagrams


class Test(unittest.TestCase):
    def test_valid_parentheses(self):
        self.assertEqual(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
        self.assertEqual(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), [
                         'carer', 'racer'])


if __name__ == '__main__':
    unittest.main()
