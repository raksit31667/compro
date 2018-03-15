# A landlord is designing the area in front of his house 
# by placing a circular pond (สระน้ำรูปวงกลม) at the center, 
# and make the remaining area a lawn with grass (ทำพื้นที่ที่เหลือให้เป็นสนามหญ้า), as shown.

# Please help him calculate the area of the lawn (i.e., the green area) 
# from the values of x, y, and d. Note that the pond will always be smaller 
# than the available area. (สระน้ำจะไม่ใหญ่เกินพื้นที่ที่มีอยู่) The result must be displayed
#  with 2 decimal places.

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