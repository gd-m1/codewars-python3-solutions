import unittest

from the_greatest_warrior import Warrior

tom = Warrior()
bruce_lee = Warrior()


class Test(unittest.TestCase):
    def test_warrior(self):
        self.assertEqual(tom.level, 1)
        self.assertEqual(tom.experience, 100)
        self.assertEqual(tom.rank, "Pushover")

        self.assertEqual(bruce_lee.level, 1)
        self.assertEqual(bruce_lee.experience, 100)
        self.assertEqual(bruce_lee.rank, "Pushover")
        self.assertEqual(bruce_lee.achievements, [])
        self.assertEqual(bruce_lee.training(["Defeated Chuck Norris", 9000, 1]), "Defeated Chuck Norris")
        self.assertEqual(bruce_lee.experience, 9100)
        self.assertEqual(bruce_lee.level, 91)
        self.assertEqual(bruce_lee.rank, "Master")
        self.assertEqual(bruce_lee.battle(90), "A good fight")
        self.assertEqual(bruce_lee.experience, 9105)
        self.assertEqual(bruce_lee.achievements, ["Defeated Chuck Norris"])


if __name__ == '__main__':
    unittest.main()
