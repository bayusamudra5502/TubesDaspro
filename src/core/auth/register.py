# Module register
# Modul ini berisi dari realisasi fitur
# F01 - Resgister pada program ini. Pada
# Modul inni terdiri dari prosedur dan
# fungsi yang terlibat dalam proses 
# registrasi (F01)

from core.database import getTable, applyChange
from .password import generatePassword

def register(username):
    dataUser = getTable("user")
    pass