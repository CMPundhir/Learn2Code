from tkinter import *
from tkinter.ttk import *


root = Tk()
root.minsize(600, 400)
root.title("Gurukul")

userNameVar = StringVar()
passwordVar = StringVar()


def performLogin(topLevel):
	username = userNameVar.get()
	password = passwordVar.get()
	print("Username: ",username, ", Password: ",password)
	topLevel.destroy()

def openLoginWindow():
	topLevel = Toplevel(root)
	topLevel.minsize(400, 300)
	Label(topLevel, text= "Please Login").pack(padx=0, pady=20)
	mainFrame = Frame(topLevel)
	mainFrame.pack()
	Label(mainFrame, text= "Username").grid(row=1, column=0, padx=10, pady=10)
	Label(mainFrame, text= "Password").grid(row=2, column=0, padx=10, pady=10)
	Entry(mainFrame, textvariable= userNameVar).grid(row=1, column=1)
	Entry(mainFrame, textvariable= passwordVar, show="*").grid(row=2, column=1)
	Button(mainFrame, text= "Login", command= lambda: performLogin(topLevel)).grid(row=3, column=1, padx=10, pady=10)


def openRegWindow():
	pass

Label(root, text= "Welcome to Gurukul").pack(padx=0, pady=20)
Label(root, text="Choose Action").pack(padx=10, pady=10)
topFrame = Frame(root)
topFrame.pack(pady=20)
Button(topFrame, text= "Login", command= openLoginWindow).grid(row=1, column=1, padx=10, pady=10)
Button(topFrame, text= "Registration", command= openRegWindow).grid(row=1, column=2, padx=10, pady=10)


root.mainloop()
