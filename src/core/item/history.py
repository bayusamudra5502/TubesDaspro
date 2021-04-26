# Module history
# Modul ini berisi riwayat dari
# peminjaman gadget, pengambilan gadget, dan
# pengambilan consumable

from core.database import applyChange, getTable #mengimpor fungsi applyChange dan getTable
from core.auth import isAdminRole #mengimpor fungsi isAdminRole

def histPinjamGadget(username):  #Fungsi utama untuk Peminjaman
    if isAdminRole(username):    #Memastikan bahwa role dari user adalah admin
        dataBorrowHist = getTable("gadget_borrow_history") #Membaca data Peminjaman Gadget dari database
        listuser = getTable("user")  #Membaca data user dari database
        itemList = getTable("gadget")#Membaca data Gadget dari database
        # Memberi nama pada setiap frasa yang digunakan
        phrase1="Peminjaman"
        phrase2="Peminjam"
        phrase3="Gadget"

        #sort tanggal
        sortedtanggal=[[0 for i in range (2)] for j in range (int(dataBorrowHist['row_number']))]
        for i in range (int(dataBorrowHist['row_number'])):
            sortedtanggal[i][0]=int(dataBorrowHist['data'][i]['tanggal_peminjaman'][6]+dataBorrowHist['data'][i]['tanggal_peminjaman'][7]+dataBorrowHist['data'][i]['tanggal_peminjaman'][8]+dataBorrowHist['data'][i]['tanggal_peminjaman'][9]+dataBorrowHist['data'][i]['tanggal_peminjaman'][3]+dataBorrowHist['data'][i]['tanggal_peminjaman'][4]+dataBorrowHist['data'][i]['tanggal_peminjaman'][0]+dataBorrowHist['data'][i]['tanggal_peminjaman'][1])
            sortedtanggal[i][1]=str(dataBorrowHist['data'][i]['id']) #menyimpan id peminjaman
        sortedtanggal.sort(reverse=True) #list telah disort descending berdasarkan tanggal
        banyakdata=len(sortedtanggal)
        print(f"\033[91mMenampilkan 5 riwayat\033[0m \033[91m{phrase1}\033[0m \033[\033[91mterbaru\033[0m")
        print()
        # Menampilkan 5 riwayat peminjaman terbaru"
        for i in range (banyakdata):  # Perulangan berdasarkan variabel banyak data
            for j in range (int(dataBorrowHist['row_number'])):
                if (dataBorrowHist['data'][j]['id'])==str(sortedtanggal[i][1]): #mencocokkan id peminjaman
                    print(f"\033[92mID {phrase1}       \033[0m: {dataBorrowHist['data'][j]['id']}")
                    for k in range (int(listuser['row_number'])): #mencocokkan nama peminjam
                        if (listuser['data'][k]['id'])==(dataBorrowHist['data'][j]['id_peminjam']):#Mencocokkan id user dengan id peminjam
                            print(f"\033[92mNama {phrase2}       \033[0m: {listuser['data'][k]['nama']}") #Mencetak hasilnya
                    for l in range (int(itemList['row_number'])): 
                        if (itemList['data'][l]['id'])== (dataBorrowHist['data'][j]['id_gadget']): #mencocokkan nama gadget
                            print(f"\033[92mNama {phrase3}         \033[0m: {itemList['data'][l]['nama']}")#Menampilkan nama peminjam
                    print(f"\033[92mTanggal {phrase1}  \033[0m: {dataBorrowHist['data'][j]['tanggal_peminjaman']}")#menampilkan tanggal peminjaman
                    print(f"\033[92mJumlah              \033[0m: {dataBorrowHist['data'][j]['jumlah']}")#menampilkan jumlah yg dipinjam
                    print(f"\033[92mJumlah Dikembalikan \033[0m: {dataBorrowHist['data'][j]['jumlah_kembali']}")#menampilkan jumlah yang dikembalikan
                    print(f"\033[92mSudah Kembali Semua \033[0m: {dataBorrowHist['data'][j]['is_returned']}")#menampilkan pesan apakah semua sudah dikembalikan
            print()
            if (i%5==4): # fungsi jika database lebih dari 5 akan ditampilkan entry selanjutnya
                lanjut=input("\033[93mIngin menampilkan entry selanjutnya? (Y/N): \033[0m")
                if lanjut.lower()=="y":
                    print()
                    continue
                else:
                    break
        applyChange(dataBorrowHist, "gadget_borrow_history") #menyimpan data
    else: #jika yang mengakses adalah user
        print("\033[92mHanya admin yang dapat melakukan fitur riwayat ini\033[0m")
    return isAdminRole


def histKembaliGadget(username): #Fungsi utama riwayat pengembalian
    if isAdminRole(username): # memastikan bahwa yang mengakses adalah admin
        dataReturnHist = getTable("gadget_return_history") #Membaca data pengembalian gadget
        dataBorrowHist = getTable("gadget_borrow_history") #Membaca data Peminjaman gadget
        listuser = getTable("user")  #Membaca data user
        itemList = getTable("gadget")#Membaca data gadget
        #Memberi nama pada setiap frasa yang digunakan
        phrase1="Pengembalian"
        phrase2="Pengembali"
        phrase3="Gadget"

        #sort tanggal
        sortedtanggal=[[0 for i in range (2)] for j in range (int(dataReturnHist['row_number']))]
        for i in range (int(dataReturnHist['row_number'])):
            sortedtanggal[i][0]=int(dataReturnHist['data'][i]['tanggal_pengembalian'][6]+dataReturnHist['data'][i]['tanggal_pengembalian'][7]+dataReturnHist['data'][i]['tanggal_pengembalian'][8]+dataReturnHist['data'][i]['tanggal_pengembalian'][9]+dataReturnHist['data'][i]['tanggal_pengembalian'][3]+dataReturnHist['data'][i]['tanggal_pengembalian'][4]+dataReturnHist['data'][i]['tanggal_pengembalian'][0]+dataReturnHist['data'][i]['tanggal_pengembalian'][1])
            sortedtanggal[i][1]=str(dataReturnHist['data'][i]['id']) #menyimpan id peminjaman
        sortedtanggal.sort(reverse=True) #list telah disort descending berdasarkan tanggal
        banyakdata=len(sortedtanggal)
        print(f"\033[91mMenampilkan 5 riwayat\033[0m \033[91m{phrase1}\033[0m \033[91mterbaru\033[0m")
        print()
        #Menampilkan 5 riwayat pengembalian terbaru
        for i in range (banyakdata):
            for j in range (int(dataReturnHist['row_number'])):
                if (dataReturnHist['data'][j]['id'])==str(sortedtanggal[i][1]): #mencocokkan id peminjaman
                    print(f"\033[92mID {phrase1}     \033[0m: {dataReturnHist['data'][j]['id']}") #menmpilkan id pengembalian
                    for k in range(int(dataBorrowHist['row_number'])):
                        if (dataBorrowHist['data'][k]['id']) == (dataReturnHist['data'][j]['id_peminjaman']): #mencocokkan id peminjaman
                            for l in range (int(listuser['row_number'])): #mencocokkan nama peminjam
                                if (listuser['data'][l]['id'])==(dataBorrowHist['data'][k]['id_peminjam']): # mencocokkan nama peminjam
                                    print(f"\033[92mNama {phrase2}     \033[0m: {listuser['data'][l]['nama']}")# Menampilkan nama pengembali
                            for m in range (int(itemList['row_number'])):
                                if (itemList['data'][m]['id'])== (dataBorrowHist['data'][k]['id_gadget']): #mencocokkan nama gadget
                                    print(f"\033[92mNama {phrase3}         \033[0m: {itemList['data'][m]['nama']}") #menampilkan nama gadget
                            print(f"\033[92mTanggal {phrase1}\033[0m: {dataReturnHist['data'][j]['tanggal_pengembalian']}") #menampilkan tanggal pengembalian
                            print(f"\033[92mJumlah              \033[0m: {dataReturnHist['data'][j]['jumlah']}")#menampilkan jumlah yang dikembalikan
            print()
            if (i%5==4): #fungsi untuk menampilkan 5 riwayat berikutnya
                lanjut=input("\033[93mIngin menampilkan entry selanjutnya? (Y/N):\033[0m ")
                if lanjut.lower()=="y":
                    print()
                    continue
                else:
                    break
        applyChange(dataReturnHist, "gadget_return_history") #menyimpan data
    else: #jika yang mengakses adalah user
        print("\033[92mHanya admin yang dapat melakukan fitur riwayat ini\033[0m")
    return isAdminRole


def histAmbilConsumable(username): #Fungsi utama Riwayat Pengambilan
    if isAdminRole(username): #memastikan yang mengakses hanyalah admin
        dataConsumableHist = getTable("consumable_history")#membaca data consumable
        listuser = getTable("user") #membaca data user
        itemList = getTable("consumable")#memvaca data consumable
        #menampilkan frasa
        phrase1="Pengambilan"
        phrase2="Pengambil"
        phrase3="Consumable"

        #sort tanggal
        sortedtanggal=[[0 for i in range (2)] for j in range (int(dataConsumableHist['row_number']))]
        for i in range (int(dataConsumableHist['row_number'])):
            sortedtanggal[i][0]=int(dataConsumableHist['data'][i]['tanggal_pengambilan'][6]+dataConsumableHist['data'][i]['tanggal_pengambilan'][7]+dataConsumableHist['data'][i]['tanggal_pengambilan'][8]+dataConsumableHist['data'][i]['tanggal_pengambilan'][9]+dataConsumableHist['data'][i]['tanggal_pengambilan'][3]+dataConsumableHist['data'][i]['tanggal_pengambilan'][4]+dataConsumableHist['data'][i]['tanggal_pengambilan'][0]+dataConsumableHist['data'][i]['tanggal_pengambilan'][1])
            sortedtanggal[i][1]=str(dataConsumableHist['data'][i]['id']) #menyimpan id peminjaman
        sortedtanggal.sort(reverse=True) #list telah disort descending berdasarkan tanggal
        banyakdata=len(sortedtanggal)
        print(f"\033[91mMenampilkan 5 riwayat\033[0m \033[91m{phrase1}\033[0m \033[91mterbaru\033[0m")
        print()
        #menampilkan 5 riwayat pengambilan terbaru
        for i in range (banyakdata):
            for j in range (int(dataConsumableHist['row_number'])):
                if (dataConsumableHist['data'][j]['id'])==str(sortedtanggal[i][1]): #mencocokkan id peminjaman
                    print(f"\033[92mID {phrase1}     \033[0m: {dataConsumableHist['data'][j]['id']}")#Menampilkan id riwayatconsumable
                    for k in range (int(listuser['row_number'])): #mencocokkan nama peminjam
                        if (listuser['data'][k]['id'])==(dataConsumableHist['data'][j]['id_pengambil']):#mencocokkan id pengambilan
                            print(f"\033[92mNama {phrase2}     \033[0m: {listuser['data'][k]['nama']}")#menampiljan nama pengambil
                    for l in range (int(itemList['row_number'])):
                        if (itemList['data'][l]['id'])== (dataConsumableHist['data'][j]['id_consumable']): #mencocokkan nama gadget
                            print(f"\033[92mNama {phrase3}    \033[0m: {itemList['data'][l]['nama']}")#menampilkan nama consumable
                    print(f"\033[92mTanggal {phrase1}\033[0m: {dataConsumableHist['data'][j]['tanggal_pengambilan']}")#menampilkan tanggal pengambilan
                    print(f"\033[92mJumlah             \033[0m: {dataConsumableHist['data'][j]['jumlah']}")#menampilkan jumlah pengambilan
            print()
            if (i%5==4):#menampilkan 5 entry selanjutnya
                lanjut=input("\033[93mIngin menampilkan entry selanjutnya? (Y/N): \033[0m")
                if lanjut.lower()=="y":
                    print()
                    continue
                else:
                    break
        applyChange(dataConsumableHist, "consumable_history")#menyimpan data
    else:#jika yang mengakses adalah user
        print("\033[92mHanya admin yang dapat melakukan fitur riwayat ini\033[0m")
    return isAdminRole

