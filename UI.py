
from distutils.archive_util import make_archive
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from main import *




path = ""
savepath=""

root=Tk()
root.title("Zip It")
root.geometry("980x320")
root.iconbitmap('zip.ico')


txtFile=Text(root,width=100,height=2)
txtFile.grid(row=0,column=0,padx=10,pady=10)





txtSave=Text(root,width=100,height=2)
txtSave.grid(row=1,column=0)



text=StringVar()
status=Label(root,textvariable=text,width=100,height=2)
status.grid(row=2,column=0,padx=10,pady=10)
text.set("Please Choose Directory to make Archive")

def openFile():
    global path
    global txtFile
    global text
    print("Open")
    path=filedialog.askdirectory()
    txtFile.delete(1.0,'end')
    txtFile.insert(1.0,path)
    text.set('Selected Path: '+path)

def select_dest():
    global txtSave
    global savepath
    global text
    savepath=filedialog.asksaveasfilename()
    txtSave.delete(1.0,'end')
    txtSave.insert(1.0,savepath)
    text.set('File will be Saved At: '+savepath)
    


def Archive():
    global savepath
    global text
    try:
        make_archive(savepath, "zip", path)
    except OSError as ex:
        messagebox.showinfo("File Error","System Cannot Find Path Specified")  
    text.set('Archive Saved At:'+savepath)


brows=Button(root,text="Brows",width=20,height=2,command=lambda:openFile())
brows.grid(row=0,column=1)



select=Button(root,text="Select Destination",width=20,height=2,command=lambda:select_dest())
select.grid(row=1,column=1)

archive=Button(root,text="Archive",width=20,height=2,command=lambda:Archive())
archive.grid(row=2,column=1)

root.mainloop()