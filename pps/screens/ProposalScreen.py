from tkinter import *
from tkinter import filedialog

class ProposalScreen:

    def __init__(self) -> None:
        root = Tk()
        self.root = root
        self.settings()
        self.render()
        self.root.mainloop()

    def settings(self):
        self.root.geometry("800x600")
        self.root.winfo_toplevel().title("Proposal")

    def render(self):
        Label(self.root, text="Welcome").pack()
        Label(self.root, text="to").pack()
        Label(self.root, text="Project Presentation Software (PPS)").pack()

        filedialog.askdirectory()

        return True


ProposalScreen()