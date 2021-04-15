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
                for k in range (len(listuser)): #mencocokkan nama peminjam
                    if listuser[k][0]==listhistory[j][1]:
                        print(f"Nama {phrase2}: {listuser[k][2]}")
                for l in range (len(itemList)):
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
    pass

def histAmbilConsumable(username):
    # Fitur F13
    dataConsumableHist = getTable("consumable_history")
    pass