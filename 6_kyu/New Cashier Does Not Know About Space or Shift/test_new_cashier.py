import unittest

from new_cashier import get_order


class Test(unittest.TestCase):
    def test_new_cashier(self):
        self.assertEqual(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"),
                         "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke")
        self.assertEqual(get_order("pizzachickenfriesburgercokemilkshakefriessandwich"),
                         "Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke")


if __name__ == '__main__':
    unittest.main()
