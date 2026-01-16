from pynput.keyboard import Controller #swapped it again
from PIL import ImageGrab
import time

#positions
#X:  493 Y:  731 RGB: (NaN, NaN, NaN)
#X:  643 Y:  731 RGB: (NaN, NaN, NaN)
#X:  793 Y:  731 RGB: (NaN, NaN, NaN)
#X:  945 Y:  731 RGB: (NaN, NaN, NaN)

#TODO figure out logic for button presses and detection
#TODO collect images/colors for open cv to detect
# color code is :r 255 g 255 b 60

#initialize 
kbd = Controller()

#list
LANES = [
    (493,750,'d'), # stands for lane # : (x coord, y coord, button)
    (643,750,'f'),
    (793,750,'j'),
    (945,750,'k')
]

COLOR_TARGET = (255,255,60) # in (red, green, blue)

def checkColor(rgb):
    r,g,b=rgb[:3]
    
    #added tolerance here just in case
    return(abs(r-COLOR_TARGET[0]) <50 and
           abs(g-COLOR_TARGET[1]) <50 and
           abs(b-COLOR_TARGET[2]) <50)

while True: # who needs safeties lmao
    img = ImageGrab.grab()
    pixel = img.load()
    
    for x,y,key in LANES:
        print(pixel[x,y])
        if checkColor(pixel[x,y]):
            print(f'pressed {key}')
            kbd.press(key)
            kbd.release(key)
        time.sleep(0.001)