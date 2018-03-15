# Help guide Turtle back home as quickly as possible while stop 
# to buy food at a food shop along the way. 
# The shop will randomly appear in Quadrant I,
# and the home will always appear randomly north-east of the shop.

# Unfortunately both home's and shop's exact locations are not known until the program starts.

LAB = "turtlelab3x.py"
import urllib.request,pathlib
pathlib.Path(LAB).exists() or urllib.request.urlretrieve(f"https://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab3x import turtle,home,shop,check
from math import sqrt,atan,degrees
shop_degrees = degrees(atan(shop.y/shop.x))
turtle.left(shop_degrees)
turtle.forward(sqrt(shop.x**2 + shop.y**2))
home_degrees = degrees(atan(home.y/home.x))
turtle.right(shop_degrees)
turtle.left(home_degrees)
turtle.forward(sqrt((home.x-turtle.x)**2 + (home.y-turtle.y)**2))
check()