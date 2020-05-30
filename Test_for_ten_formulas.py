import unittest
from math import *

class TestTenGeometricFormulas(unittest.TestCase):

    def setUp(self):
        self.area = float
        self.perimeter = float

    def test_area_square(self):
        '''area_square(площадь квадрата) = a(сторона) ** 2'''
        self.assertEqual(self.area(9), 3 ** 2)

    def test_area_triangle(self):
        '''area_triangle(площадь треугольника) = (a(основание) * h(высота)) / 2'''
        self.assertEqual(self.area(2), (2 * 2) / 2)

    def test_area_rectangle(self):
        '''area_rectangle(площадь прямоугольника) = a(сторона1) * b(сторона 2)'''
        self.assertEqual(self.area(6), 2 * 3)

    def test_area_round(self):
        '''area_round(площадь круга) = pi * (r(радиус)**2)'''
        self.assertEqual(self.area(pi * 4), pi * (2 ** 2))

    def test_area_righttriangle(self):
        '''area_righttriangle(площадь прямоугольного треугольника) = (a * b)(умножение катетов) / 2'''
        self.assertEqual(self.area(3), (3 * 2) / 2)

    def test_area_isoscelestriangle(self):
        '''area_isosceles triangle(площадь ровнобедренного треугольника) = 1/2 * b(основание) * h(высота)'''
        self.assertEqual(self.area(3), 0.5 * 2 * 3)

    def test_perimeter_round(self):
        '''
        perimeter of round = pi(число Пи) * D(диаметр окружности),
        или = 2 * pi * r(радиус)
        '''
        self.assertEqual(self.perimeter(pi * 12), 2 * pi * 6)








if __name__ == '__main__':
    unittest.main()