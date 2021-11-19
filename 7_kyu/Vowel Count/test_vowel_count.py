import unittest

from vowel_count import getCount


class Test(unittest.TestCase):
    def test_getCount(self):
        self.assertEqual(getCount("aeiou"), 5, f"Incorrect answer for \"aeiou\"")
        self.assertEqual(getCount("y"), 0, f"Incorrect answer for \"y\"")
        self.assertEqual(getCount("bcdfghjklmnpqrstvwxz y"), 0, f"Incorrect answer for \"bcdfghjklmnpqrstvwxz y\"")
        self.assertEqual(getCount(""), 0, f"Incorrect answer for empty string")
        self.assertEqual(getCount("abracadabra"), 5, f"Incorrect answer for \"abracadabra\"")


if __name__ == '__main__':
    unittest.main()
