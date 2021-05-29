import os.path
import sys
import importlib
from pathlib import Path

path = os.path.expanduser('~')
os = sys.platform

if os == 'win32':
    path += '\\current_search.txt'
else:
    path += '/current_search.txt'

def returnOrCreateFile():
    filePath = Path(path)

    if not filePath.is_file():
        with open(path, 'w+') as nf:
            pass

    file = open(filePath, 'r')
    fileAsString = file.read()
    file.close()
    return fileAsString

def writeToFile(str):
    with open(path, 'a') as f:
        f.write(str)
    # Gui = importlib.import_module('Gui')
    # Gui.generateCurrentSearch()

def addNewLine(line):
    currentContent = returnOrCreateFile()

    if currentContent:
        writeToFile('\n'+line)
    else:
        writeToFile(line)

def deleteLine(lineToDelete):
    with open(path, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()

        for line in lines:
            if line != lineToDelete:
                f.write(line)
    
