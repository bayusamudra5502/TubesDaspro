# Module register
# Modul ini berisi dari realisasi fitur
# F01 - Resgister pada program ini. Pada
# Modul inni terdiri dari prosedur dan
# fungsi yang terlibat dalam proses 
# registrasi (F01)

from core.database import getTable, applyChange
from .password import generatePassword
from .user import isAdminRole, isUnameAvailable


def register(username):
    dataUser = getTable("user")

    if isAdminRole(username):
        nama = input('Masukan nama         : ')
        user = input('Masukan username     : ')
        password = input('Masukan password : ')
        alamat = input('Masukan alamat     : ')

        if isUnameAvailable(user):
            nextIndex = dataUser['row_number']
            dataUser['data'][nextIndex]['id'] = 'P' + str(nextIndex)
            dataUser['data'][nextIndex]['user'] = user
            dataUser['data'][nextIndex]['nama'] = nama
            dataUser['data'][nextIndex]['alamat'] = alamat
            dataUser['data'][nextIndex]['password'] = generatePassword(password)
            dataUser['data'][nextIndex]['role'] = 'user'
            print('User', user, 'telah berhasil register ke dalam Kantong Ajaib.')

        else:
            print('Username tidak tersedia.')

    else:
        print('Program ini hanya dapat diakses oleh admin.')

    applyChange(dataUser, 'data')

    pass
