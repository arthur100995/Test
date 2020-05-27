import unittest
from Additional_material import *

class TestPythagorienTheorem(unittest.TestCase):
    def test_pythagorien_theorem(self):
        self.assertEqual(pythagorien_theorem(2, 2), sqrt(8))
        self.assertEqual(pythagorien_theorem(4, 2), sqrt(20))
        self.assertEqual(pythagorien_theorem(2.12, 3.23), sqrt(14.9273))


if __name__ == '__main__':
    unittest.main()