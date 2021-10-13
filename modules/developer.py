import tkinter as tk
from tkinter import Button, Frame, Entry, Label, ttk, StringVar, PhotoImage, LabelFrame
from inputs import keyinputs
from time import sleep
import webbrowser

WidgetName = "[ Necode ]"

def open(root, ButtonState):
	ButtonState["state"] = 'disabled' # Disable button

	appMargin = LabelFrame(root, text=WidgetName, bd=3, relief="sunken", bg="#23272A")
	appMargin.place(x=188, y=0, height=620, width=618)
	appMargin.configure(fg="#ffffff", font=("Courier", 10))

	# Anime Server
	def Discord_Anime():
		print("Not available")
		# OpenBtn1['state'] = "disabled"
		# webbrowser.open_new("")
		# OpenBtn1['state'] = "enable"

	# Programmer Server
	def Discord_Programmer():
		DiscordButton['state'] = "disabled"
		webbrowser.open_new("https://discord.gg/URCNH7KW4Q")
		DiscordButton['state'] = "enable"

	# Youtube Channel
	def YouTube_Channel():
		YouTubeButton['state'] = "disabled"
		webbrowser.open_new("https://www.youtube.com/channel/UCn_48Cl9BjKKjvS3ADk1Ltw")
		YouTubeButton['state'] = "enable"

	# Hide Widget
	def onHide():
		ButtonState["state"] = "normal"
		appMargin.place_forget()

	YouTubeButton = ttk.Button(appMargin, text="YouTube", command=YouTube_Channel)
	YouTubeButton.pack(fill="both")
	
	DiscordButton = ttk.Button(appMargin, text="Discord", command=Discord_Programmer)
	DiscordButton.pack(fill="both")
	DiscordButton["state"] = "disabled"

	ContributeButton = ttk.Button(appMargin, text="Contribute", command="")
	ContributeButton.pack(fill="both")
	ContributeButton["state"] = "disabled"

	HideButton = ttk.Button(appMargin, text="Hide", command=onHide)
	HideButton.pack(fill="both")