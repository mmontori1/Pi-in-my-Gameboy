from Tkinter import *
import Tkinter
import subprocess

bgcolor = "#2143a2"

# to do: have a shell script to run which this python function will call and run on terminal
def emulationScript():
	print("huh this ain't an emulator")
	subprocess.Popen(['ls', '-l'])

def main():
	root = Tk()
	root.geometry("268x201")
	root.configure(background = bgcolor)
	frame = Frame(root, background = bgcolor)
	frame.pack()
	retro = Button(frame, text="Run RetroPie?", highlightbackground = bgcolor, command = emulationScript)
	retro.pack(padx = 67, pady = 50)
	exit = Button(frame, text="exit", highlightbackground = bgcolor)
	exit.pack()
	root.mainloop()

if __name__ == "__main__":
	main()