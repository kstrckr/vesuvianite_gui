import subprocess

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.title("AutoCrop")
root.columnconfigure(3)
root.resizable(False, False)

frm = ttk.Frame(root, padding=10)
frm.grid()


ttk.Label(frm, text="Auto Crop Configurator").grid(columnspan=2, row=0, pady=10)
selectedDirStr = StringVar()


def select_directory():
  dir = filedialog.askdirectory(
    title="Choose a directory to process",
    initialdir="/"
  )
  print(dir)
  selectedDirStr.set(dir)

ttk.Label(frm, text="Choose Directory").grid(column=0, row=1, padx=5, pady=10, sticky=W)
directory = ttk.Button(
    frm,
    text='Open',
    command=select_directory
).grid(column=1, row=1, padx=5)
selectedDir = Entry(frm, textvariable=selectedDirStr, width=40, state='readonly').grid(column=0, columnspan=2, row=2, pady=10, sticky=W)

ttk.Separator(frm, orient=HORIZONTAL).grid(column=0, columnspan=2, row=3, sticky=(W, E))
ttk.Label(frm, text="Select Profile Targets").grid(column=0, row=4, padx=5, pady=10)

selected_profile = IntVar()
Radiobutton(frm, text="TOP", variable=selected_profile, value=0).grid(column=0, row=5, sticky=W)
Radiobutton(frm, text="BOTTOM", variable=selected_profile, value=1).grid(column=0, row=6, sticky=W)
Radiobutton(frm, text="BOTH", variable=selected_profile, value=2).grid(column=0, row=7, sticky=W)

ttk.Button(frm, text="RUN", command=root.destroy).grid(column=0, row=8, pady=10)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=8, pady=10)

root.mainloop()
