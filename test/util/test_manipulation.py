import sys
from os import path

CORE_PATH = path.join(path.dirname(path.abspath(__file__)), ".." , "..", "src")
sys.path.append(path.join(CORE_PATH, ".."))
sys.path.append(CORE_PATH)

from core.util import *

# Tulis tes dibawah ini

def a():
    print(split("ayam;den;lapeh",";"))

def test_nextID():
    assert generateNextID("AbS123") == "AbS124"
    assert generateNextID("AbS123") != "kambing-124"
    assert generateNextID("ayam-99") == "ayam-100"

def test_nextID_phase2():
    assert generateNextID("DATA001") == "DATA002"
    assert generateNextID("DATA099") == "DATA100"
    assert generateNextID("DATA999") == "DATA1000"

def test_nextID_phase3():
    assert generateNextID("a124b") == ""
    assert generateNextID("a12d4") == ""
    assert generateNextID("a1") == "a2"
    assert generateNextID("") == ""