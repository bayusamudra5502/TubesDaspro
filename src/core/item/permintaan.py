# Module permintaan
# modul ini berisi implementasi dari fitur
# permintaan consumable (F10)

from core.database import applyChange, getTable
from core.auth import isUserRole
from core.auth import isValidUser
from core.util import generateNextID
from core.auth import getUserID


def mintaConsumable(username):
    if isValidUser(username):
        if isUserRole(username):
            dataConsumable = getTable("consumable")
            dataConsumableHist = getTable("consumable_history")
            id_item = (input('Masukan ID item {:>4s}'.format(': ')))
            notFound=True #Asumsi item tidak ditemukan

            for i in range(int(dataConsumable['row_number'])):
                if (id_item == dataConsumable['data'][i]['id']):
                    notFound = False
                    jumlah_permintaan = int(input("Jumlah            : "))
                    tanggal_permintaan = input("Tanggal permintaan: ")
                    if (int(dataConsumable['data'][i]['jumlah'])) > jumlah_permintaan:                    
                        newConsumable =  (int(dataConsumable['data'][i]['jumlah']))-(jumlah_permintaan)
                        dataConsumable['data'][i]['jumlah'] = str(newConsumable)
                        print()
                        print("Item " + str(dataConsumable['data'][i]['nama'])+ " (x" + str(jumlah_permintaan) +") telah berhasil diambil!")
                        
                        if getUserID(username):
                            nextIndex = dataConsumableHist['row_number']
                            lastIndext = dataConsumableHist['row_number']-1
                            lastId = dataConsumableHist['data'][lastIndext]['id']
                            id = (generateNextID(lastId))
                            if generateNextID(lastId):
                                dataConsumableHist['data'][nextIndex] = \
                                {
                                    'id': id,
                                    'id_pengambil': getUserID,
                                    'id_consumable': id_item,
                                    'tanggal_pengambilan': tanggal_permintaan,
                                    'jumlah': jumlah_permintaan,
                                }
                        applyChange(dataConsumableHist, 'consumable_history')
                   
                    elif (int(dataConsumable['data'][i]['jumlah'])) == jumlah_permintaan:
                        newConsumable1 =  (int(dataConsumable['data'][i]['jumlah']))
                        dataConsumable['data'][i]['jumlah'] = str(newConsumable1)
                        print()
                        print("Item " + str(dataConsumable['data'][i]['nama'])+ " (x" + str(jumlah_permintaan) +") telah berhasil diambil!")
                        
    
            if notFound: #item tidak ditemukan
                print("Tidak ada item dengan ID tersebut!")
            
            applyChange(dataConsumable, "consumable")
            applyChange(dataConsumableHist, "consumable_history")
        else:
            print("silakan lakukan login sebagai user untuk menjalankan perintah ini")
        return isUserRole
    return isValidUser



