import tkinter as tk
from tkinter import ttk, HORIZONTAL, Label, Entry, StringVar, END
import os
import sys
import time
import keyboard
import json

# Provide relative path to packed file
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
# End

# Placeholder
class EntryWithPlaceholder(Entry):
	def __init__(self, *args, **kwargs):
		self.placeholder = kwargs.pop("placeholder", "")
		super().__init__(*args, **kwargs)

		self.insert("end", self.placeholder)
		self.bind("<FocusIn>", self.remove_placeholder)
		self.bind("<FocusOut>", self.add_placeholder)

	def remove_placeholder(self, event):
		"""Remove placeholder text, if present"""
		if self.get() == self.placeholder:
			self.delete(0, "end")

	def add_placeholder(self,event):
		"""Add placeholder text if the widget is empty"""
		if self.placeholder and self.get() == "":
			self.insert(0, self.placeholder)
# End

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

def outputConsole(output, content):
	output.delete("1.0", END)
	output.insert("end", content)

def Open(ButtonState, output):
	ButtonState["state"] = "disabled"
	outputConsole(output, "All Macro Loaded. Some of Macro Combo doesn't work at all, please prefer to use the newest Macro Combo!")

	def disableResize():
		app.resizable(False, False)

	app = tk.Toplevel()
	app.iconbitmap(resource_path('icon/ergo.ico'))
	app.title("All Macro")
	app.after(100, disableResize)

	appMarg = tk.LabelFrame(app, text="Weapons", padx=5, pady=5)
	appMarg.pack(padx=5, pady=5)


	def RightLeftRelease():
		if keyboard.is_pressed(RIGHT) == True:
			outputConsole(output, "Release key RIGHT")
			keyboard.release(RIGHT)
		if keyboard.is_pressed(LEFT) == True:
			outputConsole(output, "Release key LEFT")
			keyboard.release(LEFT)

	def RightLeftReverse():
		if keyboard.is_pressed(RIGHT) == True:
			outputConsole(output, "[Reverse]: Press key LEFT")
			keyboard.press(LEFT)
			keyboard.release(LEFT)
		if keyboard.is_pressed(LEFT) == True:
			outputConsole(output, "[Reverse]: Press key RIGHT")
			keyboard.press(RIGHT)
			keyboard.release(RIGHT)

	def UpDownReease():
		if keyboard.is_pressed(UP) == True:
			outputConsole(output, "Release key UP")
			keyboard.release(UP)
		if keyboard.is_pressed(DOWN) == True:
			outputConsole(output, "Release key DOWN")
			keyboard.release(DOWN)

	####################################################################

	def onComboType0(event):
		if event.name == CType0Text.get():
			outputConsole(output, 'Orb: SLight -> Jump -> SAir')
			# Movement 1
			outputConsole(output, "Light Attack")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			# Delay 1
			outputConsole(output, "Wait for 0.5 sec")
			time.sleep(0.5)
			# Movement 2
			outputConsole(output, "Jump")
			outputConsole(output, "Light Attack")
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			outputConsole(output, " Orb combo end ")

	def onComboType1(event):
		if event.name == CType1Text.get():
			outputConsole(output, 'Unarmed: DLight -> Jump -> GP')
			# Movement 1
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# delay 1
			outputConsole(output, "Wait for 0.22 sec")
			time.sleep(0.22)
			# Movement 2
			outputConsole(output, "Jump")
			keyboard.press(JUMP)
			keyboard.release(JUMP)
			# Delay 2
			outputConsole(output, "Wait for 0.05 sec")
			time.sleep(0.05)
			# Movement 3
			outputConsole(output, "Groundpound")
			keyboard.press(DOWN)
			keyboard.press(HeavyAttack)
			keyboard.release(DOWN)
			keyboard.release(HeavyAttack)
			outputConsole(output, " Unarmed combo end ")

	def onComboType2(event):
		if event.name == CType2Text.get():
			outputConsole(output, 'Unarmed: DLight -> Jump -> NAir')
			# Movement 1
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# delay 1
			outputConsole(output, "Wait for 0.22 sec")
			time.sleep(0.22)
			# Movement 2
			outputConsole(output, "Jump")
			keyboard.press(JUMP)
			keyboard.release(JUMP)
			# Delay 2
			outputConsole(output, "Wait for 0.55 sec")
			time.sleep(0.05)
			# Movement 3
			outputConsole(output, "Neutral Air")
			keyboard.press(UP)
			keyboard.press(LightAttack)
			keyboard.release(UP)
			keyboard.release(LightAttack)
			outputConsole(output, " Unarmed combo end ")

	def onComboType3(event):
		if event.name == CType3Text.get():
			outputConsole(output, 'Sword: DLight -> Jump -> SAir')
			# Movement 1
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# delay 1
			outputConsole(output, "Wait for 0.45 sec")
			time.sleep(0.45)
			# Movement 2
			outputConsole(output, "Jump and Light Attack (Side Air when key left or right is pressed)")
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			outputConsole(output, " Sword combo end ")

	def onComboType4(event):
		if event.name == CType4Text.get():
			outputConsole(output, 'Sword: DLight -> NAir')
			# Movement 1
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# delay 1
			outputConsole(output, "Wait for 0.45 sec")
			time.sleep(0.45)
			# Movement 2
			outputConsole(output, "Jump and Neutral Attack")
			keyboard.press(UP)
			keyboard.press(LightAttack)
			keyboard.release(UP)
			keyboard.release(LightAttack)
			outputConsole(output, " Sword combo end ")

	def onComboType5(event):
		if event.name == CType5Text.get():
			outputConsole(output, 'Sword: DLight -> Jump -> DAir')
			# Movement 1
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# delay 1
			outputConsole(output, "Wait for 0.45 sec")
			time.sleep(0.45)
			# Movement 2
			outputConsole(output, "Jump and Down Air")
			keyboard.press(JUMP)
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, " Sword combo end ")

	def onComboType6(event):
		if event.name == CType6Text.get():
			outputConsole(output, 'Sword: DLight -> Jump -> Recovery')
			# Movement 1
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# delay 1
			outputConsole(output, "Wait for 0.455 sec")
			time.sleep(0.45)
			# Movement 2
			outputConsole(output, "Jump and Recovery")
			keyboard.press(JUMP)
			keyboard.press(UP)
			keyboard.press(HeavyAttack)
			keyboard.release(JUMP)
			keyboard.release(UP)
			keyboard.release(HeavyAttack)
			outputConsole(output, " Sword combo end ")

	def onComboType7(event):
		if event.name == CType7Text.get():
			outputConsole(output, 'Lance: SLight -> Jump -> SAir/NAir') # Also work with NAir if you don't press left or right
			# Movement 1
			outputConsole(output, "Light Attack (Side Light when key left or right is pressed)")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			# delay 1
			outputConsole(output, "Wait for 0.4 sec")
			time.sleep(0.4)
			# Movement 2
			outputConsole(output, "Jump and Side Air when key left or right is pressed and NAir when key left or right is not pressed")
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			outputConsole(output, " Rocket Lance combo end ")

	def onComboType8(event):
		if event.name == CType8Text.get():
			outputConsole(output, 'Lance: SLight -> Jump -> Recovery')
			# Movement 1
			outputConsole(output, "Light Attack (Side Light when left or right key is pressed)")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			# delay 1
			outputConsole(output, "Wait for 0.4 sec")
			time.sleep(0.4)
			# Movement 2
			outputConsole(output, "Jump and Recovery (To get chance hitting the opponent, opponent must damaged 80+)")
			keyboard.press(JUMP)
			keyboard.press(HeavyAttack)
			keyboard.release(JUMP)
			keyboard.release(HeavyAttack)
			outputConsole(output, " Rocke Lance combo end ")

	def onComboType9(event):
		if event.name == CType9Text.get():
			outputConsole(output, 'Lance: SLight -> Jump -> DAir')
			# Movement 1
			outputConsole(output, "Light Attack (Side Light when left or right key is pressed)")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			# delay 1
			outputConsole(output, "Wait for 0.41 (Chance hitting the opponent based on legend dexterity)")
			time.sleep(0.41)
			# Movement 2
			outputConsole(output, "Jump and Down Air")
			keyboard.press(JUMP)
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, " Lance combo end ")

	def onComboType10(event):
		if event.name == CType10Text.get():
			outputConsole(output, 'Hammer: DLight -> Jump -> DAir')
			# Movement 1
			outputConsole(output, "Down Air")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay
			outputConsole(output, "Wait for 0.3 (It's really hard to hit the opponent by this combo)")
			time.sleep(0.3)
			# Movement 2
			outputConsole(output, "Jump and Down Air")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			outputConsole(output, " Hammer combo end ")

	def onComboType11(event):
		if event.name == CType11Text.get():
			outputConsole(output, 'Hammer: DLight -> Jump -> SAir')
			# Movement 1
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay
			outputConsole(output, "Wait for 0.35 sec")
			time.sleep(0.35)
			# Movement 2
			outputConsole(output, "Jump and Side Air (NAir when key left or right not pressed)")
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			outputConsole(output, " Hammer combo end ")

	def onComboType12(event):
		if event.name == CType12Text.get(): # Press left or right required
			outputConsole(output, 'Hammer: DLight -> Jump -> FDodge -> Recovery')
			# Movement 1
			outputConsole(output, " Russian bylat Mafia ")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay 1
			outputConsole(output, "Wait for 0.4 sec")
			time.sleep(0.4)
			# Movement 2
			outputConsole(output, "Dash Jump and forward dodge a bit following with Hammer Recovery")
			keyboard.press(JUMP)
			keyboard.release(JUMP)
			keyboard.press(DODGE)
			keyboard.press(HeavyAttack)
			# Delay 3
			outputConsole(output, "Wait for 0.12 sec")
			time.sleep(0.12)
			# Movement 4
			outputConsole(output, "Release dodge and recovery button")
			keyboard.release(DODGE)
			keyboard.release(HeavyAttack)
			outputConsole(output, " Hammer Russian Mafia end ")

	def onComboType13(event):
		if event.name == CType13Text.get(): # Press left or right required
			outputConsole(output, 'Blaster: DLight -> Jump -> DAir')
			# Movement 1
			outputConsole(output, "Down Light (Must press key left or right for better chance)")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay
			outputConsole(output, "Wait for 0.7 sec")
			time.sleep(0.7)
			# Movement 2
			outputConsole(output, "Dash Jmp and Down Air")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			outputConsole(output, " Blaster combo end ")

	def onComboType14(event):
		if event.name == CType14Text.get():
			outputConsole(output, 'Blaster: DLight -> Jump -> Recovery')
			# Movement 1
			outputConsole(output, "Down Light (Must press key left or right for better chance)")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay
			outputConsole(output, "Wait for 0.7 sec")
			time.sleep(0.7)
			# Movement 2
			outputConsole(output, "Jump and Recovery following with Blaster Recovery")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.press(JUMP)
			keyboard.release(DOWN)
			keyboard.press(HeavyAttack)
			outputConsole(output, "Release all key for this combo")
			keyboard.release(DODGE)
			keyboard.release(JUMP)
			keyboard.release(HeavyAttack)
			outputConsole(output, " Blaster combo end ")

	def onComboType15(event):
		if event.name == CType15Text.get():
			# THIS IS THE HARDEST GAUNTLET COMBO, I SPENT 6HOURS JUST TO ADJUST THI DAMN COMBO
			# YOU MAY GET 70%/50% CHANCE DOING RANDOM COMBO WITH THIS
			outputConsole(output, 'Gauntlet: DLight -> Jump -> CDodge -> NAir')
			outputConsole(output, "Down Light (Also work with GC+DLight in air)")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay 1
			outputConsole(output, "Wait for 0.4")
			time.sleep(0.4)
			# Movement 2
			outputConsole(output, "Jump and forward dodge a bit following with Neutral Air")
			keyboard.press(JUMP)
			keyboard.release(JUMP)
			keyboard.press(DODGE)
			keyboard.press(UP)
			keyboard.press(LightAttack)
			# Delay 3
			outputConsole(output, "Wait for 0.12 sec")
			time.sleep(0.12)
			# Movement 4
			keyboard.release(DODGE)
			keyboard.release(UP)
			keyboard.release(LightAttack)
			outputConsole(output, " Gauntlet combo end ")

	def onComboType16(event):
		if event.name == CType16Text.get():
			outputConsole(output, 'Greatsword')
			# Movement 1
			outputConsole(output, "Release user key up for Neutral Light")
			keyboard.press(UP)
			keyboard.press(LightAttack)
			outputConsole(output, "NLight")
			keyboard.release(UP)
			keyboard.release(LightAttack)
			# Delay 1
			outputConsole(output, "Wait for 0.3")
			time.sleep(0.3)
			# Movement 2
			UpDownReease()
			keyboard.press(LightAttack)
			outputConsole(output, "SLight")
			keyboard.release(LightAttack)
			# Delay 2
			outputConsole(output, "Wait for 0.4")
			time.sleep(0.4)
			# Movement 3
			outputConsole(output, "CD")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			outputConsole(output, " Greatsword combo (basic 1) end ")


	def onComboType17(event):
		if event.name == CType17Text.get():
			outputConsole(output, 'Greatsword')
			# Movement 1
			outputConsole(output, "Side Light (Neutral Attack when user not pressing key left or right)")
			keyboard.press(LightAttack)
			outputConsole(output, "SLight")
			keyboard.release(LightAttack)
			# Delay 1
			outputConsole(output, "Wait for 0.3 sec")
			time.sleep(0.3)
			# Movement 2
			outputConsole(output, "Release key left or right for user")
			RightLeftRelease()
			outputConsole(output, "Neutral Light")
			keyboard.press(UP)
			keyboard.press(LightAttack)
			outputConsole(output, "NLight")
			keyboard.release(UP)
			keyboard.release(LightAttack)
			# Delay 2
			outputConsole(output, "Wait for 0.4 sec")
			time.sleep(0.4)
			# Movement 3
			outputConsole(output, "CD")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			outputConsole(output, " Greatsword combo (basic 2) end ")

	def onComboType18(event):
		if event.name == CType18Text.get():
			outputConsole(output, 'Greatsword')
			# Movement 1
			outputConsole(output, "Down Light (Best starter for Greatsword combo)")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			outputConsole(output, "DLight")
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay 1
			outputConsole(output, "Wait for 0.4 sec")
			time.sleep(0.4)
			# Movement 2
			outputConsole(output, "Release key left or right for user")
			RightLeftRelease()
			outputConsole(output, "Neutral Light")
			keyboard.press(UP)
			keyboard.press(LightAttack)
			outputConsole(output, "NLight")
			keyboard.release(UP)
			keyboard.release(LightAttack)
			# Delay 2
			outputConsole(output, "Wait for 0.4 sec")
			time.sleep(0.4)
			# Movement 3
			outputConsole(output, "CD")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			outputConsole(output, " Greatsword combo (basic 3) end ")

	# Side left
	keyboard.on_press(onComboType0)
	keyboard.on_press(onComboType1)
	keyboard.on_press(onComboType2)
	keyboard.on_press(onComboType3)
	keyboard.on_press(onComboType4)
	keyboard.on_press(onComboType5)
	keyboard.on_press(onComboType6)
	keyboard.on_press(onComboType7)
	keyboard.on_press(onComboType8)
	keyboard.on_press(onComboType9)
	keyboard.on_press(onComboType10)
	keyboard.on_press(onComboType11)
	keyboard.on_press(onComboType12)
	keyboard.on_press(onComboType13)
	keyboard.on_press(onComboType14)
	keyboard.on_press(onComboType15)
	keyboard.on_press(onComboType16)
	keyboard.on_press(onComboType17)
	keyboard.on_press(onComboType18)

	def onComboType0A(event):
		if event.name == CType0TextA.get():
			outputConsole(output, "Gauntlet")
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.35 sec")
			time.sleep(0.35)
			outputConsole(output, "Dash Jump")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.press(JUMP)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			keyboard.release(JUMP)
			outputConsole(output, "Down Air")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, " Gauntlet combo end ")

	def onComboType1A(event):
		if event.name == CType1TextA.get():
			outputConsole(output, "Katar")
			keyboard.press(DODGE)
			keyboard.press(LightAttack)
			keyboard.release(DODGE)
			keyboard.release(LightAttack)
			time.sleep(0.5)
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			keyboard.release(LightAttack)
			outputConsole(output, " Katar combo end ")

	def onComboType2A(event):
		if event.name == CType2TextA.get():
			outputConsole(output, "Katar")
			outputConsole(output, "Dash Jump")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.press(JUMP)
			keyboard.release(DODGE)
			keyboard.release(JUMP)
			outputConsole(output, "Down Air")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.53 sec")
			time.sleep(0.53)
			outputConsole(output, "Down Light")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.4")
			time.sleep(0.4)
			outputConsole(output, "Jump-Down-Air")
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			keyboard.release(DOWN)
			outputConsole(output, " Katar combo end ")

	def onComboType3A(event):
		if event.name ==  CType3TextA.get():
			outputConsole(output, "Bow: Side Light -> Down Light -> Neutral Light")
			outputConsole(output, "Neutral Light if key left/right not pressed else Side Light")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.62")
			time.sleep(0.62)
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.5")
			time.sleep(0.5)
			outputConsole(output, "Neutral Light")
			keyboard.press(UP)
			keyboard.press(LightAttack)
			keyboard.release(UP)
			keyboard.release(LightAttack)
			outputConsole(output, " Bow combo end ")

	def onComboType4A(event):
		if event.name == CType4TextA.get():
			outputConsole(output, "Bow")
			outputConsole(output, "Neutral Light if key left/right not pressed else Side Light")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.62")
			time.sleep(0.62)
			outputConsole(output, "Dash Jump")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.press(JUMP)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			keyboard.release(JUMP)
			outputConsole(output, "Wait for 0.12 sec")
			time.sleep(0.12)
			outputConsole(output, "Down Air")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, " Bow combo end ")

	def onComboType5A(event):
		if event.name == CType5TextA.get():
			outputConsole(output, 'Spear: NLight -> Jump -> CDodge -> SAir')
			keyboard.press(UP)
			keyboard.press(LightAttack)
			keyboard.release(UP)
			keyboard.release(LightAttack)
			# Delay 1
			outputConsole(output, "Wait for 0.4")
			time.sleep(0.7)
			# Movement 2
			outputConsole(output, "Jump and forward dodge a bit following with Chase dodge")
			keyboard.press(JUMP)
			keyboard.release(JUMP)
			keyboard.press(DODGE)
			# keyboard.press(UP)
			keyboard.press(LightAttack)
			# Delay 3
			outputConsole(output, "Wait for 0.12 sec")
			time.sleep(0.12)
			# Movement 4
			keyboard.release(DODGE)
			# keyboard.release(UP)
			keyboard.release(LightAttack)
			outputConsole(output, " Spear combo end ")


	def onComboType6A(event):
		if event.name == CType6TextA.get():
			outputConsole(output, "Spear: Side Light -> Jump -> Side Air")
			outputConsole(output, "Neutral Light if key left/right not pressed")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.64 sec")
			time.sleep(0.64)
			outputConsole(output, "Jump and Side Air (Neutral air if left/right key not pressed)")
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			outputConsole(output, " Spear combo end ")

	def onComboType7A(event):
		if event.name == CType7TextA.get():
			outputConsole(output, "Spear: Dash Jump -> Down Light")
			outputConsole(output, "Used to attack wall hugger, work on ground too)")
			outputConsole(output, "Only dodge if left/right key not pressed")
			outputConsole(output, "Dash Jump")
			keyboard.press(DODGE)
			keyboard.press(JUMP)
			keyboard.press(DOWN)
			keyboard.release(DODGE)
			outputConsole(output, "Down Air")
			keyboard.release(JUMP)
			keyboard.press(LightAttack)
			time.sleep(0.23)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, " Spear combo end ")

	def onComboType8A(event):
		if event.name == CType8TextA.get():
			outputConsole(output, "Hammer: Side Light -> Down Light -> Dash Jump -> Down Air")
			outputConsole(output, "Side Light (Neutral Light if left/right key not pressed)")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.5 sec")
			time.sleep(0.5)
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.press(LightAttack)
			keyboard.release(DODGE)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.5")
			time.sleep(0.5)
			outputConsole(output, "Dash Jump -> Down Air")
			keyboard.press(DODGE)
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(DODGE)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			keyboard.release(DOWN)
			outputConsole(output, " Hammer combo end ")

	def onComboType9A(event):
		if event.name == CType9TextA.get():
			outputConsole(output, "Hammer: Down Light -> Throw -> Unarmed(Down Light) -> Jump Pickup -> Down Air")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			time.sleep(0.33)
			keyboard.press(THROW)
			keyboard.release(THROW)
			time.sleep(0.5)
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			time.sleep(0.2)
			keyboard.press(JUMP)
			keyboard.press(PICKUP)
			keyboard.release(JUMP)
			keyboard.release(PICKUP)
			time.sleep(0.1)
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			keyboard.release(DOWN)
			outputConsole(output, " Hammer combo end ")

	def onComboType10A(event):
		if event.name == CType10TextA.get():
			outputConsole(output, "Blaster (Hard Combo): Worked with Cannon too")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			# Delay 1
			outputConsole(output, "Wait for 0.4")
			time.sleep(0.5)
			# Movement 2
			outputConsole(output, "Jump and forward dodge a bit following with Chase dodge")
			keyboard.press(JUMP)
			keyboard.release(JUMP)
			keyboard.press(DODGE)
			keyboard.press(UP)
			keyboard.press(LightAttack)
			# Delay 3
			outputConsole(output, "Wait for 0.12 sec")
			time.sleep(0.12)
			# Movement 4
			keyboard.release(DODGE)
			keyboard.release(UP)
			keyboard.release(LightAttack)
			outputConsole(output, " Blaster combo end ")

	def onComboType11A(event):
		if event.name == CType11TextA.get():
			outputConsole(output, "Scythe (Basic): Down Light (to Back) -> Jump -> Side Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			time.sleep(0.83)
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			outputConsole(output, " Scythe combo end ")

	def onComboType12A(event):
		if event.name == CType12TextA.get():
			outputConsole(output, "Hard Gauntlet Combo. Success rate: 40%. Can be used with Blaster too.")
			outputConsole(output, "Gauntlet: Dash Jump -> Fast Fall -> Neutral Air")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.release(DOWN)
			keyboard.press(JUMP)
			keyboard.press(DOWN)
			keyboard.release(DODGE)
			outputConsole(output, "Neutral Air")
			keyboard.press(UP)
			keyboard.release(JUMP)
			keyboard.release(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(UP)
			keyboard.release(LightAttack)
			outputConsole(output, " Gauntlet combo end ")

	def onComboType13A(event):
		if event.name == CType13TextA.get():
			outputConsole(output, "Axe: Side Light -> Jump -> Side Air")
			outputConsole(output, "Side Light (Neutral Light if left/right key not pressed)")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			time.sleep(0.47)
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			outputConsole(output, " Axe combo end ")

	def onComboType14A(event):
		if event.name == CType14TextA.get():
			outputConsole(output, "Axe: Side Light -> Jump -> Neutral Air")
			outputConsole(output, "Side Light (Neutral Light if left/right key not pressed)")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			time.sleep(0.47)
			keyboard.press(JUMP)
			keyboard.press(UP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(UP)
			keyboard.release(LightAttack)
			outputConsole(output, " Axe combo end ")

	def onComboType15A(event):
		if event.name == CType15TextA.get():
			outputConsole(output, "Axe: Dash Throw Pickup -> Neutral Light")
			outputConsole(output, "Dash Throw")
			keyboard.press(DODGE)
			keyboard.press(THROW)
			keyboard.release(DODGE)
			keyboard.release(THROW)
			outputConsole(output, "Wait for 0.53 sec")
			time.sleep(0.53)
			outputConsole(output, "Pickup -> Neutral Air")
			keyboard.press(PICKUP)
			keyboard.press(UP)
			keyboard.press(LightAttack)
			keyboard.release(PICKUP)
			keyboard.release(UP)
			keyboard.release(LightAttack)
			outputConsole(output, " Axe combo end ")

	def onComboType16A(event):
		if event.name == CType16TextA.get():
			outputConsole(output, "Gauntlet: Throw -> Dash Down Light (Unarmed) -> Jump Pickup -> Down Air")
			outputConsole(output, "This combo also work with Blaster")
			outputConsole(output, "Throw")
			keyboard.press(THROW)
			keyboard.release(THROW)
			outputConsole(output, "Wait for 0.53 sec")
			time.sleep(0.53)
			outputConsole(output, "Dash Down Light")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.33 sec")
			time.sleep(0.33)
			outputConsole(output, "Jump -> Pickup -> Down Air")
			keyboard.press(JUMP)
			keyboard.press(PICKUP)
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(PICKUP)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, " Gauntlet combo end ")

	def onComboType17A(event):
		if event.name == CType17TextA.get():
			outputConsole(output, "Bow: Side Light -> Dash Throw -> Down Light (Unarmed) -> Pickup -> Neutral Air")
			outputConsole(output, "Side Light")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.63")
			time.sleep(0.63)
			outputConsole(output, "Dash Throw")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			keyboard.press(THROW)
			keyboard.release(THROW)
			outputConsole(output, "Wait for 0.53 sec")
			time.sleep(0.53)
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.33 sec")
			time.sleep(0.33)
			outputConsole(output, "Jump -> Pickup -> Neutral Air")
			keyboard.press(JUMP)
			keyboard.press(PICKUP)
			keyboard.press(UP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(PICKUP)
			keyboard.release(UP)
			keyboard.release(LightAttack)
			outputConsole(output, " Bow combo end ")

	def onComboType18A(event):
		if event.name == CType18TextA.get():
			outputConsole(output, "Bow: Down Light -> Neutral Light")
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.43 sec")
			time.sleep(0.43)
			outputConsole(output, "Neutra Light")
			keyboard.press(UP)
			keyboard.press(LightAttack)
			keyboard.release(UP)
			keyboard.release(LightAttack)
			outputConsole(output, " Bow combo end ")

	# Side right
	keyboard.on_press(onComboType0A)
	keyboard.on_press(onComboType1A)
	keyboard.on_press(onComboType2A)
	keyboard.on_press(onComboType3A)
	keyboard.on_press(onComboType4A)
	keyboard.on_press(onComboType5A)
	keyboard.on_press(onComboType6A)
	keyboard.on_press(onComboType7A)
	keyboard.on_press(onComboType8A)
	keyboard.on_press(onComboType9A)
	keyboard.on_press(onComboType10A)
	keyboard.on_press(onComboType11A)
	keyboard.on_press(onComboType12A)
	keyboard.on_press(onComboType13A)
	keyboard.on_press(onComboType14A)
	keyboard.on_press(onComboType15A)
	keyboard.on_press(onComboType16A)
	keyboard.on_press(onComboType17A)
	keyboard.on_press(onComboType18A)

	# Side right 2
	def onComboType0A2(event):
		if event.name == CType0TextA2.get():
			outputConsole(output, "Dash Jump Fast Fall")
			keyboard.press(DODGE)
			keyboard.press(JUMP)
			keyboard.press(DOWN)
			keyboard.release(DODGE)
			keyboard.release(JUMP)
			time.sleep(0.23)
			keyboard.release(DOWN)
			outputConsole(output, " DJFF end ")

	def onComboType1A2(event):
		if event.name == CType1TextA2.get():
			outputConsole(output, "Not recommended Scythe combo")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			time.sleep(0.13)
			################################################
			if keyboard.is_pressed(LEFT):
				keyboard.release(LEFT)
				outputConsole(output, "Release key left because user keep pressing key left")
				time.sleep(0.4)
				keyboard.press(LEFT)
				keyboard.press(JUMP)
				keyboard.press(DODGE)
				keyboard.press(RIGHT) # Right Reverse
				keyboard.press(UP)
				keyboard.press(LightAttack)
				keyboard.release(RIGHT) # Right Reverse
				keyboard.release(UP)
				keyboard.release(LightAttack)
				time.sleep(0.47)
				keyboard.release(LEFT)
				keyboard.release(JUMP)
				keyboard.release(DODGE)
			if keyboard.is_pressed(RIGHT):
				keyboard.release(RIGHT)
				outputConsole(output, "Release key right because user keep pressing key right")
				time.sleep(0.4)
				keyboard.press(RIGHT)
				keyboard.press(JUMP)
				keyboard.press(DODGE)
				keyboard.press(LEFT) # Left Reverse
				keyboard.press(UP)
				keyboard.press(LightAttack)
				keyboard.release(LEFT) # Left Reverse
				keyboard.release(UP)
				keyboard.release(LightAttack)
				time.sleep(0.47)
				keyboard.release(RIGHT)
				keyboard.release(JUMP)
				keyboard.release(DODGE)
			################################################
			outputConsole(output, "User have to release and press key left/right again to continue move left/right")
			outputConsole(output, " Scythe end ")

	def onComboType2A2(event):
		if event.name == CType2TextA2.get():
			outputConsole(output, "Scythe: Dash -> Neutral Air -> Jump Recovery")
			outputConsole(output, "Dash -> Neutral Air")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			keyboard.press(UP)
			keyboard.press(LightAttack)
			keyboard.release(UP)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.43 sec")
			time.sleep(0.43)
			outputConsole(output, "Jump -> Recovery")
			keyboard.press(JUMP)
			keyboard.press(HeavyAttack)
			keyboard.release(JUMP)
			keyboard.release(HeavyAttack)
			outputConsole(output, " Scythe end ")

	def onComboType3A2(event):
		if event.name == CType3TextA2.get():
			outputConsole(output, 'Orb: Side Light -> Down Light -> Jump -> Side Air')
			outputConsole(output, "Light Attack")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.5 sec")
			time.sleep(0.5)
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.43 sec")
			time.sleep(0.43)
			outputConsole(output, "Jump -> Light Attack")
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			outputConsole(output, " Orb combo end ")

	def onComboType4A2(event):
		if event.name == CType4TextA2.get():
			outputConsole(output, "Spear: Side Light -> Dash Jump -> Neutral Air")
			outputConsole(output, "Neutral Light if left/right key not pressed")
			outputConsole(output, "Side Light")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.63 sec")
			time.sleep(0.63)
			outputConsole(output, "Dash Jump Neutral Air")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			keyboard.press(JUMP)
			keyboard.press(UP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(UP)
			keyboard.release(LightAttack)
			outputConsole(output, " Spear combo end ")

	def onComboType5A2(event):
		if event.name == CType5TextA2.get():
			outputConsole(output, "Cannon: Down Light -> Jump -> Down Air")
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.5 sec")
			time.sleep(0.5)
			outputConsole(output, "Jump")
			keyboard.press(JUMP)
			keyboard.release(JUMP)
			outputConsole(output, "Down Air")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, " Cannon combo end ")		

	def onComboType6A2(event):
		if event.name == CType6TextA2.get():
			outputConsole(output, "Cannon: Down Light -> Jump -> Side Air")
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.5 sec")
			time.sleep(0.5)
			outputConsole(output, "Jump")
			keyboard.press(JUMP)
			keyboard.release(JUMP)
			outputConsole(output, "Side Air")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			outputConsole(output, " Cannon combo end ")		

	def onComboType7A2(event):
		if event.name == CType7TextA2.get():
			outputConsole(output, "Cannon: Side Light -> Jump -> Down Air")
			outputConsole(output, "Neutral Light if left/right key not pressed")
			outputConsole(output, "Side Light")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.5 sec")
			time.sleep(0.5)
			outputConsole(output, "Jump")
			keyboard.press(JUMP)
			keyboard.press(DOWN)
			outputConsole(output, "Down Air")
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, " Cannon combo end ")	

	def onComboType8A2(event):
		if event.name == CType8TextA2.get():
			outputConsole(output, "Katar: Throw -> Dash Down Light(Unarmed) -> Jump Pickup -> Down Air -> Down Light")
			outputConsole(output, "Throw")
			keyboard.press(THROW)
			keyboard.release(THROW)
			outputConsole(output, "Wait for 0.43 sec")
			time.sleep(0.43)
			outputConsole(output, "Dash Down Light")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.35 sec")
			time.sleep(0.35)
			outputConsole(output, "Jump Pickup")
			keyboard.press(JUMP)
			keyboard.press(PICKUP)
			outputConsole(output, "Down Air")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(PICKUP)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.5")
			time.sleep(0.5)
			outputConsole(output, "Down Light")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			keyboard.release(DOWN)
			outputConsole(output, " Katar combo end ")	

	def onComboType9A2(event):
		if event.name == CType9TextA2.get():
			outputConsole(output, "Katar: Throw -> Dash Down Light(Unarmed) -> Pickup -> Down Light")
			outputConsole(output, "Throw")
			keyboard.press(THROW)
			keyboard.release(THROW)
			outputConsole(output, "Wait for 0.43 sec")
			time.sleep(0.43)
			outputConsole(output, "Dash Down Light")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.33 sec")
			time.sleep(0.33)
			outputConsole(output, "Pickup")
			keyboard.press(PICKUP)
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(PICKUP)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, " Katar combo end ")	

	def onComboType10A2(event):
		if event.name == CType10TextA2.get():
			outputConsole(output, "Asuri Katar Combos")
			outputConsole(output, "Katar: Throw -> Dash Down Light(Unarmed) -> Pickup -> Neutral Heavy -> Down Light")
			outputConsole(output, "Throw")
			keyboard.press(THROW)
			keyboard.release(THROW)
			outputConsole(output, "Wait for 0.43 sec")
			time.sleep(0.43)
			outputConsole(output, "Dash Down Light")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.35 sec")
			time.sleep(0.35)
			outputConsole(output, "Jump Pickup")
			keyboard.press(PICKUP)
			outputConsole(output, "Down Air")
			keyboard.press(HeavyAttack)
			keyboard.release(PICKUP)
			keyboard.release(HeavyAttack)
			outputConsole(output, "Wait for 1.03 sec")
			time.sleep(1.05)
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, " Asuri katar combo end ")	

	def onComboType11A2(event):
		if event.name == CType11TextA2.get():
			outputConsole(output, "Nix Blaster Combos (Can be used with Cassidy's blaster)")
			outputConsole(output, "Opponent must be damaged at damage 20+")
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.7")
			time.sleep(0.7)
			outputConsole(output, "Dash Neutral Heavy")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.release(DOWN)
			keyboard.press(UP)
			keyboard.press(HeavyAttack)
			keyboard.release(DODGE)
			keyboard.release(UP)
			keyboard.release(HeavyAttack)
			outputConsole(output, " Nix Blaster combo end ")

	def onComboType12A2(event):
		if event.name == CType12TextA2.get():
			outputConsole(output, "Jiro Scythe Combos (Useless)")
			outputConsole(output, "Neutral Light")
			keyboard.press(UP)
			keyboard.press(LightAttack)
			keyboard.release(UP)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.4")
			time.sleep(0.4)
			outputConsole(output, "Dash Neutral Heavy")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.release(DOWN)
			keyboard.press(UP)
			keyboard.press(HeavyAttack)
			keyboard.release(DODGE)
			keyboard.release(UP)
			keyboard.release(HeavyAttack)
			outputConsole(output, " Jiro Scythe combo end ")

	def onComboType13A2(event):
		if event.name == CType13TextA2.get():
			outputConsole(output, "Koji Bow Combos (Can be used with Diana's Bow)")
			outputConsole(output, "Side Light")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.63 sec")
			time.sleep(0.63)
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.4")
			time.sleep(0.4)
			outputConsole(output, "Dash Neutral Heavy")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.release(DOWN)
			keyboard.press(UP)
			keyboard.press(HeavyAttack)
			keyboard.release(DODGE)
			keyboard.release(UP)
			keyboard.release(HeavyAttack)
			outputConsole(output, " Koji Bow combo end ")

	def onComboType14A2(event):
		if event.name == CType14TextA2.get():
			outputConsole(output, "Yumiko Bow Combos (Useless)")
			outputConsole(output, "33 damage if the opponent hit all Yumiko's orb")
			outputConsole(output, "Dash")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.release(DODGE)
			outputConsole(output, "Wait for 0.1 sec")
			time.sleep(0.1)
			outputConsole(output, "Down Heavy")
			keyboard.press(HeavyAttack)
			keyboard.release(DOWN)
			keyboard.release(HeavyAttack)
			outputConsole(output, "Wait for 0.9")
			time.sleep(0.9)
			outputConsole(output, "Neutral Light")
			keyboard.press(UP)
			keyboard.press(LightAttack)
			keyboard.release(UP)
			keyboard.release(LightAttack)
			outputConsole(output, " Yumiko Bow combo end ")

	def onComboType15A2(event):
		if event.name == CType15TextA2.get():
			outputConsole(output, "Teros Axe Combos (Can be used with Rayman's axe)")
			outputConsole(output, "Throw")
			keyboard.press(THROW)
			keyboard.release(THROW)
			outputConsole(output, "Wait for 0.43 sec")
			time.sleep(0.43)
			outputConsole(output, "Dash Down Light")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.35 sec")
			time.sleep(0.35)
			outputConsole(output, "Pickup")
			keyboard.press(PICKUP)
			outputConsole(output, "Neutral Heavy")
			keyboard.press(UP)
			keyboard.press(HeavyAttack)
			keyboard.release(UP)
			keyboard.release(PICKUP)
			keyboard.release(HeavyAttack)
			outputConsole(output, " Teros Axe combo end ")

	def onComboType16A2(event):
		if event.name == CType16TextA2.get():
			outputConsole(output, "Bow: Side Light -> Down Light -> Jump -> Neutral Air")
			outputConsole(output, "Neutral Light if key left/right not pressed else Side Light")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.62")
			time.sleep(0.62)
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.5")
			time.sleep(0.5)
			outputConsole(output, "Neutral Light")
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			outputConsole(output, " Bow combo end ")


	def onComboType17A2(event):
		if event.name == CType17TextA2.get():
			outputConsole(output, "Blaster (Easy Combos): Down Light -> Jump -> Side Air")
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.7")
			time.sleep(0.7)
			outputConsole(output, "Jump")
			keyboard.press(JUMP)
			outputConsole(output, "Side Air (Neutral Air if left/right key not pressed)")
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			outputConsole(output, " Blaster combo end ")

	def onComboType18A2(event):
		if event.name == CType18TextA2.get():
			outputConsole(output, "Blaster (Hard Combos): Down Light -> Dash -> Throw")
			outputConsole(output, "Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			outputConsole(output, "Wait for 0.7")
			time.sleep(0.7)
			outputConsole(output, "Dash Throw")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.press(THROW)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			keyboard.release(THROW)
			outputConsole(output, " Blaster combo end ")

	# Side right 2
	keyboard.on_press(onComboType0A2)
	keyboard.on_press(onComboType1A2)
	keyboard.on_press(onComboType2A2)
	keyboard.on_press(onComboType3A2)
	keyboard.on_press(onComboType4A2)
	keyboard.on_press(onComboType5A2)
	keyboard.on_press(onComboType6A2)
	keyboard.on_press(onComboType7A2)
	keyboard.on_press(onComboType8A2)
	keyboard.on_press(onComboType9A2)
	keyboard.on_press(onComboType10A2)
	keyboard.on_press(onComboType11A2)
	keyboard.on_press(onComboType12A2)
	keyboard.on_press(onComboType13A2)
	keyboard.on_press(onComboType14A2)
	keyboard.on_press(onComboType15A2)
	keyboard.on_press(onComboType16A2)
	keyboard.on_press(onComboType17A2)
	keyboard.on_press(onComboType18A2)

	################################## Command Disable ##################################
	def CType0DisableCmd():
		CType0Text.set('None')

	def CType1DisableCmd():
		CType1Text.set('None')

	def CType2DisableCmd():
		CType2Text.set('None')

	def CType3DisableCmd():
		CType3Text.set('None')

	def CType4DisableCmd():
		CType4Text.set('None')

	def CType5DisableCmd():
		CType5Text.set('None')

	def CType6DisableCmd():
		CType6Text.set('None')

	def CType7DisableCmd():
		CType7Text.set('None')

	def CType8DisableCmd():
		CType8Text.set('None')

	def CType9DisableCmd():
		CType9Text.set('None')

	def CType10DisableCmd():
		CType10Text.set('None')

	def CType11DisableCmd():
		CType11Text.set('None')

	def CType12DisableCmd():
		CType12Text.set('None')

	def CType13DisableCmd():
		CType13Text.set('None')

	def CType14DisableCmd():
		CType14Text.set('None')

	def CType15DisableCmd():
		CType15Text.set('None')

	def CType16DisableCmd():
		CType16Text.set('None')

	def CType17DisableCmd():
		CType17Text.set('None')

	def CType18DisableCmd():
		CType18Text.set('None')

	################################## Command Disable A ##################################
	def CType0DisableCmdA():
		CType0TextA.set('None')

	def CType1DisableCmdA():
		CType1TextA.set('None')

	def CType2DisableCmdA():
		CType2TextA.set('None')

	def CType3DisableCmdA():
		CType3TextA.set('None')

	def CType4DisableCmdA():
		CType4TextA.set('None')

	def CType5DisableCmdA():
		CType5TextA.set('None')

	def CType6DisableCmdA():
		CType6TextA.set('None')

	def CType7DisableCmdA():
		CType7TextA.set('None')

	def CType8DisableCmdA():
		CType8TextA.set('None')

	def CType9DisableCmdA():
		CType9TextA.set('None')

	def CType10DisableCmdA():
		CType10TextA.set('None')

	def CType11DisableCmdA():
		CType11TextA.set('None')

	def CType12DisableCmdA():
		CType12TextA.set('None')

	def CType13DisableCmdA():
		CType13TextA.set('None')

	def CType14DisableCmdA():
		CType14TextA.set('None')

	def CType15DisableCmdA():
		CType15TextA.set('None')

	def CType16DisableCmdA():
		CType16TextA.set('None')

	def CType17DisableCmdA():
		CType17TextA.set('None')

	def CType18DisableCmdA():
		CType18TextA.set('None')


	################################## Command Disable A 2 ##################################
	def CType0DisableCmdA2():
		CType0TextA2.set('None')

	def CType1DisableCmdA2():
		CType1TextA2.set('None')

	def CType2DisableCmdA2():
		CType2TextA2.set('None')

	def CType3DisableCmdA2():
		CType3TextA2.set('None')

	def CType4DisableCmdA2():
		CType4TextA2.set('None')

	def CType5DisableCmdA2():
		CType5TextA2.set('None')

	def CType6DisableCmdA2():
		CType6TextA2.set('None')

	def CType7DisableCmdA2():
		CType7TextA2.set('None')

	def CType8DisableCmdA2():
		CType8TextA2.set('None')

	def CType9DisableCmdA2():
		CType9TextA2.set('None')

	def CType10DisableCmdA2():
		CType10TextA2.set('None')

	def CType11DisableCmdA2():
		CType11TextA2.set('None')

	def CType12DisableCmdA2():
		CType12TextA2.set('None')

	def CType13DisableCmdA2():
		CType13TextA2.set('None')

	def CType14DisableCmdA2():
		CType14TextA2.set('None')

	def CType15DisableCmdA2():
		CType15TextA2.set('None')

	def CType16DisableCmdA2():
		CType16TextA2.set('None')

	def CType17DisableCmdA2():
		CType17TextA2.set('None')

	def CType18DisableCmdA2():
		CType18TextA2.set('None')

	################################## Label ##################################
	CType0 = Label(appMarg, text="Orb")
	CType0.grid(row=1,column=1)

	CType1 = Label(appMarg, text="Unarmed")
	CType1.grid(row=2,column=1)

	CType2 = Label(appMarg, text="Unarmed")
	CType2.grid(row=3,column=1)

	CType3 = Label(appMarg, text="Sword")
	CType3.grid(row=4,column=1)

	CType4 = Label(appMarg, text="Sword")
	CType4.grid(row=5,column=1)

	CType5 = Label(appMarg, text="Sword")
	CType5.grid(row=6,column=1)

	CType6 = Label(appMarg, text="Sword")
	CType6.grid(row=7,column=1)

	CType7 = Label(appMarg, text="Lance")
	CType7.grid(row=8,column=1)

	CType8 = Label(appMarg, text="Lance")
	CType8.grid(row=9,column=1)

	CType9 = Label(appMarg, text="Lance")
	CType9.grid(row=10,column=1)

	CType10 = Label(appMarg, text="Hammer")
	CType10.grid(row=11,column=1)

	CType11 = Label(appMarg, text="Hammer")
	CType11.grid(row=12,column=1)

	CType12 = Label(appMarg, text="Hammer")
	CType12.grid(row=13,column=1)

	CType13 = Label(appMarg, text="Blaster")
	CType13.grid(row=14,column=1)

	CType14 = Label(appMarg, text="Blaster")
	CType14.grid(row=15,column=1)

	CType15 = Label(appMarg, text="Gauntlet")
	CType15.grid(row=16,column=1)

	CType16 = Label(appMarg, text="Greatsword")
	CType16.grid(row=17,column=1)

	CType17 = Label(appMarg, text="Greatsword")
	CType17.grid(row=18,column=1)

	CType18 = Label(appMarg, text="Greatsword")
	CType18.grid(row=19,column=1)

	################################## Label A ##################################
	CType0A = Label(appMarg, text="Gauntlet")
	CType0A.grid(row=1,column=4)

	CType1A = Label(appMarg, text="Katar")
	CType1A.grid(row=2,column=4)

	CType2A = Label(appMarg, text="Katar")
	CType2A.grid(row=3,column=4)

	CType3A = Label(appMarg, text="Bow")
	CType3A.grid(row=4,column=4)

	CType4A = Label(appMarg, text="Bow")
	CType4A.grid(row=5,column=4)

	CType5A = Label(appMarg, text="Spear")
	CType5A.grid(row=6,column=4)

	CType6A = Label(appMarg, text="Spear")
	CType6A.grid(row=7,column=4)

	CType7A = Label(appMarg, text="Spear")
	CType7A.grid(row=8,column=4)

	CType8A = Label(appMarg, text="Hammer")
	CType8A.grid(row=9,column=4)

	CType9A = Label(appMarg, text="Hammer")
	CType9A.grid(row=10,column=4)

	CType10A = Label(appMarg, text="Blaster")
	CType10A.grid(row=11,column=4)

	CType11A = Label(appMarg, text="Scythe")
	CType11A.grid(row=12,column=4)

	CType12A = Label(appMarg, text="Gauntlet")
	CType12A.grid(row=13,column=4)

	CType13A = Label(appMarg, text="Axe")
	CType13A.grid(row=14,column=4)

	CType14A = Label(appMarg, text="Axe")
	CType14A.grid(row=15,column=4)

	CType15A = Label(appMarg, text="Axe")
	CType15A.grid(row=16,column=4)

	CType16A = Label(appMarg, text="Gauntlet")
	CType16A.grid(row=17,column=4)

	CType17A = Label(appMarg, text="Bow")
	CType17A.grid(row=18,column=4)

	CType18A = Label(appMarg, text="Bow")
	CType18A.grid(row=19,column=4)

	################################## Label A 2 ##################################
	CType0A2 = Label(appMarg, text="DJFF")
	CType0A2.grid(row=1,column=7)

	CType1A2 = Label(appMarg, text="Scythe")
	CType1A2.grid(row=2,column=7)

	CType2A2 = Label(appMarg, text="Scythe")
	CType2A2.grid(row=3,column=7)

	CType3A2 = Label(appMarg, text="Orb")
	CType3A2.grid(row=4,column=7)

	CType4A2 = Label(appMarg, text="Spear")
	CType4A2.grid(row=5,column=7)

	CType5A2 = Label(appMarg, text="Cannon")
	CType5A2.grid(row=6,column=7)

	CType6A2 = Label(appMarg, text="Cannon")
	CType6A2.grid(row=7,column=7)

	CType7A2 = Label(appMarg, text="Cannon")
	CType7A2.grid(row=8,column=7)

	CType8A2 = Label(appMarg, text="Katar")
	CType8A2.grid(row=9,column=7)

	CType9A2 = Label(appMarg, text="Katar")
	CType9A2.grid(row=10,column=7)

	CType10A2 = Label(appMarg, text="Asuri")
	CType10A2.grid(row=11,column=7)

	CType11A2 = Label(appMarg, text="Nix")
	CType11A2.grid(row=12,column=7)

	CType12A2 = Label(appMarg, text="Jiro")
	CType12A2.grid(row=13,column=7)

	CType13A2 = Label(appMarg, text="Koji")
	CType13A2.grid(row=14,column=7)

	CType14A2 = Label(appMarg, text="Yumiko")
	CType14A2.grid(row=15,column=7)

	CType15A2 = Label(appMarg, text="Teros")
	CType15A2.grid(row=16,column=7)

	CType16A2 = Label(appMarg, text="Bow")
	CType16A2.grid(row=17,column=7)

	CType17A2 = Label(appMarg, text="Blaster")
	CType17A2.grid(row=18,column=7)

	CType18A2 = Label(appMarg, text="Blaster")
	CType18A2.grid(row=19,column=7)

	################################## Key ##################################
	CType0Text		=	StringVar(None)
	CType0Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType0Text, state='readonly')
	CType0Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType0Input.set('None')
	CType0Input.grid(row=1,column=2)

	CType1Text		=	StringVar(None)
	CType1Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType1Text, state='readonly')
	CType1Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType1Input.set('None')
	CType1Input.grid(row=2,column=2)

	CType2Text		=	StringVar(None)
	CType2Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType2Text, state='readonly')
	CType2Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType2Input.set('None')
	CType2Input.grid(row=3,column=2)

	CType3Text		=	StringVar(None)
	CType3Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType3Text, state='readonly')
	CType3Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType3Input.set('None')
	CType3Input.grid(row=4,column=2)

	CType4Text		=	StringVar(None)
	CType4Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType4Text, state='readonly')
	CType4Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType4Input.set('None')
	CType4Input.grid(row=5,column=2)

	CType5Text		=	StringVar(None)
	CType5Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType5Text, state='readonly')
	CType5Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType5Input.set('None')
	CType5Input.grid(row=6,column=2)

	CType6Text		=	StringVar(None)
	CType6Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType6Text, state='readonly')
	CType6Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType6Input.set('None')
	CType6Input.grid(row=7,column=2)

	CType7Text		=	StringVar(None)
	CType7Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType7Text, state='readonly')
	CType7Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType7Input.set('None')
	CType7Input.grid(row=8,column=2)

	CType8Text		=	StringVar(None)
	CType8Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType8Text, state='readonly')
	CType8Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType8Input.set('None')
	CType8Input.grid(row=9,column=2)

	CType9Text		=	StringVar(None)
	CType9Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType9Text, state='readonly')
	CType9Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType9Input.set('None')
	CType9Input.grid(row=10,column=2)

	CType10Text		=	StringVar(None)
	CType10Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType10Text, state='readonly')
	CType10Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType10Input.set('None')
	CType10Input.grid(row=11,column=2)

	CType11Text		=	StringVar(None)
	CType11Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType11Text, state='readonly')
	CType11Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType11Input.set('None')
	CType11Input.grid(row=12,column=2)

	CType12Text		=	StringVar(None)
	CType12Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType12Text, state='readonly')
	CType12Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType12Input.set('None')
	CType12Input.grid(row=13,column=2)

	CType13Text		=	StringVar(None)
	CType13Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType13Text, state='readonly')
	CType13Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType13Input.set('None')
	CType13Input.grid(row=14,column=2)

	CType14Text		=	StringVar(None)
	CType14Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType14Text, state='readonly')
	CType14Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType14Input.set('None')
	CType14Input.grid(row=15,column=2)

	CType15Text		=	StringVar(None)
	CType15Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType15Text, state='readonly')
	CType15Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType15Input.set('None')
	CType15Input.grid(row=16,column=2)

	CType16Text		=	StringVar(None)
	CType16Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType16Text, state='readonly')
	CType16Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType16Input.set('None')
	CType16Input.grid(row=17,column=2)

	CType17Text		=	StringVar(None)
	CType17Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType17Text, state='readonly')
	CType17Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType17Input.set('None')
	CType17Input.grid(row=18,column=2)

	CType18Text		=	StringVar(None)
	CType18Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType18Text, state='readonly')
	CType18Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType18Input.set('None')
	CType18Input.grid(row=19,column=2)


	################################## Key A ##################################
	CType0TextA		=	StringVar(None)
	CType0InputA 	=	ttk.Combobox(appMarg, width=5, textvariable=CType0TextA, state='readonly')
	CType0InputA['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType0InputA.set('None')
	CType0InputA.grid(row=1,column=5)

	CType1TextA		=	StringVar(None)
	CType1InputA 	=	ttk.Combobox(appMarg, width=5, textvariable=CType1TextA, state='readonly')
	CType1InputA['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType1InputA.set('None')
	CType1InputA.grid(row=2,column=5)

	CType2TextA		=	StringVar(None)
	CType2InputA 	=	ttk.Combobox(appMarg, width=5, textvariable=CType2TextA, state='readonly')
	CType2InputA['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType2InputA.set('None')
	CType2InputA.grid(row=3,column=5)

	CType3TextA		=	StringVar(None)
	CType3InputA 	=	ttk.Combobox(appMarg, width=5, textvariable=CType3TextA, state='readonly')
	CType3InputA['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType3InputA.set('None')
	CType3InputA.grid(row=4,column=5)

	CType4TextA		=	StringVar(None)
	CType4InputA 	=	ttk.Combobox(appMarg, width=5, textvariable=CType4TextA, state='readonly')
	CType4InputA['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType4InputA.set('None')
	CType4InputA.grid(row=5,column=5)

	CType5TextA		=	StringVar(None)
	CType5InputA 	=	ttk.Combobox(appMarg, width=5, textvariable=CType5TextA, state='readonly')
	CType5InputA['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType5InputA.set('None')
	CType5InputA.grid(row=6,column=5)

	CType6TextA		=	StringVar(None)
	CType6InputA 	=	ttk.Combobox(appMarg, width=5, textvariable=CType6TextA, state='readonly')
	CType6InputA['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType6InputA.set('None')
	CType6InputA.grid(row=7,column=5)

	CType7TextA		=	StringVar(None)
	CType7InputA 	=	ttk.Combobox(appMarg, width=5, textvariable=CType7TextA, state='readonly')
	CType7InputA['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType7InputA.set('None')
	CType7InputA.grid(row=8,column=5)

	CType8TextA		=	StringVar(None)
	CType8InputA 	=	ttk.Combobox(appMarg, width=5, textvariable=CType8TextA, state='readonly')
	CType8InputA['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType8InputA.set('None')
	CType8InputA.grid(row=9,column=5)

	CType9TextA		=	StringVar(None)
	CType9InputA 	=	ttk.Combobox(appMarg, width=5, textvariable=CType9TextA, state='readonly')
	CType9InputA['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType9InputA.set('None')
	CType9InputA.grid(row=10,column=5)

	CType10TextA		=	StringVar(None)
	CType10InputA 	=	ttk.Combobox(appMarg, width=5, textvariable=CType10TextA, state='readonly')
	CType10InputA['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType10InputA.set('None')
	CType10InputA.grid(row=11,column=5)

	CType11TextA		=	StringVar(None)
	CType11InputA 	=	ttk.Combobox(appMarg, width=5, textvariable=CType11TextA, state='readonly')
	CType11InputA['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType11InputA.set('None')
	CType11InputA.grid(row=12,column=5)

	CType12TextA		=	StringVar(None)
	CType12InputA 	=	ttk.Combobox(appMarg, width=5, textvariable=CType12TextA, state='readonly')
	CType12InputA['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType12InputA.set('None')
	CType12InputA.grid(row=13,column=5)

	CType13TextA		=	StringVar(None)
	CType13InputA 	=	ttk.Combobox(appMarg, width=5, textvariable=CType13TextA, state='readonly')
	CType13InputA['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType13InputA.set('None')
	CType13InputA.grid(row=14,column=5)

	CType14TextA		=	StringVar(None)
	CType14InputA 	=	ttk.Combobox(appMarg, width=5, textvariable=CType14TextA, state='readonly')
	CType14InputA['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType14InputA.set('None')
	CType14InputA.grid(row=15,column=5)

	CType15TextA		=	StringVar(None)
	CType15InputA 	=	ttk.Combobox(appMarg, width=5, textvariable=CType15TextA, state='readonly')
	CType15InputA['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType15InputA.set('None')
	CType15InputA.grid(row=16,column=5)

	CType16TextA		=	StringVar(None)
	CType16InputA 	=	ttk.Combobox(appMarg, width=5, textvariable=CType16TextA, state='readonly')
	CType16InputA['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType16InputA.set('None')
	CType16InputA.grid(row=17,column=5)

	CType17TextA		=	StringVar(None)
	CType17InputA 	=	ttk.Combobox(appMarg, width=5, textvariable=CType17TextA, state='readonly')
	CType17InputA['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType17InputA.set('None')
	CType17InputA.grid(row=18,column=5)

	CType18TextA		=	StringVar(None)
	CType18InputA 	=	ttk.Combobox(appMarg, width=5, textvariable=CType18TextA, state='readonly')
	CType18InputA['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType18InputA.set('None')
	CType18InputA.grid(row=19,column=5)

	################################## Key A 2 ##################################
	CType0TextA2		=	StringVar(None)
	CType0InputA2 	=	ttk.Combobox(appMarg, width=5, textvariable=CType0TextA2, state='readonly')
	CType0InputA2['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType0InputA2.set('None')
	CType0InputA2.grid(row=1,column=8)

	CType1TextA2		=	StringVar(None)
	CType1InputA2 	=	ttk.Combobox(appMarg, width=5, textvariable=CType1TextA2, state='readonly')
	CType1InputA2['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType1InputA2.set('None')
	CType1InputA2.grid(row=2,column=8)

	CType2TextA2		=	StringVar(None)
	CType2InputA2 	=	ttk.Combobox(appMarg, width=5, textvariable=CType2TextA2, state='readonly')
	CType2InputA2['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType2InputA2.set('None')
	CType2InputA2.grid(row=3,column=8)

	CType3TextA2		=	StringVar(None)
	CType3InputA2 	=	ttk.Combobox(appMarg, width=5, textvariable=CType3TextA2, state='readonly')
	CType3InputA2['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType3InputA2.set('None')
	CType3InputA2.grid(row=4,column=8)

	CType4TextA2		=	StringVar(None)
	CType4InputA2 	=	ttk.Combobox(appMarg, width=5, textvariable=CType4TextA2, state='readonly')
	CType4InputA2['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType4InputA2.set('None')
	CType4InputA2.grid(row=5,column=8)

	CType5TextA2		=	StringVar(None)
	CType5InputA2 	=	ttk.Combobox(appMarg, width=5, textvariable=CType5TextA2, state='readonly')
	CType5InputA2['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType5InputA2.set('None')
	CType5InputA2.grid(row=6,column=8)

	CType6TextA2		=	StringVar(None)
	CType6InputA2 	=	ttk.Combobox(appMarg, width=5, textvariable=CType6TextA2, state='readonly')
	CType6InputA2['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType6InputA2.set('None')
	CType6InputA2.grid(row=7,column=8)

	CType7TextA2		=	StringVar(None)
	CType7InputA2 	=	ttk.Combobox(appMarg, width=5, textvariable=CType7TextA2, state='readonly')
	CType7InputA2['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType7InputA2.set('None')
	CType7InputA2.grid(row=8,column=8)

	CType8TextA2		=	StringVar(None)
	CType8InputA2 	=	ttk.Combobox(appMarg, width=5, textvariable=CType8TextA2, state='readonly')
	CType8InputA2['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType8InputA2.set('None')
	CType8InputA2.grid(row=9,column=8)

	CType9TextA2		=	StringVar(None)
	CType9InputA2 	=	ttk.Combobox(appMarg, width=5, textvariable=CType9TextA2, state='readonly')
	CType9InputA2['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType9InputA2.set('None')
	CType9InputA2.grid(row=10,column=8)

	CType10TextA2		=	StringVar(None)
	CType10InputA2 	=	ttk.Combobox(appMarg, width=5, textvariable=CType10TextA2, state='readonly')
	CType10InputA2['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType10InputA2.set('None')
	CType10InputA2.grid(row=11,column=8)

	CType11TextA2		=	StringVar(None)
	CType11InputA2 	=	ttk.Combobox(appMarg, width=5, textvariable=CType11TextA2, state='readonly')
	CType11InputA2['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType11InputA2.set('None')
	CType11InputA2.grid(row=12,column=8)

	CType12TextA2		=	StringVar(None)
	CType12InputA2 	=	ttk.Combobox(appMarg, width=5, textvariable=CType12TextA2, state='readonly')
	CType12InputA2['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType12InputA2.set('None')
	CType12InputA2.grid(row=13,column=8)

	CType13TextA2		=	StringVar(None)
	CType13InputA2 	=	ttk.Combobox(appMarg, width=5, textvariable=CType13TextA2, state='readonly')
	CType13InputA2['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType13InputA2.set('None')
	CType13InputA2.grid(row=14,column=8)

	CType14TextA2		=	StringVar(None)
	CType14InputA2 	=	ttk.Combobox(appMarg, width=5, textvariable=CType14TextA2, state='readonly')
	CType14InputA2['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType14InputA2.set('None')
	CType14InputA2.grid(row=15,column=8)

	CType15TextA2		=	StringVar(None)
	CType15InputA2 	=	ttk.Combobox(appMarg, width=5, textvariable=CType15TextA2, state='readonly')
	CType15InputA2['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType15InputA2.set('None')
	CType15InputA2.grid(row=16,column=8)

	CType16TextA2		=	StringVar(None)
	CType16InputA2 	=	ttk.Combobox(appMarg, width=5, textvariable=CType16TextA2, state='readonly')
	CType16InputA2['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType16InputA2.set('None')
	CType16InputA2.grid(row=17,column=8)

	CType17TextA2		=	StringVar(None)
	CType17InputA2 	=	ttk.Combobox(appMarg, width=5, textvariable=CType17TextA2, state='readonly')
	CType17InputA2['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType17InputA2.set('None')
	CType17InputA2.grid(row=18,column=8)

	CType18TextA2		=	StringVar(None)
	CType18InputA2 	=	ttk.Combobox(appMarg, width=5, textvariable=CType18TextA2, state='readonly')
	CType18InputA2['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType18InputA2.set('None')
	CType18InputA2.grid(row=19,column=8)

	################################## Reset ##################################
	CType0DisableButton = ttk.Button(appMarg, text = "Reset", command = CType0DisableCmd)
	CType0DisableButton.grid(row=1,column=3)

	CType1DisableButton = ttk.Button(appMarg, text = "Reset", command = CType1DisableCmd)
	CType1DisableButton.grid(row=2,column=3)

	CType2DisableButton = ttk.Button(appMarg, text = "Reset", command = CType2DisableCmd)
	CType2DisableButton.grid(row=3,column=3)

	CType3DisableButton = ttk.Button(appMarg, text = "Reset", command = CType3DisableCmd)
	CType3DisableButton.grid(row=4,column=3)

	CType4DisableButton = ttk.Button(appMarg, text = "Reset", command = CType4DisableCmd)
	CType4DisableButton.grid(row=5,column=3)

	CType5DisableButton = ttk.Button(appMarg, text = "Reset", command = CType5DisableCmd)
	CType5DisableButton.grid(row=6,column=3)

	CType6DisableButton = ttk.Button(appMarg, text = "Reset", command = CType6DisableCmd)
	CType6DisableButton.grid(row=7,column=3)

	CType7DisableButton = ttk.Button(appMarg, text = "Reset", command = CType7DisableCmd)
	CType7DisableButton.grid(row=8,column=3)

	CType8DisableButton = ttk.Button(appMarg, text = "Reset", command = CType8DisableCmd)
	CType8DisableButton.grid(row=9,column=3)

	CType9DisableButton = ttk.Button(appMarg, text = "Reset", command = CType9DisableCmd)
	CType9DisableButton.grid(row=10,column=3)

	CType10DisableButton = ttk.Button(appMarg, text = "Reset", command = CType10DisableCmd)
	CType10DisableButton.grid(row=11,column=3)

	CType11DisableButton = ttk.Button(appMarg, text = "Reset", command = CType11DisableCmd)
	CType11DisableButton.grid(row=12,column=3)

	CType12DisableButton = ttk.Button(appMarg, text = "Reset", command = CType12DisableCmd)
	CType12DisableButton.grid(row=13,column=3)

	CType13DisableButton = ttk.Button(appMarg, text = "Reset", command = CType13DisableCmd)
	CType13DisableButton.grid(row=14,column=3)

	CType14DisableButton = ttk.Button(appMarg, text = "Reset", command = CType14DisableCmd)
	CType14DisableButton.grid(row=15,column=3)

	CType15DisableButton = ttk.Button(appMarg, text = "Reset", command = CType15DisableCmd)
	CType15DisableButton.grid(row=16,column=3)

	CType16DisableButton = ttk.Button(appMarg, text = "Reset", command = CType16DisableCmd)
	CType16DisableButton.grid(row=17,column=3)

	CType17DisableButton = ttk.Button(appMarg, text = "Reset", command = CType17DisableCmd)
	CType17DisableButton.grid(row=18,column=3)

	CType18DisableButton = ttk.Button(appMarg, text = "Reset", command = CType18DisableCmd)
	CType18DisableButton.grid(row=19,column=3)


	################################## Reset A ##################################
	CType0DisableButtonA = ttk.Button(appMarg, text = "Reset", command = CType0DisableCmdA)
	CType0DisableButtonA.grid(row=1,column=6)

	CType1DisableButtonA = ttk.Button(appMarg, text = "Reset", command = CType1DisableCmdA)
	CType1DisableButtonA.grid(row=2,column=6)

	CType2DisableButtonA = ttk.Button(appMarg, text = "Reset", command = CType2DisableCmdA)
	CType2DisableButtonA.grid(row=3,column=6)

	CType3DisableButtonA = ttk.Button(appMarg, text = "Reset", command = CType3DisableCmdA)
	CType3DisableButtonA.grid(row=4,column=6)

	CType4DisableButtonA = ttk.Button(appMarg, text = "Reset", command = CType4DisableCmdA)
	CType4DisableButtonA.grid(row=5,column=6)

	CType5DisableButtonA = ttk.Button(appMarg, text = "Reset", command = CType5DisableCmdA)
	CType5DisableButtonA.grid(row=6,column=6)

	CType6DisableButtonA = ttk.Button(appMarg, text = "Reset", command = CType6DisableCmdA)
	CType6DisableButtonA.grid(row=7,column=6)

	CType7DisableButtonA = ttk.Button(appMarg, text = "Reset", command = CType7DisableCmdA)
	CType7DisableButtonA.grid(row=8,column=6)

	CType8DisableButtonA = ttk.Button(appMarg, text = "Reset", command = CType8DisableCmdA)
	CType8DisableButtonA.grid(row=9,column=6)

	CType9DisableButtonA = ttk.Button(appMarg, text = "Reset", command = CType9DisableCmdA)
	CType9DisableButtonA.grid(row=10,column=6)

	CType10DisableButtonA = ttk.Button(appMarg, text = "Reset", command = CType10DisableCmdA)
	CType10DisableButtonA.grid(row=11,column=6)

	CType11DisableButtonA = ttk.Button(appMarg, text = "Reset", command = CType11DisableCmdA)
	CType11DisableButtonA.grid(row=12,column=6)

	CType12DisableButtonA = ttk.Button(appMarg, text = "Reset", command = CType12DisableCmdA)
	CType12DisableButtonA.grid(row=13,column=6)

	CType13DisableButtonA = ttk.Button(appMarg, text = "Reset", command = CType13DisableCmdA)
	CType13DisableButtonA.grid(row=14,column=6)

	CType14DisableButtonA = ttk.Button(appMarg, text = "Reset", command = CType14DisableCmdA)
	CType14DisableButtonA.grid(row=15,column=6)

	CType15DisableButtonA = ttk.Button(appMarg, text = "Reset", command = CType15DisableCmdA)
	CType15DisableButtonA.grid(row=16,column=6)

	CType16DisableButtonA = ttk.Button(appMarg, text = "Reset", command = CType16DisableCmdA)
	CType16DisableButtonA.grid(row=17,column=6)

	CType17DisableButtonA = ttk.Button(appMarg, text = "Reset", command = CType17DisableCmdA)
	CType17DisableButtonA.grid(row=18,column=6)

	CType18DisableButtonA = ttk.Button(appMarg, text = "Reset", command = CType18DisableCmdA)
	CType18DisableButtonA.grid(row=19,column=6)


	################################## Reset A 2 ##################################
	CType0DisableButtonA2 = ttk.Button(appMarg, text = "Reset", command = CType0DisableCmdA2)
	CType0DisableButtonA2.grid(row=1,column=9)

	CType1DisableButtonA2 = ttk.Button(appMarg, text = "Reset", command = CType1DisableCmdA2)
	CType1DisableButtonA2.grid(row=2,column=9)

	CType2DisableButtonA2 = ttk.Button(appMarg, text = "Reset", command = CType2DisableCmdA2)
	CType2DisableButtonA2.grid(row=3,column=9)

	CType3DisableButtonA2 = ttk.Button(appMarg, text = "Reset", command = CType3DisableCmdA2)
	CType3DisableButtonA2.grid(row=4,column=9)

	CType4DisableButtonA2 = ttk.Button(appMarg, text = "Reset", command = CType4DisableCmdA2)
	CType4DisableButtonA2.grid(row=5,column=9)

	CType5DisableButtonA2 = ttk.Button(appMarg, text = "Reset", command = CType5DisableCmdA2)
	CType5DisableButtonA2.grid(row=6,column=9)

	CType6DisableButtonA2 = ttk.Button(appMarg, text = "Reset", command = CType6DisableCmdA2)
	CType6DisableButtonA2.grid(row=7,column=9)

	CType7DisableButtonA2 = ttk.Button(appMarg, text = "Reset", command = CType7DisableCmdA2)
	CType7DisableButtonA2.grid(row=8,column=9)

	CType8DisableButtonA2 = ttk.Button(appMarg, text = "Reset", command = CType8DisableCmdA2)
	CType8DisableButtonA2.grid(row=9,column=9)

	CType9DisableButtonA2 = ttk.Button(appMarg, text = "Reset", command = CType9DisableCmdA2)
	CType9DisableButtonA2.grid(row=10,column=9)

	CType10DisableButtonA2 = ttk.Button(appMarg, text = "Reset", command = CType10DisableCmdA2)
	CType10DisableButtonA2.grid(row=11,column=9)

	CType11DisableButtonA2 = ttk.Button(appMarg, text = "Reset", command = CType11DisableCmdA2)
	CType11DisableButtonA2.grid(row=12,column=9)

	CType12DisableButtonA2 = ttk.Button(appMarg, text = "Reset", command = CType12DisableCmdA2)
	CType12DisableButtonA2.grid(row=13,column=9)

	CType13DisableButtonA2 = ttk.Button(appMarg, text = "Reset", command = CType13DisableCmdA2)
	CType13DisableButtonA2.grid(row=14,column=9)

	CType14DisableButtonA2 = ttk.Button(appMarg, text = "Reset", command = CType14DisableCmdA2)
	CType14DisableButtonA2.grid(row=15,column=9)

	CType15DisableButtonA2 = ttk.Button(appMarg, text = "Reset", command = CType15DisableCmdA2)
	CType15DisableButtonA2.grid(row=16,column=9)

	CType16DisableButtonA2 = ttk.Button(appMarg, text = "Reset", command = CType16DisableCmdA2)
	CType16DisableButtonA2.grid(row=17,column=9)

	CType17DisableButtonA2 = ttk.Button(appMarg, text = "Reset", command = CType17DisableCmdA2)
	CType17DisableButtonA2.grid(row=18,column=9)

	CType18DisableButtonA2 = ttk.Button(appMarg, text = "Reset", command = CType18DisableCmdA2)
	CType18DisableButtonA2.grid(row=19,column=9)

	def OnExit():
		ButtonState["state"] = "normal"
		CType0DisableCmd(); CType1DisableCmd();
		CType2DisableCmd(); CType3DisableCmd();
		CType4DisableCmd(); CType5DisableCmd();
		CType6DisableCmd(); CType7DisableCmd();
		CType8DisableCmd(); CType9DisableCmd();
		CType10DisableCmd(); CType11DisableCmd();
		CType12DisableCmd(); CType13DisableCmd();
		CType14DisableCmd(); CType15DisableCmd();
		CType16DisableCmd(); CType17DisableCmd();
		CType18DisableCmd();

		CType0DisableCmdA(); CType1DisableCmdA();
		CType2DisableCmdA(); CType3DisableCmdA();
		CType4DisableCmdA(); CType5DisableCmdA();
		CType6DisableCmdA(); CType7DisableCmdA();
		CType8DisableCmdA(); CType9DisableCmdA();
		CType10DisableCmdA(); CType11DisableCmdA();
		CType12DisableCmdA(); CType13DisableCmdA();
		CType14DisableCmdA(); CType15DisableCmdA();
		CType16DisableCmdA(); CType17DisableCmdA();
		CType18DisableCmdA();

		CType0DisableCmdA2(); CType1DisableCmdA2();
		CType2DisableCmdA2(); CType3DisableCmdA2();
		CType4DisableCmdA2(); CType5DisableCmdA2();
		CType6DisableCmdA2(); CType7DisableCmdA2();
		CType8DisableCmdA2(); CType9DisableCmdA2();
		CType10DisableCmdA2(); CType11DisableCmdA2();
		CType12DisableCmdA2(); CType13DisableCmdA2();
		CType14DisableCmdA2(); CType15DisableCmdA2();
		CType16DisableCmdA2(); CType17DisableCmdA2();
		CType18DisableCmdA2();

		# outputConsole(output, 'Exit')
		app.destroy()

	ExitAppButton = ttk.Button(app, text="Exit", command=OnExit)
	ExitAppButton.pack(side="bottom")

	def disableX():
		pass
	app.protocol("WM_DELETE_WINDOW", disableX)
	app.mainloop()