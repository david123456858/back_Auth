from pydantic import BaseModel

class userMorse(BaseModel):
    nameUser:str
    codeMorse:str