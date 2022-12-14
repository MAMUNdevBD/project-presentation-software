import tkinter as tk
from tkinter import IntVar, ttk
from pps.screens.GitScreen import GitScreen

from pps.screens.MainScreen import MainScreen

class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Project Presentation Software")
        self.page = IntVar()
        container = tk.Frame(self, height=400, width=600) 
        self.geometry("800x600")
        
        container.pack( fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # dictionary of frames
        self.frames = {}

        for F in (MainScreen, GitScreen):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(MainScreen)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()



if __name__ == "__main__":
    testObj = windows()
    testObj.mainloop()