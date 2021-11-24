import unittest

from rot13 import rot13


class Test(unittest.TestCase):
    def test_rot13(self):
        self.assertEqual(rot13("test"), "grfg")
        self.assertEqual(rot13("Test"), "Grfg")


if __name__ == '__main__':
    unittest.main()
