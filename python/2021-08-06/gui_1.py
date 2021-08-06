from tkinter import *


root = Tk()

# create varibale for checkbuttons
m = IntVar()
f = IntVar()

def sayHello():
	print("Hello Everyone ,",m.get(),f.get())

# set window size
root.minsize(width=400, height=200)

# set title of window
root.title('CMPundhir GUI Demo')

# create a button
clickBtn = Button(root, text='CLick Me', width=25, command=sayHello)

# add button in view
clickBtn.pack()

# create a check button
mCkBtn = Checkbutton(root, text='Male', variable=m)
# add button in view
mCkBtn.pack()

# create a check button
fCkBtn = Checkbutton(root, text='Female', variable=f)
# add button in view
fCkBtn.pack()

# draw/open main windows
root.mainloop()





'''
Tkinter supports some variables which are used to manipulate the values of Tkinter widgets. These variables work like normal variables.
set() and get() methods are used to set and retrieve the values of these variables.
The values of these variables can be set using set() method or by using constructor of these variables.

There are 4 tkinter variables.

BooleanVar()
StringVar()
IntVar()
DoubleVar()
'''