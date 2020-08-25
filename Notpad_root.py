from tkinter import*
from tkinter import filedialog
from tkinter import ttk
import notepad_class
import find
import PdfConvert
import os
win=Tk()
win.title("Arun's Notepad")
notebook = ttk.Notebook(win)
tab = [Frame(notebook),Frame(notebook)]

notebook.add(tab[0],text="Tag1")
notebook.add(tab[1],text="Tag2") 
notebook.pack(side=LEFT,fill="both",expand="yes")

A=[notepad_class.Note(tab[0]),notepad_class.Note(tab[1])]

def onTabselection(*arg):
      x=notebook.index("current")
      MenuItems(A[x])

notebook.bind("<<NotebookTabChanged>>",onTabselection)
def createTab():
    i=len(tab)
    temTab=[Frame(notebook)]
    tab.append(temTab[0])
    notebook.add(tab[i],text="Tag"+str(i+1))
    tempA=[notepad_class.Note(tab[i])]
    A.append(tempA[0])
    MenuItems(A[i])
def tabRemover():
      x=notebook.select()
      if notebook.index("end")!=1:
         notebook.forget(x)

def findThis():
      wini=Tk()
      x=find.findThis(wini,notebook)
      x.entry()
      x.label()
      x.button()
      x.buttonNext()
      x.closebut()
def expPdf():
      pos=notebook.index("current")
      PdfConvert.PdfCon(pos)
def about():
      import Help
      Help.About()
def Savethis():
      pos=notebook.index("current")
      A[pos].Savethis(pos)
      pathname=notepad_class.Note.file[pos]
      filename=os.path.basename(pathname)
      notebook.add(tab[pos],text=filename)
      
def SaveAsthis():
      pos=notebook.index("current")
      A[pos].SaveAsthis(pos)
      pathname=notepad_class.Note.file[pos]
      filename=os.path.basename(pathname)
      notebook.add(tab[pos],text=filename)
def MenuItems(A):
     menubar = Menu(win)
     filemenu = Menu(menubar, tearoff=0)
     
     filemenu.add_command(label="New",command=createTab )
     filemenu.add_command(label="Open", command=A.Openthis)
     filemenu.add_command(label="Save", command=Savethis)
     filemenu.add_command(label="Save as", command=SaveAsthis)
     filemenu.add_command(label="Export as PDF", command=expPdf)
     filemenu.add_command(label="Remove current tab", command=tabRemover)
     filemenu.add_separator()
     filemenu.add_command(label="Exit",command=A.Quit)
     menubar.add_cascade(label="File", menu=filemenu)
     
     editmenu = Menu(menubar, tearoff=0)
     editmenu.add_command(label="Undo", command=A.UnDo)
     editmenu.add_command(label="Redo", command=A.ReDo)
     editmenu.add_separator()
     editmenu.add_command(label="Cut", command=A.CutThis)
     editmenu.add_command(label="Cut all", command=A.CutAll)
     editmenu.add_command(label="Copy", command=A.CopyThis)
     editmenu.add_command(label="Copy all", command=A.CopyAll)
     editmenu.add_command(label="Paste" , command=A.PasteThis)
     editmenu.add_command(label="Find" , command=findThis)
     editmenu.add_separator()
     editmenu.add_command(label="Select all", command=A.SelectAll )
     menubar.add_cascade(label="Edit" ,menu=editmenu)

     formatmenu = Menu(menubar, tearoff=0)
     formatmenu.add_command(label="Font" ,command=A.fontChanger)
     menubar.add_cascade(label="Format" ,menu=formatmenu)

     thememenu = Menu(menubar, tearoff=0)
     thememenu.add_command(label="Dark theme",command=A.DarkThemer)
     thememenu.add_command(label="Bright theme" ,command=A.BrightThemer)
     menubar.add_cascade(label="Theme" ,menu=thememenu)

     helpmenu = Menu(menubar, tearoff=0)
     helpmenu.add_command(label="View Help")
     helpmenu.add_separator()
     helpmenu.add_command(label="About Arun's notepad",command=about )
     menubar.add_cascade(label="Help" ,menu=helpmenu)
     win.config(menu=menubar)
for i in A:
   MenuItems(i)


win.mainloop()


