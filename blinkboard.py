import os, string
from time import sleep

"""

BLINK 2.0
This project allows you to blink your keyboard LEDs in morse code

To try it out, set DEMO_TEXT and INPUT_NAME

Demo text can be any string
INPUT_NAME should be a keyboard LED name. You can see available ones by running:
   ls /sys/class/leds | grep input

Default value for my PC is input3::capslock

You can also use this as a module in other projects! First, drop this file into your project. Then add this line:
import blinkboard

Then, call the module with a string input like so:
blinkboard.parseInput("Super cool string")

"""

DEMO_TEXT  = "!fuck"
INPUT_NAME = "input3::capslock"

def _DASH(): 
	os.system(f"sudo sh -c 'echo 1 > /sys/class/leds/{INPUT_NAME}/brightness'")
	sleep(0.7)
	os.system(f"sudo sh -c 'echo 0 > /sys/class/leds/{INPUT_NAME}/brightness'")
	_BREAK();

def _DOT():
	os.system(f"sudo sh -c 'echo 1 > /sys/class/leds/{INPUT_NAME}/brightness'")
	sleep(0.1)
	os.system(f"sudo sh -c 'echo 0 > /sys/class/leds/{INPUT_NAME}/brightness'")
	_BREAK();

def _SPACE(): sleep(0.6) # Pause between words
def _LETTER(): sleep(0.3) # Pause between letters
def _BREAK(): sleep(0.1) # Pause between symbols in the same letter

def a(): _DOT(); _DASH()
def b(): _DASH(); _DOT();  _DOT(); _DOT()
def c(): _DASH(); _DOT(); _DASH(); _DOT()
def d(): _DASH(); _DOT(); _DOT()
def e(): _DOT();
def f(): _DOT(); _DOT(); _DASH(); _DOT();
def g(): _DASH(); _DASH(); _DOT();
def h(): _DOT(); _DOT(); _DOT(); _DOT();
def i(): _DOT(); _DOT()
def j(): _DOT(); _DASH(); _DASH(); _DASH()
def k(): _DASH(); _DOT(); _DASH()
def l(): _DOT(); _DASH(); _DOT(); _DOT()
def m(): _DASH(); _DASH()
def n(): _DASH(); _DOT();
def o(): _DASH(); _DASH(); _DASH()
def p(): _DOT(); _DASH(); _DASH(); _DOT() 
def q(): _DASH(); _DASH(); _DOT(); _DASH()
def r(): _DOT(); _DASH(); _DOT()
def s(): _DOT(); _DOT(); _DOT()
def t(): _DASH()
def u(): _DOT(); _DOT(); _DASH()
def v(): _DOT(); _DOT(); _DOT(); _DASH()
def w(): _DOT(); _DASH(); _DASH()
def x(): _DASH(); _DOT(); _DOT(); _DASH()
def y(): _DASH(); _DOT(); _DASH(); _DASH(); 
def z(): _DASH(); _DASH(); _DOT(); _DOT()

def parseInput(input):
	for char in input: 
		if not char in string.ascii_letters: pass
		if char != " ": 
			if char.lower() in string.ascii_lowercase: exec("%s()"%char.lower()); _LETTER()

		else: _SPACE()

# Demo
if __name__ == "__main__": parseInput(DEMO_TEXT)