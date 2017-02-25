from Tkinter import *
import Tkinter
import subprocess
import tkMessageBox
import time

startClock = time.time()
bgcolor = "#2143a2"
root = Tk()

# tries to run emulate.sh, else prints out error message
def emulationScript():
	try:
		# subprocess.call(['sh emulate.sh'])
		subprocess.call(['sh', 'emulate.sh'])
	except:
		# print("huh this ain't an emulator")
		tkMessageBox.showinfo("huh this ain't an emulator", "Error: Shell Script ran into an error and couldn't run")
	looper = False

# exits 
def exitApp():
	root.destroy()
	looper = False

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
	retro.pack() #padx = 67, pady = 50
	exit = Button(frame, text="exit", highlightbackground = bgcolor, command = exitApp)
	exit.pack()

	root.mainloop()

	# rasp = PhotoImage(file = "Rasp_turn_around.gif", format = "gif -index 2")


if __name__ == "__main__":
	main()


# count = 1
# gifFormat = "gif -index " + str(count)
# label.configure(image = rasp.configure(format = gifFormat))
# count += 1

# count = 1

# while(True):
# 	gifFormat = "gif -index " + str(count)
# 	label.configure(image = rasp.configure(format = gifFormat))
# 	count += 1
# 	if(count <= 81):
# 		count = 1

# def main():
# 	root.geometry("268x201")
# 	root.configure(background = bgcolor)
# 	iFrame = Frame(root, background = bgcolor)
# 	iFrame.pack()
# 	canvas = Canvas(iFrame, background = bgcolor, highlightbackground = bgcolor)
# 	rasp = PhotoImage(file = "Rasp_turn_around.gif")
# 	image = canvas.create_image(190, -5, anchor=NE, image=rasp)
# 	canvas.pack()

# 	bFrame = Frame(root, background = bgcolor)
# 	retro = Button(bFrame, text="Run RetroPie?", highlightbackground = bgcolor, command = emulationScript)
# 	retro.pack() #padx = 67, pady = 50
# 	exit = Button(bFrame, text="exit", highlightbackground = bgcolor, command = exitApp)
# 	exit.pack()
# 	root.mainloop()