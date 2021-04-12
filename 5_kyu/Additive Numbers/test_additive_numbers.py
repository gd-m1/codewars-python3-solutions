import unittest

from additive_numbers import find_additive_numbers


class Test(unittest.TestCase):
    def test_additive_numbers(self):
        self.assertEqual(find_additive_numbers('112358'), ['1', '1', '2', '3', '5', '8'])
        self.assertEqual(find_additive_numbers('199100199'), ['1', '99', '100', '199'])
        self.assertEqual(find_additive_numbers('1023'), [])
        self.assertEqual(find_additive_numbers('112356'), [])


if __name__ == '__main__':
    unittest.main()
