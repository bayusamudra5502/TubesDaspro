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
        # Meminta input ID
        id = input("Masukan ID item : ")
        id_array = list(id)
        wrong_id = True
        # Validasi format ID
        if id_array[0] == "G" or id_array[0] == "C":
            wrong_id = False
        if wrong_id == False:
            # Meminta input jumlah
            jumlah_edit = int(input("Masukan jumlah  : "))
            # Modifikasi data gadget
            if (id_array[0]=="G"):
                notFound = True
                for i in range(dataGadget["row_number"]):
                    if(dataGadget["data"][i]["id"] == id):  # Validasi apakah id tersebut ada pada databse
                        notFound = False
                        if jumlah_edit > 0: # Menambah jumlah gadget
                            newGadget = int(dataGadget["data"][i]["jumlah"]) + (jumlah_edit)
                            dataGadget["data"][i]["jumlah"] = str(newGadget)
                            print()
                            print(str(jumlah_edit) + " " + str(dataGadget["data"][i]["nama"]) + "\033[92m berhasil ditambahkan.\033[0m" + " Stok sekarang: " + str(newGadget))
                        elif jumlah_edit == 0:  # Tidak mengubah jumlah gadget
                            print()
                            print("Jumlah " + str(dataGadget["data"][i]["nama"] + " tidak berubah. Stok sekarang: " + str(dataGadget["data"][i]["jumlah"])))
                        else:   # jumlah_edit < 0 (Mengurangi jumlah gadget)
                            if(int(dataGadget["data"][i]["jumlah"]) + (jumlah_edit) >= 0):  # Jumlah yang ingin dikurangi tidak membuat jumlah gadget negatif
                                newGadget = int(dataGadget["data"][i]["jumlah"]) + (jumlah_edit)
                                dataGadget["data"][i]["jumlah"] = str(newGadget)
                                jumlah_edit = abs(jumlah_edit)
                                print()
                                print(str(jumlah_edit) + " " + str(dataGadget["data"][i]["nama"]) + "\033[92m berhasil dibuang.\033[0m" + " Stok sekarang: " + str(newGadget))
                            else:   # int(dataGadget["data"][i]["jumlah"]) + (jumlah_edit) < 0 (Jumlah yang ingin dikurangi membuat jumlah gadget negatif)
                                jumlah_edit = abs(jumlah_edit)
                                print()
                                print(str(jumlah_edit) + " " + str(dataGadget["data"][i]["nama"]) + "\033[91m gagal dibuang \033[0m" + "karena stok kurang. Stok sekarang: " + str(dataGadget["data"][i]["jumlah"]))
                    applyChange(dataGadget, "gadget")
                if notFound:   # dataGadget["data"][i]["id"] != id
                    print()
                    print("\033[91mTidak ada item dengan ID tersebut!\033[0m")
            # Modifikasi data consumable
            else:   # (id_array[0]=="C")
                notFound = True
                for i in range(dataConsumable["row_number"]):
                    if(dataConsumable["data"][i]["id"] == id):  # Validasi apakah id tersebut ada pada database
                        notFound = False
                        if jumlah_edit > 0: # Menambah jumlah consumable
                            newConsumable = int(dataConsumable["data"][i]["jumlah"]) + (jumlah_edit)
                            dataConsumable["data"][i]["jumlah"] = str(newConsumable)
                            print(str(jumlah_edit) + " " + str(dataConsumable["data"][i]["nama"]) + "\033[92m berhasil ditambahkan.\033[0m" + " Stok sekarang: " + str(newConsumable))
                        elif jumlah_edit == 0:  # Tidak mengubah jumlah consumable
                            print("Jumlah " + str(dataConsumable["data"][i]["nama"] + " tidak berubah. Stok sekarang: " + str(dataConsumable["data"][i]["jumlah"])))
                        else:   # jumlah_edit < 0 (Mengurangi jumlah consumable)
                            if(int(dataConsumable["data"][i]["jumlah"]) + (jumlah_edit) >= 0):  # Jumlah yang ingin dikurangi tidak membuat jumlah consumable negatif
                                newConsumable = int(dataConsumable["data"][i]["jumlah"]) + (jumlah_edit)
                                dataConsumable["data"][i]["jumlah"] = str(newConsumable)
                                print(str(jumlah_edit) + " " + str(dataConsumable["data"][i]["nama"]) + "\033[92m berhasil dibuang.\033[0m" + " Stok sekarang: " + str(newConsumable))
                            else:   # dataConsumable["data"][i]["jumlah"] + (jumlah_edit) < 0 (Jumlah yang ingin dikurangi membuat jumlah consumable negatif)
                                jumlah_edit = abs(jumlah_edit)
                                print(str(jumlah_edit) + " " + str(dataConsumable["data"][i]["nama"]) + "\033[91m gagal dibuang \033[0m" + "karena stok kurang. Stok sekarang: " + str(dataConsumable["data"][i]["jumlah"]))
                    applyChange(dataConsumable, "consumable")
                if notFound:   #(dataConsumable["data"][i]["id"] != id)
                    print("\033[91mTidak ada item dengan ID tersebut, silakan masukan ID yang valid\033[0m")
        else:   # (id_array[0] != "C") and (id_array[0] != "G")
            print()
            print("\033[91mFormat ID tidak valid, silakan masukan ID yang valid\033[0m")
    else:   # Akun yang digunakan tidak memiliki role admin
        print("\033[92mSilakan lakukan login sebagai admin untuk menjalankan perintah ini\033[0m")
    return isAdminRole
