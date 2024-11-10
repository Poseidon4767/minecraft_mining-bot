import pyautogui as p
import time
from time import sleep

def start_mine(duration):
    start_time = time.time()
    p.keyDown('w')
    p.keyDown('f')
    p.mouseDown(button='left')
    try:
        while time.time() - start_time < duration:
            sleep(0.1)
    finally:
        p.mouseUp(button='left')
        p.keyUp('w')
        p.keyUp('f')

def start_normal_sprinting(duration):
    start_time = time.time()
    p.keyDown('w')
    p.keyDown('r')
    try:
        while time.time() - start_time < duration:
            sleep(0.1)
    finally:
        p.keyUp('w')
        p.keyUp('r')

def start_sprinting_jumping(duration):
    start_time = time.time()
    p.keyDown('w')
    p.keyDown('r')
    p.keyDown('space')
    try:
        while time.time() - start_time < duration:
            sleep(0.1)
    finally:
        p.keyUp('w')
        p.keyUp('r')
        p.keyUp('space')

def prevent_afk_kick(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        p.keyDown('w')
        sleep(0.5)
        p.keyUp('w')
        sleep(0.1)
        p.keyDown('a')
        sleep(0.5)
        p.keyUp('a')
        sleep(0.1)
        p.keyDown('s')
        sleep(0.5)
        p.keyUp('s')
        sleep(0.1)
        p.keyDown('d')
        sleep(0.5)
        p.keyUp('d')
        sleep(0.1)

def auto_click(duration, gap=1):
    start_time = time.time()
    while time.time() - start_time < duration:
        p.click()
        sleep(gap)

def hold_click(duration, button):
    start_time = time.time()
    while time.time() - start_time < duration:
        p.mouseDown(button=button)
        sleep(duration)
        p.mouseUp(button=button)

print("\n\n**********Minecraft Bot**********\n")
print("Credits: Poseidon4767 for the ENTIRE code.\nGithub Profile: https://github.com/Poseidon4767\n\n")
while True:
    print("Please choose your option:"
          "\n1. Mine\n2. Sprint\n3. Sprint Jumping."
          "\n4. Prevent getting AFK kicked.\n5. Auto Click."
          "\n6. Hold Click.\n7. Quit")
    option = input()
    if option == '1':
        mine_duration = int(input("Enter the duration of mining in seconds: "))
        print("Please switch to Minecraft and wait for 5 seconds before bot starts mining...")
        sleep(5)
        start_mine(mine_duration)
    elif option == '2':
        sprint_duration = int(input("Enter the duration of sprinting in seconds: "))
        print("Please switch to Minecraft and wait for 5 seconds before bot starts sprinting...")
        sleep(5)
        start_normal_sprinting(sprint_duration)
    elif option == '3':
        sprint_duration = int(input("Enter the duration of sprinting in seconds: "))
        print("Please switch to Minecraft and wait for 5 seconds before bot starts sprinting...")
        sleep(5)
        start_sprinting_jumping(sprint_duration)
    elif option == '4':
        afk_duration = int(input("Enter the duration of AFK auto-moving in seconds: "))
        print("Please switch to Minecraft and wait for 5 seconds before bot starts preventing auto AFK movement...")
        sleep(5)
        prevent_afk_kick(afk_duration)
    elif option == '5':
        click_duration = int(input("Enter the duration of auto-clicking in seconds: "))
        gap = int(input("Enter the gap between clicks in seconds(default: 1 second): "))
        print("Please switch to Minecraft and wait for 5 seconds before bot starts auto-clicking...")
        sleep(5)
        auto_click(click_duration, gap)
    elif option == '6':
        click_duration = int(input("Enter the duration of holding mouse click in seconds: "))
        choice = int(input("1 for left, 2 for right: "))
        if choice == 1:
            button='left'
        elif choice == 2:
            button='right'
        print("Please switch to Minecraft and wait for 5 seconds before bot starts auto-clicking...")
        sleep(5)
        hold_click(click_duration, button)
    elif option == '7':
        print("Exiting...")
        break
    else:
        print("Invalid option selected.")