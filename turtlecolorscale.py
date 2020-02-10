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

def hilbert2(step, rule, angle, depth, t):
    if depth > 0:
        a = lambda: hilbert2(step, "a", angle, depth - 1, t)
        b = lambda: hilbert2(step, "b", angle, depth - 1, t)
        left = lambda: t.left(angle)
        right = lambda: t.right(angle)
        forward = lambda: t.forward(step)
        if rule == "a":
            left(); b(); forward(); right(); a(); forward(); a(); right(); forward(); b(); left()
        if rule == "b":
            right(); a(); forward(); left(); b(); forward(); b(); left(); forward(); a(); right()

turtle = turtle(display)
turtle.penup()

turtle.goto(-80, -80)
turtle.pendown()
hilbert2(5, "a", 90, 5, turtle)

while True:
    pass
