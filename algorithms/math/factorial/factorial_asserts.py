import unittest
from factorial_iterative import factorial_iterative
from factorial_recursive import factorial_recursive

class TestFactorialFunctions (unittest.TestCase):

    def test_factorial_iterative (self):
        self.assertEqual(factorial_iterative(5), 120)
        self.assertEqual(factorial_iterative(7), 5040)
        self.assertEqual(factorial_iterative(0), 1)
    
    def test_factorial_recursive (self):
        self.assertEqual(factorial_recursive(5), 120)
        self.assertEqual(factorial_recursive(7), 5040)
        self.assertEqual(factorial_recursive(0), 1)

if __name__ == '__main__':
    unittest.main()
