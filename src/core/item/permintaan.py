# Module permintaan
# modul ini berisi implementasi dari fitur
# permintaan consumable (F10)

from core.database import applyChange, getTable
from core.auth import isValidUser

def mintaConsumable(username):
    dataConsumable = getTable("consumable")
    if isValidUser:
        id_item = (input('Masukan ID item {:>4s}'.format(': ')))
        notFound=True

        for i in range(int(dataConsumable['row_number'])):
            if (id_item == dataConsumable['data'][i]['id']):
                jumlah_permintaan = int(input("Jumlah            : "))
                tanggal_permintaan = input("Tanggal permintaan: ")
                if (int(dataConsumable['data'][i]['jumlah'])) > jumlah_permintaan:
                    newConsumable =  (int(dataConsumable['data'][i]['jumlah']))-(jumlah_permintaan)
                    dataConsumable['data'][i]['jumlah'] = str(newConsumable)
                    print()
                    print("Item " + str(dataConsumable['data'][i]['nama'])+ " (x" + str(jumlah_permintaan) +") telah berhasil diambil!")
                
                elif (int(dataConsumable['data'][i]['jumlah'])) == jumlah_permintaan:
                    newConsumable1 =  (int(dataConsumable['data'][i]['jumlah']))
                    dataConsumable['data'][i]['jumlah'] = str(newConsumable1)
                    print()
                    print("Item " + str(dataConsumable['data'][i]['nama'])+ " (x" + str(jumlah_permintaan) +") telah berhasil diambil!")
    else:
        print("silakan lakukan login terlebih dahulu untuk menjalankan perintah lain")
    applyChange(dataConsumable, "consumable")
    pass



