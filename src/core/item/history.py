# Module history
# Modul ini berisi riwayat dari
# peminjaman gadget, pengambilan gadget, dan
# pengambilan consumable

from core.database import applyChange, getTable
from core.auth import isAdminRole

def histPinjamGadget(username):
    # Fitur F11
    listhistory = getTable("gadget_borrow_history")
    listuser = getTable("user")
    itemList = getTable("gadget")

    phrase1="Peminjaman"
    phrase2="Peminjam"
    phrase3="Gadget"
    itemList=itemList[1:]
    listhistory=listhistory[1:]

    #sort tanggal
    sortedtanggal=[[0 for i in range (2)] for j in range (int(listhistory['row_number']))]
    for i in range (int(listhistory['row_number'])):
        sortedtanggal[i][0]=int(listhistory[i][3][6]+listhistory[i][3][7]+listhistory[i][3][8]+listhistory[i][3][9]+listhistory[i][3][3]+listhistory[i][3][4]+listhistory[i][3][0]+listhistory[i][3][1])
        sortedtanggal[i][1]=int(listhistory[i][0]) #menyimpan id peminjaman
    sortedtanggal.sort(reverse=True) #list telah disort descending berdasarkan tanggal
    banyakdata=len(sortedtanggal)
    print(f"Menampilkan 5 riwayat {phrase1} terbaru\n")

    for i in range (banyakdata):
        for j in range (int(listhistory['row_number'])):
            if listhistory['data'][j][0]==str(sortedtanggal[i][1]): #mencocokkan id peminjaman
                print(f"ID {phrase1}: {listhistory[j][0]}")
                for k in range (int(listuser['row_number'])): #mencocokkan nama peminjam
                    if listuser[k][0]==listhistory[j][1]:
                        print(f"Nama {phrase2}: {listuser[k][2]}")
                for l in range (int(itemList['row_number'])):
                    if itemList[l][0]==listhistory[j][2]: #mencocokkan nama gadget
                        print(f"Nama {phrase3}: {itemList[l][1]}")
                print(f"Tanggal {phrase1}: {listhistory[j][3]}")
                print(f"Jumlah: {listhistory[j][4]}")
        print()
        if (i%5==4):
            lanjut=input("Ingin menampilkan entry selanjutnya? (Y/N): ")
            if lanjut.lower()=="y":
                print()
                continue
            else:
                break

    pass

def histKembaliGadget(username):
    # Fitur F12
    dataReturnHist = getTable("gadget_return_history")
    phrase1="Pengembalian"
    phrase2="Pengembali"
    phrase3="Gadget"
    listuser = getTable("user")
    itemList = getTable("gadget")
    itemList=itemList[1:]
    dataReturnHist = dataReturnHist[1:]
    #sort tanggal
    sortedtanggal=[[0 for i in range (2)] for j in range (int(dataReturnHist['row_number']))]
    for i in range (int(dataReturnHist['row_number'])):
        sortedtanggal[i][0]=int(dataReturnHist[i][3][6]+dataReturnHist[i][3][7]+dataReturnHist[i][3][8]+dataReturnHist[i][3][9]+dataReturnHist[i][3][3]+dataReturnHist[i][3][4]+dataReturnHist[i][3][0]+dataReturnHist[i][3][1])
        sortedtanggal[i][1]=int(dataReturnHist[i][0]) #menyimpan id peminjaman
    sortedtanggal.sort(reverse=True) #list telah disort descending berdasarkan tanggal
    banyakdata=len(sortedtanggal)
    print(f"Menampilkan 5 riwayat {phrase1} terbaru\n")

    for i in range (banyakdata):
        for j in range (int(dataReturnHist['row_number'])):
            if dataReturnHist['data'][j][0]==str(sortedtanggal[i][1]): #mencocokkan id peminjaman
                print(f"ID {phrase1}: {dataReturnHist[j][0]}")
                for k in range (int(listuser['row_number'])): #mencocokkan nama peminjam
                    if listuser[k][0]==dataReturnHist[j][1]:
                        print(f"Nama {phrase2}: {listuser[k][2]}")
                for l in range (int(itemList['row_number'])):
                    if itemList[l][0]==dataReturnHist[j][2]: #mencocokkan nama gadget
                        print(f"Nama {phrase3}: {itemList[l][1]}")
                print(f"Tanggal {phrase1}: {dataReturnHist[j][3]}")
                print(f"Jumlah: {dataReturnHist[j][4]}")
        print()
        if (i%5==4):
            lanjut=input("Ingin menampilkan entry selanjutnya? (Y/N): ")
            if lanjut.lower()=="y":
                print()
                continue
            else:
                break

    pass

def histAmbilConsumable(username):
    # Fitur F13
    dataConsumableHist = getTable("consumable_history")
    phrase1="Pengambilan"
    phrase2="Pengambil"
    phrase3="Consumable"
    listuser = getTable("user")
    itemList = getTable("gadget")
    itemList=itemList[1:]
    dataConsumableHist = dataConsumableHist[1:]

    #sort tanggal
    sortedtanggal=[[0 for i in range (2)] for j in range (int(dataConsumableHist['row_number']))]
    for i in range (int(dataConsumableHist['row_number'])):
        sortedtanggal[i][0]=int(dataConsumableHist[i][3][6]+dataConsumableHist[i][3][7]+dataConsumableHist[i][3][8]+dataConsumableHist[i][3][9]+dataConsumableHist[i][3][3]+dataConsumableHist[i][3][4]+dataConsumableHist[i][3][0]+dataConsumableHist[i][3][1])
        sortedtanggal[i][1]=int(dataConsumableHist[i][0]) #menyimpan id peminjaman
    sortedtanggal.sort(reverse=True) #list telah disort descending berdasarkan tanggal
    banyakdata=len(sortedtanggal)
    print(f"Menampilkan 5 riwayat {phrase1} terbaru\n")

    for i in range (banyakdata):
        for j in range (int(dataConsumableHist['row_number'])):
            if dataConsumableHist['data'][j][0]==str(sortedtanggal[i][1]): #mencocokkan id peminjaman
                print(f"ID {phrase1}: {dataConsumableHist[j][0]}")
                for k in range (int(listuser['row_number'])): #mencocokkan nama peminjam
                    if listuser[k][0]==dataConsumableHist[j][1]:
                        print(f"Nama {phrase2}: {listuser[k][2]}")
                for l in range (int(itemList['row_number'])):
                    if itemList[l][0]==dataConsumableHist[j][2]: #mencocokkan nama gadget
                        print(f"Nama {phrase3}: {itemList[l][1]}")
                print(f"Tanggal {phrase1}: {dataConsumableHist[j][3]}")
                print(f"Jumlah: {dataConsumableHist[j][4]}")
        print()
        if (i%5==4):
            lanjut=input("Ingin menampilkan entry selanjutnya? (Y/N): ")
            if lanjut.lower()=="y":
                print()
                continue
            else:
                break

    pass