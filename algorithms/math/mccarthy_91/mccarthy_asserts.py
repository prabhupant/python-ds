import unittest
from mccarthy_function import mccarthy_function

class TestAckermannFunction (unittest.TestCase):

    def test_ackerman_function(self):
        self.assertEqual(mccarthy_function(87), 91)
        self.assertEqual(mccarthy_function(99), 91)
        self.assertEqual(mccarthy_function(101), 91)

if __name__ == '__main__':
    unittest.main()
