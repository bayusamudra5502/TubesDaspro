# Module pengembalian
# Modul ini berisi implementasi dari fitur
# pengembalian gadget (F09 dan FB02)

from core.database import applyChange, getTable
from core.auth import isValidUser

def pengembalianGadget(username):
    dataGadget = getTable("gadget")
    pass