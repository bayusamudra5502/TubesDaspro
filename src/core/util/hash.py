# Module hash
# Modul ini berisi semua fungsi yang berkaitan dengan
# proses hashing string 

# PUSTAKA
from math import log2

from core.constant import HASH_LEN

# KAMUS

# function hash(str: string) -> int
# Fungsi ini akan menerima sebuah string str lalu akan
# menghitung nilai hashnya. Hash yang dihasilkan akan
# memiliki besar HASH_LEN bit (32 bit)

# function padding(num: integer) -> int
# Fungsi ini akan membuat num akan memiliki besar
# dengan kelipatan 2^HASH_LEN (dengan HASH_LEN = 32) 
# dengan cara menempelkan 1 pada bit terakhir lalu 
# menambah 0 hingga jumlah bit mencapai panjang yang 
# sesuai. Jika num sudah 32bit, maka hasil dikeluarkan

# function bitLength(num:integer) -> int
# Fungsi ini akan menghitung panjang bit dari num

def hash(str: str):
    """Fungsi ini menerima sebuah variabel string dan
    akan menghasilkan string yang merupakan nilai hash
    dari input."""
    pass

def padding(num: int):
    """Fungsi ini akan membuat num akan memiliki besar
    dengan kelipatan (HASH_LEN) bit"""
    # KAMUS
    #   isOneInserted : boolean {Penanda apakah bit 1
    #                      sudah dimasukan atau belum }

    # ALGORITMA
    isOneInserted = False
    while  (bitLength(num) < HASH_LEN 
            and bitLength(num) % HASH_LEN != 0):
        if(not isOneInserted):
            num = num * 2 + 1
            isOneInserted = True
        else:
            num *= 2
    
    return num

def bitLength(num : int):
    """Fungsi ini akan menghitung jumlah bit dari num."""
    return int(log2(num))

def strToInt(str:str):
    """Fungsi strToInt akan mengubah str menjadi integer"""
    # KAMUS
    #   sum : integer { Hasil konversi }

    # ALGORITMA
    sum = 0
    for i in range(len(str)):
        sum *= 256
        sum += ord(strToInt[i])
    
    return sum