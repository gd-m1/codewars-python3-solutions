import unittest

from vasya_clerk import tickets


class Test(unittest.TestCase):
    def test_vasya_clerk(self):
        self.assertEqual(tickets([25, 25, 50]), "YES")
        self.assertEqual(tickets([25, 100]), "NO")


if __name__ == '__main__':
    unittest.main()
