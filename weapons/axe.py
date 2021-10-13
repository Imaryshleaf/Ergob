import tkinter as tk
from tkinter import Button, Frame, Entry, Label, ttk, StringVar, PhotoImage, LabelFrame, END
import os
import sys
from inputs import keyinputs 
import keyboard
from time import sleep

MacroName = "Axe"
TotalComboMacro = 3

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
			self.appMarg.grid(row=1, column=2)

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
					keyinputs.SLight(output)
					sleep(0.47)
					keyinputs.Jump(output)
					keyinputs.SAir(output)
			keyboard.on_press(ComboMacro1)

			def ComboMacro2(event):
				TriggerKey = self.entryDB[1][0]
				if event.name == TriggerKey.get():
					keyinputs.SLight(output)
					sleep(0.47)
					keyinputs.Jump(output)
					keyinputs.NAir(output)
			keyboard.on_press(ComboMacro2)

			def ComboMacro3(event):
				TriggerKey = self.entryDB[2][0]
				if event.name == TriggerKey.get():
					keyinputs.NLight(output)
					sleep(0.8)
					keyinputs.DodgeForward(output)
					keyinputs.SLight(output)
					sleep(0.47)
					keyinputs.Jump(output)
					keyinputs.SAir(output)
			keyboard.on_press(ComboMacro3)

	App(root)