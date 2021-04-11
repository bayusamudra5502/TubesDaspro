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

def exit(saveDir, username) -> bool:
    if(isChanged() and (username) != ""):
        resp = ""
        while(not (toLower(resp) == "y" or 
                toLower(resp) == "n" or
                toLower(resp) == "c")):
            resp = input("Apakah anda ingin meyimpan perubahan? [Y/n/c] : ")

            if(toLower(resp) == "y"):
                if(isValidUser(username)):
                    if(save(saveDir)):
                        print("Perubahan Berhasil disimpan...")
                    return True
                else:
                    print("Perubahan tidak berhasil disimpan.")
            elif(toLower(resp) == "n"):
                print("Perubahan tidak disimpan")
                return True
            elif(toLower(resp) == "c"):
                return False
            else:
                print("Input tidak valid. Silahkan coba lagi.")
    else:
        return True

def main(saveDir):
    isExit = False
    username = "admin"
    errorCnt = 0

    print("Selamat datang di kantong ajaib")
    print()
    print("Untuk melihat perintah yang tersedia, gunakan perintah 'help'")

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
                isExit = exit(saveDir, username)
                errorCnt = 0
                command = ""
            elif command == "login":
                username = login()
                errorCnt = 0
            elif command == "save":
                if username == "":
                    print("Anda belum melakukan login. Silahkan login terlebih dahulu dengan menggunakan perintah 'login'")
                elif isValidUser(username):
                    if save(saveDir):
                        print("Data berhasil disimpan")
                
                errorCnt = 0
            elif command == "":
                pass
            elif command == "help":
                commandDriver["help"](username)
            else:
                if username == "":
                    print("Anda belum melakukan login. Silahkan login terlebih dahulu dengan menggunakan perintah 'login'")
                else:
                    isValidComm = False
                    for i in range(len(commandList)):
                        if commandList[i] == command:
                            isValidComm = True
                    
                    if(isValidComm):
                        commandDriver[command](username)
                        errorCnt = 0
                    else:
                        print("Perintah tidak valid, Silahkan coba lagi.")

                        if errorCnt >= 3:
                            print("Tips : Gunakan help untuk melihat perintah yang tersedia.")
                        
                        errorCnt += 1

        except KeyboardInterrupt:
            command = "exit"
            print()
            isExit = exit(saveDir, username)
            command = ""