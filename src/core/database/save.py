# Module save
# Modul ini merupakan implementasi dari fitur
# Penyimpanan pada program ini.

from typing import cast
from .database import readDatabase, resetChanged
from os.path import join, abspath, isdir, exists
from os import W_OK, access, mkdir

def save(saveDir):
    """Fungsi ini akan menyimpan semua data pada database di
    folder saveDir dalam format csv. Jika proses berhasil,
    fungsi mengembalikan True"""
    
    if not exists(saveDir):
        print(f"\033[33mPERINGATAN:\033[0m Lokasi '{saveDir}' tidak ditemukan. Akan dibuat folder baru.")
        try:
            mkdir(saveDir)
        except Exception:
            print(f"\033[91mERROR:\033[0m Tidak bisa membuat folder {saveDir}. Pastikan anda memiliki akses.")
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