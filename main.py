#!/usr/bin/python

import Tkinter as tk
import json
import logging

class Application(tk.Frame):
    def __init__(self, master):

        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        pad=3
        master.attributes("-fullscreen", True)

    def readJson(self):
        json_data=open('apps.json').read()
        self.apps = json.loads(json_data)

    def runApp(self, path):
        logging.warning(path)

    def createWidgets(self):
        self.readJson()

        for app in self.apps:
            button = tk.Button(self, text=app.get("name"), command=lambda:self.run(app.get("name")))
            button.grid()

        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

root=tk.Tk()
app = Application(root)
app.master.title('Sample Application')
app.mainloop()
