import pyautogui
import win32gui
import time
from ahk import AHK
import cv2
import numpy as np
import os
    
    
def hold_click(duration_ms):
    #ahk = AHK(executable_path='C:\\Program Files\\AutoHotkey\\v1.1.37.01\\AutoHotkeyA32.exe')
    ahk = AHK(executable_path='C:\Program Files\AutoHotkey\AutoHotkeyA32.exe')
    
    with open("Script/drag.ahk", "r") as file:
        script = file.read().replace('%1%', str(duration_ms))
    
    ahk.run_script(script, blocking=False)

def simple_click():
    #ahk = AHK(executable_path='C:\\Program Files\\AutoHotkey\\v1.1.37.01\\AutoHotkeyA32.exe')
    ahk = AHK(executable_path='C:\Program Files\AutoHotkey\AutoHotkeyA32.exe')
    
    with open("Script/simple_click.ahk", "r") as file:
        script = file.read()
    
    ahk.run_script(script, blocking=False)


