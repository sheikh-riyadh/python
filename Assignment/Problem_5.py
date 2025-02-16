import pyautogui
from time import sleep

value = int(input("Please enter number: "))

sleep(5)

for num in range(1, value + 1):
    pyautogui.write("#" *num)
    pyautogui.write("\n")

