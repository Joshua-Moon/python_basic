import turtle
import time
t1 = turtle.Turtle()
t1.shape("turtle")
i = 1
while i <= 4:
    t1.forward(100)
    t1.left(90)
    i = i + 1
    time.sleep(5)
