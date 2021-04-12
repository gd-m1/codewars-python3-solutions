import unittest

from codewars_style_ranking_system import User

user = User()


class Test(unittest.TestCase):
    def test_ranking_system(self):
        self.assertEqual(user.rank, -8)
        self.assertEqual(user.progress, 0)
        user.inc_progress(-7)
        self.assertEqual(user.progress, 10)
        user.inc_progress(-5)
        self.assertEqual(user.progress, 0)
        self.assertEqual(user.rank, -7)


if __name__ == '__main__':
    unittest.main()
