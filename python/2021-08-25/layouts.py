from tkinter import *


root = Tk()
root.minsize(400, 500)

parentFrame = Frame(root)
parentFrame.pack()

frame0 = Frame(parentFrame, width = 200, height = 200, background="blue")
frame0.grid(row = 0, column = 0 )

frame01 = Frame(frame0, width = 100, height = 100, background="red")
frame01.grid(row = 0, column = 0 )

frame02 = Frame(frame0, width = 100, height = 100, background="pink")
frame02.grid(row = 0, column = 1 )

frame03 = Frame(frame0, width = 100, height = 100, background="grey")
frame03.grid(row = 1, column = 0 )

frame04 = Frame(frame0, width = 100, height = 100, background="black")
frame04.grid(row = 1, column = 1 )


frame1 = Frame(parentFrame, width = 200, height = 200, background="green")
frame1.grid(row = 0, column = 1 )

Button(frame1, text="Click Me", background="black").grid(row = 0, column = 0)
Button(frame1, text="Click Me", background="black").grid(row = 0, column = 1)
Button(frame1, text="Click Me", background="black").grid(row = 0, column = 2)
Button(frame1, text="Click Me", background="black").grid(row = 1, columnspan=3)



frame2 = Frame(parentFrame, width = 200, height = 200, background="red")
frame2.grid(row = 1, column = 0 )

frame3 = Frame(parentFrame, width = 200, height = 200, background="yellow")
frame3.grid(row = 1, column = 1 )


root.mainloop()
