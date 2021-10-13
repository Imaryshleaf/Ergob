import tkinter as tk
from tkinter import Button, Frame, Entry, Label, ttk, StringVar, PhotoImage, filedialog
import os
import sys
from inputs import keyinputs
from time import sleep
import json

# Provide relative path to packed file
def resource_path(relative_path):
	try:
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)
# End

# Json 1
try:
	if os.path.exists(os.getcwd() + '/collections/keybinds.json'):
		with open("./collections/keybinds.json") as f:
			keybindData = json.load(f)
	UP = keybindData["Move Up"]
	DOWN = keybindData["Move Down"]
	RIGHT = keybindData["Move Right"]
	LEFT = keybindData["Move Left"]
	JUMP = keybindData["Jump"]
	DODGE = keybindData["Dodge"]
	THROW = keybindData["Throw"]
	PICKUP = keybindData["Pickup"]
	LightAttack = keybindData["Quick Attack"]
	HeavyAttack = keybindData["Heavy Attack"]
except Exception:
	pass

# Json 2
try:
	if os.path.exists(os.getcwd() + '/collections/application.json'):
		with open("./collections/application.json") as f:
			applicationData = json.load(f);
	AvatarLocation = applicationData["AvatarLocation"];
except Exception:
	pass

# Open Settings
def Open(widget):
	# Ask to update avatar image
	def ChooseAvatar():
		try:
			global filename
			print("Recommended Image Dimension: 128x128")
			UpdateAvatarButton['state'] = "disabled"
			filename = filedialog.askopenfile(title='Select Image File')
			applicationData["AvatarLocation"] = filename.name;
			with open (os.getcwd() + '/collections/application.json', 'w+') as f:
				json.dump(applicationData, f, indent=4, sort_keys=False)
			sys.exit(1)
		except Exception:
			print("Cancelled update avatar")
			UpdateAvatarButton["state"] = "enabled"
	# End

	# Save avatar Frame Rate
	def UpdateAvatarFrameRate():
		applicationData["AnimationSpeed"] = FrameRateTxt.get();
		with open (os.getcwd() + '/collections/application.json', 'w+') as f:
			json.dump(applicationData, f, indent=4, sort_keys=False)
		sys.exit(1)
	# End

	app = tk.Toplevel()
	app.resizable(False, False)
	app.configure(bg="#424549")
	app.geometry("370x330")
	app.title("Settings")
	app.iconbitmap(resource_path('icon/ergo.ico'))
	# app.attributes('-topmost', 'true')

	appMargin = tk.LabelFrame(app)
	appMargin.grid(row=0, column=0)
	appMargin.configure(bd=3, padx=2, pady=2)

	appMarg = tk.LabelFrame(appMargin, text="Avatar")
	appMarg.grid(row=1, column=1)
	appMarg.configure(bd=2, padx=2, pady=2)

	appMarg1 = tk.LabelFrame(appMargin, text="Controller")
	appMarg1.grid(row=2, column=1)
	appMarg1.configure(bd=2, padx=2, pady=2)

	UpdateAvatarButton = ttk.Button(appMarg, text="Update Avatar", command=ChooseAvatar)
	UpdateAvatarButton.grid(row=1, column=1)
	UpdateAvatarFrame = tk.Label(appMarg, text="Avatar Frame Rate: ")
	UpdateAvatarFrame.grid(row=1, column=2)

	FrameRateTxt = StringVar(None)
	FrameRateOpt =ttk.Combobox(appMarg, width=10, textvariable=FrameRateTxt, state='readonly')
	FrameRateOpt['values']= ("10","30","50","70","100", "150", "200")
	FrameRateOpt.grid(row=1,column=3)
	FrameRateOpt.set('None')

	SaveFrameRateButton = ttk.Button(appMarg, text="Save", command=UpdateAvatarFrameRate)
	SaveFrameRateButton.grid(row=1, column=4)

	# Move Up
	# Save Move Up Key
	def SaveMoveUpKey():
		keybindData["Move Up"] = MoveUpTxt.get();
		with open (os.getcwd() + '/collections/keybinds.json', 'w+') as f:
			json.dump(keybindData, f, indent=4, sort_keys=False)
		sys.exit(1)
	# End
	MoveUpLabel = tk.Label(appMarg1, text="Move Up:")
	MoveUpLabel.grid(row=1,column=1)
	MoveUpTxt = StringVar(None)
	MoveUpKey =ttk.Combobox(appMarg1, width=15, textvariable=MoveUpTxt, state='readonly')
	MoveUpKey['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Down', 'DOWN', 'Up', 'UP', 'Left', 'LEFT', 'Right', 'RIGHT', 'Shift', 'SHIFT', 'Ctrl', 'CTRL', 'Esc', 'ESC', 'Alt', 'ALT', 'Space', 'SPACE', 'Enter', 'ENTER','Spacebar', 'SPACEBAR', 'Tab', 'TAB', 'Home', 'HOME', 'End', 'END', 'Plus', 'PLUS', 'Minus', 'MINUS', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Up arrow', 'Down arrow', 'Left arrow', 'Right arrow')
	MoveUpKey.grid(row=1,column=2)
	MoveUpKey.set('None')
	MoveUpUpdateButton = ttk.Button(appMarg1, text="Update", command=SaveMoveUpKey)
	MoveUpUpdateButton.grid(row=1,column=3)

	# Move Down
	# Save Move Down Key
	def SaveMoveDownKey():
		keybindData["Move Down"] = MoveDownTxt.get();
		with open (os.getcwd() + '/collections/keybinds.json', 'w+') as f:
			json.dump(keybindData, f, indent=4, sort_keys=False)
		sys.exit(1)
	# End
	MoveDownLabel = tk.Label(appMarg1, text="Move Down:")
	MoveDownLabel.grid(row=2,column=1)
	MoveDownTxt = StringVar(None)
	MoveDownKey =ttk.Combobox(appMarg1, width=15, textvariable=MoveDownTxt, state='readonly')
	MoveDownKey['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Down', 'DOWN', 'Up', 'UP', 'Left', 'LEFT', 'Right', 'RIGHT', 'Shift', 'SHIFT', 'Ctrl', 'CTRL', 'Esc', 'ESC', 'Alt', 'ALT', 'Space', 'SPACE', 'Enter', 'ENTER','Spacebar', 'SPACEBAR', 'Tab', 'TAB', 'Home', 'HOME', 'End', 'END', 'Plus', 'PLUS', 'Minus', 'MINUS', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Up arrow', 'Down arrow', 'Left arrow', 'Right arrow')
	MoveDownKey.grid(row=2,column=2)
	MoveDownKey.set('None')
	MoveDownUpdateButton = ttk.Button(appMarg1, text="Update", command=SaveMoveDownKey)
	MoveDownUpdateButton.grid(row=2,column=3)

	# Move Left
	# Save Move Left Key
	def SaveMoveLeftKey():
		keybindData["Move Left"] = MoveLeftTxt.get();
		with open (os.getcwd() + '/collections/keybinds.json', 'w+') as f:
			json.dump(keybindData, f, indent=4, sort_keys=False)
		sys.exit(1)
	# End
	MoveLeftLabel = tk.Label(appMarg1, text="Move Left:")
	MoveLeftLabel.grid(row=3,column=1)
	MoveLeftTxt = StringVar(None)
	MoveLeftKey =ttk.Combobox(appMarg1, width=15, textvariable=MoveLeftTxt, state='readonly')
	MoveLeftKey['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Down', 'DOWN', 'Up', 'UP', 'Left', 'LEFT', 'Right', 'RIGHT', 'Shift', 'SHIFT', 'Ctrl', 'CTRL', 'Esc', 'ESC', 'Alt', 'ALT', 'Space', 'SPACE', 'Enter', 'ENTER','Spacebar', 'SPACEBAR', 'Tab', 'TAB', 'Home', 'HOME', 'End', 'END', 'Plus', 'PLUS', 'Minus', 'MINUS', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Up arrow', 'Down arrow', 'Left arrow', 'Right arrow')
	MoveLeftKey.grid(row=3,column=2)
	MoveLeftKey.set('None')
	MoveLeftUpdateButton = ttk.Button(appMarg1, text="Update", command=SaveMoveLeftKey)
	MoveLeftUpdateButton.grid(row=3,column=3)

	# Move Right
	# Save Move Right Key
	def SaveMoveRightKey():
		keybindData["Move Right"] = MoveRightTxt.get();
		with open (os.getcwd() + '/collections/keybinds.json', 'w+') as f:
			json.dump(keybindData, f, indent=4, sort_keys=False)
		sys.exit(1)
	# End
	MoveRightLabel = tk.Label(appMarg1, text="Move Right:")
	MoveRightLabel.grid(row=4,column=1)
	MoveRightTxt = StringVar(None)
	MoveRightKey =ttk.Combobox(appMarg1, width=15, textvariable=MoveRightTxt, state='readonly')
	MoveRightKey['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Down', 'DOWN', 'Up', 'UP', 'Left', 'LEFT', 'Right', 'RIGHT', 'Shift', 'SHIFT', 'Ctrl', 'CTRL', 'Esc', 'ESC', 'Alt', 'ALT', 'Space', 'SPACE', 'Enter', 'ENTER','Spacebar', 'SPACEBAR', 'Tab', 'TAB', 'Home', 'HOME', 'End', 'END', 'Plus', 'PLUS', 'Minus', 'MINUS', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Up arrow', 'Down arrow', 'Left arrow', 'Right arrow')
	MoveRightKey.grid(row=4,column=2)
	MoveRightKey.set('None')
	MoveRightUpdateButton = ttk.Button(appMarg1, text="Update", command=SaveMoveRightKey)
	MoveRightUpdateButton.grid(row=4,column=3)

	# Jump
	# Save Move Jump Key
	def SaveMoveJumpKey():
		keybindData["Jump"] = MoveJumpTxt.get();
		with open (os.getcwd() + '/collections/keybinds.json', 'w+') as f:
			json.dump(keybindData, f, indent=4, sort_keys=False)
		sys.exit(1)
	# End
	MoveJumpLabel = tk.Label(appMarg1, text="Jump:")
	MoveJumpLabel.grid(row=5,column=1)
	MoveJumpTxt = StringVar(None)
	MoveJumpKey =ttk.Combobox(appMarg1, width=15, textvariable=MoveJumpTxt, state='readonly')
	MoveJumpKey['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Down', 'DOWN', 'Up', 'UP', 'Left', 'LEFT', 'Right', 'RIGHT', 'Shift', 'SHIFT', 'Ctrl', 'CTRL', 'Esc', 'ESC', 'Alt', 'ALT', 'Space', 'SPACE', 'Enter', 'ENTER','Spacebar', 'SPACEBAR', 'Tab', 'TAB', 'Home', 'HOME', 'End', 'END', 'Plus', 'PLUS', 'Minus', 'MINUS', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Up arrow', 'Down arrow', 'Left arrow', 'Right arrow')
	MoveJumpKey.grid(row=5,column=2)
	MoveJumpKey.set('None')
	MoveJumpUpdateButton = ttk.Button(appMarg1, text="Update", command=SaveMoveJumpKey)
	MoveJumpUpdateButton.grid(row=5,column=3)

	# Dodge
	# Save Move Dodge Key
	def SaveMoveDodgeKey():
		keybindData["Dodge"] = MoveDodgeTxt.get();
		with open (os.getcwd() + '/collections/keybinds.json', 'w+') as f:
			json.dump(keybindData, f, indent=4, sort_keys=False)
		sys.exit(1)
	# End
	MoveDodgeLabel = tk.Label(appMarg1, text="Dodge:")
	MoveDodgeLabel.grid(row=6,column=1)
	MoveDodgeTxt = StringVar(None)
	MoveDodgeKey =ttk.Combobox(appMarg1, width=15, textvariable=MoveDodgeTxt, state='readonly')
	MoveDodgeKey['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Down', 'DOWN', 'Up', 'UP', 'Left', 'LEFT', 'Right', 'RIGHT', 'Shift', 'SHIFT', 'Ctrl', 'CTRL', 'Esc', 'ESC', 'Alt', 'ALT', 'Space', 'SPACE', 'Enter', 'ENTER','Spacebar', 'SPACEBAR', 'Tab', 'TAB', 'Home', 'HOME', 'End', 'END', 'Plus', 'PLUS', 'Minus', 'MINUS', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Up arrow', 'Down arrow', 'Left arrow', 'Right arrow')
	MoveDodgeKey.grid(row=6,column=2)
	MoveDodgeKey.set('None')
	MoveDodgeUpdateButton = ttk.Button(appMarg1, text="Update", command=SaveMoveDodgeKey)
	MoveDodgeUpdateButton.grid(row=6,column=3)

	# Throw
	# Save Move Throw Key
	def SaveMoveThrowKey():
		keybindData["Throw"] = MoveThrowTxt.get();
		with open (os.getcwd() + '/collections/keybinds.json', 'w+') as f:
			json.dump(keybindData, f, indent=4, sort_keys=False)
		sys.exit(1)
	# End
	MoveThrowLabel = tk.Label(appMarg1, text="Throw:")
	MoveThrowLabel.grid(row=7,column=1)
	MoveThrowTxt = StringVar(None)
	MoveThrowKey =ttk.Combobox(appMarg1, width=15, textvariable=MoveThrowTxt, state='readonly')
	MoveThrowKey['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Down', 'DOWN', 'Up', 'UP', 'Left', 'LEFT', 'Right', 'RIGHT', 'Shift', 'SHIFT', 'Ctrl', 'CTRL', 'Esc', 'ESC', 'Alt', 'ALT', 'Space', 'SPACE', 'Enter', 'ENTER','Spacebar', 'SPACEBAR', 'Tab', 'TAB', 'Home', 'HOME', 'End', 'END', 'Plus', 'PLUS', 'Minus', 'MINUS', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Up arrow', 'Down arrow', 'Left arrow', 'Right arrow')
	MoveThrowKey.grid(row=7,column=2)
	MoveThrowKey.set('None')
	MoveThrowUpdateButton = ttk.Button(appMarg1, text="Update", command=SaveMoveThrowKey)
	MoveThrowUpdateButton.grid(row=7,column=3)

	# Pickup
	# Save Move Pickup Key
	def SaveMovePickupKey():
		keybindData["Pickup"] = MovePickupTxt.get();
		with open (os.getcwd() + '/collections/keybinds.json', 'w+') as f:
			json.dump(keybindData, f, indent=4, sort_keys=False)
		sys.exit(1)
	# End
	MovePickupLabel = tk.Label(appMarg1, text="Pickup:")
	MovePickupLabel.grid(row=8,column=1)
	MovePickupTxt = StringVar(None)
	MovePickupKey =ttk.Combobox(appMarg1, width=15, textvariable=MovePickupTxt, state='readonly')
	MovePickupKey['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Down', 'DOWN', 'Up', 'UP', 'Left', 'LEFT', 'Right', 'RIGHT', 'Shift', 'SHIFT', 'Ctrl', 'CTRL', 'Esc', 'ESC', 'Alt', 'ALT', 'Space', 'SPACE', 'Enter', 'ENTER','Spacebar', 'SPACEBAR', 'Tab', 'TAB', 'Home', 'HOME', 'End', 'END', 'Plus', 'PLUS', 'Minus', 'MINUS', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Up arrow', 'Down arrow', 'Left arrow', 'Right arrow')
	MovePickupKey.grid(row=8,column=2)
	MovePickupKey.set('None')
	MovePickupUpdateButton = ttk.Button(appMarg1, text="Update", command=SaveMovePickupKey)
	MovePickupUpdateButton.grid(row=8,column=3)

	# Quick Attack
	# Save Quick Attack Key
	def SaveMoveQuickAttackKey():
		keybindData["Quick Attack"] = MoveQuickAttackTxt.get();
		with open (os.getcwd() + '/collections/keybinds.json', 'w+') as f:
			json.dump(keybindData, f, indent=4, sort_keys=False)
		sys.exit(1)
	# End
	MoveQuickAttackLabel = tk.Label(appMarg1, text="Quick Attack:")
	MoveQuickAttackLabel.grid(row=9,column=1)
	MoveQuickAttackTxt = StringVar(None)
	MoveQuickAttackKey =ttk.Combobox(appMarg1, width=15, textvariable=MoveQuickAttackTxt, state='readonly')
	MoveQuickAttackKey['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Down', 'DOWN', 'Up', 'UP', 'Left', 'LEFT', 'Right', 'RIGHT', 'Shift', 'SHIFT', 'Ctrl', 'CTRL', 'Esc', 'ESC', 'Alt', 'ALT', 'Space', 'SPACE', 'Enter', 'ENTER','Spacebar', 'SPACEBAR', 'Tab', 'TAB', 'Home', 'HOME', 'End', 'END', 'Plus', 'PLUS', 'Minus', 'MINUS', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Up arrow', 'Down arrow', 'Left arrow', 'Right arrow')
	MoveQuickAttackKey.grid(row=9,column=2)
	MoveQuickAttackKey.set('None')
	MoveQuickAttackUpdateButton = ttk.Button(appMarg1, text="Update", command=SaveMoveQuickAttackKey)
	MoveQuickAttackUpdateButton.grid(row=9,column=3)

	# Heavy Attack
	# Save Heavy Attack Key
	def SaveMoveHeavyAttackKey():
		keybindData["Heavy Attack"] = MoveHeavyAttackTxt.get();
		with open (os.getcwd() + '/collections/keybinds.json', 'w+') as f:
			json.dump(keybindData, f, indent=4, sort_keys=False)
		sys.exit(1)
	# End
	MoveHeavyAttackLabel = tk.Label(appMarg1, text="Heavy Attack:")
	MoveHeavyAttackLabel.grid(row=10,column=1)
	MoveHeavyAttackTxt = StringVar(None)
	MoveHeavyAttackKey =ttk.Combobox(appMarg1, width=15, textvariable=MoveHeavyAttackTxt, state='readonly')
	MoveHeavyAttackKey['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Down', 'DOWN', 'Up', 'UP', 'Left', 'LEFT', 'Right', 'RIGHT', 'Shift', 'SHIFT', 'Ctrl', 'CTRL', 'Esc', 'ESC', 'Alt', 'ALT', 'Space', 'SPACE', 'Enter', 'ENTER','Spacebar', 'SPACEBAR', 'Tab', 'TAB', 'Home', 'HOME', 'End', 'END', 'Plus', 'PLUS', 'Minus', 'MINUS', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Up arrow', 'Down arrow', 'Left arrow', 'Right arrow')
	MoveHeavyAttackKey.grid(row=10,column=2)
	MoveHeavyAttackKey.set('None')
	MoveHeavyAttackUpdateButton = ttk.Button(appMarg1, text="Update", command=SaveMoveHeavyAttackKey)
	MoveHeavyAttackUpdateButton.grid(row=10,column=3)