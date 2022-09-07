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
        call(["python", f"{path+root}.py", "runserver"])

print(PyBuddy.scrapDependencies("projects/uvproject"))

# PyBuddy.installDependencies(PyBuddy.scrapDependencies("projects/uvproject"))

PyBuddy.runProject("projects/uvproject/", 'manage')