from tkinter import*

class findThis():
    
    def __init__ (self,win,note):
        self.win=win
        self.note=note
        self.win.title("Find")
        self.idx = '1.0'
    def entry(self):
        self.entry=Entry(self.win,width=50)
        self.entry.grid(row=0,column=1)
        self.findText=self.entry.get()
    def label(self):
        self.label=Label(self.win,text="Find:")
        self.label.grid(row=0,column=0)
    def button(self):
        self.button=Button(self.win,text="Find",width=10,command=self.Find)
        self.button.grid(row=0,column=2)
    def buttonNext(self):
        self.buttonNext=Button(self.win,text="Next",width=10,command=self.Find)
        self.buttonNext.grid(row=1,column=2)
    def closebut(self):
        self.closebut=Button(self.win,text="Close",width=10,command=self.quit)
        self.closebut.grid(row=1,column=1,sticky="w")
    def quit(self):
        self.win.destroy()
    def Find(self):
        import notepad_class
        pos=self.note.index("current")
        s=self.entry.get()
        text=notepad_class.Note.txt[pos]
        text.tag_remove("found","1.0",END)
        if s:
          
          while 1:
               self.idx  = text.search(s,self.idx,nocase=1,stopindex=END)
               if not self.idx:
                   self.idx='1.0'
                   break
               lastidx = '%s+%dc' % (self.idx, len(s))
               text.tag_add('found', self.idx, lastidx)
               self.idx = lastidx
               text.tag_config('found', foreground='red',background="yellow")
               text.see(self.idx)
               if self.idx:break
        self.entry.focus_set()
