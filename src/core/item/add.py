# Module Add
# Modul ini berisi dari implementasi
# penambahan item (F05)

from core.database import applyChange, getTable
from core.auth import isAdminRole

def addItem(username):
    dataGadget = getTable("gadget")
    dataConsumable = getTable("consumable")
    pass