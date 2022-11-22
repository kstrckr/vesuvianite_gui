import os
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

cr2_count = IntVar()

def select_directory():
  count = 0
  dir = filedialog.askdirectory(
    title="Choose a directory to process",
    initialdir="/"
  )
  print(dir)
  for x in os.listdir(dir):
    if x.endswith(".html"):
        count = count + 1
  cr2_count.set(count)
  print(cr2_count.get())
  selectedDirStr.set(dir)

# row section 30 -------------------------------------------------
ttk.Label(frm, text="Choose Directory").grid(column=0, row=30, padx=5, pady=10, sticky=W)
directory = ttk.Button(
    frm,
    text='Open',
    command=select_directory
).grid(column=1, row=30, padx=5)
selectedDir = Entry(frm, textvariable=selectedDirStr, width=40, state='readonly').grid(column=0, columnspan=2, row=31, pady=5, sticky=W)

# row section 40 -------------------------------------------------
ttk.Label(frm, text=".cr2 File Count:").grid(column=0, row=41, padx=5, pady=5, sticky=E)
selectedDir = Entry(frm, textvariable=cr2_count, width=4, state='readonly').grid(column=1, columnspan=2, row=41, pady=5, sticky=W)

# row section 50 -------------------------------------------------
ttk.Separator(frm, orient=HORIZONTAL).grid(column=0, columnspan=2, row=50, sticky=(W, E))
ttk.Label(frm, text="Select Profile Targets").grid(column=0, row=51, padx=5, pady=10)

selected_profile = IntVar()
Radiobutton(frm, text="TOP", variable=selected_profile, value=0).grid(column=0, row=52, sticky=W)
Radiobutton(frm, text="BOTTOM", variable=selected_profile, value=1).grid(column=0, row=53, sticky=W)
Radiobutton(frm, text="BOTH", variable=selected_profile, value=2).grid(column=0, row=54, sticky=W)


# row section 100 -------------------------------------------------
ttk.Button(frm, text="RUN", command=root.destroy).grid(column=0, row=100, pady=10)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=100, pady=10)

root.mainloop()
