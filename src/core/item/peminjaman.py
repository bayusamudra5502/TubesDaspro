# Module Pengembalian
# Modul ini berisi implementasi dari
# fitur peminjaman gadget (F08)

from core.database import applyChange, getTable
from core.auth import isUserRole

def peminjamanGadget(username):
    dataGadget = getTable("gadget")
    pass