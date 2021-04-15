#  Module database
# Modul ini berisi  realisasi fungsi
# getTable yang akan digunakan untuk 
# mengambil tabel dari data database

from core.constant import MAX_ARRAY_NUM


db = {
    "data" : {},
    "tableName" : ["" for i in range(MAX_ARRAY_NUM)],
    "numTable" : 0
}
isChange = False

def getTable(name:str) -> dict:
    """
    getTable menerima sebuah name yang merupakan nama dari tabel
    pada database. Nama tabel adalah nama file tanpa ekstensi. 
    
    Fungsi ini akan mengembalikan sebuah dict yang merupakan 
    struktur data tabel. LIhat dokumentasi.
    """
    global db

    if db == {}:
        print("ERROR: database belum diload.")
        return {}
    else:
        isExist = False

        for i in range(db["numTable"]):
            if(name  == db["tableName"][i]):
                isExist = True
                break
        
        if not isExist:
            print("ERROR : Tabel tidak ditemukan")
            return {}
        
        return db["data"][name]

def applyChange(changedTable : dict, tableName:str):
    global db, isChange

    db["data"][tableName] = changedTable
    isEditing = False
    for i in range(db["numTable"]):
        isEditing = isEditing or (db["tableName"][i] == tableName)

    if not isEditing:
        db["tableName"][db["numTable"]] = tableName
        db["numTable"] += 1

    isChange = True

def isChanged() -> bool:
    return isChange

def readDatabase():
    return db

def resetChanged():
    global isChange
    isChange = False