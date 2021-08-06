import tkinter as tk
import time

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.counter = 0
        self.start = None
        self.now = None
        self.master = master
        master.minsize(640,420)
        master.maxsize(2560,1440)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.btn = tk.Button(self)
        self.btn.config(height = 10, width = 20)
        self.btn["text"] = "Click Me"
        self.btn["command"] = self.say_hi
        self.btn.pack(side="top")

        self.resetBtn = tk.Button(self)
        self.resetBtn.config(height = 10, width = 20)
        self.resetBtn["text"] = "Reset"
        self.resetBtn["command"] = self.reset
        self.resetBtn.pack(side="top")

        self.txt = tk.Label()
        self.txt["text"] = "Counter: "
        self.txt.pack(side="top")

    def say_hi(self):
        t = time.time()
        if self.start:
            self.now = t
            diff = int(self.now - self.start)
            if diff >0:
                print("Total clicks: ",self.counter)
                self.txt["text"] = f"Total clicks: {self.counter}"
                return
        else:
            self.start = t
            print(self.counter,". Start time: ", t)
        self.counter += 1

    def reset(self):
        self.counter = 0
        self.start = None
        self.now = None
        self.txt["text"] = "Total clicks Reset"

root = tk.Tk()
app = Application(master=root)
app.mainloop()