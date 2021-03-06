# Module permintaan
# modul ini berisi implementasi dari fitur
# permintaan consumable (F10)

from core.database import applyChange, getTable #Mengimpor fungsi applyChange dan getTable
from core.auth import isUserRole                #Mengimpor fungsi isUserRole
from core.auth import isValidUser               #Mengimpor fungsi isValidUser
from core.util import generateNextID            #Mengimpor fungsi generateNextID
from core.auth import getUserID                 #Mengimpor fungsi getUserID
from core.util import isValidTanggal            #Mengimpor fungsi isValidTanggal


def mintaConsumable(username): #Fungsi utama permintaan
    if isValidUser(username):  #Memastikan bahwa user valid
        if isUserRole(username): #Memastikan bahwa yang mengakses adalah user
            dataConsumable = getTable("consumable")                  #Membaca data consumable
            dataConsumableHist = getTable("consumable_history")      #Membaca data consumable history
            id_item = (input('\033[92mMasukan ID item {:>4s}'.format('  : \033[0m'))) #mengnputkan id item
            notFound=True #Asumsi item tidak ditemukan

            for i in range(int(dataConsumable['row_number'])):
                if (id_item == dataConsumable['data'][i]['id']): #mencocokkan id consumble
                    notFound = False #item ditemukan
                    jumlah_permintaan = int(input("\033[92mJumlah            : \033[0m"))#memasukkan jumlah permintaan
                    tanggal_permintaan = input("\33[92mTanggal permintaan: \033[0m")#memasukkan tanggal permintaan

                    if isValidTanggal(tanggal_permintaan): #melakukan validasi tanggal
                        if (int(dataConsumable['data'][i]['jumlah'])) >= jumlah_permintaan: #jika jumlah yg diminta kecil dari database            
                            newConsumable =  (int(dataConsumable['data'][i]['jumlah']))-(jumlah_permintaan)#jumlah pada database berkurang
                            dataConsumable['data'][i]['jumlah'] = str(newConsumable)#data baru setelah jumlah berkurang
                            print() #mencetak hasil keluaran
                            print("\033[36mItem " + str(dataConsumable['data'][i]['nama'])+ " (x" + str(jumlah_permintaan) +") telah berhasil diambil!\033[0m")
                            
                            if getUserID(username): #fungsi untuk mendapatkan id riwayat consumable
                                lastID = "PMT-0" #asumsi awal id ketika data kosong
                                nextIndex = dataConsumableHist["row_number"] #indeks selanjutnya dari data

                                if(dataConsumableHist["row_number"] > 0): #jika jumlah baris > 0
                                    lastIndext = dataConsumableHist["row_number"]-1 #indeks sebelumnya
                                    lastID = dataConsumableHist["data"][lastIndext]["id"] #id dari indeks sebelumnya

                                id1 = (generateNextID(lastID)) #mendapatkan id selanjutnya
                                if generateNextID(lastID): #fungsi mengisi data consumable History
                                    dataConsumableHist['data'][nextIndex] = \
                                    {
                                        'id': id1,
                                        'id_pengambil': str(getUserID(username)),
                                        'id_consumable': id_item,
                                        'tanggal_pengambilan': tanggal_permintaan,
                                        'jumlah': str(jumlah_permintaan),
                                    }

                                applyChange(dataConsumableHist, 'consumable_history') #menyimpan data

                            return getUserID

                        else:#jumlah pengambilan melebihi sistem
                            print()
                            print("\033[36mJumlah pengambilan melebihi jumlah item yang ada, silakan kurangi jumlah\033[0m")
                    else:#masukan tanggal tidak valid
                        print()
                        print("\033[36mMasukan tanggal tidak valid, silakan masukkan tanggal yang valid\033[0m")
                      
            if notFound:#jika item tidak ditemukan
                print('\033[36mid item yang dimasukkan tidak valid silakan coba lagi\033[0m')
        else:#jika yang mengakses adalah admin
            print("\033[36msilakan lakukan login sebagai user untuk menjalankan perintah ini\033[0m")



