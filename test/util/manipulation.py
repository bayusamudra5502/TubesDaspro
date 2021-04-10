import sys
from os import path

CORE_PATH = path.join(path.dirname(path.abspath(__file__)), ".." , "..", "src")
sys.path.append(path.join(CORE_PATH, ".."))
sys.path.append(CORE_PATH)

from core.util import *

# Tulis tes dibawah ini

print(split("ayam;den;lapeh",";"))