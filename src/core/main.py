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

currentDBLocation = ""

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
            print()
            print("\033[36mPenyimpanan data ke database")
            print("---------------------------------\033[0m\n")
            print("Silahkan masukkan lokasi penyimpanan database.")
            print("Jika anda ingin menyimpan database pada lokasi sebelumnya, masukkan \033[34m.*.\033[0m")
            print()

            saveDir = input("Lokasi Penyimpanan : ")
            if(saveDir == ".*."):
                saveDir = currentDBLocation
            
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
    global currentDBLocation

    currentDBLocation = saveDir

    isExit = False
    username = ""
    errorCnt = 0

    system("cls || clear")

    # Diambil dari : https://patorjk.com/software/taag/#p=display&f=Big&t=Kantong%20Ajaib
    print("""\033[32m

  _  __           _                               _       _ _     
 | |/ /          | |                        /\   (_)     (_) |    
 | ' / __ _ _ __ | |_ ___  _ __   __ _     /  \   _  __ _ _| |__  
 |  < / _` | '_ \| __/ _ \| '_ \ / _` |   / /\ \ | |/ _` | | '_ \ 
 | . \ (_| | | | | || (_) | | | | (_| |  / ____ \| | (_| | | |_) |
 |_|\_\__,_|_| |_|\__\___/|_| |_|\__, | /_/    \_\ |\__,_|_|_.__/ 
                                  __/ |         _/ |              
                                 |___/         |__/   \033[36m v1.0 \033[0m
""")
    print("Selamat datang di kantong ajaib")
    print()
    print("Silahkan lakukan login dengan menggunakan perintah \033[34mLOGIN\033[0m")
    print("Untuk melihat perintah yang tersedia, gunakan perintah \033[34mHELP\033[0m\n")

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
        "eksperimen": eksperimen,
        "save": doSave
    }

    commandList = list(commandDriver.keys()) + \
                    ["whois","login","help","exit","logout","", "save"]
    command = ""

    while not isExit:
        try:
            command = toLower(input(">>> "))

            # Cek perintah valid atau tidak
            isValidComm = False
            for i in range(len(commandList)):
                if commandList[i] == command:
                    isValidComm = True
                    
            if(not isValidComm):
                print("\033[91mPerintah tidak valid, silahkan coba lagi.\033[0m")
                if errorCnt >= 3:
                    print("Tips : Gunakan help untuk melihat perintah yang tersedia.")
                
                errorCnt += 1
            elif command == "login":
                if username == "":
                    username = login()
                    if username == None:
                        username = ""
                else:
                    print(f"\033[32mINFO : \033[0mAnda sudah melakukan login sebagai {username}.")
                    print("Silahkan logout terlebih dahulu untuk mengganti user.")
                    print("Gunakan perintah \033[34mLOGOUT\033[0m untuk logout.")
                
                errorCnt = 0
            elif command == "help":
                commandDriver["help"](username)
            elif command == "exit":
                isExit = exit(username)
                errorCnt = 0
                command = ""
            elif isValidUser(username) and command != "":
                if command == "whois":
                        print()
                        print("\033[36mStatus Login")
                        print("----------------\033[0m")
                        print("Saat ini anda login sebagai")
                        print(f"Username : {username}")
                        if(isUserRole(username)):
                            print(f"Role : User")
                        elif(isAdminRole(username)):
                            print("Role : Administrator")
                elif(command == "logout"):
                    username = ""
                    print("Anda berhasil logout.")
                elif command == "save":
                    doSave(username)
                else:
                    commandDriver[command](username)

            elif command == "":
                pass
            else:
                print("\033[33mPERINGATAN:\033[0m Anda belum melakukan login. \nSilahkan login terlebih dahulu dengan menggunakan perintah \033[34mLOGIN\033[0m.")
                errorCnt = 0

        except KeyboardInterrupt:
            command = "exit"
            print()
            isExit = exit(username)
            command = ""
        finally:
            if(command != ""):
                print()