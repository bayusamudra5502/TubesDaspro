# Module edit
# Modul ini berisi implementasi dari
# fitur mengubah jumlah gadget atau
# consumable pada inventory (F07)

from core.database import applyChange, getTable
from core.auth import isAdminRole

def edit(username):
    dataGadget = getTable("gadget")
    dataConsumable = getTable("consumable")
    pass