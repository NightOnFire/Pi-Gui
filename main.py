#!/usr/bin/python

import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):

        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        pad=3
        master.attributes("-fullscreen", True)

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

root=tk.Tk()
app = Application(root)
app.master.title('Sample Application')
app.mainloop()
