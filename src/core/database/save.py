# Module save
# Modul ini merupakan implementasi dari fitur
# Penyimpanan pada program ini.

from .database import readDatabase
from os.path import join, abspath

def save(saveDir):
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
        
        file.close()