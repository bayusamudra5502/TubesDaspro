# Module main
# Modul ini berisi implementasi dari fitur
# antarmuka perintah dan fitur exit. Pada 
# bagian ini, user akan memasukan perintahnya
# untuk mengakses kantong ajaib.

# PUSTAKA
from os import system
from os.path import abspath
from core.auth import *
from core.item import *
from core.database import isChanged, save
from core.item.permintaan import mintaConsumable
from core.util import toLower
from core.help import help

# KAMUS
# currentDBLocation : string = ""
currentDBLocation = ""

# function exit(username:string) -> boolean
# Fungsi ini akan menangani proses exit program. Fungsi
# ini akan memeriksa apakah user telah melakukan perubahan
# pada database atau belum. Jika sudah, akan diberi opsi
# untuk menyimpan perubahan atau tidak.
# Fungsi ini akan menghasilkan True bila program dihendaki
# untuk ditutup, dan False bila batal ditutup.

# procedure doSave(input username: string)
# Prosedur ini akan menjadi view dari proses penyimpanan data.
# User yang memiliki hak menyimpan akan diminta lokasi
# penyimpanan data.

# procedure main(input savedir: string, 
#               input/output currentDBLocation: string)
# Prosedur ini akan menjadi menu utama dalam program. Prosedur
# ini akan menjadi perantara pada program

# procedure header()
# Prosedur ini akan mencetak header program pada layar

def exit(username) -> bool:
    """Fungsi ini akan menangani proses exit program. Fungsi
    ini akan memeriksa apakah user telah melakukan perubahan
    pada database atau belum. Jika sudah, akan diberi opsi
    untuk menyimpan perubahan atau tidak.
    
    Fungsi ini akan menghasilkan True bila program dihendaki
    untuk ditutup, dan False bila batal ditutup.
    """
    # KAMUS LOKAL
    # resp : char
    # errResp : char

    # ALGORTIMA
    if(isChanged() and (username) != ""):
        resp = ""
        while(not (toLower(resp) == "y" or 
                toLower(resp) == "n" or
                toLower(resp) == "c")):
            print()
            print("\033[33mPERHATIAN\033[0m")
            resp = input("Apakah anda ingin meyimpan perubahan yang telah dilakukan? [Y/n/c] : ")

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
    """Prosedur ini akan menjadi view dari proses penyimpanan data.
    User yang memiliki hak menyimpan akan diminta lokasi
    penyimpanan data.
    """
    # KAMUS LOKAL
    # isOKLocation : boolean
    # isValidResp : boolean
    # saveDir : string
    # resp : string

    # ALGORITMA
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

def header():
    """Mencetak Header Program"""
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
    print("Untuk melihat perintah yang tersedia, gunakan perintah \033[34mHELP\033[0m")

def main(saveDir):
    """
    Prosedur ini akan menjadi menu utama dalam program. Prosedur ini akan
    menjadi perantara dari berbagai fitur pada program.
    """
    global currentDBLocation

    # KAMUS LOKAL
    # isExit: boolean 
    # username: string
    # errorCnt: integer
    # commandList: Array[0..21] of string
    # command: string
    # isValidComm: boolean
    # i : integer

    # ALGORITMA
    currentDBLocation = saveDir

    isExit = False
    username = ""
    errorCnt = 0

    header()
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
        "eksperimen": eksperimen,
        "save": doSave
    }

    commandList = list(commandDriver.keys()) + \
                    ["whois","login","help","exit","logout","", "save", "clear"]
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
            elif command == "clear":
                header()
            elif isValidUser(username) and command != "":
                if command == "whois":
                        print()
                        print("\033[36mSTATUS LOGIN\033[0m")
                        print()
                        print("Saat ini anda login sebagai")
                        print(f"Username : {username}")
                        if(isUserRole(username)):
                            print(f"Role : User")
                        elif(isAdminRole(username)):
                            print("Role : Administrator")
                elif command == "eksperimen":
                    if commandDriver["eksperimen"](username):
                        header()
                elif(command == "logout"):
                    username = ""
                    print()
                    print("\033[36mINFORMASI\033[0m")
                    print("Anda telah berhasil logout.")
                elif command == "save":
                    doSave(username)
                else:
                    commandDriver[command](username)

            elif command == "":
                pass
            else:
                print()
                print("\033[33mPERINGATAN\n\033[0mAnda belum melakukan login saat ini. \nSilahkan login terlebih dahulu dengan menggunakan perintah \033[34mLOGIN\033[0m.")
                errorCnt = 0

        except KeyboardInterrupt:
            command = "exit"
            print()
            isExit = exit(username)
            command = ""
        finally:
            if(command != ""):
                print()