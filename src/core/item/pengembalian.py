# Module pengembalian
# Modul ini berisi implementasi dari fitur
# pengembalian gadget (F09 dan FB02)

from core.database import applyChange, getTable
from core.auth import isValidUser
from core.auth import isUserRole

def pengembalianGadget(username):
    if isValidUser(username):
        if isUserRole(username):
            dataGadget = getTable("gadget")
            dataPinjamGadget = getTable("gadget_borrow_history")
            dataKembaliGadget = getTable("gadget_return_history")
            for i in range(dataPinjamGadget["row_number"]):
pass