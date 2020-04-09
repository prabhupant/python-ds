import unittest
from catalan_number import catalan_function

class TestAckermannFunction (unittest.TestCase):

    def test_ackerman_function (self):
        self.assertEqual(catalan_function(3), 5)
        self.assertEqual(catalan_function(6), 132)
        self.assertEqual(catalan_function(9), 4862)

if __name__ == '__main__':
    unittest.main()
