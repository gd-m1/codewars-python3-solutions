import unittest

from count_the_smiley_faces import count_smileys


class Test(unittest.TestCase):
    def test_count_the_smiley_faces(self):
        self.assertEqual(count_smileys([]), 0)
        self.assertEqual(count_smileys([':D', ':~)', ';~D', ':)']), 4)
        self.assertEqual(count_smileys([':)', ':(', ':D', ':O', ':;']), 2)
        self.assertEqual(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)


if __name__ == '__main__':
    unittest.main()
