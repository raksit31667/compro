import math
def all_area(width,length):
    return width*length

def circle_area(d):
    return math.pi*((d/2)**2)

x = float(input(("Enter x: ")))
y = float(input(("Enter y: ")))
d = float(input(("Enter d: ")))

lawn_area = all_area(x,y) - circle_area(d)
print(f"The area of the lawn is {lawn_area:<.2f} sq.m.")