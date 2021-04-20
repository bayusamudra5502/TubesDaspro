# Module permintaan
# modul ini berisi implementasi dari fitur
# permintaan consumable (F10)

from core.database import applyChange, getTable
from core.auth import isUserRole
from core.auth import isValidUser
from core.util import generateNextID
from core.auth import getUserID
from core.util import isValidTanggal


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
                    if isValidTanggal(tanggal_permintaan):
                        if (int(dataConsumable['data'][i]['jumlah'])) > jumlah_permintaan:                    
                            newConsumable =  (int(dataConsumable['data'][i]['jumlah']))-(jumlah_permintaan)
                            dataConsumable['data'][i]['jumlah'] = str(newConsumable)
                            print()
                            print("Item " + str(dataConsumable['data'][i]['nama'])+ " (x" + str(jumlah_permintaan) +") telah berhasil diambil!")
                            
                            if getUserID(username):
                                nextIndex = dataConsumableHist['row_number']
                                lastIndext = dataConsumableHist['row_number']-1
                                lastId = dataConsumableHist['data'][lastIndext]['id']
                                id1 = (generateNextID(lastId))
                                if generateNextID(lastId):
                                    dataConsumableHist['data'][nextIndex] = \
                                    {
                                        'id': id1,
                                        'id_pengambil': str(getUserID(username)),
                                        'id_consumable': id_item,
                                        'tanggal_pengambilan': tanggal_permintaan,
                                        'jumlah': str(jumlah_permintaan),
                                    }
                                applyChange(dataConsumableHist, 'consumable_history')
                            return getUserID

                        elif (int(dataConsumable['data'][i]['jumlah'])) == jumlah_permintaan:
                            newConsumable1 =  (int(dataConsumable['data'][i]['jumlah']))
                            dataConsumable['data'][i]['jumlah'] = str(newConsumable1)
                            print()
                            print("Item " + str(dataConsumable['data'][i]['nama'])+ " (x" + str(jumlah_permintaan) +") telah berhasil diambil!")
                        
                            if getUserID(username):
                                nextIndex = dataConsumableHist['row_number']
                                lastIndext = dataConsumableHist['row_number']-1
                                lastId = dataConsumableHist['data'][lastIndext]['id']
                                id1 = (generateNextID(lastId))
                                if generateNextID(lastId):
                                    dataConsumableHist['data'][nextIndex] = \
                                    {
                                        'id': id1,
                                        'id_pengambil': str(getUserID(username)),
                                        'id_consumable': id_item,
                                        'tanggal_pengambilan': tanggal_permintaan,
                                        'jumlah': str(jumlah_permintaan),
                                    }
                                applyChange(dataConsumableHist, 'consumable_history')
                            return getUserID
                        else:
                            print()
                            print("Jumlah pengambilan melebihi jumlah item yang ada, silakan kurangi jumlah")
                    else:
                        print()
                        print("Masukan tanggal tidak valid, silakan masukkan tanggal yang valid")
                    return isValidTanggal
        
                    
            if notFound:
                print('id item yang dimasukkan tidak valid silakan coba lagi')
        else:
            print("silakan lakukan login sebagai user untuk menjalankan perintah ini")
        return isUserRole
    return isValidUser



