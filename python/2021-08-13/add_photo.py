from tkinter import *

root = Tk()

photo = PhotoImage(file = r"pranshu.png")

photo = photo.subsample(2,2)

btn = Button(root, 
	text = "CLick", 
	image = photo,)
btn.pack()

root.mainloop()