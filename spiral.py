from turtle import *
import random
t = Turtle()

setup(500, 500)

t.hideturtle()
t.speed(0)
for i in range(500):
    t.forward(5 * i)
    t.right(random.randrange(50, 360, 5))
