# Module load
# Modul ini berisi fungsi yang berkaitan
# dengan pemuatan data dari file csv

from os import walk
from os.path import isdir, isfile

def readFile(path:str) -> str:
    if(isfile(path)):
        fileReader = open(path, "r")
        return fileReader.read()
    else:
        print("ERROR : Input harus merupakan lokasi file")
        return ""

def loadDatabase(dir:str) -> dict:
    pass