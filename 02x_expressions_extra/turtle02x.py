# Help guide Turtle back home while stop to buy food at a food shop along the way. 
# The shop will randomly appear in Quadrant I, and the home will always appear 
# randomly north-east of the shop.

# Unfortunately both home's and shop's exact locations are not known until the program starts.



LAB = "turtlelab2x.py"
import urllib.request,pathlib
pathlib.Path(LAB).exists() or urllib.request.urlretrieve(f"https://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab2x import turtle,home,shop,check

turtle.forward(shop.x)
turtle.left(90)
turtle.forward(shop.y)
turtle.forward(home.y - shop.y)
turtle.right(90)
turtle.forward(home.x - shop.x)
check()