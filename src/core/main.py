# Module main
# Modul ini berisi implementasi dari fitur
# antarmuka perintah dan fitur exit. Pada 
# bagian ini, user akan memasukan perintahnya
# untuk mengakses kantong ajaib.

from os import system
from os.path import abspath
import sys
from core.auth import *
from core.item import *
from core.database import isChanged, save
from core.item.permintaan import mintaConsumable
from core.util import toLower
from core.help import help

def exit(username) -> bool:
    if(isChanged() and (username) != ""):
        resp = ""
        while(not (toLower(resp) == "y" or 
                toLower(resp) == "n" or
                toLower(resp) == "c")):
            resp = input("Apakah anda ingin meyimpan perubahan? [Y/n/c] : ")

            if(toLower(resp) == "y"):
                if(doSave(username)):
                    return True
                else:
                    errResp = toLower(input("Apakah anda ingin tetap keluar tanpa menyimpan? [Y/n] : ")) 
                    if(errResp == "y"):
                        return True
                    else:
                        return False
            elif(toLower(resp) == "n"):
                print("Perubahan tidak disimpan")
                return True
            elif(toLower(resp) == "c"):
                return False
            else:
                print("Input tidak valid. Silahkan coba lagi.")
    else:
        return True

def doSave(username):
    if(isValidUser(username)):
        isOKLocation = False
        saveDir = ""
        while not isOKLocation:
            print("Silahkan masukkan lokasi penyimpanan database.")
            print()

            saveDir = input("Lokasi Penyimpanan : ")
            print()

            print("Lokasi penyimpanan yang dipilih: ")
            print(abspath(saveDir))
            print()

            isValidResp = False
            while not isValidResp:
                resp = input("Apakah lokasi penyimpanan sudah benar? [Y/n] : ")
                if(toLower(resp) == "y"):
                    isOKLocation = True
                    isValidResp = True
                elif(toLower(resp) == "n"):
                    isValidResp = True
                else:
                    print("Input tidak valid. Silahkan coba lagi.")

        if(save(saveDir)):
            print("Perubahan Berhasil disimpan...")
            return True
        else:
            print("Perubahan gagal disimpan.")
            return False
    else:
        print("Anda tidak memiliki akses untuk menyimpan data.")
        return False

def main(saveDir):
    isExit = False
    username = ""
    errorCnt = 0

    system("cls || clear")

    # Diambil dari : https://patorjk.com/software/taag/#p=display&f=Big&t=Kantong%20Ajaib
    print("""
  _  __           _                               _       _ _     
 | |/ /          | |                        /\   (_)     (_) |    
 | ' / __ _ _ __ | |_ ___  _ __   __ _     /  \   _  __ _ _| |__  
 |  < / _` | '_ \| __/ _ \| '_ \ / _` |   / /\ \ | |/ _` | | '_ \ 
 | . \ (_| | | | | || (_) | | | | (_| |  / ____ \| | (_| | | |_) |
 |_|\_\__,_|_| |_|\__\___/|_| |_|\__, | /_/    \_\ |\__,_|_|_.__/ 
                                  __/ |         _/ |              
                                 |___/         |__/   v1.0
""")
    print("Selamat datang di kantong ajaib")
    print()
    print("Silahkan lakukan login dengan menggunakan perintah 'login'")
    print("Untuk melihat perintah yang tersedia, gunakan perintah 'help'\n")

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

            if command == "whois":
                if username != "":
                    print("Anda login sebagai")
                    print(f"Username : {username}")
                    if(isUserRole(username)):
                        print(f"Role : User")
                    elif(isAdminRole(username)):
                        print("Role : Administrator")
                    
                else:
                    print("Anda belum melakukan login. Silahkan login terlebih dahulu.")
            elif(command == "logout"):
                if(username != ""):
                    username = ""
                    print("Anda berhasil logout.")
                else:
                    print("Anda belum melakukan login. Silahkan gunakan perintah LOGIN.")
            elif command == "exit":
                isExit = exit(username)
                errorCnt = 0
                command = ""
            elif command == "login":
                username = login()
                errorCnt = 0
            elif command == "save":
                if username == "":
                    print("Anda belum melakukan login. Silahkan login terlebih dahulu dengan menggunakan perintah 'login'")
                elif isValidUser(username):
                    doSave(username)
                
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
            isExit = exit(username)
            command = ""
        finally:
            if(command != ""):
                print()