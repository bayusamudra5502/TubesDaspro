import sys
from os import path

CORE_PATH = path.join(path.dirname(path.abspath(__file__)), ".." , "..", "src")
sys.path.append(path.join(CORE_PATH, ".."))
sys.path.append(CORE_PATH)

from core.util import *

# Tulis tes dibawah ini

## SESI A
# TEST 1
# print(util.bitLength(123))
# print(f"{123:b}")

# data = util.padding(123)
# print(f"{data:b}")

# # TEST 2
# print()
# print(util.bitLength(0xbf3d9e2a))
# print(f"{0xbf3d9e2a:b}")

# data = util.padding(0xbf3d9e2a)
# print(f"{data:b}")

# # TEST 3
# print()
# print(util.bitLength(0x1bf3d9e2a))
# print(f"{0x1bf3d9e2a:b}")
# print(f"{util.padding(0x1bf3d9e2a):b}")

# # TEST 4
# print()
# print(util.strToInt('ayam goreng'))
# print(f"{util.strToInt('ayam goreng'):x}")
# print(f"{util.padding(util.strToInt('ayam goreng')):x}")

# Cek fungsi pengacak
# print()
# print(f"{util.fungsiPengacak(0xC300000000000000):x}")
# print(f"{util.fungsiPengacak(1):x}")
# print(f"{util.fungsiPengacak(2):x}")
# print(f"{util.fungsiPengacak(94):x}")
# print(f"{util.fungsiPengacak(95):x}")
# print(f"{util.fungsiPengacak(0xabcdef122):x}")
# print(f"{util.fungsiPengacak(0xabcdef123):x}")
# print(f"{util.fungsiPengacak(0xabcdef124):x}")

# Cek fungsi hash
print()
print(f"{intHash('a'):x}")
print(f"{intHash('b'):x}")
print(f"{intHash('c'):x}")
print(f"{intHash('ac'):x}")
print(f"{intHash('ad'):x}")
print(f"{intHash('bayv'):x}")
print(f"{intHash('bayu'):x}")
print(f"{intHash('samudra'):x}")
print(f"{intHash('Aku Anak Sehat Tubuhku Kuat Karena Ibuku Rajin Dann Cermat'):x}")
print(f"{intHash('$abc.def'):x}")
print()
print(f"{hash('$abc.defghi')}")
print(f"{hash('b')}")
print(f"{hash('$abc.def')}")