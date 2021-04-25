# Module help
# Modul ini adalah modul yang berisi fungsi
# yang berkaitan dengan fitur help (F16)

from core.auth import isAdminRole, isValidUser
from os import system

def help(username):
    system("clear || cls")
    print("""\033[32m
          __    __   _______  __       ______   
         |  |  |  | |   ____||  |     |   _  \  
         |  |__|  | |  |__   |  |     |  |_)  | 
         |   __   | |   __|  |  |     |   ___/  
         |  |  |  | |  |____ |  `----.|  |      
         |__|  |__| |_______||_______|| _|    \033[36m v1.0 \033[0m                                              
""")
    print("===================== Kantong Ajaib ======================")
    print()
    print("== Berikut merupakan petunjuk penggunaan fitur-fitur di ==")
    print("=============== Laboratorium Doramonangis ================")
    print("""
1. Perintah "register"
   akses    : admin
   fungsi   : untuk melakukan pendaftaran user baru

2. Perintah "login"
   akses    : admin, user
   fungsi   : untuk melakukan login ke sistem

3. Perintah "carirarity"
   akses    : admin, user
   fungsi   : untuk melakukan pencarian gadget berdasarkan raritynya

4. Perintah "caritahun"
   akses    : admin, user
   fungsi   : untuk melakukan pencarian gadget berdasarkan tahun ditemukan

5. Perintah "tambahitem"
   akses    : admin
   fungsi   : untuk melakukan penambahan item 

6. Perintah "hapusitem"
   akses    : admin
   fungsi   : untuk melakukan penghapusan item

7. Perintah "ubahjumlah"
   akses    : admin
   fungsi   : untuk mengubah jumlah gadget dan consumable yang terdapat di dalam sistem

8. Perintah "pinjam"
   akses    : user
   fungsi   : untuk melakukan peminjaman gadget pada sistem

9. Perintah "kembalikan"
   akses    : user
   fungsi   : untuk melakukan pengembalian pada gadget yang telah dipinjam kepada sistem

10.Perintah "minta"
   akses    : user
   fungsi   : untuk melakukan permintaan consumable

11.Perintah "riwayatambil"
   akses    : admin
   fungsi   : untuk melihat riwayat 5 permintaan consumable terbaru yang descending tanggal

12.Perintah "riwayatpinjam"
   akses    : admin
   fungsi   : untuk melihat riwayat 5 peminjaman gadget terbaru yang descending tanggal

13.Perintah "riwayatkembali"
   akses    : admin
   fungsi   : untuk melihat riwayat 5 pengembalian gadget terbaru yang descending tanggal

14.Perintah "eksperimen"
   akses    : user
   fungsi   : untuk menggabungkan consumable menjadi consumable yang baru dengan rarity yang baru

15.Perintah "help"
   akses    : admin, user
   fungsi   : * menampilkan petunjuk dan fitur-fitur yang ada pada sistem
              * dapat diakses tanpa harus melakukan login terlebih dahulu

16.Perintah "save"
   akses    : admin, user
   fungsi   : untuk melakukan penyimpanan data
        
17.Perintah "exit"
   akses    : admin, user
   fungsi   : untuk keluar dari sistem, pilihan:
               Y/y = ya, menyimpan perubahan yang telah dilakukan pada sistem
               N/n = tidak, tidak menyimpan perubahan yang dilakukan pada sistem
               C/c = cancel, batalkan perintah exit

================= silahkan pilih salah satu menu di atas ==================
==================== lakukan login terlebih dahulu ========================
===== jika belum menjadi user maka mintalah admin untuk melakukannya ======""")
    