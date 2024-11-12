import math

class Rectangle:
    length = 20
    breadth = 10

R1 = Rectangle()
print(R1.length)
print(R1.breadth)

area = R1.length*R1.breadth
print(area)

class Circle:
    def cal_Area(self, radius):
        Radius = radius
        print("Radius: ", radius)
        area = math.pi*(Radius**2)
        return area
    
oj = Circle()
areaCircle = oj.cal_Area(5)
print(areaCircle)