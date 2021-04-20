# Module Pengembalian
# Modul ini berisi implementasi dari
# fitur peminjaman gadget (F08)

from core.database import applyChange, getTable
from core.auth import isValidUser
from core.auth import isUserRole
from core.util import generateNextID
from core.auth import getUserID
from core.util import isValidTanggal

def peminjamanGadget(username):
    if isValidUser(username):
        if isUserRole(username):
            dataGadget = getTable("gadget")
            dataPinjamGadget = getTable("gadget_borrow_history")
            dataKembaliGadget = getTable("gadget_return_history")
            # Meminta input
            id_item = input("Masukan ID item: ")
            tanggal_pinjam = input("Tanggal peminjaman: ")
            jumlah_pinjam = int(input("Jumlah peminjaman: "))
            jumlah_gadget_kembali = 0
            jumlah_gadget_pinjam = 0
            is_returned = False
            # Validasi dan modifikasi data
            if jumlah_pinjam > 0:
                if isValidTanggal(tanggal_pinjam):
                    for i in range(dataKembaliGadget["row_number"]):
                        if(dataKembaliGadget["data"][i]["id"] == id_item):
                            jumlah_gadget_kembali = jumlah_gadget_kembali + int(dataKembaliGadget["data"][i]["jumlah"])
                        else:   # dataKembaliGadget["data"][i]["id"] != id_item
                            break
                    for i in range(dataPinjamGadget["row_number"]):
                        if(dataPinjamGadget["data"][i]["id"] == id_item):
                            jumlah_gadget_pinjam = jumlah_gadget_pinjam + int(dataPinjamGadget["data"][i]["jumlah"])
                        else:   # dataPinjamGadget["data"][i]["id"] != id_item
                            break
                    if(jumlah_gadget_kembali == jumlah_gadget_pinjam):
                        for i in range(dataGadget["row_number"]):
                            if(dataGadget["data"][i]["id"] == id_item):
                                if(int(dataGadget["data"][i]["jumlah"]) > 0) and (int(dataGadget["data"][i]["jumlah"]) >= jumlah_pinjam):
                                    newGadget = int(dataGadget["data"][i]["jumlah"]) - (jumlah_pinjam)
                                    dataGadget["data"][i]["jumlah"] = str(newGadget)
                                    print("Item " + str(dataGadget["data"][dataGadget][i]["nama"]) + " (" + str(dataGadget["data"][i]["jumlah"]) + ") " "berhasil dipinjam")
                                    applyChange(dataGadget, "gadget")
                                    if getUserID(username):
                                        nextIndex = dataPinjamGadget["row_number"]
                                        lastIndext = dataPinjamGadget["row_number"]-1
                                        lastID = dataPinjamGadget["data"][lastIndext]["id"]
                                        id1 = (generateNextID(lastID))
                                        if generateNextID(lastID):
                                            dataPinjamGadget["data"][nextIndex] = \
                                            {
                                            "id": id1,
                                            "id_peminjam": str(getUserID(username)),
                                            "id_gadget": id_item,
                                            "tanggal_peminjaman": tanggal_pinjam,
                                            "jumlah": str(jumlah_pinjam),
                                            "is_returned": str(is_returned),
                                            }
                                        applyChange(dataPinjamGadget, "gadget_borrow_history")
                                    return getUserID
                                else:   #(dataGadget["data"][i]["jumlah"]) <= 0) or (dataGadget["data"][i]["jumlah"] < jumlah_pinjam)
                                    print("Jumlah yang ingin dipinjam melebihi stok item. Stok sekarang: " + str(dataGadget["data"][i]["jumlah"]))
                            else:   # dataGadget["data"][i]["id"] != id_item
                                print("Tidak ada item dengan ID tersebut!")
                    else:  # jumlah_gadget_kembali != jumlah_gadget_pinjam 
                        print("Kembalikan item dari peminjaman sebelumnya untuk dapat meminjam kembali")
                else:
                    print("Masukan tanggal tidak valid, silakan masukan format tanggal yang valid")
                return isValidTanggal
            else:   # jumlah_pinjam <= 0
                print("Jumlah peminjaman harus lebih besar dari nol")
        else:
            print("Silakan lakukan login sebagai user untuk menjalankan perintah ini")
        return isUserRole
    return isValidUser