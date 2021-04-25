# Module login
# Modul ini adalah realisasi dari fitur login
# pada program ini. Pada modul ini terdiri dari
# Fungsi-fungsi yang berkaitan dengan login


# PUSTAKA
from core.database import getTable
from .password import isValidPassword


# KAMUS
# module login()
# Modul ini akan menerima input username dan password
# yang kemudian divalidasi dengan data pada user.csv
# Jika pengguna berhasil login, modul akan mereturn
# username user sehingga modul-modul lain dapat
# memvalidasi role pengguna


# ALGORITMA
def login() -> str:
    dataUser = getTable("user")
    errcode = 1

    username = input('Masukan username: ')
    password = input('Masukan password: ')

    for i in range(dataUser['row_number']):
        # Login Benar
        if (username == dataUser['data'][i]['username']) and isValidPassword(password, dataUser['data'][i]['password']):
            print('Halo', username + '!', 'Selamat datang di Kantong Ajaib.')
            errcode = 0
            return username

        # Password Salah
        elif (username == dataUser['data'][i]['username']) and (
        not isValidPassword(password, dataUser['data'][i]['password'])):
            errcode = 0
            print('Halo', username + '!', 'Password yang kamu input salah.')
            continue

        # Username tidak ditemukan
        else:
            errcode = 1
            continue

    if (errcode == 1):
        print('Username tidak ditemukan.')