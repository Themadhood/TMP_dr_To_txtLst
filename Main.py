__Program__     = "TMP_dr_To_txtLst"    
__Programer__   = "Themadhood Pequot"
__Date__        = "1/14/2025"
__Version__     = "0.0.1"
__Time__        = "0000:00:00: 00:45:00"
__Update__      = ""
__Info__        = ""

#10:43

#Imports
#import Error
import os,sys,io
import tkinter as TK
from tkinter import messagebox as MB
from tkinter import filedialog as FD

#compile PYsInfo
VersionLst = [f"{__Program__}: {__Version__}: {__Time__}"]

#if importing with *
#VersionLst += [f"{__Program__}: {__version__}: {__Time__}"]

#presets
BG = "black"
FG = "white"

class Main(TK.Tk):
    drPath = None
    def __init__(self):
        TK.Tk.__init__(self)

        self.title('List Drectory')
        self.geometry("+341+285")
        self.resizable(width = False, height = False)
        self.config(bg=BG)


        TK.Button(takefocus = True, text = 'Directory',
                  command=self.SetDr).grid(row=0, column=0,padx=10,pady=10)

        TK.Button(takefocus = True, text = 'Text File',
                  command=self.SaveFile).grid(row=1,
                                              column=2,padx=10,pady=10)
        
        self.drlbl = TK.Label(bg=BG,fg=FG,takefocus = True,
                              text = str(self.drPath),wraplength=200)
        self.drlbl.grid(row=1, column=0,padx=10,pady=10)

        TK.Label(bg=BG,fg=FG,takefocus = True,
                 text = '---->>', ).grid(row=1, column=1,padx=10,pady=10)

        self.mainloop()



    def SetDr(self):
        path = FD.askdirectory()
        if path == "":
            return
        self.drPath = path

        self.drlbl.config(text = str(self.drPath))
        
    def SaveFile(self):
        if self.drPath == None:
            MB.showwarning('warning','Directory path is not selected')
            return
        path = FD.asksaveasfile(filetypes =[('Text Document', '*.txt')],
                                defaultextension=[('Text Document', '*.txt')])
        if path == None:
            MB.showwarning('warning','Plese select a file to save')
            return
            
        path = path.name

        #read directory files
        fileLst = self.ReadDrFiles()

        #write to file
        with io.open(path, "w", encoding='utf-8') as file:
            file.write(fileLst)
            file.close()

        self.drPath = None
        self.drlbl.config(text = str(self.drPath))


    def ReadDrFiles(self):
        drLst = os.listdir(self.drPath)
        retar = ""
        for file in drLst:
            retar += file
            retar += "\n"
        return retar






def test_dummy():
    pass










Main()



