from pydantic import BaseModel


class userInfoType(BaseModel):
    nameUser:str
    typeAuth:str
