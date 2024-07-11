import pyautogui
import pyperclip
import time
pyperclip.copy("C:\\Users\\ADMIN\\AppData\\Local\\Google\\Chrome")
pyautogui.hotkey("win", "r")

pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("delete")
pyautogui.hotkey("enter")

pyautogui.hotkey("ctrl", "w")

time.sleep(0.5)

pyautogui.hotkey("win")
pyperclip.copy("Chrome")
pyautogui.hotkey("ctrl", "v")

time.sleep(0.5)

pyautogui.hotkey("enter")
