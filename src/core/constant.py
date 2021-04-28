# Module Constant
# Modul ini beris semua konstanta dinamis 
# yang digunakan pada Program ini

from os.path import join, abspath, dirname

# KAMUS
# constant MAX_ITEM : integer = 100
MAX_ARRAY_NUM = 10000
# constant MAX_COLUMNS : integer = 10
MAX_COLUMNS = 10

# RANDOM GENERATOR SETTINGS
# constant A_COEF : integer = 69248439517783
A_COEF = 0x3EFB28A38257
# constant MOD_COEF : integer = 2^64-1
MOD_COEF = 2**64-1
# constant C_COEF : integer = 1
C_CONST = 1

# HASH SETTINGS
# constant HASH_LEN : integer = 64
HASH_LEN = 64
# constant HASH_INIT_CONST : integer = 602759026678606591
HASH_INIT_CONST = 0x85D6E242656AAFF
# constant HASH_CONST_1 : integer = 9283
HASH_CONST_1 = 0x2443
# constant HASH_CONST_2 : integer = 19861
HASH_CONST_2 = 0x4D95
# constant HASH_ROUND : integer = 80
HASH_ROUND = 80

# DATABASE
# type DBFileArr = < array[0..N] of string, Neff: integer>

# constant DB_FILES_NAME : DBFileArr = <["consumable_history.csv", 
#               "consumable.csv",
#               "gadget_borrow_history.csv",
#               "gadget_return_history.csv",
#               "gadget.csv",
#               "user.csv"], 6>

DB_FILES_NAME = (["consumable_history.csv", 
                 "consumable.csv",
                 "gadget_borrow_history.csv",
                 "gadget_return_history.csv",
                 "gadget.csv",
                 "user.csv"], 6)

# LABORATORIUM
# type engineChartItem = <energi:integer, 
#       maxFaktor: integer, waktu: integer
# >

# type engineChart: <STONE: engineChartItem, 
#                   IRON: engineChartItem, 
#                   GOLD: engineChartItem, 
#                   DIAMOND: engineChartItem
# >

# constant ENGINE_CHART : engineChart = <
#       <10,2,30>,<50,6,20>,<100,7,5>,<110,10,10>
# >
ENGINE_CHART = {
        "STONE" : {
            "energi" : 10,
            "maxFaktor" : 2,
            "waktu" : 30
        },
        "IRON" : {
            "energi" : 50,
            "maxFaktor" : 6,
            "waktu" : 20
        },
        "GOLD" : {
            "energi" : 100,
            "maxFaktor" : 7,
            "waktu" : 5
        },
        "DIAMOND" : {
            "energi" : 110,
            "maxFaktor" : 10,
            "waktu" : 10
        },
    }
    
RARITY_CHART = {
        "C" : 5,
        "B" : 10,
        "A" : 25,
        "S" : 100
}

LAB_LOWER_DIV = 2