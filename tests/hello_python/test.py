import unittest
from App.hello_python.hello import *


class TestHello(unittest.TestCase):
    def test_add(self):
        '''Тесты для функции add_func'''
        self.assertEqual(add_func(5, 5), 10)
        self.assertEqual(add_func(17, 3), 20)
        self.assertEqual(add_func(5.12, 5), 10.12)
        self.assertEqual(add_func(1.11, 2.12), 3.23)

    def test_true_division(self):
        '''Тест для функции true_division'''
        self.assertEqual(true_division(20, 10), 2)
        self.assertEqual(true_division(20.20, 10), 2.02)

    def test_exponantional_to(self):
        '''Тест для функции exponantional_to'''
        self.assertEqual(exponantional_to(2, 3), 8)

    def test_exchange_values(self):
        '''Тест для функции exchange_values'''
        self.assertEqual(exchange_values(1, 2), (2, 1))
        self.assertEqual(exchange_values([1, 2, 3], [2, 3, 4]), ([2, 3, 4], [1, 2, 3]))

    def test_candies_to_smash(self):
        '''Тест для функции candies_to_smash'''
        self.assertEqual(candies_to_smash(30, 30, 31), 1)
        self.assertEqual(candies_to_smash(20, 20, 21.22), 1.22)


if __name__ == '__main__':
    unittest.main()
