import unittest
from App.Strings_And_Dictionaries.string_dictionary import *


class StrDictTest(unittest.TestCase):

    def test_is_valid_zip(self):
        """test for function is_valid_zip"""
        self.assertTrue(is_valid_zip('11345'))
        self.assertFalse(is_valid_zip('123ds'))
        self.assertFalse(is_valid_zip('12345 '))
        self.assertFalse(is_valid_zip('12 345'))





if __name__ == '__main__':
    unittest.main()