# Bayu Samudra (16520420) - 6 April 2020

# Module Random
# Modul ini berisi fungsi  Random yang dapat
# menghasilkan bilangan acak.

# PUSTAKA
import time
from .. import constant as const

# KAMUS
# lastValue : integer

# function random() -> real
# { Fungsi ini akan menghasilkan bilangan random antara
#   0 dan 1 (inklusif) }

# ALGORITMA
lastValue = -1

def random() -> float:
    """ Fungsi ini akan menghasilkan bilangan acak antara
    0 dan 1 (inklusif) """
    global lastValue

    if (lastValue == -1):
        lastValue = int(time.time()) # Seeding
    
    lastValue = (const.A_COEF * lastValue + const.C_CONST) % const.MOD_COEF
    return (1/(const.MOD_COEF) * lastValue)
