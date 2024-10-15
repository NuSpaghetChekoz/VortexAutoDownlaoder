from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import os
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Change the directory if needed
counter_mod=0;
# Verify the existence of the files.
download_path = 'images/download.png'
sdownload_path = 'images/sdownload.png'

if not os.path.isfile(download_path):
    print(f"File {download_path} not found.")
else:
    print(f"File {download_path} found.")

if not os.path.isfile(sdownload_path):
    print(f"File {sdownload_path} not found.")
else:
    print(f"File {sdownload_path} found.")
#Set the region of the screen where the program try to find on screen buttons to press like "Dowload" and "Slow Downlaod"
region_download = (1100,300,200,150)
region_slow = (900,600,300,250)

while True:
    try:
        # It searches for the vortex "download" button. Then click.
        download_location = pyautogui.locateOnScreen(download_path, region=region_download, grayscale=True, confidence=0.6) #region: is the region where he has to search. "grayscale" if you have to take the locate in grayscale or not. "confidence" how precise the correspondence must be between the input image and what python sees
        if download_location is not None:
            print("Found download.png")
            pyautogui.click(pyautogui.center(download_location))
            time.sleep(4)  # Waiting time for the next step.

        button_location = pyautogui.locateOnScreen('sdownload.png')

        if button_location: 
            button_point = pyautogui.center(button_location)
            pyautogui.click(button_point)
            print("Found sdowndload.png")
            counter_mod += 1
            print("Mod successful downloaded:", counter_mod)
            time.sleep (8) 

    except Exception as e:
        print(f"An error occurred: {e}")
        screenshot = pyautogui.screenshot(region =(900,600,300,250))
        screenshot.save('screenshot_test.png')
    time.sleep(0.5)  # Tempo di attesa prima del prossimo controllo
