#!/opt/homebrew/bin/python3

import pynput.mouse
from pynput.keyboard import Key, Listener
from time import sleep
from datetime import datetime
import sys

if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numSeconds = 60
else:
    numSeconds = int(sys.argv[1])

global it, stopMotion
it = 0
stopMotion = False


def on_move(x, y):
    #print('Pointer moved to {0}'.format((x, y)))
    global it
    it = 0

def on_click(x, y, button, pressed):
    #print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    global it, stopMotion
    it = 0
    stopMotion = True	

def on_scroll(x, y, dx, dy):
    #print('Scrolled {0}'.format((x, y)))
    global it, stopMotion
    it = 0
    stopMotion = True	

def on_press(key):
    #print('{0} pressed'.format(key))
    global it, stopMotion
    it = 0
    stopMotion = True	

def on_release(key):
    #print('{0} release'.format(key))
    global it, stopMotion
    it = 0
    stopMotion = True	

# register events 
mouselistener = pynput.mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll
	) 

kblistener = Listener(
        on_press=on_press,
	on_release=on_release,
	) 

#Start listeners for events
mouselistener.start()
kblistener.start()
import pyautogui
pyautogui.FAILSAFE = False

def jiggle():
	global stopMotion
	loop = 0
	while(loop < 5):
		for i in range(0, 60):
			pyautogui.move(0, 5)
			sleep(.001)
			if stopMotion:
				break
		for i in range(0, 60):
			pyautogui.move(0, -5)
			sleep(.001)
			if stopMotion:
				break
		loop = loop + 1
while(True):
	sleep(1)
	it = it + 1
	#print("slept " + str(it))
	if (it > numSeconds):
		stopMotion = False
		print("Jiggled at {}".format(datetime.now().time()))
		jiggle()
		it = 0

mouselistener.stop()
kblistener.stop()
