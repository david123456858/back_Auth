from sqlalchemy import Column, LargeBinary, String, ARRAY, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Entidad que representa la tabla 'users'
class User(Base):
    __tablename__ = 'users'
    
    nameUser = Column(String, primary_key=True, index=True)
    codeMorse = Column(String, index=True)
    questions = Column(ARRAY(JSON), index=True)
    imagenes = Column(ARRAY(LargeBinary))  # Columna que guarda la imagen



# Entidad que representa la tabla 'users_face'
class UserFace(Base):
    __tablename__ = 'users_face'
    
    nameUser = Column(String, primary_key=True, index=True)
    imagenes = Column(ARRAY(LargeBinary))  # Columna que guarda la imagen
