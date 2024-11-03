from src.entity.User import User
from src.DTOS.userInfoType import userInfoType

def verifyType(user:User):
    if user.imagenes:
        return userInfoType(nameUser=user.nameUser, typeAuth="Face")
    elif user.codeMorse:
        return userInfoType(nameUser=user.nameUser, typeAuth="Morse")
    else:
        return userInfoType(nameUser=user.nameUser, typeAuth="Questions")
    
    
    
    