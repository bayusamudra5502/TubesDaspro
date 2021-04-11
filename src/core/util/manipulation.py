# Module Manipulation
"""Modul ini berisi fungsi-fungsi utilitas lain yang
memiliki fungsi untuk mengubah dan mengelola input 
menjadi bentuk lain yang dapat membantu pada proses
selanjutnya."""

# LIBRARY
from core.constant import MAX_ARRAY_NUM

# KAMUS
# type TabString : < data : array[0..MAX_ARRAY_NUM] of string,
#                Neff : integer >

# function intToHex(num:integer)->string
# Fungsi ini akan menerima sebuah bilangan bulat integer
# lalu akan mengeluarkan bentuk heksadesimalnya

# function split(text:string, delimeter:string) -> intToHex
# Fungsi split menerima sebuah string text
# dan char delimeter. Fungsi ini akan mengembalikan
# tuple berupa array dari data hasil pemecahan dan
# jumlah data efektif.

# function countSubString(text: string, substr: string) -> integer
# Fungsi ini akan menghitung jumlah kemunculan 
# sting substr pada string text.

# ALGORITMA

def intToHex(num:int)->str:
    """Fungsi ini menerima sebuah integer num
    dan mengeluarkan hasil heksadesimal dari num"""

    # KAMUS LOKAL
    # hexNumber : array[0..15] of character
    # result : string

    # ALGORITMA
    hexNumber = "0123456789abcdef"
    result = ""

    while (num > 0):
        result += hexNumber[num % 16]
        num //= 16
    
    return result

def split(text:str, delimeter:str) -> tuple:
    """Fungsi split menerima sebuah string text
    dan char delimeter. Fungsi ini akan mengembalikan
    tuple berupa array dari data hasil pemecahan dan
    jumlah data efektif."""

    # KAMUS LOKAL
    #   cntData, pos, i : integer
    #   data : TabString

    cntData = countSubstring(text, delimeter) + 1
    data = ["" for i in range(MAX_ARRAY_NUM)]
    pos = 0

    for i in range(len(text)):
        if(text[i] == delimeter):
            pos += 1
        else:
            data[pos] += text[i]
    
    return (data, cntData)

def countSubstring(text:str, substr:str) -> int:
    """Fungsi ini akan menghitung jumlah kemunculan
    substring substr pada text."""

    # KAMUS LOKAL
    #   state, cnt, pos : integer

    # ALGORITMA
    state = 0
    cnt = 0

    for pos in range(len(text)):
        if(text[pos] == substr[state]):
            state += 1
        else:
            state = 0
        
        if(state == len(substr)):
            cnt += 1
            state = 0
        
        pos += 1
    
    return cnt

def toLower(str:str) -> str:
    strRes = ""
    for i in range(len(str)):
        intChar = ord(str[i])

        if(65<=intChar<=90):
            intChar += 32
        
        strRes += chr(intChar)
    
    return str