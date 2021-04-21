# Module help
# Modul ini adalah modul yang berisi fungsi
# yang berkaitan dengan fitur help (F16)

from core.auth import isAdminRole, isValidUser

def help(username):
    print("========================== HELP ===========================")
    print("===========================================================")
    print("====================== Kantong Ajaib ======================")
    print()
    print()
    print("register      = untuk melakukan pendaftaran user baru hanya bisa dilakukan oleh admin")
    print("login         = untuk melakukan login ke sistem (admin/user)")
    print("carirarity    = untuk melakukan pencarian gadget berdasarkan raritynya(admin,user)")
    print("caritahun     = untuk melakukan pencarian gadget berdasarkan tahun ditemukan(admin,user)")
    print("tambahitem    = untuk melakukan penambahan item(admin)")
    print("hapusitem     = untuk melakukan penghapusan item(admin)")
    print("ubahjumlah    = untuk mengubah jumlah gadget dan consumable yang terdapat di dalam sistem(admin)")
    print("pinjam        = untuk melakukan peminjaman gadget yang akan menambahkan entry pada file history bila di save(user)")
    print("kembalikan    = untuk melakukan pengembalian gadget secara seutuhnya(user)")
    print("minta         = untuk meminya consumable yang tersedia(user)")
    print("riwayatpinjam = untuk melihat riwayat peminjaman gadget(admin)")
    print("riwayatkembali= untuk melihat riwayat pengembalian gadget(admin)")
    print("riwayatambil  = untuk melihat riwayat permintaan consumable(admin)")
    print("eksperimen   = untuk menggabungkan consumable menjadi consumable yang baru(user)")
    print("save          = untuk melakukan penyimpanan data yang telah diubah")
    print("help          = untuk meminta petunjuk penggunaan sistem")
    print("exit          = untuk keluar dari dalam sistem catt: Y = ya, n = no, c = cancel/batal")
    print()
    print("silahkan pilih salah satu menu di atas")
    print("lakukan login terlebih dahulu")
    print("jika belum menjadi user maka mintalah admin untuk melakukannya")
    