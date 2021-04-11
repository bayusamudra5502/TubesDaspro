# Module login
# Modul ini adalah realisasi dari fitur login
# pada program ini. Pada modul ini terdiri dari
# Fungsi-fungsi yang berkaitan dengan login

from core.database import getTable
from .password import isValidPassword

def login() -> str:
    dataUser = getTable("user")
    pass