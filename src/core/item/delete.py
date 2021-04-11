# Module delete
# Modul ini berisi implementasi dari fitur
# penghapusan gadget ataupun consumable (F06)

from core.database import applyChange, getTable

def delete(username):
    dataGadget = getTable("gadget")
    dataConsumable = getTable("consumable")
    pass