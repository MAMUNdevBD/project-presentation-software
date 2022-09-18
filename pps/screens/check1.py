from tkinter import Button, IntVar, Label, StringVar, Tk

from ProposalScreen import ProposalScreen
root = Tk()
root.geometry("800x600")

screen = StringVar()

def changeScreen(s):
    screen.set(s)
    

def check1(root):
    root.winfo_toplevel().title("1 Project Presentation Software (PPS)")
    Label(root, textvariable=screen).pack()
    Button(root, text="Click me", command=changeScreen("Home2")).pack()

match screen:
    case "home":
        check1(root)
    case "proposal":
        ProposalScreen()



root.mainloop()