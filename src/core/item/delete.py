# Module delete
# Modul ini berisi implementasi dari fitur
# penghapusan gadget ataupun consumable (F06)

from core.database import applyChange, getTable
from core.auth import isAdminRole

def delete(username):
    if isAdminRole(username):
        dataGadget = getTable("gadget")
        dataConsumable = getTable("consumable")
        id = input("Masukan ID item: ")
        id_array = list(id)
        if (id_array[0]=="G"):
            for i in range(dataGadget["row_number"]):
                if(dataGadget["data"][i]["id"] == id):
                    print("Apakah anda yakin ingin menghapus " + str(dataGadget["data"][i]["nama"]) + " (Y/N)?", end="")
                    validation = input()
                    while (validation != "Y") and (validation != "y") and (validation != "N") and (validation != "n"):
                        print("Masukan yang diberikan salah")
                        print()
                        print("Apakah anda yakin ingin menghapus " + str(dataGadget["data"][i]["nama"]) + " (Y/N)?", end="")
                        validation = input()
                    if (validation == 'Y') or (validation == 'y'):
                        dataGadget["data"][i] ={}
                        print("Item telah berhasil dihapus dari database")
                    else:   #(validation == "N") or (validation == "n")
                        break
                else:    #(dataGadget["data"][i]["id"] != id)
                    print("Tidak ada item dengan ID tersebut")
        elif (id_array[0]=="C"):
            for i in range(dataConsumable["row_number"]):
                if(dataConsumable["data"][i]["id"] == id):
                    print("Apakah anda yakin ingin menghapus " + str(dataConsumable["data"][i]["nama"]) + " (Y/N)", end="")
                    validation = input()
                    while(validation != "Y") and (validation != "y") and (validation != "N") and (validation != "n"):
                        print("Masukan yang diberikan salah")
                        print()
                        print("Apakah anda yakin ingin menghapus " + str(dataGadget["data"][i]["nama"]) + " (Y/N)?", end="")
                        validation = input()
                    if(validation == "Y") or (validation == "y"):
                        dataConsumable["data"][i] = {}
                        print("Item telah berhasil dihapus dari database")
                    else:   #(validation == "N") or (validation == "n")
                        break
                else:   #(dataConsumable["data"][i]["id"] != id)
                    print("Tidak ada item dengan ID tersebut")
        else:   #(id_array[0] != "G") and (id_array[0] != "C")
            print("Tidak ada item dengan ID tersebut")
        applyChange(dataGadget, "gadget")
        applyChange(dataConsumable, "consumable")
    else:
        print("Silakan lakukan login sebagai admin untuk menjalankan perintah ini")
    return isAdminRole