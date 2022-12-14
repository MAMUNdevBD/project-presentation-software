import json, os


class DataService:
    def __init__(self) -> None:
        cwd = os.getcwd()
        self.filePath = cwd+"/pps/storage/data.caz"

    def getAllData(self):
        f = open(self.filePath, "r")
        data = json.load(f)
        f.close()
        return data

    def saveData(self, data):
        json_object = json.dumps(data, indent=4)
        f = open(self.filePath,"w")
        f.write(json_object)
        f.close()      