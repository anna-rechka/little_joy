from drawbot_skia.drawbot import *

x = 0
y = 0

for x in range (7):
    for y in range (7):
        oval(x*120, y*120, 100, 100)

saveImage("simpledots.pdf")
