import sys
from os import path

CORE_PATH = path.join(path.dirname(path.abspath(__file__)), ".." , "..", "src")
sys.path.append(path.join(CORE_PATH, ".."))
sys.path.append(CORE_PATH)

from core.util import *

def test_format():
    assert isValidTanggal("01/01/2020")
    assert isValidTanggal("01/09/0001")
    assert not isValidTanggal("10/13/2020")
    assert not isValidTanggal("05-05-2002")

def test_kabisat():
    assert isValidTanggal("29/02/2000")
    assert not isValidTanggal("29/02/2001")
    assert not isValidTanggal("29/02/1900")
    assert not isValidTanggal("30/02/2003")
    assert not isValidTanggal("30/02/2000")

def test_outRange():
    assert not isValidTanggal("32/01/2000")
    assert not isValidTanggal("2020/10/13")
    assert not isValidTanggal("31/04/2000")

def test_lenTahun():
    assert not isValidTanggal("30/12/12000")
    assert not isValidTanggal("30/12/12")
    assert isValidTanggal("30/12/1200")