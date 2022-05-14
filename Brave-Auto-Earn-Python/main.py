import os
import pyautogui
import time
import random
import colorama
from colorama import *

orange = '\33[31m'

os.system('cls')

print("")

print(orange +"██████╗░██████╗░░█████╗░██╗░░░██╗███████╗   ░█████╗░██╗░░░██╗████████╗░█████╗░   ███████╗░█████╗░██████╗░███╗░░██╗" + orange)
print(orange +"██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔════╝   ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗   ██╔════╝██╔══██╗██╔══██╗████╗░██║" + orange)
print(orange +"██████╦╝██████╔╝███████║╚██╗░██╔╝█████╗░░   ███████║██║░░░██║░░░██║░░░██║░░██║   █████╗░░███████║██████╔╝██╔██╗██║" + orange)
print(orange +"██╔══██╗██╔══██╗██╔══██║░╚████╔╝░██╔══╝░░   ██╔══██║██║░░░██║░░░██║░░░██║░░██║   ██╔══╝░░██╔══██║██╔══██╗██║╚████║" + orange)
print(orange +"██████╦╝██║░░██║██║░░██║░░╚██╔╝░░███████╗   ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝   ███████╗██║░░██║██║░░██║██║░╚███║" + orange)
print(orange +"╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝   ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░   ╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝" + orange)


print("")
cycles = int(input("Enter the number of times you want to run the script (use  a high number for most effective results) : "))

print('Make sure to have pasted the complete path to the brave executable in the location.txt file')
time.sleep(2)

with open("location.txt") as f:
    location = f.read()
    if sys.platform == "win32":
        os.startfile(location)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, location])

os.startfile(location)

i = 1

while i <= (cycles):

    
    ran_search = ['Brave ','Bitcoin ','Earn money ','Privacy ','Brave browser ','Brave browser 2022 ','Best browser ','Brave browser review ','Respectful browsing ','What is brave ']
    time.sleep(3)
    pyautogui.write(random.choice(ran_search)) #Enters a search in the engine
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    print('Search completed')
    pyautogui.click(1682,807) #Clicks on advert when present
    time.sleep(2)

    pyautogui.click(329,17) #Opens new brave tab
    time.sleep(3)
    print('New tab opened')
    pyautogui.click(289,18) #Closes first brave tab
    time.sleep(3)
    print('First tab closed')
    time.sleep(3)
    i = i+1
    print("A Cycle has completed successfully!")
    print("")

while i > (cycles):
    pyautogui.write("That's all folks!")
    print("That's all folks!")
    raise SystemExit
