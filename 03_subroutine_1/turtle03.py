LAB = "turtlelab3.py"
import urllib.request,pathlib
pathlib.Path(LAB).exists() or urllib.request.urlretrieve(f"https://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab3 import turtle,home,check
from math import sqrt,atan,degrees

turtle.left(degrees(atan(home.y/home.x)))
turtle.forward(sqrt(home.x**2 + home.y**2))

check()
