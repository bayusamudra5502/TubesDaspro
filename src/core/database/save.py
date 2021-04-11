# Module save
# Modul ini merupakan implementasi dari fitur
# Penyimpanan pada program ini.

from .database import readDatabase, resetChanged
from os.path import join, abspath, isdir, exists
from os import W_OK, access

def save(saveDir):
    """Fungsi ini akan menyimpan semua data pada database di
    folder saveDir dalam format csv. Jika proses berhasil,
    fungsi mengembalikan True"""

    if not exists(saveDir):
        print(f"Lokasi '{saveDir}' tidak ditemukan.")
        return False

    if not isdir(saveDir):
        print(f"Lokasi '{saveDir}' bukan merupakan folder.")
        return False
    
    if not access(saveDir, W_OK):
        print(f"Lokasi '{saveDir}' tidak bisa ditulis. Pastikan anda memiliki akses.")
        return False

    database = readDatabase()

    for i in range(database["numTable"]):
        tableName = database["tableName"][i]
        fileName = tableName + ".csv"
        filePath = abspath(join(saveDir, fileName))
        tableData = database["data"][tableName]

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

    resetChanged()
    return True