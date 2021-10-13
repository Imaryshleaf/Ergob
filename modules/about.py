import tkinter as tk
from tkinter import Button, Frame, Entry, Label, ttk, StringVar, PhotoImage, LabelFrame
import os
import sys
from inputs import keyinputs
import keyboard
from time import sleep

WidgetName = "[ Developer Tab ]"

def open(root, ButtonState):
	ButtonState["state"] = 'disabled' # Disable button

	appMargin = LabelFrame(root, text="Information")
	appMargin.place(x=1, y=2)

	quote = """1. Software witten in Python Language and compiled in Windows 8.1 with 64 bit-os using Pyinstaller.
	\n2. Software unable to run very well in windows 10 and not supported for 32 bit-os.
	\n3. Software can't read, write and modify your game memory and can't automated play like bot.
	\n4. Software can't give you 100% guarantee to hit the opponent perfectly (True Combo).
	\n5. Please use this software at your own risk. We are not responsible in any situation that cause your account terminated or banned.
	\n6. Software not supported controller, please pardon us not making this software compatible with any controller.
	\n7. If sotware doesn't work at all, please delete this software from your pc. For the best option available is by downloading other free macro from other websites.
	"""
	# Well, I think they want to abuse the software
	# \n8. Software will use your internet connection once everytime at the start of program to send login username to our server.

	texbox = tk.Text(appMargin, width=29, height=30, wrap=tk.WORD)
	texbox.grid(row=1, column=1)
	texbox.insert("end", quote)
	texbox.configure(state="disabled")

	def onClose():
		ButtonState["state"] = 'normal'
		appMargin.place_forget()

	CloseButton = ttk.Button(appMargin, text="Close", command=onClose)
	CloseButton.grid(row=2, column=1)