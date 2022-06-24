import time
import pyautogui

while True:
    pyautogui.click()
    pyautogui.move(100,0,0.5)
    pyautogui.move(-100,0,0.5)
    pyautogui.click()
    time.sleep(60)