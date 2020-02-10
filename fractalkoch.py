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

generation_colors = [Color.RED, Color.BLUE, Color.GREEN]

def f(side_length, depth, generation):
    if depth == 0:
        side = turtle.forward(side_length)
    else:
        side = lambda: f(side_length / 3, depth - 1, generation + 1)
        side()
        turtle.left(60)
        side()
        turtle.right(120)
        side()
        turtle.left(60)
        side()

def snowflake(num_generations, generation_color):
    top_side = lambda: f(top_len, num_generations, 0)
    turtle.pencolor(generation_color)
    top_side()
    turtle.right(120)
    top_side()
    turtle.right(120)
    top_side()


unit= min(display.width / 3, display.height / 4)
top_len = unit * 3
print(top_len)
turtle.penup()
turtle.goto(-1.5 * unit, unit)
turtle.pendown()

for generations in range(3):
    snowflake(generations, generation_colors[generations])
    turtle.right(120)

while True:
    pass
