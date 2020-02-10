"""
This test will initialize the display using displayio and draw a solid green
background, a smaller purple rectangle, and some yellow text.
"""
import time
import board
from adafruit_circuitplayground import cp
from adafruit_gizmo import tft_gizmo
from adafruit_turtle import turtle, Color

print("Turtle time! Lets draw a square with dots")
display = tft_gizmo.TFT_Gizmo()
turtle = turtle(display)

turtle.pendown()

while True:
    if cp.button_a:
        print("Button A pressed!")
        turtle.right(15)
        time.sleep(.1)
        pass
    if cp.button_b:
        print("Button B pressed!")
        if cp.switch:
            turtle.forward(10)
            time.sleep(.1)
        else:
            turtle.backward(10)
            time.sleep(.1)
        pass
    pass
