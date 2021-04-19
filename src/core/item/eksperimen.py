# Module Eksperimen
# Modul ini merupakan realisasi dari fitur
# FB03, yaitu meningkatkan rarity Consumable

from core.constant import MAX_ARRAY_NUM
from core.database import getTable
from core.auth import isValidUser, user
from core.database import applyChange
from core.util import random
from core.util import toLower
from os import system
from time import sleep
from core.constant import ENGINE_CHART, RARITY_CHART

MAX_SHOW_NUM = 5

consumables = [{} for i in range(MAX_ARRAY_NUM)]
engine = {}
nItem = 0
dataConsumable = []

def selectIndex(len):
    isOK = False
    index = -1
    while not isOK:
        try:
            isValidIndex = False

            while not isValidIndex:
                index = int(input("Nomor Urut : ")) - 1
                if(index < 0):
                    print("Nomor urut tidak valid silahkan coba lagi.")
                elif(index >= len):
                    print("Nomor urut diluar batas. Pastikan anda memasukan nomor urut yang benar.")
                else:
                    isValidIndex = True 

            isOK = True
        except Exception:
            print("Pastikan anda hanya memasukkan bilangan bulat saja.") 
    
    return index

def getCount(num):
    try:
        count = -1
        isOKCount = False
        while not isOKCount:
            count = int(input("Jumlah Item : "))
            if count > num:
                print("Jumlah yang diinputkan tidak mencukupi dengan stok!")
                print()
            elif(count <= 0):
                print("Masukkan jumlah consumable yang benar! Pastikan anda memasukan nilai > 0.")
                print()
            else:
                isOKCount = True

        return count
    except Exception:
        print("Error! Pastikan anda hanya memasukan bilangan bulat saja.")

def showData(data, title):
    system("cls || clear")

    print(title)
    print()

    showStartNum = 0
    showEndNum = data["row_number"]
    cmd = "n"

    if(showEndNum >= MAX_SHOW_NUM):
        showEndNum = MAX_SHOW_NUM

    while toLower(cmd) == "n":
        for i in range(showStartNum, showEndNum):
            print("%d. %s (Rarity %s) (%d)" 
                % (i+1,data["data"][i]["nama"]))

        print()

        cmd = "n"
        if((data["row_number"] > (showStartNum + MAX_SHOW_NUM))):
            print("...")
            print()
            cmd = input("Tampilkan data selanjutnya [Y/n] :")
            if(toLower(cmd) == "y"):
                showStartNum += MAX_SHOW_NUM
                if(data["row_number"] - (showEndNum + MAX_SHOW_NUM) > 0):
                    showEndNum += MAX_SHOW_NUM
                else:
                    showEndNum = data["row_number"]

def addItem():
    global consumables, nItem, dataConsumable
    print()
    isOK = False
    while not isOK:
        print("Silahkan masukkan nomor urut consumable yang ingin digunakan:")
        index = selectIndex(dataConsumable["row_number"])

        isInCart = False
        for i in range(nItem):
            isInCart = isInCart or \
                (dataConsumable["data"][index]["nama"] == consumables[i]["nama"])
    
        if isInCart:
            print("Nama barang sudah ada di keranjang. Jika anda ingin melakukan perubahan silahkan lakukan edit barang.")
            isOK = not ((toLower(input("Apakah anda ingin kembali ke halaman laboratorium? [Y/n] : ")) == "y"))
            print()
        else:
            count = getCount(dataConsumable["data"][index]["jumlah"])

            selectedObject = {
                "nama" : dataConsumable["data"][index]["nama"],
                "jumlah" : count,
                "rarity" : dataConsumable["data"][index]["rarity"],
                "dbIndex" : index
            }

            print()
            print("Berikut consumable yang dipilih : ")
            print(f"Nama\t: {selectedObject['nama']}")
            print(f"Jumlah yang dipilih\t: {selectedObject['jumlah']}")
            print(f"Rarity\t: {selectedObject['rarity']}")
            print()

            isOK = (toLower(input("Apakah data diatas sudah benar? [Y/n] : ")) == "y")
                    
            if(isOK):
                consumables[nItem] = selectedObject
                dataConsumable["data"][index]["jumlah"] -= count
                nItem += 1

def deleteItem():
    try:
        isLocked = True
        while isLocked:
            print("Silahkan isi nomor urut consumable pada keranjang yang akan dihapus.")

            index = selectIndex(nItem)

            print()
            print("Berikut ini adalah consumable yang akan dihapus dari daftar keranjang:")
            print()

            print(f"Nama Consumable : {consumables[index]['nama']}")
            print(f"Jumlah : {consumables[index]['jumlah']}")
            print(f"Rarity : {consumables[index]['rarity']}")

            print()
            isValidCMD = False
            while not isValidCMD:
                cmd = toLower(input("Apakah data diatas sudah benar? [Y/n/c] : ")) 
                if(cmd == "y"):
                    for i in range(index, nItem):
                        consumables[i] = consumables[i+1]
                    
                    consumables[nItem] = {}
                    nItem -= 1
                    print("Data Berhasil dihapus.")
                    isValidCMD = True
                    isLocked = False
                elif(cmd == "c"):
                    isValidCMD = True
                    print("Aksi dibatalkan.")
                    isLocked = False
                elif(cmd == "n"):
                    isValidCMD = True
                else:
                    print("Masukan tidak dikenali, ulangi.")

    except Exception:
        print("Input hanya menerima bilangan bulat!")

def editItem():
    global consumables, nItem, dataConsumable
    isLocked = True
    while isLocked:
        print("Silahkan pilih nomor consumable yang akan diubah:")
        index = selectIndex(nItem)

        print("Silahkan masukkan jumlah baru yang diinginkan")
        dbIndex = consumables[index]["dbIndex"]
        total = dataConsumable["data"][dbIndex]["jumlah"] + consumables[index]["jumlah"]

        newCnt = getCount(total)

        print()
        print("Berikut ini adalah keranjanng yang akan diubah : ")
        print(f"Nama : {consumables[index]['nama']}")
        print(f"Jumlah : {consumables[index]['jumlah']} -> {newCnt}")
        print()

        isValidCMD = False
        while not isValidCMD:
            cmd = toLower(input("Apakah data diatas sudah benar? [Y/n/c] : ")) 
            if(cmd == "y"):
                dataConsumable["data"][dbIndex]["jumlah"] = total - newCnt
                consumables[index]['jumlah'] = newCnt

                print("Data keranjang berhasil diubah.")
                isValidCMD = True
                isLocked = False
            elif(cmd == "c"):
                isValidCMD = True
                print("Aksi dibatalkan.")
                isLocked = False

            elif(cmd == "n"):
                isValidCMD = True
            else:
                print("Masukan tidak dikenali, ulangi.")

def setEngine():
    global engine
    engine = {}
    userInput = ""
    isValidInput = False
    isLocked = False

    while isLocked:
        while not isValidInput:
            print("Silahkan pilih mesin pencampur yang akan digunakan: ")
            print("1. STONE - Stone Engine")
            print("2. IRON - Iron Engine")
            print("3. GOLD - Gold Engine ")
            print("4. DIAMOND - Diamond Engine")
            
            print("Ketik C untuk membatalkan aksi ini.")
            print("Ketik DOCS untuk membaca dokumentasi dari mesin")
            userInput = (input("Silahkan masukan nama mesin (dalam kapital) : "))

            isValidInput = userInput in ["STONE","IRON","GOLD","DIAMOND","c","docs", "C", "DOCS"]
            if not isValidInput:
                print("Input tidak valid. Silahkan coba lagi.")

        if(toLower(userInput) == "docs"):
            system("cls || clear")
            print("DOKUMENTASI\n")
            print("Spesifikasi Mesin")
            print("----------------------------")
            print("1. Mesin STONE")
            print(f"   Energi : {ENGINE_CHART['STONE']['energi']} Dorapower.")
            print(f"   Waktu proses pencampuran : {ENGINE_CHART['STONE']['waktu']} detik.")
            print(f"   Range Pengali Keberuntungan : 1-{ENGINE_CHART['STONE']['maxFaktor']}")
            print()

            print("2. Mesin IRON")
            print(f"   Energi : {ENGINE_CHART['IRON']['energi']} Dorapower.")
            print(f"   Waktu proses pencampuran : {ENGINE_CHART['IRON']['waktu']} detik.")
            print(f"   Range Pengali Keberuntungan : 1-{ENGINE_CHART['IRON']['maxFaktor']}")
            print()

            print("3. Mesin GOLD")
            print(f"   Energi : {ENGINE_CHART['GOLD']['energi']} Dorapower.")
            print(f"   Waktu proses pencampuran : {ENGINE_CHART['GOLD']['waktu']} detik.")
            print(f"   Range Pengali Keberuntungan : 1-{ENGINE_CHART['GOLD']['maxFaktor']}")
            print()

            print("4. Mesin DIAMOND")
            print(f"   Energi : {ENGINE_CHART['DIAMOND']['energi']} Dorapower.")
            print(f"   Waktu proses pencampuran : {ENGINE_CHART['DIAMOND']['waktu']} detik.")
            print(f"   Range Pengali Keberuntungan : 1-{ENGINE_CHART['DIAMOND']['maxFaktor']}")
            print()

            print("5. Tanpa Mesin")
            print("   Jika mesin tidak digunakan, proses pengadukan membutuhkan waktu")
            print("   waktu selama 1 menit dan pengali keberuntungan di set ke nilai 1.")
            print()

            print("Energi")
            print("------")
            print("Dalam proses pengadukan dengan mesin, diperlukan energi.")
            print("Energi didapat dengan memasukkan item-item consumable dalam mesin.")
            print()

            print("Berikut ini adalah konversi energi dari item consumable:")
            print(f"1. Rarity C = {RARITY_CHART['C']} Dorapower")
            print(f"2. Rarity B = {RARITY_CHART['B']} Dorapower")
            print(f"3. Rarity A = {RARITY_CHART['A']} Dorapower")
            print(f"4. Rarity S = {RARITY_CHART['S']} Dorapower")
            print("")
            print("NOTE: Item consumable yang sudah dikonversi tidak bisa dikembalikan.")
            print("Walaupun energi yang digunakan masih tersisa.")
            print()
            
            input("Tekan ENTER untuk kembali.")
        elif(toLower(userInput) == "c"):
            print("Aksi dibatalkan.")
            isLocked = False
        else:
            engine["nama"] = userInput
            totalEnergy = 0

            while totalEnergy >= ENGINE_CHART[userInput]["energi"]:
                system("cls || clear")
                print("PENGISIAN ENERGI")
                print("")
                print(f"Total Energi Terkumpul : {totalEnergy} Dorapower.")
                print(f"Kebutuhan Energi : {ENGINE_CHART[userInput]['energi']} Dorapower")
                print(f"Kekurangan Energi : {ENGINE_CHART[userInput]['energi'] - totalEnergy} Dorapower")
                print()

                print("Perintah yang tersedia:")
                print("1. LIHAT - Melihat daftar consumable yang tersedia.")
                print("2. TAMBAH - Menambah Energi")
                print("3. BATAL - Membatalkan proses dan membuang semua energi yang sudah terkumpul.")
                print("")
                print("Bagian ini akan tertutup setelah energi yang diisikan sudah melebihi batas minimum.")
                
                print()
                print("Tuliskanlah perintah yang dipilih : ")
                cmd = input("Pilihan Perintah : ")

                if(toLower(cmd) == "lihat"):
                    showData(dataConsumable, "DATA CONSUMABLE")
                elif(toLower(cmd) == "tambah"):
                    index = selectIndex(dataConsumable["row_number"])
                    cnt = getCount(dataConsumable["data"][index]["jumlah"])

                    totalEnergy += RARITY_CHART[dataConsumable["data"][index]["rarity"]] * cnt
                    dataConsumable["data"][index]["jumlah"] -= cnt
                elif(toLower(cmd) == "batal"):
                    isLocked = False
                else:
                    print("ERROR! Perintah tidak dikenal, silahkan coba lagi.")
            
            # Machine Assembly
            print("Mempersiapkan Mesin...")
            sleep(1.5)
            print("Mengisikan energi pada mesin...")
            sleep(1.5)

            factor = random() * ENGINE_CHART[userInput]["maxFaktor"]

            engine = {
                "nama" : userInput,
                "faktorPengali" : factor
            }

            print("Done!")
            sleep(1)
            
            

def mix():
    pass

def eksperimen(username):
    global dataConsumable
    dataConsumable = getTable("consumable")
    
    if isValidUser(username):
        option = ""
        while (option != "mix"):
            system("cls || clear")
            print("""

██╗░░░░░░█████╗░██████╗░░█████╗░██████╗░░█████╗░████████╗░█████╗░██████╗░██╗░░░██╗
██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗╚██╗░██╔╝
██║░░░░░███████║██████╦╝██║░░██║██████╔╝███████║░░░██║░░░██║░░██║██████╔╝░╚████╔╝░
██║░░░░░██╔══██║██╔══██╗██║░░██║██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗░░╚██╔╝░░
███████╗██║░░██║██████╦╝╚█████╔╝██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
""")
            print("Halo, selamat datang di laboratorium doraemonangis.")
            print()

            print("--------------------------------------")
            print("Daftar Objek yang akan diproses")
            print("--------------------------------------")

            if(engine != {}):
                print(f"MESIN PENCAMPUR : {engine['nama']}")
            else:
                print("MESIN PENCAMPUR : TIDAK ADA")

            print()
            print("KERANJANG CONSUMABLE: ")
            if(nItem > 0):
                for i in range(nItem):
                    print(f"{i+1}. {consumables[i]['nama']}", end="")
                    print(f" - Rarity {consumables[i]['rarity']}", end="")
                    print(f" ({consumables[i]['jumlah']}x)")
            else:
                print("BELUM ADA CONSUMABLE YANG DIPILIH")
            
            print()

            print("Perintah yang tersedia: ")
            print("1. SHOW - Tampilkan Consumable")
            print("2. ADD - Tambah Consumable")
            print("3. DELETE - Hapus Data Consumable yang dipilih")
            print("4. EDIT - Edit jumlah consumable yang dipilih")
            print("5. ENGINE - Pilih mesin yang digunakan untuk mencampurkan")
            print("6. MIX - Lakukan pencampuran")

            print()

            isValid = False
            while not isValid:
                option = toLower(input("Perintah yang dipilih :"))
                print()

                if option == "show":
                    showData(dataConsumable, "DAFTAR CONSUMABLE")
                elif option == "add":
                    addItem()
                elif option == "delete":
                    deleteItem()
                    
                    