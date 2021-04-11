# Module permintaan
# modul ini berisi implementasi dari fitur
# permintaan consumable (F10)

from core.database import applyChange, getTable

def mintaConsumable(username):
    dataConsumable = getTable("consumable")
    pass