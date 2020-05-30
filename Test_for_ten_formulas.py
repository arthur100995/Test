import unittest
from math import *

class TestTenGeometricFormulas(unittest.TestCase):

    def test_area_square(self):
        '''area_square(площадь квадрата) = a(сторона) ** 2'''
        a = int()
        area_square = a ** 2
        self.assertEqual(area_square == 9, a == 3)

    def test_area_triangle(self):
        '''area_triangle(площадь треугольника) = (a(основание) * h(высота)) / 2'''
        a = int()
        h = int()
        area_triangle = (a * h) / 2
        self.assertEqual(area_triangle == 3, a == 2, h == 3)

    def test_area_rectangle(self):
        '''area_rectangle(площадь прямоугольника) = a(сторона1) * b(сторона 2)'''
        a = int()
        b = int()
        area_rectangle = a * b
        self.assertEqual(area_rectangle == 15, a == 3, b == 5)

    def test_area_round(self):
        '''area_round(площадь круга) = pi * (r(радиус)**2)'''
        r = int()
        area_round = pi * (r**2)
        self.assertEqual(area_round == (pi * 9), r == 3)

    def test_area_righttriangle(self):
        '''area_righttriangle(площадь прямоугольного треугольника) = (a * b)(умножение катетов) / 2'''
        a = int()
        b = int()
        area_righttriangle = (a * b) / 2
        self.assertEqual(area_righttriangle == 5, a == 2, b == 5)

    def test_area_isoscelestriangle(self):
        '''area_isosceles triangle(площадь ровнобедренного треугольника) = 1/2 * b(основание) * h(высота)'''
        b = int()
        h = int()
        area_isosceles_triangle = 0.5 * b * h
        self.assertEqual(area_isosceles_triangle == 8, b == 4, h == 4)

    def test_perimeter_round(self):
        '''
        perimeter of round = pi(число Пи) * D(диаметр окружности),
        или = 2 * pi * r(радиус)
        '''
        D = int()
        perimeter_round = pi * D
        self.assertEqual(perimeter_round == pi * 12, D == 12)








if __name__ == '__main__':
    unittest.main()