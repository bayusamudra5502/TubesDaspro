# Module Pengembalian
# Modul ini berisi implementasi dari
# fitur peminjaman gadget (F08)

from core.database import applyChange, getTable
from core.auth import getUserID
from core.auth import isUserRole
from core.util import generateNextID
from core.util import isValidTanggal

def peminjamanGadget(username):
    if getUserID(username):
        if isUserRole(username):
            dataGadget = getTable("gadget")
            dataPinjamGadget = getTable("gadget_borrow_history")
            id_item = input("Masukan ID item: ")
            id_peminjam = username
            tanggal_pinjam = input("Tanggal peminjaman: ")
            jumlah_pinjam = int(input("Jumlah peminjaman: "))
            for i in range(dataGadget["row_number"]):
                if(dataGadget["data"][i]["id"] == id):
                    if(int(dataGadget["data"][i]["jumlah"]) > 0) and (int(dataGadget["data"][i]["jumlah"]) >= jumlah_pinjam):
                        newGadget = int(dataGadget["data"][i]["jumlah"]) - jumlah_pinjam
                        dataGadget["data"][i]["jumlah"] = str(newGadget)
                        print("Item " + str(dataGadget["data"][dataGadget][i]["nama"]) + " (" + str(dataGadget["data"][i]["jumlah"]) + ") " "berhasil dipinjam")
                        dataPinjamGadget["data"][dataPinjamGadget["numRows"]]["id"] = generateNextID
                        dataPinjamGadget["data"][dataPinjamGadget["numRows"]]["id_peminjam"] = id_peminjam
                        dataPinjamGadget["data"][dataPinjamGadget["numRows"]]["id_gadget"] = id_item
                        dataPinjamGadget["data"][dataPinjamGadget["numRows"]]["tanggal_peminjaman"] = tanggal_pinjam
                        dataPinjamGadget["data"][dataPinjamGadget["numRows"]]["jumlah"] = jumlah_pinjam
                    else:   #(dataGadget["data"][i]["jumlah"]) <= 0) or (dataGadget["data"][i]["jumlah"] < jumlah_pinjam)
                        print("Jumlah yang ingin dipinjam melebihi stok item. Stok sekarang: " + str(dataGadget["data"][i]["jumlah"]))
                else:
                    print("Tidak ada item dengan ID tersebut!")
            applyChange(dataGadget, "gadget")
            applyChange(dataPinjamGadget, "gadget_borrow_history")
        return isUserRole
    return getUserID