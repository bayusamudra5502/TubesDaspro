# Module history
# Modul ini berisi riwayat dari
# peminjaman gadget, pengambilan gadget, dan
# pengambilan consumable

from core.database import applyChange, getTable

def histPinjamGadget(username):
    # Fitur F11
    dataBorrowHist = getTable("gadget_borrow_history")
    pass

def histKembaliGadget(username):
    # Fitur F12
    dataReturnHist = getTable("gadget_return_history")
    pass

def histAmbilConsumable(username):
    # Fitur F13
    dataConsumableHist = getTable("consumable_history")
    pass