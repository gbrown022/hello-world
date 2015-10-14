from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

# get the turtle to draw a square
for x in range(4):
    fd(bob, 100)
    lt(bob)

wait_for_user()
