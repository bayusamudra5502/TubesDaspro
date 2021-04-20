# Module edit
# Modul ini berisi implementasi dari
# fitur mengubah jumlah gadget atau
# consumable pada inventory (F07)

from core.database import applyChange, getTable
from core.auth import isAdminRole

def edit(username):
    if isAdminRole(username):
        dataGadget = getTable("gadget")
        dataConsumable = getTable("consumable")
        # Meminta input
        id = input("Masukan ID item: ")
        jumlah_edit = int(input("Masukan jumlah: "))
        id_array = list(id)
        # Validasi dan modifikasi data
        if (id_array[0]=="G"):
            notFound = True
            for i in range(dataGadget["row_number"]):
                if(dataGadget["data"][i]["id"] == id):
                    notFound = False
                    if jumlah_edit > 0:
                        newGadget = int(dataGadget["data"][i]["jumlah"]) + (jumlah_edit)
                        dataGadget["data"][i]["jumlah"] = str(newGadget)
                        print()
                        print(str(jumlah_edit) + " " + str(dataGadget["data"][i]["nama"]) + " berhasil ditambahkan. Stok sekarang: " + str(newGadget))
                    elif jumlah_edit == 0:
                        print()
                        print("Jumlah " + str(dataGadget["data"][i]["nama"] + " tidak berubah. Stok sekarang: " + str(dataGadget["data"][i]["jumlah"])))
                    else:   # jumlah_edit < 0
                        if(int(dataGadget["data"][i]["jumlah"]) + (jumlah_edit) >= 0):
                            newGadget = int(dataGadget["data"][i]["jumlah"]) + (jumlah_edit)
                            dataGadget["data"][i]["jumlah"] = str(newGadget)
                            print()
                            print(str(jumlah_edit) + " " + str(dataGadget["data"][i]["nama"]) + " berhasil dibuang. Stok sekarang: " + str(newGadget))
                        else:
                            jumlah_edit = abs(jumlah_edit)
                            print()
                            print(str(jumlah_edit) + " " + str(dataGadget["data"][i]["nama"]) + " gagal dibuang karena stok kurang. Stok sekarang: " + str(dataGadget["data"][i]["jumlah"]))
                applyChange(dataGadget, "gadget")
            if notFound:   # dataGadget["data"][i]["id"] != id
                print()
                print("Tidak ada item dengan ID tersebut!")
        elif(id_array[0]=="C"):
            notFound = True
            for i in range(dataConsumable["row_number"]):
                if(dataConsumable["data"][i]["id"] == id):
                    notFound = False
                    if jumlah_edit > 0:
                        newConsumable = int(dataConsumable["data"][i]["jumlah"]) + (jumlah_edit)
                        dataConsumable["data"][i]["jumlah"] = str(newConsumable)
                        print(str(jumlah_edit) + " " + str(dataConsumable["data"][i]["nama"]) + " berhasil ditambahkan. Stok sekarang: " + str(newConsumable))
                    elif jumlah_edit == 0:
                        print("Jumlah " + str(dataConsumable["data"][i]["nama"] + " tidak berubah. Stok sekarang: " + str(dataConsumable["data"][i]["jumlah"])))
                    else:   # jumlah_edit < 0
                        if(int(dataConsumable["data"][i]["jumlah"]) + (jumlah_edit) >= 0):
                            newConsumable = int(dataConsumable["data"][i]["jumlah"]) + (jumlah_edit)
                            dataConsumable["data"][i]["jumlah"] = str(newConsumable)
                            print(str(jumlah_edit) + " " + str(dataConsumable["data"][i]["nama"]) + " berhasil dibuang. Stok sekarang: " + str(newConsumable))
                        else:   # (dataConsumable["data"][i]["jumlah"] + (jumlah_edit) < 0)
                            jumlah_edit = abs(jumlah_edit)
                            print(str(jumlah_edit) + " " + str(dataConsumable["data"][i]["nama"]) + " gagal dibuang karena stok kurang. Stok sekarang: " + str(dataConsumable["data"][i]["jumlah"]))
                applyChange(dataConsumable, "consumable")
            if notFound:   #(dataConsumable["data"][i]["id"] != id)
                print("Tidak ada item dengan ID tersebut, silakan masukan ID yang valid")
        else:   # (id_array[0] != "C") and (id_array[0] != "G") 
            print("Tidak ada item dengan ID tersebut, silakan masukan ID yang valid")
    else:
        print("Silakan lakukan login sebagai admin untuk menjalankan perintah ini")
    return isAdminRole