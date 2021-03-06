# Module save
# Modul ini merupakan implementasi dari fitur
# Penyimpanan pada program ini.

# PUSTAKA
from .database import readDatabase, resetChanged
from os.path import join, abspath, isdir, exists, dirname, basename
from os import W_OK, access, mkdir

# KAMUS
# type table = < data: Array of ..., {Menyesuaikan dengan jenis tabelnya}
#                   row_number: integer,
#                   col_number: integer,
#                   columnName: Array of string>

# type row = <...> { Menyesuaikan dengan kolom pada database. Nama field
#                    adalah nama kolom dan valuenya adalah nilai pada 
#                    database }

# type dbDataType = <
#   consumable_history: table,
#   consumable: table,
#   gadget_return_history: table,
#   gadget_borrow_history: table,
#   gadget: table,
#   user: table
# >

# type db = <
#       data: dbDataType,
#       tableName: Array[0..6] of string,
#       numTable: integer
# >

# procedure save(input saveDir: string)
# Fungsi ini akan menyimpan semua data pada database di
# folder saveDir dalam format csv. Jika proses berhasil,
# fungsi mengembalikan True.

# ALGORITMA
def save(saveDir):
    """Fungsi ini akan menyimpan semua data pada database di
    folder saveDir dalam format csv. Jika proses berhasil,
    fungsi mengembalikan True."""
    # KAMUS LOKAL
    # database: db
    # tableData: table

    # isChangeApply, isChangePartial : boolean
    # i, j, k: integer
    # tableName : string
    # fileName, filePath : string

    # file: SEQFILE of
    #         (*) data: string
    #         (1) \0x1A { EOF Character }

    # ALGORITMA
    if not exists(saveDir):
        print(f"\033[33mPERINGATAN:\033[0m Lokasi '{saveDir}' tidak ditemukan. Akan dibuat folder baru.")
        try:
            noDirs = [basename(saveDir)]
            dirpath = dirname(abspath(saveDir))

            while not exists(dirpath):
                noDirs.append(basename(dirpath))
                dirpath = abspath(join(dirpath, ".."))
            
            for i in range(len(noDirs)-1 , -1,-1):
                dirpath = abspath(join(dirpath, noDirs[i]))
                mkdir(dirpath)
        except Exception:
            print(f"\033[91mERROR:\033[0m Tidak bisa membuat folder {saveDir}. Pastikan anda memiliki akses dan nama folder valid.")

            return False
    
    if not isdir(saveDir):
        print(f"\033[91mERROR:\033[0m Lokasi '{saveDir}' bukan merupakan folder.")
        return False

    if not access(saveDir, W_OK):
        print(f"\033[91mERROR:\033[0m Lokasi '{saveDir}' tidak bisa ditulis. Pastikan anda memiliki akses.")
        return False

    database = readDatabase()
    isChangeApply = True
    isChangePartial = False

    for i in range(database["numTable"]):
        tableName = database["tableName"][i]
        fileName = tableName + ".csv"
        filePath = abspath(join(saveDir, fileName))
        tableData = database["data"][tableName]

        if (access(filePath, W_OK) or not exists(filePath)):
            file = open(filePath, "w")
            for j in range(tableData["col_number"]):
                file.write(tableData["columnName"][j])
                if j != (tableData["col_number"] - 1):
                    file.write(";")
                else:
                    file.write("\n")

            for j in range(tableData["row_number"]):
                for k in range(tableData["col_number"]):
                    file.write(tableData["data"][j][tableData["columnName"][k]])
                    if k != (tableData["col_number"] - 1):
                        file.write(";")
                    else:
                        file.write("\n")
            
            isChangePartial = True
            file.close()
        else:
            isChangeApply = False
            print(f"\033[91mERROR:\033[0m File '{filePath}' tidak bisa ditulis. Pastikan anda memiliki akses.")

    if isChangeApply:
        resetChanged()
    elif isChangePartial:
        print("\033[33mSebagian file telah berhasil tersimpan.\033[0m\n")
    else:
        print("\033[91mGagal menyimpan seluruh file.\033[0m\n")

    return isChangeApply