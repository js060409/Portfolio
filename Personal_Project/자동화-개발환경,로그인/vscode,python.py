import pyautogui
import pyperclip
import time

id = str(input("id: "))
password = str(input("password: "))

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

time.sleep(3)

pyautogui.click(1236,863)

pyperclip.copy(id)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

pyperclip.copy(password)
time.sleep(3)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

time.sleep(6)
pyautogui.click(1234,865)

time.sleep(1)
pyautogui.click(477,74)
pyperclip.copy("https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

pyautogui.click(477,74)
pyperclip.copy("https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

time.sleep(10)
pyperclip.copy("C:\\Users\\ADMIN\\Downloads\\VSCodeUserSetup-x64-1.91.1.exe")
pyautogui.hotkey("win", "r")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

pyperclip.copy("C:\\Users\\ADMIN\\Downloads\\python-3.12.3-amd64.exe")
pyautogui.hotkey("win", "r")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

