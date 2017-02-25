from Tkinter import *
import tkMessageBox
import Tkinter

root = Tkinter.Tk()
# to do: have a shell script to run which this python function will call and run on terminal
def emulationScript():
	print("huh this ain't an emulator")

retro = Tkinter.Button(root, text="Run RetroPie?", command = emulationScript)
retro.pack()

root.mainloop()