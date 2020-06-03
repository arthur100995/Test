import unittest

from App.Lists.lists import *


class ListTests(unittest.TestCase):
    """List tests"""

    def test_select_second(self):
        """Test for function 'select_second'"""
        self.assertIs(select_second([0, 15, 2]), 15)
        self.assertIsNone(select_second(['alone']))
        self.assertIsNone(select_second([3]))

    def test_losing_team_captain(self):
        """Test for function 'losing_team_captain'"""
        self.assertEqual(losing_team_captain([[1], [2], [0, 7]]), 7)




if __name__ == '__main__':
    unittest.main()