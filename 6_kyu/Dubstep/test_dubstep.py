import unittest

from dubstep import song_decoder


class Test(unittest.TestCase):
    def test_dubstep(self):
        self.assertEqual(song_decoder("AWUBBWUBC"), "A B C")
        self.assertEqual(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C")
        self.assertEqual(song_decoder("WUBAWUBBWUBCWUB"), "A B C")


if __name__ == '__main__':
    unittest.main()
