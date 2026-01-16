from pyautogui import *
import pyautogui
import time
import keyboard

COLOR = (255,255,60) # color
TOLERANCE = 30

def color_match(pixel_color, target_color, tol):
    sum = 0
    r1, g1, b1 = pixel_color
    r2, g2, b2 = target_color
    
    r_diff = abs(r1-r2)
    g_diff = abs(g1-g2)
    b_diff = abs(b1-b2)
    
    sum = r_diff + g_diff + b_diff
    
    return sum <=tol

def check_and_press(x,y,key):
    pixel = pyautogui.pixel(x,y)
    if color_match(pixel,COLOR,TOLERANCE):
        pyautogui.keyDown(key)
        print(f"{key} pressed at X: {x} Y: {y}")
        pyautogui.keyUp(key)

#X:  493 Y:  724 RGB: (NaN, NaN, NaN)
#X:  640 Y:  727 RGB: (NaN, NaN, NaN)
#X:  798 Y:  733 RGB: (NaN, NaN, NaN)
#X:  945 Y:  737 RGB: (NaN, NaN, NaN)

while True:
    check_and_press(493,724,'d')
    check_and_press(640,724,'f')
    check_and_press(798,724,'j')
    check_and_press(945,724,'k')