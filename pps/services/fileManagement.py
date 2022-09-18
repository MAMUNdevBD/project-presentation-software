from pathlib import Path
import random
import shutil
import requests
from git import rmtree

class FileManager:

    @staticmethod
    def downloadFIle(url):
        r = requests.get(url, allow_redirects=True)
        rname = random.randint(111111111,999999999999)
        open(f'./assets/temp/{rname}.pdf', 'wb').write(r.content)
        return rname

    def moveFile(oldPath, newPath):
        Path(oldPath).rename(newPath)

    def renameFile(file, newName):
        newFile = file+newName
        Path(file).rename(newFile)

    def removeFolder(path):
        rmtree(path)
        shutil.rmtree(path,ignore_errors=True)
