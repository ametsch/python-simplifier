class FileHelper:

    __doc__ = '''
        A class of functions to assist in reading from files
    '''

    def __init__(self):
        pass

    def readFile(self, path: str) -> str:
        temp = None
        with open(path, 'r') as f:
            temp = f.read()
        return temp
    readFile.__doc__ = 'A function to read an entire file into a string'

    def readListFile(self, path: str, sep: str) -> list:
        temp = None
        with open(path, "r") as f:
            temp = f.read().split(sep)
        return temp
    readListFile.__doc__ = 'A function to read sections of a file seperated by \'sep\' into a list'
    
    def readcsv(self, path: str) -> list:
        list = []
        with open(path, 'r') as f:
            list = f.readlines()
        out = []
        for i in list:
            out.append(i.split(','))
        return out
    readcsv.__doc__ = 'A function to read a csv file into a list of lists'