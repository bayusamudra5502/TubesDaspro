# Module Constant
# Modul ini beris semua konstanta dinamis 
# yang digunakan pada Program ini

from os.path import join, abspath, dirname

# KAMUS
# ROOT LOCATION
ROOT_PATH = abspath(join(dirname(__file__), ".."))

# constant MAX_ITEM : integer = 100
MAX_ARRAY_NUM = 10000

# RANDOM GENERATOR SETTINGS
# constant A_COEF : integer
A_COEF = 0x3EFB28A38257
# constant MOD_COEF : integer
MOD_COEF = 2**64-1
# constant C_COEF : integer
C_CONST = 1

# HASH SETTINGS
# constant HASH_LEN : integer
HASH_LEN = 64
# constant HASH_INIT_CONST : integer
HASH_INIT_CONST = 0x85D6E242656AAFF
# constant HASH_CONST_1 : integer
HASH_CONST_1 = 0x2443
# constant HASH_CONST_2 : integer
HASH_CONST_2 = 0x4D95
# constant HASH_ROUND : integer
HASH_ROUND = 80

# DATABASE
# constant DB_FILES_NAME : array[0..5] of string
DB_FILES_NAME = (["consumable_history.csv", 
                 "consumable.csv",
                 "gadget_borrow_history.csv",
                 "gadget_return_history.csv",
                 "gadget.csv",
                 "user.csv"], 6)