# Module Pengembalian
# Modul ini berisi implementasi dari
# fitur peminjaman gadget (F08)

from core.database import applyChange, getTable
from core.auth import getUserID
from core.auth import isUserRole
from core.util import generateNextID
from core.auth import getUserID
from core.util import isValidTanggal

def peminjamanGadget(username):
    if getUserID(username):
        if isUserRole(username):
            dataGadget = getTable("gadget")
            dataPinjamGadget = getTable("gadget_borrow_history")

            # Meminta input
            id_item = input("Masukan ID item    : ")
            tanggal_pinjam = input("Tanggal peminjaman : ")
            jumlah_pinjam = int(input("Jumlah peminjaman  : "))

            is_returned = "FALSE"
            can_borrow = True

            # Validasi dan modifikasi data
            if jumlah_pinjam > 0:
                if isValidTanggal(tanggal_pinjam):

                    # Cek apakah ada yang belum dikembalikan atau belum?
                    for i in range(dataPinjamGadget["row_number"]):
                        if(dataPinjamGadget["data"][i]["is_returned"] == "FALSE")\
                           and (dataPinjamGadget["data"][i]["id_gadget"] == id_item)\
                           and (dataPinjamGadget["data"][i]["id_peminjam"] == str(getUserID(username))):
                            can_borrow = False
                    
                    if(can_borrow):
                        # User bisa meminjam

                        notFound = True
                        for i in range(dataGadget["row_number"]):
                            if(dataGadget["data"][i]["id"] == id_item):
                                notFound = False

                                if(int(dataGadget["data"][i]["jumlah"]) > 0)\
                                     and (int(dataGadget["data"][i]["jumlah"]) >= jumlah_pinjam):
                                    # Edit Jumlah gadget yang tersedia di database
                                    newGadget = int(dataGadget["data"][i]["jumlah"]) - (jumlah_pinjam)
                                    dataGadget["data"][i]["jumlah"] = str(newGadget)

                                    print()
                                    print("Item " + str(dataGadget["data"][i]["nama"]) + " (x" + str(jumlah_pinjam) + ") " "berhasil dipinjam!")
                                    applyChange(dataGadget, "gadget")
                                    
                                    if getUserID(username):
                                        lastID = "PJM-0"
                                        nextIndex = dataPinjamGadget["row_number"]

                                        if(dataPinjamGadget["row_number"] > 0):
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
                                                "jumlah_kembali": "0",
                                                "is_returned": is_returned,
                                            }
                                        applyChange(dataPinjamGadget, "gadget_borrow_history")

                                    return getUserID
                                else:   #(dataGadget["data"][i]["jumlah"]) <= 0) or (dataGadget["data"][i]["jumlah"] < jumlah_pinjam)
                                    print()
                                    print("Jumlah yang ingin dipinjam melebihi stok item. Stok sekarang: " + str(dataGadget["data"][i]["jumlah"]))
                        
                        if notFound:   # dataGadget["data"][i]["id"] != id_item
                            print()  
                            print("Tidak ada item dengan ID tersebut!, silakan masukan ID yang valid")
                    else:  # jumlah_gadget_kembali != jumlah_gadget_pinjam 
                        print()
                        print("Kembalikan item dari peminjaman sebelumnya untuk dapat meminjam kembali")
                else:
                    print()
                    print("Masukan tanggal tidak valid, silakan masukan format tanggal yang valid")
            else:   # jumlah_pinjam <= 0
                print()
                print("Jumlah peminjaman harus lebih besar dari nol")
        else:
            print()
            print("Silakan lakukan login sebagai user untuk menjalankan perintah ini")