# Module password
"""Modul ini berisi beberapa fungsi yang digunakan
dalam proses pengecekan dan pembentukan password
baru"""

# LIBRARY
from core.util import random
from core.util import hash
from core.util import intToHex
from core.util import split

# KAMUS
# type TabString : < data : array[0..MAX_ARRAY_NUM] of string,
#                Neff : integer >

# function generatePassword(password:string) -> string
#   Fungsi ini menerima sebuah string password dan
#   mengembalikan hash dari password tersebut dan 
#   dilengkapi dengan salt.

# function isValidPassword(password:string, 
#               passwordHash:string) -> boolean
#   Fungsi ini akan menerima dua buah string, yaitu
#   password dan passwordHash dan akan mengembalikan
#   True bila password memiliki passwordHash yang sama.
#   
#   passwordHash haruslah berupa saltedPassword yang
#   dihasilkan generatePassword

# ALGORITMA
def generatePassword(password:str)->str:
    """Fungsi ini menerima sebuah string password dan
    mengembalikan hash dari password tersebut dan 
    dilengkapi dengan salt."""
    
    # KAMUS LOKAL
    #   salt : integer { salt ini memiliki besar 24 bit }

    # ALGORITMA
    salt = intToHex(int(random() * (2 ** 24) + 1) % (2 ** 24))

    return salt + "." + saltedHash(password, salt)

def isValidPassword(password:str, passwordHash:str) -> bool:
    """Fungsi ini akan menerima dua buah string, yaitu
    password dan passwordHash dan akan mengembalikan
    True bila password memiliki passwordHash yang sama.
    
    passwordHash haruslah berupa saltedPassword yang
    dihasilkan generatePassword"""

    # KAMUS LOKAL
    #   splittedData : TabString
    #   salt, saltHash, inputSalted : string

    # ALGORITMA
    splittedData = split(passwordHash, ".")[0]
    salt, saltHash = splittedData[0], splittedData[1]

    inputSalted = saltedHash(password, salt)
    return saltHash == inputSalted

def saltedHash(password:str, salt:str)->str:
    """Fungsi ini akan menerima string password dan salt
    lalu akan menghitung salted hash dari kedua input
    tersebut."""
    # KAMUS LOKAL
    #   salt : integer { salt ini memiliki besar 24 bit }

    # ALGORITMA
    unsaltedHash = hash(password)
    saltedHash = hash(salt + unsaltedHash)

    return saltedHash