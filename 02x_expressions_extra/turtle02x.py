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