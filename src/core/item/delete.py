# Module delete
# Modul ini berisi implementasi dari fitur
# penghapusan gadget ataupun consumable (F06)

from core.database import applyChange, getTable
from core.auth import isAdminRole

def delete(username):
    if isAdminRole(username):
        dataGadget = getTable("gadget")
        dataConsumable = getTable("consumable")
        # Meminta input
        id = input("Masukan ID item: ")
        id_array = list(id)
        # Validasi dan modifikasi data gadget
        if (id_array[0]=="G"):
            notFound1 = True
            for i in range(dataGadget["row_number"]):
                if(dataGadget["data"][i]["id"] == id):
                    notFound1 = False
                    print("Apakah anda yakin ingin menghapus " + str(dataGadget["data"][i]["nama"]) + " (Y/N)?", end="")
                    validation = input()
                    while (validation != "Y") and (validation != "y") and (validation != "N") and (validation != "n"):
                        print("Masukan yang diberikan salah")
                        print()
                        print("Apakah anda yakin ingin menghapus " + str(dataGadget["data"][i]["nama"]) + " (Y/N)?", end="")
                        validation = input()
                    # Menghapus data
                    if (validation == 'Y') or (validation == 'y'):
                        dataGadget["data"][i] ={}
                        print()
                        print("Item telah berhasil dihapus dari database")
                        applyChange(dataGadget, "gadget")
                    else:   #(validation == "N") or (validation == "n")
                        break
            if notFound1:    #(dataGadget["data"][i]["id"] != id)
                print()
                print("Tidak ada item dengan ID tersebut")
        # Validasi dan modifikasi data consumable
        elif (id_array[0]=="C"):
            notFound = True
            for i in range(dataConsumable["row_number"]):
                if(dataConsumable["data"][i]["id"] == id):
                    notFound = False
                    print("Apakah anda yakin ingin menghapus " + str(dataConsumable["data"][i]["nama"]) + " (Y/N)", end="")
                    validation = input()
                    # Validasi input Y dan N
                    while(validation != "Y") and (validation != "y") and (validation != "N") and (validation != "n"):
                        print("Masukan yang diberikan salah")
                        print()
                        print("Apakah anda yakin ingin menghapus " + str(dataGadget["data"][i]["nama"]) + " (Y/N)?", end="")
                        validation = input()
                    if(validation == "Y") or (validation == "y"):   # Menghapus data
                        dataConsumable["data"][i] = {}
                        print()
                        print("Item telah berhasil dihapus dari database")
                        applyChange(dataConsumable, "consumable")
                    else:   #(validation == "N") or (validation == "n")
                        break
            if notFound:   #(dataConsumable["data"][i]["id"] != id)
                print()
                print("Tidak ada item dengan ID tersebut")
        else:   #(id_array[0] != "G") and (id_array[0] != "C")
            print()
            print("Format ID tidak valid, silakan masukan ID yang valid")
    else:
        print()
        print("Silakan lakukan login sebagai admin untuk menjalankan perintah ini")
    return isAdminRole