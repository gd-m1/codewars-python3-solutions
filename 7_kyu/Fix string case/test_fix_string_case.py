import unittest

from fix_string_case import solve


class Test(unittest.TestCase):
    def test_fix_string_case(self):
        self.assertEqual(solve("code"), "code")
        self.assertEqual(solve("CODe"), "CODE")
        self.assertEqual(solve("COde"), "code")
        self.assertEqual(solve("Code"), "code")


if __name__ == '__main__':
    unittest.main()
