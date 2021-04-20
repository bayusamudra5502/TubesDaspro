  
# Module pengembalian
# Modul ini berisi implementasi dari fitur
# pengembalian gadget (F09 dan FB02)

from core.database import applyChange, getTable
from core.auth import isValidUser
from core.auth import isUserRole
from core.util import generateNextID
from core.auth import getUserID
from core.util import isValidTanggal

def pengembalianGadget(username):
    if isValidUser(username):
        if isUserRole(username):
            dataGadget = getTable("gadget")
            dataPinjamGadget = getTable("gadget_borrow_history")
            dataKembaliGadget = getTable("gadget_return_history")
            # Print daftar gadget yang dipinjam
            for i in range(dataPinjamGadget["row_number"]):
                for j in range(dataGadget["row_number"]):
                    if (dataPinjamGadget['data'][i]['id_gadget'])==(dataGadget['data'][j]['id']):
                        print(dataPinjamGadget["data"][i]["id"] + ". " + dataGadget["data"][j]["nama"])
            # Meminta input
            nomor_pinjam = input("Masukan nomor peminjaman: ")
            jumlah_kembali = int(input("Masukan jumlah item yang dikembalikan: "))
            tanggal_kembali = input("Tanggal pengembalian: ")
            validation_jumlah = False
            is_returned = True
            # Validasi dan modifikasi data
            if jumlah_kembali > 0:
                if isValidTanggal(tanggal_kembali):
                    notFound=True
                    for i in range(dataPinjamGadget["row_number"]):
                        if(dataPinjamGadget["data"][i]["id"] == str(nomor_pinjam)):
                            notFound=False
                            if(int(dataPinjamGadget["data"][i]["jumlah"]) > jumlah_kembali):
                                validation_jumlah = True
                                id_item = dataPinjamGadget["data"][i]["id_gadget"]
                            elif(int(dataPinjamGadget["data"][i]["jumlah"]) == jumlah_kembali):
                                validation_jumlah = True
                                id_item = dataPinjamGadget["data"][i]["id_gadget"]
                                dataPinjamGadget["data"][i]["is_returned"] = str(is_returned)
                    if notFound:   #dataPinjamGadget["data"][i]["id"] != str(nomor_pinjam)
                        print("Tidak ada item dengan nomor peminjaman tersebut")
                    if validation_jumlah == True:
                        notFound1 =True
                        for i in range(dataGadget["row_number"]):
                            if(dataGadget["data"][i]["id"] == id_item):
                                notFound1 = False
                                newGadget = int(dataGadget["data"][i]["jumlah"]) + jumlah_kembali
                                dataGadget["data"][i]["jumlah"] = str(newGadget)
                                print()
                                print("Item "+ dataGadget['data'][i]['nama'] + " (x"+str(jumlah_kembali) + ") " + " telah dikembalikan!")
                                if getUserID(username):
                                    nextIndex = dataKembaliGadget["row_number"]
                                    lastIndext = dataKembaliGadget["row_number"]-1
                                    lastID = dataKembaliGadget["data"][lastIndext]["id"]
                                    id1 = (generateNextID(lastID))
                                    if generateNextID(lastID):
                                        dataKembaliGadget["data"][nextIndex] = \
                                        {
                                        "id": id1,
                                        "id_peminjaman": nomor_pinjam,
                                        "tanggal_pengembalian": tanggal_kembali,
                                        "jumlah_kembali": str(jumlah_kembali)
                                        }
                                    applyChange(dataKembaliGadget, "gadget_return_history")
                                return getUserID
                        if notFound1:   # dataGadget["data"][i]["id"] != id_item
                            print("Item tersebut sudah tidak ada dalam database gadget")
                    else:   # validation_jumlah = False
                        print()
                        print("Jumlah yang ingin dikembalikan melebihi jumlah peminjaman")
                else:
                    print()
                    print("Masukan tanggal tidak valid, silakan masukan format tanggal yang valid")
                return isValidTanggal
            else:   # jumlah_kembali <= 0
                print("Jumlah pengembalian harus lebih besar dari nol")
        else:
            print()
            print("Silakan lakukan login sebagai user untuk menjalankan perintah ini")
        return isUserRole
    return isValidUser