import pyautogui as p
import keyboard as k
from time import sleep

#variables
c = 0

#unpause game
p.click(1450, 391)

#mineBlocks
def mineBlock():
    p.mouseDown()
    sleep(1)
    p.mouseUp()
    sleep(0.8)

#walkForward
def walkForward():
    k.press('f')
    k.press('w')
    sleep(0.7)
    k.release('w')
    sleep(0.2)
    k.release('f')
    sleep(0.5)

#program begins
while c < 2:
    mineBlock()
    p.moveRel(0, 300)
    mineBlock()
    p.moveRel(0, -300)
    sleep(0.5)
    walkForward()
    #c += 1
