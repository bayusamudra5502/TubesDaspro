import sys
from os import path

CORE_PATH = path.join(path.dirname(path.abspath(__file__)), "..", "src")
sys.path.append(path.join(CORE_PATH, ".."))
sys.path.append(CORE_PATH)

from core import util

print(util.split("ayam;den;lapeh",";"))