# Name: Ivy Loi
# Class Section: 3
# File Purpose: To Test the functions in the modules I have made

from mathematics import whoami as math_whoami
from mathematics.numbers import *
from mathematics.numbers import simple
from mathematics.geometry import *
from mathematics.geometry import rectangle

print ("Main package name:", math_whoami.getname())

print("\nNumbers whoami:", numbers_whoami.getname())
print("Sum:", series.sum_total(total = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("Average:", series.average(avg = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("Addition:", simple.addition(left = 7, right = 7))
print("Subtraction:", simple.subtraction(left = 2, right = 7))
print("Multiplication:", simple.multiplication(left = 5, right = -2))
print("Division:", simple.division(left = 2, right = 7))

print("\nGeometry whoami:", whoami.getname())
print("Rectangle perimeter:", rectangle.perimeter(length = 7, width = 2))
print("Rectangle area:", rectangle.area(length = 7, width = 7))
print("Circle circumference:", circle.circumference(radius = 9))
print("Circle area:", circle.area(radius = 3))
print("Cube surface area:", cube.surface_area(side = 10))
print("Cube volume:", cube.volume(side = 2))
