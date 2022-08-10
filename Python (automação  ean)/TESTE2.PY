import pyautogui

import time
time.sleep(4)

repeticao=6

for i in range(repeticao):
    

    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('up')
    pyautogui.press('enter')

    with pyautogui.hold('shift'):
         pyautogui.press('left',5)

    pyautogui.hotkey('ctrl','c')

    pyautogui.press('enter')

    pyautogui.press('right')
    pyautogui.press('right')

    pyautogui.press('up')
    
    pyautogui.press('enter')

    pyautogui.press('left',3)

    with pyautogui.hold('shift'):
         pyautogui.press('left',5)

    pyautogui.hotkey('ctrl','v')

    pyautogui.press('enter')
    

    

    
    
    
    

    
