# Module validasi
# Modul ini berisi beberapa fungsi yang berkaitan
# dengan proses validasi

# LIBRARY
from .manipulation import split

# KAMUS
# function isValidTanggal(date: str) -> bool
# fungsi ini akan memeriksa apakah date merupakan
# tanggal yang valid, yaitu memiliki format
# DD/MM/YYYY dan tahun harus >= 0

def isValidTanggal(date:str) -> bool:
    date, length = split(date, "/")
    if length == 3:
        hari = int(date[0])
        bulan = int(date[1])
        tahun = int(date[2])

        if(1 <= bulan <= 12 and tahun >= 0):
            if(bulan == 2):
                if((tahun % 4 == 0 and tahun % 100 != 0)
                    or tahun % 400 == 0):
                    # Tahun kabisat
                    return 1 <= hari <= 29
                else:
                    # BUkan tahun kabisat
                    return 1 <= hari <= 28
            elif(bulan in [1,3,5,7,8,10,12]):
                return 1 <= hari <= 31
            else:
                return 1 <= hari <= 30
        else:
            return False
    else:
        return False
