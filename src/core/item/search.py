# Module search
# Modul ini merupakan implementasi dari fitur
# pencarian gadget berdasarkan rarity dan tahun
# ditemukannya (F03 dan F04)

from core.database import applyChange, getTable
from core.auth import isValidUser
from core.util import toUpper


def searchByRarity(username):
    # Fitur F03
    dataGadget = getTable("gadget")

    if isValidUser:
        rarityPencarian = toUpper(input('Masukan rarity {:>3s}'.format(': ')))
        found = 0

        print()
        print('Hasil pencarian {:>2s}'.format(':'))

        for i in range(int(dataGadget['row_number'])):
            if (rarityPencarian == dataGadget['data'][i]['rarity']):
                found += 1
                print()
                print('Nama {:>13s} {}'.format(':', dataGadget['data'][i]['nama']))
                print('Deskripsi {:>8s} {}'.format(':', dataGadget['data'][i]['deskripsi']))
                print('Jumlah {:>11s} {}'.format(':', dataGadget['data'][i]['jumlah']))
                print('Rarity {:>11s} {}'.format(':', dataGadget['data'][i]['rarity']))
                print('Tahun Ditemukan {:>2s} {}'.format(':', dataGadget['data'][i]['tahun_ditemukan']))

        if found == 0:
            print('Tidak ada barang dengan rarity {}.'.format(rarityPencarian))

    else:
        print('Silahkan login terlebih dahulu sebelum menjalankan program lain.')

    pass


def searchByYear(username):
    # Fitur F04
    dataGadget = getTable("gadget")

    if isValidUser(username):
        tahunPencarian = int(input('Masukan tahun {:>5s}'.format(': ')))
        kategoriPencarian = input('Masukan kategori {:>1s}'.format(': '))
        found = 0

        print()
        print('Hasil pencarian {:>2s}'.format(':'))

        for i in range(int(dataGadget['row_number'])):
            if (kategoriPencarian == '>'):
                if (int(dataGadget['data'][i]['tahun_ditemukan']) > tahunPencarian):
                    found += 1
                    print()
                    print('Nama {:>13s} {}'.format(':', dataGadget['data'][i]['nama']))
                    print('Deskripsi {:>8s} {}'.format(':', dataGadget['data'][i]['deskripsi']))
                    print('Jumlah {:>11s} {}'.format(':', dataGadget['data'][i]['jumlah']))
                    print('Rarity {:>11s} {}'.format(':', dataGadget['data'][i]['rarity']))
                    print('Tahun Ditemukan {:>2s} {}'.format(':', dataGadget['data'][i]['tahun_ditemukan']))

            elif (kategoriPencarian == '>='):
                if (int(dataGadget['data'][i]['tahun_ditemukan']) >= tahunPencarian):
                    found += 1
                    print()
                    print('Nama {:>13s} {}'.format(':', dataGadget['data'][i]['nama']))
                    print('Deskripsi {:>8s} {}'.format(':', dataGadget['data'][i]['deskripsi']))
                    print('Jumlah {:>11s} {}'.format(':', dataGadget['data'][i]['jumlah']))
                    print('Rarity {:>11s} {}'.format(':', dataGadget['data'][i]['rarity']))
                    print('Tahun Ditemukan {:>2s} {}'.format(':', dataGadget['data'][i]['tahun_ditemukan']))

            elif (kategoriPencarian == '='):
                if (int(dataGadget['data'][i]['tahun_ditemukan']) == tahunPencarian):
                    found += 1
                    print()
                    print('Nama {:>13s} {}'.format(':', dataGadget['data'][i]['nama']))
                    print('Deskripsi {:>8s} {}'.format(':', dataGadget['data'][i]['deskripsi']))
                    print('Jumlah {:>11s} {}'.format(':', dataGadget['data'][i]['jumlah']))
                    print('Rarity {:>11s} {}'.format(':', dataGadget['data'][i]['rarity']))
                    print('Tahun Ditemukan {:>2s} {}'.format(':', dataGadget['data'][i]['tahun_ditemukan']))

            elif (kategoriPencarian == '<='):
                if (int(dataGadget['data'][i]['tahun_ditemukan']) <= tahunPencarian):
                    found += 1
                    print()
                    print('Nama {:>13s} {}'.format(':', dataGadget['data'][i]['nama']))
                    print('Deskripsi {:>8s} {}'.format(':', dataGadget['data'][i]['deskripsi']))
                    print('Jumlah {:>11s} {}'.format(':', dataGadget['data'][i]['jumlah']))
                    print('Rarity {:>11s} {}'.format(':', dataGadget['data'][i]['rarity']))
                    print('Tahun Ditemukan {:>2s} {}'.format(':', dataGadget['data'][i]['tahun_ditemukan']))

            elif (kategoriPencarian == '<'):
                if (int(dataGadget['data'][i]['tahun_ditemukan']) < tahunPencarian):
                    found += 1
                    print()
                    print('Nama {:>13s} {}'.format(':', dataGadget['data'][i]['nama']))
                    print('Deskripsi {:>8s} {}'.format(':', dataGadget['data'][i]['deskripsi']))
                    print('Jumlah {:>11s} {}'.format(':', dataGadget['data'][i]['jumlah']))
                    print('Rarity {:>11s} {}'.format(':', dataGadget['data'][i]['rarity']))
                    print('Tahun Ditemukan {:>2s} {}'.format(':', dataGadget['data'][i]['tahun_ditemukan']))

            else:
                print()
                print('Masukan kategori salah.')

        if (found == 0):
            if (kategoriPencarian == '>'):
                print('Tidak ditemukan barang yang ditemukan setelah tahun {}.'.format(tahunPencarian))

            elif (kategoriPencarian == '>='):
                print('Tidak ditemukan barang yang ditemukan pada tahun {} dan setelahnya.'.format(tahunPencarian))

            elif (kategoriPencarian == '='):
                print('Tidak ditemukan barang yang ditemukan pada tahun {}.'.format(tahunPencarian))

            elif (kategoriPencarian == '<='):
                print('Tidak ditemukan barang yang ditemukan pada tahun {} dan sebelumnya.'.format(tahunPencarian))

            elif (kategoriPencarian == '<'):
                print('Tidak ditemukan barang yang ditemukan sebelum tahun {}.'.format(tahunPencarian))
        applyChange(dataGadget,"gadget")
    else:
        print('Silahkan login terlebih dahulu sebelum menjalankan program lain.')
    return isValidUser
    pass
    