import keyboard
import mouse
import time
from art import tprint

isClicking = False
isWorking = True


def exit_window():
    global isWorking
    isWorking = False


def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print(" OFF")
    else:
        isClicking = True
        print(" ON")


keyboard.add_hotkey('alt + z', set_clicker)
keyboard.add_hotkey('esc', exit_window)

tprint("autoclicker")
print("\n start/stop clicking: alt + z \n exit program: esc \n\n clicking status:")
while isWorking:
    if isClicking:
        mouse.double_click(button='left')
        time.sleep(0.01)
