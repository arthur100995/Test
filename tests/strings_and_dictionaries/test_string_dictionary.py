import unittest
from app.strings_and_dictionaries.string_dictionary import *


class StrDictTest(unittest.TestCase):

    def test_is_valid_zip(self):
        """test for function 'is_valid_zip'"""
        self.assertTrue(is_valid_zip('11345'))
        self.assertFalse(is_valid_zip('123ds'))
        self.assertFalse(is_valid_zip('12345 '))
        self.assertFalse(is_valid_zip('12 345'))

    def test_word_search(self):
        """test for function 'word_search'"""
        self.assertEqual(word_search(["Challenge Casino.", "They bought a car", "Casinoville"], 'casino'), [0])
        self.assertEqual(word_search(["Challenge Casino.", "They bought a car", "Casinoville"], 'Bought'), [1])

    def test_multi_word_search(self):
        """test for function multi_word_search"""
        self.assertEqual(
            # Takes list of documents (each document is a string) and a list of keywords.
            multi_word_search(["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville Theybay"],
                              ['casino', 'they']),
            # Returns a dictionary where each key is a keyword, and the value is a list of indices
            # (from doc_list) of the documents containing that keyword
            {'casino': [0, 1], 'they': [1]}
        )


if __name__ == '__main__':
    unittest.main()
