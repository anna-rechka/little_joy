from drawbot_skia.drawbot import oval, saveImage
#    x    y   w    h
#oval(100, y+step, 550, 550)
saveImage('circle01.pdf')
step = 170
y = 100
for i in range(5):
    oval(100, y, 150, 150)
    y = y + step
saveImage('circle02.pdf')

