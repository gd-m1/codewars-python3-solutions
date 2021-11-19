import unittest

from spin_words import spin_words


class Test(unittest.TestCase):
    def test_spin_words(self):
        self.assertEqual(spin_words("Welcome"), "emocleW")


if __name__ == '__main__':
    unittest.main()
