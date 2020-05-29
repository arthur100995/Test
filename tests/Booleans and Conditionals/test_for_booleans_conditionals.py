import unittest
import sys
sys.path.append('/home/bear/PycharmProjects/Test/App/Booleans and Conditionals')
from booleans_conditionals import *

class TestBooleansConditionals(unittest.TestCase):

    def test_can_run_for_president(self):
        self.assertTrue(can_run_for_president(35, True))
        self.assertFalse(can_run_for_president(20, True))
        self.assertFalse(can_run_for_president(17, True))
        self.assertFalse(can_run_for_president(40, False))

    def test_sign(self):
        """Тесты для ф-ции sign"""
        self.assertIs(sign(3), 1)
        self.assertIsNot(sign(0), 1)
        self.assertIs(sign(3.2156), 1)
        self.assertIs(sign(-2), -1)
        self.assertIsNot(sign(3), -1)
        self.assertIs(sign(0), 0)

    def test_exactly_one_toping(self):
        """Test for exactly_one_toping"""
        self.assertTrue(exactly_one_toping(True, False, False))
        self.assertTrue(exactly_one_toping(False, False, True))
        self.assertTrue(exactly_one_toping(False, True, False))
        self.assertFalse(exactly_one_toping(True, False, True))
        self.assertFalse(exactly_one_toping(True, True, True))




if __name__ == '__main__':
    unittest.main()

    

