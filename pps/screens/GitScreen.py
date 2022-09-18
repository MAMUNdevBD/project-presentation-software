from tkinter.ttk import Progressbar
import git, glob, os
from tkinter import Button, Frame, Label
from services.pyBuddy import PyBuddy
from services.fileManagement import FileManager
from services.dataService import DataService
from services.githubManager import GitController


class GitScreen(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.d = None
        self.files = []

        # self.d = DataService().getAllData()

        Label(self, text="Repository Page").pack(pady=20)
        # Label(self, text="Your Repository is: "+ self.d['git']).pack(pady=20)

        
        self.installDep = Button(self, text="Install Dependencies", command=lambda: self.installDependencies())

        self.lb = Label(self, text="Select your main file to run")

        self.cloneB = Button(self, text="Proceed Cloning Repository", command=lambda: self.cloneGit())
        self.cloneB.pack()
        self.pb = Progressbar(self, orient='horizontal', length=100, mode="determinate")
        self.pb.pack(pady=20)

    def runCodes(self, file):
        print(file)
        PyBuddy.runProject(self.d['project_path']+"/source", file)

    def installDependencies(self):
        self.pb['value'] = 0
        deps = PyBuddy.scrapDependencies(self.d['project_path'])
        PyBuddy.installDependencies(deps)
        self.pb['value'] = 100
        self.installDep.pack_forget()
        os.chdir(self.d['project_path']+"/source")
        for file in glob.glob("*.py"):
            self.files.append(file)
        self.lb.pack()
        for file in self.files:
            self.runCode = Button(self, text=file, command=lambda: self.runCodes(file))
            self.runCode.pack(pady=50)


    def cloneComplete(self):
        self.pb['value'] = 100
        self.cloneB.pack_forget()
        self.installDep.pack()

    def cloneGit(self):
        self.d = DataService().getAllData()
        FileManager.removeFolder(self.d['project_path']+"/source")
        git.Repo.clone_from(self.d['git'], self.d['project_path']+"/source", progress=self.cloneComplete())