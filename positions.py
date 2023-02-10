import pyautogui as pt
from time import sleep
while True:
    posyXY = pt.position() # Gives the coordinates of your mouse pointer
    print(posyXY,pt.pixel(posyXY[0],posyXY[1])) # Prints the coordinates x,y
    sleep(1)
    if posyXY[0]==0:
        break

