from pydantic import BaseModel
from typing import List,Dict

class userQuestions(BaseModel):
    nameUser:str
    questions:List[Dict[str,str]]
  