# Module permintaan
# modul ini berisi implementasi dari fitur
# permintaan consumable (F10)

from core.database import applyChange, getTable
from core.auth import isUserRole
from core.auth import isValidUser

def mintaConsumable(username):
    if isValidUser(username):
        if isUserRole(username):
            dataConsumable = getTable("consumable")
            dataConsumableHist = getTable("consumable_history")
            dataUser = getTable("user")
            id_item = (input('Masukan ID item {:>4s}'.format(': ')))
            notFound=True #Asumsi item tidak ditemukan

            for i in range(int(dataConsumable['row_number'])):
                if (id_item == dataConsumable['data'][i]['id']):
                    notFound = False
                    jumlah_permintaan = int(input("Jumlah            : "))
                    tanggal_permintaan = input("Tanggal permintaan: ")

                    if (int(dataConsumable['data'][i]['jumlah'])) > jumlah_permintaan:                    
                        for j in range (int(dataConsumableHist['row_number'])): #mengecek apakah item sudah pernah dipinjam/ada di inventory
                            if dataConsumableHist['data'][j]['id_pengambil']== dataUser['data'][i]['id'] and dataConsumableHist['data'][j]['id_consumable']==id_item: #mengecek ID user dengan ID item yang dimiliki 
                                dataConsumableHist['data'][j]['jumlah']=str(int(dataConsumableHist['data'][j]['jumlah'])+jumlah_permintaan) #mengubah jumlah item yang telah pernah dipinjam/diambil 
                        
                        newConsumable =  (int(dataConsumable['data'][i]['jumlah']))-(jumlah_permintaan)
                        dataConsumable['data'][i]['jumlah'] = str(newConsumable)
                        print()
                        print("Item " + str(dataConsumable['data'][i]['nama'])+ " (x" + str(jumlah_permintaan) +") telah berhasil diambil!")
                    
                    elif (int(dataConsumable['data'][i]['jumlah'])) == jumlah_permintaan:
                        newConsumable1 =  (int(dataConsumable['data'][i]['jumlah']))
                        dataConsumable['data'][i]['jumlah'] = str(newConsumable1)
                        print()
                        print("Item " + str(dataConsumable['data'][i]['nama'])+ " (x" + str(jumlah_permintaan) +") telah berhasil diambil!")
            if notFound: #item tidak ditemukan
                print("Tidak ada item dengan ID tersebut!")
        else:
            print("silakan lakukan login sebagai user untuk menjalankan perintah ini")
        return isUserRole
    return isValidUser
    applyChange(dataConsumable, "consumable")
    applyChange(dataConsumableHist, "consumable_history")
    pass



