from pipreqs.pipreqs import get_all_imports
import subprocess
import sys
import pip

class PyBuddy:

    @staticmethod
    def scrapDependencies(path):
        return get_all_imports(path, "utf-8")
        
    def installDependencies(deps):
        for dep in deps:
                if hasattr(pip, 'main'):
                    pip.main(['install', dep])
                else:
                    pip._internal.main(['install', dep])
            # subprocess.check_call([sys.executable, "-m", "pip3", "install", dep])
        return True

    def runProject(path, pyfile, django=False):
        if django:
            subprocess.run(["python", f"{path}/manage.py", "runserver"], shell=True)
        else:
            subprocess.run(["python", f"{path}/{pyfile}"])

# print(PyBuddy.scrapDependencies("projects/uvproject"))

# PyBuddy.installDependencies(PyBuddy.scrapDependencies("projects/uvproject"))

# PyBuddy.runProject("projects/uvproject/", 'manage')