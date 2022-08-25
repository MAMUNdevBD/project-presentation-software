from pipreqs.pipreqs import get_all_imports
import subprocess
import sys
from subprocess import call

class PyBuddy:

    @staticmethod
    def scrapDependencies(path):
        return get_all_imports(path, "utf-8")
        
    def installDependencies(deps):
        for dep in deps:
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])

    def runProject(path, root):
        call(["python", "projects/project-presentation-software/main.py"])

# PyBuddy.installDependencies(PyBuddy.scrapDependencies("projects/project-presentation-software"))

PyBuddy.runProject("projects/project-presentation-software/", 'a')