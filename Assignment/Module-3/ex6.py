from turtle import *

def draw_square(length):
    for _ in range(4):
        forward(length)
        right(90)

def draw_circle(radius):
    circle(radius)
    right(90)

draw_square(100)
draw_circle(50)

print("Drawing Completed Successfully....!!")