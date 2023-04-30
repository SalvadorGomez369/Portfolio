# python script for the page drive.google.com that lets you create ne folders out of a list
# in order to work properly, you must have this configuration:
# this is done with 100% browser zoom level
# have the google drive page open in your browser
# configurate the code acording to your browser

import pyautogui
import time

# The list of folder names to create
folder_names = ['Folder 1', 'Folder 2', 'Folder 3']

# Locate the Firefox window
firefox_window = pyautogui.getWindowsWithTitle('Mozilla Firefox')[0]

# Locate the Google Chrome window (do it with google Chrome)
#chrome_window = pyautogui.getWindowsWithTitle('Google Chrome')[0]

# Activate the Firefox windowFolder 3
firefox_window.activate()

# Activate the Google Chrome window (do it with google Chrome)
#chrome_window.activate()

# Wait for the window to activate
pyautogui.sleep(1)

# Move the cursor to coordinates (x=90, y=180)
pyautogui.moveTo(90, 180)

# Create each folder in the list
for folder_name in folder_names:
    # Type the folder name and press enter
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.typewrite(folder_name + '\n')
    time.sleep(2) # change it according to the speed of the internet,the (2) are seconds