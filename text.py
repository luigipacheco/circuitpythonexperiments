"""
This test will initialize the display using displayio and draw a solid green
background, a smaller purple rectangle, and some yellow text.
"""
import board
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_gizmo import tft_gizmo

# Create the TFT Gizmo display

display = tft_gizmo.TFT_Gizmo()

# Set text, font, and color
text = "HELLO WORLD"
font = terminalio.FONT
color = 0x0000FF

# Create the test label
text_area = label.Label(font, text=text, color=color)

# Set the location
text_area.x = 50
text_area.y = 80

# Show it
display.show(text_area)

while True:
    pass
