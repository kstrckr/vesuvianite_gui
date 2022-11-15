from tkinter import filedialog

def select_directory():
  dir = filedialog.askdirectory(
    title="Choose a directory to process",
    initialdir="/"
  )
  print(dir)
  return dir

  # showinfo(title="selected Directory", message=dir)
