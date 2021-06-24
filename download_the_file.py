from Xlib import X
import pyautogui
import time
import pyperclip
import pandas as pd

pyautogui.PAUSE = 2.5
#abrir aba do navegador
pyautogui.hotkey('alt', 'tab')

pyautogui.hotkey('ctrl', 't')

link = "https://drive.google.com/drive/folders/14oLE59U1RqyRqlBbKpsyymW-mitvbtoh"

pyperclip.copy(link)

pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(4)
pyautogui.click(x=356, y=376, clicks=1, button='right')
pyautogui.click(x=433, y=682)
pyautogui.click(x=593, y=493)
#pyautogui.click(x=1042, y=591)

#time.sleep(5)
#print(pyautogui.position())