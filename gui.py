from Tkinter import *
import Tkinter

# to do: have a shell script to run which this python function will call and run on terminal
def emulationScript():
	print("huh this ain't an emulator")

def main():
	root = Tk()
	frame = Frame(root, width = 400, height = 400, background = "#2143a2")
	retro = Button(frame, text="Run RetroPie?", bg = "#2143a2", command = emulationScript)
	retro.pack(padx = 100, pady = 100)
	frame.pack()
	root.mainloop()

if __name__ == "__main__":
	main()