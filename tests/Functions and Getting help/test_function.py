import unittest
import sys
sys.path.append('/home/bear/PycharmProjects/Test/App/Functions and Getting help')
from function import *




class TestFunction(unittest.TestCase):

    def test_round_two_places(self):
        self.assertEqual(round_two(3), 3.00)
        self.assertEqual(round_two(5.15116126), 5.15)
        self.assertEqual(round_two(3.02 / 2), 1.51)





if __name__ == '__main__':
    unittest.main()