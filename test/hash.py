import sys
from os import path

CORE_PATH = path.join(path.dirname(path.abspath(__file__)), "..", "src")
sys.path.append(path.join(CORE_PATH, ".."))
sys.path.append(CORE_PATH)

from core import util

# TEST 1
print(util.bitLength(123))
print(f"{123:b}")

data = util.padding(123)
print(f"{data:b}")

# TEST 2
print()
print(util.bitLength(0xbf3d9e2a))
print(f"{0x1bf3d9e2a:b}")

data = util.padding(0xbf3d9e2a)
print(f"{data:b}")