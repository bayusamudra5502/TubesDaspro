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
        nama = input('Masukan nama {:>6s}'.format(': '))
        user = input('Masukan username {:>2s}'.format(': '))
        password = generatePassword(input('Masukan password {:>2s}'.format(': ')))
        alamat = input('Masukan alamat {:>4s}'.format(': '))

        if isUnameAvailable(user):
            nextIndex = dataUser['row_number']
            dataUser['data'][nextIndex] = \
                {
                    'id': 'P' + str(nextIndex),
                    'username': user,
                    'nama': nama,
                    'alamat': alamat,
                    'password': password,
                    'role': 'user'
                }
            print('User', user, 'telah berhasil register ke dalam Kantong Ajaib.')

        else:
            print('Username tidak tersedia.')

    else:
        print('Program ini hanya dapat diakses oleh admin.')

    applyChange(dataUser, 'user')

    pass
