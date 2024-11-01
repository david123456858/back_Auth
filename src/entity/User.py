from typing import List
from sqlalchemy import Column,String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
#entidad que va a la base datos
class User(Base):
    __tablename__ =  'users'
    
    nameUser = Column(String, primary_key=True,index=True)
    codeMorse= Column(String,index=True)
    questions= Column(String,index=True)
    # columan que guarda la imagen
    
    