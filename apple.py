from drawbot_skia.drawbot import *
def apple (x,y):
    polygon((x+20, y+30), (x+40, y+10), (x+50, y+17), (x+60, y+10), (x+80, y+20), (x+88, y+47), (x+80, y+70), (x+60, y+80), (x+50, y+70), (x+80, y+110), (x+77, y+110), (x+60, y+87), (x+40, y+97), (x+25, y+94), (x+33, y+85), (x+57, y+83), (x+47, y+70), (x+35, y+75), (x+20, y+63), (x+17, y+50), close=True)
#        1         2         3         4         5         6         7         8         9         10        11         12         13         14        15         16         17        18        19        20

for x in range(7):
    for y in range(7):
        apple(x*140, y*140)


saveImage('multy_apple.pdf')

#multy apple