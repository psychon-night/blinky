import os, sys

# You can ignore this class, it's just utility functions
class alphabetMap():
	def a(): os.system(sys.path[0] + "/bin/alphabet/a")
	def b(): os.system(sys.path[0] + "/bin/alphabet/b")
	def c(): os.system(sys.path[0] + "/bin/alphabet/c")
	def d(): os.system("bash " + sys.path[0] + "/bin/alphabet/d")
	def e(): os.system("bash " + sys.path[0] + "/bin/alphabet/e")
	def f(): os.system("bash " + sys.path[0] + "/bin/alphabet/f")
	def g(): os.system("bash " + sys.path[0] + "/bin/alphabet/g")
	def h(): os.system("bash " + sys.path[0] + "/bin/alphabet/h")
	def i(): os.system("bash " + sys.path[0] + "/bin/alphabet/i")
	def j(): os.system("bash " + sys.path[0] + "/bin/alphabet/j")
	def k(): os.system("bash " + sys.path[0] + "/bin/alphabet/k")
	def l(): os.system("bash " + sys.path[0] + "/bin/alphabet/l")
	def m(): os.system("bash " + sys.path[0] + "/bin/alphabet/m")
	def n(): os.system("bash " + sys.path[0] + "/bin/alphabet/n")
	def o(): os.system("bash " + sys.path[0] + "/bin/alphabet/o")
	def p(): os.system("bash " + sys.path[0] + "/bin/alphabet/p")
	def q(): os.system("bash " + sys.path[0] + "/bin/alphabet/q")
	def r(): os.system("bash " + sys.path[0] + "/bin/alphabet/r")
	def s(): os.system("bash " + sys.path[0] + "/bin/alphabet/s")
	def t(): os.system("bash " + sys.path[0] + "/bin/alphabet/t")
	def u(): os.system("bash " + sys.path[0] + "/bin/alphabet/u")
	def v(): os.system("bash " + sys.path[0] + "/bin/alphabet/v")
	def w(): os.system("bash " + sys.path[0] + "/bin/alphabet/w")
	def x(): os.system("bash " + sys.path[0] + "/bin/alphabet/x")
	def y(): os.system("bash " + sys.path[0] + "/bin/alphabet/y")
	def z(): os.system("bash " + sys.path[0] + "/bin/alphabet/z")
	def space(): os.system(sys.path[0] + "/bin/split")

def parseInput(input):
	for char in input: 
		if char != " ": exec("alphabetMap.%s()"%char)
		else: exec("alphabetMap.space()")

def getInputClassName():
	# List available LEDs
	# If this says "input2" for example, go to /bin/long and replace /sys/class/leds/input3::capslock/brightness with /sys/class/leds/input2::capslock/brightness'
	# Do the same for /bin/short

	os.system("ls /sys/class/leds/ | grep input")

def setExecBit():
	# Automatically configures the files to be executable
	os.system("chmod +x %s/bin/long %s/bin/short"%sys.path[0])
	os.system("cd %s/bin/alphabet && chmod +x *"%sys.path[0])

# Uncomment to print available inputs
"""getInputClassName()"""

# Uncomment to set the files to executable. You need to do this if you get `permission denied` errors
"""setExecBit()"""

# Smack any string into this and turn it into morse code!
parseInput("hello world")
