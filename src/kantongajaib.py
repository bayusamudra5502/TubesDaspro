# Program kantongAjaib
# Deskripsi Program

# LIBRARY
from core import main
from core.database import isValidDir
from sys import argv

# KAMUS

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
        main(argv[1])
    else:
        print("Gunakan: python kantongajaib.py -h untuk menampilkan bantuan")
        print()