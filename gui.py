from Tkinter import *
import Tkinter
import os
import subprocess
import tkMessageBox
from PIL import Image, ImageTk

bgcolor = "#2143a2"
root = Tk()

# animated gif logo 
class logo(Label):
	def __init__(self, master, filename, background):
		anim = Image.open(filename)
		gif = []
		self.frames = []
		self.index = 0
		self.delay = anim.info['duration']

		#append until at end
		try:
			while True:
				gif.append(anim.copy())
				anim.seek(anim.tell() + 1)
		except EOFError:
			pass

		#convert and adds all frames
		self.first = gif[0].convert('RGBA')
		self.frames.append(ImageTk.PhotoImage(self.first))

		Label.__init__(self, master, image = self.frames[0], background = bgcolor)
		next = gif[0]
		for image in gif:
			next.paste(image)
			self.frame = next.convert('RGBA')
			self.frames.append(ImageTk.PhotoImage(self.frame))

		#loops through and reconfigures GUI with a new gif frame
		loop = self.after(self.delay, self.play)

	def play(self):
		self.config(image = self.frames[self.index])
		self.index += 1
		if self.index == len(self.frames):
			self.index = 0
		loop = self.after(self.delay, self.play)

# tries to run emulate.sh, else prints out error message
def emulationScript():
	try:
		# run if the file exists
		if(os.path.exists('emulate.sh')):
			subprocess.call(['sh', 'emulate.sh'])
			root.destroy()
		# error show if not found or in directory
		else:
			tkMessageBox.showinfo("huh this ain't an emulator", "Error: Shell Script not found in directory!")
	#error with the subprocess call
	except:
		tkMessageBox.showinfo("huh this ain't an emulator", "Error: subprocess call unrecognized")

# exits the app to Raspbian
def exitApp():
	root.destroy()

# runs app
def main():
	#size, color, title
	root.geometry("268x201")
	root.configure(background = bgcolor)
	root.wm_title("Pi in my Gameboy")
	
	#logo animation
	anim = logo(root, "Rasp_turn_around.gif", background = bgcolor)
	anim.pack()

	#window frame to add buttons
	frame = Frame(root, background = bgcolor)
	frame.pack()

	#buttons
	retro = Button(frame, text="Run RetroPie", highlightbackground = bgcolor, command = emulationScript)
	retro.pack()
	exit = Button(frame, text="Exit to Raspbian", highlightbackground = bgcolor, command = exitApp)
	exit.pack()

	#GUI loop
	root.mainloop()

if __name__ == "__main__":
	main()