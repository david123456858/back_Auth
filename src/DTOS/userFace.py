from typing import List
from pydantic import BaseModel


class userFace(BaseModel):
    nameUser: str
    imagenes: List[str]