# Module pengembalian
# Modul ini berisi implementasi dari fitur
# pengembalian gadget (F09 dan FB02)

from core.database import applyChange, getTable

def pengembalianGadget(username):
    dataGadget = getTable("gadget")
    pass