from tkinter import *


root = Tk()
root.minsize(400, 500)

Label(root, text="Welcome to CM's Calculator").pack()
Label(root, text="--------------------------").pack()

exp = StringVar()

def prt(s):
	exp.set(exp.get() + s)


Label(root, text="Result here", textvariable= exp, width=25, height=5, background="#fde").pack()
Label(root, text="").pack()
Label(root, text="").pack()
frame = Frame(root)

Button(frame, text="1", width=10, height=3, command= lambda : prt("1")).grid(row=1, column=0)
Button(frame, text="2", width=10, height=3, command= lambda : prt("2")).grid(row=1, column=1)
Button(frame, text="3", width=10, height=3, command= lambda : prt("3")).grid(row=1, column=2)
Button(frame, text="*", width=10, height=3, command= lambda : prt("*")).grid(row=1, column=3)

Button(frame, text="4", width=10, height=3, command= lambda : prt("4")).grid(row=2, column=0)
Button(frame, text="5", width=10, height=3, command= lambda : prt("5")).grid(row=2, column=1)
Button(frame, text="6", width=10, height=3, command= lambda : prt("6")).grid(row=2, column=2)
Button(frame, text="/", width=10, height=3, command= lambda : prt("/")).grid(row=2, column=3)

Button(frame, text="7", width=10, height=3, command= lambda : prt("7")).grid(row=3, column=0)
Button(frame, text="8", width=10, height=3, command= lambda : prt("8")).grid(row=3, column=1)
Button(frame, text="9", width=10, height=3, command= lambda : prt("9")).grid(row=3, column=2)
Button(frame, text="-", width=10, height=3, command= lambda : prt("-")).grid(row=3, column=3)

Button(frame, text=".", width=10, height=3, command= lambda : prt(".")).grid(row=4, column=0)
Button(frame, text="0", width=10, height=3, command= lambda : prt("0")).grid(row=4, column=1)
Button(frame, text="X", width=10, height=3, command= lambda : prt("x")).grid(row=4, column=2)
Button(frame, text="+", width=10, height=3, command= lambda : prt("+")).grid(row=4, column=3)

Button(frame, text="=", width=20, height=3, command= lambda : prt("=")).grid(row=5, column=2, columnspan=2)

frame.pack()
root.mainloop()
