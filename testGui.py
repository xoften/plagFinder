#import tkinter as tk
#from tkinter import filedialog

#root = tk.Tk()
#root.withdraw()

#file_path = filedialog.askopenfilename()

from tkinter import *

root = Tk()
root.geometry("500x200+30+30")
root.title("Plag Finder")

chooseFileLabel = Message(root, width=500,
                          text="Choose the zipped submission archive downloaded from moodle:"
                          ).grid(row=1)

runButton = Button(root, text="Run")
chooseFileButton = Button(root, text="Browse Files")

root.mainloop()