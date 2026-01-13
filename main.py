from pynput.keyboard import Controller
import pyautogui #using this instead of win32api
import keyboard

#positions
#X:  493 Y:  731 RGB: (NaN, NaN, NaN)
#X:  643 Y:  731 RGB: (NaN, NaN, NaN)
#X:  793 Y:  731 RGB: (NaN, NaN, NaN)
#X:  945 Y:  731 RGB: (NaN, NaN, NaN)

#TODO figure out logic for button presses and detection
#TODO collect images/colors for open cv to detect
# color code is :r 255 g 255 b 60

def click(lane):
    if(lane == 1):
        pyautogui.press("d")
    elif(lane == 2):
        pyautogui.press("f")
    elif(lane == 3):
        pyautogui.press("j")
    elif(lane == 4):
        pyautogui.press("k")

while not keyboard.is_pressed('q'): #to quit out of the bot use q
    if pyautogui.pixel(493,731) == (255,255,60):
        print('lane 1')
    if pyautogui.pixel(643,731) == (255,255,60):
        print('lane 2')
    if pyautogui.pixel(793,731) == (255,255,60):
        print('lane 3')
    if pyautogui.pixel(945,731) == (255,255,60):
        print('lane 4')