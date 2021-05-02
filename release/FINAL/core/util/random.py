# Bayu Samudra (16520420) - 6 April 2020

# Module Random
"""Modul ini berisi fungsi  Random yang dapat
menghasilkan bilangan acak. Seed yang digunakan
adalah waktu pertama kali fungsi random dipanggil"""

# PUSTAKA
import time
from core.constant import A_COEF, C_CONST, MOD_COEF

# KAMUS
# lastValue : integer

# function random() -> real
# Fungsi ini akan menghasilkan bilangan random antara
#   0 dan 1 (inklusif)

# ALGORITMA
lastValue = -1

def random() -> float:
    """ Fungsi ini akan menghasilkan bilangan acak antara
    0 dan 1 (inklusif) """
    global lastValue

    if (lastValue == -1):
        lastValue = int(time.time() * 10 ** 4) # Seeding
    
    # Fungsi : f(n+1) = (f(n) * A + C) mod M
    lastValue = (A_COEF * lastValue + C_CONST) % MOD_COEF
    return (1/(MOD_COEF) * lastValue)
