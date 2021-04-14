# Module permintaan
# modul ini berisi implementasi dari fitur
# permintaan consumable (F10)

from core.database import applyChange, getTable
from core.auth import isValidUser

def mintaConsumable(username):
    consumabledata = getTable("consumable")
    line = False
    while not line:
        id_item = input("Masukan ID item   : ")
        jumlah_permintaan = int(input("Jumlah            : "))
        tanggal_permintaan = input("Tanggal permintaan: ")

        for i in range(len(consumabledata)):
            if (consumabledata[i][0] == id_item):
                if (int(consumabledata[i][3])) > jumlah_permintaan:
                    newConsumable = int(consumabledata[i][3])-(jumlah_permintaan)
                    consumabledata[i][3]= newConsumable
                    print()
                    print("item " + str(consumabledata[i][1])+ " (x" + str(jumlah_permintaan) +") telah diambil!!!")
                elif (int(consumabledata[i][3]))== jumlah_permintaan:
                    newConsumable1 = int(consumabledata[i][3])
                    consumabledata[i][3]= newConsumable1  
                    print()
                    print("item " + str(consumabledata[i][1])+ " (x" + str(jumlah_permintaan) +") telah diambil!!!")   
    pass