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
            no_returned = True

            # Print daftar gadget yang dipinjam
            cntNum = 0
            print("Berikut ini adalah daftar pinjaman anda yang belum dikembalikan:")
            for i in range(dataPinjamGadget["row_number"]):
                for j in range(dataGadget["row_number"]):
                    if(dataPinjamGadget["data"][i]["id_peminjam"] == str(getUserID(username))):
                        if (dataPinjamGadget['data'][i]['id_gadget'])==(dataGadget['data'][j]['id']) and (dataPinjamGadget["data"][i]["is_returned"] == "FALSE"):
                            cntNum += 1
                            jumlah_tersisa = int(dataPinjamGadget['data'][i]['jumlah']) - int(dataPinjamGadget['data'][i]['jumlah_kembali'])
                            
                            print(str(cntNum) + ". " + dataGadget["data"][j]["nama"])
                            print(f"    ID Peminjaman : {dataPinjamGadget['data'][i]['id']}")
                            print(f"    Tanggal peminjaman : {dataPinjamGadget['data'][i]['tanggal_peminjaman']}")
                            print(f"    Jumlah yg belum dikembalikan : {jumlah_tersisa} item \n")
                            
                            no_returned = False
            
            if cntNum == 0:
                print("Anda tidak memiliki gadget yang dipinjam saat ini.")
            else:
                # Meminta input
                if no_returned == False:
<<<<<<< HEAD
                    print("Silahkan input data objek yang ingin dikembalikan")
                    nomor_pinjam = input("ID peminjaman : ")
                    validation_jumlah = False

                    # Validasi data
                    notFound = True
                    validation_jumlah = False
                    for i in range(dataPinjamGadget["row_number"]):
                        if(dataPinjamGadget["data"][i]["id"] == str(nomor_pinjam)):
                            notFound=False
                            if notFound == False:
                                jumlah_kembali = int(input("Masukan jumlah item yang dikembalikan : "))
                                if jumlah_kembali > 0:
=======
                    print("Silahkan input data objek yang ingin dikembalikan:")
                    nomor_pinjam = input("ID peminjaman : ")
                    jumlah_kembali = int(input("Masukan jumlah item yang dikembalikan : "))
                    tanggal_kembali = input("Tanggal pengembalian : ")
                    validation_jumlah = False

                    # Validasi dan modifikasi data
                    if jumlah_kembali > 0:
                        if isValidTanggal(tanggal_kembali):
                            notFound = True
                            id_item = ""

                            for i in range(dataPinjamGadget["row_number"]):
                                if(dataPinjamGadget["data"][i]["id"] == str(nomor_pinjam)):
                                    notFound=False

>>>>>>> acfed677c5496db3a9afc7844c011c53eae11d67
                                    if(int(dataPinjamGadget["data"][i]["jumlah"]) - int(dataPinjamGadget["data"][i]["jumlah_kembali"]) > jumlah_kembali):
                                        validation_jumlah = True

                                        id_item = dataPinjamGadget["data"][i]["id_gadget"]
                                        dataPinjamGadget["data"][i]["jumlah_kembali"] = \
                                            str(int(dataPinjamGadget["data"][i]["jumlah_kembali"]) + jumlah_kembali)

                                    elif(int(dataPinjamGadget["data"][i]["jumlah"]) - int(dataPinjamGadget["data"][i]["jumlah_kembali"]) == jumlah_kembali):
                                        validation_jumlah = True

                                        id_item = dataPinjamGadget["data"][i]["id_gadget"]
                                        dataPinjamGadget["data"][i]["is_returned"] = "TRUE"
                                        dataPinjamGadget["data"][i]["jumlah_kembali"] = \
                                            str(int(dataPinjamGadget["data"][i]["jumlah_kembali"]) + jumlah_kembali)
<<<<<<< HEAD
                                else:   #jumlah_kembali <= 0
                                    print()
                                    print("Jumlah pengembalian harus lebih besar dari nol")
                                        
                    # Modifikasi data
                    if notFound == True:   #dataPinjamGadget["data"][i]["id"] != str(nomor_pinjam)
                        print()
                        print("Tidak ada item dengan nomor peminjaman tersebut")
                    else:
                        if validation_jumlah:
                            tanggal_kembali = input("Tanggal pengembalian : ")
                            if isValidTanggal(tanggal_kembali):
                                notFound1 = True

                                for i in range(dataGadget["row_number"]):
                                    if(dataGadget["data"][i]["id"] == id_item):
                                        # Update data gadget di db
                                        notFound1 = False
                                        newGadget = int(dataGadget["data"][i]["jumlah"]) + jumlah_kembali
                                        dataGadget["data"][i]["jumlah"] = str(newGadget)

                                        print()
                                        print("Item "+ dataGadget['data'][i]['nama'] + " (x"+str(jumlah_kembali) + ") " + " telah dikembalikan!")

                                        if getUserID(username):
                                            lastID = "KMB-0"
                                            nextIndex = dataKembaliGadget["row_number"]

                                            if(dataKembaliGadget["row_number"] > 0):
                                                lastIndext = dataKembaliGadget["row_number"]-1
                                                lastID = dataKembaliGadget["data"][lastIndext]["id"]

                                            id1 = (generateNextID(lastID))

                                            dataKembaliGadget["data"][nextIndex] = \
                                                {
                                                    "id": id1,
                                                    "id_peminjaman": nomor_pinjam,
                                                    "tanggal_pengembalian": tanggal_kembali,
                                                    "jumlah": str(jumlah_kembali)
                                                }
                                                
                                            # Terapkan perubahan di db
                                            applyChange(dataGadget, "gadget")
                                            applyChange(dataPinjamGadget, "gadget_borrow_history")
                                            applyChange(dataKembaliGadget, "gadget_return_history")

                                if notFound1: 
                                    print()  
                                    print("Item tersebut sudah tidak ada dalam database gadget")
                            else:
                                print()
                                print("Masukan tanggal tidak valid, silakan masukan format tanggal yang valid")
                        else:   # validation_jumlah = False
                            print()
                            print("Jumlah yang ingin dikembalikan melebihi jumlah peminjaman")
                else:   # no_returned == True
                    print()
                    print("Tidak ada item yang perlu anda kembalikan")
        else:
            print()
=======
                                    

                            if notFound:   #dataPinjamGadget["data"][i]["id"] != str(nomor_pinjam)
                                print("Tidak ada item dengan nomor peminjaman tersebut")
                            else:
                                if validation_jumlah:
                                    notFound1 = True

                                    for i in range(dataGadget["row_number"]):
                                        if(dataGadget["data"][i]["id"] == id_item):
                                            # Update data gadget di db
                                            notFound1 = False
                                            newGadget = int(dataGadget["data"][i]["jumlah"]) + jumlah_kembali
                                            dataGadget["data"][i]["jumlah"] = str(newGadget)

                                            print()
                                            print("Item "+ dataGadget['data'][i]['nama'] + " (x"+str(jumlah_kembali) + ") " + " telah dikembalikan!")

                                            if getUserID(username):
                                                lastID = "KMB-0"
                                                nextIndex = dataKembaliGadget["row_number"]

                                                if(dataKembaliGadget["row_number"] > 0):
                                                    lastIndext = dataKembaliGadget["row_number"]-1
                                                    lastID = dataKembaliGadget["data"][lastIndext]["id"]

                                                id1 = (generateNextID(lastID))

                                                dataKembaliGadget["data"][nextIndex] = \
                                                    {
                                                        "id": id1,
                                                        "id_peminjaman": nomor_pinjam,
                                                        "tanggal_pengembalian": tanggal_kembali,
                                                        "jumlah": str(jumlah_kembali)
                                                    }
                                                
                                                # Terapkan perubahan di db
                                                applyChange(dataGadget, "gadget")
                                                applyChange(dataPinjamGadget, "gadget_borrow_history")
                                                applyChange(dataKembaliGadget, "gadget_return_history")

                                    if notFound1:   # dataGadget["data"][i]["id"] != id_item
                                        print("Item tersebut sudah tidak ada dalam database gadget")
                                else:   # validation_jumlah = False
                                    print()
                                    print("Jumlah yang ingin dikembalikan melebihi jumlah peminjaman")
                        else:
                            print()
                            print("Masukan tanggal tidak valid, silakan masukan format tanggal yang valid")
                    else:   # jumlah_kembali <= 0
                        print("Jumlah pengembalian harus lebih besar dari nol")
                else:   # no_returned == True
                    print("Tidak ada item yang perlu anda kembalikan")
        else:
>>>>>>> acfed677c5496db3a9afc7844c011c53eae11d67
            print("Silakan lakukan login sebagai user untuk menjalankan perintah ini")