import unittest
import sys
sys.path.append('/home/bear/PycharmProjects/Test/App/Functions and Getting help')
from function import *




class TestFunction(unittest.TestCase):

    def test_round_two_places(self):
        """Тест для функции round_two_places"""
        self.assertEqual(round_two(3), 3.00)
        self.assertEqual(round_two(5.15116126), 5.15)
        self.assertEqual(round_two(3.02 / 2), 1.51)

    def test_round_negative_ndigits(self):
        """Тесты для функции round_negative_ndigits"""
        self.assertEqual(round_negative_ndigits(321.222194), 320)
        self.assertEqual(round_negative_ndigits(-321.222194), -320)
        self.assertEqual(round_negative_ndigits(2), 2)

    def test_candies_to_smash_new(self):
        """Тесты для функции candies_to_smash_new"""
        self.assertEqual(candies_to_smash_new(91, 3), 1)
        self.assertEqual(candies_to_smash_new(3.5, 3), 0.5)
        self.assertEqual(candies_to_smash_new(91), 1)

    def test_smallest_absolute(self):
        """Тесты для функции smallest_absolute"""
        self.assertEqual(smallest_absolute(-10, 5), 5)
        self.assertEqual(smallest_absolute(-1.22, 12), 1.22)
        self.assertEqual(smallest_absolute(-10.12, 5.34), 5.34)






if __name__ == '__main__':
    unittest.main()