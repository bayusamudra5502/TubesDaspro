# Module user
# Modul ini berisi implementasi fungsi yang
# merupakan fungsi utilitas untuk user

# PUSTAKA
from core.database import getTable
from .password import isValidPassword

# KAMUS LOKAL
# type user = < 
#       id: string,
#       username: string,
#       nama: string,
#       alamat: string,
#       password: string,
#       role: string>

# type userTable = < data: Array of user,
#                   row_number: integer,
#                   col_number: integer,
#                   columnName: Array of string>

# function getObjectUser(username:string) -> user
# Fungsi ini menerima sebuah string username dan
# akan mengeluarkan objek user dengan
# nama username dan jika tidak ditemukan akan
# mengeluarkan objek kosong ({}).

# function getUserID(username:string) -> string
# Fungsi ini akan menerima sebuah string username
# dan mengeluarkan id-nya bila username ada. Bila
# tidak ada, maka akan mengaluarkan string kosong.

# function isAdminRole(username:string) -> boolean
# fungsi ini akan menerima sebuah string dan
# menghasilkan nilai True bila username memiliki role
# admin.

# function isUserRole(username:string) -> boolean
# fungsi ini akan menerima sebuah string dan
# menghasilkan nilai True bila username memiliki role
# user.

# function isValidUser(username:string) -> boolean
# fungsi ini akan menerima sebuah string dan
# menghasilkan nilai True bila username ada.

# function isUnameAvailable(username:string) -> boolean
# fungsi ini akan menerima sebuah string dan
# menghasilkan nilai True bila username belum ada di
# database.

# ALGORITMA
def getObjectUser(username):
    """Fungsi ini menerima sebuah string username dan
    akan mengeluarkan objek user dengan nama username 
    dan jika tidak ditemukan akan mengeluarkan objek 
    kosong ({}).
    """
    # KAMUS LOKAL
    # dataUser: userTable
    # objUser: user

    # ALGORITMA
    dataUser = getTable("user")
    for i in range(dataUser["row_number"]):
        objUser = dataUser["data"][i]

        if(objUser["username"] == username):
            return objUser
    
    return {}

def getUserID(username):
    """Fungsi ini akan menerima sebuah string username
    dan mengeluarkan id-nya bila username ada. Bila
    tidak ada, maka akan mengaluarkan string kosong.
    """
    # KAMUS LOKAL
    # objUser: userTable

    # ALGORITMA
    objUser = getObjectUser(username)
    if objUser != {}:
        return objUser["id"]
    else:
        return ""

def isAdminRole(username):
    """Fungsi ini akan menerima sebuah string dan
    menghasilkan nilai True bila username memiliki 
    role admin.
    """
    # KAMUS LOKAL
    # objUser: userTable

    # ALGORITMA
    if isValidUser(username):
        objUser = getObjectUser(username)
        return objUser["role"] == "admin"
    else:
        return False

def isUserRole(username):
    """Fungsi ini akan menerima sebuah string dan
    menghasilkan nilai True bila username memiliki 
    role user.
    """
    # KAMUS LOKAL
    # objUser: userTable

    # ALGORITMA
    if isValidUser(username):
        objUser = getObjectUser(username)
        return objUser["role"] == "user"
    else:
        return False

def isValidUser(username):
    """Fungsi ini akan menerima sebuah string dan
    menghasilkan nilai True bila username ada.
    """
    # KAMUS LOKAL
    # objUser: userTable

    # ALGORITMA
    objUser = getObjectUser(username)

    if(objUser == {}):
        return False
    else:
        return True

def isUnameAvailable(username):
    """Fungsi ini akan menerima sebuah string dan
    menghasilkan nilai True bila username tidak ada.
    """
    # KAMUS LOKAL

    # ALGORITMA
    return (getObjectUser(username) == {})

