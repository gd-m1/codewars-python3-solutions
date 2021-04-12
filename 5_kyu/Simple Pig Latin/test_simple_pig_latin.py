import unittest

from simple_pig_latin import pig_it


class Test(unittest.TestCase):
    def test_simple_pig_latin(self):
        self.assertEqual(pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay')
        self.assertEqual(pig_it('This is my string'), 'hisTay siay ymay tringsay')


if __name__ == '__main__':
    unittest.main()
