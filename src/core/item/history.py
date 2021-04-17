# Module history
# Modul ini berisi riwayat dari
# peminjaman gadget, pengambilan gadget, dan
# pengambilan consumable

from core.database import applyChange, getTable
from core.auth import isAdminRole

def histPinjamGadget(username):
    if isAdminRole:
        dataBorrowHist = getTable("gadget_borrow_history")
        listuser = getTable("user")
        itemList = getTable("gadget")

        phrase1="Peminjaman"
        phrase2="Peminjam"
        phrase3="Gadget"

        #sort tanggal
        sortedtanggal=[[0 for i in range (2)] for j in range (int(dataBorrowHist['row_number']))]
        for i in range (int(dataBorrowHist['row_number'])):
            sortedtanggal[i][0]=int(dataBorrowHist['data'][i]['tanggal_peminjaman'][6]+dataBorrowHist['data'][i]['tanggal_peminjaman'][7]+dataBorrowHist['data'][i]['tanggal_peminjaman'][8]+dataBorrowHist['data'][i]['tanggal_peminjaman'][9]+dataBorrowHist['data'][i]['tanggal_peminjaman'][3]+dataBorrowHist['data'][i]['tanggal_peminjaman'][4]+dataBorrowHist['data'][i]['tanggal_peminjaman'][0]+dataBorrowHist['data'][i]['tanggal_peminjaman'][1])
            sortedtanggal[i][1]=int(dataBorrowHist['data'][i]['id']) #menyimpan id peminjaman
        sortedtanggal.sort(reverse=True) #list telah disort descending berdasarkan tanggal
        banyakdata=len(sortedtanggal)
        print(f"Menampilkan 5 riwayat {phrase1} terbaru\n")

        for i in range (banyakdata):
            for j in range (int(dataBorrowHist['row_number'])):
                if (dataBorrowHist['data'][j]['id'])==str(sortedtanggal[i][1]): #mencocokkan id peminjaman
                    print(f"ID {phrase1}: {dataBorrowHist['data'][j]['id']}")
                    for k in range (int(listuser['row_number'])): #mencocokkan nama peminjam
                        if (listuser['data'][k]['id'])==(dataBorrowHist['data'][j]['id_peminjam']):
                            print(f"Nama {phrase2}: {listuser['data'][k]['nama']}")
                    for l in range (int(itemList['row_number'])):
                        if (itemList['data'][l]['id'])== (dataBorrowHist['data'][j]['id_gadget']): #mencocokkan nama gadget
                            print(f"Nama {phrase3}: {itemList['data'][l]['nama']}")
                    print(f"Tanggal {phrase1}: {dataBorrowHist['data'][j]['tanggal_peminjaman']}")
                    print(f"Jumlah: {dataBorrowHist['data'][j]['jumlah']}")
            print()
            if (i%5==4):
                lanjut=input("Ingin menampilkan entry selanjutnya? (Y/N): ")
                if lanjut.lower()=="y":
                    print()
                    continue
                else:
                    break
        applyChange(dataBorrowHist, "gadget_borrow_history")
    else:
        print("Hanya admin yang dapat melakukan fitur riwayat ini")
    return isAdminRole


def histKembaliGadget(username):
    if isAdminRole(username):
        dataReturnHist = getTable("gadget_return_history")
        listuser = getTable("user")
        itemList = getTable("gadget")

        phrase1="Pengembalian"
        phrase2="Pengembali"
        phrase3="Gadget"

        #sort tanggal
        sortedtanggal=[[0 for i in range (2)] for j in range (int(dataReturnHist['row_number']))]
        for i in range (int(dataReturnHist['row_number'])):
            sortedtanggal[i][0]=int(dataReturnHist['data'][i]['tanggal_pengembalian'][6]+dataReturnHist['data'][i]['tanggal_pengembalian'][7]+dataReturnHist['data'][i]['tanggal_pengembalian'][8]+dataReturnHist['data'][i]['tanggal_pengembalian'][9]+dataReturnHist['data'][i]['tanggal_pengembalian'][3]+dataReturnHist['data'][i]['tanggal_pengembalian'][4]+dataReturnHist['data'][i]['tanggal_pengembalian'][0]+dataReturnHist['data'][i]['tanggal_pengembalian'][1])
            sortedtanggal[i][1]=int(dataReturnHist['data'][i]['id']) #menyimpan id peminjaman
        sortedtanggal.sort(reverse=True) #list telah disort descending berdasarkan tanggal
        banyakdata=len(sortedtanggal)
        print(f"Menampilkan 5 riwayat {phrase1} terbaru\n")

        for i in range (banyakdata):
            for j in range (int(dataReturnHist['row_number'])):
                if (dataReturnHist['data'][j]['id'])==str(sortedtanggal[i][1]): #mencocokkan id peminjaman
                    print(f"ID {phrase1}     : {dataReturnHist['data'][j]['id']}")
                    for k in range (int(listuser['row_number'])): #mencocokkan nama peminjam
                        if (listuser['data'][k]['id'])==(dataReturnHist['data'][j]['id_pengembali']):
                            print(f"Nama {phrase2}     : {listuser['data'][k]['nama']}")
                    for l in range (int(itemList['row_number'])):
                        if (itemList['data'][l]['id'])== (dataReturnHist['data'][j]['id_gadget']): #mencocokkan nama gadget
                            print(f"Nama {phrase3}    : {itemList['data'][l]['nama']}")
                    print(f"Tanggal {phrase1}: {dataReturnHist['data'][j]['tanggal_pengembalian']}")
                    print(f"Jumlah             : {dataReturnHist['data'][j]['jumlah']}")
            print()
            if (i%5==4):
                lanjut=input("Ingin menampilkan entry selanjutnya? (Y/N): ")
                if lanjut.lower()=="y":
                    print()
                    continue
                else:
                    break
        applyChange(dataReturnHist, "gadget_return_history")
    else:
        print("Hanya admin yang dapat melakukan fitur riwayat ini")
    return isAdminRole


def histAmbilConsumable(username):
    if isAdminRole(username):
        dataConsumableHist = getTable("consumable_history")
        listuser = getTable("user")
        itemList = getTable("consumable")

        phrase1="Pengambilan"
        phrase2="Pengambil"
        phrase3="Consumable"

        #sort tanggal
        sortedtanggal=[[0 for i in range (2)] for j in range (int(dataConsumableHist['row_number']))]
        for i in range (int(dataConsumableHist['row_number'])):
            sortedtanggal[i][0]=int(dataConsumableHist['data'][i]['tanggal_pengambilan'][6]+dataConsumableHist['data'][i]['tanggal_pengambilan'][7]+dataConsumableHist['data'][i]['tanggal_pengambilan'][8]+dataConsumableHist['data'][i]['tanggal_pengambilan'][9]+dataConsumableHist['data'][i]['tanggal_pengambilan'][3]+dataConsumableHist['data'][i]['tanggal_pengambilan'][4]+dataConsumableHist['data'][i]['tanggal_pengambilan'][0]+dataConsumableHist['data'][i]['tanggal_pengambilan'][1])
            sortedtanggal[i][1]=int(dataConsumableHist['data'][i]['id']) #menyimpan id peminjaman
        sortedtanggal.sort(reverse=True) #list telah disort descending berdasarkan tanggal
        banyakdata=len(sortedtanggal)
        print(f"Menampilkan 5 riwayat {phrase1} terbaru\n")

        for i in range (banyakdata):
            for j in range (int(dataConsumableHist['row_number'])):
                if (dataConsumableHist['data'][j]['id'])==str(sortedtanggal[i][1]): #mencocokkan id peminjaman
                    print(f"ID {phrase1}     : {dataConsumableHist['data'][j]['id']}")
                    for k in range (int(listuser['row_number'])): #mencocokkan nama peminjam
                        if (listuser['data'][k]['id'])==(dataConsumableHist['data'][j]['id_pengambil']):
                            print(f"Nama {phrase2}     : {listuser['data'][k]['nama']}")
                    for l in range (int(itemList['row_number'])):
                        if (itemList['data'][l]['id'])== (dataConsumableHist['data'][j]['id_consumable']): #mencocokkan nama gadget
                            print(f"Nama {phrase3}    : {itemList['data'][l]['nama']}")
                    print(f"Tanggal {phrase1}: {dataConsumableHist['data'][j]['tanggal_pengambilan']}")
                    print(f"Jumlah             : {dataConsumableHist['data'][j]['jumlah']}")
            print()
            if (i%5==4):
                lanjut=input("Ingin menampilkan entry selanjutnya? (Y/N): ")
                if lanjut.lower()=="y":
                    print()
                    continue
                else:
                    break
        applyChange(dataConsumableHist, "consumable_history")
    else:
        print("Hanya admin yang dapat melakukan fitur riwayat ini")
    return isAdminRole

    