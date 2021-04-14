# Module login
# Modul ini adalah realisasi dari fitur login
# pada program ini. Pada modul ini terdiri dari
# Fungsi-fungsi yang berkaitan dengan login

from core.database import getTable
from .password import isValidPassword

def login() -> str:
    dataUser = getTable("user")

    loggedin = False

    while not loggedin:
        username = input('Masukan username: ')
        password = input('Masukan password: ')

        for i in range(len(dataUser)):
            if (username == dataUser['data'][i]['username']) and isValidPassword(password, dataUser['data'][i]['password']):
                print('Halo', username + '!', 'Selamat datang di Kantong Ajaib.')
                loggedin = True
                break

            elif (username == dataUser['data'][i]['username']) and (not isValidPassword(password, dataUser['data'][i]['password'])):
                print('Halo', username + '!', 'Password yang kamu input salah.')
                print()
                break

            else:
                print('Username tidak ditemukan.')
                print()
                break
    pass