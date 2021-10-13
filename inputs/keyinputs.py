import keyboard
import os
import json
from time import sleep
from tkinter import END

try:
	if os.path.exists(os.getcwd() + '/collections/keybinds.json'):
		# if json file exist, read it!
		with open("./collections/keybinds.json") as f:
			keybindData = json.load(f)
	# Read
	UP = keybindData["Move Up"]
	DOWN = keybindData["Move Down"]
	LEFT = keybindData["Move Left"]
	RIGHT = keybindData["Move Right"]
	JUMP = keybindData["Jump"]
	DODGE = keybindData["Dodge"]
	THROW = keybindData["Throw"]
	PICKUP = keybindData["Pickup"]
	LightAttack = keybindData["Quick Attack"]
	HeavyAttack = keybindData["Heavy Attack"]
except Exception:
	pass


def RightLeftRelease():
	if keyboard.is_pressed(RIGHT) == True:
		# print("Release key RIGHT")
		keyboard.release(RIGHT)
	if keyboard.is_pressed(LEFT) == True:
		# print("Release key LEFT")
		keyboard.release(LEFT)

def RightLeftReverse():
	if keyboard.is_pressed(RIGHT) == True:
		# print("[Reverse]: Press key LEFT")
		keyboard.press(LEFT)
		keyboard.release(LEFT)
	if keyboard.is_pressed(LEFT) == True:
		# print("[Reverse]: Press key RIGHT")
		keyboard.press(RIGHT)
		keyboard.release(RIGHT)

def UpDownReease():
	if keyboard.is_pressed(UP) == True:
		# print("Release key UP")
		keyboard.release(UP)
	if keyboard.is_pressed(DOWN) == True:
		# print("Release key DOWN")
		keyboard.release(DOWN)

def outputConsole(output, content):
	output.delete("1.0", END)
	output.insert("end", content)

# Heavy Attack
def NSig(output):
	if keyboard.is_pressed(RIGHT) == True:
		outputConsole(output, "[User] Side Sig [Input: Key Right]\n")
		keyboard.press(UP)
		keyboard.press(HeavyAttack)
		keyboard.release(UP)
		keyboard.release(HeavyAttack)
	elif keyboard.is_pressed(LEFT) == True:
		outputConsole(output, "[User] Side Sig [Input: Key Left]\n")
		keyboard.press(UP)
		keyboard.press(HeavyAttack)
		keyboard.release(UP)
		keyboard.release(HeavyAttack)
	else:
		outputConsole(output, "[Macro] Neutral Sig [Auto]\n")
		keyboard.press(HeavyAttack)
		keyboard.release(HeavyAttack)

def DSig(output):
	if keyboard.is_pressed(DOWN) == True:
		outputConsole(output, "[User] Down Sig [Input: Key Down]\n")
		keyboard.press(HeavyAttack)
		keyboard.release(HeavyAttack)
	else:
		outputConsole(output, "[Macro] Down Sig [Auto]\n")
		keyboard.press(DOWN)
		keyboard.press(HeavyAttack)
		keyboard.release(DOWN)
		keyboard.release(HeavyAttack)

def SSig(output):
	if keyboard.is_pressed(RIGHT) == True:
		outputConsole(output, "[User] Side Sig [Input: Key Right]\n")
		keyboard.press(HeavyAttack)
		keyboard.release(HeavyAttack)
	elif keyboard.is_pressed(LEFT) == True:
		outputConsole(output, "[User] Side Sig [Input: Key Left]\n")
		keyboard.press(HeavyAttack)
		keyboard.release(HeavyAttack)
	else:
		outputConsole(output, "[Macro] Side Sig Failed [Input Not Provided]\n")

# Light Attacks
def NLight(output):
	if keyboard.is_pressed(RIGHT) == True:
		outputConsole(output, "[User] Side Light [Input: Key Right]\n")
		keyboard.press(UP)
		keyboard.press(LightAttack)
		keyboard.release(UP)
		keyboard.release(LightAttack)
	elif keyboard.is_pressed(LEFT) == True:
		outputConsole(output, "[User] Side Light [Input: Key Left]\n")
		keyboard.press(UP)
		keyboard.press(LightAttack)
		keyboard.release(UP)
		keyboard.release(LightAttack)
	else:
		outputConsole(output, "[Macro] Neutral Light [Auto]\n")
		keyboard.press(LightAttack)
		keyboard.release(LightAttack)

def DLight(output):
	if keyboard.is_pressed(DOWN) == True:
		outputConsole(output, "[User] Down Light [Input: Key Down]\n")
		keyboard.press(LightAttack)
		keyboard.release(LightAttack)
	elif keyboard.is_pressed(RIGHT) == True:
		outputConsole(output, "[User] Down Light [Input: Key Right]\n")
		keyboard.press(DOWN)
		keyboard.press(LightAttack)
		keyboard.release(DOWN)
		keyboard.release(LightAttack)
	elif keyboard.is_pressed(LEFT) == True:
		outputConsole(output, "[User] Down Light [Input: Key Left]\n")
		keyboard.press(DOWN)
		keyboard.press(LightAttack)
		keyboard.release(DOWN)
		keyboard.release(LightAttack)
	else:
		outputConsole(output, "[Macro] Down Light [Auto]\n")
		keyboard.press(DOWN)
		keyboard.press(LightAttack)
		keyboard.release(DOWN)
		keyboard.release(LightAttack)

def SLight(output):
	if keyboard.is_pressed(RIGHT) == True:
		outputConsole(output, "[User] Side Light [Input: Key Right]\n")
		keyboard.press(LightAttack)
		keyboard.release(LightAttack)
	elif keyboard.is_pressed(LEFT) == True:
		outputConsole(output, "[User] Side Light [Input: Key Left]\n")
		keyboard.press(LightAttack)
		keyboard.release(LightAttack)
	else:
		outputConsole(output, "[Macro] Side Light Failed [Input Not Provided]\n")

# Aerial Attacks
def Recovery(output):
	outputConsole(output, "[Macro] Recovery [Auto]\n")
	keyboard.press(HeavyAttack)
	keyboard.release(HeavyAttack)

def GroundPound(output):
	if keyboard.is_pressed(DOWN) == True:
		outputConsole(output, "[User] GroundPound [Input: Key Down]\n")
		keyboard.press(HeavyAttack)
		keyboard.release(HeavyAttack)
	else:
		outputConsole(output, "[Macro] GroundPound [Auto]\n")
		keyboard.press(DOWN)
		keyboard.press(HeavyAttack)
		keyboard.release(DOWN)
		keyboard.release(HeavyAttack)

def NAir(output):
	if keyboard.is_pressed(RIGHT) == True:
		outputConsole(output, "[User] Neutral Air [Input: Key Right]\n")
		keyboard.press(UP)
		keyboard.press(LightAttack)
		keyboard.release(UP)
		keyboard.release(LightAttack)
	elif keyboard.is_pressed(LEFT) == True:
		outputConsole(output, "[User] Neutral Air [Input: Key Left]\n")
		keyboard.press(UP)
		keyboard.press(LightAttack)
		keyboard.release(UP)
		keyboard.release(LightAttack)
	else:
		outputConsole(output, "[Macro] Neutral Air [Auto]\n")
		keyboard.press(UP)
		keyboard.press(LightAttack)
		keyboard.release(UP)
		keyboard.release(LightAttack)

def DAir(output):
		outputConsole(output, "[Macro] Down Air [Auto]\n")
		keyboard.press(DOWN)
		keyboard.press(LightAttack)
		keyboard.release(DOWN)
		keyboard.release(LightAttack)

def SAir(output):
	if keyboard.is_pressed(RIGHT) == True:
		outputConsole(output, "[User] Side Air [Input: Key Right]\n")
		keyboard.press(LightAttack)
		keyboard.release(LightAttack)
	elif keyboard.is_pressed(LEFT) == True:
		outputConsole(output, "[User] Side Air [Input: Key Left]\n")
		keyboard.press(LightAttack)
		keyboard.release(LightAttack)
	else:
		outputConsole(output, "[Macro] Side Air Failed [Input Not Provided]\n")

# Other
def Jump(output):
	outputConsole(output, "[Macro] Jump [Auto]\n")
	keyboard.press(JUMP)
	keyboard.release(JUMP)

def Groundpound(output):
	outputConsole(output, "[Macro] Groundpound [Auto]\n")
	keyboard.press(DOWN)
	keyboard.press(HeavyAttack)
	keyboard.release(DOWN)
	keyboard.release(HeavyAttack)

def Dash(output):
	outputConsole(output, "[Macro] Dash [Auto]\n")
	keyboard.press(DOWN)
	keyboard.press(DODGE)
	keyboard.release(DOWN)
	keyboard.release(DODGE)

def DashJump(output):
	outputConsole(output, "[Macro] Dash Jump [Auto]\n")
	keyboard.press(DOWN)
	keyboard.press(DODGE)
	keyboard.press(JUMP)
	keyboard.release(DOWN)
	keyboard.release(DODGE)
	keyboard.release(JUMP)

def DashJumpFastFall(output):
	outputConsole(output, "[Macro] Dash Jump Fast Fall [Auto]\n")
	keyboard.press(DODGE)
	keyboard.press(JUMP)
	keyboard.press(DOWN)
	keyboard.release(DODGE)
	keyboard.release(JUMP)
	sleep(0.23)
	keyboard.release(DOWN)

def DownFall(output):
	outputConsole(output, "[Macro] Down / Fall [Auto]\n")
	print("Fast Fall")
	keyboard.press(DOWN)
	keyboard.release(DOWN)

def Dodge(output):
	outputConsole(output, "[Macro] Dodge [Auto]\n")
	keyboard.press(DODGE)
	keyboard.release(DODGE)

def DodgeUp(output):
	outputConsole(output, "[Macro] Dodge Up [Auto]\n")
	keyboard.press(DODGE)
	keyboard.press(UP)
	keyboard.release(DODGE)
	keyboard.release(UP)

def DodgeForward(output):
	if keyboard.is_pressed(RIGHT) == True:
		outputConsole(output, "[User] Dodge Forward [Input: Key Right]\n")
		keyboard.press(DODGE)
		sleep(0.12)
		keyboard.release(DODGE)
	elif keyboard.is_pressed(LEFT) == True:
		outputConsole(output, "[User] Dodge Forward [Input: Key Left]\n")
		keyboard.press(DODGE)
		sleep(0.12)
		keyboard.release(DODGE)
	else:
		outputConsole(output, "[Macro] Dodge Forward Failed [Input Not Provided]\n")

def DodgeDown(output):
	if keyboard.is_pressed(DOWN) == True:
		outputConsole(output, "[User] Dodge Down [Input: Key Down]\n")
		keyboard.press(DODGE)
		keyboard.release(DODGE)
	else:
		outputConsole(output, "[Macro] Dodge Down [Auto]\n")
		keyboard.press(DOWN)
		keyboard.press(DODGE)
		keyboard.release(DOWN)
		keyboard.release(DODGE)

def Throw(output):
	outputConsole(output, "[Macro] Throw [Auto]\n")
	keyboard.press(THROW)
	keyboard.release(THROW)

def Pickup(output):
	outputConsole(output, "[Macro] Pickup [Auto]\n")
	keyboard.press(PICKUP)
	keyboard.release(PICKUP)







# Specific Weapon
def GreatswordNLightSLight(output):
	outputConsole(output, "[Macro] Greatsword NLight Slight [Auto]\n")
	keyboard.press(UP)
	keyboard.press(LightAttack)
	keyboard.release(UP)
	keyboard.release(LightAttack)
	sleep(0.3)
	UpDownReease()
	keyboard.press(LightAttack)
	keyboard.release(LightAttack)
	sleep(0.4)
	keyboard.press(DOWN)
	keyboard.press(DODGE)
	keyboard.release(DOWN)
	keyboard.release(DODGE)

def GreatswordSLightNLight(output):
	outputConsole(output, "[Macro] Greatsword Slight NLight [Auto]\n")
	keyboard.press(LightAttack)
	keyboard.release(LightAttack)
	sleep(0.3)
	RightLeftRelease()
	keyboard.press(UP)
	keyboard.press(LightAttack)
	keyboard.release(UP)
	keyboard.release(LightAttack)
	sleep(0.4)
	keyboard.press(DOWN)
	keyboard.press(DODGE)
	keyboard.release(DOWN)
	keyboard.release(DODGE)

def GreatswordDLightNLight(output):
	outputConsole(output, "[Macro] Greatsword DLight NLight [Auto]\n")
	keyboard.press(DOWN)
	keyboard.press(LightAttack)
	keyboard.release(DOWN)
	keyboard.release(LightAttack)
	sleep(0.4)
	RightLeftRelease()
	keyboard.press(UP)
	keyboard.press(LightAttack)
	keyboard.release(UP)
	keyboard.release(LightAttack)
	sleep(0.4)
	keyboard.press(DOWN)
	keyboard.press(DODGE)
	keyboard.release(DOWN)
	keyboard.release(DODGE)

# Special Combo
def HammerRussianMafia(output):
	outputConsole(output, "[Macro] Russian Mafia [Auto]\n")
	keyboard.press(DOWN)
	keyboard.press(LightAttack)
	keyboard.release(DOWN)
	keyboard.release(LightAttack)
	sleep(0.4)
	keyboard.press(JUMP)
	keyboard.release(JUMP)
	keyboard.press(DODGE)
	keyboard.press(HeavyAttack)
	sleep(0.12)
	keyboard.release(DODGE)
	keyboard.release(HeavyAttack)

# Hard Combo
def UnknownBlasterHardCombo(output):
	outputConsole(output, "[Macro] Unknown Blaster Hard Combo [Auto]\n")
	keyboard.press(LightAttack)
	keyboard.release(LightAttack)
	sleep(0.5)
	keyboard.press(JUMP)
	keyboard.release(JUMP)
	keyboard.press(DODGE)
	keyboard.press(UP)
	keyboard.press(LightAttack)
	sleep(0.12)
	keyboard.release(DODGE)
	keyboard.release(UP)
	keyboard.release(LightAttack)

def UnknownGauntletBlasterHardCombo(output):
	outputConsole(output, "[Macro] Unknown Gauntlet/Blaster Hard Combo [Auto]\n")
	keyboard.press(DOWN)
	keyboard.press(DODGE)
	keyboard.release(DOWN)
	keyboard.press(JUMP)
	keyboard.press(DOWN)
	keyboard.release(DODGE)
	keyboard.press(UP)
	keyboard.release(JUMP)
	keyboard.release(DOWN)
	keyboard.press(LightAttack)
	keyboard.release(UP)
	keyboard.release(LightAttack)

def UnknownSpearChaseHardCombo(output):
	outputConsole(output, "[Macro] Unknown Spear Chase Hard Combo [Auto]\n")
	keyboard.press(UP)
	keyboard.press(LightAttack)
	keyboard.release(UP)
	keyboard.release(LightAttack)
	sleep(0.7)
	keyboard.press(JUMP)
	keyboard.release(JUMP)
	keyboard.press(DODGE)
	# keyboard.press(UP)
	keyboard.press(LightAttack)
	sleep(0.12)
	keyboard.release(DODGE)
	# keyboard.release(UP)
	keyboard.release(LightAttack)

def UnknownGauntletHardCombo(output):
	outputConsole(output, "[Macro] Unknown Gauntlet Hard Combo [Auto]\n")
	keyboard.press(DOWN)
	keyboard.press(LightAttack)
	keyboard.release(DOWN)
	keyboard.release(LightAttack)
	sleep(0.41)
	keyboard.press(JUMP)
	keyboard.release(JUMP)
	keyboard.press(DODGE)
	keyboard.press(UP)
	keyboard.press(LightAttack)
	sleep(0.12)
	keyboard.release(DODGE)
	keyboard.release(UP)
	keyboard.release(LightAttack)
# I don't know what's the combo name for it, so I name it like that

def BlasterInstantGPRMP(output):
	outputConsole(output, "[Macro] Blaster Instant GP (Edge Map (Right)) [Auto]\n")
	keyboard.press(RIGHT)
	keyboard.press_and_release(DODGE, do_press=True, do_release=True)
	keyboard.release(RIGHT)
	sleep(0.1)
	keyboard.press(LEFT)
	keyboard.press_and_release(DODGE, do_press=True, do_release=True)
	keyboard.release(LEFT)
	sleep(0.1)
	keyboard.press(DOWN)
	keyboard.press_and_release(JUMP, do_press=True, do_release=True)
	keyboard.press(HeavyAttack)
	keyboard.release(DOWN)
	keyboard.release(HeavyAttack)

def BlasterInstantGPLMP(output):
	outputConsole(output, "[Macro] Blaster Instant GP (Edge Map (Left)) [Auto]\n")
	keyboard.press(LEFT)
	keyboard.press_and_release(DODGE, do_press=True, do_release=True)
	keyboard.release(LEFT)
	sleep(0.1)
	keyboard.press(RIGHT)
	keyboard.press_and_release(DODGE, do_press=True, do_release=True)
	keyboard.release(RIGHT)
	sleep(0.1)
	keyboard.press(DOWN)
	keyboard.press_and_release(JUMP, do_press=True, do_release=True)
	keyboard.press(HeavyAttack)
	keyboard.release(DOWN)
	keyboard.release(HeavyAttack)

# Damn hard