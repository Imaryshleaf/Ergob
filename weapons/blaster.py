import tkinter as tk
from tkinter import Button, Frame, Entry, Label, ttk, StringVar, PhotoImage, LabelFrame, END
import os
import sys
from inputs import keyinputs
import keyboard
from time import sleep

MacroName = "Blaster"
TotalComboMacro = 7

def outputConsole(output, content):
	output.delete("1.0", END)
	output.insert("end", content)

def play(root, ButtonState, output):
	outputConsole(output, f"{MacroName} Macro Loaded: {TotalComboMacro} available\n")
	ButtonState["state"] = 'disabled' # Disable button

	class App:
		def __init__(self, root):
			self.frameDB = []
			self.entryDB = []
			self.count = 0
			self.root = root
			self.appMarg = tk.LabelFrame(self.root, text=MacroName)
			self.appMarg.grid(row=1, column=4)

			self.CloseMacro = ttk.Button(self.appMarg, text="Close", command=lambda counter=self.count: self.CloseWidget(counter=counter))
			self.CloseMacro.grid(row=99, column=3)
			self.root.after(0, lambda: self.SetdefaultKey(self.count))

			for i in range(9):
				LabelCounter = i+1
				self.frameDB.append(Frame(self.appMarg, borderwidth=0, relief="solid"))
				self.frameDB[self.count].grid(row=LabelCounter,column=3)
				# Count the widgets
				LabelNumber = Label(self.appMarg, text=f"{LabelCounter}")
				LabelNumber.grid(row=LabelCounter, column=2)
				# Trigger Key
				TriggerKey = StringVar(None)
				WeaponKeyCombox = ttk.Combobox(self.frameDB[self.count], width=15, textvariable=TriggerKey, state='readonly')
				WeaponKeyCombox['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Down', 'DOWN', 'Up', 'UP', 'Left', 'LEFT', 'Right', 'RIGHT', 'Shift', 'SHIFT', 'Ctrl', 'CTRL', 'Esc', 'ESC', 'Alt', 'ALT', 'Space', 'SPACE', 'Enter', 'ENTER','Spacebar', 'SPACEBAR', 'Tab', 'TAB', 'Home', 'HOME', 'End', 'END', 'Plus', 'PLUS', 'Minus', 'MINUS', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Up arrow key', 'Down arrow key', 'Left arrow key', 'Right arrow key')
				WeaponKeyCombox.set('None')
				WeaponKeyCombox.grid(row=LabelCounter,column=2)
				# Reset Button
				ResetButton = ttk.Button(self.frameDB[self.count], text="Clear", command=lambda counter=self.count: self.ResetTriggerKey(counter=counter))
				ResetButton.grid(row=LabelCounter,column=3)
				# Array data
				self.entryDB.append([WeaponKeyCombox])
				self.count += 1
		
		def SetdefaultKey(self, counter):
			self.MacroLoaded(counter)
			for i in range(9):
				EveryPickedKey = self.entryDB[i][0]
				EveryPickedKey.set("None")

		def CloseWidget(self, counter):
			for i in range(9):
				EveryPickedKey = self.entryDB[i][0]
				EveryPickedKey.set("None")
			self.frameDB.clear()
			self.entryDB.clear()
			self.appMarg.grid_forget()
			ButtonState["state"] = 'normal'

		def ResetTriggerKey(self, counter):
			TriggerKeyData = self.entryDB[counter][0]
			TriggerKeyData.set("None")

		def MacroLoaded(self, counter):
			# Start Making Combo from here
			def ComboMacro1(event):
				TriggerKey = self.entryDB[0][0]
				if event.name == TriggerKey.get():
					keyinputs.DLight(output)
					sleep(0.71)
					keyinputs.DashJump(output)
					keyinputs.DAir(output)
			keyboard.on_press(ComboMacro1)

			def ComboMacro2(event):
				TriggerKey = self.entryDB[1][0]
				if event.name == TriggerKey.get():
					keyinputs.DLight(output)
					sleep(0.71)
					keyinputs.DashJump(output)
					keyinputs.Recovery(output)
			keyboard.on_press(ComboMacro2)

			def ComboMacro3(event):
				TriggerKey = self.entryDB[2][0]
				if event.name == TriggerKey.get():
					keyinputs.UnknownBlasterHardCombo(output)
			keyboard.on_press(ComboMacro3)

			def ComboMacro4(event):
				TriggerKey = self.entryDB[3][0]
				if event.name == TriggerKey.get():
					keyinputs.UnknownGauntletBlasterHardCombo(output)
			keyboard.on_press(ComboMacro4)

			def ComboMacro5(event):
				TriggerKey = self.entryDB[4][0]
				if event.name == TriggerKey.get():
					keyinputs.Throw(output)
					sleep(0.45)
					keyinputs.DLight(output)
					sleep(0.43)
					keyinputs.Jump(output)
					keyinputs.Pickup(output)
					keyinputs.DAir(output)
			keyboard.on_press(ComboMacro5)

			def ComboMacro6(event):
				TriggerKey = self.entryDB[5][0]
				if event.name == TriggerKey.get():
					keyinputs.DLight(output)
					sleep(0.71)
					keyinputs.Jump(output)
					keyinputs.SAir(output)
			keyboard.on_press(ComboMacro6)

			def ComboMacro7(event):
				TriggerKey = self.entryDB[6][0]
				if event.name == TriggerKey.get():
					keyinputs.BlasterInstantGPRMP(output)
			keyboard.on_press(ComboMacro7)

			def ComboMacro8(event):
				TriggerKey = self.entryDB[7][0]
				if event.name == TriggerKey.get():
					keyinputs.BlasterInstantGPLMP(output)
			keyboard.on_press(ComboMacro8)

	App(root)