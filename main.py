from tkinter import *
from PdfScrapper import PdfScrapper

from fileManagement import FileManager

        
root = Tk()
root.geometry("800x600")
root.winfo_toplevel().title("Project Presentation Software (PPS)")

pdfUrl = StringVar()
studentID = StringVar()

def getPDF():
    # tname = FileManager.downloadFIle(pdfUrl.get())
    # FileManager.moveFile(f"./assets/temp/{tname}.pdf", f"./assets/pdf/{studentID.get()}.pdf")
    text = PdfScrapper.readFile(50238)
    PdfScrapper.getData(text, 'stId', 'github')


H1 = Label(root, text="Welcome")
H2 = Label(root, text="to")
H3 = Label(root, text="Project Presentation Software (PPS)")

idLabel = Label(root, text="Student ID:")
idEntry = Entry(root, textvariable=studentID, width=100)

l = Label(root, text="Enter pdf url of the project")
pdfUrlEntry = Entry(root, textvariable=pdfUrl, width=100)

b = Button(root, text="Submit", padx=10, cursor="hand2", command=getPDF)

H1.pack()
H2.pack()
H3.pack()
idLabel.pack(pady=(100,0))
idEntry.pack()
l.pack(pady=(20,0))
pdfUrlEntry.pack()
b.pack()



root.mainloop()