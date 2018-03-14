# Help guide Turtle back home. His home will always show up randomly in Quadrant I. 
# Unfortunately its exact location is not known until the program is started.
LAB = "turtlelab2.py"
import urllib.request,pathlib
pathlib.Path(LAB).exists() or urllib.request.urlretrieve(f"https://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab2 import turtle,home,check

turtle.forward(home.x)
turtle.left(90)
turtle.forward(home.y)
check()