from Tkinter import *
import Tkinter
import subprocess
import tkMessageBox

bgcolor = "#2143a2"
root = Tk()

# tries to run emulate.sh, else prints out error message
def emulationScript():
	try:
		subprocess.call(['sh', 'emulate.sh'])
	except:
		tkMessageBox.showinfo("huh this ain't an emulator", "Error: Shell Script ran into an error and couldn't run")

# exits the app to Raspbian
def exitApp():
	root.destroy()

# runs app
def main():
	root.geometry("268x201")
	root.configure(background = bgcolor)
	
	rasp = PhotoImage(file = "Rasp_turn_around.gif")
	rasp2 = PhotoImage(file = "Rasp_turn_around.gif", format = "gif -index 20")
	label = Label(background = bgcolor, image = rasp)
	label.pack()

	frame = Frame(root, background = bgcolor)
	frame.pack()

	retro = Button(frame, text="Run RetroPie?", highlightbackground = bgcolor, command = emulationScript)
	retro.pack()
	exit = Button(frame, text="exit", highlightbackground = bgcolor, command = exitApp)
	exit.pack()

	root.mainloop()

if __name__ == "__main__":
	main()