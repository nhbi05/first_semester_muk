import math

def area_circle(r):
    A1 = math.pi * r * r
    return A1

def area_square(l):
    A2 = l*l
    return A2

circle_area = area_circle(3)
square_area = area_square(3)
print ("The area of the circle is: ", circle_area)
print ("The area of the circle is: ", square_area)
