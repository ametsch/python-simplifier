import glob

__doc__ = '''
    A group of functions to assist in reading from files
'''

def readFile(path: str) -> str:
    temp = None
    with open(path, 'r') as f:
        temp = f.read()
    return temp
readFile.__doc__ = 'A function to read an entire file into a string'

def readListFile(path: str, sep="\n") -> list:
    temp = None
    with open(path, "r") as f:
        temp = f.read().split(sep)
    return temp
readListFile.__doc__ = 'A function to read sections of a file seperated by \'sep\' into a list'

def readcsv(path: str) -> list:
    list = []
    with open(path, 'r') as f:
        list = f.readlines()
    out = []
    for i in list:
        out.append(i.split(','))
    return out
readcsv.__doc__ = 'A function to read a csv file into a list of lists'

def appendFiles(outPath: str, globPatern: str) -> None:
    with open(outPath, 'w') as f:
        pass
    li = glob.glob(globPatern)

    for path in li:
        data = []
        with open(path, 'r') as f:
            data = f.readlines()
        with open(outPath, 'a') as f:
            f.writelines(data)
appendFiles.__doc__ = 'A function to combine all files which match the given glob pattern and write it to the given output path'

def strToFile(path: str, contents: str) -> None:
    with open(path, 'w') as f:
        f.write(contents)