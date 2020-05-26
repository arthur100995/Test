import unittest
import sys, os
from hello import *

class TestAreaCircle(unittest.TestCase):

    def test_radius_of_circle(self):
        self.assertEqual(radius_of_circle(12), 6)
        self.assertEqual(radius_of_circle(24), 12)
        self.assertEqual(radius_of_circle(142), 71)

    def test_value_of_area(self):
        self.assertEqual(area_of_circle(2), (4 * 3.14159))
        self.assertEqual(area_of_circle(6), (36 * 3.14159))


if __name__ == '__main__':
    unittest.main()


