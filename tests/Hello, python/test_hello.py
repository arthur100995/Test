import unittest

from hello_python import *


class TestFavoriteColor(unittest.TestCase):
    def test_my_favorite_color(self):
        self.assertEqual(favorite_color(str()), 'Blue')



if __name__ == '__main__':
    unittest.main()