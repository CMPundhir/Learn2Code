from tkinter import *
from tkinter.ttk import *
'''
To add styling on the ttk.Button we cannot directly pass the value in the options. 
'''
root = Tk()

# This will create style object
style = Style()

# This will be adding style, and
# naming that style variable as
# b.Tbutton (TButton is used for ttk.Button).
style.configure(
	'b1.TButton', 
	font = ('calibri', 28, 'bold', 'underline'),
    foreground = 'red'
    )
style.configure(
	'b2.TButton', 
	font = ('calibri', 24, 'bold', ),
    foreground = 'blue'
    )

# Changes will be reflected
# by the movement of mouse.
style.map('b1.TButton', 
	foreground = [('active', 'green'), ('disabled', 'grey')],
    background = [('active', 'red')])
 

btn = Button(root, 
	text = "Click",
	style = "b1.TButton")

btn2 = Button(root, 
	text = "Click",
	style = "b2.TButton")

btn.pack()
btn2.pack()

root.mainloop()