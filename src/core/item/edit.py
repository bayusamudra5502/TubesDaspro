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
            for i in range(dataGadget["row_number"]):
                if(dataGadget["data"][i]["id"] == id):
                    if(int(dataGadget["data"][i]["jumlah"]) >= jumlah_edit):
                        if jumlah_edit > 0:
                            newGadget = int(dataGadget["data"][i]["jumlah"]) + (jumlah_edit)
                            dataGadget["data"][i]["jumlah"] = str(newGadget)
                            print(str(jumlah_edit) + " " + str(dataGadget["data"][i]["nama"]) + " berhasil ditambahkan. Stok sekarang: " + str(newGadget))
                        elif jumlah_edit == 0:
                            print("Jumlah " + str(dataGadget["data"][i]["nama"] + " tidak berubah. Stok sekarang: " + str(dataGadget["data"][i]["jumlah"])))
                        else:   # jumlah_edit < 0
                            newGadget = int(dataGadget["data"][i]["jumlah"]) + (jumlah_edit)
                            dataGadget["data"][i]["jumlah"] = str(newGadget)
                            print(str(jumlah_edit) + " " + str(dataGadget["data"][i]["nama"]) + " berhasil dibuang. Stok sekarang: " + str(newGadget))
                    else:   #(dataGadget["data"][i]["jumlah"] < jumlah_edit)
                        jumlah_edit = abs(jumlah_edit)
                        print(str(jumlah_edit) + " " + str(dataGadget["data"][i]["nama"]) + " gagal dibuang karena stok kurang. Stok sekarang: " + str(dataGadget["data"][i]["jumlah"]))
                else:   # dataGadget["data"][i]["id"] != id
                    print("Tidak ada item dengan ID tersebut!")
                applyChange(dataGadget, "gadget")
        elif(id_array[0]=="C"):
            for i in range (dataConsumable["row_number"]):
                if(dataConsumable["data"][i]["id"] == id):
                    if(int(dataConsumable["data"][i]["jumlah"]) >= jumlah_edit):
                        if jumlah_edit > 0:
                            newGadget = int(dataGadget["data"][i]["jumlah"]) + (jumlah_edit)
                            dataGadget["data"][i]["jumlah"] = str(newGadget)
                            print(str(jumlah_edit) + " " + str(dataGadget["data"][i]["nama"]) + " berhasil ditambahkan. Stok sekarang: " + str(newGadget))
                        elif jumlah_edit == 0:
                            print("Jumlah " + str(dataGadget["data"][i]["nama"] + " tidak berubah. Stok sekarang: " + str(dataGadget["data"][i]["jumlah"])))
                        else:   # jumlah_edit < 0
                            newConsumable = int(dataConsumable["data"][i]["jumlah"]) + (jumlah_edit)
                            dataConsumable["data"][i]["jumlah"] = str(newConsumable)
                            print(str(jumlah_edit) + " " + str(dataConsumable["data"][i]["nama"]) + " berhasil dibuang. Stok sekarang: " + str(newConsumable))                            
                    else:   #(int(dataConsumable["data"][dataConsumable[i]]["jumlah"]) < jumlah_edit)
                        jumlah_edit = abs(jumlah_edit)
                        print(str(jumlah_edit) + " " + str(dataConsumable["data"][i]["nama"]) + " gagal dibuang karena stok kurang. Stok sekarang: " + str(dataConsumable["data"][i]["jumlah"]))
                else:   #(dataConsumable["data"][i]["id"] != id)
                    print("Tidak ada item dengan ID tersebut!")
                applyChange(dataConsumable, "consumable")
        else:   # (id_array[0] != "C") and (id_array[0] != "G") 
            print("Tidak ada item dengan ID tersebut!")
    else:
        print("Silakan lakukan login sebagai admin untuk menjalankan perintah ini")
    return isAdminRole