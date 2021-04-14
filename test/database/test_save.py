import sys
from os import path

CORE_PATH = path.join(path.dirname(path.abspath(__file__)), ".." , "..", "src")
sys.path.append(path.join(CORE_PATH, ".."))
sys.path.append(CORE_PATH)

from core.database import *
from os.path import dirname, join, abspath

# Tulis tes dibawah ini
import hashlib

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # Source : https://www.programiz.com/python-programming/examples/hash-file

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

def test_ujiCopy():
    IRIS_PATH = "/home/bayu/Documents/TubesDaspro/test/database/Iris.csv"
    TEST_ROOT = abspath(dirname(IRIS_PATH))

    table = tableParser(readFile(IRIS_PATH))

    applyChange(table, "IrisTable")
    print(getDB())

    save(TEST_ROOT)
    assert hash_file(IRIS_PATH) == hash_file(join(TEST_ROOT, "IrisTable.csv"))
