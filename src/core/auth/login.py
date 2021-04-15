# Module login
# Modul ini adalah realisasi dari fitur login
# pada program ini. Pada modul ini terdiri dari
# Fungsi-fungsi yang berkaitan dengan login

from core.database import getTable
from .password import isValidPassword


def login() -> str:
    dataUser = getTable("user")
    errcode = 0

    username = input('Masukan username: ')
    password = input('Masukan password: ')

    for i in range(dataUser['row_number']):
        if (username == dataUser['data'][i]['username']) and isValidPassword(password, dataUser['data'][i]['password']):
            print('Halo', username + '!', 'Selamat datang di Kantong Ajaib.')
            return username

        elif (username == dataUser['data'][i]['username']) and (
        not isValidPassword(password, dataUser['data'][i]['password'])):
            errcode = 0
            print('Halo', username + '!', 'Password yang kamu input salah.')
            break

        else:
            errcode = 1
            continue

    if (errcode == 1):
        print('Username tidak ditemukan.')

    pass
