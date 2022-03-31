
from distutils.archive_util import make_archive
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox



class App:

    def __init__(self):
        self.root = Tk()
        self.root.title("Zip It")
        self.root.geometry("980x320")
        #self.root.iconbitmap('zip.ico')

        self.txtFile = Text(self.root, width=100, height=2)
        self.txtFile.grid(row=0, column=0, padx=10, pady=10)


        self.text = StringVar()
        self.status = Label(self.root, textvariable=self.text, width=100, height=2)
        self.status.grid(row=2, column=0, padx=10, pady=10)

        self.text.set("Please Choose Directory to make Archive")

        self.btnOpen = Button(self.root, text="Open", command=self.openFile)
        self.btnOpen.grid(row=3, column=0, padx=10, pady=10)

        self.btnSave = Button(self.root, text="Save", command=self.saveZip)
        self.btnSave.grid(row=4, column=0, padx=10, pady=10)
        self.btnSave.config(state=DISABLED)


        self.root.mainloop()


    def openFile(self):
        self.txtFile.delete(1.0,'end')
        self.txtFile.insert(1.0,filedialog.askdirectory())
        self.text.set("Selected Path: "+self.txtFile.get(1.0,'end'))
        self.btnSave.config(state=NORMAL)

    def saveZip(self):
        self.text.set("Please Wait...")
        try:
            make_archive(self.txtFile.get(1.0,'end')[:-1], "zip", self.txtFile.get(1.0,'end')[:-1])
        except OSError as ex:
            self.text.set("Error: "+str(ex))
            self.btnSave.config(state=DISABLED)
            messagebox.showerror("File Error",str(ex))  
        else:
            self.text.set("Archive Created Successfully")
            messagebox.showinfo("File Created", "Archive Created Successfully")
            self.btnSave.config(state=DISABLED)
