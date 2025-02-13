from polygon import Polygon
from math import sqrt
class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def getArea(self):
        p = (self.a + self.b + self.c)/2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
    def getPerimeter(self):
        return self.a + self.b + self.c
triangule = Triangle(2,3,4)
print(triangule.getArea())
print(triangule.getPerimeter())