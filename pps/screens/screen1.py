from tkinter import *
from tkinter.ttk import Separator
from screens.screen2 import callS2
from services.PdfScrapper import PdfScrapper
from services.fileManagement import FileManager

def screen1(root):
    root.winfo_toplevel().title("1 Project Presentation Software (PPS)")

    pdfUrl = StringVar()
    studentID = StringVar()

    def getPDF():
        # tname = FileManager.downloadFIle(pdfUrl.get())
        # FileManager.moveFile(f"./assets/temp/{tname}.pdf", f"./assets/pdf/{studentID.get()}.pdf")
        text = PdfScrapper.readFile(50229)
        data = PdfScrapper.getData(text, 'stId', 'github')
        print(data)
        root.destroy()
        callS2()


    Label(root, text="Welcome").pack()
    Label(root, text="to").pack()
    Label(root, text="Project Presentation Software (PPS)").pack()

    # Label(root, text="Student ID:").pack(pady=(100,0))
    # Entry(root, textvariable=studentID, width=100).pack()

    Label(root, text="Enter pdf url of the project").pack(pady=(20,0))
    Entry(root, textvariable=pdfUrl, width=100).pack()
    Separator(root, orient='vertical').pack(fill='x')

    Button(root, text="Submit", padx=10, cursor="hand2", command=getPDF, width=20).pack(pady=20)

def call():
    root = Tk()
    root.geometry("800x600")
    screen1(root)
    root.mainloop()
