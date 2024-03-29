'''
Q. What are Widgets in TKinter?
Ans. 
Tkinter is Python’s standard GUI (Graphical User Interface) package. tkinter provides us with a variety of common GUI 
elements which we can use to build out interface – such as buttons, menus and various kind of entry fields and display
 areas. We call these elements Widgets.

'''

from tkinter import *


root = Tk()
root.minsize(400,240)


title = StringVar()
title.set("Hello CMPundhir")

lTitle = Label(root, textvariable = title)
lTitle.pack()

btn = Button(root, 
	text = "CLick Me", 
	width = 25, 
	height = 5, 
	command = lambda : print("Hi"))
btn.place(x=100, 
	y = 100)

root.mainloop()


'''
Widgets	Description
Label		: It is used to display text or image on the screen
Button		: It is used to add buttons to your application
Canvas		: It is used to draw pictures and others layouts like texts, graphics etc.
ComboBox	: It contains a down arrow to select from list of available options
CheckButton	: It displays a number of options to the user as toggle buttons from which user can select any number of options.
RadiButton	: It is used to implement one-of-many selection as it allows only one option to be selected
Entry		: It is used to input single line text entry from user
Frame		: It is used as container to hold and organize the widgets
Message		: It works same as that of label and refers to multi-line and non-editable text
Scale		: It is used to provide a graphical slider which allows to select any value from that scale
Scrollbar	: It is used to scroll down the contents. It provides a slide controller.
SpinBox		: It is allows user to select from given set of values
Text		: It allows user to edit multiline text and format the way it has to be displayed
Menu		: It is used to create all kinds of menu used by an application
'''