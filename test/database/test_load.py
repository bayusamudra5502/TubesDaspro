import sys
from os import path

CORE_PATH = path.join(path.dirname(path.abspath(__file__)), ".." , "..", "src")
sys.path.append(path.join(CORE_PATH, ".."))
sys.path.append(CORE_PATH)

from core.database import *

# Tulis tes dibawah ini
def test_readFileNull():
    assert readFile("/home/bayu/Downloads") == ""

def test_readFileIris():
    data = readFile("/home/bayu/Documents/TubesDaspro/test/database/Iris.csv")
    assert data != ""

def test_isValidDir():
    assert not isValidDir("/home/bayu/Downloads")
    assert not isValidDir("/home/bayu/Documents/TubesDaspro/")
    assert isValidDir("/home/bayu/Documents/TubesDaspro/db")

def test_tableParser():
    data = readFile("/home/bayu/Documents/TubesDaspro/test/database/Iris.csv")
    prototipe = {
        "data" : [{} for i in range(MAX_ARRAY_NUM)],
        "rows_number" : 0
    }
    fResult = tableParser(data)
    print(fResult)

    assert fResult != prototipe
    cnt = 0
    for i in fResult["data"]:
        if i != {}:
            cnt += 1
    
    assert fResult["row_number"] == cnt
    assert fResult["data"][fResult["row_number"]-1] != {"id":""}

def test_loadDatabase():
    assert loadDatabase("/home/bayu/Documents/TubesDaspro/db")

    assert readDatabase() != {}
    assert not isChanged()

    applyChange({"berubah" : True}, "user")
    assert isChanged()
    assert readDatabase()["data"]["user"] == {"berubah":True}