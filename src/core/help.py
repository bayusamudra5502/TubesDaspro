# Module help
# Modul ini adalah modul yang berisi fungsi
# yang berkaitan dengan fitur help (F16)

from os import system

def help(username): #Fungsi utama help untuk menampilkan semua petunjuk dalam sistem
    system("clear || cls")
    print("""\033[32m
           __    __   _______  __       ______   
          |  |  |  | |   ____||  |     |   _  \  
          |  |__|  | |  |__   |  |     |  |_)  | 
          |   __   | |   __|  |  |     |   ___/  
          |  |  |  | |  |____ |  `----.|  |      
          |__|  |__| |_______||_______|| _|    \033[36m v1.0 \033[0m
    """)
    print()
    print("===================== \033[34mKantong Ajaib\033[0m ======================")
    print()
    print("== \033[34mBerikut merupakan petunjuk penggunaan fitur-fitur di\033[0m ==")
    print("=============== \033[34mLaboratorium Doramonangis\033[0m ================")
    print("""
1. \033[31mPerintah "register"\033[0m
   \033[36makses\033[0m    : admin
   \033[36mfungsi\033[0m   : untuk melakukan pendaftaran user baru

2. \033[31mPerintah "login"\033[0m
   \033[36makses\033[0m    : admin, user
   \033[36mfungsi\033[0m   : untuk melakukan login ke sistem

3. \033[31mPerintah "carirarity"\033[0m
   \033[36makses\033[0m    : admin, user
   \033[36mfungsi\033[0m    : untuk melakukan pencarian gadget berdasarkan raritynya

4. \033[31mPerintah "caritahun"\033[0m
   \033[36makses\033[0m     : admin, user
   \033[36mfungsi\033[0m    : untuk melakukan pencarian gadget berdasarkan tahun ditemukan

5. \033[31mPerintah "tambahitem"\033[0m
   \033[36makses\033[0m     : admin
   \033[36mfungsi\033[0m    : untuk melakukan penambahan item 

6. \033[31mPerintah "hapusitem"\033[0m
   \033[36makses\033[0m     : admin
   \033[36mfungsi\033[0m    : untuk melakukan penghapusan item

7. \033[31mPerintah "ubahjumlah"\033[0m
   \033[36makses\033[0m     : admin
   \033[36mfungsi\033[0m    : untuk mengubah jumlah gadget dan consumable yang terdapat di dalam sistem

8. \033[31mPerintah "pinjam"\033[0m
   \033[36makses\033[0m     : user
   \033[36mfungsi\033[0m    : untuk melakukan peminjaman gadget pada sistem

9. \033[31mPerintah "kembalikan"\033[0m
   \033[36makses\033[0m     : user
   \033[36mfungsi\033[0m    : untuk melakukan pengembalian pada gadget yang telah dipinjam kepada sistem

10.\033[31mPerintah "minta"\033[0m
   \033[36makses\033[0m     : user
   \033[36mfungsi\033[0m    : untuk melakukan permintaan consumable

11.\033[31mPerintah "riwayatambil"\033[0m
   \033[36makses\033[0m     : admin
   \033[36mfungsi\033[0m    : untuk melihat riwayat 5 permintaan consumable terbaru yang descending tanggal

12.\033[31mPerintah "riwayatpinjam"\033[0m
   \033[36makses\033[0m     : admin
   \033[36mfungsi\033[0m    : untuk melihat riwayat 5 peminjaman gadget terbaru yang descending tanggal

13.\033[31mPerintah "riwayatkembali"\033[0m
   \033[36makses\033[0m     : admin
   \033[36mfungsi\033[0m    : untuk melihat riwayat 5 pengembalian gadget terbaru yang descending tanggal

14.\033[31mPerintah "eksperimen"\033[0m
   \033[36makses\033[0m     : user
   \033[36mfungsi\033[0m    : untuk menggabungkan consumable menjadi consumable yang baru dengan rarity yang baru

15.\033[31mPerintah "help"\033[0m
   \033[36makses\033[0m     : admin, user
   \033[36mfungsi\033[0m    : * menampilkan petunjuk dan fitur-fitur yang ada pada sistem
               * dapat diakses tanpa harus melakukan login terlebih dahulu

16.\033[31mPerintah "save"\033[0m
   \033[36makses\033[0m     : admin, user
   \033[36mfungsi\033[0m    : untuk melakukan penyimpanan data

17.\033[31mPerintah "logout"\033[0m
   \033[36makses\033[0m     : admin, user
   \033[36mfungsi\033[0m    : untuk melakukan logout dari sistem dan beralih ke akun lain
        
18.\033[31mPerintah "exit"\033[0m
   \033[36makses\033[0m     : admin, user
   \033[36mfungsi\033[0m    : untuk keluar dari sistem, pilihan:
               Y/y = ya, menyimpan perubahan yang telah dilakukan pada sistem
               N/n = tidak, tidak menyimpan perubahan yang dilakukan pada sistem
               C/c = cancel, batalkan perintah exit

================= \033[34msilahkan pilih salah satu menu di atas\033[0m ==================
==================== \033[34mlakukan login terlebih dahulu\033[0m ========================
===== \033[34mjika belum menjadi user maka mintalah admin untuk melakukannya\033[0m ======""")
    