import sys
from os import path

CORE_PATH = path.join(path.dirname(path.abspath(__file__)), "..", "src")
sys.path.append(path.join(CORE_PATH, ".."))
sys.path.append(CORE_PATH)

from core.auth import password

passwd = "Pg@M%V38B42u3jCX+PjQ"
genPass = password.generatePassword("Pg@M%V38B42u3jCX+PjQ")

print(genPass)
print(password.isValidPassword(passwd, genPass)) # True
print(password.isValidPassword("Ayam Goreng Enak", genPass)) # False