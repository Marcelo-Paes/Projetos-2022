from tkinter import *
from turtle import position
import pyautogui

import time
time.sleep(4)

repeticao=5
 

for i in range(repeticao):
    time.sleep(0.3)
    pyautogui.hotkey('ctrl','c')
    time.sleep(0.3)
    pyautogui.click(424,8)
    time.sleep(0.3)
    pyautogui.click(496,498)
    time.sleep(0.3)
    pyautogui.hotkey('ctrl','a')
    time.sleep(0.3)
    pyautogui.press('del')
    time.sleep(0.3)
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.3)
    pyautogui.click(693,493)
    time.sleep(0.3)
    time.sleep(0.3)
    pyautogui.click(534,623)
    time.sleep(0.3)
    pyautogui.click(186,9)
    time.sleep(0.3)
    pyautogui.press('right')

    pyautogui.hotkey('ctrl','shift','v')

    pyautogui.press('enter')

    pyautogui.press('left')

    pyautogui.press('-')

    pyautogui.press('enter')

    pyautogui.press('left')







    