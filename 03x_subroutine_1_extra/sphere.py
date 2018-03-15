# Write a program that takes a sphere's radius from user, 
# then reports the volume and the surface area of the sphere with two decimal places.

import math
def sphere_volume(radius):
    return 4*math.pi*pow(radius,3)/3
def sphere_surface_area(radius):
    return 4*math.pi*pow(radius,2)

radius = float(input("Enter sphere radius: "))
volume = sphere_volume(radius)
surface_area = sphere_surface_area(radius)
print(f"Sphere volume is {volume:<.2f}")
print(f"Sphere surface area is {surface_area:<.2f}")