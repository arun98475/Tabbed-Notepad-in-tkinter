from tkinter import*
class About:
    def __init__(self):
        self.win=Tk()
        self.win.title("About")
        self.win.geometry('400x400')
        self.c=Canvas(self.win,width=300,height=300,bg="black")
        self.c.place(x=50,y=50)
        rect=self.c.create_rectangle(25,25,275,275,fill="blue")
        txt=self.c.create_text(150,100,fill="black",font="Times 20 italic bold",text="Created By Arun")
        txt1=self.c.create_text(150,150,fill="black",font="Times 20 italic bold",text="Created in Python")
       # self.line=self.c.create_line(0,25,25,25,fill="white")
        self.y1=25
        self.y3=275
        
        while True:
             self.win.update() 
             self.c.after(50, self.move())
    def move(self):
            self.y1=self.y1+5
            self.y3=self.y3-5
            if self.y1<300 :
                
                self.line=self.c.create_line(0,self.y1,25,self.y1,fill="white") 
                self.line=self.c.create_line(self.y1,275,self.y1,300,fill="white")
                self.line=self.c.create_line(275,self.y3,300,self.y3,fill="white")
                self.line=self.c.create_line(self.y3,25,self.y3,0,fill="white")
            else:
                self.y1=25
                self.y3=275
                for i in range (60):
                    self.y1=self.y1+5
                    self.y3=self.y3-5
                    self.line=self.c.create_line(0,self.y1,25,self.y1,fill="black") 
                    self.line=self.c.create_line(self.y1,275,self.y1,300,fill="black")
                    self.line=self.c.create_line(275,self.y3,300,self.y3,fill="black")
                    self.line=self.c.create_line(self.y3,25,self.y3,0,fill="black")
                self.y1=25
                self.y3=275
                     
        

