# Module register
# Modul ini berisi dari realisasi fitur
# F01 - Resgister pada program ini. Pada
# Modul inni terdiri dari prosedur dan
# fungsi yang terlibat dalam proses 
# registrasi (F01)


# PUSTAKA
from core.database import getTable, applyChange
from .password import generatePassword
from .user import isAdminRole, isUnameAvailable

# KAMUS
# module register(username)
# Modul ini hanya dapat dijalankan oleh admin, maka
# diperlukan username admin untuk menjalankannya.
# Modul ini akan meminta input identitas pengguna
# beserta username dan password. Bila username belum
# ada di database, username tersebut dapat digunakan.
# Password yang diinput diencrypt menggunakan fungsi
# hashing.


# ALGORITMA
def register(username):
    dataUser = getTable("user")

    # Validasi User
    if isAdminRole(username):
        # Input Identitas
        nama = input('Masukan nama {:>6s}'.format(': '))
        user = input('Masukan username {:>2s}'.format(': '))
        password = generatePassword(input('Masukan password {:>2s}'.format(': ')))
        alamat = input('Masukan alamat {:>4s}'.format(': '))

        # Validasi Username
        if isUnameAvailable(user):
            nextIndex = dataUser['row_number']
            dataUser['data'][nextIndex] = \
                {
                    'id': 'P' + str(nextIndex + 1),
                    'username': user,
                    'nama': nama,
                    'alamat': alamat,
                    'password': password,
                    'role': 'user'
                }
            print('User', user, 'telah berhasil register ke dalam Kantong Ajaib.')

        # Username sudah digunakan
        else:
            print('Username tidak tersedia.')

    # Diakses user biasa
    else:
        print('Program ini hanya dapat diakses oleh admin.')

    applyChange(dataUser, 'user')

    pass
