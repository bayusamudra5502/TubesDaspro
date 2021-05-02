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
            is_returned = "FALSE"
            can_borrow = True
            notFound = True

            # Meminta input ID
            id_item = input("Masukan ID item    : ")

            # Cek apakah format ID sudah benar
            wrong_id = True
            id_array = list(id_item)
            if id_array[0] == "G" or id_array[0] == "C":
                wrong_id = False

            # Cek status peminjaman item
            for i in range(dataPinjamGadget["row_number"]):
                if(dataPinjamGadget["data"][i]["is_returned"] == "FALSE")\
                    and (dataPinjamGadget["data"][i]["id_gadget"] == id_item)\
                    and (dataPinjamGadget["data"][i]["id_peminjam"] == str(getUserID(username))):
                    can_borrow = False

            if(can_borrow) == True and wrong_id == False: # User bisa meminjam
                for i in range(dataGadget["row_number"]):
                    if(dataGadget["data"][i]["id"] == id_item):
                        notFound = False
                    else:
                        pass
                if notFound == False:
                    tanggal_pinjam = input("Tanggal peminjaman : ") # Meminta input tanggal
                    if isValidTanggal(tanggal_pinjam):  # Validasi input tanggal
                        jumlah_pinjam = int(input("Jumlah peminjaman  : ")) # Meminta input jumlah pinjam
                        if jumlah_pinjam > 0:   # Validasi input jumlah pinjam
                            for i in range(dataGadget["row_number"]):
                                if(dataGadget["data"][i]["id"] == id_item):
                                    if(int(dataGadget["data"][i]["jumlah"]) > 0)\
                                        and (int(dataGadget["data"][i]["jumlah"]) >= jumlah_pinjam):    # Validasi jika gadget yang ingin dipinjam ada dan jumlah yang ingin dipinjam tidak lebih dari jumlah gadget
                                        # Edit Jumlah gadget yang tersedia di database
                                        newGadget = int(dataGadget["data"][i]["jumlah"]) - (jumlah_pinjam)
                                        dataGadget["data"][i]["jumlah"] = str(newGadget)

                                        print()
                                        print("Item " + str(dataGadget["data"][i]["nama"]) + " (x" + str(jumlah_pinjam) + ") " "\033[92mberhasil dipinjam!\033[0m")
                                        applyChange(dataGadget, "gadget")
                                        # Menambah data pada database peminjaman
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
                                    else:   #(dataGadget["data"][i]["jumlah"]) <= 0) or (dataGadget["data"][i]["jumlah"] < jumlah_pinjam) (Gadget yang ingin dipinjam tidak ada atau jumlah peminjaman melebihi jumlah gadget yang tersedia)
                                        print()
                                        print("\033[91mJumlah yang ingin dipinjam melebihi stok item\033[0m. Stok sekarang: " + str(dataGadget["data"][i]["jumlah"]))                      
                        else:  # jumlah_pinjam < 0
                            print()
                            print("\033[91mJumlah peminjaman harus lebih besar dari nol\033[0m")
                    else:
                        print()
                        print("\033[91mMasukan tanggal tidak valid, silakan masukan format tanggal yang valid\033[0m")
                else:   # notFound == True
                    print()
                    print("\033[91mTidak ada item dengan ID tersebut!, silakan masukan ID yang valid\033[0m")
            elif wrong_id == True:  # (id_array[0] != "C") and (id_array[0] != "G")
                print()
                print("\033[91mFormat ID tidak valid, silakan masukan ID yang valid\033[0m")           
            else:   # can_borrow == False
                print()
                print("\033[91mKembalikan item dari peminjaman sebelumnya untuk dapat meminjam kembali\033[0m")
        else:   # Akun yang digunakan tidak memiliki role user
            print()
            print("\033[92mSilakan lakukan login sebagai user untuk menjalankan perintah ini\033[0m")
