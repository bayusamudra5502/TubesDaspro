# Module load
# Modul ini berisi fungsi yang berkaitan
# dengan pemuatan data dari file csv

from os import read, walk
from os.path import isdir, isfile, join

from core.util import split
from core.constant import DB_FILES_NAME, MAX_ARRAY_NUM
from .database import *

def readFile(path:str) -> str:
    """Fungsi ini mengeluarkan isi dari file pada path"""

    if(isfile(path)):
        fileReader = open(path, "r")
        hasil = fileReader.read()
        fileReader.close()
        
        return hasil
    else:
        print("ERROR : Input harus merupakan lokasi file")
        return ""

def loadDatabase(dir:str) -> bool:
    """Fungsi ini akan menerima sebuah direktori dir dari database
    lalu memparse datanya. Jika parsing berhasil akan mengeluarkan
    True dan mengubah data db. Jika tidak berhasil, mengeluarkan
    False."""

    if isValidDir(dir):
        for i in range(DB_FILES_NAME[1]):
            # Membaca data dari file
            fileData = readFile(join(dir, DB_FILES_NAME[0][i]))
            parsedTable = tableParser(fileData)
            
            applyChange(parsedTable, DB_FILES_NAME[0][i][:-4], isLoad=True)
        
        return True
    else:
        return False

def tableParser(tableData):
    """Fungsi ini akan memparse data mentah tableData
    menjadi table yang dapat diproses pada file ini."""

    parsedTable = {
        "data" : [{} for i in range(MAX_ARRAY_NUM)],
        "columnName" : ["" for i in range(MAX_ARRAY_NUM)],
        "row_number" : 0,
        "col_number": 0
    }

    rawRow = split(tableData, "\n")
    tableColumns = ()

    for i in range(rawRow[1]):
        # Membaca data tiap baris
        
        if i == 0:
            tableColumns = split(rawRow[0][i], ";")
            parsedTable["col_number"] = tableColumns[1]
            parsedTable["columnName"] = tableColumns[0]
        elif(rawRow[0][i] != ""):
            parsedRow = {}
            splittedRow = split(rawRow[0][i], ";")
            
            for j in range(splittedRow[1]):
                parsedRow[tableColumns[0][j]] = splittedRow[0][j]
            
            parsedTable["data"][i-1] = parsedRow
            parsedTable["row_number"] += 1
    
    return parsedTable

def isValidDir(dir:str) -> bool:
    """Fungsi ini memeriksa apakah folder dir merupakan folder
    database yang valid. Folder yang valid terdiri dari file yang
    dibutuhkan dan berada dalam root tertinggi dari dir."""

    if(isdir(dir)):
        fileCheck = {}
        for i in range(DB_FILES_NAME[1]):
            fileCheck[DB_FILES_NAME[0][i]] = False

        for (root, dirs, files) in walk(dir, topdown=True):
            if root == dir:
                for i in files:
                    fileCheck[i] = True
        
        isRequiredExist = True
        for i in range(DB_FILES_NAME[1]):
            isRequiredExist = \
                isRequiredExist and fileCheck[DB_FILES_NAME[0][i]]
        
        if (isRequiredExist):
            return True
        else:
            print("ERROR : File yang dibutuhkan tidak ditemukan atau tidak berada pada level teratas.")
            return False
    else:
        print("ERROR : Path bukan merupakan folder")
        return False