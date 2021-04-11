# Module main
# Modul ini berisi implementasi dari fitur
# antarmuka perintah dan fitur exit. Pada 
# bagian ini, user akan memasukan perintahnya
# untuk mengakses kantong ajaib.

from os import error
from core.auth import *
from core.item import *
from core.database import isChanged, save
from core.item.permintaan import mintaConsumable
from core.util import toLower
from core.help import help

def exit(saveDir) -> bool:
    if(isChanged()):
        resp = ""
        while(toLower(resp) == "y" or 
                toLower(resp) == "n" or
                toLower(resp) == "c"):
            input("Apakah anda ingin meyimpan perubahan? [Y/n/c] : ")

            if(toLower(resp) == "y"):
                if(save(saveDir)):
                    print("\nPerubahan Berhasil disimpan...")
                return True
            elif(toLower(resp) == "n"):
                return True
            elif(toLower(resp) == "c"):
                return False
            else:
                print("Input tidak valid. Silahkan coba lagi.\n")
    else:
        return True

def main(saveDir):
    isExit = False
    username = ""
    errorCnt = 0

    print("Selamat datang di kantong ajaib")
    print()
    print("Untuk melihat perintah yang tersedia, gunakan perintah 'help'")
    print()

    commandDriver = {
        "carirarity" : searchByRarity,
        "caritahun" : searchByYear,
        "register" : register,
        "tambahitem" : addItem,
        "hapusitem" : delete,
        "ubahjumlah" : edit,
        "pinjam" : peminjamanGadget,
        "kembalikan" : pengembalianGadget,
        "minta" : mintaConsumable,
        "riwayatpinjam" : histPinjamGadget,
        "riwayatkembali" : histKembaliGadget,
        "riwayatambil" : histAmbilConsumable,
        "help" : help,
        "eksperimen": eksperimen
    }

    commandList = list(commandDriver.keys())
    command = ""

    while not isExit:
        try:
            command = toLower(input(">>> "))
            
            if command == "exit":
                isExit = exit(saveDir)
                errorCnt = 0
            elif command == "login":
                username = login()
                errorCnt = 0
            elif command == "save":
                if isValidUser(username):
                    if save(saveDir):
                        print("Data berhasil disimpan")
                
                errorCnt = 0
            else:
                isValidComm = False
                for i in range(len(commandList)):
                    if commandList[i] == command:
                        isValidComm = True
                
                if(isValidComm):
                    commandDriver[command](username)
                    errorCnt = 0
                elif(command != ""):
                    print("Perintah tidak valid, Silahkan coba lagi.")

                    if errorCnt >= 3:
                        print("Tips : Gunakan help untuk melihat perintah yang tersedia.")

        except KeyboardInterrupt:
            command = "exit"
            isExit = exit(saveDir)
        
        if(command != ""):
            print()