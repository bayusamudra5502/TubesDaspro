# Module Eksperimen
# Modul ini merupakan realisasi dari fitur
# FB03, yaitu meningkatkan rarity Consumable

from core.database import getTable
from core.auth import isValidUser

def eksperimen(username):
    dataConsumable = getTable("consumable")
    pass