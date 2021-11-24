import unittest

from cakes import cakes


class Test(unittest.TestCase):
    def test_cakes(self):
        recipe = {"flour": 500, "sugar": 200, "eggs": 1}
        available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
        self.assertEqual(cakes(recipe, available), 2)
        recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
        available = {"sugar": 500, "flour": 2000, "milk": 2000}
        self.assertEqual(cakes(recipe, available), 0)


if __name__ == '__main__':
    unittest.main()
