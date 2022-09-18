from glob import glob
import tkinter as tk
import json
from tkinter import Button, Frame, Label, filedialog
from pps.services.dataService import DataService
from pps.services.PdfScrapper import PdfScrapper
# from services.dataService import DataService

from pps.screens.GitScreen import GitScreen

class MainScreen(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        

        Label(self, text="Welcome").pack()
        Label(self, text="to").pack()
        Label(self, text="Project Presentation Software (PPS)").pack()

        Button(self, text="Select Folder", cursor="hand2", width=20, command=lambda: self.selectDirectory()).pack(pady=20)

    def selectDirectory(self):
        path = filedialog.askdirectory()
        data = {
            "project_path": path
        }
        DataService().saveData(data)

        self.readPDF()

        self.controller.show_frame(GitScreen)
        self.controller.page = 2

    def readPDF(self):
        data = DataService().getAllData()
        filePath = data["project_path"]
        pdfs = glob(filePath+"/*.pdf")
        for pdf in pdfs:
            d = PdfScrapper.getData(PdfScrapper.readFile(pdf), "stId", "github")
            data.update(d)
            DataService().saveData(data)
        

        



  

    # Button(root, text="Submit", padx=10, cursor="hand2", command=getPDF, width=20).pack(pady=20)