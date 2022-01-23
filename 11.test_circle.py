import unittest
from circle import getArea, getPerimeter

class Circle_Test(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(5), 78.53975)
        self.assertAlmostEqual(getArea(10), 314.159)
    def test_perimeter(self):
        self.assertAlmostEqual(getPerimeter(5), 31.4159)

unittest.main()
