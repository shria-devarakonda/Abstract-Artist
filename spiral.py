from turtle import *
import random
t = Turtle()

setup(500, 500)

t.hideturtle()
t.speed(0)
for i in range(500):
# try forward(i) or forward(2 * i) for more intricate stuff
    t.forward(5 * i)
    t.right(random.randrange(50, 360, 5))
