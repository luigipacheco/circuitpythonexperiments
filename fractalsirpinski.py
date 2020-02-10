"""
This test will initialize the display using displayio and draw a solid green
background, a smaller purple rectangle, and some yellow text.
"""
import time
import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_imageload
from adafruit_gizmo import tft_gizmo
from adafruit_turtle import turtle, Color

print("Turtle time! Lets draw a square with dots")
display = tft_gizmo.TFT_Gizmo()
turtle = turtle(display)

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2) #find midpoint

def triangle(points, depth):

    turtle.penup()
    turtle.goto(points[0][0], points[0][1])
    turtle.pendown()
    turtle.goto(points[1][0], points[1][1])
    turtle.goto(points[2][0], points[2][1])
    turtle.goto(points[0][0], points[0][1])

    if depth > 0:
        triangle([points[0],
                  getMid(points[0], points[1]),
                  getMid(points[0], points[2])],
                 depth-1)
        triangle([points[1],
                  getMid(points[0], points[1]),
                  getMid(points[1], points[2])],
                 depth-1)
        triangle([points[2],
                  getMid(points[2], points[1]),
                  getMid(points[0], points[2])],
                 depth-1)

big = min(display.width / 2, display.height / 2)
little = big / 1.4
seed_points = [[-big, -little],[0,big],[big,-little]] #size of triangle
triangle(seed_points,4)

while True:
    pass
