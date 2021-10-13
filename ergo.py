# Main
import tkinter as tk
from tkinter import Label, Text, Entry, StringVar, ttk, filedialog, PhotoImage, Canvas, FLAT, GROOVE, END
from PIL import Image, ImageTk, ImageSequence
# Path, Json
import json
import os
import sys
# Load Modules
from modules import settings, custom, developer, about, cmacro
from weapons import sword, hammer, blaster, lance, spear, katars, axe, bow, gauntlet, scythe, cannon, orb, greatsword

# Json 1
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
	None
# End

# Json 2
try:
	if os.path.exists(os.getcwd() + '/collections/application.json'):
		with open("./collections/application.json") as f:
			applicationData = json.load(f);
	AvatarLocation = applicationData["AvatarLocation"];
	AnimationSpeed = applicationData["AnimationSpeed"];
	UserDisplyName = applicationData["Username"]
except Exception:
	None
# End

# Provide relative path to packed file
def resource_path(relative_path):
	try:
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)
# End

def RunApplication():
	# AvatarImg
	def AvatarProfile(app):
		canvas = tk.Canvas(app, width=110, height=110, bd=0, highlightthickness=2, relief=FLAT, bg="#424549")
		canvas.place(x=35, y=25)
		sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(rf'{resource_path(AvatarLocation)}'))]
		images = canvas.create_image(55, 55, image=sequence[0])
		def animate(counter):
			canvas.itemconfig(images, image=sequence[counter])
			app.after(AnimationSpeed, lambda: animate((counter+1) % len(sequence)))
		animate(0)
	# End

	# Window
	def disableResize():
		app.resizable(False, False)
	def rgbColor(rgb):
		return "#%02x%02x%02x" % rgb

	app = tk.Tk()
	app.title("Ergo B")
	app.iconbitmap(resource_path('icon/ergo.ico'))
	app.configure(bg=rgbColor((30,33,36))) 
	app.after(100, disableResize)
	app.geometry("1050x620+150+50")

	# App Margin and Grid for all widgets
	AppMargin = tk.LabelFrame(app, text=f"[ {UserDisplyName} ]", bg="#7289da")
	AppMargin.grid(row=0, column=0)
	AppMargin.configure(fg="#ffffff", font=("Courier", 10))

	# Main widget
	PanelTab = tk.LabelFrame(AppMargin, padx=0, pady=0, bd=0)
	PanelTab.grid(row=1, column=1)

	# Profile Panel
	SideLeftProfileLabel = tk.Frame(PanelTab, width="185", height="295", bg="#7289da")
	SideLeftProfileLabel.config(highlightbackground="#7289da", bd=0, highlightthickness=1)
	SideLeftProfileLabel.grid(row=1, column=1)

	# Avatar Profile
	AvatarProfile(app)
	OpenMacroSetting = ttk.Button(app, text="Settings", command=lambda:settings.Open(AppMargin))
	OpenMacroSetting.place(x=55, y=140)

	# Textbox
	TextboxOutput = Text(app, height=5, width=22, wrap=tk.WORD)
	TextboxOutput.place(x=4, y=227)

	# Custom Macro Button
	CMButton = ttk.Button(app, text="Custom", command=lambda:custom.Open(CMButton,TextboxOutput))
	CMButton.place(x=55, y=170)
	
	# All Macro
	LoadOldMacroButton = ttk.Button(app, text="All", command=lambda:cmacro.Open(LoadOldMacroButton, TextboxOutput))
	LoadOldMacroButton.place(x=55, y=200)

	# ================================================================ #
	# Weapon Button
	SideLeftWeaponButtons = tk.LabelFrame(PanelTab, padx=1, pady=1, bg="#7289da")
	SideLeftWeaponButtons.grid(row=2, column=1)

	# Weapon Sword
	SwordPrev = PhotoImage(file=resource_path("images/Sword_Icon.png"))
	WeapSword = tk.Button(SideLeftWeaponButtons, image=SwordPrev, compound="center", command=lambda:sword.play(PanelTab, WeapSword, TextboxOutput), relief=GROOVE) #, text="Sword")
	WeapSword.grid(row=1,column=1)
	# End

	# Weapon Hammer
	HammPrev = PhotoImage(file=resource_path("images/Hammer_Icon.png"))
	WeapHamm = tk.Button(SideLeftWeaponButtons, image=HammPrev, compound="center", command=lambda:hammer.play(PanelTab, WeapHamm, TextboxOutput), relief=GROOVE) #, text="Hammer")
	WeapHamm.grid(row=1, column=2)
	# End

	# Weapon Blaster
	BlstPrev = PhotoImage(file=resource_path("images/Blasters_Icon.png"))
	WeapBlst = tk.Button(SideLeftWeaponButtons, image=BlstPrev, compound="center", command=lambda:blaster.play(PanelTab, WeapBlst, TextboxOutput), relief=GROOVE) #, text="Blaster")
	WeapBlst.grid(row=1, column=3)
	# End

	# Weapon Lance
	LancPrev = PhotoImage(file=resource_path("images/Lance_Icon.png"))
	WeapLanc = tk.Button(SideLeftWeaponButtons, image=LancPrev, compound="center", command=lambda:lance.play(PanelTab, WeapLanc, TextboxOutput), relief=GROOVE) #, text="Lance")
	WeapLanc.grid(row=2, column=1)
	# End

	# Weapon Spear
	SperPrev = PhotoImage(file=resource_path("images/Spear_Icon.png"))
	WeapSper = tk.Button(SideLeftWeaponButtons, image=SperPrev, compound="center", command=lambda:spear.play(PanelTab, WeapSper, TextboxOutput), relief=GROOVE) #, text="Spear")
	WeapSper.grid(row=2, column=2)
	# End

	# Weapon Katars
	KatrPrev = PhotoImage(file=resource_path("images/Katars_Icon.png"))
	WeapKatr = tk.Button(SideLeftWeaponButtons, image=KatrPrev, compound="center", command=lambda:katars.play(PanelTab, WeapKatr, TextboxOutput), relief=GROOVE) #, text="Katars")
	WeapKatr.grid(row=2, column=3)
	# End

	# Weapon Axe
	AxesPrev = PhotoImage(file=resource_path("images/Axe_Icon.png"))
	WeapAxes = tk.Button(SideLeftWeaponButtons, image=AxesPrev, compound="center", command=lambda:axe.play(PanelTab, WeapAxes, TextboxOutput), relief=GROOVE) #, text="Axe")
	WeapAxes.grid(row=3, column=1)
	# End

	# Weapon Bow
	BowsPrev = PhotoImage(file=resource_path("images/Bow_Icon.png"))
	WeapBows = tk.Button(SideLeftWeaponButtons, image=BowsPrev, compound="center", command=lambda:bow.play(PanelTab, WeapBows, TextboxOutput), relief=GROOVE) #, text="Bow")
	WeapBows.grid(row=3, column=2)
	# End

	# Weapon Gauntlet
	GnltPrev = PhotoImage(file=resource_path("images/Gauntlets_Icon.png"))
	WeapGnlt = tk.Button(SideLeftWeaponButtons, image=GnltPrev, compound="center", command=lambda:gauntlet.play(PanelTab, WeapGnlt, TextboxOutput), relief=GROOVE) #, text="Gauntlet")
	WeapGnlt.grid(row=3, column=3)
	# End

	# Weapon Scythe
	ScytPrev = PhotoImage(file=resource_path("images/Scythe_Icon.png"))
	WeapScyt = tk.Button(SideLeftWeaponButtons, image=ScytPrev, compound="center", command=lambda:scythe.play(PanelTab, WeapScyt, TextboxOutput), relief=GROOVE) #, text="Scythe")
	WeapScyt.grid(row=4, column=1)
	# End

	# Weapon Cannon
	CannPrev = PhotoImage(file=resource_path("images/Cannon_Icon.png"))
	WeapCann = tk.Button(SideLeftWeaponButtons, image=CannPrev, compound="center", command=lambda:cannon.play(PanelTab, WeapCann, TextboxOutput), relief=GROOVE) #, text="Cannon")
	WeapCann.grid(row=4, column=2)
	# End

	# Weapon Orb
	OrbsPrev = PhotoImage(file=resource_path("images/Orb_Icon.png"))
	WeapOrbs = tk.Button(SideLeftWeaponButtons, image=OrbsPrev, compound="center", command=lambda:orb.play(PanelTab, WeapOrbs, TextboxOutput), relief=GROOVE) #, text="Orb")
	WeapOrbs.grid(row=4, column=3)
	# End

	# Weapon Greatsword
	GrsdPrev = PhotoImage(file=resource_path("images/Greatsword_Icon.png"))
	WeapGrsd = tk.Button(SideLeftWeaponButtons, image=GrsdPrev, compound="center", command=lambda:greatsword.play(PanelTab, WeapGrsd, TextboxOutput), relief=GROOVE) #, text="Greatsword")
	WeapGrsd.grid(row=5, column=2)
	# End

	# Deloper Panel Tab
	DeveloperPanel = tk.LabelFrame(app, text="[ BrawlMacro : 2nd Build ]", bg="#7289da", fg="#ffffff", highlightthickness=0)
	DeveloperPanel.place(x=805, y=0, height=620, width=245)
	DeveloperPanel.configure(fg="#ffffff", font=("Courier", 10))
	# End

	# Developer Button
	Avnecode = PhotoImage(file=resource_path("images/Necode.png"))
	Avnecbtn = tk.Button(SideLeftWeaponButtons, image=Avnecode, compound="center", command=lambda:developer.open(app, Avnecbtn), relief=GROOVE) #, text="Necode")
	Avnecbtn.grid(row=5, column=1)
	# End

	# Info
	InfoPrev = PhotoImage(file=resource_path("images/Info.png"))
	InfoBttn = tk.Button(SideLeftWeaponButtons, image=InfoPrev, compound="center", command=lambda:about.open(DeveloperPanel, InfoBttn), relief=GROOVE) #, text="Necode")
	InfoBttn.grid(row=5, column=3)
	InfoBttn["state"] = "disabled"
	about.open(DeveloperPanel, InfoBttn)

	# End

	# Send Report 
	def SendReport():
		ReportButton["state"] = "disabled"
	ReportButton = ttk.Button(DeveloperPanel, text="Send Report", command=SendReport, width=38)
	ReportButton.place(x=2, y=525)

	# Edit Macro
	EditButton = ttk.Button(DeveloperPanel, text="Edit", command="", width=38)
	EditButton.place(x=2, y=550)
	EditButton["state"] = "disabled"

	# # Exit Button
	ExitButton = ttk.Button(DeveloperPanel, text="Exit", command=lambda:app.destroy(), width=38)
	ExitButton.place(x=2, y=575)
	# End
	# ================================================================ #
	try:
		app.mainloop()
	except KeyboardInterrupt:
		sys.exit(1)


# Awesome Entry
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


dirName = "collections"
if not os.path.exists(dirName):
	print("Collection not exist")
	app = tk.Tk()
	app.title(" ")
	app.geometry("250x170+250+250")
	app.configure(bg="#2C2F33")
	app.iconbitmap(resource_path('ergo.ico'))
	def disableResize():
		app.resizable(False, False)
	app.after(100, disableResize)
	def RegisterUsername():
		os.makedirs(dirName)
		print("Directory " , dirName ,  " Created ")
		# # if json file not exist, create new one with this template
		configTemplate = { 
			"Move Up": "None",
			"Move Down": "None",
			"Move Left": "None",
			"Move Right": "None",
			"Jump": "None",
			"Dodge": "None",
			"Throw": "None",
			"Pickup": "None",
			"Quick Attack": "None",
			"Heavy Attack": "None"
		}
		# write the template
		with open (os.getcwd() + '/collections/keybinds.json', 'w+') as f:
			json.dump(configTemplate, f, indent=4, sort_keys=False)
		######################## End #######################
		defConfig = {
			"Dev": "Necode",
			"YTs": "https://www.youtube.com/channel/UCn_48Cl9BjKKjvS3ADk1Ltw",
			"AvatarLocation": "images/ergo.png",
			"AnimationSpeed": 30,
			"Username": UsernameTxt.get()
		}
		with open (os.getcwd() + '/collections/application.json', 'w+') as f:
			json.dump(defConfig, f, indent=4, sort_keys=False)
		######################## End #######################
		app.destroy()
		sys.exit(0)

	# Frame
	AppFrame = tk.LabelFrame(app, text="[ First Time Setup ]", fg="#056cfc")
	AppFrame.place(x=0, y=0)
	# Label
	LabelName = Label(AppFrame, text="Username: ", height=8)
	LabelName.grid(row=1, column=1)
	# Entry
	UsernameTxt = StringVar(None)
	EntryBox = EntryWithPlaceholder(AppFrame, placeholder="Bodvar", text=UsernameTxt, width=17, relief=FLAT)
	EntryBox.grid(row=1, column=2)
	# Button
	EnterButton = ttk.Button(AppFrame, text="OK", command=RegisterUsername)
	EnterButton.grid(row=1, column=3)
	# Label Description
	LabelDesc = Label(app, text="[ Program will exit after entering username ]", fg="#056cfc")
	LabelDesc.pack(side="bottom", fill="both")
	# Exit
	ExitButton = ttk.Button(app, text="Exit", command=lambda:app.destroy())
	ExitButton.pack(side="bottom", fill="both")
	# Window
	try:
		app.mainloop()
	except KeyboardInterrupt:
		sys.exit(1)
		
else:
	import requests
	def Login():
		url = ""
		data = {
			"content" : f"**{UserDisplyName}** Logged-in to **Ergo B** <:emojiName:emojiID>" ,
			# "username" : "Ergo B"
		}
		result = requests.post(url, json=data)
		try:
			result.raise_for_status()
		except requests.exceptions.HTTPError as err:
			print(err)
		else:
			print("Successfully login, code {}.".format(result.status_code))
	# Login()
	
	try:
		app = RunApplication
		app()
	except KeyboardInterrupt:
		sys.exit(1)