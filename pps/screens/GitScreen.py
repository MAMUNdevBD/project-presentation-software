from tkinter.ttk import Progressbar
import git, glob, os
from tkinter import Button, Frame, Label
from pps.services.pyBuddy import PyBuddy
from pps.services.fileManagement import FileManager
from pps.services.dataService import DataService
from pps.services.githubManager import GitController


class GitScreen(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.d = None
        self.files = []

        # self.d = DataService().getAllData()

        Label(self, text="Repository Page").pack(pady=20)
        # Label(self, text="Your Repository is: "+ self.d['git']).pack(pady=20)

        
        self.installDep = Button(self, text="Install Dependencies", command=lambda: self.installDependencies())

        self.cloneB = Button(self, text="Proceed Cloning Repository", command=lambda: self.cloneGit())
        self.cloneB.pack()
        self.pb = Progressbar(self, orient='horizontal', length=100, mode="determinate")
        self.pb.pack(pady=20)

    def runCodes(self, file=None, k=0):
        print(file)
        if file:
            PyBuddy.runProject(self.d['project_path']+"/source", file)
        else:
            PyBuddy.runProject(self.d['project_path']+"/source", file, django=True)

    def installDependencies(self):
        self.pb['value'] = 0
        self.deps = PyBuddy.scrapDependencies(self.d['project_path'])
        PyBuddy.installDependencies(self.deps)
        self.pb['value'] = 100
        self.installDep.pack_forget()
        # os.chdir(self.d['project_path']+"/source")
        for file in glob.glob(self.d['project_path']+"/source/*.py"):
            self.files.append(file)
        Label(self, text="Dependencies used in this project").pack()
        self.d.update({"dependencies": self.deps})
        DataService().saveData(self.d)
        for dep in self.deps:
            Label(self, text=dep).pack()
        if "django" in self.deps:
            Button(self, text="Run The Project", command=lambda: self.runCodes()).pack(pady=5)
        else:
            Label(self, text="Select your main file to run").pack()
            for i in range(len(self.files)):
                Button(self, text=self.files[i], command=lambda i=i: self.runCodes(self.files[i])).pack(pady=5)


    def cloneComplete(self):
        self.pb['value'] = 100
        self.cloneB.pack_forget()
        self.installDep.pack()

    def cloneGit(self):
        self.d = DataService().getAllData()
        FileManager.removeFolder(self.d['project_path']+"/source")
        git.Repo.clone_from(self.d['git'], self.d['project_path']+"/source", progress=self.cloneComplete())