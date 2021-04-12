import unittest

from function_addition import FuncAdd


class Test(unittest.TestCase):
    def test_func_add(self):
        @FuncAdd
        def bar(n):
            return n+2
        
        @FuncAdd
        def bar(n):
            return n*2
        self.assertEqual(bar(5), (7, 10))
        self.assertEqual(bar(n=5), (7, 10))


if __name__ == '__main__':
    unittest.main()
