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

def applyChange(changedTable : dict, tableName:str, isLoad:bool = False):
    global db, isChange

    db["data"][tableName] = changedTable
    db["tableName"][db["numTable"]] = tableName
    db["numTable"] += 1
    isChange = not isLoad

def isChanged() -> bool:
    return isChange

def readDatabase():
    return db