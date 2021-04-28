#  Module database
# Modul ini berisi  realisasi fungsi
# getTable yang akan digunakan untuk 
# mengambil tabel dari data database

# PUSTAKA
from core.constant import MAX_ARRAY_NUM

# KAMUS

# {KOMPONEN ITEM TABEL}
#  type consumableHistory = <
#       id: string
#       id_pengambil: string
#       id_consumable: string
#       tanggal_pengambilan:string
#       jumlah: string
# >

# type consumable = <
#       id: string,
#       nama: string
#       deskripsi: string
#       jumlah: string
#       rarity: character
# >

# type gadgetBorrowHistory = <
#       id: string,
#       id_peminjam: string,
#       id_gadget: string,
#       tanggak_peminjaman: string,
#       jumlah: string,
#       jumlah_kembali: string,
#       is_returned: string
# >

# type gadgetReturnHistory = <
#       id: string,
#       id_peminjamanL string,
#       tanggal_pengambilan: string
#       jumlah: string
# >

# type gadget = <
#       id: string
#       nama: string
#       deskripsi: string
#       jumlah: string
#       rarity: character
#       tahun_ditemukan: string
# >

# type user = < 
#       id: string,
#       username: string,
#       nama: string,
#       alamat: string,
#       password: string,
#       role: string>

# {TIPE DATA TABEL}
# type table = < data: Array of ..., {Menyesuaikan dengan jenis tabelnya}
#                   row_number: integer,
#                   col_number: integer,
#                   columnName: Array of string>

# { DATABASE }
# type dbDataType = <
#   consumable_history: table,
#   consumable: table,
#   gadget_return_history: table,
#   gadget_borrow_history: table,
#   gadget: table,
#   user: table
# >

# type database = <
#       data: dbDataType,
#       tableName: Array[0..6] of string,
#       numTable: integer
# >

# { KAMUS VARIABEL PROGRAM }
# db: database
# ischange: boolean

# function getTable(name: string) -> table
# getTable menerima sebuah name yang merupakan nama dari tabel
# pada database. Nama tabel adalah nama file tanpa ekstensi. 
# Fungsi ini akan mengembalikan sebuah dict yang merupakan 
# struktur data tabel.

# procedure ApplyChange(input changedTable: table, input tableName: string)
# applyChange akan menyimpan perubahan pada database. Parameter 
# changeTable merupakan struktur data `table` yang diambil dengan 
# menggunakan fungsi `getTable()` yang telah diubah. tableName 
# merupakan nama tabel  yang dimaksud. Nama tabel harus sama 
# dengan nama file tanpa ekstensi seperti pada `getTable()`.

# function isChanged() -> boolean
# Fungsi ini akan memeriksa apakah sudah ada perubahan yang
# dilakukan pada database. Jika sudah, akan mengembalikan
# True.

# function readDatabase() -> database
# Fungsi ini akan mengeluarkan objek database saat fungsi ini
# dijalankan.

# procedure resetChanged()
# Prosedur ini akan mengubah status perubahan menjadi False.

db = {
    "data" : {},
    "tableName" : ["" for i in range(MAX_ARRAY_NUM)],
    "numTable" : 0
}

isChange = False

# ALGORITMA
def getTable(name:str) -> dict:
    """
    getTable menerima sebuah name yang merupakan nama dari tabel
    pada database. Nama tabel adalah nama file tanpa ekstensi. 
    
    Fungsi ini akan mengembalikan sebuah dict yang merupakan 
    struktur data tabel. LIhat dokumentasi.
    """
    # KAMUS LOKAL
    # isExist : boolean
    # i : integer

    # ALGORTIMA
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

    Prosedur ini harus dijalankan setelah melakukan perubahan pada 
    table agar tersimpan pada struktur data database.
    """
    # KAMUS LOKAL
    # formattedTable : table
    # numRows : integer
    # i : integer
    # isEditing : boolean


    # ALGORITMA
    global db, isChange

    # Pengaturan jumlah Row
    formattedTable = {
        "data" : [{} for i in range(MAX_ARRAY_NUM)],
        "columnName" : [],
        "row_number": 0,
        "col_number": 0
    }

    numRows = 0
    for i in range(MAX_ARRAY_NUM):
        if changedTable["data"][i] != {}:
            formattedTable["data"][numRows] = changedTable["data"][i]
            numRows += 1

    formattedTable["row_number"] = numRows
    formattedTable["columnName"] = changedTable["columnName"]
    formattedTable["col_number"] = changedTable["col_number"]

    isEditing = False
    for i in range(db["numTable"]):
        isEditing = isEditing or (db["tableName"][i] == tableName)

    db["data"][tableName] = formattedTable

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
    # KAMUS LOKAL

    # ALGORITMA
    return isChange

def readDatabase():
    """
    Fungsi ini akan mengeluarkan objek database saat fungsi ini
    dijalankan.
    """
    # KAMUS LOKAL

    # ALGORITMA
    return db

def resetChanged():
    """
    Prosedur ini akan mengubah status perubahan menjadi False.
    """
    # KAMUS LOKAL

    # ALGORITMA
    global isChange
    isChange = False