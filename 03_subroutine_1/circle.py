# Write a program that takes a circle's radius from user, 
# then reports the area and the circumference of the circle with two decimal places.

import math
def circle_circumference(radius):
    return 2*math.pi*radius
def circle_area(radius):
    return math.pi*radius**2

radius = float(input("Enter circle radius: "))
circumference = circle_circumference(radius)
area = circle_area(radius)
print(f"Circle circumference is {circumference:<.2f}")
print(f"Circle area is {area:<.2f}")