# Module load
# Modul ini berisi fungsi yang berkaitan
# dengan pemuatan data dari file csv

# PUSTAKA
from os import R_OK,  walk
from os import access
from os.path import abspath, isabs, isdir, isfile, join, exists

from core.util import split
from core.constant import DB_FILES_NAME, MAX_ARRAY_NUM
from .database import *

# KAMUS
# type table = < data: Array of ..., {Menyesuaikan dengan jenis tabelnya}
#                   row_number: integer,
#                   col_number: integer,
#                   columnName: Array of string>

# type row = <...> { Menyesuaikan dengan kolom pada database. Nama field
#                    adalah nama kolom dan valuenya adalah nilai pada 
#                    database }

# function readFile(path:string) -> string
# Fungsi ini mengeluarkan isi dari file pada path.
# Jika path tidak valid, bukan file atau tidak ada,
# akan mengeluarkan pesan error.

# function loadDatabase(dir:string) -> boolean
# Fungsi ini akan menerima sebuah direktori dir dari database
# lalu memparse datanya. Jika parsing berhasil akan mengeluarkan
# True dan mengubah data db. Jika tidak berhasil, mengeluarkan
# False.

# function tableParser(tableData:string) -> table
# Fungsi ini akan memparse data mentah tableData
# menjadi table yang dapat diproses pada file ini.

# function isValidDir(dir:str) -> boolean
# Fungsi ini memeriksa apakah folder dir merupakan folder
# database yang valid. Folder yang valid terdiri dari file yang
# dibutuhkan dan berada dalam root tertinggi dari dir.

# ALGORITMA
def readFile(path:str) -> str:
    """Fungsi ini mengeluarkan isi dari file pada path"""
    # KAMUS LOKAL
    # fileReader : SEQFILE of 
    #          (*) hasil: string
    #          (1) \0x1A { EOF CHARACTER } 

    # ALGORITMA
    if(access(path, R_OK)):
        if(isfile(path)):
            fileReader = open(path, "r")
            hasil = fileReader.read()
            fileReader.close()
            
            return hasil
        else:
            print("ERROR : Input harus merupakan lokasi file")
            return ""
    else:
        print(f"ERROR : File '{path}' tidak bisa diakses.")
        return ""

def loadDatabase(dir:str) -> bool:
    """Fungsi ini akan menerima sebuah direktori dir dari database
    lalu memparse datanya. Jika parsing berhasil akan mengeluarkan
    True dan mengubah data db. Jika tidak berhasil, mengeluarkan
    False."""
    # KAMUS LOKAL
    # i : integer
    # fileData : string
    # parsedTable : table

    # ALGORITMA
    if isValidDir(dir):
        for i in range(DB_FILES_NAME[1]):
            # Membaca data dari file
            fileData = readFile(join(dir, DB_FILES_NAME[0][i]))
            if fileData != "":
                parsedTable = tableParser(fileData)
                applyChange(parsedTable, DB_FILES_NAME[0][i][:-4])
                resetChanged()
            else:
                return False
            
        return True
    else:
        return False

def tableParser(tableData):
    """Fungsi ini akan memparse data mentah tableData
    menjadi table yang dapat diproses pada file ini."""
    # KAMUS LOKAL
    # parsedRow: row
    # parsedTable: table
    # rawRow: Array of string
    # tableColumns: Array of string
    # splittedRow : Array of  string
    # i,j : integer

    # ALGORITMA
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
    # KAMUS LOKAL
    # type fileCollection = <
    #      "consumable_history.csv": boolean,
    #      "consumable.csv": boolean,
    #      "gadget_borrow_history.csv": boolean,
    #      "gadget_return_history.csv": boolean,
    #      "gadget.csv": boolean,
    #      "user.csv": boolean
    # >

    # root, dirs, files: string
    # fileCheck : fileCollection
    # i : integer
    # isRequiredExist: boolean

    # ALGORITMA
    if(not isabs(dir)):
        # Membuat path menjadi absolute
        dir = abspath(dir)

    if(isdir(dir)):
        if(exists(dir)):
            if(access(dir, R_OK)):
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
                print(f"ERROR : TIdak dapat membaca folder '{dir}'.")
                return False
        else:
            print(f"ERROR : Lokasi '{dir}' tidak ditemukan.")
            return False
    else:
        print(f"Lokasi '{dir}' bukan merupakan folder yang sah")
        return False