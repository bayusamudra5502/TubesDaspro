# Module permintaan
# modul ini berisi implementasi dari fitur
# permintaan consumable (F10)

from core.database import applyChange, getTable
from core.auth import isValidUser

def mintaConsumable(username):
    consumabledata = getTable("consumable")
    id_item = input("Masukan ID item   : ")
    jumlah_permintaan = int(input("Jumlah            : "))
    tanggal_permintaan = input("Tanggal permintaan: ")

    for i in range(int(consumabledata['row_number'])):
        if (consumabledata['data'][i]['id'] == id_item):
            if (int(consumabledata['data'][i]['jumlah']))> jumlah_permintaan:
                newConsumable =  (int(consumabledata['data'][i]['jumlah']))-(jumlah_permintaan)
                (consumabledata['data'][i]['jumlah']) = newConsumable
                print()
                print("Item " + str(consumabledata['data'][i]['nama'])+ " (x" + str(jumlah_permintaan) +") telah diambil!!!")
            elif  (int(consumabledata['data'][i]['jumlah'])) == jumlah_permintaan:
                newConsumable1 =  (consumabledata['data'][i]['jumlah'])
                (consumabledata['data'][i]['jumlah']) = newConsumable1  
                print()
                print("Item " + str(consumabledata['data'][i]['nama']) + " (x" + str(jumlah_permintaan) +") telah diambil!!!")
    pass