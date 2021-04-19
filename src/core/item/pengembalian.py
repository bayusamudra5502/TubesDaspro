# Module pengembalian
# Modul ini berisi implementasi dari fitur
# pengembalian gadget (F09 dan FB02)

from core.database import applyChange, getTable
from core.auth import isValidUser
from core.auth import isUserRole
from core.util import generateNextID
from core.util import isValidTanggal

def pengembalianGadget(username):
    if isValidUser(username):
        if isUserRole(username):
            dataGadget = getTable("gadget")
            dataPinjamGadget = getTable("gadget_borrow_history")
            dataKembaliGadget = getTable("gadget_return_history")
            nomor_pinjam = input("Masukan nomor peminjaman: ")
            jumlah_kembali = int(input("Masukan jumlah item yang dikembalikan: "))
            tanggal_kembali = input("Tanggal pengembalian: ")
            id_pengembalian = username
            validation_jumlah = False
            for i in range(dataPinjamGadget["row_number"]):
                print(dataPinjamGadget["data"][i]["id"] + ". ")
            for i in range(dataPinjamGadget["row_number"]):
                if(dataPinjamGadget["data"][i]["id"] == str(nomor_pinjam)):
                    if(int(dataPinjamGadget["data"][i]["jumlah"]) >= jumlah_kembali):
                        validation_jumlah = True
                        id_item = dataPinjamGadget["data"][i]["id_gadget"]
                    else:
                        break
                else:
                    print("Tidak ada item dengan nomor peminjaman tersebut")
            if validation_jumlah == True:
                for i in range(dataGadget["row_number"]):
                    if(dataGadget["data"][i]["id"] == id_item):
                        newGadget = int(dataGadget["data"][i]["jumlah"]) + jumlah_kembali
                        dataGadget["data"][i]["jumlah"] = str(newGadget)
                        dataKembaliGadget["data"][dataKembaliGadget["numRows"]]["id"] = generateNextID
                        dataKembaliGadget["data"][dataKembaliGadget["numRows"]]["id_pengembalian"] = id_pengembalian
                        dataKembaliGadget["data"][dataKembaliGadget["numRows"]]["id_gadget"] = id_item
                        dataKembaliGadget["data"][dataKembaliGadget["numRows"]]["tanggal_pengembalian"] = tanggal_kembali
                        dataKembaliGadget["data"][dataKembaliGadget["numRows"]]["jumlah"] = jumlah_kembali
                    else:
                        print("Item tersebut sudah tidak ada dalam database gadget")
            else:
                print("Jumlah yang ingin dikembalikan melebihi jumlah peminjaman")
pass