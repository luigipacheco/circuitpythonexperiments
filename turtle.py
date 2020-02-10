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

turtle = turtle(tft_gizmo.TFT_Gizmo())
turtle.pendown()

for _ in range(4):
    turtle.dot(2)
    turtle.left(90)
    turtle.forward(25)

while True:
    pass

# Add the Group to the Display
display.show(group)

# Set sprite location
group.x = 50
group.y = 50

# Loop through each sprite in the sprite sheet
source_index = 0
while True:
    sprite[0] = source_index % 6
    source_index += 1
    time.sleep(2)
