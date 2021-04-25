# Module Add
# Modul ini berisi dari implementasi
# penambahan item (F05)


# PUSTAKA
from core.database import applyChange, getTable
from core.auth import isAdminRole
from core.util import generateNextID


# KAMUS
# function checkRarity(rarity: string) -> bool
# Fungsi ini akan menerima input rarity dalam bentuk
# string lalu akan memvalidasi apakah rarity tersebut
# valid atau tidak. Jika valid, fungsi akan menghasil
# kan True. Sebaliknya, False.

# function checkIDAvailability(ID: string) -> bool
# Fungsi ini akan menerima input ID dalam bentuk
# string lalu akan memvalidasi apakah ID tersebut
# valid atau tidak . Jika valid, fungsi akan cek
# apakah ID tersebut sudah digunakan atau belum.
# Jika belum, fungsi menghasilkan True. Sebaliknya,
# False.

# module addItem(username)
# Modul ini akan menerima input username untuk validasi
# apakah user telah login dan merupakan admin. Modul lalu
# membaca database gadget dan consumable menggunakan fungsi
# getTable lalu meminta input item ID untuk lalu divalidasi
# menggunakan fungsi checkIDAvailality. Jika valid, fungsi
# dilanjutkan dengan input beberapa keterangan item, pada
# input rarity, dipanggil fungsi checkRarity untuk memvalidasi
# input. Jika semua sudah benar, maka item baru akan ditambah
# menggunakan fungsi applyChange.


# ALGORITMA
def checkRarity(rarity: str) -> bool:
    if rarity in ['C', 'B', 'A', 'S']:
        return True

    else:
        print('Input rarity tidak valid!')
        return False


def checkIDAvailability(ID: str) -> bool:
    dataGadget = getTable("gadget")
    dataConsumable = getTable("consumable")

    # Input ID Gadget
    if (ID[0] == 'G'):
        for i in range(dataGadget['row_number']):
            if ID == dataGadget['data'][i]['id']:
                print('Gagal menambahkan item karena ID sudah ada.')
                return False

    # Input ID Consumables
    elif (ID[0] == 'C'):
        for i in range(dataConsumable['row_number']):
            if ID == dataConsumable['data'][i]['id']:
                print('Gagal menambahkan item karena ID sudah ada.')
                return False

    else:
        print('Gagal menambahkan item karena ID tidak valid.')
        return False

    return True


def addItem(username):
    dataGadget = getTable("gadget")
    dataConsumable = getTable("consumable")

    # Validasi User
    if isAdminRole(username):
        id = input('Masukan id: ').upper()

        # Validasi ID Item
        if checkIDAvailability(id):
            nama = input('Masukan nama: ')
            deskripsi = input('Masukan deskripsi: ')
            while True:
                jumlah = input('Masukan jumlah: ')

                if int(jumlah) > 0:
                    break

                else:
                    print('Jumlah tidak valid.')
            rarity = input('Masukan rarity: ').upper()

            # Validasi Rarity Item
            if checkRarity(rarity):
                # Tambah Gadget
                if (id[0] == 'G'):
                    while True:
                        tahun_ditemukan = input('Masukan tahun ditemukan: ')

                        if int(jumlah) > 0:
                            break

                        else:
                            print('Tahun tidak valid.')
                    nextIndex = dataGadget['row_number']
                    dataGadget['data'][nextIndex] = \
                        {
                            'id': id,
                            'nama': nama,
                            'deskripsi': deskripsi,
                            'jumlah': jumlah,
                            'rarity': rarity,
                            'tahun_ditemukan': tahun_ditemukan
                        }
                    print('Item telah berhasil ditambahkan ke database.')
                    applyChange(dataGadget, 'gadget')

                # Tambah Consumables
                elif (id[0] == 'C'):
                    nextIndex = dataConsumable['row_number']
                    dataConsumable['data'][nextIndex] = \
                        {
                            'id': id,
                            'nama': nama,
                            'deskripsi': deskripsi,
                            'jumlah': jumlah,
                            'rarity': rarity,
                        }
                    print('Item telah berhasil ditambahkan ke database.')
                    applyChange(dataConsumable, 'consumable')
    else:
        print('Hanya admin yang dapat melakukan fitur tambah item ini.')
    return isAdminRole
