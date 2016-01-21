import ImageGrab
import os
import time
# Globals
# ------------------
 
x_pad = 464
y_pad = 220

def screenGrab():
    box = (x_pad+1,y_pad+1,x_pad + 640,y_pad + 482)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()