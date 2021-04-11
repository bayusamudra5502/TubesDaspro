# Module permintaan
# modul ini berisi implementasi dari fitur
# permintaan consumable (F10)

from core.database import applyChange, getTable
from core.auth import isValidUser

def mintaConsumable(username):
    dataConsumable = getTable("consumable")
    pass