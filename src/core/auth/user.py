# Module user
# Modul ini berisi implementasi fungsi yang
# merupakan fungsi utilitas untuk user

from core.database import getTable
from .password import isValidPassword

def getObjectUser(username):
    dataUser = getTable("user")
    for i in range(dataUser["row_number"]):
        objUser = dataUser["data"][i]

        if(objUser["username"] == username):
            return objUser
    
    return {}

def getUserID(username):
    objUser = getObjectUser(username)
    
    if objUser != {}:
        return objUser["id"]
    else:
        return ""

def isAdminRole(username):
    if isValidUser(username):
        objUser = getObjectUser(username)
        return objUser["role"] == "admin"
    else:
        return False

def isUserRole(username):
    if isValidUser(username):
        objUser = getObjectUser(username)
        return objUser["role"] == "user"
    else:
        return False

def isValidUser(username):
    objUser = getObjectUser(username)

    if(objUser == {}):
        print(f"User {username} tidak ditemukan.")
        return False
    else:
        return True

def isUnameAvailable(username):
    return (getObjectUser(username) == {})