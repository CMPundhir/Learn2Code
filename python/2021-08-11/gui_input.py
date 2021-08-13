'''
Entry Widget: 

'''

from tkinter import *


root = Tk()

# create varibale for checkbuttons
fname = StringVar()
lname = StringVar()

def sayHello():
	print("Hello",fname.get(), lname.get())

# set window size
root.minsize(width=400, height=200)

# set title of window
root.title('CMPundhir GUI Input Demo')

# create an entry
eFname = Entry(root, textvariable = fname)

# add entry in view
eFname.pack()

# create another entry
eLname = Entry(root, textvariable = lname)

# add eLname entry in view
eLname.pack()

# create a button
clickBtn = Button(root, text='CLick Me', width=25, command=sayHello)

# add button in view
clickBtn.pack()

# draw/open main windows
root.mainloop()
