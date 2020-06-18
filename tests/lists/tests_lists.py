import unittest

from app.lists.lists import *


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

    def test_purple_shell(self):
        """Test for function 'purple_shell'"""
        self.assertEqual(purple_shell([0, 1, 2, 3]), [3, 1, 2, 0])


    def test_fashionably_late(self):
        """Test for function 'fashionably_late'"""
        self.assertTrue(fashionably_late([1, 2, 3, 4, 5], 4))
        self.assertTrue(fashionably_late(['a', 'b', 'c', 'd', 'e', 'f'], 'e'))
        self.assertIs(fashionably_late(['a', 'b', 'c', 'd', 'e', 'f'], 'e'), True)




if __name__ == '__main__':
    unittest.main()