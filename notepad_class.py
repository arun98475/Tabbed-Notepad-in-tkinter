from tkinter import*
from tkinter import filedialog
class Note:
  #count=0
  txt=[]
  file=[]
  def __init__(self,frame):
    self.win=frame
    xscroll=Scrollbar(self.win,orient=HORIZONTAL)
    xscroll.grid(row=1,column=0,sticky=S+W+E)
    yscroll=Scrollbar(self.win)
    yscroll.grid(row=0,column=1,sticky=E+S+N)
    self.text=Text(self.win,wrap='none',xscrollcommand=xscroll.set,yscrollcommand=yscroll.set,undo=True)
    
    self.text.grid(row=0,column=0,sticky=N+S+E+W)
    xscroll.config(command=self.text.xview)
    yscroll.config(command=self.text.yview)
    self.win.grid_rowconfigure(0, weight=1) # For row 0
    self.win.grid_columnconfigure(0, weight=1) # For column 0
    temp=[self.text]
    Note.txt.extend(temp)
  def Savethis(self,pos):
      self.pos=pos
      global filesave
      if len(Note.file)<=pos:
         filesave = filedialog.asksaveasfilename(title="select",defaultextension="*.txt",filetypes=(("Text","*.txt"),("All files","*.*")))
         self.temfile=[filesave]
         Note.file.extend(self.temfile)
         f=open(Note.file[self.pos],'w')
         f.write(self.text.get("1.0",END))
         f.close
      else:
         f=open(Note.file[self.pos],'w')
         f.write(self.text.get("1.0",END))
         f.close
  
  def SaveAsthis(self,pos):
      self.pos=pos
      filesaveas = filedialog.asksaveasfilename(title="select",defaultextension="*.txt",filetypes=(("Text","*.txt"),("All files","*.*")))
      Note.file[self.pos]=filesaveas
      f=open(filesaveas,'w')
      f.write(self.text.get("1.0",END))
      f.close
  
  def Openthis(self):
      fileopen = filedialog.askopenfilename(title="select",defaultextension="*.txt",filetypes=[("Text","*.txt")])
      f=open(fileopen,'r')
      content=f.read()
      self.text.delete("1.0",END)
      self.text.insert(END,content)
      f.close
  
  def Quit(self):
      exit()
  
  def PasteThis(self):
      point=self.text.index(INSERT)
      self.text.insert(point,self.win.clipboard_get())
   
  def CopyThis(self):
      self.win.clipboard_clear()
      selection=self.text.get(SEL_FIRST, SEL_LAST)
      self.win.clipboard_append(selection)
    
  def CopyAll(self):
      self.text.tag_add(SEL,"1.0", END)
      self.win.clipboard_clear()
      selection=self.text.get("1.0", END)
      self.win.clipboard_append(selection)
    
  def CutAll(self):
      self.win.clipboard_clear()
      selection=self.text.get("1.0", END)
      self.text.delete("1.0", END)
      self.win.clipboard_append(selection)
  
  def CutThis(self):
      self.win.clipboard_clear()
      selection=self.text.get(SEL_FIRST, SEL_LAST)
      self.text.delete(SEL_FIRST, SEL_LAST)
      self.win.clipboard_append(selection)
    
  def SelectAll(self):
      self.text.tag_add(SEL,"1.0", END)
      self.text.mark_set(INSERT, "1.0")
      self.text.see(INSERT)
    
  def UnDo(self):
      self.text.edit_undo()
  
  def ReDo(self):
      self.text.edit_redo()
      
  def DarkThemer(self):
      self.text.config(bg="Black")
      self.text.config(fg="White")
      self.text.config(insertbackground="White")
      
  def BrightThemer(self):
      self.text.config(bg="White")
      self.text.config(fg="Black")
      self.text.config(insertbackground="Black")
 
  def fontChanger(self):
      def changeFont():
        self.text.config(font="{0} {1} {2}" .format(font.get(),size.get(),fontstyle.get()))
      FormatWin=Tk()
      FormatWin.title("Select your Font")
      FormatWin.geometry("450x60")
    
      font=ttk.Combobox(FormatWin,values=["Calibri","Cambria_Math","Candara"])
      font.current(0)
      size=ttk.Combobox(FormatWin,values=["12","20","36"])
      size.current(0)
      fontstyle=ttk.Combobox(FormatWin,values=["normal","bold","italic"])
      fontstyle.current(0)
      size.grid(row=0,column=0)
      font.grid(row=0,column=1)
      fontstyle.grid(row=0,column=2)
      Button(FormatWin,text="Apply",padx=5,command=changeFont).grid(row=1,column=2,sticky="e")
      
      


