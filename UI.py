
from distutils.archive_util import make_archive
from tkinter import *
from tkinter import filedialog
from main import *


path = ""

def openFile():
    global path
    print("Open")
    path=filedialog.askdirectory()
    print(path)

def Archive():
    print("Archive")
    make_archive(path, "zip", path)
    print(path)
    


root=Tk()
root.title("Zip It")
root.geometry("300x300")

open=Button(root,text="Open",width=10,height=2,command=lambda:openFile())
open.pack()
archive=Button(root,text="Archive",width=10,height=2,command=lambda:Archive())
archive.pack()



root.mainloop()