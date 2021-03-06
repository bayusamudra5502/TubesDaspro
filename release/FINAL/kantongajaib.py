# Program kantongAjaib
# Program sistem inventori kantong ajaib doraemonangis.

# LIBRARY
from core import main
from core.database import isValidDir
from sys import argv
from core.database.load import loadDatabase
from time import  sleep

# KAMUS
# argv: Array of string

# ALGORITMA
if len(argv) < 2:
    print("Tidak ada lokasi folder yang diberikan!")
    print("Gunakan: python kantongajaib.py -h untuk menampilkan bantuan")
    print()
elif argv[1] == "-h" or argv[1] == "--help":
    print("Program inventori kantong ajaib")
    print()
    print("Gunakan: python kantongajaib.py [-h] db")
    print()
    print("Argumen :")
    print("db\t\tLokasi folder database")
    print("-h --help\tMenampilkan bantuan")
    print()
    print("Gunakan hanya satu argumen")
    print()
else:
    if(isValidDir(argv[1])):
        print("Memuat database...")
        if(loadDatabase(argv[1])):
            sleep(1)
            print("\033[92mPemuatan database berhasil.\033[0m")
            sleep(.5)
            main(argv[1])
        else:
            print("\033[91mERR: Pemuatan database gagal.\033[0m")
    else:
        print("Gunakan: \033[33mpython kantongajaib.py -h\033[0m untuk menampilkan bantuan")
        print()