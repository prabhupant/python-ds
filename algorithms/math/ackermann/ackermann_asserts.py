import unittest
from ackermann import ackermann_function

class TestAckermannFunction (unittest.TestCase):

    def test_ackerman_function (self):
        self.assertEqual(ackermann_function(1, 2), 4)
        self.assertEqual(ackermann_function(2, 3), 9)
        self.assertEqual(ackermann_function(3, 2), 29)

if __name__ == '__main__':
    unittest.main()
