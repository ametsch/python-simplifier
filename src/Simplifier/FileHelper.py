class FileHelper:
    def __init__(self):
        pass

    def readFile(self, path: str):
        temp = None
        with open(path, 'r') as f:
            temp = f.read()
        return temp
    
    def readListFile(self, path: str, sep: str):
        temp = None
        with open(path, "r") as f:
            temp = f.read().split(sep)
        return temp