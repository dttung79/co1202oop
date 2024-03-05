from circle import Circle
from rectangle import Rectangle
from square import Square


c1 = Circle('C1', 5) # create a Circle object named C1 with radius 5
print(c1) # Circle C1
print(f'Area: {c1.area()}') # 78.5
r1 = Rectangle('R1', 3, 4) # create a Rectangle object named R1 with width 3 and height 4
print(r1)
print(f'Area: {r1.area()}') # 12

s1 = Square('S1', 5) # create a Square object named S1 with side 5
print(s1)
print(f'Area: {s1.area()}') # 25
print(f'Size: {s1.side}')   # use the property side to get the side of the square