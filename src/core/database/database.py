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
    """
    applyChange akan menyimpan perubahan pada database. Parameter 
    changeTable merupakan struktur data `table` yang diambil dengan 
    menggunakan fungsi `getTable()` yang telah diubah. tableName 
    merupakan nama tabel  yang dimaksud. Nama tabel harus sama 
    dengan nama file tanpa ekstensi seperti pada `getTable()`.

    FUugsi ini harus dijalankan setelah melakukan perubahan pada 
    table agar tersimpan pada struktur data database.
    """
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
    """
    Fungsi ini akan memeriksa apakah sudah ada perubahan yang
    dilakukan pada database. Jika sudah, akan mengembalikan
    True.
    """
    return isChange

def readDatabase():
    """
    Fungsi ini akan mengeluarkan objek database saat fungsi ini
    dijalankan.
    """
    return db

def resetChanged():
    """
    Prosedur ini akan mengubah status perubahan menjadi False.
    """
    global isChange
    isChange = False