#Annoy your bestfriends :p

import random
import string
import time

import pyautogui

number = int(input('Enter the number : ')) #Enter the number of random texts you want to send then,
open whatsapp web and move your cursor on the text area and Boom!! XD

time.sleep(5)

for _ in range(number):
    stri = string.ascii_lowercase
    message = ''.join(random.sample(stri,10))
    pyautogui.typewrite(message)
    pyautogui.press('Enter')
