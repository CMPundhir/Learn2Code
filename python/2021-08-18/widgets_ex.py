from tkinter import *
from tkinter.ttk import * 
import time

root = Tk()
root.minsize(500, 500)

Label(root, text = "Widgets Demo", font = "60").place(x = 200, y = 40)

# Message widget
Message(root, text = "I am a Message widget. Welcome to tkinter world", width= 400).place(x = 20, y = 60)

# Menu widget
menubar = Menu(root)

# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)
  
# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Tk Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About Tk', command = None)

# display Menu
root.config(menu = menubar)



# Progress bar widget
progress = Progressbar(root, orient = HORIZONTAL,
              length = 100, mode = 'determinate')
progress.place(x = 20, y = 100)

counter = 20

def bar():
    global counter
    progress['value'] = counter
    root.update_idletasks()
    time.sleep(1)
    if counter == 100:
        counter = 0
    else:
        counter = counter + 20
Button(root, text = 'Start Progress', command = bar).place(x = 20, y = 120)


# scrollbar
scroll_bar = Scrollbar(root)
  
scroll_bar.place(x = 200, y = 150)


# listbox
listBox = Listbox(root, yscrollcommand = scroll_bar.set )
listBox.place(x = 20, y = 150)

for line in range(1, 26):
    listBox.insert(END, "Geeks " + str(line))

root.mainloop()