from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from tkinter import*
from tkinter import filedialog
import notepad_class
class PdfCon:
    def __init__(self,pos):
        self.pos=pos
        text=notepad_class.Note.txt[self.pos]
        content=text.get('1.0',END).splitlines()
        styles = getSampleStyleSheet()
        try:
          filesave = filedialog.asksaveasfilename(title="select",defaultextension="*.pdf",filetypes=(("PDF","*.pdf"),("All files","*.*")))
          doc = SimpleDocTemplate(filesave)
          Story = [Spacer(1,0.1*inch)]
          style = styles["Normal"]
          for i in content:
               p = Paragraph(i, style)
               Story.append(p)
               Story.append(Spacer(1,0.1*inch))
          doc.build(Story)
        except:
            None






